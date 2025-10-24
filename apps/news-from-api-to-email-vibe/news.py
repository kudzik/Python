import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
from newsapi import NewsApiClient

# 1. Wczytanie zmiennych środowiskowych z pliku .env
load_dotenv()

# --- Konfiguracja (pobierana z .env) ---
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
SEARCH_PHRASE = os.getenv("SEARCH_PHRASE")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")  # adres email odbiorcy

SMTP_SERVER = os.getenv("SMTP_SERVER")  # serwer SMTP
SMTP_PORT = int(os.getenv("SMTP_PORT"))  # port SMTP
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")  # adres email nadawcy
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # Hasło do aplikacji!

# ----------------------------------------


def get_polish_news(phrase):
    """Pobiera polskie wiadomości z NewsAPI na podstawie frazy."""
    print(f"-> Rozpoczynanie wyszukiwania dla frazy: '{phrase}'...")
    try:
        # Inicjalizacja klienta NewsAPI
        newsapi = NewsApiClient(api_key=NEWS_API_KEY)

        # Pobieranie wszystkich artykułów pasujących do frazy, tylko w języku polskim
        all_articles = newsapi.get_everything(
            q=phrase,
            language="en",
            sort_by="publishedAt",  # Najnowsze
            page_size=100,  # Maksymalna liczba artykułów
        )

        articles = all_articles.get("articles", [])
        print(f"-> Znaleziono {len(articles)} artykułów.")
        return articles

    except Exception as e:
        print(f"Błąd podczas pobierania danych z NewsAPI: {e}")
        return None


def format_email_body(articles, phrase):
    """Formatuje listę artykułów do treści wiadomości e-mail w HTML."""
    if not articles:
        return "Nie znaleziono żadnych nowych wiadomości w języku polskim dla frazy '{}'.".format(
            phrase
        )

    html_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
            .article {{ border-left: 3px solid #007bff; padding-left: 10px; margin-bottom: 15px; }}
            .title {{ font-weight: bold; color: #333; }}
            .source {{ font-size: 0.9em; color: #666; }}
        </style>
    </head>
    <body>
        <h2>Wyniki wyszukiwania wiadomości dla frazy: "<strong>{phrase.capitalize()}</strong>"</h2>
        <p>Znaleziono {len(articles)} artykułów:</p>
        <hr>
    """

    for article in articles:
        title = article.get("title", "Brak tytułu")
        url = article.get("url", "#")
        source = article.get("source", {}).get("name", "Nieznane źródło")
        published = article.get("publishedAt", "Brak daty")[:10]  # Pobranie tylko daty

        html_content += f"""
        <div class="article">
            <p class="title"><a href="{url}" target="_blank">{title}</a></p>
            <p class="source">Źródło: {source} ({published})</p>
        </div>
        """

    html_content += """
    <hr>
    <p>Automatyczny raport z NewsAPI.</p>
    </body>
    </html>
    """
    return html_content


def send_email(subject, body, sender, recipient, password, smtp_server, smtp_port):
    """Wysyła wiadomość e-mail za pomocą protokołu SMTP."""
    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = recipient

        # Używamy subtypu 'html'
        msg.set_content(body, subtype="html")

        # Połączenie z serwerem SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()  # Zabezpieczenie połączenia protokołem TLS
            server.login(sender, password)
            server.send_message(msg)

        print(f"\n✅ Pomyślnie wysłano e-mail do: {recipient}")

    except Exception as e:
        print("\n❌ Błąd podczas wysyłania e-maila:")
        print(
            f"Upewnij się, że używasz 'Hasła do aplikacji' i włączony jest protokół TLS (port {smtp_port}). Błąd: {e}"
        )


def main():
    """Główna funkcja programu."""

    if not all(
        [NEWS_API_KEY, SEARCH_PHRASE, RECIPIENT_EMAIL, EMAIL_ADDRESS, EMAIL_PASSWORD]
        # [NEWS_API_KEY, SEARCH_PHRASE]
    ):
        print(
            "BŁĄD KONFIGURACJI: Upewnij się, że wszystkie zmienne w pliku .env zostały poprawnie uzupełnione."
        )
        return

    # 1. Pobranie danych
    articles = get_polish_news(SEARCH_PHRASE)

    if articles is None:
        return  # Przerwij, jeśli wystąpił błąd API

    # 2. Formatowanie wiadomości
    subject = f"Codzienny Raport Wiadomości: {SEARCH_PHRASE.capitalize()}"
    email_body = format_email_body(articles, SEARCH_PHRASE)

    # 3. Wysyłka wiadomości
    send_email(
        subject,
        email_body,
        EMAIL_ADDRESS,
        RECIPIENT_EMAIL,
        EMAIL_PASSWORD,
        SMTP_SERVER,
        SMTP_PORT,
    )


if __name__ == "__main__":
    main()

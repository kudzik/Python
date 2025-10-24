# News from API to Email

Aplikacja do automatycznego pobierania wiadomości z NewsAPI i wysyłania ich na adres email w formacie HTML.

## Opis

Ta aplikacja umożliwia:
- Pobieranie najnowszych wiadomości z NewsAPI na podstawie określonej frazy wyszukiwania
- Formatowanie wiadomości w czytelny format HTML
- Automatyczne wysyłanie sformatowanych wiadomości na określony adres email

## Funkcjonalności

- 🔍 Wyszukiwanie wiadomości według frazy
- 📧 Automatyczne wysyłanie emaili w formacie HTML
- 🎨 Czytelne formatowanie wiadomości
- 🔒 Bezpieczne połączenie SMTP z TLS
- ⚙️ Konfiguracja przez zmienne środowiskowe

## Wymagania

- Python 3.7+
- Konto NewsAPI (darmowy klucz API)
- Konto email z obsługą SMTP
- Dostęp do internetu

## Instalacja

1. Sklonuj repozytorium:
```bash
git clone <url-repozytorium>
cd news-from-api-to-email-vibe
```

2. Zainstaluj zależności:
```bash
pip install -r requirements.txt
```

3. Skonfiguruj zmienne środowiskowe (patrz sekcja Konfiguracja)

## Konfiguracja

Utwórz plik `.env` w głównym katalogu projektu i dodaj następujące zmienne:

```env
# NewsAPI Configuration
NEWS_API_KEY=twoj_klucz_api_newsapi
SEARCH_PHRASE=fraza_ktora_chcesz_wyszukiwac

# Email Configuration
RECIPIENT_EMAIL=adres@email.com
EMAIL_ADDRESS=twoj@email.com
EMAIL_PASSWORD=haslo_do_aplikacji

# SMTP Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### Uzyskiwanie klucza NewsAPI

1. Przejdź na [newsapi.org](https://newsapi.org)
2. Zarejestruj się (darmowe konto)
3. Skopiuj swój klucz API z panelu użytkownika

### Konfiguracja Gmail

1. Włącz 2FA na swoim koncie Google
2. Wygeneruj "Hasło do aplikacji" w ustawieniach bezpieczeństwa Google
3. Użyj tego hasła jako `EMAIL_PASSWORD`

## Użytkowanie

### Uruchomienie aplikacji

```bash
python news.py
```

### Automatyzacja (Linux/macOS)

Aby uruchamiać aplikację codziennie, dodaj do crontab:

```bash
# Edytuj crontab
crontab -e

# Dodaj linię (codziennie o 8:00)
0 8 * * * cd /ścieżka/do/projektu && python news.py
```

## Struktura projektu

```
news-from-api-to-email-vibe/
├── news.py              # Główny plik aplikacji
├── requirements.txt      # Zależności Python
├── .env.example         # Przykład konfiguracji
├── .env                 # Twoja konfiguracja (nie w repo)
├── .gitignore           # Pliki ignorowane przez git
└── README.md            # Ta dokumentacja
```

## Funkcje aplikacji

### `get_polish_news(phrase)`
Pobiera wiadomości z NewsAPI dla określonej frazy.

**Parametry:**
- `phrase` (str): Fraza do wyszukiwania

**Zwraca:**
- Lista artykułów lub None w przypadku błędu

### `format_email_body(articles, phrase)`
Formatuje listę artykułów do treści email w HTML.

**Parametry:**
- `articles` (list): Lista artykułów z NewsAPI
- `phrase` (str): Fraza wyszukiwania

**Zwraca:**
- HTML string z sformatowanymi artykułami

### `send_email(subject, body, sender, recipient, password, smtp_server, smtp_port)`
Wysyła email przez SMTP.

**Parametry:**
- `subject` (str): Temat wiadomości
- `body` (str): Treść wiadomości (HTML)
- `sender` (str): Adres nadawcy
- `recipient` (str): Adres odbiorcy
- `password` (str): Hasło do aplikacji
- `smtp_server` (str): Serwer SMTP
- `smtp_port` (int): Port SMTP

## Rozwiązywanie problemów

### Błąd autoryzacji NewsAPI
- Sprawdź czy klucz API jest poprawny
- Upewnij się, że masz dostęp do NewsAPI

### Błąd wysyłania email
- Sprawdź ustawienia SMTP
- Upewnij się, że używasz "Hasła do aplikacji" (nie zwykłego hasła)
- Sprawdź czy port 587 jest dostępny

### Brak wiadomości
- Sprawdź czy fraza wyszukiwania jest poprawna
- Upewnij się, że NewsAPI ma dostępne artykuły dla tej frazy

## Licencja

Ten projekt jest udostępniony na licencji MIT.

## Wsparcie

W przypadku problemów, sprawdź:
1. Czy wszystkie zmienne w `.env` są poprawnie ustawione
2. Czy masz dostęp do internetu
3. Czy klucze API są ważne

## Changelog

### v1.0.0
- Pierwsza wersja aplikacji
- Podstawowa funkcjonalność pobierania i wysyłania wiadomości
- Obsługa HTML w emailach
- Konfiguracja przez zmienne środowiskowe

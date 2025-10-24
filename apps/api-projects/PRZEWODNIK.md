# Przewodnik Użytkowania - News from API to Email

## Szybki Start

### 1. Przygotowanie środowiska

```bash
# Sklonuj repozytorium
git clone <url-repozytorium>
cd news-from-api-to-email-vibe

# Utwórz środowisko wirtualne (opcjonalnie)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# lub
venv\Scripts\activate     # Windows

# Zainstaluj zależności
pip install -r requirements.txt
```

### 2. Konfiguracja

```bash
# Skopiuj przykładową konfigurację
cp env.example .env

# Edytuj plik .env
nano .env  # lub użyj swojego edytora
```

### 3. Uruchomienie

```bash
python news.py
```

## Szczegółowa Konfiguracja

### Uzyskiwanie klucza NewsAPI

1. **Rejestracja:**
   - Przejdź na [newsapi.org](https://newsapi.org)
   - Kliknij "Get API Key"
   - Zarejestruj się (darmowe)

2. **Pobranie klucza:**
   - Po zalogowaniu skopiuj klucz API
   - Wklej do pliku `.env` jako `NEWS_API_KEY`

### Konfiguracja Gmail

1. **Włączenie 2FA:**
   - Przejdź do [myaccount.google.com](https://myaccount.google.com)
   - Bezpieczeństwo > Weryfikacja dwuetapowa
   - Włącz 2FA

2. **Generowanie hasła aplikacji:**
   - Bezpieczeństwo > Hasła do aplikacji
   - Wybierz "Poczta" i "Inne (nazwa niestandardowa)"
   - Wpisz "News App"
   - Skopiuj wygenerowane hasło

3. **Konfiguracja w .env:**
```env
EMAIL_ADDRESS=twoj@gmail.com
EMAIL_PASSWORD=wygenerowane_haslo_16_znakow
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### Konfiguracja innych dostawców email

#### Outlook/Hotmail
```env
SMTP_SERVER=smtp-mail.outlook.com
SMTP_PORT=587
```

#### Yahoo
```env
SMTP_SERVER=smtp.mail.yahoo.com
SMTP_PORT=587
```

## Przykłady Użycia

### Podstawowe uruchomienie
```bash
python news.py
```

### Automatyzacja z cron (Linux/macOS)

1. **Otwórz crontab:**
```bash
crontab -e
```

2. **Dodaj zadanie:**
```bash
# Codziennie o 8:00 rano
0 8 * * * cd /ścieżka/do/projektu && python news.py

# Co 6 godzin
0 */6 * * * cd /ścieżka/do/projektu && python news.py

# Tylko w dni robocze o 9:00
0 9 * * 1-5 cd /ścieżka/do/projektu && python news.py
```

### Automatyzacja z Task Scheduler (Windows)

1. Otwórz "Harmonogram zadań"
2. Utwórz nowe zadanie
3. Ustaw akcję: `python.exe C:\ścieżka\do\projektu\news.py`
4. Ustaw harmonogram według potrzeb

## Rozwiązywanie Problemów

### Błąd: "BŁĄD KONFIGURACJI"
**Przyczyna:** Nie wszystkie zmienne w `.env` są ustawione

**Rozwiązanie:**
```bash
# Sprawdź zawartość pliku .env
cat .env

# Upewnij się, że wszystkie zmienne są ustawione:
# NEWS_API_KEY, SEARCH_PHRASE, RECIPIENT_EMAIL, EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT
```

### Błąd: "Błąd podczas pobierania danych z NewsAPI"
**Przyczyny:**
- Nieprawidłowy klucz API
- Przekroczenie limitu zapytań
- Brak połączenia z internetem

**Rozwiązanie:**
```bash
# Sprawdź klucz API na newsapi.org
# Sprawdź połączenie internetowe
# Sprawdź czy nie przekroczyłeś limitu (1000 zapytań/dzień dla darmowego planu)
```

### Błąd: "Błąd podczas wysyłania e-maila"
**Przyczyny:**
- Nieprawidłowe hasło
- Blokada przez dostawcę email
- Nieprawidłowe ustawienia SMTP

**Rozwiązanie:**
```bash
# Dla Gmail - upewnij się, że używasz "Hasła do aplikacji"
# Sprawdź ustawienia SMTP
# Sprawdź czy 2FA jest włączone
```

### Brak wiadomości w wynikach
**Przyczyny:**
- Fraza wyszukiwania jest zbyt specyficzna
- Brak artykułów w języku angielskim dla tej frazy
- Problemy z NewsAPI

**Rozwiązanie:**
```bash
# Zmień frazę wyszukiwania na bardziej ogólną
# Sprawdź czy fraza jest w języku angielskim
# Przetestuj z inną frazą
```

## Zaawansowane Użycie

### Modyfikacja kodu

#### Zmiana języka wyszukiwania
W pliku `news.py`, linia 34:
```python
# Zmień z "en" na "pl" dla polskich wiadomości
language="pl",
```

#### Zmiana liczby artykułów
W pliku `news.py`, linia 36:
```python
# Zmień maksymalną liczbę artykułów
page_size=50,  # zamiast 100
```

#### Dodanie filtrów daty
```python
# Dodaj filtrowanie po dacie
all_articles = newsapi.get_everything(
    q=phrase,
    language="en",
    from_param="2024-01-01",  # Od daty
    to="2024-12-31",          # Do daty
    sort_by="publishedAt",
    page_size=100,
)
```

### Logowanie

Dodaj logowanie do pliku:
```python
import logging

# Na początku pliku
logging.basicConfig(
    filename='news_app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# W funkcjach
logging.info(f"Pobrano {len(articles)} artykułów")
```

## Bezpieczeństwo

### Ochrona danych
- **Nigdy nie commituj pliku `.env`** do repozytorium
- Używaj "Haseł do aplikacji" zamiast zwykłych haseł
- Regularnie rotuj klucze API

### Sprawdzanie bezpieczeństwa
```bash
# Sprawdź czy .env jest w .gitignore
grep -n "\.env" .gitignore

# Sprawdź czy nie ma .env w repozytorium
git status
```

## Monitoring i Debugowanie

### Sprawdzanie logów
```bash
# Jeśli dodałeś logowanie
tail -f news_app.log
```

### Testowanie połączenia
```python
# Dodaj do main() przed wysyłką
print(f"Testowanie połączenia z {SMTP_SERVER}:{SMTP_PORT}")
```

### Sprawdzanie limitów API
```python
# Dodaj do get_polish_news()
print(f"Pozostało zapytań: {all_articles.get('totalResults', 'N/A')}")
```

## Wsparcie

W przypadku problemów:
1. Sprawdź logi aplikacji
2. Zweryfikuj konfigurację w `.env`
3. Przetestuj połączenie internetowe
4. Sprawdź status NewsAPI
5. Zweryfikuj ustawienia email

## Changelog

### v1.0.0
- Podstawowa funkcjonalność
- Obsługa NewsAPI
- Wysyłka email HTML
- Konfiguracja przez .env

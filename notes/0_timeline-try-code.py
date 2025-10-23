# Prompt:
# Przeanalizuj i zredaguj załączony plik kodu Python.
# Moja odpowiedź powinna być ustrukturyzowana w następujący sposób:

# 1.  **Podsumowanie Materiału:** Krótko wymień główne koncepcje programistyczne (np. pętle, funkcje, list comprehensions, obsługa I/O, moduły), które kod demonstruje.
# 2.  **Zredagowany Kod z Komentarzami:** Przedstaw pełny kod z pliku, ale:
#     * Dodaj **czytelne komentarze** (w języku polskim) objaśniające działanie *każdego* bloku kodu i kluczowych linii.
#     * Grupuj tematycznie bloki kodu (np. I/O i Refaktoryzacja, List Comprehensions, Funkcje).
#     * **ZACHOWAJ** wszystkie oryginalne znaczniki komórek `# %%` w kodzie.
#     * Wskaż i popraw (lub skomentuj) wszelkie oczywiste błędy lub potencjalne problemy.


import random

# Lekcja 1: Refaktoryzacja I/O
# Połączyliśmy operacje 'input' i 'print' w jedną zwięzłą linię.
print(f"You have {input('Enter a todo:')} to do")

# Stworzyliśmy listę i od razu wypełniliśmy ją wartościami z input()
todos = [
    input("Enter a todo 1: "),
    input("Enter a todo 2: "),
    input("Enter a todo 3: "),
]

# Dodanie kolejnego elementu, co już było zwięzłe
todos.append(input("Enter a todo 4: "))

print(todos)

# %%
# Pętla for - standardowe zbieranie inputu (tutaj z range)
messages = []
for message in range(3):
    messages.append(input("Enter text"))
print(messages)


# %%
# Pętla while - kontrolowana przez 'wartownika' ("q")
messages = []
message = ""
while message != "q":
    message = input("Enter q to quit")
    messages.append(message)
print(messages)

# %%
# Pętla while - kontrolowana przez długość listy (zbieranie 5 elementów)
ten_element_list = []
while len(ten_element_list) < 5:
    ten_element_list.append(input("Enter element name"))
print(ten_element_list)


##################################


print(dir(list))  # Wyświetlenie wszystkich metod i atrybutów dla typu list
print(help(list.count))  # Wyświetlenie dokumentacji metody .count

# %%
# Użycie instrukcji match/case dla prostego menu
user_message = "Type 'add' or 'show': "

todos = []

while True:
    user_action = input(user_message)
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            # Zawsze dodaj element z kapitalizacją
            todos.append(todo.capitalize())
        case "show":
            print(todos)
        case _:  # Obsługa domyślna
            print("Nieznana akcja. Spróbuj 'add' lub 'show'.")


# %%
# Użycie instrukcji match/case z wieloma warunkami (aliasami)
country = "USA"

match country:
    case "USA" | "United States":
        print("Hello")
    case "Italy":
        print("Ciao")
    case "Germany":
        print("Hallo")
    case _:
        print("Nieznany kraj.")

# %%
# Iterowanie po tupli, użycie .capitalize (uwaga: brakuje nawiasów, więc drukujemy referencję do metody)
for item in ("sandals", "glasses", "trousers"):
    print(item.capitalize)  # Powinno być print(item.capitalize())

# %%
lista = ["A", "B", "C"]
# Znalezienie indeksu elementu po wartości
print(f"Index B: {lista.index('B')}")

# %%
# Konwersja i sumowanie elementów listy
numbers = ["10", "20"]
result = int(numbers[0]) + int(numbers[1])
print(result)

# %%
# Użycie enumerate() do iteracji po plikach z niestandardowym startem (start=1)
filenames = ["document", "report", "presentation"]

for index, file in enumerate(filenames, start=1):
    print(f"{index}-{file}.txt")


# %%
# Sortowanie listy, a następnie iteracja z enumerate
waiting_list = ["Zoe", "Alice", "Jim", "Jill"]
waiting_list.sort()
for index, name in enumerate(waiting_list, start=1):
    print(f"{index}. {name}")

# %%
# Przykład pobierania elementu z listy za pomocą indeksu z input()
menu = ["pasta", "pizza", "salad"]

# UWAGA: Wprowadzenie nieprawidłowego indeksu (spoza zakresu) spowoduje błąd IndexError.
try:
    user_choice = int(input("Enter the index of the item: "))
    message = f"You chose {menu[user_choice]}."
    print(message)
except ValueError:
    print("Wprowadź liczbę!")
except IndexError:
    print("Wybrano indeks spoza zakresu listy.")

# %%
# Prosty przykład enumerate
menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print(f"{i}.{j}")


# %%
# Rozpakowanie tupli w pętli for
buttons = [("John", "Sen", "Morro"), ("Lin", "Ajay", "Filip")]
for first, second, third in buttons:
    print(first, second, third)
# %%
# Obsługa plików za pomocą 'with open' (bezpieczny odczyt)
# Uwaga: poprawiona składnia argumentów "essay.txt, r" na "essay.txt", "r"
# Zakładając istnienie pliku 'essay.txt'
# try:
#     with open("essay.txt", "r") as file:
#         content = file.read().capitalize()
#         print(content)
# except FileNotFoundError:
#     print("Plik 'essay.txt' nie został znaleziony.")

# %%
# List comprehension - Proste przekształcenie: title()
names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)

# %%
# List comprehension - Generowanie kwadratów
numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]
print(squares)

# %%
# List comprehension - Z warunkiem: tylko kwadraty liczb parzystych
numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers if number % 2 == 0]
print(squares)

# %%
# List comprehension - Konwersja stringów na float i sumowanie
user_entries = ["10", "19.1", "20"]
user_entries = sum([float(entries) for entries in user_entries])
print(user_entries)

# %%
# Moduł random - Losowy wybór
names = ["John", "Jane", "Jim", "Jill"]
print(random.choice(names))


# %%
# Definicja funkcji sprawdzającej siłę hasła (z użyciem any() i type hinting)
def is_strong_password(password: str) -> bool:
    has_upper = any(
        char.isupper() for char in password
    )  # Czy jest choć jedna duża litera
    has_digit = any(char.isdigit() for char in password)  # Czy jest choć jedna cyfra
    is_long_enough = len(password) > 8  # Czy jest dłuższe niż 8 znaków

    return has_upper and has_digit and is_long_enough


# Przykłady użycia
print(is_strong_password("abc123"))  # False
print(is_strong_password("Abc123456"))  # True
print(is_strong_password("abcdefghij"))  # False
print(is_strong_password("A1short"))  # False


# %%
# Funkcja zwracająca szczegółowy raport siły hasła (z użyciem all())
def check_password_strength(password: str) -> dict:
    checks = {
        "has_uppercase": any(char.isupper() for char in password),
        "has_digit": any(char.isdigit() for char in password),
        "is_long_enough": len(password) > 8,
    }
    # Użycie all() do sprawdzenia, czy wszystkie warunki w słowniku są True
    checks["is_strong"] = all(checks.values())
    return checks


# Przykład użycia
result = check_password_strength("Abc123456")
for condition, passed in result.items():
    print(f"{condition}: {'✅' if passed else '❌'}")

# %%
# Proste sprawdzenie długości hasła z instrukcją if/else
passwords = "Abcgdgfgdfgfdg"

result = len(passwords) > 7

if result:
    print("Great password there!")
else:
    print("Your password is weak.")


# %%
# Obsługa błędów (try/except) podczas konwersji inputu na float
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    percentage = (value / total_value) * 100

    print(f"That is {percentage}%")

except ValueError:
    # Obsługa, gdy użytkownik nie wprowadzi liczby
    print("You need to enter a number. Run the program again.")
    exit()
except ZeroDivisionError:
    # Dodatkowa obsługa, gdy total_value = 0
    print("Total value cannot be zero.")


# %%
# List comprehension - Filtrowanie liczb większych niż 50
colors = [11, 34, 98, 43, 45, 54, 54]
res = [color for color in colors if color > 50]
print(res)

# %%
# Pętla for i list comprehension do filtrowania słabych haseł (długość < 8)
passwords = ["acasd9983k", "34aiufaac99", "98jjanf", "afjj879"]

# Wersja z pętlą for
for password in passwords:
    if len(password) < 8:
        print(password)

# Wersja z list comprehension (bardziej zwięzła)
print([password for password in passwords if len(password) < 8])


# %%
# List comprehension - Łączenie przekształceń stringów (capitalize, replace)
filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]

result = [files.capitalize().replace(".txt", "") for files in filenames]

for res in result:
    print(res)

# %%
# Funkcja do obliczania średniej, ignorująca pierwszy element listy
temperatures = ["temperature", 10, -20, -289, 100]


def get_avarage(temperatures: list) -> float:
    # Pobiera listę wartości liczbowych (pomijając pierwszy element - nazwę)
    values = temperatures[1:]
    # Konwersja na float (chociaż w tym przypadku są już int/float)
    values = [float(value) for value in values]
    # Obliczenie średniej
    avarage = sum(values) / len(values)
    return avarage


print(get_avarage(temperatures))


# %%
# Funkcja zwracająca min i max z wewnętrznie zdefiniowanej listy
def get_max() -> str:
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    return f"Max: {maximum}, Min: {minimum}"


print(get_max())


# %%
# Funkcja z type hinting i prostą konwersją jednostek
def liters_to_m3(liters: int) -> float:
    return liters / 1000


print(liters_to_m3(1000))


# %%
# Funkcja sprawdzająca siłę hasła z użyciem if/else
def strength(password: str) -> str:
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_eight = len(password) >= 8

    if has_upper and has_eight and has_digit:
        return "Strong Password"
    else:
        return "Weak Password"


# %%
# Funkcja obliczająca średnią (inna nazwa niż w poprzednich przykładach)
def foo(list_numbers: list) -> float:
    return sum(list_numbers) / len(list_numbers)


print(foo([10, 20, 30, 40]))


# %%
# Funkcja do formatowania tekstu (title, strip)
def prepare(text: str) -> str:
    text = text.title()
    text = text.strip()
    return text


print(prepare("hello    "))
# %%


# Funkcja z argumentem domyślnym (current_year)
def get_age(year_of_birth: int, current_year: int = 2025) -> int:
    return current_year - year_of_birth


print(get_age(1983))
# %%

# Funkcja licząca słowa w ciągu znaków
user_input = "Raz dwa trzy"


def get_nr_items(user_input: str) -> int:
    split_input = user_input.split(" ")  # Dzieli ciąg na listę słów
    return len(split_input)  # Zwraca liczbę słów (elementów listy)


print(get_nr_items(user_input))


# %%
# Błędna implementacja: iteruje po stringu jako po liście liter, a następnie filtruje
# Lepszym podejściem byłoby przekazanie listy słów.
def foo(text):
    # Dzieli tekst na litery, a następnie liczy długość liter, które są krótsze niż 8 (zawsze True dla pojedynczych liter)
    return [len(text) for text in text if len(text) < 8]


print(foo("Raz dwa trzy"))


# %%
# Funkcja z klasycznym if/elif/else
def water_state(temperature: float) -> str:
    if temperature <= 0:
        return "Solid"
    elif temperature < 100:  # Wystarczy < 100, ponieważ > 0 jest już niejawne
        return "Liquid"
    else:  # temperature >= 100
        return "Gas"


print(water_state(0))
print(water_state(100))
print(water_state(101))

# %%

# TODO: KOD do zredagowania

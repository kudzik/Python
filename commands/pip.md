# Pip Cheatsheet

## Pip Cheatsheet (Ściągawka)

| Polecenie                             | Komentarz                                                                                    |
| :------------------------------------ | :------------------------------------------------------------------------------------------- |
| `pip install nazwa-pakietu`           | Instaluje najnowszą wersję pakietu z PyPI.                                                   |
| `pip install nazwa-pakietu==1.2.3`    | Instaluje określoną wersję pakietu.                                                          |
| `pip install nazwa-pakietu>=1.0.0`    | Instaluje minimalną wymaganą wersję.                                                         |
| `pip install --upgrade nazwa-pakietu` | Aktualizuje istniejący pakiet do najnowszej wersji.                                          |
| `pip uninstall nazwa-pakietu`         | Odinstalowuje pakiet.                                                                        |
| `pip list`                            | Wyświetla listę wszystkich zainstalowanych pakietów.                                         |
| `pip freeze`                          | Wyświetla listę zainstalowanych pakietów w formacie odpowiednim do pliku `requirements.txt`. |
| `pip freeze > requirements.txt`       | Zapisuje listę pakietów i ich wersji do pliku. **Kluczowe dla reprodukcji środowiska\!**     |
| `pip install -r requirements.txt`     | Instaluje pakiety wymienione w pliku `requirements.txt`.                                     |
| `pip show nazwa-pakietu`              | Wyświetla szczegółowe informacje o pakiecie (np. wersja, lokalizacja, zależności).           |
| `pip check`                           | Weryfikuje, czy zainstalowane pakiety mają spełnione zależności.                             |
| `pip install -e /ścieżka/do/projektu` | Instaluje projekt lokalny w trybie edytowalnym (editable/development mode).                  |
| `pip --version`                       | Wyświetla bieżącą wersję `pip`.                                                              |

### Opcje ogólne (przydatne)

| Opcja                  | Komentarz                                                                                                      |
| :--------------------- | :------------------------------------------------------------------------------------------------------------- |
| `--no-cache-dir`       | Wyłącza buforowanie, co może być przydatne do rozwiązywania problemów.                                         |
| `--pre`                | Włącza instalację wersji przedpremierowych/deweloperskich (pre-releases).                                      |
| `--user`               | Instaluje pakiety w katalogu użytkownika, a nie systemowym (przydatne, gdy nie masz uprawnień administratora). |
| `-v` (lub `--verbose`) | Zwiększa poziom szczegółowości komunikatów.                                                                    |

### Uwaga: Zalecany sposób uruchamiania

Zaleca się uruchamianie `pip` jako modułu Pythona, aby mieć pewność, że używasz `pip` powiązanego z konkretnym interpreterem Pythona (szczególnie w środowiskach wirtualnych):

```bash
python -m pip install nazwa-pakietu
```

Lub, jeśli używasz Pythona 3 i chcesz być konkretny:

```bash
python3 -m pip install nazwa-pakietu
```

**Pamiętaj o środowiskach wirtualnych (Virtual Environments)\!** Zawsze używaj `pip` w środowisku wirtualnym, aby izolować zależności projektów.
import os
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

#   Pobieranie obrazu z Google (przykład)

# image_url = (
#     "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
# )

# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }

# response = requests.get(image_url, headers=header)

# if response.status_code == 200:
#     try:
#         with open("img/googlelogo.png", "wb") as f:
#             f.write(response.content)
#     except Exception as e:
#         print(f"Failed to save image: {e}")
# else:
#     print(f"Failed to download image: {response.status_code}")


#####################################################################################################################

# pobieranie wszystkich obrazów ze strony


def download_all_images(page_url, save_dir="img"):
    # Utwórz katalog, jeśli nie istnieje
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(page_url, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"Nie udało się pobrać strony: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    img_tags = soup.find_all("img")
    print(f"Znaleziono {len(img_tags)} obrazów.")

    for idx, img in enumerate(img_tags):
        img_url = img.get("src")
        if not img_url:
            continue

        # Obsłuż srcset, jeśli występuje
        if "," in img_url:
            img_url = img_url.split(",")[0].split()[0]

        # Absolutny URL
        full_url = urljoin(page_url, img_url)
        try:
            img_resp = requests.get(full_url, headers=headers)
            img_resp.raise_for_status()
        except Exception as e:
            print(f"[{idx + 1}] Błąd pobierania obrazu {full_url}: {e}")
            continue

        # Nazwa pliku - może nie mieć nazwy
        img_name = os.path.basename(urlparse(full_url).path)
        if not img_name:
            img_name = f"image_{idx + 1}.jpg"
        save_path = os.path.join(save_dir, img_name)
        # Jeśli plik już istnieje, dodaj sufiks
        base, ext = os.path.splitext(save_path)
        count = 1
        while os.path.exists(save_path):
            save_path = f"{base}_{count}{ext}"
            count += 1

        try:
            with open(save_path, "wb") as f:
                f.write(img_resp.content)
            print(f"[{idx + 1}] Zapisano obraz: {save_path}")
        except Exception as e:
            print(f"[{idx + 1}] Błąd zapisu obrazu {save_path}: {e}")


# Przykład użycia:
# podaj URL strony docelowej

if __name__ == "__main__":
    url = input("Podaj adres strony internetowej: ")
    download_all_images(url)

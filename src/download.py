# Скрипт для скачивания с гугл диска

import gdown
def download_from_disk(id):  
  gdown.download(f'https://drive.google.com/uc?id={id}&confirm=t', quiet=False)

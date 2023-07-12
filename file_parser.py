import sys
from pathlib import Path

JPEG_IMEGS = []
JPG_IMEGS = []
PNG_IMEGS = []
SVG_IMEGS = []
MP3_AUDIO = []
MY_OTHER = []
ARCHIVES = []

REGISTER_EXTENSION = {
    'JPEG': JPEG_IMEGS,
    'JPG': JPG_IMEGS,
    'PNG': PNG_IMEGS,
    'SVG': SVG_IMEGS,
    'MP3': MP3_AUDIO,
    'ZIP': ARCHIVES  
}

FOLDERS = []
EXTENSION = set() 
UNKNOWN = set()

def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()

def scan(folder: Path) -> None: 
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        ext = get_extension(item.name)
        fullname = folder / item.name
        if not ext:
            MY_OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSION.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                MY_OTHER.append(fullname)

if __name__ == "__main__":
    folder_to_scan = sys.argv[1]
    scan(Path(folder_to_scan))
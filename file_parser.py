import sys
from pathlib import Path

JPEG_IMG = []
JPG_IMG = []
PNG_IMG = []
SVG_IMG = []
MP3_AUDIO = []
TXT_DOCUMENTS = []
XLSX_DOCUMENTS = []
DOC_DOCUMENTS = []
AVI_VIDEO = []
MOV_VIDEO = []
MP4_VIDEO = []
MY_OTHER = []
ARCHIVES = []

REGISTER_EXTENSION = {
    "JPEG": JPEG_IMG,
    "JPG": JPG_IMG,
    "PNG": PNG_IMG,
    "SVG": SVG_IMG,
    "MP3": MP3_AUDIO,
    "TXT": TXT_DOCUMENTS,
    "XLSX": XLSX_DOCUMENTS,
    "DOC": DOC_DOCUMENTS,
    "AVI": AVI_VIDEO,
    "MOV": MOV_VIDEO,
    "MP4": MP4_VIDEO,
    "ZIP": ARCHIVES,
}

FOLDERS = []
EXTENSION = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in (
                "archives",
                "video",
                "audio",
                "documents",
                "images",
                "MY_OTHER",
            ):
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


def run():
    folder_to_scan = sys.argv[1]
    scan(Path(folder_to_scan))


if __name__ == "__main__":
    run()

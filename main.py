from pathlib import Path
import shutil
import sys
import file_parser as parser
from normalize import normalize

def handle_madia(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename))

def handle_other(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename))

def handle_archive(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(filename, folder_for_file)
    except shutil.ReadError:
        print('NOT archive')
        folder_for_file.rmdir()
    filename.unlink()

def handel_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f"Can't delete {folder}")

def main(folder: Path):
    parser.scan(folder)
    for file in parser.JPEG_IMEGS:
        handle_madia(file, folder / 'images' / 'JPEG')
    for file in parser.JPG_IMEGS:
        handle_madia(file, folder / 'images' / 'JPG')
    for file in parser.PNG_IMEGS:
        handle_madia(file, folder / 'images' / 'PNG')
    for file in parser.SVG_IMEGS:
        handle_madia(file, folder / 'images' / 'SVG')
    for file in parser.MP3_AUDIO:
        handle_madia(file, folder / 'audio' / 'PM3')

    for file in parser.MY_OTHER:
        handle_madia(file, folder / 'MY_OTHER')
    for file in parser.ARCHIVE:
        handle_madia(file, folder / 'ARCHIVE')

    for folder in parser.FOLDERS[::-1]:
        handel_folder(folder)

if __name__ == "__main__":
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        print(f"Start in folder {folder_for_scan.resolve()}")
        main(folder_for_scan.resolve())
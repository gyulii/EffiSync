import argparse
import subprocess

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument(
    '-b', '--build_location', action='store_true',
    help='Build location for the created program')

args = parser.parse_args()

#TODO: Replace the #path with the current dir and test it
subprocess.call(r"pyinstaller --noconfirm --onedir --windowed --icon #path/icon.ico --paths #path/app --add-data #path/extensions;extensions/ --add-data #path/app/app.py --distpath #path/build/")





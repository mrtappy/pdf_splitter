import PyPDF2 as pdf
from pathlib import Path
import os
import argparse 

parser = argparse.ArgumentParser(description="Save all pages from a PDF as a single PDF for easy MS Word import")
parser.add_argument("source_dir", type=str, help="path to the source PDF. The base for the path is your home directory! If the path includes blank spaces use \"...\" to wrap the path-string")

args = parser.parse_args()

path = str(Path.home()) + args.source_dir

# Variables intended for customisation
TARGET_DIRECTORY = "single_files"
SUFFIX = "_page_"
# -----------------------------------

base_file_name = path[path.rfind("/")+1:path.rfind(".")]
file_type = ".pdf"
target_path = path[:path.rfind("/")] + "/" + TARGET_DIRECTORY

input_file = pdf.PdfFileReader(str(path))

try: os.mkdir(target_path)
except:
    print("Target directory already exists")

for x in range(input_file.getNumPages()):
    print("working on page: " + str(x+1) + "/" + str(input_file.getNumPages()), end='\r')
    pdf_writer = pdf.PdfFileWriter()
    pdf_writer.addPage(input_file.getPage(x))
    with Path(target_path + "/" + base_file_name + SUFFIX + str(x+1) + file_type).open(mode="wb") as output_file:
        pdf_writer.write(output_file)

print("\nDone!")

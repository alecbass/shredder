import click
import word_shredder
import pdf_shredder
import sys
from os import listdir
from os.path import isfile, join
import parser

default = "clean_tender.docx"
modes = ["capture", "compliance"]

@click.command()
@click.option("--filename", "-f", default=default, help="Word document filename to shred")
@click.option("--mode", "-m", default="", help="Capture plan or compliance rules")
@click.option("--words", "-w", multiple=True, default=[])
def shred(filename: str, mode: str, words):
    if mode not in modes:
        print("The given modes should be one of:\n")
        for m in modes:
            print("{},".format(m), end="")
        sys.exit(1)
    if filename.endswith(".docx"):
        word_shredder.begin_shred(filename, mode, words)
    elif filename.endswith(".pdf"):
        pdf_shredder.begin_shred(filename, mode, words)

if __name__ == '__main__':
    shred()
import click
import word_shredder
import pdf_shredder
from os import listdir
from os.path import isfile, join
import parser

default = "clean_tender.docx"

@click.command()
@click.option("--filename", "-f", default=default, help="Word document filename to shred")
@click.option("--words", "-w", multiple=True)
def shred(filename: str, words):
    if filename.endswith(".docx"):
        word_shredder.begin_shred(filename, words)
    elif filename.endswith(".pdf"):
        pdf_shredder.begin_shred(filename, words)

if __name__ == '__main__':
    shred()
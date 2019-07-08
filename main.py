import click
import shredder
from os import listdir
from os.path import isfile, join
import parser

default = "clean_tender.docx"

@click.command()
@click.option("--filename", "-f", default=default, help="Word document filename to shred")
@click.option("--words", "-w", multiple=True)
def shred(filename, words):
    print(filename)
    print(" ".join(words))
    shredder.begin_shred(filename, words, False)

if __name__ == '__main__':
    shred()
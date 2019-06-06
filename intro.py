import click
import shredder
from os import listdir
from os.path import isfile, join
import parser

@click.command()
@click.option("--filename", "-f", default="docx1.docx", help="Word document filename to shred")
@click.option("--words", "-w", multiple=True)
def shred(filename, words):
    print(filename)
    print(" ".join(words))
    shredder.begin_shred(filename, words)

if __name__ == '__main__':
    shred()
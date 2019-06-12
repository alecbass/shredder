import click
import shredder
from os import listdir
from os.path import isfile, join
import parser

default = "tender_response_schedules.docx"

@click.command()
@click.option("--filename", "-f", default=default, help="Word document filename to shred")
@click.option("--words", "-w", multiple=True)
#@click.option("--addTables", "-t", default=False, help="Whether to add the text from the document's tables to the output")
def shred(filename, words):
    print(filename)
    print(" ".join(words))
    shredder.begin_shred(filename, words, False)

if __name__ == '__main__':
    shred()
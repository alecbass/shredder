import click
import shredder
from os import listdir
from os.path import isfile, join
import parser

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

@click.command()
@click.option("--filename", "-f", default="docx1.docx", help="Word document filename to shred")
@click.option("--words", "-w", multiple=True)
def words(filename, words):
    print(filename)
    print(" ".join(words))
    shredder.begin_shred(filename, words)

if __name__ == '__main__':
    words()
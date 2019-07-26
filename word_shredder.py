from docx import Document
import os
import sys
from utils import remove_duplicates_from_list

def write_sentences_to_docx(fileName: str, sentences: list):
    document = Document()
    for sentence in sentences:
        document.add_paragraph(sentence)
    document.save(fileName[:-5] + "_output.docx")

def write_sentences_to_text(fileName: str, sentences: list):
    file = open(fileName, "w")
    for sentence in sentences:
        file.write(sentence + "\n\n")
    file.close()

############### 08/07/2019 Redo

def start(document: Document, wordsToCapture: tuple):
    sentences: list = []
    # NOTE(alec): Sentences
    for para in document.paragraphs:
        for word in wordsToCapture:
            if word in para.text.lower():
                sentences.append(para.text)

    #NOTE(alec): Tables
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                for word in wordsToCapture:
                    if word in cell.text.lower():
                        sentences.append(cell.text)
    return sentences

def paragraphs_to_sentences(paragraphs: list, wordsToCapture: tuple):
    sentences = []
    for para in paragraphs:
        splitPara = para.split(".")
        for word in wordsToCapture:
            for sentence in splitPara:
                if word in sentence:
                    sentences.append(sentence)
    return sentences

######### COMPLIANCE RULES

heading_limit = 15

def is_rule_in_string(text: str, heading_point: int, subheading_point: int):
    """
    Returns true if the paragraph begins with a short or long rule i.e. "1." or "1.1" and if the rule isn't the entire paragraph
    """
    short_rule = "{}.".format(heading_point)
    long_rule = "{0}.{1}".format(heading_point, subheading_point)
    # NOTE(alec): Going (text != short_rule or text != long_rule) didn't work so I just used a length check
    return (text.startswith(short_rule) or text.startswith(long_rule)) and len(text) > 3

def read_compliance_rules(document: Document):
    rules = []
    for para in document.paragraphs:
        for i in range(heading_limit):
            for j in range(heading_limit):
                if is_rule_in_string(para.text, i, j):
                    rules.append(para.text)
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                for i in range(heading_limit):
                    for j in range(heading_limit):
                        if is_rule_in_string(cell.text, i, j):
                            rules.append(cell.text)
    rules = remove_duplicates_from_list(rules)
    write_sentences_to_text("rules.txt", rules)
    return rules

######### MAIN

def begin_shred(filename: str, mode: str, wordsToCapture: tuple):
    document = Document(filename)
    if mode == "capture":
        validSentences: list = []
        paragraphs = start(document, wordsToCapture)
        sentences = paragraphs_to_sentences(paragraphs, wordsToCapture)
        # tada
        write_sentences_to_docx(filename, sentences)
    elif mode == "compliance":
        rules = read_compliance_rules(document)
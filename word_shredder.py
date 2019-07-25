from docx import Document
import os
import sys

def write_sentences_to_docx(fileName: str, sentences: list):
    document = Document()
    for sentence in sentences:
        document.add_paragraph(sentence)
    document.save(fileName[:-5] + "_output.docx")


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

def read_compliance_rules(document: Document):
    rules = []
    for para in document.paragraphs:
        for i in range(15):
            for j in range(15):
                if "{0}.{1}".format(i, j) in para.text:
                    rules.append(para.text)
                    print(para.text)
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                for i in range(15):
                    for j in range(15):
                        if "{0}.{1}".format(i, j) in cell.text:
                            rules.append(cell.text)
                            print(cell.text)
    file = open("rules.txt", "w")
    for rule in rules:
        # TODO(alec): Change this as writing to a .txt is placeholder
        file.write(rule + "\n\n")
    file.close()
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
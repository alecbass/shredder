from docx import Document
import os
import sys

def all_text(paragraphs):
    return "\n".join(paragraphs)

def read(document):
    fullText = []
    for para in document.paragraphs:
        fullText.append(para.text)
    return fullText

def get_sentences_from_tables(document, wordsToCapture):
    validSentences = []
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    splitLowered = paragraph.text.lower().split(" ")
                    if any(word in paragraph.text for word in wordsToCapture):
                        validSentences.append(paragraph.text)
    return validSentences

def find_sentences_from_text(text: str, wordsToCapture):
    sentences = text.split(".")
    validSentences = []
    for sentence in sentences:
        splitLowered = sentence.lower().split(" ")
        if any(word in splitLowered for word in wordsToCapture):
            validSentences.append(sentence)
    return validSentences

def find_sentences_from_paragraphs(document, wordsToCapture):
    validParagraphs = []
    for paragraph in document.paragraphs:
        if (word in paragraph.text.lower() for word in wordsToCapture):
            validParagraphs.append(paragraph.text)
    return validParagraphs

def write_sentences_to_docx(fileName, sentences):
    document = Document()
    for sentence in sentences:
        document.add_paragraph(sentence)
    document.save(fileName)

def begin_shred(fileName: str, wordsToCapture: list):
    document = Document(fileName)
    validSentences = get_sentences_from_tables(document, wordsToCapture)
    validSentences.append(find_sentences_from_paragraphs(document, wordsToCapture))
    outputFileName = fileName[0: len(fileName) - 5] + "_output.docx"
    write_sentences_to_docx(outputFileName, validSentences)
    print("Wrote file to " + outputFileName)

if __name__ == "__main__":
    fileName = sys.argv[1] if (len(sys.argv) > 1 and sys.argv[1].endswith(".docx")) else "clean_tender.docx"
    wordsToCapture = sys.argv[2:] if (len(sys.argv) > 2) else ["should", "could", "with", "has"]
    
    begin_shred(fileName)
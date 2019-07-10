import PyPDF2
from docx import Document

def write_pdf(filename: str, lines: list):
    # NOTE(alec): Writing to pdfs is more complicated than I thought
    outputFilename = filename.split(".")[0] + "_output"
    if filename.endswith(".txt") or filename.endswith(".pdf"):
        outputFile = open(outputFilename + ".txt", "w")
        for line in lines:
            outputFile.write(line + "\n")
        outputFile.close()
    elif filename.endswith(".docx"):
        print("HERE")
        outputDocument = Document()
        for line in lines:
            outputDocument.add_paragraph(line)
        outputDocument.save(outputFilename + ".docx")
    # writer = PyPDF2.PdfFileWriter()
    # writer.insertBlankPage()
    # page = PyPDF2.pdf.PageObject()
    # print(page)
    # writer.insertPage(page, 0)
    # outputFile = open(originalFilename, "wb")
    # writer.write(outputFile)
    # outputFile.close()

def start(pdf, wordsToCapture: tuple):
    lines = []
    page = pdf.getPage(0)
    for line in page.extractText().split("\n"):
        for word in wordsToCapture:
            if word.lower() in line.lower():
                lines.append(line)
    return lines

def begin_shred(filename: str, wordsToCapture: tuple):
    file = open(filename, "rb")
    pdfReader = PyPDF2.PdfFileReader(file)
    lines = start(pdfReader, wordsToCapture)
    write_pdf(filename, lines)
    file.close()
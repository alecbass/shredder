import PyPDF2

def write_pdf(filename: str, lines: list):
    # NOTE(alec): Doesn't work currently
    originalFilename = filename[:-4] + "_output.pdf"
    print("writing to " + originalFilename)
    writer = PyPDF2.PdfFileWriter()
    # writer.insertBlankPage()
    page = PyPDF2.pdf.PageObject()
    print(page)
    writer.insertPage(page, 0)
    outputFile = open(originalFilename, "wb")
    writer.write(outputFile)
    outputFile.close()

def start(pdf, wordsToCapture: tuple):
    lines = []
    page = pdf.getPage(0)
    for line in page.extractText().split("\n"):
        for word in wordsToCapture:
            if word in line.lower():
                print(line)
                lines.append(line)
    return lines

def begin_shred(filename: str, wordsToCapture: tuple):
    file = open(filename, "rb")
    pdfReader = PyPDF2.PdfFileReader(file)
    lines = start(pdfReader, wordsToCapture)
    # write_pdf(filename, lines)
    file.close()
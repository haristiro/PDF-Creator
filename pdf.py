import PyPDF2 


with open('Scan_2021-11-26_13-56-48-004.pdf', 'rb') as file:
	reader = PyPDF2.PdfFileReader(file)
	page = reader.getPage(0)
	page.rotateClockwise(180)
	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)
	with open('Propustka.pdf', 'wb') as new_file:
		writer.write(new_file)

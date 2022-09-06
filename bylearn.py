from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter
from datetime import datetime

caminho = '1984.pdf'
pdf = PdfFileReader(caminho)

print(pdf)

numPDF = pdf.getNumPages()
print(numPDF)
print('#' * 60)

infoPDF = pdf.documentInfo
print(infoPDF)
print('#' * 60)

autor = pdf.documentInfo.author
titulo = pdf.documentInfo.title

#date formatting
metadados_data_criacao = pdf.documentInfo['/CreationDate']
string_data_criacao = metadados_data_criacao[2:-7]
data_criacao = datetime.strptime(string_data_criacao, '%Y%m%d%H%M%S')
formato_brl = '%d/%m/%Y %H:%M:%S'
data_criacao = data_criacao.strftime(formato_brl)

print("O título do livro é: {}".format(titulo))
print("O autor do livro é: {}".format(autor))
print("A data de criação é de: {}".format(data_criacao))
print('#' * 60)

primeira_pagina = pdf.getPage(0)
print(primeira_pagina)
primeira_pagina = primeira_pagina.extractText()
print(primeira_pagina)
print('#' * 60)

segunda_pagina = pdf.getPage(1)
print(segunda_pagina)
segunda_pagina = segunda_pagina.extractText()
print(segunda_pagina)
print('#' * 60)

terceira_pagina = pdf.getPage(2)
print(terceira_pagina)
terceira_pagina = terceira_pagina.extractText()
print(terceira_pagina)
print('#' * 60)

#Find text on pages
for num_pagina in range(pdf.getNumPages()):
    pagina = pdf.getPage(num_pagina)
    texto = pagina.extractText()
    if 'home' in texto:
        print(f"Encontrei na página: {num_pagina}")
print('#' * 60)

#sum number of pages
total_paginas = 0
for num_pagina in range(pdf.getNumPages()):
    pagina = pdf.getPage(num_pagina)
    texto = pagina.extractText()
    if 'home' in texto:
        print(f"Encontrei na página: {num_pagina}")
        total_paginas += num_pagina
print(f"A soma total é de: {total_paginas}")
print('#' * 60)

#join pdf
juntar_pdf = PdfFileMerger()
pdfs = ['dracula.pdf', '1984.pdf']
for pdf in pdfs:
    juntar_pdf.append(pdf)
with open('dracula_1984.pdf', 'wb') as pdf_junto:
    juntar_pdf.write(pdf_junto)
print('#' * 60)

#rotate pdf
pdf_dracula = 'dracula.pdf'
dracula_original = PdfFileReader(pdf_dracula)

pdf_dracula_rotacionado = PdfFileWriter()

for num_pagina in range(dracula_original.getNumPages()):
    pagina = dracula_original.getPage(num_pagina).rotateClockwise(90)
    pdf_dracula_rotacionado.addPage(pagina)
with open('dracula_rotacionado.pdf', 'wb') as pdf_rotacionado:
    pdf_dracula_rotacionado.write(pdf_rotacionado)

#separete pdf
dracula_original = PdfFileReader('dracula.pdf')
dracula_impar = PdfFileWriter()
dracula_par = PdfFileWriter()

for indice_pagina in range(dracula_original.getNumPages()):
    pagina = dracula_original.getPage(indice_pagina)

    numero_pagina_real = indice_pagina + 1

    if numero_pagina_real % 2 == 0:
        dracula_par.addPage(pagina)
    else:
        dracula_impar.addPage(pagina)

with open('dracula_par.pdf', 'wb') as pdf_par:
    dracula_par.write(pdf_par)

with open('dracula_impar.pdf', 'wb') as pdf_impar:
    dracula_impar.write(pdf_impar)

#secure files
dracula_original = PdfFileReader('dracula.pdf')
dracula_seguro = PdfFileWriter()

for indice_pagina in range(dracula_original.getNumPages()):
    pagina = dracula_original.getPage(indice_pagina)
    dracula_seguro.addPage(pagina)

dracula_seguro.encrypt(user_pwd='minhasenha123', use_128bit=True)

with open('dracula_seguro.pdf', 'wb') as pdf_seguro:
    dracula_seguro.write(pdf_seguro)

dracula_seguro = PdfFileReader('dracula_seguro.pdf')

if dracula_seguro.isEncrypted:
    dracula_seguro.decrypt('minhasenha123')

print(f'O PDF seguro tem: {dracula_seguro.getNumPages()} páginas')

#metadata
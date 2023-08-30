
import tabula
from PyPDF2 import  PdfReader, PdfWriter

def decrypt_pdf(input_path, output_path, password):
  with open(input_path, 'rb') as input_file, \
    open(output_path, 'wb') as output_file:
    # reader = PdfFileReader(input_file)
    reader = PdfReader(input_file)
    reader.decrypt(password)

    writer = PdfWriter()

    for i in range(len(reader.pages)):
        writer.add_page(reader.pages[i]) 

    writer.write(output_file)

#   df = tabula.read_pdf('decrypted.pdf', pages = 3, lattice = True)[1]
#   df.to_excel('data.xlsx')
df = tabula.read_pdf('decrypted.pdf', pages = 3, lattice = True)[1]

df.columns = df.columns.str.replace('\r', ' ')
data = df.dropna()
data.to_excel('data.xlsx')

if __name__ == '__main__':
  # example usage:
  decrypt_pdf('my_encrypted.pdf', 'decrypted.pdf', 'password')
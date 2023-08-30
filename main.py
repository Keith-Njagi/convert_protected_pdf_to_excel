import tabula
import pandas as pd
from PyPDF2 import PdfReader

# Specify the path to the password-protected PDF file
pdf_path = 'encrypted.pdf'
output_excel_path = 'decrypted.xlsx'
pdf_password = 'password'

# Open and decrypt the PDF using PyPDF2
pdf_reader = PdfReader(pdf_path)
pdf_reader.decrypt(pdf_password)

# Convert PDF to DataFrame (tabula.read_pdf() returns a list of DataFrames)
data_frames = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

# Concatenate DataFrames into a single DataFrame
combined_data = pd.concat(data_frames, ignore_index=True)

# Save the DataFrame to an Excel file
combined_data.to_excel(output_excel_path, index=False)

print("Conversion completed.")

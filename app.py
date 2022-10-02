import streamlit as st
import numpy as np
import base64
from functions import convert_pdf_to_txt_file, save_pages, convert_pdf_to_txt_pages, displayPDF
from pathlib import Path
import tempfile
from PyPDF2 import PdfFileReader, PdfFileWriter
with st.sidebar:
    st.title("PDF to Text")
    pdf_file = st.file_uploader("Load your PDF file", type="pdf")
with st.sidebar:
    number1 = st.number_input('First Page')
    number2 = st.number_input('Last Page')
    
if pdf_file:
    file_base_name = pdf_file.name.replace('.pdf', '')

    pdf = PdfFileReader(pdf_file)

    pages = np.arange(int(number1),int(number2)+1,1,int)-1
    pdfWriter = PdfFileWriter()

    for page_num in pages:
      pdfWriter.addPage(pdf.getPage(page_num))

    with open('{0}_subset.pdf'.format(file_base_name), 'wb') as f:
      pdfWriter.write(f)
      f.close()

   
# new_pdf_file = pdf_file.replace('.pdf', '')+"_subset.pdf" 


if pdf_file:
    # display document
    # print(pdf_file.name)
    # with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        # st.markdown("## Original PDF File")
        # fp = Path(tmp_file.name)
        # fp.write_bytes((file_base_name+"_subset.pdf").getvalue())
    if int(number1) and int(number2) :
      st.write(displayPDF('{0}_subset.pdf'.format(file_base_name)))
    # with st.expander("Display document"):
    #     displayPDF(pdf_file.name)

       
        
    
    # pdf to text
    # if textOutput == 'One text file (.txt)':
    text_data_f, nbPages = convert_pdf_to_txt_file(pdf_file)
    totalPages = str(nbPages)+" pages in total."
    st.info(totalPages)
    st.download_button("Download txt file", text_data_f)
    # else:
    #     text_data, nbPages = convert_pdf_to_txt_pages(pdf_file)
    #     totalPages = str(nbPages)+" pages in total."
    #     st.info(totalPages)
    #     zipPath = save_pages(text_data)
    #     # download text data    
    #     with open(zipPath, "rb") as fp:
    #         btn = st.download_button(
    #             label="Download ZIP (txt)",
    #             data=fp,
    #             file_name="pdf_to_txt.zip",
    #             mime="application/zip"
    #         )
   
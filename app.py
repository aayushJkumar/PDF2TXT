import streamlit as st
import base64
from functions import convert_pdf_to_txt_file, save_pages, convert_pdf_to_txt_pages, displayPDF
from pathlib import Path
import tempfile
with st.sidebar:
    st.title("PDF to Text")
    pdf_file = st.file_uploader("Load your PDF file", type="pdf")
    # print(pdf_file.name)
    # number1 = st.number_input('First Page')
    # number2 = st.number_input('Last Page')
    # values = st.slider('Select a range of pages',0.0,500.0,(number1,number2))
# st.write('Values:', values)
 
   
    


if pdf_file:
    # display document
    # print(pdf_file.name)
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        st.markdown("## Original PDF File")
        fp = Path(tmp_file.name)
        fp.write_bytes(pdf_file.getvalue())
        st.write(displayPDF(tmp_file.name))
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
   
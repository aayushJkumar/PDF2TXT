import streamlit as st
from functions import convert_pdf_to_txt_file, save_pages, convert_pdf_to_txt_pages





with st.sidebar:
    st.title("PDF to Text")
    pdf_file = st.file_uploader("Load your PDF file", type="pdf")
    


if pdf_file:
    # display document
    # with st.expander("Display document"):
    #     displayPDF(pdf_file)
    
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
    

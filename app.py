import streamlit as st
import os
import numpy as np
import base64
from functions import convertPdfToTxtFile, save_pages, convert_pdf_to_txt_pages, displayPDF, OcrScannedPdf
from pathlib import Path
import tempfile
from PyPDF2 import PdfFileReader, PdfFileWriter
def main():
    with st.sidebar:
        st.title("PDF to Text")
        pdf_file = st.file_uploader("Load your PDF file", type="pdf")
    with st.sidebar:
        number1 = st.number_input('First Page', min_value=0, step=1)
        number2 = st.number_input('Last Page', min_value=0, step=1)

    if pdf_file and (int(number1) and int(number2)):
        file_base_name = pdf_file.name.replace('.pdf', '')

        pdf = PdfFileReader(pdf_file)

        pages = np.arange(int(number1), int(number2)+1, 1, int)-1
        pdfWriter = PdfFileWriter()

        for page_num in pages:
            pdfWriter.addPage(pdf.getPage(page_num))

        with open('{0}_subset.pdf'.format(file_base_name), 'wb') as f:
            pdfWriter.write(f)
            f.close()
        # path=open('{0}_subset.pdf'.format(file_base_name), 'rb')
        OcrScannedPdf('{0}_subset.pdf'.format(file_base_name),
                    '{0}_subset_scanned.pdf'.format(file_base_name))
        path = open('{0}_subset_scanned.pdf'.format(file_base_name), 'rb')
        text_data_f, nbPages = convertPdfToTxtFile(path)
        totalPages = str(nbPages)+" pages in total."
        # st.info(totalPages)
        st.markdown("## Overview Of The PDF File")
        st.info(totalPages)
        st.write(displayPDF('{0}_subset.pdf'.format(file_base_name)))
        # text_data_f, nbPages = convert_pdf_to_txt_file(path)
        # os.remove('C:/Users/Aayush/Workspace/Internship_ISB_IIDS/pdf-text-data-extractor-main/pdf2txt/'+'{0}_subset.pdf'.format(file_base_name))#2_Changing_cost_of_crop_production_Srivastava_et_al_subset.pdf
        # totalPages = str(nbPages)+" pages in total."
        # st.info(totalPages)
        st.download_button("Download", text_data_f,
                        file_name='{0}.txt'.format(file_base_name))


    # new_pdf_file = pdf_file.replace('.pdf', '')+"_subset.pdf"


    # if pdf_file and (int(number1) and int(number2)):
        # display document
        # print(pdf_file.name)
        # with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        # st.markdown("## Original PDF File")
        # fp = Path(tmp_file.name)
        # fp.write_bytes((file_base_name+"_subset.pdf").getvalue())

        # st.write(displayPDF('{0}_subset.pdf'.format(file_base_name)))
        # with st.expander("Display document"):
        #     displayPDF(pdf_file.name)


    # if pdf_file and (int(number1)==0 or int(number2)==0):
    #   with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
    #         st.markdown("## Original PDF File")
    #         fp = Path(tmp_file.name)
    #         fp.write_bytes(pdf_file.getvalue())
    #         st.write(displayPDF(tmp_file.name))


    #     # pdf to text
    #     # if textOutput == 'One text file (.txt)':
    #     text_data_f, nbPages = convert_pdf_to_txt_file(pdf_file)
    #     totalPages = str(nbPages)+" pages in total."
    #     st.info(totalPages)
    #     st.download_button("Download txt file", text_data_f)
    #     # else:
    #     #     text_data, nbPages = convert_pdf_to_txt_pages(pdf_file)
    #     #     totalPages = str(nbPages)+" pages in total."
    #     #     st.info(totalPages)
    #     #     zipPath = save_pages(text_data)
    #     #     # download text data
    #     #     with open(zipPath, "rb") as fp:
    #     #         btn = st.download_button(
    #     #             label="Download ZIP (txt)",
    #     #             data=fp,
    #     #             file_name="pdf_to_txt.zip",
    #     #             mime="application/zip"
    #     #         )


if __name__ == '__main__':
    main()
from pypdf import PdfWriter
from methods import getFilesInDir

def merge_pdfs(pdf_list, output_filename):
    """
    Merges a list of PDF files into a single output file.

    Args:
        pdf_list (list): A list of file paths for the input PDFs.
        output_filename (str): The filename for the merged PDF output.
    """
    merger = PdfWriter()

    for pdf in pdf_list:
        if '.pdf' in pdf:
            merger.append(pdf) # Appends the entire PDF file

    merger.write(output_filename)
    merger.close() # Important to close files in a timely manner

if __name__ == "__main__":
    # Example usage:
    pdfs_to_merge = getFilesInDir('./0.Tools/rawPDFs')
    output_name = "result.pdf"
    merge_pdfs(pdfs_to_merge, output_name)
    print(f"Successfully merged {pdfs_to_merge} into {output_name}")

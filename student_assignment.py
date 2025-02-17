from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter,RecursiveCharacterTextSplitter

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"

def hw02_1(pdf):
    # Load the PDF file
    pdf_loader = PyPDFLoader(pdf)
    documents = pdf_loader.load()

    # Use CharacterTextSplitter to split the document by pages
    text_splitter = CharacterTextSplitter(separator='\f', chunk_size=1000, chunk_overlap=0)
    #chunks_by_pages = text_splitter.split_text(document_text)
    last_document = text_splitter.split_documents(documents)

    return last_document[-1]

def hw02_2(pdf):
    # Load the PDF file
    pdf_loader = PyPDFLoader(file_path=pdf)
    documents = pdf_loader.load()

    # Combine the document text into a single string
    document_text = "\n".join([doc.page_content for doc in documents])

    # Use RecursiveCharacterTextSplitter to split the document by pages
    recursive_splitter = RecursiveCharacterTextSplitter(
        separators=[
            r"第\s+[一二三四五六七八九十]+\s+章",
            r"第\s+[\d-]+\s+條"
        ],
        chunk_size=0,
        chunk_overlap=0,
        is_separator_regex = True)
    chunks_by_pages_recursive = recursive_splitter.split_text(document_text)

    return len(chunks_by_pages_recursive)
    documents = pdf_loader.load()

    # Combine the document text into a single string
    document_text = "\n".join([doc.page_content for doc in documents])

    # Use RecursiveCharacterTextSplitter to split the document by pages
    recursive_splitter = RecursiveCharacterTextSplitter(
        separators=[
            r"第\s+[一二三四五六七八九十]+\s+章",
            r"第\s+[0-9]+(?:-[0-9]+)?\s+條"
        ],
        chunk_size=0,
        chunk_overlap=0,
        is_separator_regex = True)
    chunks_by_pages_recursive = recursive_splitter.split_text(document_text)

    return len(chunks_by_pages_recursive)

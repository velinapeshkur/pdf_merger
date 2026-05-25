from pypdf import PdfWriter
from pathlib import Path
from itertools import batched


def batch_files(folder_path: str, files_per_file: int) -> list[tuple[str]]:
    folder = Path(folder_path)
    files = []
    
    for item in sorted(folder.iterdir()):
        if item.name.endswith(".pdf"):
            files.append(item.name)
    
    files_for_merge = list(batched(files, files_per_file))
    return files_for_merge    


def create_folder_for_merged_files(folder_path: str) -> Path:
    original_folder = Path(folder_path)
    new_folder = Path(f"{original_folder.parent}/merged/")
    new_folder.mkdir(parents=True, exist_ok=True)
    return new_folder
    

def merge_pdf(folder_path: str, files_per_file: int) -> None: 
    files_for_merge = batch_files(folder_path, files_per_file)
    new_folder = create_folder_for_merged_files(folder_path)

    # Merge each row of files to a new PDF file
    for row in files_for_merge:
        merger = PdfWriter()
        pdf_name = f"{row[0][:5]} - {row[-1][:5]}" # Merged file name, can be customized
        
        for pdf in row:
            merger.append(f"{folder_path}/{pdf}")
        
        with open(f"{new_folder.resolve()}/{pdf_name}.pdf", "wb") as f:
            merger.write(f)

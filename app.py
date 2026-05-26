import platform
import subprocess
from pypdf import PdfWriter
from pathlib import Path
from itertools import batched


def batch_files(folder_path: str, files_per_file: int) -> list[tuple]:
    folder = Path(folder_path)
    files = []
    
    for item in sorted(folder.iterdir()):
        if item.name.endswith(".pdf"):
            files.append(item.name)
    
    files_for_merge = list(batched(files, files_per_file))

    return files_for_merge


def create_output_dir(folder_path: str) -> Path:
    input_dir = Path(folder_path)
    output_dir = Path(f"{input_dir.parent}/merged/")
    
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir
    
    else:
        counter = 1
        
        while True:
            output_dir = Path(f"{input_dir.parent}/merged ({counter})/")

            if not output_dir.exists():
                output_dir.mkdir(parents=True, exist_ok=True)
                return output_dir
            counter += 1


def open_output_dir(output_dir):
    match platform.system():
        case "Windows":
            subprocess.run(["explorer", output_dir])
        case "Darwin": # macOS
            subprocess.run(["open", output_dir])
        case _: # Linux
            subprocess.run(["xdg-open", output_dir])
    

def merge_pdf(folder_path: str, files_per_file: str) -> dict:
    try:
        files_per_file = int(files_per_file) 
        files_for_merge = batch_files(folder_path, files_per_file)    
        
        if not files_for_merge:
            return {"success": False, "error": "No PDF files to merge."}

        output_dir = create_output_dir(folder_path)
        
        # Merge each row of files to a new PDF file
        for index, row in enumerate(files_for_merge):
            merger = PdfWriter()
            
            for pdf in row:
                merger.append(Path(folder_path) / pdf)
            
            with open(f"{output_dir.resolve()}/{index + 1}.pdf", "wb") as f:
                merger.write(f)
        
        open_output_dir(output_dir)

        return {"success": True}

    except ValueError:
        return {"success": False, "error": "Please enter a valid number."}

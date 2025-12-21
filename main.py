from tools import OCRProcessor, MarkItDownProcessor
from pathlib import Path
from dotenv import load_dotenv
import os


load_dotenv()

input_dir = Path(os.getenv("INPUT_DIR", "./test"))

if not input_dir.exists():
    raise FileNotFoundError(f"Input directory not found: {input_dir}")


output_dir = Path(os.getenv("OUTPUT_DIR", "./res"))
output_dir.mkdir(exist_ok=True)

ocr_extensions = {".pdf", ".jpeg", ".jpg", ".png"}
mid_extensions = {".docx", ".pptx", ".xls", ".xlsx"}


ocr_processor = OCRProcessor(
    cache_folder="./cache",
    no_image=True,
    no_table=False,
    delete_cache=True,
)

mid_processor = MarkItDownProcessor(enable_plugins=False)


for file_path in input_dir.iterdir():
    try:
        if file_path.suffix.lower() in ocr_extensions:
            print(f"Processing with OCR: {file_path}")
            output = ocr_processor.process(input_path=str(file_path))
            if output and Path(output).exists():
                dest = output_dir / Path(output).name
                Path(output).rename(dest)
                print(f"Moved output to: {dest}")
            else:
                print(f"Warning: OCR produced no output for {file_path}")

        elif file_path.suffix.lower() in mid_extensions:
            print(f"Processing with MarkItDown: {file_path}")
            output = mid_processor.process(str(file_path))
            if output and Path(output).exists():
                dest = output_dir / Path(output).name
                Path(output).rename(dest)
                print(f"Moved output to: {dest}")
            else:
                print(f"Warning: MarkItDown produced no output for {file_path}")

        else:
            print(f"Skipped unsupported file: {file_path}")

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        continue

print("All files processed.")

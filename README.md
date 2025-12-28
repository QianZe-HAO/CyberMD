# CyberMD

CyberMD (aka. Cyber Markdown) is a flexible tool for converting various document formats into clean Markdown, supporting both OCR-based extraction (for PDFs and images) and direct conversion (for DOCX, PPTX, XLSX). The project includes a Streamlit web interface for interactive use and a CLI script for batch processing.

## Features

- **Multi-format Support**: Convert PDF, JPG, PNG, DOCX, PPTX, XLS, XLSX to Markdown.
- **OCR Processing**: Extract text and structure from scanned documents and images using `Rednote DotsOCR`.
- **Direct Conversion**: Use `MarkItDown` for accurate conversion of Office files without OCR overhead.
- **Web Interface**: Interactive UI with file upload, progress tracking, and download capability.
- **CLI Mode**: Batch process files from an input directory using environment configuration.
- **Caching & Cleanup**: Temporary file management with cache control and cleanup functionality.

## Supported File Types

| Type       | Extensions                     | Processor     |
|------------|--------------------------------|---------------|
| OCR Input  | `.pdf`, `.jpg`, `.jpeg`, `.png` | OCRProcessor  |
| Office     | `.docx`, `.pptx`, `.xls`, `.xlsx` | MarkItDownProcessor |

## Quick Start

### 1. Installation (via `uv`)

```bash
uv sync --python 3.12
```

Clone or set up the project with the following structure:

```
project-root/
├── main.py
├── cli.py
├── tools.py
├── input/
├── output/
├── cache/
├── .env (optional)
```

### 2. Run the Web App

Launch the Streamlit interface:

```bash
uv run streamlit run main.py
```

Upload a document, click "Start Processing", and download the resulting Markdown.

### 3. Use CLI for Batch Processing

Place files in the `input/` directory and run:

```bash
uv run cli.py
```

Processed Markdown files will appear in the `output/` directory.

> **Note**: You can customize input/output paths via `.env` file (see Configuration).

## Configuration

Create a `.env` file to override default settings:

```env
INPUT_DIR=./input
OUTPUT_DIR=./output
```

In `main.py`, you can also adjust these global settings:

```python
NO_IMAGE = True      # Skip image output in OCR
NO_TABEL = False     # Enable table extraction in OCR
```

## Processors

### OCRProcessor
Handles scanned documents and images using OCR. Outputs structured Markdown with layout preservation.

### MarkItDownProcessor
Converts Office files directly to Markdown, preserving headings, lists, tables, and formatting.

## Directory Structure

- `input/`: Upload or place files here for processing.
- `output/`: Final Markdown results are stored here.
- `cache/`: Temporary files generated during OCR (automatically cleaned if `delete_cache=True`).

## Cleaning Up

Use the **"Clear Cache and Output"** button in the sidebar to remove all temporary and output files.

Alternatively, manually delete the `cache/` and `output/` directories.

## Customization

To modify behavior:

- Edit `get_processors()` in `main.py` to change OCR or MarkItDown settings.
- Update file extension lists (`OCR_EXTENSIONS`, `MID_EXTENSIONS`) to support more types.
- Extend `cli.py` to handle additional formats or logging.

## License

This project is open-source. See the LICENSE file for details.
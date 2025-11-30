from pathlib import Path
from docling.document_converter import DocumentConverter
import shutil


def convert_pdf_to_markdown(input_path: Path, output_path: Path) -> None:
    """
    Convert a single PDF to a Markdown file using Docling.
    """
    converter = DocumentConverter()
    result = converter.convert(str(input_path))

    md_content = result.document.export_to_markdown()

    output_path.write_text(md_content, encoding="utf-8")
    print(f"✅ Converted: {input_path.name}")
    print(f"📄 Output saved to: {output_path}")


def move_pdf_to_completed(input_path: Path, completed_dir: Path) -> None:
    """
    Move the processed PDF to completed-pdfs/ to avoid reprocessing it.
    """
    completed_dir.mkdir(exist_ok=True)
    destination = completed_dir / input_path.name
    shutil.move(str(input_path), str(destination))
    print(f"📦 Moved to completed-pdfs/: {input_path.name}")


def main() -> None:
    """
    Convert all PDFs in inputs/ to Markdown and then move them to completed-pdfs/.
    """
    inputs_dir = Path("inputs")
    outputs_dir = Path("outputs")
    completed_dir = Path("completed-pdfs")

    outputs_dir.mkdir(exist_ok=True)

    pdf_files = list(inputs_dir.glob("*.pdf"))

    if not pdf_files:
        print("⚠️ No PDF files found in inputs/. Add one or more PDFs to the inputs/ folder and run again.")
        return

    for pdf in pdf_files:
        output_md = outputs_dir / f"{pdf.stem}.md"

        # Convert to Markdown
        convert_pdf_to_markdown(pdf, output_md)

        # Move to completed-pdfs/
        move_pdf_to_completed(pdf, completed_dir)


if __name__ == "__main__":
    main()

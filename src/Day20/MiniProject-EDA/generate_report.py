from fpdf import FPDF
import re


class PDFReport(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Title
        self.cell(0, 10, 'Mini Project EDA Executive Report', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')


def markdown_to_plaintext(md_text: str) -> str:
    """Convert a subset of markdown to plain text with minimal formatting."""
    lines = []
    for line in md_text.splitlines():
        # headings (# ..)
        if line.startswith('#'):
            # remove leading # and maybe spaces
            text = line.lstrip('#').strip()
            lines.append(text.upper())
        elif line.startswith('- ') or line.startswith('* ') or re.match(r"\d+\. ", line):
            # bullet or numbered list
            lines.append('  ' + re.sub(r"^(?:- |\* |\d+\. )", '- ', line))
        else:
            lines.append(line)
    return "\n".join(lines)


def safe_text(text: str) -> str:
    """Return text with characters unsupported by latin-1 replaced."""
    return text.encode('latin-1', errors='replace').decode('latin-1')


def generate_pdf(input_path: str, output_pdf: str):
    """Generate a PDF from either a markdown file or a Jupyter notebook.

    - markdown: uses simple text conversion with FPDF (header/footer only).
    - notebook: exports to HTML with nbconvert and then converts to PDF via WeasyPrint.
    """
    if input_path.lower().endswith('.ipynb'):
        # manually read notebook and render content to PDF (code, outputs, markdown)
        import nbformat
        import base64
        import tempfile

        nb = nbformat.read(input_path, as_version=4)
        pdf = PDFReport()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        for cell in nb.cells:
            if cell.cell_type == 'markdown':
                text = markdown_to_plaintext(cell.source)
                for line in text.splitlines():
                    pdf.set_font('Arial', '', 12)
                    pdf.multi_cell(0, 8, safe_text(line))
                pdf.ln(2)
            elif cell.cell_type == 'code':
                pdf.set_font('Courier', '', 10)
                # show code
                for line in cell.source.splitlines():
                    pdf.multi_cell(0, 6, safe_text(line))
                pdf.ln(1)
                # outputs
                for output in cell.get('outputs', []):
                    otype = output.get('output_type')
                    if otype == 'stream':
                        pdf.set_font('Courier', '', 10)
                        pdf.multi_cell(0, 6, safe_text(output.get('text', '')))
                    elif otype in ('display_data', 'execute_result'):
                        data = output.get('data', {})
                        if 'text/plain' in data:
                            pdf.set_font('Courier', '', 10)
                            pdf.multi_cell(0, 6, safe_text(data['text/plain']))
                        if 'image/png' in data:
                            imgdata = base64.b64decode(data['image/png'])
                            with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tf:
                                tf.write(imgdata)
                                imgpath = tf.name
                            # scale image to page width minus margins
                            page_width = pdf.w - pdf.l_margin - pdf.r_margin
                            pdf.image(imgpath, w=page_width)
                            pdf.ln(1)
        pdf.output(output_pdf)
        print(f"PDF generated from notebook: {output_pdf}")
    else:
        # assume markdown
        with open(input_path, 'r', encoding='utf-8') as f:
            md_text = f.read()

        content = markdown_to_plaintext(md_text)
        pdf = PDFReport()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font('Arial', '', 12)
        for line in content.splitlines():
            pdf.multi_cell(0, 8, safe_text(line))
        pdf.output(output_pdf)
        print(f"PDF generated: {output_pdf}")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Generate PDF report from markdown file')
    parser.add_argument('input', help='Markdown input file (e.g. report.md)')
    parser.add_argument('output', nargs='?', default='project_report.pdf', help='Output PDF file name')
    args = parser.parse_args()

    generate_pdf(args.input, args.output)

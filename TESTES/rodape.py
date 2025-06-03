import os
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

# Texto da observação
observacao = "Observação: Documento revisado em 2025."

# Pasta com os PDFs
pasta_pdfs = "."  # mesma pasta do script
saida_pasta = "./pdfs_editados"  # cria subpasta para os PDFs com observações

os.makedirs(saida_pasta, exist_ok=True)

def criar_overlay(texto):
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica", 10)
    can.drawString(50, 30, texto)  # posição no rodapé
    can.save()
    packet.seek(0)
    return PdfReader(packet)

# Iterar sobre arquivos PDF na pasta
for nome_arquivo in os.listdir(pasta_pdfs):
    if nome_arquivo.lower().endswith(".pdf"):
        caminho_pdf = os.path.join(pasta_pdfs, nome_arquivo)
        reader = PdfReader(caminho_pdf)
        writer = PdfWriter()

        overlay = criar_overlay(observacao)

        for pagina in reader.pages:
            pagina.merge_page(overlay.pages[0])  # aplica o texto sobre a página
            writer.add_page(pagina)

        nome_saida = os.path.join(saida_pasta, nome_arquivo)
        with open(nome_saida, "wb") as saida_pdf:
            writer.write(saida_pdf)

print("Observações inseridas em todos os PDFs com sucesso!")
from pathlib import Path

pasta = Path("pasta_teste")
pasta.mkdir(exist_ok=True)

nomes = [
    "foto.jpg", "foto2.png", "contrato.pdf", "notas.txt",
    "planilha.xlsx", "video.mp4", "musica.mp3",
    "backup.zip", "arquivo_estranho.xyz",
]

for nome in nomes:
    (pasta / nome).write_text("Arquivo de teste")
    
print(f"{len(nomes)} arquivos criados em '{pasta}'.")
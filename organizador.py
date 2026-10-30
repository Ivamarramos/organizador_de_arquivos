from pathlib import Path
import shutil

CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audios": [".mp3", ".wav", ".ogg"],
    "Compactados": [".zip", ".rar", ".7z"],
}


def descobrir_categoria(extensao):
    """Recebe uma extensão (ex: '.jpg') e devolve o nome da categoria."""
    for categoria, extensoes in CATEGORIAS.items():
        if extensao.lower() in extensoes:
            return categoria
    return "Outros"
    

def organizar(caminho_pasta):
    pasta = Path(caminho_pasta)
    
    if not pasta.is_dir():
        print("Pasta não encontrada. Confira o caminho.")
        return
    
    movidos = 0
    
    for item in pasta.iterdir():
        if not item.is_file():
            continue
        
        categoria = descobrir_categoria(item.suffix)
        pasta_destino = pasta / categoria
        pasta_destino.mkdir(exist_ok=True)
        
        destino = pasta_destino / item.name
        if destino.exists():
            destino = pasta_destino / f"{item.stem}_copia{item.suffix}"
            
        shutil.move(str(item), str(destino))
        print(f"{item.name} -> {categoria}/")
        movidos += 1
        
    print(f"\nPronto! {movidos} arquivo(s) organizado(s).")
    

if __name__ == "__main__":
    caminho = input("Digite o caminho da pasta a organizar: ")
    organizar(caminho)
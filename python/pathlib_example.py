import os
from pathlib import Path

os.system('cls')

caminho_projeto = Path()
print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
print(caminho_arquivo)

print(caminho_arquivo.parent)
print(caminho_arquivo.parent.parent)

idea = caminho_arquivo.parent / 'pathlib'
# print(idea / 'pathlib.txt')

# print(Path.home() / 'Desktop' / 'teste')
file = Path.home() / 'Desktop' / 'teste.bat'
file.touch()
print(file)
file.write_text('calc.exe')
print(file.read_text())
os.system(file.read_text())
file.unlink() #Apaga o arquivo

file_folder = Path.home()/ 'Desktop' / 'Cool Folder'
file_folder.mkdir(exist_ok=True)
file_subfolder = file_folder / 'subfolder'
file_subfolder.mkdir(exist_ok=True)

# file_folder.rmdir() #Apagando de forma recursiva

files = file_folder / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'
    if file.exists():
        file.unlink()
    else:
        file.touch()
    
    with file.open('a+') as text_file:
        text_file.write('Salve gurizadinha\n')
        text_file.write(f'file_{i}.txt')

def rmtree(root: Path, remove_root= True):
    for file in root.glob('*'):
        if file.is_dir():
            rmtree(file, False)
            file.rmdir()

        else:
            file.unlink()

    if remove_root:
        root.rmdir()

rmtree(file_folder)
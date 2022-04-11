from pathlib import Path

def help():
    File= open("CLI Help.txt","r")
    print(File.read())
    File.close()


def hello(name="World"):
    print("Hello",name)

def sum(NbA,NbB):
    return(NbA+NbB)

def cat(file_name=""):
    if file_name=="":
        return "Vous n'avez pas rentrer de chemin. Recommencer"
    else:
        File=Path(file_name)
        if File.is_file() :
            Fichier=open(file_name,'r')
            print (Fichier.read())
            Fichier.close()
            return '\nLe fichier a bien été trouvé'
        else:
            return "Le chemin n'est pas bon. Recommencer"

print(cat("U:\cleme.pannecoucke\Mes documents\Projet\CLI Help.txt"))
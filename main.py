""" Logiciel de scan photo local """
import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image as img
from PIL import UnidentifiedImageError as ImgError
from PIL import ExifTags

print("==================================================================================")
print("PROGRAMME D'ANALYSE D'IMAGE")
print("==================================================================================")
print("\n")

root = tk.Tk()
root.withdraw()

chemin = fd.askopenfilename(
    title='Selectionner un fichier',
    filetypes=[
        ("image", "*.png"),
        ("image", "*.jpg"),
        ("image", "*.webp"),
        ("image", "*.jpeg"),
        ("image", "*.gif"),
        ("image", "*.tif"),
        ("image", "*.tiff"),
        ("image", "*.bmp"),
        ("image", "*.avif"),
        ("tous les fichiers", "*.*"),
    ],
)

if chemin:
    print("\n")
    print("Fichier sélectionné :", chemin)
    print("\n")
# Début de l'analyse du fichier 

    try:
        with img.open (chemin) as f:            
            print("\n")
            print("==============================================")
            print("Caractéristiques du fichier ")
            print("Format", f.format)
            print("Taille", f.size)
            print("Mode", f.mode)
            print("\n")

            exif = f.getexif()
            if exif:
                for key, value in exif.items():
                    key = ExifTags.TAGS.get(key, key)
                    print(key, "=>", value)
            else:
                print("Données EXIF non présentes sur cette image")
            #print(ExifTags.GPSTAGS)
            print(exif.get_ifd(34853))
            #print(exif.get_ifd())
            print("==============================================")
    except ImgError:
        print("Erreur lors de l'ouverture du fichier (Le fichier n'est pas une image reconnue)")

    except PermissionError:
        print("Accès au fichier refusé.")

    except OSError:
        print("Une erreur d'entrée/sortie est survenue.")

    else:
        print("Analyse effectuée avec succès.")

    finally:
        
        print("Fin de l'analyse.")

else:
    print("\n")
    print("Aucun fichier sélectionné.")
    


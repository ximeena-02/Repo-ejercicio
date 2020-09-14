import os
try:
    import requests
except ImportError:
    os.system("pip install requests")
    print('Installing requests...')
    print('Ejecuta de nuevo tu script...')
    exit()
try:
    from bs4 import BeautifulSoup as bs
except ImportError:
    os.system("pip install bs4")
    print("Installing bs4...")
    print('Ejecuta de nuevo tu script...')
    exit()
try:
    import sys
except ImportError:
    os.system("pip install sys")
    print("Installing sys...")
    print('Ejecuta de nuevo tu script...')
    exit()
try:
    import webbrowser
except ImportError:
    os.system("pip install webbrowser")
    print("Inatlling webbrowser...")
    print('Ejecuta de nuevo tu script...')
    exit()
    
# Ximena Pérez Escamilla #1898135
# Lo que hace este script es buscar entre la pagina de noticias de la uanl
# ordenandole escribir un rango entre las noticias que se quieren
# investigar, por lo tanto, el programa va buscando de noticia en noticia
# en la url de la uanl, ya cuando tiene la pagina de la noticia verifica
# si la pagina se encontro o no, si se encontro entonces realiza
# un beautifulsoup en donde saca la informacion como los links y parrafos,
# de cada una de las noticias y verifica si la dependencia que se desea
# aparece en un algun parrafo de esa noticia, si si aparece entonces te abre
# la pagina de la noticia que esta relacionanda con la dependencia que
# investigamos

print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango, finRango = finRango, inicioRango
for i in range(inicioRango, finRango, 1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get(url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content, "html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content, "html.parser")
                parrafos = soup2.select("p")
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print("Abriendo", url2)
                        webbrowser.open(url2)
                        break

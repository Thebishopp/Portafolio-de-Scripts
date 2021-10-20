### Script que permite comprimir en un ZIP de forma recursiva un directorio con la extensión de archivo necesaria.
### Fue utilizado comprimir todos los *.csv para su posterior análisis en un dashboard
import glob
import zipfile
import os

def extractor(path, namezip):
    data = glob.glob(path, recursive=True)
    with zipfile.ZipFile(namezip, "w") as zipMe:
        for i in data:
            zipMe.write(i, compress_type=zipfile.ZIP_DEFLATED)

extractor("?:\Datos Patente\?????\**/.csv", "exata.zip" )

import glob
import zipfile
import os

def extractor(path, namezip):
    data = glob.glob(path, recursive=True)
    with zipfile.ZipFile(namezip, "w") as zipMe:
        for i in data:
            zipMe.write(i, compress_type=zipfile.ZIP_DEFLATED)

extractor("?:\Datos Patente\?????\**/", "exata.zip" )

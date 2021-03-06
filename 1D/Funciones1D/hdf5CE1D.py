import h5py
import numpy as np
import sys
def leerParametros(archivoHDF5,*parametros,diccionario={}):
    with h5py.File(archivoHDF5,'r') as f:
        for parametro in parametros:
            valor=f.get(parametro)
            if valor==None:
                print('Parametro :', parametro,' no encontrado')
                continue

            if valor.dtype == int:
                diccionario[parametro]=int(np.array(valor))

            elif valor.dtype == float:
                try:
                    diccionario[parametro]=float(np.array(valor))
                except TypeError:
                    diccionario[parametro]=np.array(valor)
            elif valor.dtype == np.float16:
                diccionario[parametro]=np.array(valor,dtype=np.float16)
            elif valor.dtype == object:
                diccionario[parametro]=np.array2string(valor)
        return diccionario


def saveParametros(archivoHDF5,diccionario):


    with h5py.File(archivoHDF5,'w') as f:
        for key,values in diccionario.items():
            f[key]=values



if __name__ == "__main__":
    try:
        in_file_name=sys.argv[1]
    except:
        mensaje = """ Error: La ejecucion de este programa requiere de 1 argumento.
        Ejecucion correcta: python hdf5.py ENTRADA1
        donde el nombre "ENTRADA" es el nombre del archivo donde
        se almacenan los datos del problema.
        Los datos que se guardan en el archivo ENTRADA son los que se encuentran en
        este archivo hdf5.py

        Por ejemplo: python hdf5.py ENTRADA"""

        print(mensaje)
        sys.exit(1)

    #Generamos parametros
    archivo=in_file_name
    Datos={
        'L' :1.0, 
        'N':20, 
        'kappa' : 0.1,
        'rho': 1.0, 
        'vel' : 2.1, 
        'T0': 1.0, 
        'TL': 0
    }

    saveParametros(archivo,Datos)

# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import zipfile
import csv


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```

    """
    # Descomprimir el archivo input.zip
    with zipfile.ZipFile('files/input.zip', 'r') as zip_ref:
        zip_ref.extractall('.')

    # Crear la carpeta output si no existe
    os.makedirs('files/output', exist_ok=True)

    # Función para procesar un conjunto de datos (train o test)
    def process_dataset(dataset_name):
        data = []
        base_path = f'input/{dataset_name}'
        for sentiment in ['positive', 'negative', 'neutral']:
            sentiment_path = os.path.join(base_path, sentiment)
            for file in os.listdir(sentiment_path):
                if file.endswith('.txt'):
                    with open(os.path.join(sentiment_path, file), 'r', encoding='utf-8') as f:
                        phrase = f.read().strip()
                    data.append({'phrase': phrase, 'target': sentiment})
        # Escribir el CSV
        with open(f'files/output/{dataset_name}_dataset.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['phrase', 'target']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    # Procesar train y test
    process_dataset('train')
    process_dataset('test')

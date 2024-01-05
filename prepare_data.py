import os
import requests


def prepare_data():
    """
    Descarga los datos de entrenamiento del modelo Phi-2 y los prepara para su uso.

    Devuelve:
        La ruta a los datos de entrenamiento preparados.
    """

    data_path = os.path.join("data", "phi-2")
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    # Descarga los datos de entrenamiento

    url = "https://download.microsoft.com/download/3/E/A/3EA3B729-418F-463D-8309-23D7086059F6/phi-2-data.zip"
    response = requests.get(url)
    with open(os.path.join(data_path, "phi-2-data.zip"), "wb") as f:
        f.write(response.content)

    # Descomprime los datos de entrenamiento

    with zipfile.ZipFile(os.path.join(data_path, "phi-2-data.zip")) as zip_file:
        zip_file.extractall(data_path)

    return data_path


if __name__ == "__main__":
    data_path = prepare_data()
    print(data_path)

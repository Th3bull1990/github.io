import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def train(data_path, output_path):
    """
    Entrena el modelo Phi-2.

    Args:
        data_path: La ruta a los datos de entrenamiento.
        output_path: La ruta a donde se guardar
        

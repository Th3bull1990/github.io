import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-2")
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-2")

def generate_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=200)
    text = tokenizer.batch_decode(outputs)[0]
    return text

if __name__ == "__main__":
    prompt = "¿Cuál es la capital de España?"
    print(generate_text(prompt))

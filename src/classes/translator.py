from operator import mod
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class Translator:
    tokenizer_pretrained = "salesken/translation-spanish-and-portuguese-to-english"
    model_pretrained = "salesken/translation-spanish-and-portuguese-to-english"

    def __init__(self, tokenizer=None, model=None):
        if tokenizer:
            self.tokenizer_pretrained = tokenizer
        if model:
            self.model_pretrained = model

        self.tokenizer = AutoTokenizer.from_pretrained(self.tokenizer_pretrained)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_pretrained)

    def translate(self, text, callback=None):
        inputs = self.tokenizer.encode(
            text, return_tensors="pt", padding=True, max_length=512, truncation=True
        )
        outputs = self.model.generate(
            inputs, max_length=128, num_beams=None, early_stopping=True
        )
        translation = (
            self.tokenizer.decode(outputs[0]).replace("<pad>", "").strip().lower()
        )
        if callback:
            callback(translation)
        return translation

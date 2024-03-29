from transformers import pipeline


class Translator:
    def __init__(self):
        self.special_tokens_dict = {
            ")": "<cp> ",
            "(": "<op> ",
            "?": "<qm> ",
            "=": "<equal>",
            "#": "<hash> ",
            "@": "<at> ",
            "&": "<ampersand> ",
            "%": "<percent> ",
            "$": "<dollar> ",
            "£": "<pound> ",
            "€": "<euro> ",
            "¥": "<yen> ",
        }
        self.reverse_special_tokens_dict = {
            v.strip(): k for k, v in self.special_tokens_dict.items()
        }

        self.model_en_to_es = pipeline(
            "translation", model="Helsinki-NLP/opus-mt-en-es"
        )
        self.model_es_to_en = pipeline(
            "translation", model="Helsinki-NLP/opus-mt-es-en"
        )

    def english_to_spanish(self, text) -> str:
        for key, value in self.special_tokens_dict.items():
            text = text.replace(key, value)

        translation = self.model_en_to_es(text)
        if len(translation) > 0:
            text = translation[0]["translation_text"]

        for key, value in self.reverse_special_tokens_dict.items():
            text = text.replace(key, value)

        return text

    def spanish_to_english(self, text) -> str:
        if "¿" not in text and "?" in text:
            text = "¿" + text

        for key, value in self.special_tokens_dict.items():
            text = text.replace(key, value)

        translation = self.model_es_to_en(text)
        if len(translation) > 0:
            text = translation[0]["translation_text"]

        for key, value in self.reverse_special_tokens_dict.items():
            text = text.replace(key, value)

        return text

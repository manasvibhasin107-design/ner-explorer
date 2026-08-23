from fastapi import FastAPI
import spacy

app = FastAPI()

nlp = spacy.load("en_core_web_sm")

@app.get("/")
def home():
    return {
        "message": "NER Explorer API Running"
    }

@app.post("/analyze")
def analyze(text: str):

    doc = nlp(text)

    tokens = [token.text for token in doc]

    lemmas = [token.lemma_ for token in doc]

    pos_tags = [
        {
            "word": token.text,
            "pos": token.pos_
        }
        for token in doc
    ]

    stop_words = [
        token.text
        for token in doc
        if token.is_stop
    ]

    entities = [
        {
            "text": ent.text,
            "label": ent.label_
        }
        for ent in doc.ents
    ]

    return {
        "tokens": tokens,
        "lemmas": lemmas,
        "stop_words": stop_words,
        "pos_tags": pos_tags,
        "entities": entities
    }
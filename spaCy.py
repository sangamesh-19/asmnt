import spacy

nlp = spacy.load('en_core_web_sm')

def classify_article(content):
    doc = nlp(content)
    # Implement custom classification logic based on keywords, phrases, etc.
    if "protest" in content or "riot" in content:
        return "Terrorism / protest / political unrest / riot"
    elif "earthquake" in content or "flood" in content:
        return "Natural Disasters"
    elif "inspiring" in content or "achievement" in content:
        return "Positive/Uplifting"
    else:
        return "Others"

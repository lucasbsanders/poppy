from spellchecker import SpellChecker
import pytesseract
import re
from image_processor import img_pipeline


def correct_directive(directive):
    # The directives get checked and corrected using spellchecker distance ?
    # The strings get corrected to their closest words in the corpus
    # "TAGE 1 TAGLET" becomes "TAKE 1 TABLET"
    spell = SpellChecker()
    # Tokenize the directive
    token_directive = directive.split()
    # Spell Check and correct all the elements of the list
    for counter, token in enumerate(token_directive):
        if token[0].isalpha():
            token_directive[counter] = spell.correction(token)
        # Make the tokens uppercase
    upper_directive = [token.upper() for token in token_directive]

    return upper_directive


def correct_duration(duration):
    # The durations get checked and corrected using spellchecker distance ?
    # The strings get corrected to their closest words in the corpus
    # "Ery 8 Hours" becomes "EVERY 8 HOURS and "
    spell = SpellChecker()
    # Tokenize the duration
    token_duration = duration.split()
    # Spell Check and correct all the elements of the list
    for counter, token in enumerate(token_duration):
        if token[0].isalpha():
            token_duration[counter] = spell.correction(token)
    # Make the tokens uppercase
    upper_duration = [token.upper() for token in token_duration]

    return upper_duration


def text_pipeline():
    token_duration = []
    token_directive = []
    # extract the text from the images
    processed_img = img_pipeline()
    text_one = pytesseract.image_to_string(processed_img)
    # print the text
    print("The text from the image is: ", text_one)

    # Extract the directive from the prescription
    text = "Take many pills as Needed"
    # Add try catches
    try:
        directive_searcher = re.search(
            "([Tt]?[Aa][Kk][Ee]?|[Gg]?[Ii][Vv][Ee]?|[Aa]?[Dd][Mm][Ii][Nn][Ii][Ss][Tt][Ee][Rr]?)(.*)([Mm]?["
            "Oo][Uu]?[Tt]?[Hh]?|[Oo]?[Rr]?[Aa][Ll][Ll][Yy]?|[Tt]?[Aa][Bb][Ll][Ee][Tt][Ss]?)", text_one)
        directive = directive_searcher.group(0)
        token_directive = correct_directive(directive)
        print("This is the directive:", directive)
    except AttributeError:
        print("Couldn't Find the Directive")

    try:
        duration_searcher = re.search(
            "([Ee]?[Vv]?[Ee][Rr][Yy]|[Oo][Nn]?[Cc][Ee]|[Tt][Ww]?[Ii]?[Cc]?[Ee]|[Tt][Hh]?[Rr]?[Ii]?[Cc]?[Ee]|"
            "[Dd][Aa]?[Ii]?[Ll]?[Yy]|\d\s)(.*)([Dd][Aa]?[Ii]?[Ll]?[Yy]|[Hh]?[Oo][Uu][Rr][Ss]?|"
            "[Dd][Aa][Yy][Ss]?|[Ww][Ee][Ee][Kk][Ss]|[Mm][Oo][Rr][Nn][Ii][Nn][Gg][Ss]?|[Aa][Ff][Tt][Ee][Rr]"
            "[Nn][Oo][Oo][Nn][Ss]?|[Nn][Ii][Gg][Hh][Tt][Ss]?)", text_one)
        duration = duration_searcher.group(0)
        token_duration = correct_duration(duration)
        print("This is the duration: ", duration)
    except AttributeError:
        print("Couldn't Find the Duration")

    print(token_duration)
    print(token_directive)
    return token_directive, token_duration

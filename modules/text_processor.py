from spellchecker import SpellChecker
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
    duration = ""
    directive = ""
    # extract the text from the images
    # img_pipeline() returns the preprocessed text from the image_processor module
    # make the text upppercase, remove newline chracters
    preprocessed_text = img_pipeline().upper()
    preprocessed_text = preprocessed_text.strip("\n")
    # print the text
    print("The text from the image is: ", preprocessed_text)

    # Extract the directive from the prescription
    text = "Take many pills as Needed"
    # Add try catches
    try:
        directive_searcher = re.search(
            "([T]?[A][K][E]?|[G]?[I][V][E]?|[A]?[D][M][I][N][I][S][T][E][R]?)(.*)([M]["
            "O][U][T]?[H]?|[O]?[R]?[A][L][L][Y]?|[T]?[A][B][L][E][T][S]?|[C][A][P][S][U][L][E][S]|"
            "[T][I][M][E][S]?|[D][A]?[I]?[L][Y])",
            preprocessed_text)
        directive = directive_searcher.group(0)
        token_directive = correct_directive(directive)
        print("This is the directive:", directive)
    except AttributeError:
        print("Couldn't Find the Directive")

    try:
        duration_searcher = re.search(
            "([E]?[V]?[E][R][Y]|[D][A][I][L][Y])(.*)"
            "([D][A][I][L][Y]|[H]?[O][U][R][S]?|"
            "[D][A][Y][S]?|[W][E][E][K][S]|[M][O][R][N][I][N][G][S]?|[A][F][T][E][R]"
            "[N][O][O][N][S]?|[N][I][G][H][T][S]?)", preprocessed_text)
        duration = duration_searcher.group(0)
        token_duration = correct_duration(duration)
        print("This is the duration: ", duration)
    except AttributeError:
        duration = "EVERY DAY"
        token_duration = correct_duration(duration)
        print("This is the duration: ", duration)

    print(token_duration)
    print(token_directive)
    return token_directive, token_duration

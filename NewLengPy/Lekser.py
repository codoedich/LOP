import re

from Tokeni import Tokeni, DICT_TOKENOW
import Errors


def checkBracket(tokens, line):
    z = 0
    for elem in tokens:
        if elem.TypeToken() == "BRACKET":
            z += 1
        if elem.TypeToken() == "BRACKET_BACK":
            z -= 1
    if z != 0:
        raise Errors.NotBracket(")", line)


def checkFigBracket(tokens, line):
    z = 0
    for elem in tokens:
        if elem.TypeToken() == "FIGURE_BRACKET":
            z += 1
        if elem.TypeToken() == "FIGURE_BRACKET_BACK":
            z -= 1
    if z != 0:
        raise Errors.NotFigBracket("}", line)


class Lekser:

    def __init__(self, kod):
        self.kod = kod
        self.lexemes_lines = list()

    def analise(self):
        for v in range(len(self.kod)):

            lexemes = list()
            words = self.kod[v].split()
            for jj in range(len(words)):
                lexemes.append(self.search_token(words[jj], v + 1, jj + 1))
                if lexemes[0].TypeToken() == "INT":
                    raise Errors.IntInStartLine(lexemes[0].Value(), jj + 1)
            checkBracket(lexemes, v + 1)
            checkFigBracket(lexemes, v + 1)
            self.lexemes_lines.append(lexemes)

    def search_token(self, word, num_line, num):

        for elem in DICT_TOKENOW:
            result = re.search(DICT_TOKENOW[elem], word)
            if result:
                return Tokeni(elem, word, num_line, num)
        raise Errors.FalseSyntaksis(word, num_line, num)

    def show(self):
        for v in range(len(self.lexemes_lines)):
            for elem in self.lexemes_lines[v]:
                elem.toString()

    def get(self):
        return self.lexemes_lines

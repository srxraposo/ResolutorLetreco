import glob
import re

def remove_accents(raw_text):
    """Removes common accent characters.

    Our goal is to brute force login mechanisms, and I work primary with
    companies deploying Engligh-language systems. From my experience, user
    accounts tend to be created without special accented characters. This
    function tries to swap those out for standard Engligh alphabet.

    https://github.com/initstring/linkedin2username
    
    MIT License

    Copyright (c) 2018 InitString

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """

    raw_text = re.sub(u"[àáâãäå]", 'a', raw_text)
    raw_text = re.sub(u"[èéêë]", 'e', raw_text)
    raw_text = re.sub(u"[ìíîï]", 'i', raw_text)
    raw_text = re.sub(u"[òóôõö]", 'o', raw_text)
    raw_text = re.sub(u"[ùúûü]", 'u', raw_text)
    raw_text = re.sub(u"[ýÿ]", 'y', raw_text)
    raw_text = re.sub(u"[ß]", 'ss', raw_text)
    raw_text = re.sub(u"[ñ]", 'n', raw_text)
    raw_text = re.sub(u"[ç]", 'c', raw_text)
    return raw_text 

class WordList:
    def __init__(self, data_folder):
        files = glob.glob(data_folder+"/*txt")
        self.__words = self.__get_words(files) # backup list
        self.words = [*self.__words]            # visible    
        self.undo = []
    
    def __get_words(self, files):
        words = set()
        for file in files:
            with open(file, encoding="utf-8") as f:
                for i in f.readlines(): 
                    if len(i) == 6:
                        words.add(remove_accents(i.rstrip("\n").lower()).upper())
        return list(words)

    def restore_list(self):
        self.words = [*self.__words]         # visible    

    def print_words(self):
            print(self.words)

    def remove_letters(self, letters):
        self.undo = [*self.words]
        for letter in letters:
            self.words = list(filter(lambda word: letter.upper() not in word, self.words))
    
    def include_letters(self, letters):
        self.undo = [*self.words]
        for letter in letters:
            self.words = list(filter(lambda word: letter.upper() in word, self.words))

    def place_letters(self, letters_pos):
        self.undo = [*self.words]
        for letter, pos in letters_pos:
            self.words = list(filter(lambda word: letter.upper() == word[int(pos)], self.words))
    
    def remove_positions(self, letters_pos):
        self.undo = [*self.words]
        for letter, pos in letters_pos:
            self.words = list(filter(lambda word: letter.upper() != word[int(pos)], self.words))

    def undo_last_filter(self):
        self.words = self.undo
        self.undo = []

MENU = """MODOS:\n[0] REMOVER LETRAS\n[1] POSICIONAR LETRAS\n[2] INCLUIR LETRAS\n[3] REMOVER POSICOES\n[5] Reiniciar"""

if __name__ == "__main__":
    a = WordList("word-data/")

    while True:
        mode = input(MENU)

        if mode == "0":
            letras = input().split()
            a.remove_letters(letras)
        elif mode == "1":
            letras_pos = list(map(lambda x: x.split(","), input().split(" ")))
            a.place_letters(letras_pos)
        elif mode == "2":
            letras = input().split()
            a.include_letters(letras)
        elif mode == "3":
            letras_pos = list(map(lambda x: x.split(","), input().split(" ")))
            a.remove_positions(letras_pos)
        elif mode == "5":
            a.restore_list()

        a.print_words()
                


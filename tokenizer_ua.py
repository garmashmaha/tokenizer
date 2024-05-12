class Tokenizer:
    def __init__(self, separators=[' ', '-', "'"]):
        self.separators = separators

    def tokenize(self, text):
        tokens = [] 
        word = '' 
        for i in range(len(text)):
            if text[i] in self.separators:
                if text[i] in ["-", "'"] and i > 0 and i < len(text) - 1 and text[i-1].isalpha() and text[i+1].isalpha():
                    word += text[i]
                else:
                    if word:
                        tokens.append(word)
                        word = ''
            else:
                word += text[i]
        if word:
            tokens.append(word)
        return tokens

# Testowanie
tokenizer = Tokenizer()
text = "По-перше, постіль не була м'якою, а по-друге - це взагалі не можна назвати постіллю."
tokens = tokenizer.tokenize(text)
print(tokens)

def word_given(text , text2):
    if not isinstance(text, text2, str):
        print("Input must be a string.")
        return None
    word = text[0]
    word2 = text2[0]
    
    if  word == word2:
        print(f"'{text}' and '{text2}' first letter is same")
    else:        
        print(f"'{text}' and '{text2}' first letter is different")
word_given("hello", "hi")
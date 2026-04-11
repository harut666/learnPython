def howSymbol(number):
    if not isinstance(number, int):
         print("It's not an integer")
         return None
         
    number = abs(number)     
    how_symbols = str(number)
    return len(how_symbols)

print(howSymbol(1234567890))




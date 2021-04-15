def is_palindrome(word):
    word = word.lower().replace(" ", "")
    if word == word[::-1]:
        return True
    else:
        return False

def run():
    word = input("Escribe una palabra: ")
    if is_palindrome(word):
        print("Es palíndromo")
    else:
        print("No es palíndromo")

if __name__ == "__main__":
    run()
def main():
    word = input("Enter a word to reverse: ")
    l = ""
    size = len(word)

    while size > 0:
        # Reverse the string by removing the last letter and moving it up front based on the lenght of the string
        l += word[size-1]
        # Length left
        size = size - 1
    print(f"The word {word} reversed is {l}")

if __name__ == '__main__':
    main()
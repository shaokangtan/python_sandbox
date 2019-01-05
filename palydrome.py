def polydrome(input):
    length = len(input)
    for i in range (length//2):
        if input[i] != input[length-i-1]:
            return False
    return True



if __name__ == "__main__":
    print (polydrome("21233212"))
#return most frequent character on success; return "" on failure
#
#rules: cannot use libraries or packages
#       cannot use collections.OrderedDict. the ordinary dictionary is not orderred !!!
#       cannot use sorted()
#       upper case letter are converted into lower case
#       empty string is treaed as illegal input and returned as failure
#       unicode and hidden ASCII keys are not checked in this scope
#       language: python, version: 3.0

def character_freq(string):
    if string=="":
        return ""
    freq = {} # dictionary to track character frequency
    order = {} # dictionary to track character apperance order
    for i in range(len(string)):
        c = string [i].lower()
        if c == " ": # dismiss space character
            continue
        if c in freq:
            freq[c] = freq[c] + 1
        else:
            freq[c] = 1
            order[c] = i

    # find the most freqent character in the string, when more than one character has the same frequency
    # use the sequence of apperance in the string to decide the rule
    key_freq = -1
    key_order = -1
    key = -1
    for c,f in freq.items():
        if f > key_freq:
            key = c
            key_freq = f
            key_order = order[c]
        elif f == key_freq:
            if order[c] < order[key]:
                key = c
                key_order = order[c]
                #print ("%c %d".format(key, key_order))
    #print("key: {}, freq: {}, order: {}".format (key, key_freq, key_order))
    return key


#test

def test_character_freq(string,result):
    c = character_freq(string)
    assert c == result
    print ("most freqent character is {}".format(c))

test_character_freq("", "")
test_character_freq("aaabbc","a")
test_character_freq("zzzbbccc","z")
test_character_freq("ZZZbbccc","z")
test_character_freq("ZZZbbcccBb","b")
test_character_freq("ZZZbbccc111","z")
test_character_freq("111ZZZbbccc","1")
test_character_freq("222111ZZZbbccc","2")
test_character_freq("aaabbcccdc","c")
test_character_freq("!a#a$a%b^bccc","a")
test_character_freq("aaabbcccdcefghefghefghefghefghefgh","e")
long_string = "Please write a method in the language of your choice " \
                "that takes a String as an input parameter, and returns the character that occurs most" \
                " often within the input String. Notes: a) If the result would be that several characters " \
                "appear with the same highest number, return the character that appears first in the String. " \
                "b) Do not use 3rd party libraries for support. If the API of your chosen language contains " \
                "a method for this functionality, do not call it but write the method from scratch. " \
                "c) Do not try to solve for all possible scenarios in this implementation (e.g. unicode support). " \
                "However, your code should protect against common invalid input parameters like an empty String. " \
                "You can add remarks about other robustness checks you would implement, if there was more time."

test_character_freq(long_string,"t")

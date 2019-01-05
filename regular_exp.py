import re
def check_valid_email(email):
    #ptrn = re.compile("^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$")
    ptrn = re.compile("[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}")
    for n in re.finditer(ptrn, email):
        print ("{}".format(n))
    return ptrn.match(email)

#check_valid_email("h@gmail.com i@gmail.com")


def test_reg_exp(regex, test_str):

    index_match = re.search(regex, test_str,  re.MULTILINE | re.DOTALL)
    #index_match = re.search(regex, test_str)

    matches = re.finditer(regex, test_str)


    for matchNum, match in enumerate(matches): #find the match
        matchNum = matchNum + 1
        print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum,
                start = match.start(), end = match.end(), match = match.group()))
        for groupNum in range(0, len(match.groups())): # find the group
            groupNum = groupNum + 1
            print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


tests= [
    [r"(?<=123)456(?=789)", "123456789"],
    [r"(?<=123)456(?=789)", "123456789 123456789 123456789"],
    [r"(123)456(789)", "123456789"],
    [r"(123)456(789)", "123456789 123456789 123456789"],
    #[r"^123.*\n.+\n.+11", "123456\n789\n101112"],
    #[r"\A123.*\n.+\n.+11", "123456\n789\n101112"],
    [r"BEGIN (.*) END", '''BEGIN hello
     world END'''],
    [r"^\S+$", '''hello
     world''']
]

for reg_exp,test_str in tests:
    print ("re:{}, test string:{}".format(reg_exp,test_str))
    test_reg_exp(reg_exp,test_str)

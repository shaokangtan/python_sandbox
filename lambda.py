
def exe_1():
    def fibonacci(n):
        # return a list of fibonacci numbers
        if n < 2:
            return n
        return fibonacci(n-2) + fibonacci(n-1)

    #How-to:
    #cube is a list, use map and list to create cube
    #use lambda to render fibonacc**3
    #use map and range to iterate fibonacci
    cube = list(map(lambda x: x **3, map(fibonacci, range(int(input())))))  # complete the lambda function

    print (cube)

def exe_2():
    """
        input :
        3
        lara@hackerrank.com
        brian-23@hackerrank.com
        britts_54@hackerrank.com

        Valid email addresses must follow these rules:
        It must have the username@websitename.extension format type.
        The username can only contain letters, digits, dashes and underscores.
        The website name can only have letters and digits.
        The maximum length of the extension is 3
        hint:
            l = list(filter(lambda x: x > 10 and x < 80, l))

    """
    def check_valid(email):
        try:
            username, url = email.split("@")
            website, extension = url.split(".")
        except ValueError:
            return False
        if not username.replace("-", "").replace("_", "").isalnum():
            return False
        if not website.isalnum():
            return False
        if len(extension) > 3:
            return False
        return True

    import re
    def check_valid1(email):
        ptrn = re.compile("^[a-zA-Z][\w-]*@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$")
        return ptrn.match(email)

    # \w it allows [0-9_]

    n = int(input())
    emails = [input().strip() for email in range(n)]

    valid = list(filter(check_valid1, emails))
    print(sorted(valid))

bills = [1,2,5,10,20,50,100]
large_bills = list(filter(lambda x: x >= 50, bills))
print (large_bills)
if __name__ == "__main__":
    exe_2()
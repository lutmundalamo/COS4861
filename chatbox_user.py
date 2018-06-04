import re, string,math

patterns = [(r"\b(i’m|i am)\b", "Hi "),
           (r"\w+ly", 'you feel strongly about this hey'),
            (r"\b(stupid)\b", "please be nice"),
            (r"^(19|20)\d\d([- /.])(0[1-9]|1[012])\2(0[1-9]|[12][0-9]|3[01])$", "Is this your date of birth?"),
            ( r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b", "perfect valid email"),
            (r"((\b[0-9]+)?\.)?[0-9]+\b", "That's my favourite number too"),
            ]

while True:
    comment = raw_input("Hello User")
    response = comment.lower()
    for pat, sub in patterns:
        response = re.sub(pat, sub, response)
    print response.upper()
    

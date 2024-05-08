def timeConversion(s):
    # Write your code here
    if s[-2] == "P":
        if int(s[0:2]) < 12:
            return str(int(s[0:2]) + 12) + s[2:8]
        else:
            return s[0:8]
    if s[-2] == "A":
        if int(s[0:2]) >= 12:
            if int(s[0:2]) > 9:
                return str(int(s[0:2]) - 12) + s[2:8]
            else:
                return "0" + str(int(s[0:2]) - 12) + s[2:8]
        else:
            return s[0:8]

print(timeConversion("12:02:22AM"))
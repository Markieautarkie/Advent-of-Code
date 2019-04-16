import hashlib # for MD5 encoding

# input and counter
input = "bgvyzdsv"
i = 0

# keep looping with the new md5 strings
# break when hex with amount of leading zeroes is detected
while True:
    i += 1
    md5 = hashlib.md5((input + str(i)).encode())
    if md5.hexdigest().startswith("000000"):
        print("The first number with the amount of leading zeroes is: " + str(i))
        break
def writeFile(text,number):
    data = text + "," + str(number) + "\n"
    filename = "ktest.csv"
    f = open(filename,"a")
    f.write(data)
    f.close()

if __name__ == "__main__":
    text = "text test"
    num = 12345
    writeFile(text,num)
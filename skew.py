
reader = open("input", "r")
writer = open("output", "w")

textlist = reader.readlines()
text = ""

for i in range(0, len(textlist)):
    text = text + textlist[i].strip()

skew = 0
skewlist = []
skewlist.append(skew)

for i in range(0, len(text)):
    char = text[i]
    if(char == 'C'):
        skew = skew - 1
    elif(char == 'G'):
        skew = skew + 1
    skewlist.append(skew)

msg = ""
skewlist.pop(0)
minimum = min(skewlist)

for i in range(0, len(skewlist)):
    if(skewlist[i] == minimum):
        msg = msg + str(i + 1) + " "

msg = msg[:-1]
writer.write(msg)

reader.close()
writer.close()

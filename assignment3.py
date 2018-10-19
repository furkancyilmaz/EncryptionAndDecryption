# BBM103 Introduction to Programming Lab 1 - Fall 2017 - Programming Assignment 3 Starter Code
import sys
'''
This program will save the human race if done properly, 
so please do your best to get 100 from this assignment. 
You can do it! :)
'''
# Opening the input files
hurap_file = open(sys.argv[1], "r")
schuckscii_file = open(sys.argv[2], "r")
virus_codes_file = open(sys.argv[3], "r")
# Mission 00: Decrypting the HuRAP
print("""*********************
     Mission 00 
*********************""", end="\n\n")
print("""--- hex of encrypted code ---
-----------------------------""", end="\n\n")

# Your code which calculates and prints out the hexadecimal representation
# of HuRAP goes here

diziencryptekullanilacak = []
dizihex=[]
complementler=[]
specialLine=""
def split_str(seq, chunk, skip_tail=False):
    lst = []
    if chunk <= len(seq):
        lst.extend([seq[:chunk]])
        lst.extend(split_str(seq[chunk:], chunk, skip_tail))
    elif not skip_tail and seq:
        lst.extend([seq])
    return lst
p=[]
def toTwosComplement(binarySequence):
    convertedSequence = [0] * len(binarySequence)
    carryBit = 1
    for i in range(0, len(binarySequence)):
        if binarySequence[i] == '0':
            convertedSequence[i] = 1
        else:
            convertedSequence[i] = 0
    if convertedSequence[-1] == 0:
            convertedSequence[-1] = 1
            return ''.join(str(x) for x in convertedSequence)
    for bit in range(0, len(binarySequence)):
        if carryBit == 0:
            break
        index = len(binarySequence) - bit - 1
        if convertedSequence[index] == 1:
            convertedSequence[index] = 0
            carryBit = 1
        else:
            convertedSequence[index] = 1
            carryBit = 0
    return ''.join(str(x) for x in convertedSequence)
while(1):
    b = hurap_file.readline()
    if not b:
        break
    if (b[0] != '1' and b[0] != '0'):
        specialLine = b
        continue
    bin_chunks = [b[8 * i:8 * (i + 1)] for i in range(len(b) // 8)]
    for j in bin_chunks:
        complementler.append(toTwosComplement(j))
    for i in bin_chunks:
        d=split_str(i,4)
        for j in d:
            if j == "0000":
                dizihex.append('0')
            if j == "0001":
                dizihex.append('1')
            if j == "0010":
                dizihex.append('2')
            if j == "0011":
                dizihex.append('3')
            if j == "0100":
                dizihex.append('4')
            if j == "0101":
                dizihex.append('5')
            if j == "0110":
                dizihex.append('6')
            if j == "0111":
                dizihex.append('7')
            if j == "1000":
                dizihex.append('8')
            if j == "1001":
                dizihex.append('9')
            if j == "1010":
                dizihex.append('A')
            if j == "1011":
                dizihex.append('B')
            if j == "1100":
                dizihex.append('C')
            if j == "1101":
                dizihex.append('D')
            if j == "1110":
                dizihex.append('E')
            if j == "1111":
                dizihex.append('F')
    hexString = "".join(dizihex)
    diziencryptekullanilacak.append(hexString)
    dizihex.clear()
    print(hexString)
print("""\n--- encrypted code ----
-----------------------""", end="\n\n")
dizidecryptekullanilacak=[]
x=[]
key=[]
value=[]
while 1:
    line = schuckscii_file.readline()
    if not line:
        break
    x=line.split("\t")
    key.append(x[0])
    value.append(x[1])
encryptFinalList=[]
for i in diziencryptekullanilacak:
    encrypt = split_str(i,2)
    for i in encrypt:
        for j in value:
            if(i==j):
                indis = value.index(j)
                encryptFinalList.append(key[indis])
    encryptFinalString = "".join(encryptFinalList)
    print(encryptFinalString)
    dizidecryptekullanilacak.append(encryptFinalString)
    encryptFinalList.clear()
# Your code which calculates and prints the encrypted character
# representation of HuRAP goes here
print("""\n--- decrypted code ---
----------------------""", end="\n\n")
asilMesaj=""
sayac1=-1
sayacüstMüAltmi=-1
specialLineNumber=specialLine[1:len(specialLine)-1]
x=toTwosComplement(specialLine[1:len(specialLine)-1])

if(specialLineNumber[0]=='0'):
    a=int(specialLineNumber,2)
    sayacüstMüAltmi=0
elif(specialLineNumber[0]=='1'):
    x=toTwosComplement(specialLineNumber)
    a = -int(x, 2)
    sayacüstMüAltmi=1
for j in key:
    sayac1 = sayac1 + 1
    if(j==dizidecryptekullanilacak[0][0]):
        originalChar = (a) % key.__len__()
        break
kaydirmaMiktari = originalChar
asilMesajDizi=[]
asilMesajVirusDizi=[]
for i in range(dizidecryptekullanilacak.__len__()):
    for j in dizidecryptekullanilacak[i]:
        asilMesaj=""
        sayac2 = -1
        sayacp=-1
        for p in key:
            sayacp=sayacp+1
            if (p == j):
                sayac2=key.index(j)
                sayac2kaydirmaMiktari=sayac2-kaydirmaMiktari
                if(sayac2kaydirmaMiktari>key.__len__()):
                    sayac2kaydirmaMiktari=sayac2kaydirmaMiktari%key.__len__()
                k=key[sayac2kaydirmaMiktari]
                asilMesajDizi.append(k)
    asilMesaj="".join(asilMesajDizi)
    asilMesajVirusDizi.append(asilMesaj)
    print(asilMesaj)
    asilMesajDizi.clear()
# Your code which decrypts and prints the
# HuRAP goes here
# Mission 01: Coding the virus
print("""\n*********************
     Mission 01 
*********************""", end="\n\n")
virusKey=[]
virusKey2=[]
virusValue=[]
virusValue2=[]
while 1:
    line = virus_codes_file.readline()
    if not line:
        break
    line=line.replace('\n','')
    x=line.split(":")
    virusKey.append(x[0])
    virusValue.append(x[1])
mesaj=""
syc1=-1
syc2=-1
str3=""
virusStrings=[]
for i in asilMesajVirusDizi:
    str1a = "".join(i)
    syc1=0
    for j in virusKey:
        syc1 = syc1 + 1
        if(j in i):
            str2a = str1a.replace(j,virusValue[syc1-1])
            index1 = asilMesajVirusDizi.index(i)
            asilMesajVirusDizi.remove(i)
            asilMesajVirusDizi.insert(index1,str2a)
            break
        else:
            continue
for i1 in asilMesajVirusDizi:
    str1b = "".join(i1)
    syc2=0
    for j1 in virusKey:
        indexKey = virusKey.index(j1)
        syc2 = syc2 + 1
        if (virusValue[indexKey] in str1b):
            continue
        if (j1 in i1):
            str2b = str1b.replace(j1, virusValue[syc2-1])
            index2 = asilMesajVirusDizi.index(i1)
            asilMesajVirusDizi.remove(i1)
            asilMesajVirusDizi.insert(index2, str2b)
            break
        else:
            continue
for i1 in asilMesajVirusDizi:
    str1b = "".join(i1)
    syc2=0
    for j1 in virusKey:
        indexKey = virusKey.index(j1)
        syc2 = syc2 + 1
        if (virusValue[indexKey] in str1b):
            continue
        if (j1 in i1):
            str2b = str1b.replace(j1, virusValue[syc2-1])
            index2 = asilMesajVirusDizi.index(i1)
            asilMesajVirusDizi.remove(i1)
            asilMesajVirusDizi.insert(index2, str2b)
            break
        else:
            continue

for i in asilMesajVirusDizi:
    print(i)
# Your code which transforms the original HuRAP and prints
# the virus-infected HuRAP goes here
# Mission 10: Encrypting the virus-infected HuRAP

print("""\n*********************
     Mission 10 
*********************""", end="\n\n")
print("""--- encrypted code ---
----------------------""", end="\n\n")
yeniDizi1=[]
hexOfEncryptedCode=[]
if(sayacüstMüAltmi==0):
    kaydirmaMiktari=-kaydirmaMiktari%key.__len__()
for i in asilMesajVirusDizi:
    str1 = "".join(i)
    for j in str1:
        for p in key:
            if(j==p):
               index=key.index(j)
               if (sayacüstMüAltmi == 0):
                    index2=index-kaydirmaMiktari
               elif(sayacüstMüAltmi == 1):
                    index2 = index + kaydirmaMiktari
               x=key[index2]
               yeniDizi1.append(x)
    str2="".join(yeniDizi1)
    print(str2)
    hexOfEncryptedCode.append(str2)
    yeniDizi1.clear()

# Your code which encrypts and prints the encrypted character
# representation of the virus-infected HuRAP goes here

dizi2=[]
binOfEncryptedCode=[]

print("""\n--- hex of encrypted code ---
-----------------------------""", end="\n\n")




# Your code which calculates and prints out the hexadecimal representation
# of virus-infected and encrypted HuRAP goes here

for i in range(hexOfEncryptedCode.__len__()):
    for j in hexOfEncryptedCode[i]:
       for p in key:
           if(j==p):
               index = key.index(p)
               y=value[index]
               dizi2.append(y)
    str2="".join(dizi2)
    print(str2)
    binOfEncryptedCode.append(str2)
    dizi2.clear()

print("""\n--- bin of encrypted code ---
-----------------------------""", end="\n\n")

binaryNumbers=[]
for i in range(binOfEncryptedCode.__len__()):
    for j in binOfEncryptedCode[i]:
        if j == "0":
            binaryNumbers.append('0000')
        if j == "0":
            binaryNumbers.append('0001')
        if j == "2":
            binaryNumbers.append('0010')
        if j == "3":
            binaryNumbers.append('0011')
        if j == "4":
            binaryNumbers.append('0100')
        if j == "5":
            binaryNumbers.append('0101')
        if j == "6":
            binaryNumbers.append('0110')
        if j == "7":
            binaryNumbers.append('0111')
        if j == "8":
            binaryNumbers.append('1000')
        if j == "9":
            binaryNumbers.append('1001')
        if j == "A":
            binaryNumbers.append('1010')
        if j == "B":
            binaryNumbers.append('1011')
        if j == "C":
            binaryNumbers.append('1100')
        if j == "D":
            binaryNumbers.append('1101')
        if j == "E":
            binaryNumbers.append('1110')
        if j == "F":
            binaryNumbers.append('1111')
    str2 = "".join(binaryNumbers)
    print(str2)
    binaryNumbers.clear()
# Your code which calculates and prints out the binary representation
# of virus-infected and encrypted HuRAP goes here
# Closing the input files
hurap_file.close()
schuckscii_file.close()
virus_codes_file.close()

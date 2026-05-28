from collections import Counter

inputA = ['anagram', 'magrana']
imputB = ['rat', 'car']
inputC = ['natan', 'natan']
inputD = ['', 'a']
inputE = ['avb', 'adf']

def isAnagram(string1, string2):
    if len(string1) != len(string2): 
        return False
    
    charFrequency1 = {}
    charFrequency2 = {}

    for char in string1:
        charFrequency1[char] = charFrequency1.get(char, 0) + 1
    
    for char in string2:
        charFrequency2[char] = charFrequency2.get(char, 0) + 1

    print('Hashtables: ',charFrequency1, charFrequency2 )

    return charFrequency1 == charFrequency2

def isAnagramWithCounter(string1, string2):
    return Counter(string1) == Counter(string2)


print('inputA isAnagram', isAnagram(inputA[0], inputA[1]))
print('imputB isAnagram', isAnagram(imputB[0], imputB[1]))
print('inputC isAnagram', isAnagram(inputC[0], inputC[1]))
print('imputD isAnagram', isAnagram(inputD[0], inputD[1]))
print('inputE isAnagram', isAnagram(inputE[0], inputE[1]))
print('inputA isAnagramWithCounter', isAnagramWithCounter(inputA[0], inputA[1]))
print('imputB isAnagramWithCounter', isAnagramWithCounter(imputB[0], imputB[1]))
print('inputC isAnagramWithCounter', isAnagramWithCounter(inputC[0], inputC[1]))
print('inputD isAnagramWithCounter', isAnagramWithCounter(inputD[0], inputD[1]))
print('inputE isAnagramWithCounter', isAnagramWithCounter(inputE[0], inputE[1]))

# // There is a string, , of lowercase English letters that is repeated 
# // infinitely many times. Given an integer, , find and print the 
# // number of letter a's in the first  letters of the infinite string.
# // Example
# // The substring we consider is , the first  characters of the infinite 
# // string. There are  occurrences of a in the substring.

# // Function Description

# // Complete the repeatedString function in the editor below.
# // repeatedString has the following parameter(s):

# // s: a string to repeat
# // n: the number of characters to consider
# // Returns

# // int: the frequency of a in the substring
# // Input Format

# // The first line contains a single string, .
# // The second line contains an integer, 

Input = dict[str, int]
input: Input= {
    's': 'aba',
    'n': 10,
}

def repeatedAs(input: Input) -> int:
    # calculate the number of loops to achieve the total string
    numberOfLoops = input['n'] // len(input['s'])
    # track count of As in s
    asInS = input['s'].count('a')
    # track As in rest
    restChars =  input['n'] % len(input['s'])
    asInRest = input['s'][:restChars].count('a')

    
    return numberOfLoops * asInS + asInRest

print(repeatedAs(input))

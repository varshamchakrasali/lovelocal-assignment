#You are given a string s. You can convert s to a palindrome by adding characters in front of it.Return the shortest palindrome you can find by performing this transformation
def shortestPalindrome(s):
       
        def kmp(text, pattern):
            string = pattern + '#' + text
            #longest prefix suffix table
            lps = [0] * len(string)
            #i=1(pointer to current element)
            #because for i=0, lpsvalue will be 0
            #length: previous lps value
            i,length = 1,0

            while i<len(string):
                if string[i]==string[length]:
                    length+=1
                    lps[i] = length
                    i += 1
                else:
                    if length>0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps[-1]  
        cnt = kmp(s[::-1],s)
        return s[cnt:][::-1] + s      

string = input("Enter the string: ")
print(shortestPalindrome(string))
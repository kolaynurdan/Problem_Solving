#There is a sequence of words in CamelCase as a string of letters,s, having the following properties:
#It is a concatenation of one or more words consisting of English letters.
#All letters in the first word are lowercase.
#For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
#Given s , determine the number of words in s .
def camelCase(s):
  res=1
  for let in s:
    if let.isupper():
      res+=1
  if not s:
    res=0
  return res

if __name__=="__main__":
  s=input().strip()
  result=camelCase(s)
  print(result)

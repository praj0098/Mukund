n=input()
if((n>='a' and n<='z') or (n>='A' and n<='Z')):
  n=n.lower()
  if(n=='a' or n=='e' or n=='i' or n=='o' or n=='u'):
     print("Vowel")
  else:
     print("Consonant")
else:
    print("Invalid")

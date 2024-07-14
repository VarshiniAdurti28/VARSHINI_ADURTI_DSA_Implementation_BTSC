import hashlib

def Alice(text):
  
  hash_fnAlice = hashlib.sha256()

  hash_fnAlice.update(text)

  hashAlice= hash_fnAlice.hexdigest()
 
  return [hashAlice, text]


def Verify(text):

  values=Alice(text)
  
  hash_Alice=values[0]
  textAlice=values[1]

  hash_fnBob = hashlib.sha256()
  
  hash_fnBob.update(textAlice)

  hash_Bob = hash_fnBob.hexdigest()

  if(hash_Alice==hash_Bob):
    print("Transmission Not tampered\n")

  else:
    print("The hashes are different\n")



inp=b"Hello, How Are You?"

Verify(inp)





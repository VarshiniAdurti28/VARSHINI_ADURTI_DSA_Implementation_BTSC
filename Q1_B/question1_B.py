import hashlib

def Alice(text):
  
  hash_fnAlice = hashlib.sha256()


  hash_fnAlice.update(text)

  hashAlice= hash_fnAlice.hexdigest()

  return hashAlice


def Bob(text):

  hash_fnBob = hashlib.sha256()


  hash_fnBob.update(text)

  hashBob = hash_fnBob.hexdigest()

  return hashBob


input=b"Hello, How Are You?"
hash_Alice= Alice(input)
hash_Bob= Bob(input)

if(hash_Alice==hash_Bob):
  print("Transmission Not tampered\n")

else:
  print("The hashes are different\n")





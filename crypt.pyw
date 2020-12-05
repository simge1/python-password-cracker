import crypt
def testPass(cryptPass):
    salt=cryptPass[0:2]
    
    dictFile=open('dictionary.txt','r')
    for word in dictFile.readlines():
        word=word.strip("\n")
        cryptWord=crypt.crypt(word,salt)
        if cryptPass==cryptWord:
            print("Found Password: "+word)
            return
        else:
            print ("Password Not Found")
            return
           
    
def main():
    passFile=open('passwords.txt')
    for line in passFile.readlines():
            if ":" in line:
                 user=line.split(':')[0]
                 cryptPass=line.split(':')[1].rstrip("\n")
                 print ("[*] Cracking Password For: "+user)
                 testPass(cryptPass)
        
if __name__=="__main__":
        main()


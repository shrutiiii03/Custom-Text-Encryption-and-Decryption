import random 

def insert(str,n):
    before=''
    for i in range(0,n):
     before+=''.join(random.choice('abcdefghijklmnopqrstuvwxyz'))
    
    after=''
    for i in range(0,n):
     after+=''.join(random.choice('abcdefghijklmnopqrstuvwxyz'))

    return before+str+after



#encryption
def encrytion(a,words):
        final=[]
        for word in words:
            if len(word) < 4:
                rev=word[::-1]
                final.append(rev)
            else:
                word=word[1:]+word[0]
                a=insert(word,3)
                final.append(a)
        strs=" ".join(final)
        return strs
        #print("encrypted msg is ",str)



def decryption(a,words):
        final=[]
        
        for word in words:      
            if len(word) < 4:
                rev=word[::-1]
                final.append(rev)
            else:
                word=word[3:-3]
                newmsg=word[-1]+word[:-1]
                final.append(newmsg)
        str=" ".join(final)
        return str
        #print("decrypted msg is", str)       


msg=input("enter the message")
words=msg.split()
a=int(input("enter 1 for encryption 2 for decryption"))    
print(encrytion(a,words)) if a==1 else print(decryption(a,words)) if a==2 else print("wrong input")
 


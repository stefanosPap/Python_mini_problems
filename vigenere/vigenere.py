class VigenereCipher(object):
    
    def __init__(self, key, alphabet):
        #initializations 
        self.key = key
        self.alphabet = alphabet
        #create a dictionary in order to access our alphabet easily 
        self.dict = {}
        for i in range(len(self.alphabet)):
            self.dict.update({self.alphabet[i] : i}) 
    
    #method for encode plaintext
    def encode(self, text):
        i = 0
        comparison = "" #in comparison we keep the key repeatedly to correspond to each letter of the ciphertext
        length = len(text)
        
        while i < length:
            comparison += self.key
            i += len(self.key)  
        
        comparison = comparison[:length]
        key_list = list(self.dict.keys())
        val_list = list(self.dict.values())
        
        encode = ""
        for i in range(len(text)):
            if text[i] in self.alphabet: #if the current letter belongs to our alphabet then we apply caesar algorithm 
                up = (self.dict[text[i]] + self.dict[comparison[i]]) % len(self.alphabet)
                encode += key_list[val_list.index(up)]
            else: #else we keep it as it is 
                encode += text[i]
                
        return encode
    #method for decode ciphertext 
    def decode(self, text):
        i = 0
        comparison = ""
        length = len(text)
        
        while i < length:
            comparison += self.key
            i += len(self.key)  
        
        comparison = comparison[:length]
        key_list = list(self.dict.keys())
        val_list = list(self.dict.values()) 
        #------the procedure is the same as in the encode method till here------ 
        
        decode = ""
        for i in range(len(text)):#for each element
            
            if text[i] in self.alphabet: #if the current letter belongs to our alphabet 
                up = self.dict[text[i]] - self.dict[comparison[i]] #subtract the value of the key in order to take the initial value 
                if up < 0: #if up negative then we subtract thiw negative value from the number of alphabet's elements 
                    up = len(self.alphabet) + up 
                decode += key_list[val_list.index(up)]
            else:
                decode += text[i]
        return decode

#test
c = VigenereCipher('password','abcdefghijklmnopqrstuvwxyz')
cipher = c.encode("my secret code i want to secure")
print(c.decode(cipher))
import caesar_art

#welcome function
def welcome():
  print(caesar_art.logo)
  print("Welcome to Caeser Cipher Program.")
  
#Caeser function
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(start_text, shift_amount, cipher_direcction):
  end_text = ""
  
  #If decode?
  if cipher_direcction == "decode":
    #change shift amount
    shift_amount *= -1
  
  #Loop now
  for char in start_text:
    
    if char in alphabet:
    
      #find the index of the letter in alphabet list
      position = alphabet.index(char)
      
      #get new position
      newp = position + shift_amount
      
      #obtain new letter and add to end_text
      end_text += alphabet[newp]
    
    else:
      end_text += char
  
  print(f"The {cipher_direcction} text is {end_text}.")

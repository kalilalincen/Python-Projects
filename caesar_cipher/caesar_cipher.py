import caesar_art
import caesar_functions
  
#Main function
caesar_functions.welcome()

#Pre-define 
end_game = False

while end_game == False:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #prevent out of range
  shift = shift%26

  #Call function
  caesar_functions.caeser(start_text=text, shift_amount=shift, cipher_direcction=direction)

  #Again or exit?
  again = input("\nType 'yes' if you wish to try again. Otherwise, type 'no' to exit the program.\n")
  if again == "no":
    print("\nYou have exited the program.")
    end_game = True
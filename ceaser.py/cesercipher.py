import ceaser
print("-----------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------")
print(ceaser.logo)
print("-----------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------")
j = 0
while j == 0:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message: \n")
    shift_number = int(input("Type the shift number: \n"))
    letters_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if shift_number >= len(letters_list):
        shift_number = shift_number%26
    if choice == "encode":
        ceaser.encrypt(message=message,shift=shift_number,list=letters_list)
    elif choice  == "decode":
        ceaser.decrypt(message=message,shift=shift_number,list=letters_list)
    j = int(input("Enter '0' to go again, Otherwise type '1' to exit:\n"))
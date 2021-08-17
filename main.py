emails=[]

#Asking the user whether he/she has a middle name
Middlename_Answer=input("Do you have a middle name? Y/N \n ")
Middlename_Answer= Middlename_Answer.upper() #converting answer to uppercase to 
                                            #ensure that

firstName = input("Enter your first name: ") #obtaning middle name
lastName = input("Enter your last name: ")  #obtaining last name

"\n"

new_email = ' ' #holds newly formed email address

if Middlename_Answer == 'Y':
    middleName = input("Enter your middle name: ")
    new_email = (firstName[0] + middleName[0]+lastName).lower() + "@organization.edu"
    
else:
    new_email = (firstName[0]+lastName).lower() + "@organization.edu"
    
counter = 0
indexA = new_email.index('@')
insertionpoint = indexA-1 # Point where to insert an integer to distinguish
                          # Same email addresses

counter = 0

#Checking whether there are similar
#emails in the email repository that are the 
#same as the email created

for email in emails:
    while new_email == email:
        counter = counter + 1
        
        new_email =new_email[0:indexA-1] + str(counter)
        
        
    
print(new_email)
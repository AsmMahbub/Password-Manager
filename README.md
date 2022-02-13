# Password-Manager
n this project I use python to store username and passwords and encrypt that information on a separate file. Users can run the the code to add more login information or by using a master password they can view the decrypted version of their password.

The reason I'm creating this project is because as we progress and time goes on, we will have more and more applications and devices. In all of them we want privacy and security, that's why we set up secure passwords. Even now people have lists  of passwords that can be stolen or lost and cause them a security risk. So I wanted to create a password manager that would locally store your sensitive information and encrypt them for added security.

The process for this code is simple:
1)Ask the user for the master password
2)Ask them if they would like to add new info, view their current ones or quit the application
2a)If they want to add the information, they will be prompted to add an username and password which all then automatically get encrypted and saved on a file
2b)If the user wishes to view their username and passwords, the program will take the information for the said file and decrypt them and display it on the terminal but only if the master password was correct otherwise it will prompt you to quit the program
2c)If the user wishes to quit then the program will close

Some ways I plan to further improve this project is making it an application people can download from a website, create another option for users to indicate what the login is for and encrypt the username as well for added security.

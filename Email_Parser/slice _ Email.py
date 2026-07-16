name =input("What\'s your name?").capitalize().strip()
email =input("What\'s your Email?").strip()

username = email[:email.index("@")]
userwebsite = email[email.index("@") +1:]

print(f'Hello {name} Your Email Is {email}')
print(f'your user name {username} \n your email {userwebsite}')

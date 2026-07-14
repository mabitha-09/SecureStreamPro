from cryptography.fernet import Fernet

# we will be encrypting the below string.
message = "hello geeks"



'''key = Fernet.generate_key()


print(key)

fernet = Fernet(key)



encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)'''


#b'gAAAAABjpFbJFmuLFeWZdXzQNSrqEbstMMr2JDUjc7vIbHWU8_n8-N4pNU4mLUiLFHqhfH08VI0L_WYJkPUDFWSILtCJv5IrzKxk_GkrjbGT6kkUnPpcQ8a-0mnjV-EIt0sNJIC-PyHJf98cmEfoAozNRgkdgtbMQE8IIjxor-3h0czxU8p2eb
#b'-ap-4b6wnae6XQPxldpzBU7k3nNWJLus5W3nzIiB5K0='

key = b'-ap-4b6wnae6XQPxldpzBU7k3nNWJLus5W3nzIiB5K0='
fernet = Fernet(key)


encMessage=b'gAAAAABjpFbJFmuLFeWZdXzQNSrqEbstMMr2JDUjc7vIbHWU8_n8-N4pNU4mLUiLFHqhfH08VI0L_WYJkPUDFWSILtCJv5IrzKxk_GkrjbGT6kkUnPpcQ8a-0mnjV-EIt0sNJIC-PyHJf98cmEfoAozNRgkdgtbMQE8IIjxor-3h0czxU8p2eb=='
decMessage = fernet.decrypt(encMessage).decode()
print("decrypted string: ", decMessage)



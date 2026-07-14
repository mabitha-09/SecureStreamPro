from stegano import lsb
import os
'''secret = lsb.hide("./static/images/123.jpg", "b'gAAAAABjoxpdAWbVeiG5iqgzu8yOyluLIf1FmImZMjoTNF7CX4ll5X4dbyeS6nSQ3T3xWuo7diQUc2F-YGa28yalOhvXLU3CdA=='")

pathname, extension = os.path.splitext('./static/images/123.jpg')
filename = pathname.split('/')

print(filename[-1])

secret.save("./static/Encode/123.png")'''



clear_message = lsb.reveal("./static/Decode/78976.png")
print(clear_message)


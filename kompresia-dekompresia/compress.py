import base64
import zlib

with open ("text.txt", "r") as myfile:
    data=myfile.read()
    
data = bytes(data,"utf-8")
compressed_data = zlib.compress(data)
compressed_data_base64 = base64.b64encode(compressed_data)

decoded_data =  compressed_data_base64.decode("utf-8")
with open("compressed.txt", "w") as myfile:
    myfile.write(decoded_data)

print("File compressed and saved as compressed.txt")
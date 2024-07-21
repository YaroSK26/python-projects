import base64
import zlib

with open("compressed.txt", "r") as myfile:
    compressed_data_base64 = myfile.read()

compressed_data = base64.b64decode(compressed_data_base64)

decompressed_data_bytes = zlib.decompress(compressed_data)
decompressed_data = decompressed_data_bytes.decode("utf-8")

with open("decompressed.txt", "w") as myfile:
    myfile.write(decompressed_data)
    
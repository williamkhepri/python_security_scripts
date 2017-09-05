#!/usr/bin/python
code = raw_input("Introduce los datos que quieres codificar a Base64:")
answer=code.encode('base64','strict')
print answer

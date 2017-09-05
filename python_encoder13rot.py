#!/usr/bin/python
code = raw_input("Introduce los datos para codificar en Base64 (Rot13)")
answer=code.encode('rot13','strict')
print answer

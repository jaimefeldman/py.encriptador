import gen_pass
import re

# print("clave generada: ", gen_pass.genpass(20))
print("password: ",re.sub(r'((?:(?=(10|.))\2){4})(?!$)', r'\1-',gen_pass.genpass(16)))

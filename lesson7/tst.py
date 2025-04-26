import os
import re
print(dir(os))

"+7(9NN)NNN-NN-NN"

a = '+7(911)555-55-55'

r = r"\+7\(9\d{2}\)\d{3}-\d{2}-\d{2}"
r2 = r"\+7\(9\d{2}\)\d{3}[-\d]{6}"
print(re.findall(r2, a))



# hiko's first python test

import random


class random_test:
	def __init__(self, start, end, code_index, code_str):
		self.code_index = code_index
		self.code_str = code_str
		self.code_index = [chr(i) for i in range(start, end)]
		random.shuffle(self.code_index)
		self.code_str = "".join(self.code_index)

o = object
print ("hello world!")
print (o)

#code_index = [chr(i) for i in range(97, 124)]
#random.shuffle(code_index)
#code_str = "".join(code_index)
code_index = 0;
code_str = ""
rt = random_test(97, 124, code_index, code_str)



print()
print(rt.code_str)

print("=== THE END ===")




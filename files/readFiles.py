import pdb

sample_file = "./files/sample.txt"
with open (sample_file,'r') as file:
   content = file.read()
   print(content)
file.close()


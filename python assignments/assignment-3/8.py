"""output to this question can vary as it depends how we have copied the data in testfile.txt from the data provided
for it in the whatsapp message"""
import os
print(os.stat('test.txt').st_size)
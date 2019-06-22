# Write to file

f = open('write.txt', 'a')
f.write('hello all')
f.close()

# Remove file
import os
os.remove('write.txt')
# Reading file


#############################################
############ Simple file reading ############
#############################################
f = open('hello.txt')
data = f.read()

print('my data:', data)
print('my data type:', type(data))



#############################################
########### Simple data cleaning ############
#############################################

# Main Goal: To transform our text file data into a list of 10 numeric value

# Reading line by line
f = open('hello.txt')
raw_data = f.readlines()
print('raw_data:', raw_data)

# data cleaning step 1
clean_data = []
for x in raw_data:
    clean_data.append(x.strip('\n'))
print('clean_data:', clean_data)

# data cleaning step 2
numeric_data = []
for x in clean_data:
    y = x.split(' ')
    print('what is y?' ,y)
    numeric_data.extend(y)
print('what is numeric data?', numeric_data)

# convert string data to numeric
numeric_data = [int(x) for x in numeric_data]
print('what is numeric_data after conversion?', numeric_data)





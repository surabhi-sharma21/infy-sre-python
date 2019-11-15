path = '/Users/mehulc/Documents/requirements.txt' # absolute path

fp = open(path) # by default mode = 'rt'
''' print(fp)
print(type(fp)) '''

image_path = '/Users/mehulc/Documents/sample.png'
fi = open(image_path, mode='rb')
''' print(fi)
print(type(fi)) '''

print('Reading for the first time')
# read from the text file
for line in fp:
    print(line.rstrip()) # while reading from text file, reads line with a \n

print('Reading for the second time')
# reading from a file is pointer sensitive
# the previous read operation got the internal file pointer to the EOF
for line in fp:
    print(line.rstrip())

# reset the pointer to start of the file
fp.seek(0)
print('Reading for the third time')
for line in fp:
    print(line.rstrip())

fp.seek(0)

# read all the lines from the file in one shot
print('Reading for the fourth time')
lines = fp.readlines()
print(lines)
print(type(lines))
for line in lines:
    print(line.rstrip())

fp.seek(0)

# read all the contents in a string in one shot
print('Reading for the fifth time')
contents = fp.read()
print(contents.rstrip())
print(type(contents))

fp.seek(0)

# close the connection to the file resource once done
fp.close()
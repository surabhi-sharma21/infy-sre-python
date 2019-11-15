path = '/Users/mehulc/Documents/requirements.txt' # absolute path

with open(path) as fp:
    for line in fp:
        print(line.rstrip())

# once the program flows out of the with block, the fp will be automatically closed
# avoids we giving a manual .close()
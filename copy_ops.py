from pathlib import Path
from shutil import copy

source_path = input('Enter source path: ')
destination_path = input('Enter destination path: ')
sobj = Path(source_path)
dobj = Path(destination_path)

if sobj.exists() and dobj.exists():
    if sobj.is_file():
        if dobj.is_dir():
            copy(source_path, destination_path)
            print('Copying done')

            ''' source_file_name = sobj.name
            with open(source_path) as fs:
                with open(destination_path + '/' + source_file_name, mode='wt') as fw:
                    for line in fs:
                        fw.write(line)
                    print('Copying done') '''
        else:
            print('Destination path must be an existing directory')
    else:
        print('Source path must be a file')
else:
    print('Source/Destination path does not exist')
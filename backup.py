# -*- coding: UTF-8 -*-
import os
import time
import sys
import zipfile
import string

parameter = ['-v', '-q']
target_dir = 'D:\\Backup'
source = [
r'd:/document/unity.md',
r'd:/Outlook.pst'
]

# if the Backup directory is not exists, creat it
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# subdirectories name and filename
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

# apart argv to set
input_parameter = set(sys.argv[1:]) & set(parameter)
input_filename = set(sys.argv[1:]) - set(parameter)

# append input filename to source
[source.append(s) for s in input_filename]

# add comment with filename
if '-q' in input_parameter:
    comment = ''
else:
    comment = raw_input('Enter a comment -->')

# full target zip filename
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# if the subdirectories is not exists, creat it
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory', today

# creat zipfile handle
zf = zipfile.ZipFile(target, mode = 'a')

try:
    # make windows drive unified and source file unique
    # write zip files
    [zf.write(n) for n in set(string.capitalize() for string in source)]
finally:
    # close file
    zf.close()

if '-v' in input_parameter:
    print 'Successful backup to', target


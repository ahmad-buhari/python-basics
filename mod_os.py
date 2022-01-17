#Exercise with os

import os

p = os.path.join('/home','ahmad','Documents')
print(p)

if os.path.exists(p):
    print('path exist')
    print('Folder size:',os.path.getsize(p),'bytes')
else:
    print('Invalid path')

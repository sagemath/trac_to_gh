# Issue 129: relocation problem

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2006-10-14 05:35:46

Assignee: was

When you build a sage tree at one location and then move it to another location, introspection is broken. Example:

NumberField?

would still quote an absolute file name in the old location and

NumberField??

would fail.



---

Comment by was created at 2006-10-14 07:07:19

This is trac #81.


---

Comment by was created at 2006-10-14 07:07:19

Resolution: duplicate


---

Comment by was created at 2006-10-15 17:11:24

This is now fixed.  I fixed it by creating the script below and calling
it from the sage_setup() section of sage-sage:


```/usr/bin/env sage.bin

import os

SAGE_ROOT = os.environ['SAGE_ROOT']

location_file = '%s/local/lib/sage-current-location.txt'%SAGE_ROOT

def install_moved():
    if not os.path.exists(location_file) or open(location_file).read() != SAGE_ROOT:
        open(location_file,'w').write(SAGE_ROOT)
        return True
    return False

def update_hardcoded_files(path):
    # The only known files with hard coded paths.
    if os.path.isdir(path):
        for X in os.listdir(path):
            update_hardcoded_files('%s/%s'%(path,X))
    else:
        P = path[-4:]
        if P == '.pyo' or P == '.pyc':
            try:
                os.unlink(path)
            except OSError, msg:
                print msg

if __name__ ==  '__main__':
    # Check if SAGE has moved, and if so delete all .pyo and .pyc files
    # in the python libs directory, so they are rebuilt. 
    if install_moved():
        print "The SAGE install tree may have moved."
        print "Regenerating files that hardcode the install PATH (please wait a few seconds)..."
        update_hardcoded_files(SAGE_ROOT + '/local/lib/python/')
```


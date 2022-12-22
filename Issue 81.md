# Issue 81: directory paths hardcoded into .pyc installed files. (?)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-24 16:11:01

Assignee: was


```
But I'm somewhat
surprised, it's specified, in the "SAGE Installation Guide", that "The
directory where you built SAGE is NOT hardcoded into any part of SAGE."
but it's not possible to see the source code of a function if you moved
SAGE after the build. Same thing when an error is reported, for example:
 
===========================================================================
R = PolynomialRing(QQ)
factor(R)
---------------------------------------------------------------------------
exceptions.TypeError                                 Traceback (most
recent call last)
 
/usr/local/sage-test/<ipython console> 
 
/usr/local/sage/local/lib/python2.4/site-packages/sage/rings/arith.py in
factor(n, proof, int_, algorithm, verbose)
 
TypeError: unable to factor n
 
============================================================================
but here, the path to sage is /usr/local/sage-test. Do I have to report
this as a bug ?
 
Greg
```



---

Comment by was created at 2006-10-14 06:57:25


```
>  - When you relocate the tree, source lookup fails badly: I tried
> NumberField?? and it complained it couldn't find the source --
> NumberField? shows the old source file name, so these paths seem to get
> compiled in hard.

This is a known problem.  Fixing this is high on the list.  Probably
the solution will be just to check if the tree has moved on startup,
and if so to delete the 
    <SAGE_ROOT>/devel/sage/build 
directory.  Doing so should update the paths.

 -- William
```



---

Comment by was created at 2006-10-15 07:58:11

The solution will be to detect that SAGE_ROOT has changed (we should save the last known SAGE_ROOT somewhere). If so, recursively delete all .pyc and .pyo files from the python/site-packages directories.  This will fix the problem completely, since those
get safely generated on restart.


---

Comment by was created at 2006-10-15 17:12:41

Resolution: fixed


---

Comment by was created at 2006-10-15 17:12:41

Fixed with the following script being called from the sage_setup
function in local/bin/sage-sage.



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


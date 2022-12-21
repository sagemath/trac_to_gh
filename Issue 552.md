# Issue 552: come up with a better way of deciding whether or not the SAGE install has moved

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-01 16:55:28

Assignee: was

All too often, because of symlinks, etc., my script for detecting whether or not the SAGE install
tree has moved gets it wrong.  This is frickin' annoying.  I would like a way to determine this
that is much more intelligent. 

The relevant code is SAGE_ROOT/local/bin/sage-location:
{{{#!/usr/bin/env sage.bin

import os

SAGE_ROOT = os.environ['SAGE_ROOT']

location_file = '%s/local/lib/sage-current-location.txt'%SAGE_ROOT

def install_moved():
    if not os.path.exists(location_file):
        O = open(location_file,'w')
        O.write(SAGE_ROOT)
        O.close()
        return False, ''   # first time -- so no need to update; this was during the build.

    O = open(location_file)
    R = O.read().strip()
    O.close()
    if os.path.abspath(R) != os.path.abspath(SAGE_ROOT):  # really different
        return True, R  # it moved
    return False, ''
```


Any better ideas???


---

Comment by craigcitro created at 2007-09-07 05:27:52

Changing component from algebraic geometry to packages.


---

Comment by mabshoff created at 2008-09-26 09:24:53

We can use the shell program "readlink" since that follows symbolic links and friends. We already use it in the sage script to determine the actual location of the sage script.

Cheers,

Michael


---

Attachment

os.path.realpath() takes care of symlinks.

It's that simple folks.


---

Comment by mabshoff created at 2008-10-31 21:27:13

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-31 21:30:19

Resolution: fixed


---

Comment by mabshoff created at 2008-10-31 21:30:19

Merged in Sage 3.2.alpha2

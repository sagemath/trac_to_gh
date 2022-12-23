# Issue 1720: [with spkg] update numpy to 1.0.4, also fix silent build problems with gfortran

Issue created by migration from https://trac.sagemath.org/ticket/1720

Original creator: jkantor

Original creation time: 2008-01-08 10:05:30

Assignee: mabshoff

This updates the numpy package to the latest version 

http://sage.math.washington.edu/home/jkantor/spkgs/numpy-20080104-1.0.4.spkg

(note I have removed a section of the spkg-install that was allowing numpy to build without
atlas if the inital build didn't work. I saw that this was happengin when using gfortran. I think I fixed the initial problem but this may cause build failures that were going unnoticed to become manifest. I want to know so I can fix them.)


---

Comment by mabshoff created at 2008-01-08 23:54:16

An updated spkg with SPKG.txt and hg repo added is at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha1/numpy-20080104-1.0.4.p0.spkg

Cheers,

Michael


---

Comment by jkantor created at 2008-01-09 00:40:22

Added detailed information to SPKG.txt


http://sage.math.washington.edu/home/jkantor/spkgs/numpy-20080104-1.0.4.p1.spkg


---

Comment by mabshoff created at 2008-01-09 01:57:47

I updated the SPKG.txt with a changelog entry, removed `*~` from the spkg and updated `.hgignore`. The updated spkg with the same name as Josh's last one linked above is at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha1/numpy-20080104-1.0.4.p1.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-09 01:57:47

Resolution: fixed

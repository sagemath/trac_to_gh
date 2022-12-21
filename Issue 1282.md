# Issue 1282: make flint.spkg depend on python

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-26 20:25:01

Assignee: mabshoff


```
The thing to do is to change the sage build process so that building
FLINT depends on
having already built Python.    Then python-2.5.1 -- built by sage -- will get
used if you put
  #!/usr/bin/env python
at the top of a script or whatever.  I.e., it will be in your path.

I hadn't realized that building flint required Python, so we didn't
put that as a dependency
in the overall Sage makefile.

william
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-11-26 20:25:07

Changing status from new to assigned.


---

Comment by pdenapo created at 2007-12-03 20:03:53

Script started on Mon Dec  3 14:08:30 2007
When trying to build sage-2.8.15 under Slackware Linux, the build broke with the following messages:

/sage/sage-2.8.14/spkg/build/flint-0.9-r1075.p1/src
bash-3.1# make
python make-profile-tables.py fmpz_poly
/usr/bin/python: /usr/bin/python: cannot execute binary file
make: *** [fmpz_poly-profile-tables.o] Error 126
bash-3.1# exit
exit

Actually, I had a broken symlink /usr/bin/python (to python2.4) , but no python was
really installed the system. 

It seems that flint tries to use python from the system, instead of the version 
included in Sage.


---

Comment by was created at 2007-12-04 06:48:25

I made the 10 character change...


---

Comment by was created at 2007-12-04 06:48:25

Resolution: fixed

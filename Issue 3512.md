# Issue 3512: [with spkg, needs review] upgrade to sqlalchemy 0.4.6

Issue created by migration from https://trac.sagemath.org/ticket/3512

Original creator: yi

Original creation time: 2008-06-25 21:51:23

Assignee: yi

CC:  jvoight

John Voight ran into a problem running dsage that is caused by a bug in the version of sqlalchemy (0.4.3) we ship. The latest upstream stable version is 0.4.6. 
All dsage unit tests pass with the new sqlalchemy installed, and I think dsage is the only package using sqlalchemy currently.

Here is the new spkg:

http://sage.math.washington.edu/home/yqiang/spkgs/sqlalchemy-0.4.6.p0.spkg

I commented out copying the documentation since it's readily available online, and I saw very little else in $SAGE_ROOT/local/doc. Feel to uncomment that if need be. 


---

Comment by mabshoff created at 2008-06-26 03:10:36

Positive review. I added a line to delete old SQLAlchemy installs.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-26 03:10:36

Changing assignee from yi to mabshoff.


---

Comment by mabshoff created at 2008-06-26 03:10:36

Changing component from dsage to packages.


---

Comment by mabshoff created at 2008-06-26 03:10:51

Resolution: fixed


---

Comment by mabshoff created at 2008-06-26 03:10:51

Merged in Sage 3.0.4.alpha1

# Issue 4848: [with patch, needs review] Remove deadwood: sage/schemes/elliptic_curves/heegner.py

Issue created by migration from https://trac.sagemath.org/ticket/4848

Original creator: mabshoff

Original creation time: 2008-12-21 16:19:30

Assignee: mabshoff

CC:  wstein

The file sage/schemes/elliptic_curves/heegner.py is mainly some comments and a bunch of Magma code. I don't see anything useful in there, so let's get rid of it.

Long doctests pass with the file and its copies removed from build.

Cheers,

Michael


---

Attachment

The file is also from 2005 and hasn't been touched for ages:

```
changeset:   1097:e9c1649fcc14
user:        wstein@gmail.com
date:        Fri Sep 01 02:31:25 2006 +0000
summary:     [project @ wstein@ucsd.edu --> wstein@gmail.com (hundreds of changes)]

changeset:   0:039f6310c6fe
user:        tornaria@math.utexas.edu
date:        Sat Feb 11 01:13:08 2006 +0000
summary:     [project @ original sage-0.10.12]
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-12-21 16:23:22

Changing status from new to assigned.


---

Comment by mhampton created at 2008-12-21 16:35:01

Changing priority from major to minor.


---

Comment by mhampton created at 2008-12-21 16:35:01

This is all magma code.  If it does something useful then it should be moved upstream or perhaps put in an optional spkg.  Since its William Stein's code perhaps he could bless its removal...


---

Comment by was created at 2008-12-21 17:52:19

What should happen is that there should be a new *enhancement* ticket that is called "add functionality for computing Heegner points to Sage".   Then the file heegner.py should be attached to that ticket, since to do that ticket, one might want to port some of what's in there to Sage.   That said, it's not so simple, since better algorithms for computing Heegner points were found after that code was written. 

So I am OK with this ticket if and only if the above enhancement ticket is created.


---

Comment by mabshoff created at 2008-12-21 22:11:06

Replying to [comment:3 was]:

> So I am OK with this ticket if and only if the above enhancement ticket is created. 

See #4849.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-21 22:13:52

Merged in Sage 3.2.3.alpha0


---

Comment by mabshoff created at 2008-12-21 22:13:52

Resolution: fixed

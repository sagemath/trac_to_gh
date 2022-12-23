# Issue 8180: sh: kpsewhich: not found reported on 4.3.0.1.alpha3 on Solaris 10.

Issue created by migration from https://trac.sagemath.org/ticket/8180

Original creator: drkirkby

Original creation time: 2010-02-03 20:06:36

Assignee: drkirkby

CC:  mvngu jsp

Minh created a 4.3.0.1.alpha3 which should have really been called 4.3.0.2.alpha3, as it was based on the 4.3.0.1 sources, with patches applied. It was  created to sort out what broke the Sage build between 4.3.0 and 4.3.1. 

The previous version, 4.3.0.1.alpha2 did not have this issue, but 4.3.0.1.alpha3 is reporting the error message about kpsewhich is not found. From what I can gather, this kpsewhich is part of Latex. Since Latex is not a requirement to build Sage, this error should not be happening. It would appear one of the following patches is causing this, though none of them look as though they are likely to caused the problem. 

#5174, #1321, #6595, #6820, #6965


But these are the only patches applied between a version which did not generate the error, and one which does. 


```
Upon loading this alpha3, it now shows that kpsewhich is not found:

[mvngu@t2 sage-4.3.0.1.alpha3-32-bit-t2.math-gcc]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sh: kpsewhich: not found
sh: kpsewhich: not found
sage: 2 + 3
5
```

| Sage Version 4.3.0.1.alpha3, Release Date: 2010-01-28              |
| Type notebook() for the GUI, and license() for information.        |
Dave


---

Comment by jhpalmieri created at 2010-02-03 23:49:23

I think the culprit is #1321.  If you want evidence: in `sage/graphs/all.py`, change the end of the file from

```
from graph_database import graph_db_info
from graph_editor import graph_editor
```

to

```
from graph_database import graph_db_info

print "no kpsewhich error message yet"

from graph_editor import graph_editor

print "now you just saw the error message"
```

Note that if you use the version of graph_editor in Sage 4.3.2.alpha1, then I think you don't get this message, so the problem seems to have been fixed at some point.  I can't find the ticket, though...


---

Comment by jhpalmieri created at 2010-02-04 02:48:29

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-02-04 02:48:29

Actually, I think using the newer version of graph_editor just delays the error message until you run some graph theory command like `graphs.CompleteGraph(2)`.  

Here's a patch which does fix the problem, I think.


---

Attachment


---

Comment by was created at 2010-02-04 02:57:57

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 15:01:50

Resolution: fixed


---

Comment by drkirkby created at 2010-03-05 13:46:27

The patch does not prevent this error message occuring on Solaris. I have created another ticket, #8445 to preport the same problem still existing. 

Dave

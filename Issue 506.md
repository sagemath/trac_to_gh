# Issue 506: add %timeit support to the notebook

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-08-29 02:47:47

Assignee: boothby

CC:  jason-sage@creativetrax.com

Like in Ipython, it would be good if the notebook had support for using %timeit to time
blocks of code. 


---

Comment by was created at 2008-02-15 05:09:27

Changing assignee from boothby to was.


---

Comment by was created at 2008-02-15 05:09:27

Changing status from new to assigned.


---

Attachment

In addition to adding the requested functionality there is now a command timeit that one can also use from the command line, which correctly uses the preparser.


---

Attachment

apply both this and trac-506.ptch


---

Comment by mhansen created at 2008-02-15 06:46:33

Looks good to me.


---

Comment by ncalexan created at 2008-02-15 07:02:42

Looks good to me too.


---

Comment by mabshoff created at 2008-02-15 22:00:30

Merged in Sage 2.10.2.alpha1


---

Comment by mabshoff created at 2008-02-15 22:00:30

Resolution: fixed

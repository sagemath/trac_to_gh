# Issue 6121: use metaclasses to support nested class pickling

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-05-22 23:06:34

Assignee: cwitty

CC:  sage-combinat cwitty

Keywords: pickling, nested classes

We can work around this by shipping and always using a custom cPickle, and hopefully this will eventually be fixed in Python itself, but a metaclass seems to be a less hackish solution. 

Another solution is decorators, but this requires a decorator on every use. 


---

Comment by nthiery created at 2009-05-23 03:30:17

Thanks in advance for doing it.

Notes:
 - Fundamentally, the two approaches work the same (fixing the name, and inserting it in the module).
   The only difference is when this occur.
 - We anyway need to ship a patched cPickle for #5985.
 - This is a blocker for a bunch of later patches.


---

Comment by robertwb created at 2009-06-10 09:03:21

Depends on #6110

Authorship credit should go to nthiery as well.


---

Attachment


---

Comment by nthiery created at 2009-06-12 15:59:56

Applies and test smoothly (and 4.1, with #6110 applied first) and does its job.


---

Comment by nthiery created at 2009-06-12 15:59:56

Changing type from defect to enhancement.


---

Comment by ncalexan created at 2009-06-13 21:54:19

Resolution: fixed


---

Comment by jason created at 2009-09-22 17:09:48

A comment on #5986 indicates that it may be solved with this ticket.

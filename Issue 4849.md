# Issue 4849: add functionality for computing Heegner points to Sage

Issue created by migration from https://trac.sagemath.org/ticket/4849

Original creator: mabshoff

Original creation time: 2008-12-21 22:08:10

Assignee: was

See #4848 for a motivation. Attached is some Magma code, but note that according to William

```
Then the file heegner.py should be attached to that ticket, since to do that 
ticket, one might want to port some of what's in there to Sage. That said, it's 
not so simple, since better algorithms for computing Heegner points were found 
after that code was written.
```



---

Attachment

This is mostly Magma code


---

Comment by mabshoff created at 2008-12-21 22:11:30

Changing type from defect to enhancement.


---

Comment by davidloeffler created at 2009-07-15 20:39:14

This is fixed by #6045. I'm flagging this to "positive review" so it will come to the attention of mvngu, who has the authority to close tickets as 4.1.1 release manager.


---

Comment by mvngu created at 2009-07-16 10:14:22

The patches on #6045 result in some numerical noise. Once that is fixed, this ticket can get positive review. At the moment, I don't have the privilege to close tickets. But I've merged some tickets in my tree. If you're interested, refer to the file

http://sage.math.washington.edu/home/mvngu/release/merged-tkt.txt


---

Comment by mvngu created at 2009-07-20 15:52:03

Resolution: duplicate


---

Comment by mvngu created at 2009-07-20 15:52:03

I'm closing this as a duplicate of #6045.

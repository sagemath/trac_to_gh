# Issue 9331: can't build PDF version of reference manual in Sage 4.4.4

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-06-24 17:56:34

Assignee: mvngu

CC:  sage-combinat

From [sage-devel](https://groups.google.com/group/sage-devel/browse_thread/thread/bd0ef674ff168fe7):

```
In Sage 4.4.4, I can't build the PDF version of the reference manual,
even though the HTML version builds fine. Here is the error messsage:

Overfull \hbox (41.96407pt too wide) in paragraph at lines 73487--73489
[]\T1/pcr/m/n/10 MyClass2.__classcall__() \T1/ptm/m/n/10 should re-turn the re-
sult of \T1/pcr/m/n/10 UniqueRepresentation.__classcall__()
[890]
! TeX capacity exceeded, sorry [input stack size=5000].
\reserved`@`a ->\def \reserved`@`a
                               *{\ttl`@`assign`@`i {\`@`tempskipb }}\reserved`@`a
l.73597 ...{UniqueRepresentation}} and unpickling}

!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on reference.log.
make: *** [reference.pdf] Error 1 
```

This is traced to ticket #9106.


---

Attachment


---

Comment by mvngu created at 2010-06-24 18:01:32

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-06-25 05:44:17

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-06-25 05:44:17

I am fine with the change! Thanks for tracking it down. Please open a new ticket to remind us about putting the link back once sphinx is fixed!


---

Comment by rlm created at 2010-07-06 08:52:43

Resolution: fixed

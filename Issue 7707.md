# Issue 7707: change picklejar doctest to be more robust

Issue created by migration from https://trac.sagemath.org/ticket/7707

Original creator: was

Original creation time: 2009-12-16 09:11:02

Assignee: tbd

The picklejar doctest in structure/sage_object.pyx has to be changed whenever we update the picklejar, when things get deprecated, etc.  That's silly.  Let's change the test to be like this:


```
        sage: print "x"; sage....
        x...
        Failed to unpickle 0 objects.
```



---

Attachment


---

Comment by was created at 2009-12-16 09:13:08

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-12-19 21:11:21

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-19 21:11:21

Looks good to me.


---

Comment by mhansen created at 2009-12-20 07:20:14

Resolution: fixed

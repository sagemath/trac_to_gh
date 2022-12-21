# Issue 1201: add gramm-schmidt to sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-18 21:50:48

Assignee: was*

Add function to do gramm schmidt orthogonalization and also to verify the LLL criterion to Sage.

NOTE: I have mostly done this.  This trac is just so I have a place to submit a patch.  So you shouldn't do this :-).



---

Attachment


---

Comment by was created at 2007-11-19 03:38:36

NOTE -- this is a generic implementation.  There is surely a vastly faster implementation in the case of an RDF or CDF base field (by calling to numpy).


---

Comment by was created at 2007-11-21 12:31:40

From David Joyner:

```
I looked at it but can't figure out how to apply it to a cloned version
of SAGE. It seems to make sense but I'd like to test it out.
Sorry for the delay. I had a final to type up and lots of grading.
```



---

Comment by was created at 2007-11-26 06:40:06

also apply this patch (after the first)


---

Attachment


---

Comment by mhansen created at 2007-12-02 05:13:30

I think this can go in.


---

Comment by mabshoff created at 2007-12-02 05:54:22

Resolution: fixed


---

Comment by mabshoff created at 2007-12-02 05:54:22

Merged in 2.8.15.alpha2.

# Issue 2586: latex products need to be space separated

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-03-18 17:01:07

Assignee: was

CC:  ncalexan

Keywords: latex product polynomial

I'm sure this is a dupe, but couldn't find a ticket.  It might need fixing at an awful lot of places... but polynomials are a start:


```
sage: ZZ['a']['b']([0, ZZ['a'].0])
a*b
sage: latex(ZZ['a']['b']([0, ZZ['a'].0]))
ab
```



---

Comment by ncalexan created at 2008-03-18 17:01:55

Some people might not think this is a problem.  This definitely is:


```
sage: latex(ZZ['alpha']['b']([0, ZZ['alpha'].0]))
\alphab
```



---

Comment by mabshoff created at 2008-03-18 20:41:15

I agree that this is a bug and I think the ticket you are referring to is the one where we discussed removing `\cdot`. 

Cheers,

Michael


---

Attachment


---

Attachment


---

Comment by AlexGhitza created at 2008-03-19 23:33:04

Actually, it's not due to #384: that only touched the symbolic expressions, and you can check that the code puts spaces where \cdot's used to be.

But it does happen in a few places in the polynomials code.  I believe the patch fixes all of them.  In particular, Nick's examples now work properly.

This (un)broke a bunch of doctests, so I've fixed them as well.  See also the doc patch with a small fix to const.tex due to these changes.


---

Comment by mabshoff created at 2008-03-21 03:36:42

Both patches look good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-21 04:16:57

referee's patch to fix some more doctest failures


---

Comment by mabshoff created at 2008-03-21 04:17:19

Resolution: fixed


---

Attachment

Merged all three patches in Sage 2.11.alpha1

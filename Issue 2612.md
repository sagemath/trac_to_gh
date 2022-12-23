# Issue 2612: String to Integer Conversion

Issue created by migration from https://trac.sagemath.org/ticket/2612

Original creator: vgermrk

Original creation time: 2008-03-20 12:40:51

Assignee: somebody

Since python does well with a leading sign (+ or -)

```
sage: int('+1')
1
sage: int('-1')
-1
```

the sage Integers should do the same.

```
sage: Integer('-1')
-1
sage: Integer('+1')
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/mrk/<ipython console> in <module>()

/home/mrk/integer.pyx in sage.rings.integer.Integer.__init__()

<type 'exceptions.TypeError'>: unable to convert x (=+1) to an integer
```

So the case of a leading "+" must be fixed


---

Attachment


---

Comment by AlexGhitza created at 2008-03-27 22:47:00

Looks good: fixes the bug, doesn't break anything else.


---

Comment by mabshoff created at 2008-03-28 08:37:51

Merged in Sage 2.11.alpha2. I had to merge the first hunk of 2612-integer_plus.patch manually due to trivial merge conflicts.


---

Comment by mabshoff created at 2008-03-28 08:37:51

Resolution: fixed

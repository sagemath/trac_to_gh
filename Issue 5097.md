# Issue 5097: doctest failures in 3.3.alpha2 due to lack of #optional tag

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-01-25 08:20:07

Assignee: AlexGhitza

Several doctests in interfaces/octave.py and interfaces/maple.py should be marked optional but aren't.  Trivial patch coming up.



---

Comment by mabshoff created at 2009-01-25 14:48:02

Thanks for the fixes, but they all should read

```
# optional -- requires Octave 
```

or whatever system is required. I will fix the patch if no one beats me to it.

Cheers,

Michael


---

Attachment


---

Comment by AlexGhitza created at 2009-01-25 16:53:41

Done.


---

Comment by mabshoff created at 2009-01-25 21:03:22

Positive review. I changed some of the doctests tags to be more consitent, but now the doctests without maple and octave pass.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-25 21:03:34

Merged in Sage 3.3.alpha3


---

Comment by mabshoff created at 2009-01-25 21:03:34

Resolution: fixed

# Issue 5927: [with patch; needs review] singular prompt problem on solaris sparc

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-29 01:36:52

Assignee: mabshoff

Credit to William Stein, Mike Hansen, and Michael Abshoff?


---

Comment by was created at 2009-04-29 01:40:17

I tested it, and it works.


---

Comment by mabshoff created at 2009-04-29 23:00:11

Oops, there are three doctest failures with this patch applied:

```
        sage -t -long devel/sage/sage/interfaces/expect.py # 1 doctests failed
        sage -t -long devel/sage/doc/en/developer/coding_in_other.rst # 2 doctests failed
        sage -t -long devel/sage/doc/en/constructions/algebraic_geometry.rst # 4 doctests failed
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-05-15 14:33:17

This is a 4.0 blocker. 

Mike: Any comments?

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2009-05-21 17:56:02

Changing status from new to assigned.


---

Comment by mhansen created at 2009-05-21 17:56:02

All of the failures are harmless.  I've attached a new patch which fixes the doctests.


---

Comment by mhansen created at 2009-05-21 17:56:02

Changing assignee from mabshoff to mhansen.


---

Comment by mabshoff created at 2009-05-22 12:49:33

Hmm, I am not so sure the patch does fix every problem:
Without the patch:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: singular.eval("intvec G = 4,4,4,0,0,0;")
''
```

With the patch applied:

```
mabshoff`@`sage:/scratch/mabshoff/sage-4.0.rc1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: singular.eval("intvec G = 4,4,4,0,0,0;")
'intvec G = 4,4,4,0,0,0;'
sage: 
```

| Sage Version 4.0.rc0, Release Date: 2009-05-21                     |
| Type notebook() for the GUI, and license() for information.        |
| Sage Version 4.0.rc0, Release Date: 2009-05-21                     |
| Type notebook() for the GUI, and license() for information.        |
If you look at the attached patch here it seems that we sometimes get the echo of the command and some times not. It might be consistent, i.e. the doctests pass on all platforms (I hope), but something still seems fishy.

I am not saying we shouldn't apply the patch since it fixes a much more severe bug, I just think that there is more to the story. Anyway, doctests do pass, so I will open a followup ticket and merge this patch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-22 13:17:37

Merged in Sage 4.0.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-22 13:17:37

Resolution: fixed

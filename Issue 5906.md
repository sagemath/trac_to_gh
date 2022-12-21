# Issue 5906: "libpng error: Image width or height is zero in IHDR" when plotting CompleteGraph(2)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-26 21:47:04

Assignee: rlm

This came up in https://groups.google.com/group/sage-devel/t/d9b64b5ddc24bb6b

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: g = graphs.CompleteGraph(2)
sage: g.show()
libpng error: Image width or height is zero in IHDR
<SNIP>
```

| Sage Version 3.4.1, Release Date: 2009-04-21                       |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-05-04 18:40:43

Ooops, I forgot to review this for 3.4.2, but positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-04 18:41:04

Resolution: fixed


---

Comment by mabshoff created at 2009-05-04 18:41:04

Merged in Sage 4.0.alpha0.

Cheers,

Michael

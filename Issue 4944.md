# Issue 4944: speed regression in finding roots over number fields when an embedding is specified

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-01-06 00:48:32

Assignee: was

CC:  robertwb was

Keywords: roots number field embedding


```
sage: x = ZZ['x'].0; (x^2 + 1).roots(NumberField(x^2 - 106*x + 2789, 'a', embedding=CC.0))
```


Doesn't terminate in reasonable time on sage.math or my Mac OS X box.


---

Comment by mabshoff created at 2009-01-06 01:07:31

Nick,

this looks similar to #4723 and there is a patch from Carl. The patch over there (which isn't merged yet) fixes the problem for me. Before I killed it after 10 seconds CPU time, with the patch applied:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: time x = ZZ['x'].0; (x^2 + 1).roots(NumberField(x^2 - 106*x + 2789, 'a', embedding=CC.0))
CPU times: user 0.02 s, sys: 0.01 s, total: 0.03 s
Wall time: 0.03 s
sage: x = ZZ['x'].0; (x^2 + 1).roots(NumberField(x^2 - 106*x + 2789, 'a', embedding=CC.0))
[]
```

Ironically the other issue was also reported by you :)
| Sage Version 3.2.3.final, Release Date: 2009-01-02                 |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael


---

Comment by mabshoff created at 2009-01-06 02:37:51

This won't make it into 3.2.3, better luck in 3.3. I also assume this is a dupe since Carl's patch fixes the problem (unless the new patch doesn't find some roots, etc).

Cheers,

Michael


---

Comment by ncalexan created at 2009-01-17 06:11:46

The patch for #4723 fixes this.


---

Comment by mabshoff created at 2009-01-18 15:48:44

Fixed by merging #4723.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-18 15:48:44

Resolution: fixed

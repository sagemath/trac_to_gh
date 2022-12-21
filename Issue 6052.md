# Issue 6052: partial_fraction_decomposition is broken for irreducible denominators

Issue created by migration from Trac.

Original creator: tornaria

Original creation time: 2009-05-17 02:43:00

Assignee: tornaria


```
19:34 < rickhg12hs> having some issues with partial fraction decomposition
19:37 < rickhg12hs> sage: R.<x> = GF(2)[];((x+1)/(x^3+x+1)).partial_fraction_decomposition()
19:37 < rickhg12hs> ... generates type errors
19:39 < rickhg12hs> sage: P.<y>=ZZ[];((y+1)/(y^2+y+1)).partial_fraction_decomposition()
19:39 < rickhg12hs> ... generates type errors also
19:41 < rickhg12hs> sage: ((y+1)/(y^2+y+1) + (y+1)/(y^2+1)).partial_fraction_decomposition()
19:41 < rickhg12hs> ... the line above works
19:43 < rickhg12hs> sage: ((x+1)/(x^3+x+1) + (x+1)/(x^3+x^2+1)).partial_fraction_decomposition()
19:43 < rickhg12hs> ... the line above works
19:46 < rickhg12hs> FYI:
19:46 < rickhg12hs> sage: version()
19:46 < rickhg12hs> 'Sage Version 3.4.2, Release Date: 2009-05-05'
```



---

Attachment

Looks good to me.  I just updated some minor Sphinx formatting issues in the patch.

Other than that, all tests pass and things look good to me.


---

Comment by mabshoff created at 2009-05-19 18:44:04

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-19 18:44:04

Resolution: fixed

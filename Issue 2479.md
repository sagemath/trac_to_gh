# Issue 2479: RDF polynomial factoring bug

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-03-12 00:49:24

Assignee: somebody


```
sage: x = polygen(RDF,'x')
sage: (-2*x^2 - 1).factor()
[]
```


degree 4?


---

Attachment

Attached patch fixes this problem.


---

Comment by craigcitro created at 2008-03-12 01:33:25

Yep, looks good. 

I'm giving this a positive review, even though I had trouble applying this patch on my home machine. I think something got screwed up with my home machine's install, because it was an upgrade from 2.10.1 to 2.10.2 to 2.10.3. I tested, and the patch applies just fine against the copy of 2.10.3.rc1 I have on sage.math, so I'm pretty sure this is a local problem with my setup. Maybe it's an issue with upgrades from 2.10.2 to 2.10.3? In any event, it shouldn't be a problem for whoever is rolling 2.10.3.1 or whatnot.


---

Comment by craigcitro created at 2008-03-12 01:38:03

Actually, I take it back. I think that the version that William made this patch against isn't 2.10.3, because the same hunk that failed for me will fail on sage.math and another upgrade that just finished for me. I'm going to submit a second patch in about 30 seconds; one of the two should work.


---

Comment by craigcitro created at 2008-03-12 01:51:08

Ok, re-based the patch. The name on the commit should get changed to William, since it's really his patch.


---

Attachment

same patch as above, but applies clean against 2.10.3


---

Comment by mabshoff created at 2008-03-12 19:34:24

Resolution: fixed


---

Comment by mabshoff created at 2008-03-12 19:34:24

Merged trac-2479-v2.patch in Sage 2.10.4.alpha0

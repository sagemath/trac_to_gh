# Issue 7985: fix doctest in base.pyx

Issue created by migration from https://trac.sagemath.org/ticket/7985

Original creator: wcauchois

Original creation time: 2010-01-19 00:10:01

Assignee: was

The following doctest from line 757 of base.pyx:

```
sage: G = tetrahedron(color='red') + tetrahedron(color='yellow') + tetrahedron(color='red', opacity=0.5)
sage: G.texture_set()
set([Texture(texture..., red, ff0000), Texture(texture..., yellow, ffff00), Texture(texture..., red, ff0000)])
```

will fail sometimes because the order of the elements of the set is not fixed. The attached patch fixes this by outputting first the two red textures, and then the yellow texture.


---

Comment by wcauchois created at 2010-01-19 00:10:43

based on sage 4.3.1.rc0


---

Comment by wjp created at 2010-01-19 04:39:07

Changing status from new to needs_review.


---

Attachment


---

Comment by wjp created at 2010-01-19 04:39:24

Looks good.


---

Comment by wjp created at 2010-01-19 04:39:24

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-19 05:32:31

Resolution: fixed

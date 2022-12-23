# Issue 3451: inaccurate error message in scheme morphisms

Issue created by migration from https://trac.sagemath.org/ticket/3451

Original creator: moretti

Original creation time: 2008-06-17 22:17:24

Assignee: moretti

CC:  alexghitza

Keywords: affine, scheme, morphism


```
R.<x,y> = QQ[]
A = AffineSpace(R)
H = A.Hom(A)
f = H([x-y, x*y])
f([0,1])
Traceback (click to the left for traceback)
...
TypeError: x (=[0, 1]) must be a projective point given by coordinates
```


When of course the error message should say that x must be an affine point...

The fix would be trivial, but would it be acceptable to make scheme morphisms try converting their input to elements of their domain, first, so that the above would not raise an error?



---

Attachment


---

Comment by AlexGhitza created at 2008-08-27 08:55:08

I have changed things in the following way: if we try to evaluate f(p), then the first step is to coerce p into the domain of f.  If that works, then the evaluation goes forth.  Otherwise, there is of course an error message saying that p has no business being there in the first place.

The change is in the generic scheme morphism code, so it should work for affine spaces, projective spaces, and whatever else inherits from schemes.


---

Comment by AlexGhitza created at 2008-09-01 09:15:23

Changing assignee from moretti to AlexGhitza.


---

Comment by AlexGhitza created at 2008-09-01 10:04:03

Changing status from new to assigned.


---

Comment by cremona created at 2008-09-01 19:50:22

Looks ok to me.  I see that you are relying on whatever error message is produced by "dom(x)" in case x cannot be coerced into dom rather than supplying your own, of the form "... cannot be coerced into the domain", but that is ok.

Patch applies cleanly to 3.1.2.alpha3 and all doctests in sage.schemes.generic pass.


---

Comment by mabshoff created at 2008-09-02 11:46:39

Merged in Sage 3.1.2.alpha4


---

Comment by mabshoff created at 2008-09-02 11:46:39

Resolution: fixed

# Issue 5886: Bug in free module homomorphism creation

Issue created by migration from https://trac.sagemath.org/ticket/5886

Original creator: was

Original creation time: 2009-04-24 03:40:43

Assignee: was

Consider the following

```
sage: V = (QQ^3).span_of_basis([[1,1,0],[1,0,2]]); V
Vector space of degree 3 and dimension 2 over Rational Field
User basis matrix:
[1 1 0]
[1 0 2]
sage: V.hom([V.0, V.1])
Traceback (most recent call last):
...
TypeError: entries has the wrong length
```


The hom command above *should* create the identity morphism, since according to the docs hom takes as input a list of the images of the generators.    Instead, what is happening is that the list is being turned into a matrix directly.  Conclusion, the above just goes boom, since the matrix would have to be 2x2, as V has rank 2.   E.g., this works:

```
sage: V.hom([[1,2],[3,4]], V)
Free module morphism defined by the matrix
[1 2]
[3 4]
Domain: Vector space of degree 3 and dimension 2 over Rational Field
User ...
Codomain: Vector space of degree 3 and dimension 2 over Rational Field
User ...
```


The really *scary* thing is that this broken code will accidentally and _silently_ give totally wrong answers in some cases, e.g.,

```
sage: V = (QQ^2).span_of_basis([[1,2],[3,4]])
sage: I = V.hom([V.0,V.1]); I
Free module morphism defined by the matrix
[1 2]
[3 4]
Domain: Vector space of degree 2 and dimension 2 over Rational Field
User ...
Codomain: Vector space of degree 2 and dimension 2 over Rational Field
User ...
sage: I(V.0)
(7, 10)
sage: V.0
(1, 2)
```


Notice above that I *should* be the identity map, but it's most certainly not -- it's the map defined by the matrix [[1,2],[3,4]].  


---

Attachment

It looks good. I'm having trouble running any doctests (applied to a pre-3.4.1 branch after upgrading) but the examples I tried manually work.


---

Comment by was created at 2009-04-24 04:53:03

No doctests break :-)

Seriously, I did apply this patch to a clean 3.4.1 build on sage.math, run --long doctests, and got no failures.


---

Comment by robertwb created at 2009-04-24 04:59:32

Good.


---

Comment by mabshoff created at 2009-04-24 05:03:00

I can confirm William's observation: no doctest breakage with -long in my 3.4.2.alpha0 merge tree.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-24 05:03:13

Resolution: fixed


---

Comment by mabshoff created at 2009-04-24 05:03:13

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael

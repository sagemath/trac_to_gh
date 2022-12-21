# Issue 8143: Efficient Gram-Schmidt

Issue created by migration from Trac.

Original creator: rlindner

Original creation time: 2010-02-01 17:09:40

Assignee: AlexGhitza

CC:  jason

As a Crypto PhD, I enjoy using the many functionalities in SAGE that interface the NTL library, however an important function was left out, namely the Gram-Schmidt Orthogonalization.

There is an implementation in SAGE which is in pure python and very slow (but exact). I propose to add an option to use NTL for matrices of dimensions > 200.

Richard


---

Comment by AlexGhitza created at 2010-09-02 10:48:36

Changing assignee from AlexGhitza to jason, was.


---

Comment by AlexGhitza created at 2010-09-02 10:48:36

Changing component from algebra to linear algebra.


---

Comment by rbeezer created at 2011-02-24 05:17:14

I have been working on the exact Gram-Schmidt routine and on matrices over double-precision floating point numbers (RDF, CDF).

Are you interested in an exact routine, or a fast approximate one?

I couldn't find Gram-Schmidt via the NTL website (didn't look real hard).  Can you provide a pointer to whichever file contains it?

Rob

# Issue 3493: Notes on Elliptic curves documentation

Issue created by migration from Trac.

Original creator: ljpk

Original creation time: 2008-06-23 09:07:08

Assignee: tba

In part 37.8 of the Reference Manual (the Elliptic curves over finite fields section) there are some formatting issues. For instance, in the section on the frobenius_polynomial, we have the sentence:


```
The Frobenius endomorphism of the elliptic curve has quadratic characteristic polynomial. 
In most cases this is irreducible and defines an imaginary quadratic order; 
for some supersingular curves, Frobenius is an integer a and the polynomial is 1703#326 .}}}

I assume that the 1703#326 is some sort of broken formatting code.

There are similar examples throughout this page.

On a slightly different tack, in the documentation for cardinality and order, it would be helpful to say that "sea" (as in the algorithm) means Schoof-Elkies-Atkin.


---

Comment by cremona created at 2008-08-01 02:05:46

The strange omission or garblings are all for pieces of docstrings in LaTeX format, i.e. between $...$.  But there are many other such parts of docstrings which display fine.  So I don't know why some don't come out right.


---

Comment by jhpalmieri created at 2009-02-26 17:20:47

The first issue doesn't seem to be a problem with the new documentation.  I'm attaching a patch for the second one ('sea').


---

Attachment


---

Comment by mabshoff created at 2009-03-23 22:12:57

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-23 22:12:57

Resolution: fixed

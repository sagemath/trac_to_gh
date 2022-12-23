# Issue 5146: implement MPolynomial_ideal.varierty() for GF(p) with p > than what Singular supports

Issue created by migration from https://trac.sagemath.org/ticket/5146

Original creator: malb

Original creation time: 2009-01-31 18:06:25

Assignee: malb

CC:  john_perry


```
R.<x,y> = PolynomialRing(GF(2147483659),order='lex')
I=ideal([x^3-2*y^2,3*x+y^4])
sage: I.variety()
...
   ? `2147483659` greater than 2147483647(max. integer representation)
   ? error occurred in STDIN line 172: `ring sage86=2147483659,(x, y),lp;`
   ? expected ring-expression. type 'help ring;'
```



---

Comment by mabshoff created at 2009-02-06 23:00:14

3.4 is for ReST tickets only.

Cheers,

Michael


---

Comment by john_perry created at 2009-02-21 08:19:03

Implementing Lazard's algorithm to solve this required a few subalgorithms as well. Rather than clutter `multi_polynomial_ideal.py`, I appended the functions to `toy_buchberger.py`. That seemed a natural location, since this is a toy implementation, and computing the variety of a zero-dimensional ideal is not an unnatural follow-up to Buchberger's algorithm. That said, if someone prefers that this be placed in `multi_polynomial_ideal.py`, or even in a new file, I can work with that.

The implementation provided is (unsurprisingly) unoptimized more or less, not even requiring a lexicographic ordering. On the upside, you don't need a lexicographic ordering. Check out the doctest on `triangular_factorization`.

I added doctests for all the new functions in `toy_buchberger.py`, and a new doctest which tests for the system listed above. The patch uploaded passes all the doctests, at least on my machine.


---

Comment by mabshoff created at 2009-02-21 08:21:26

Replying to [comment:3 john_perry]:

Hi John,

> Implementing Lazard's algorithm to solve this required a few subalgorithms as well. Rather than clutter `multi_polynomial_ideal.py`, I appended the functions to `toy_buchberger.py`. That seemed a natural location, since this is a toy implementation, and computing the variety of a zero-dimensional ideal is not an unnatural follow-up to Buchberger's algorithm. That said, if someone prefers that this be placed in `multi_polynomial_ideal.py`, or even in a new file, I can work with that.

I would suggest to place it in its own file, but maybe Martin should pipe in there, too.

Cheers,

Michael


---

Attachment

New version of the patch:
 * Separated functions related to triangularization into a new file, `toy_variety.py`

 * Completely rewrote two subalgorithms that check for and express linear dependence between polynomials. Lazard did not specify the details, and I implemented the previous versions in a manner that in no way could be described as intelligent. (Ironically, I'm scheduled to teach introductory linear algebra this summer.) The present version uses basic linear algebra to answer these questions.

 * Removed some doctests on the same two functions, because they are now nested. If there is a way to doctest nested functions, let me know, and I'll restore the doctests.


---

Comment by malb created at 2009-03-16 12:06:57

rebased to 3.4


---

Attachment

I rebased the attached patch against 3.4 and changed the docstrings to the new ReST format. I think actually that the nested functions shouldn't be nested and should get proper examples/doctests. 

(Btw. there is a `coefficient_matrix()` function in `mq.MPolynomialSystem` but that is the material of another ticket)


---

Comment by malb created at 2009-03-16 12:09:26

also: I'm sorry to have let bitrot this patch for so long, I know the ball was in my corner.


---

Attachment

Updated with some of Martin's comments


---

Comment by john_perry created at 2009-03-18 00:16:34

I made the changes Martin recommended: namely, de-nesting the nested functions and adding doctests.

One reason the functions were nested is that I was using certain assumptions. I thought that made life easier but in retrospect it doesn't. This allowed me to simplify the functions.

In addition the documentation follows the format Martin was using (ReST?). I'm still using my own coefficient_matrix() but I reckon that can be adjusted if desired.


---

Comment by malb created at 2009-03-20 14:08:12

John, I guess you don't run 3.4 because your new patch does break the same stuff I fixed for the first patch. I'll fix it again.


---

Attachment


---

Comment by malb created at 2009-03-20 14:17:07

If John agrees to my changes, the patch has a positive review. John, note that the indentation in the docs has meaning and we can't just remove it.


---

Comment by john_perry created at 2009-03-25 17:39:00

All doctests passed on my setup.


---

Comment by mabshoff created at 2009-03-26 00:08:41

Merged toy_variety.patch in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-26 00:08:41

Resolution: fixed

# Issue 6442: Random(?) index error with determinant method

Issue created by migration from Trac.

Original creator: spancratz

Original creation time: 2009-06-28 18:23:15

Assignee: somebody

CC:  mjo

Keywords: det, determinant, IndexError

On some occasions, the call A.det() for a matrix A results in an error, namely:

    IndexError: list index out of range

The error occurs during the dictionary lookup.  It seems that rather than finding no item (and hence creating a new one and then computing determinant), an empty item D is found and indexing into D results in the error.

If run into this strange problem twice during the SAGE Days 16.  I've attached an example file to this email, which contains a saved matrix.  The code

    sage: A = load("DetBugMatrix.sobj")
    sage: A.det()

should trigger the problem.  If I recall correctly, I obtained the matrix from the following code

    sage: R = Zp(p=5,prec=3,type="capped-abs",print_mode="series")
    sage: A = random_matrix(R, 10, 10)

Strangely enough (although perhaps not that strange after checking that the error happens during the lookup), the call A.copy().det() returns the determinant without any problems.

I have no clue as to how one could systematically reproduce the bug.

In case it may help, I downloaded SAGE 4.0.2 and built it locally.  The machine used is a Lenovo T500 laptop with two intel centrino, running Ubuntu.  If there's any further information that would help, please let me know.


---

Comment by spancratz created at 2009-06-28 18:24:10

Matrix to trigger the IndexError


---

Attachment


---

Comment by davidloeffler created at 2009-07-05 08:09:47

Changing component from algebra to linear algebra.


---

Comment by mjo created at 2012-01-04 00:51:16

We've got two charpoly() algorithms at the moment, but back when this bug was reported, I think the hessenberg algorithm was the default. If we try charpoly() on this matrix,


```
sage: A = load('/home/mjo/DetBugMatrix.sobj')
sage: A.charpoly(algorithm='hessenberg')
...
ValueError: element valuation cannot be negative.
```


If we look at the code for charpoly(), we see that the empty hash {} is cached before the attempt to compute charpoly(). In matrix2.pyx,


```
D = self.fetch('charpoly')

if not D is None:
    if D.has_key(var):
        return D[var]
else:
    D = {}
    self.cache('charpoly',D)

<compute the charpoly>

# Cache the result
D[var] = f
return f  
```


So if computation of charpoly() fails, we'll have {} cached, and det() will blow up. A full example:


```
sage: A = load('/home/mjo/DetBugMatrix.sobj')
sage: A.charpoly(algorithm='hessenberg')
...
ValueError: element valuation cannot be negative.
sage: A.det()
...
IndexError: list index out of range
sage: A.charpoly()
(1 + O(5^3))*x^10 + (2 + 4*5 + 2*5^2 + O(5^3))*x^9 + (4 + 4*5 + 4*5^2 + O(5^3))*x^8 + (4 + 5^2 + O(5^3))*x^7 + (4*5^2 + O(5^3))*x^6 + (3 + 5 + 5^2 + O(5^3))*x^5 + (1 + 3*5 + 5^2 + O(5^3))*x^4 + (1 + 4*5 + 4*5^2 + O(5^3))*x^3 + (1 + 4*5 + 4*5^2 + O(5^3))*x^2 + (2 + 4*5 + 4*5^2 + O(5^3))*x + (2*5 + 4*5^2 + O(5^3))
sage: A.det()
2*5 + 4*5^2 + O(5^3)
```


So the solution, I think, is to avoid caching the empty hash until we know we've got a charpoly.


---

Comment by mjo created at 2012-01-05 02:27:07

Here's a patch that should prevent this problem in the future. I used the smallest matrix I could find for the doctest, but I was just creating them randomly. I'd be happy to replace it with a smaller example.


---

Comment by mjo created at 2012-01-05 02:27:07

Changing status from new to needs_review.


---

Comment by zimmerma created at 2012-01-10 10:27:36

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2012-01-10 10:27:36

I tried the attached patch on top of 4.7.2 but the problem with the initial matrix still exists:

```
[zimmerma`@`coing tmp]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: 6442
sage: A = load ("DetBugMatrix.sobj")
sage: A.det()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
| Sage Version 4.7.2, Release Date: 2011-10-29                       |
| Type notebook() for the GUI, and license() for information.        |
/tmp/<ipython console> in <module>()

/usr/local/sage-4.7.2/sage/local/lib/python2.6/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.det (sage/matrix/matrix2.c:8222)()

/usr/local/sage-4.7.2/sage/local/lib/python2.6/site-packages/sage/matrix/matrix2.so in sage.matrix.matrix2.Matrix.determinant (sage/matrix/matrix2.c:6889)()

IndexError: list index out of range
```

Paul


---

Comment by zimmerma created at 2012-01-10 10:42:58

Changing keywords from "det, determinant, IndexError" to "det, determinant, IndexError, sd35.5".


---

Comment by mjo created at 2012-01-10 13:18:54

The bug wasn't in the saving/loading of matrices, only in the cache code. DetBugMatrix.sobj contains a broken matrix -- one with an empty dictionary cached as the charpoly(). When you load it from file, it's still broken, so some operations won't work on it.

The patch prevents creating these matrices in the future by fixing the cache bug (hopefully).

The code from the doctest should work only after the patch, because prior to the patch, it would have created a matrix with the same problem as the one in DetBugMatrix.sobj.


---

Comment by zimmerma created at 2012-01-10 14:34:13

the doctest example can be simplified to:

```
A = matrix(z, [ [3 + O(5^1), 4 + O(5^1), 4 + O(5^1)],
[2*5^2 + O(5^3), 2 + O(5^1), 1 + O(5^1)],
[5 + O(5^2), 1 + O(5^1), 1 + O(5^1)]])
```

Paul


---

Comment by zimmerma created at 2012-01-10 14:42:34

> The bug wasn't in the saving/loading of matrices, only in the cache code [...]

ok, I put it back to "needs review". However the summary is misleading.

Paul


---

Comment by zimmerma created at 2012-01-10 14:42:34

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2012-01-10 14:46:51

two minor points:

(1) the comment `Cache the result` on line 1465 should be in fact on line 1470. The code at
line 1465 only initializes an empty cache.

(2) it seems to me that if charpoly is called with the same matrix but different variables, the computation is done twice, whereas it would suffice to substitute the first variable by the second one, no? Maybe this can be in a separate ticket.

Paul


---

Comment by mjo created at 2012-01-10 14:59:20

Thanks for the simplified test case, I'll be able to update the patch in a bit.

I think you're correct about (2), but I would do that in a separate ticket since it's unrelated to this problem.


---

Comment by mjo created at 2012-01-10 15:25:57

Updated patch with simpler test case and a better comment.


---

Attachment

I just updated the patch with your test case.

I moved the "Cache the result" comment to where it belongs, but also added a comment above the code that creates the dictionary, explaining why it occurs near the end of the function.


---

Comment by zimmerma created at 2012-01-11 07:22:10

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2012-01-11 07:22:10

thank you Michael for your changes. All doctests pass. I give a positive review.

Paul


---

Comment by zimmerma created at 2012-01-11 07:32:51

the efficiency issue with the cache is now ticket #12292.

Paul


---

Comment by jdemeyer created at 2012-01-29 11:17:20

Resolution: fixed

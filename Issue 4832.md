# Issue 4832: [with patch, needs review] prevent search_src and search_doc from printing the sage banner

Issue created by migration from https://trac.sagemath.org/ticket/4832

Original creator: jhpalmieri

Original creation time: 2008-12-19 16:06:44

Assignee: jhpalmieri

Keywords: search_src, banner

Right now, running `search_src` from the command line with a single argument prints the sage banner as well as the search results.  If you include more than one argument, then the banner is not printed. (This isn't true if there enough results to feed into the pager.)  The same goes for `search_doc`.  The reason is that these functions all call `sage -grep` which prints the banner, but including an extra argument calls grep on the output, and the banner won't match.  The function `search_def` doesn't have this problem, because it just calls `search_src` with an extra argument "def".

Here's an example:

```
sage: search_src('noncommutative')
----------------------------------------------------------------------
----------------------------------------------------------------------
algebras/quaternion_algebra.py:        Return False always, since all quaternion algebras are noncommutative and all fields are commutative.
algebras/quaternion_algebra.py:        Return False always, since all quaternion algebras are noncommutative and integral domains are commutative (in SAGE).
matrix/matrix_space.py:commutative or noncommutative ring.
matrix/matrix0.pyx:        EXAMPLE of matrix multiplication over a noncommutative base ring:
matrix/matrix0.pyx:        EXAMPLE of scalar multiplication in the noncommutative case:
| Sage Version 3.2.2.rc1, Release Date: 2008-12-17                   |
| Type notebook() for the GUI, and license() for information.        |
sage: search_src('noncommutative', 'ring')
matrix/matrix_space.py:commutative or noncommutative ring.
matrix/matrix0.pyx:        EXAMPLE of matrix multiplication over a noncommutative base ring:

```


The attached patch prevents the banner from printing by temporarily setting the environment variable SAGE_BANNER to be "no". 



---

Attachment

Read only review -- there's no way this fails :)


---

Comment by mabshoff created at 2009-01-23 10:27:08

Merged in Sage 3.3.alpha1

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 10:27:08

Resolution: fixed

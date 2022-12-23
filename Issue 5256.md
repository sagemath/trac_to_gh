# Issue 5256: [with patch, needs review] coherent handling of trivial matrices (depend on #5244, #5242).

Issue created by migration from https://trac.sagemath.org/ticket/5256

Original creator: hivert

Original creation time: 2009-02-13 18:47:24

Assignee: was

CC:  sage-combinat

Keywords: matrices, invert, determinant

There where a lot of inconsistency and bugs in the handling of trivial matrices.
The following patch aims to solve these and to check systematicly the coherence. Here is a selection of weirdness:
 * plain wrong answers

```
sage: m = matrix(SR, 1,1, [1])
sage: m.inverse()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

sage: m = matrix(RDF, 0,2)
sage: m.inverse()
[]
```

 * Inconsistencies in the answers depending on the base ring

```
sage: m = matrix(RDF, 1,1)
sage: m.inverse()
---------------------------------------------------------------------------
LinAlgError                               Traceback (most recent call last)
```

   whereas

```
sage: m = matrix(QQ, 1,1)
sage: m.inverse()
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
```


Aside rewriting some error messages, changing some exception and working around several bug in particular in maxima's handling of matrix over SR, the main contribution of this patch lies in the function `test_trivial_matrices_inverse` in `sage/matrix/matrix_space.py` and its associated doctests. Trough a bunch of assertions this function indirectly checks the behavior of matrix spaces. Any new implementation of a kind of matrices should be checked be this function. 

Patch Author: Florent Hivert


---

Comment by hivert created at 2009-02-13 18:50:34

Changing assignee from was to hivert.


---

Comment by hivert created at 2009-02-13 18:50:34

Changing status from new to assigned.


---

Comment by jason created at 2009-02-13 19:23:47

I'm really happy you did all this.  I'll look at this soon, unless someone else gets to it before me.

It'd be great to have a system-wide function that tested different Sage types for consistency on things like this.  That way, all someone would have to remember to do is add their new sage type to a doctest like:


```
sage: check_consistency(MY_NEW_TYPE)
True
```


That function would automatically call things like the function in this patch and other functions for vectors, polynomials, etc.


---

Comment by hivert created at 2009-02-13 20:05:56

In his category framework, Nicolas Thiery wrote a very handy feature that allows one to add some plug in function to test properties on a parent object. For example in the category of groups there are among other the following methods (some are inherited from higher categories): 
 - test_some_elements
 - test_associativity
 - test_unity
 - test_inverse
Then once you have a group G you can ask for G.check() which lauch automatically all those tests. Unfortunately this is buried in the category framework and cannot be used right now. (see [sage-devel] Generic tests and categories 6 Feb 2009). In the mean time I do this by hands.


---

Comment by hivert created at 2009-02-13 20:13:14

New version with a corrected typo (thanks Jason)


---

Attachment

*Review*
patch looks good except
 * typo: "seld" -> "self" (2402)
 * docstring INPUT block of `test_trivial_matrices_inverse` does not conform to Sage's conventions
 * "TODO: must be adapted to Nicolas check framework (see trac FIXME)." The FIXME should probably be addressed

i.e. all issues are trivial.

I didn't run doctests yet, will do now.


---

Comment by mabshoff created at 2009-02-14 16:42:19

I have doctested this patch on top of #5242 and #5244 in my current Sage 3.3.rc1 merge tree and:

```
All tests passed!
```


Cheers,

Michael


---

Comment by hivert created at 2009-02-14 17:46:01

Replying to [comment:4 malb]:
Done ! See the new patch. 

Note that I currently didn't had time to check it. It's currently being done on my machine but it takes times. I only change docs from the first version but who knows...


---

Comment by hivert created at 2009-02-14 19:30:20

Reupped after malb request on irc.


---

Attachment

Positive review on trivial_matrices_inverse-5256-submitted.patch.


---

Comment by mhansen created at 2009-02-14 23:38:05

Note that there is #5274 for the TODO/FIXME.


---

Comment by mabshoff created at 2009-02-15 07:17:43

Merged trivial_matrices_inverse-5256-submitted.patch in Sage 3.3.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-15 07:17:43

Resolution: fixed

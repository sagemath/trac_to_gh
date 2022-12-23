# Issue 8977: Bug in QuadraticForm.rational_diagonal_form()

Issue created by migration from https://trac.sagemath.org/ticket/8977

Original creator: gdrama

Original creation time: 2010-05-16 01:16:41

Assignee: justin

CC:  tornaria jonhanke

Keywords: rational_diagonal_form()

The function rational_diagonal_form() fails in some quadratic forms. For example:

```
sage: Q = QuadraticForm(ZZ,2,[0,1,-1])
sage: Q
Quadratic form in 2 variables over Integer Ring with coefficients: 
[ 0 1 ]
[ * -1 ]


sage: Q.rational_diagonal_form()
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)

/home/gustavo/<ipython console> in <module>()

/home/gustavo/sage-4.3.3/local/lib/python2.6/site-packages/sage/quadratic_forms/quadratic_form__local_field_invariants.pyc in rational_diagonal_form(self, return_matrix)
    113         for j in range(i+1, n):
    114             if Q[i,j] != 0:
--> 115                 temp[i,j] = -Q[i,j] / (Q[i,i] * 2)    ## This should only occur when Q[i,i] != 0, which the above step guarantees.
    116 
    117         Q = Q(temp)

/home/gustavo/sage-4.3.3/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__div__ (sage/structure/element.c:11882)()

/home/gustavo/sage-4.3.3/local/lib/python2.6/site-packages/sage/rings/rational.so in sage.rings.rational.Rational._div_ (sage/rings/rational.c:14641)()

ZeroDivisionError: Rational division by zero
```



---

Comment by tornaria created at 2010-05-18 20:33:32

I think a short explanation of the bug (and the fix) here in trac would be useful. Also, adding an example to the docstring to test for this would be nice.

Otherwise, the patch seems reasonable, asuming I understood it correctly (I _can_ reproduce the bug, but I did _not_ try the fix)


---

Comment by gdrama created at 2010-05-28 01:24:01

Changed the patch to add the example given to the doctest, and fixed the doctest also.


---

Comment by tornaria created at 2010-12-03 11:50:18

Changing status from new to needs_review.


---

Comment by mstreng created at 2011-01-16 14:22:42

The patch fails to apply (4.6.1.rc1).
Also, the INPUT and OUTPUT blocks should only have a single colon (see [here](http://www.sagemath.org/doc/developer/conventions.html))


---

Comment by mstreng created at 2011-01-16 14:22:42

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by gdrama created at 2011-02-05 15:32:58

I fixed the patch for sage-4.6.1 and make the corrections mstreng told.


---

Comment by mstreng created at 2011-02-06 23:50:25

Can anyone reproduce this? A seemingly unrelated doctest fails.

```
The following tests failed:

        sage -t -long devel/sage/sage/groups/matrix_gps/matrix_group.py # 4 doctests failed
```

All 4 are of the following form:

```
File "/storage/marco/sage-4.6.1/devel/sage-main/sage/groups/matrix_gps/matrix_group.py", line 668:
    sage: G.random_element()
Expected:
    [2 1 1 1]
    [1 0 2 1]
    [0 1 1 0]
    [1 0 0 1]
Got:
    [0 1 1 0]
    [1 2 2 2]
    [1 1 1 0]
    [2 0 1 2]
```

I tried removing and reapplying the patch. All tests pass on an unpatched 4.6.2.alpha3, and 4 tests of the form `G.random_element()` fail with the patch applied. I've had problems like this before with other tickets, so I won't change this ticket to needs_work (yet).

Oops, it seems that the ticket still is needs_work. Was it not ready for review yet?


---

Comment by tornaria created at 2011-02-07 00:41:11

Changing status from needs_work to needs_review.


---

Comment by tornaria created at 2011-02-07 00:41:11

I don't think the issue you reported above (about matrix groups `random_element()`) is related in any way to this ticket.

The patch is pretty straightforward, is almost one-liner, and clearly changes only the `rational_diagonal_form()` method.

I've just tried on 4.6.1 and:
 a. the bug is reproducible
 b. the doctest in the patch triggers the bug
 c. after applying the patch, the bug is fixed, and the doctest passes.

----

I also tried long-doctesting the `matrix_group.py` file (with the patch applied) but got no error.

Maybe it's showing randomly for you (and you think it's correlated to the patch in this ticket, but is not). Or perhaps something in 4.6.2.alpha3 is affecting this.

----

In my opinion, the patch is ready. I'll switch to "needs_review", in the hope that somebody else gives the positive review soon.


---

Comment by mstreng created at 2011-02-07 20:39:44

Fresh install, no more failing doctests.

I already clicked "positive_review", and then noticed that the first line of the patch only says "Trac" instead of giving the ticket number and a description of the patch. I'm afraid it would only be set back to "needs_work" by the release manager, as happened [here](http://trac.sagemath.org/sage_trac/ticket/10702#comment:3).


---

Attachment

added ticket description to patch


---

Comment by mstreng created at 2011-02-07 20:52:33

Apply trac_8977_rational_diagonal_form_fix2.patch


---

Comment by tornaria created at 2011-03-08 20:36:20

Can we merge this, please?


---

Comment by tornaria created at 2011-03-08 20:36:20

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-03-17 19:22:45

Resolution: fixed

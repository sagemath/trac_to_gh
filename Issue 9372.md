# Issue 9372: implement regulator function for elliptic curves over number fields

Issue created by migration from https://trac.sagemath.org/ticket/9372

Original creator: cremona

Original creation time: 2010-06-29 04:58:30

Assignee: AlexGhitza

CC:  robertwb

Now that we have canonical heights over number fields, the regulator_of_points code can be moved up from ell_rational_field to ell_number_field.


---

Comment by cremona created at 2010-06-29 04:58:48

Changing component from algebra to elliptic curves.


---

Comment by cremona created at 2010-06-29 04:58:48

Changing assignee from AlexGhitza to cremona.


---

Comment by cremona created at 2010-06-29 05:54:25

Applies to 4.4.4


---

Attachment

The patch moves the two functions height_pairing_matrix and regulator_of_points, and adds doctests over number fields.


---

Comment by cremona created at 2010-06-29 05:56:28

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-06-29 13:03:47

I'm getting a couple of doctest failures -- something is off by a sign in the `height_pairing_matrix` code:

```
sage -t -long ell_number_field.py
**********************************************************************
File "/storage/masiao/sage-4.4.4/devel/sage-reviewing/sage/schemes/elliptic_curves/ell_number_field.py", line 308:
    sage: E.height_pairing_matrix([P,Q])
Expected:
    [ 0.686667083305587 -0.268478098806726]
    [-0.268478098806726  0.327000773651605]
Got:
    [0.686667083305587 0.268478098806726]
    [0.268478098806726 0.327000773651605]
**********************************************************************
File "/storage/masiao/sage-4.4.4/devel/sage-reviewing/sage/schemes/elliptic_curves/ell_number_field.py", line 317:
    sage: EK.height_pairing_matrix([EK(P),EK(Q)])
Expected:
    [ 0.686667083305586 -0.268478098806726]
    [-0.268478098806726  0.327000773651605]
Got:
    [0.686667083305586 0.268478098806726]
    [0.268478098806726 0.327000773651605]
**********************************************************************
1 items had failures:
   2 of  23 in __main__.example_4
***Test Failed*** 2 failures.
```


Also, a very tiny quibble: the second argument "precision" to `height_pairing_matrix` is missing its bullet point in the docstring.


---

Comment by davidloeffler created at 2010-06-29 13:03:47

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-06-29 14:38:37

Probably I used E.gens() which is a bad idea in odctests, better to enter the points manually.

No time to fix now, about to leave SD22 for home.... but thanks all the same!  Put this patch up from a coffee shop last night just before it closed (about a dozen Sagers being chased out!)


---

Comment by aly.deines created at 2010-06-29 23:42:37

`@`cremona: You did you E.gens().  I get:

```
sage: E = EllipticCurve('389a1')
sage: E.gens()
[(-1 : 1 : 1), (0 : -1 : 1)]
```


Should I change the doc test to the following?


```
sage: E = EllipticCurve('389a1')
sage: P,Q = E.point([-1,1,1]),E.point([0,-1,1])
sage: E.height_pairing_matrix([P,Q])
[0.686667083305587 0.268478098806726]
[0.268478098806726 0.327000773651605]
```


}}}


---

Comment by aly.deines created at 2010-06-30 03:34:18

doctest fixed -- replaces previous patch


---

Comment by aly.deines created at 2010-06-30 03:35:34

Changing status from needs_work to needs_review.


---

Attachment

If the only problem was that the doctest called E.gens(), this fixes those doctests and you can give this a positive review.


---

Comment by robertwb created at 2010-06-30 07:25:58

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-06-30 11:43:14

Thanks to all for sorting that out.  I should have known better.  Even for curves in the database, it is not safe to use gens() since unless you have the larger database installed the gens are computed on the fly and are not unique.  (And doctests definitely should not assume an optional spkg is installed!).


---

Comment by mpatel created at 2010-07-20 07:17:21

Resolution: fixed


---

Comment by mpatel created at 2010-07-20 07:17:21

I'm updating the Reviewer(s) field.  Please correct me if I'm wrong.

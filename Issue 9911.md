# Issue 9911: extraneous argument in deprecation in #7154

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-09-15 13:47:29

Assignee: jason, was

CC:  ryan

In #7154, the rename_keyword deprecation decorator has an extra argument.  Right now, it's:


```
`@`rename_keyword(deprecated='Sage 4.6', deprecated_option='thickness', thickness='width') 
```


but should just be


```
`@`rename_keyword(deprecated='Sage 4.6', thickness='width') 
```


My bad for not catching this in the review stage.


---

Comment by leif created at 2010-09-16 09:04:51

Just for the record, this then also needs to be fixed:

```
sage -t -long "devel/sage/sage/geometry/polyhedra.py"       
**********************************************************************
File "/home/leif/Sage/sage-4.6.alpha1/devel/sage/sage/geometry/polyhedra.py", line 1270:
    sage: p1.projection().show() + p2.projection().show() + p3.projection().show()
Expected nothing
Got:
    doctest:4555: DeprecationWarning: (Since Sage 4.6) use the option 'width' instead of 'thickness'
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of  14 in __main__.example_66
***Test Failed*** 1 failures.
```



---

Comment by jason created at 2010-09-16 09:16:00

Leif: is that the only failure in all long doctests (i.e., ptestlong or similar?)

If not, I'll run ptestlong to check.


---

Comment by leif created at 2010-09-16 09:25:44

Replying to [comment:2 jason]:
> Leif: is that the only failure in all long doctests (i.e., ptestlong or similar?)

The only one related to this (`DeprecationWarning`) with the _unreleased_ 4.6.alpha1.

If you put the deprecation warning into the doctest ("expected"), don't forget to not hard-code the line number (from `ncadoctest.py`!).


---

Comment by mkoeppe created at 2021-09-10 06:55:41

Outdated, should close


---

Comment by mkoeppe created at 2021-09-10 06:55:41

Changing status from new to needs_review.


---

Comment by klee created at 2021-09-10 11:08:31

I agree


---

Comment by klee created at 2021-09-10 11:08:39

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2021-09-10 17:33:19

Resolution: invalid

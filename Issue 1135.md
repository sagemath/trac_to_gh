# Issue 1135: Error in preparsing generators, QuadraticField

Issue created by migration from https://trac.sagemath.org/ticket/1135

Original creator: ncalexan

Original creation time: 2007-11-09 21:03:33

Assignee: ncalexan

Keywords: preparse generators QuadraticField


```
sage: K.<a> = QuadraticField(-55, 'a')
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/ncalexan/emacs/<ipython console> in <module>()

<type 'exceptions.TypeError'>: QuadraticField() got multiple values for keyword argument 'names'
```



---

Comment by davidloeffler created at 2010-04-16 16:03:05

This clearly belongs in "number fields" ("interfaces" is for Sage interfaces to other software, not for user-interface issues).


---

Comment by davidloeffler created at 2010-04-16 16:03:05

Changing component from interfaces to number fields.


---

Attachment


---

Comment by lftabera created at 2010-09-17 14:58:40

Changing status from new to needs_review.


---

Comment by lftabera created at 2010-09-17 14:58:40

This is a small error that is embarrasingly old. This patch solves the problem. You can use a generator name and the preparser in all combinations.

- I have added a default name for the generator 'a' to be consistent with NumberField.

- I have documented the behaviour of Sage when QuadraticField and NumberField are given two generators but there is a conflict in their names. The generator name given by the preparser has precedence in this case.


---

Comment by ncalexan created at 2010-09-17 15:21:09

Looks fine to me and passes tests on sage.math.  Positive review!


---

Comment by ncalexan created at 2010-09-17 15:21:09

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-28 10:55:02

Resolution: fixed

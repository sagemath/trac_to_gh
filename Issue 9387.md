# Issue 9387: Add method for elliptic curves over number fields

Issue created by migration from Trac.

Original creator: justin

Original creation time: 2010-06-29 23:32:43

Assignee: cremona

Keywords: elliptic curve, tamagawa number

Elliptic curves over the rationals have a method that returns a list of tamagawa numbers for the curve.  There is no such method in the case of number fields.



---

Comment by justin created at 2010-06-29 23:39:11

Added patch with the method tamagawa_numbers(), essentially a duplication of the code for the rational case.


---

Comment by justin created at 2010-06-29 23:39:11

Changing status from new to needs_review.


---

Comment by justin created at 2010-06-29 23:53:20

Updated the patch with a corrected doctest (run and passed).


---

Comment by davidloeffler created at 2010-06-30 08:24:46

Just a suggestion: why duplicate the code? Since `EllipticCurve_rational_field` inherits from `EllipticCurve_number_field`, you could just *move* the code. Then we don't have the overhead of maintaining two routines doing exactly the same, and the likelihood of bugs is halved. Compare John's regulator patch at #9372.


---

Comment by cremona created at 2010-06-30 11:20:48

That's a good idea.  Justin, all that's needed is (a) delete the version in ell_rational_field, (b) make sure that the code in ell_number_field works over Q (say by moving the old doctest into the new function -- it should have examples over Q and over another field.

There might be other functions like this.  If you notice any, make a ticket!


---

Comment by cremona created at 2010-06-30 11:20:48

Changing status from needs_review to needs_work.


---

Comment by justin created at 2010-06-30 22:26:50

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-07-02 20:19:03


```
sage -t  ell_number_field.py
**********************************************************************
File "/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/schemes/elliptic_curves/ell_number_field.py", line 1049:
    sage: K=NumberField(x^2+3)
Exception raised:
    Traceback (most recent call last):
      File "/storage/masiao/sage-4.5.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/masiao/sage-4.5.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/storage/masiao/sage-4.5.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_22[5]>", line 1, in <module>
        K=NumberField(x**Integer(2)+Integer(3))###line 1049:
    sage: K=NumberField(x^2+3)
      File "/storage/masiao/sage-4.5.alpha1/local/lib/python/site-packages/sage/rings/number_field/number_field.py", line 431, in NumberField
        raise TypeError, "You must specify the name of the generator."
    TypeError: You must specify the name of the generator.
**********************************************************************                           
```


You should also probably delete, rather than comment out, the code in ell_rational_field.


---

Comment by davidloeffler created at 2010-07-02 20:19:03

Changing status from needs_review to needs_work.


---

Comment by justin created at 2010-07-02 22:20:24

OK, that's weird.  Turns out I popped when I should have pushed, so I was testing unmodified code.  I'll be back.


---

Attachment

New version of patch following DavidL's suggestion


---

Comment by justin created at 2010-07-02 23:31:58

New patch, replacing previous one.  This time, with some luck, I verified the patch against both 4.4.4 and 4.5.a1.

Comments, brickbats, scotch all welcome.


---

Comment by justin created at 2010-07-02 23:31:58

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-07-03 08:29:52

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-07-03 08:29:52

Looks good to me.


---

Comment by mpatel created at 2010-07-20 07:17:38

Resolution: fixed

# Issue 6083: speedup integer division

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-05-19 07:35:58

Assignee: somebody

remove _sig_on and _sig_off for small operands, specialize for int divisor


---

Attachment


---

Comment by fredrik.johansson created at 2009-06-03 18:43:05

I now get one trivial test failure (changed exception message):


```
File "/home/fredrik/sage-4.0/devel/sage-mpmath/sage/rings/integer.pyx", line 2163:
    sage: z % 0
Expected:
    Traceback (most recent call last):
    ...
    ZeroDivisionError: Integer modulo by zero
Got:
    Traceback (most recent call last):
      File "/space/wstein/farm/sage-4.0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/wstein/farm/sage-4.0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/wstein/farm/sage-4.0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_46[4]>", line 1, in <module>
        z % Integer(0)###line 2163:
    sage: z % 0
      File "integer.pyx", line 2189, in sage.rings.integer.Integer.__mod__ (sage/rings/integer.c:15033)
    ZeroDivisionError: other must be nonzero
```


Otherwise, this patch has my approval.


---

Comment by robertwb created at 2009-06-03 19:00:04

Thanks for looking at these. I'll fix this (the original error seems better).


---

Comment by craigcitro created at 2009-06-05 04:47:48

This patch looks good. I've added a referee patch that makes a few really minor changes:

 * removes the unused `_floordiv` function
 * changes the error messages: they all now say either "Integer division by zero" or "Integer modulo by zero." I think these are more informative, and they also now mirror the Python ones (which all say "integer division or modulus by zero"). The old ones were of the form `"other (=%s) must be nonzero"%other`, and by definition *always* had other equal to 0, so that just seemed silly. 

Unless Robert or Fredrik has any objections to the second patch, I'd say this is good to go.


---

Comment by robertwb created at 2009-06-05 11:15:05

Yep, looks good.


---

Comment by ncalexan created at 2009-06-13 21:06:14

Unfortunately, this causes a segfault with the 4.0.2.alpha0 singular:

```
----------------------------------------------------------------------

The following tests failed:

        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # Segfault
----------------------------------------------------------------------
Total time for all tests: 524.4 seconds
Tests failed!
```



---

Attachment

It turns out the segfault was coming from an infinite loop in Cython. The issue was that after the first patch above, doing `Integer % IntegerMod_gmp` would call into the `__mod__` on `IntegerMod_gmp`, which tried to check if something was zero by doing something of the form `Integer % IntegerMod_gmp` ... and repeat ad infinitum. 

So the new patch adds a small snippet to fix this, and a doctest.


---

Comment by cremona created at 2009-06-28 13:18:18

Although I have not been following all the details of this one, I applied all patches successfully to 4.1.alpha2 and ran -testall successfully, so I'm giving it a positive review.


---

Comment by rlm created at 2009-07-04 02:09:23

Resolution: fixed

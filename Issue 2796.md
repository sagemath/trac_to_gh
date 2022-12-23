# Issue 2796: Integer digits/ndigit disagree on default base

Issue created by migration from https://trac.sagemath.org/ticket/2796

Original creator: jbmohler

Original creation time: 2008-04-04 12:56:01

Assignee: somebody

I find this quite non-intuitive:

```
sage: n=15
sage: n.digits()
[1, 1, 1, 1]
sage: n.ndigits()
2
sage: n.bits()
4
```


The reason is that digits and ndigits have a different default for the base parameter.  I think they should both default to base=10.

I also think that 'bits' should be renamed to 'nbits' and possibly the 'bits' method should call 'digits(base=2)'.  I enter this with-out a patch for the moment because I wanted some feedback before I submit a patch which could break user code.  Please vote in this ticket.


---

Attachment

the attached patch changes the default base to 10 for digits, so that digits and ndigits agree:

```
sage: n=15
sage: n.digits()
[5, 1]
sage: n.ndigits()
2
```

As a consequence, calls to digits() were changed into digits(2).


---

Comment by cremona created at 2008-10-21 20:17:36

I like this as far as it goes, but would also like n.bits() to return n.digits(2) and n.nbits() to return what n.bits() currently does.  Can we add that too?


---

Attachment

Replying to [comment:2 cremona]:
> I like this as far as it goes, but would also like n.bits() to return n.digits(2) and n.nbits() to return what n.bits() currently does.  Can we add that too?

The second patch (to be applied after the 1st one) does this. sage -t -long * returned the following failures,
but I guess they are related to another patch. In any case the reviewer should check them before and after applying
the 2nd patch:

```
      sage -t -long devel/sage-main/sage/modular/modform/j_invariant.py
      sage -t -long devel/sage-main/sage/schemes/elliptic_curves/padics.py
      sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_generic.py
```



---

Comment by robertwb created at 2008-11-14 01:43:03

Looks good to me, and I think this is a good change too. 

I didn't get those modular/elliptic curve errors, so it must be due to something else.


---

Comment by mabshoff created at 2008-11-14 05:22:16

The two patches here cause the following failures:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.rc1$ ./sage -t -long devel/sage/sage/symbolic/expression.pyx
sage -t -long devel/sage/sage/symbolic/expression.pyx       
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/symbolic/expression.pyx", line 1269:
    sage: (x^3 - 1).gcd(x-1)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_38[4]>", line 1, in <module>
        (x**Integer(3) - Integer(1)).gcd(x-Integer(1))###line 1269:
    sage: (x^3 - 1).gcd(x-1)
      File "expression.pyx", line 1286, in sage.symbolic.expression.Expression.gcd (sage/symbolic/expression.cpp:5544)
      File "pynac.pyx", line 575, in sage.symbolic.pynac.py_int_length (sage/symbolic/pynac.cpp:7102)
    TypeError: an integer is required
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/symbolic/expression.pyx", line 1271:
    sage: (x^3 - 1).gcd(x^2+x+1)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_38[5]>", line 1, in <module>
        (x**Integer(3) - Integer(1)).gcd(x**Integer(2)+x+Integer(1))###line 1271:
    sage: (x^3 - 1).gcd(x^2+x+1)
      File "expression.pyx", line 1286, in sage.symbolic.expression.Expression.gcd (sage/symbolic/expression.cpp:5544)
      File "pynac.pyx", line 575, in sage.symbolic.pynac.py_int_length (sage/symbolic/pynac.cpp:7102)
    TypeError: an integer is required
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/symbolic/expression.pyx", line 1277:
    sage: gcd(x^3 - y^3, x-y)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_38[7]>", line 1, in <module>
        gcd(x**Integer(3) - y**Integer(3), x-y)###line 1277:
    sage: gcd(x^3 - y^3, x-y)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/lib/python2.5/site-packages/sage/rings/arith.py", line 1037, in gcd
        return a.gcd(b, **kwargs)
      File "expression.pyx", line 1286, in sage.symbolic.expression.Expression.gcd (sage/symbolic/expression.cpp:5544)
      File "pynac.pyx", line 575, in sage.symbolic.pynac.py_int_length (sage/symbolic/pynac.cpp:7102)
    TypeError: an integer is required
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/symbolic/expression.pyx", line 1279:
    sage: gcd(x^100-y^100, x^10-y^10)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_38[8]>", line 1, in <module>
        gcd(x**Integer(100)-y**Integer(100), x**Integer(10)-y**Integer(10))###line 1279:
    sage: gcd(x^100-y^100, x^10-y^10)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/lib/python2.5/site-packages/sage/rings/arith.py", line 1037, in gcd
        return a.gcd(b, **kwargs)
      File "expression.pyx", line 1286, in sage.symbolic.expression.Expression.gcd (sage/symbolic/expression.cpp:5544)
      File "pynac.pyx", line 575, in sage.symbolic.pynac.py_int_length (sage/symbolic/pynac.cpp:7102)
    TypeError: an integer is required
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/devel/sage/sage/symbolic/expression.pyx", line 1281:
    sage: gcd(expand( (x^2+17*x+3/7*y)*(x^5 - 17*y + 2/3) ), expand((x^13+17*x+3/7*y)*(x^5 - 17*y + 2/3)) )
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_38[9]>", line 1, in <module>
        gcd(expand( (x**Integer(2)+Integer(17)*x+Integer(3)/Integer(7)*y)*(x**Integer(5) - Integer(17)*y + Integer(2)/Integer(3)) ), expand((x**Integer(13)+Integer(17)*x+Integer(3)/Integer(7)*y)*(x**Integer(5) - Integer(17)*y + Integer(2)/Integer(3))) )###line 1281:
    sage: gcd(expand( (x^2+17*x+3/7*y)*(x^5 - 17*y + 2/3) ), expand((x^13+17*x+3/7*y)*(x^5 - 17*y + 2/3)) )
      File "/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/lib/python2.5/site-packages/sage/rings/arith.py", line 1037, in gcd
        return a.gcd(b, **kwargs)
      File "expression.pyx", line 1286, in sage.symbolic.expression.Expression.gcd (sage/symbolic/expression.cpp:5544)
      File "pynac.pyx", line 575, in sage.symbolic.pynac.py_int_length (sage/symbolic/pynac.cpp:7102)
    TypeError: an integer is required
**********************************************************************
1 items had failures:
   5 of  10 in __main__.example_38
***Test Failed*** 5 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.rc1/tmp/.doctest_expression.py
	 [10.3 s]
exit code: 1024
 
----------------------------------------------------------------------
```



---

Comment by robertwb created at 2008-11-14 06:25:38

Hmm... this seems totally unrelated to the ticket. Given 3.2 is out soon, I'll see again if there's any interaction with the symbolic code.


---

Attachment

apply after the previous two patches


---

Comment by AlexGhitza created at 2008-12-11 11:37:11

Ah yes, my shortest patch to date.  Apply trac_2796b.patch after the other two to fix the symbolic/expression.pyx failure.

It is of course trivial, yet it took about half an hour to find...

The first two patches look good to me, otherwise.


---

Comment by robertwb created at 2008-12-12 01:37:11

Looks like that fixed it. Positive review on all three patches.


---

Comment by zimmerma created at 2008-12-12 07:30:55

Indeed. I have checked the first three tests and the last one, and all four pass now.


---

Comment by mabshoff created at 2008-12-12 13:48:20

Resolution: fixed


---

Comment by mabshoff created at 2008-12-12 13:48:20

Merged in Sage 3.2.2.alpha2

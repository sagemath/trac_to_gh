# Issue 5096: implement beautiful printing support for pynac

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-25 08:14:36

Assignee: burcin

CC:  mhansen




---

Comment by was created at 2009-01-25 08:15:26

See http://sage.math.washington.edu/home/burcin/pynac for the new spkg and patches to the core sage library.


---

Comment by was created at 2009-01-25 08:29:59

REFEREE REPORT:

 * Add a short description at the top docstring for `x.operator?`.

 * Make sure the latex docstring actually passes.


---

Attachment

add .operator() method


---

Comment by burcin created at 2009-01-30 13:55:31

allow pynac expressions as arguments to binomial and factorial


---

Attachment

add iterator and __getitem__ support to expressions


---

Comment by burcin created at 2009-01-30 13:56:40

.subs() now works with multiple arguments


---

Attachment

fix doctests for printing changes


---

Comment by burcin created at 2009-01-30 13:57:44

add .collect_common_factors() method


---

Attachment

add latex printing support, fix is_integer method


---

Attachment

correct coercion of symbolic constants


---

Comment by burcin created at 2009-01-30 14:04:48

Changing status from new to assigned.


---

Comment by burcin created at 2009-01-30 14:04:48

A new version of pynac is available here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.2.spkg


The attached patches implement various enhancements to the pynac interface.

This issue now depends on #5132.


---

Comment by mabshoff created at 2009-02-02 06:52:40

The spkg looks good, but someone needs to review Burcin's nine patches to the Sage library :)

Cheers,

Michael


---

Comment by mhansen created at 2009-02-02 07:18:59

Assuming the patches apply and pass tests, I think these can go in.  All of the changes are pretty straightforward.


---

Comment by mabshoff created at 2009-02-02 07:42:25

With the new spkg and all nine patches applied I am seeing two doctest failures:

```
	sage -t -long devel/sage/sage/calculus/calculus.py # 6 doctests failed
	sage -t -long devel/sage/sage/modules/free_module_element.pyx # 1 doctests failed
```

They all seem to be of the kind

```
sage -t -long "devel/sage/sage/modules/free_module_element.pyx"
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha4/devel/sage/sage/modules/free_module_element.pyx", line 1637:
    sage: g(x=3, y=2)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_52[11]>", line 1, in <module>
        g(x=Integer(3), y=Integer(2))###line 1637:
    sage: g(x=3, y=2)
      File "free_module_element.pyx", line 1640, in sage.modules.free_module_element.FreeModuleElement_generic_dense.__call__ (sage/modules/free_module_element.c:13259)
      File "/scratch/mabshoff/sage-3.3.alpha4/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 6044, in __call__
        raise ValueError, "Expected %s arguments, got %s"%(len(myvars),len(args))
    ValueError: Expected 2 arguments, got 0
**********************************************************************
```


Cheers,

Michael


---

Comment by burcin created at 2009-02-02 14:25:09

I uploaded a new version of trac_5096-09_callable_expression.patch which reverts the check for the number of arguments of `CallableSymbolicExpression`s. The doctests pass now.


---

Comment by burcin created at 2009-02-02 16:43:09

add .function() method to create `CallableSymbolicExpressions`


---

Attachment

Merged all nine patches as well as the spkg into Sage 3.3.alpha4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 17:20:02

Resolution: fixed

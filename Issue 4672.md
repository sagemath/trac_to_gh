# Issue 4672: plot functions do not work with ?? because they are wrapped in @options

Issue created by migration from https://trac.sagemath.org/ticket/4672

Original creator: jason

Original creation time: 2008-12-02 05:43:05

Assignee: was


```
sage: bar_chart??
Type:		function
Base Class:	<type 'function'>
String Form:	<function bar_chart at 0x88b4b1c>
Namespace:	Interactive
File:		/home/jason/sage/local/lib/python2.5/site-packages/sage/plot/misc.py
Definition:	bar_chart(*args, **kwds)
Source:
        @wraps(func)
        def wrapper(*args, **kwds):
            options = copy(wrapper.options)
            if self.original_opts:
                options['__original_opts'] = kwds
            options.update(kwds)
            return func(*args, **options)
```



---

Comment by mhansen created at 2008-12-02 06:00:34

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2008-12-02 06:00:34

Changing assignee from was to mhansen.


---

Comment by jason created at 2008-12-02 06:07:12

Code looks reasonable, applies (with fuzz) to my Sage 3.2, and fixes the issue pointed out above, so positive review.


---

Comment by was created at 2008-12-02 17:12:11

I also tried the code, etc., and it looks good, so another positive review from me. 

When I was reviewing though I noticed that, which has nothing a priori to do with this ticket but is worrisome. 

```
sage: a = plot(sin)
sage: a == loads(dumps(a))
False
```



---

Comment by mabshoff created at 2008-12-03 10:23:14

This patch breaks one doctest:

```
sage -t -long "devel/sage/sage/combinat/sloane_functions.py"
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/devel/sage/sage/combinat/sloane_functions.py", line 156:
    sage: sloane.A000045._sage_src_()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[2]>", line 1, in <module>
        sloane.A000045._sage_src_()###line 156:
    sage: sloane.A000045._sage_src_()
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/combinat/sloane_functions.py", line 160, in _sage_src_
        return sage_getsource(self.__class__)
      File "/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 367, in sage_getsource
        return obj._sage_src_()
    TypeError: unbound method _sage_src_() must be called with A000045 instance as first argument (got nothing instead)
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/tmp/.doctest_sloane_functions.py
	 [6.6 s]
exit code: 1024
```



---

Attachment


---

Comment by mhansen created at 2008-12-04 10:57:41

I've attached a second patch which fixes the issue.


---

Comment by mabshoff created at 2008-12-04 14:11:00

Mike's second patch fixes the issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-04 14:11:12

Merged in Sage 3.2.2.alpha0


---

Comment by mabshoff created at 2008-12-04 14:11:12

Resolution: fixed

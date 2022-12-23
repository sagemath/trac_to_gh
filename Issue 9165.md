# Issue 9165: cygwin: lcalc does not work for elliptic curves on cygwin

Issue created by migration from https://trac.sagemath.org/ticket/9165

Original creator: was

Original creation time: 2010-06-07 04:05:45

Assignee: tbd

lcalc works fine for the zeta function on cygwin, evidently:


```
sage: time lcalc.zeros(4)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.19 s
[14.1347251, 21.0220396, 25.0108576, 30.4248761]
```


However, it doesn't work for computing with elliptic curves:


```
sage -t  "devel/sage/sage/lfunctions/lcalc.py"              
  ***   not enough memory
  ***   not enough memory
  ***   not enough memory
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/lfunctions/lcalc.py", line 120:
    sage: lcalc.zeros(3, EllipticCurve('37a'))     # long
Expected:
    [0.000000000, 5.00317001, 6.87039122]
Got:
    []
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/lfunctions/lcalc.py", line 229:
    sage: E.lseries().values_along_line(0.5, 3, 5)
Expected:
    [(0, 0.209951303),
     (0.500000000, -...e-16),
     (1.00000000, 0.133768433),
     (1.50000000, 0.360092864),
     (2.00000000, 0.552975867)]
Got:
    lcalc:  
    []
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/lfunctions/lcalc.py", line 374:
    sage: lcalc.analytic_rank(E)
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[3]>", line 1, in <module>
        lcalc.analytic_rank(E)###line 374:
    sage: lcalc.analytic_rank(E)
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/lfunctions/lcalc.py", line 381, in analytic_rank
        return Z(s[i+6:])
      File "integer.pyx", line 614, in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6388)
    TypeError: unable to convert x (=) to an integer
**********************************************************************
3 items had failures:
   1 of   5 in __main__.example_2
   1 of   6 in __main__.example_5
   1 of   4 in __main__.example_8
***Test Failed*** 3 failures.
For whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_lcalc.py
	 [17.7 s]
```



---

Comment by was created at 2010-06-07 04:43:22

Another test failure resulting from lcalc not working:

```

sage -t  "devel/sage/sage/plot/line.py"                     
  ***   not enough memory
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/plot/line.py", line 375:
    sage: vals = E.lseries().values_along_line(1-I, 1+10*I, 100) # critical line
Expected nothing
Got:
    lcalc:  
**********************************************************************
1 items had failures:
```



---

Comment by drkirkby created at 2010-08-02 04:23:09

Note gcc gives many compiler warnings and SunStudio refuses to compile the source code. These matters are probably not entirely unrelated.


---

Comment by kcrisman created at 2011-08-02 02:29:47

The lfunctions/ directory appears to pass doctests on a recent build of mine on XP.


---

Comment by kcrisman created at 2011-08-02 02:33:33

plot/line.py also passes tests (though many others do not in plot/, perhaps due to "I" currently not working).


---

Comment by kcrisman created at 2011-08-19 14:36:12

But there is a segfault on the very first example above.  Strange that the tests pass.


---

Comment by kcrisman created at 2013-01-15 16:23:09

Changing status from new to needs_review.


---

Comment by kcrisman created at 2013-01-15 16:23:09

Changing priority from major to minor.


---

Comment by kcrisman created at 2013-01-15 16:23:09

These both pass and work "by hand" on XP now.  I do get warnings about the new stack size, which keeps going down from 1 MB to .981, .957, .955 with these commands, but they do _work_ (as does the one in line.py) so I would suggest a different ticket for handling the stack on Cygwin.

JP, can you confirm these pass on Win 7?  Then we should be set.


---

Comment by jpflori created at 2013-01-30 12:43:10

For info, this file passes its tests on my Windows 7 install (without #13351).

So let's close this one.


---

Comment by jpflori created at 2013-01-30 12:43:10

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-01-31 20:36:43

Resolution: worksforme

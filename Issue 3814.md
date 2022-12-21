# Issue 3814: [with patch, needs quick review] Bug introduced in trac #3800 fix

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-08-12 11:58:09

Assignee: craigcitro

I introduced a small bug in trac #3800, which John Cremona ran into while running doctests. Here's a chunk of code that illustrates the failure:


```
sage: chi = DirichletGroup(20).1**3 ; M = ModularSymbols(chi, weight=3, sign=1)

sage: M.cuspidal_subspace()
```


This raises an exception, but shouldn't be a problem. Patch coming up.


---

Comment by cremona created at 2008-08-12 19:56:43

Where's the patch??!


---

Comment by craigcitro created at 2008-08-12 20:49:21

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-08-12 20:49:21

Oops. Tag removed until I post the patch. ;)


---

Comment by craigcitro created at 2008-08-14 10:07:29

Ok, I'm posting a patch now.


---

Attachment

Patch code looks good to me, it applies cleanly to a fresh 3.1.alpha2, and all doctests in sage/modular ....passed (in 392s) except for these two:

```
	sage -t  devel/sage-3814/sage/modular/modsym/modsym.py
	sage -t  devel/sage-3814/sage/modular/modsym/boundary.py
```


Details:

```
sage -t  devel/sage-3814/sage/modular/modsym/modsym.py      **********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/modsym.py", line 51:
    sage: ModularSymbols(DirichletGroup(20).1**3, weight=3, sign=1).cuspidal_subspace()
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-3.1.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[17]>", line 1, in <module>
        ModularSymbols(DirichletGroup(Integer(20)).gen(1)**Integer(3), weight=Integer(3), sign=Integer(1)).cuspidal_subspace()###line 51:
    sage: ModularSymbols(DirichletGroup(20).1**3, weight=3, sign=1).cuspidal_subspace()
      File "/home/john/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 156, in cuspidal_subspace
        return self.cuspidal_submodule()
      File "/home/john/sage-3.1.alpha2/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py", line 896, in cuspidal_submodule
        assert d == S.dimension(), "According to dimension formulas the cuspidal subspace of \"%s\" has dimension %s; however, computing it using modular symbols we obtained %s, so there is a bug (please report!)."%(self, d, S.dimension())
    AssertionError: According to dimension formulas the cuspidal subspace of "Modular Symbols space of dimension 6 and level 20, weight 3, character [1, -zeta4], sign 1, over Cyclotomic Field of order 4 and degree 2" has dimension 3; however, computing it using modular symbols we obtained 2, so there is a bug (please report!).
**********************************************************************
1 items had failures:
   1 of  18 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/john/sage-3.1.alpha2/tmp/.doctest_modsym.py
	 [3.1 s]
```


and


```
sage -t  devel/sage-3814/sage/modular/modsym/boundary.py    **********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/boundary.py", line 794:
    sage: B._coerce_cusp(Cusp(0))
Expected:
    0
Got:
    [0]
**********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/boundary.py", line 813:
    sage: [ B(Cusp(i,7)) for i in range(7) ]
Expected:
    [[0], 0, 0, 0, 0, 0, 0]
Got:
    [[0], [1/7], [2/7], [3/7], -[3/7], -[2/7], -[1/7]]
**********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/boundary.py", line 816:
    sage: [ B(Cusp(i,7)) for i in range(7) ]
Expected:
    [0, [1/7], [2/7], [3/7], -[3/7], -[2/7], -[1/7]]
Got:
    [[0], [1/7], [2/7], [3/7], -[3/7], -[2/7], -[1/7]]
**********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/boundary.py", line 1003:
    sage: [ B(Cusp(i,11)) for i in range(11) ]
Expected:
    [[0], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Got:
    [[0], [1/11], -[1/11], [1/11], [1/11], [1/11], -[1/11], -[1/11], -[1/11], [1/11], -[1/11]]
**********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/boundary.py", line 1006:
    sage: [ B(Cusp(i,11)) for i in range(11) ]
Expected:
    [0,
    [1/11],
    -[1/11],
    [1/11],
    [1/11],
    [1/11],
    -[1/11],
    -[1/11],
    -[1/11],
    [1/11],
    -[1/11]]
Got:
    [[0], [1/11], -[1/11], [1/11], [1/11], [1/11], -[1/11], -[1/11], -[1/11], [1/11], -[1/11]]
**********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/boundary.py", line 1206:
    sage: [ B(Cusp(i,13)) for i in range(13) ]
Expected:
    [[0], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Got:
    [[0], [1/13], (-zeta4)*[1/13], [1/13], (-1)*[1/13], (-zeta4)*[1/13], (-zeta4)*[1/13], zeta4*[1/13], zeta4*[1/13], [1/13], (-1)*[1/13], zeta4*[1/13], (-1)*[1/13]]
**********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/boundary.py", line 1208:
    sage: B._coerce_cusp(Cusp(oo))
Expected:
    0
Got:
    [1/13]
**********************************************************************
File "/home/john/sage-3.1.alpha2/tmp/boundary.py", line 1211:
    sage: [ B(Cusp(i,13)) for i in range(13) ]
Expected:
    [0,
    [1/13],
    (-zeta4)*[1/13],
    [1/13],
    (-1)*[1/13],
    (-zeta4)*[1/13],
    (-zeta4)*[1/13],
    zeta4*[1/13],
    zeta4*[1/13],
    [1/13],
    (-1)*[1/13],
    zeta4*[1/13],
    (-1)*[1/13]]
Got:
    [[0], [1/13], (-zeta4)*[1/13], [1/13], (-1)*[1/13], (-zeta4)*[1/13], (-zeta4)*[1/13], zeta4*[1/13], zeta4*[1/13], [1/13], (-1)*[1/13], zeta4*[1/13], (-1)*[1/13]]
**********************************************************************
3 items had failures:
   3 of  20 in __main__.example_32
   2 of  15 in __main__.example_37
   3 of  14 in __main__.example_42
***Test Failed*** 8 failures.
For whitespace errors, see the file /home/john/sage-3.1.alpha2/tmp/.doctest_boundary.py
```


My guess is that some of these are caused by other differences between 3.1.alpha2 and whatever version Craig was working with.


---

Comment by cremona created at 2008-08-14 17:21:37

My mistake, apologies to Craig:  I forgot to do "sage -b" after applying the patches and testing.  Those two files do pass.

The patch is good!


---

Comment by mabshoff created at 2008-08-15 01:33:59

Resolution: fixed


---

Comment by mabshoff created at 2008-08-15 01:33:59

Merged in Sage 3.1.rc0

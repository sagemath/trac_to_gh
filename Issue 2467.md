# Issue 2467: sage-2.10.3: failures in tut.tex

Issue created by migration from https://trac.sagemath.org/ticket/2467

Original creator: was

Original creation time: 2008-03-11 02:26:45

Assignee: failure


```
sage -t  tut.tex                                            **********************************************************************
File "tut.py", line 1453:
    : eigvecs = g.eigenspaces()[0][1], g.eigenspaces()[1][1]; eigvecs
Expected:
    ([
    (1, 5)
    ], [
    (1, 1)
    ])
Got:
    (Vector space of degree 2 and dimension 1 over Finite Field of size 7
    User basis matrix:
    [1 5], Vector space of degree 2 and dimension 1 over Finite Field of size 7
    User basis matrix:
    [1 1])
**********************************************************************
File "tut.py", line 1604:
    : e.word_problem([b1,b2,b3,b4,b5],display=False)
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_63[7]>", line 1, in <module>
        e.word_problem([b1,b2,b3,b4,b5],display=False)###line 1604:
    : e.word_problem([b1,b2,b3,b4,b5],display=False)
    TypeError: word_problem() got an unexpected keyword argument 'display'
**********************************************************************
2 items had failures:
   1 of   4 in __main__.example_57
   1 of  16 in __main__.example_63
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_tut.tex
	 [17.5 s]
exit code: 256
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  tut.tex
```



---

Comment by mabshoff created at 2008-03-11 02:50:29

Resolution: fixed


---

Comment by mabshoff created at 2008-03-11 02:50:29

Same as #2371.

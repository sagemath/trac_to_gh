# Issue 675: Solaris 10: random_element: "ValueError: denominator must not be 0"

Issue created by migration from https://trac.sagemath.org/ticket/675

Original creator: mabshoff

Original creation time: 2007-09-17 00:38:46

Assignee: was

Keywords: Solaris 10


```
File "tut.py", line 1373:
    : A = M.random_element(density = 0.05)
Exception raised:
    Traceback (most recent call last):
      File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_53[1]>", line 1, in <module>
        _= A = M.random_element(density = RealNumber('0.05'))###line 1373:
    : A = M.random_element(density = 0.05)
      File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py", line 753, in random_element
        Z.randomize(density, *args, **kwds)
      File "matrix2.pyx", line 2595, in matrix2.Matrix.randomize
      File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/rings/rational_field.py", line 342, in random_element
        ZZ.random_element(distribution=distribution)))
      File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/rings/rational_field.py", line 182, in __call__
        return sage.rings.rational.Rational(x, base)
      File "rational.pyx", line 160, in rational.Rational.__init__
      File "rational.pyx", line 248, in rational.Rational.__set_value
    ValueError: denominator must not be 0
```



---

Comment by mabshoff created at 2007-09-17 01:24:28

Changing component from packages to doctest.


---

Comment by mabshoff created at 2007-09-17 01:24:28

Changing assignee from was to failure.


---

Comment by mabshoff created at 2008-01-20 20:14:41

This has been fixed in 2.9.x when making sure that 64 bits values in 32 bit mode on Solaris are long long.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-20 20:14:41

Resolution: fixed

# Issue 953: the axiom / sage interface is currently totally broken, at least on 64-bit linux

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-20 23:49:20

Assignee: was

With  axiom4sage-0.3.1 installed:

This is terrible.  


```
was`@`ubuntu:~/d/sage/sage/interfaces$ sage -t --optional axiom.py
sage -t --optional axiom.py                                 **********************************************************************
File "axiom.py", line 38:
    sage: axiom('3 * 5')                     # optional
Expected:
    15
Got:
    <BLANKLINE>
**********************************************************************
File "axiom.py", line 40:
    sage: a = axiom(3) * axiom(5); a         # optional
Expected:
    15
Got:
    <BLANKLINE>
      5                                                                                                                                                                                                                          Type: PositiveInteger
**********************************************************************
File "axiom.py", line 56:
    sage: F = axiom.factor('x^5 - y^5'); F      # optional
Expected:
               4      3    2 2    3     4
    - (y - x)(y  + x y  + x y  + x y + x )
Got:
    15
**********************************************************************
File "axiom.py", line 61:
    sage: F.type()                              # optional
Expected:
    Factored Polynomial Integer
Got:
    PositiveInteger
**********************************************************************
File "axiom.py", line 69:
    sage: a = axiom('2/3'); a          # optional
Expected:
    2
    -
    3
Got:
    <BLANKLINE>
**********************************************************************
File "axiom.py", line 73:
    sage: str(a)                       # optional
Expected:
    '2/3'
Got:
    '             4      3    2 2    3     4\r\n  - (y - x)(y  + x y  + x y  + x y + x )'
**********************************************************************
File "axiom.py", line 76:
    sage: str(a)                       # optional
Expected:
    'x*x+3/7'
Got:
    ''
**********************************************************************
File "axiom.py", line 84:
    sage: print axiom.eval('factor(x^5 - y^5)')   # optional
Expected:
               4      3    2 2    3     4
    - (y - x)(y  + x y  + x y  + x y + x )
    <BLANKLINE>
    Type: Factored Polynomial Integer
Got:
    unparse(sage2::InputForm)

       >> Fortran translation error:
       No corresponding Fortran structure for:

       (y - x) :: Polynomial Integer

       >> Fortran translation error:
       No corresponding Fortran structure for:

         4      3    2 2    3     4
       (y  + x y  + x y  + x y + x ) :: Polynomial Integer

       (10)  "-primeFactor(,1)*primeFactor(,1)"
                                                                                                                                                                                                                                             Type: String
    <BLANKLINE>
**********************************************************************
File "axiom.py", line 94:
    sage: f^2                                     # optional
Expected:
     10     5 5    10
    y   - 2x y  + x
Got:
    <BLANKLINE>
**********************************************************************
File "axiom.py", line 97:
    sage: f.factor()                              # optional
Expected:
               4      3    2 2    3     4
    - (y - x)(y  + x y  + x y  + x y + x )
Got:
    <BLANKLINE>
      2  -  3                                                                                                                                                                                                                        Type: Fraction Integer
**********************************************************************
File "axiom.py", line 110:
    sage: axiom('1/100 + 1/101')                  # optional
Expected:
       201
      -----
      10100
Got:
    <BLANKLINE>
       2   3  x  + -       7                                                                                                                                                                                                             Type: Polynomial Fraction Integer
**********************************************************************
File "axiom.py", line 115:
    sage: a = axiom('(1 + sqrt(2))^5'); a         # optional
Expected:
         +-+
      29\|2  + 41
Got:
                 4      3    2 2    3     4  - (y - x)(y  + x y  + x y  + x y + x )                                                                                                                                                                                                             Type: Factored Polynomial Integer
**********************************************************************
File "axiom.py", line 458:
    sage: v = axiom('[i*x^i for i in 0..5]'); v          # optional
Expected:
           2   3   4   5
    [0,x,2x ,3x ,4x ,5x ]
Got:
    <BLANKLINE>
      2                                                                                                                                                                                                                         Type: PositiveInteger
**********************************************************************
File "axiom.py", line 461:
    sage: v[4]                                           # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[1]>", line 1, in <module>
        v[Integer(4)]                                           # optional###line 461:
    sage: v[4]                                           # optional
      File "/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py", line 472, in __getitem__
        if n <= 0 or n > len(self):
      File "/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py", line 444, in __len__
        return int(s[:i-1])
    ValueError: invalid literal for int() with base 10: '10     5 5    10\r\n  y   - 2x y  + x\r\n                                                                                                                                                                   '
**********************************************************************
File "axiom.py", line 464:
    sage: v[1]                                           # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[2]>", line 1, in <module>
        v[Integer(1)]                                           # optional###line 464:
    sage: v[1]                                           # optional
      File "/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py", line 472, in __getitem__
        if n <= 0 or n > len(self):
      File "/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py", line 444, in __len__
        return int(s[:i-1])
    ValueError: invalid literal for int() with base 10: ''
**********************************************************************
File "axiom.py", line 466:
    sage: v[10]                                          # optional
Expected:
    Traceback (most recent call last):
    ...
    IndexError: index out of range
Got:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[3]>", line 1, in <module>
        v[Integer(10)]                                          # optional###line 466:
    sage: v[10]                                          # optional
      File "/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py", line 472, in __getitem__
        if n <= 0 or n > len(self):
      File "/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py", line 444, in __len__
        return int(s[:i-1])
    ValueError: invalid literal for int() with base 10: ''
**********************************************************************
File "axiom.py", line 359:
    sage: a == b                                      # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[1]>", line 1, in <module>
        a == b                                      # optional###line 359:
    sage: a == b                                      # optional
      File "element.pyx", line 623, in element.Element.__richcmp__
      File "element.pyx", line 595, in element.Element._richcmp
      File "/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py", line 381, in __cmp__
        elif P('%s > %s'%(self.name(), other.name())).__repr__().strip() == t:
      File "/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py", line 417, in __repr__
        return self.str()
      File "/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py", line 404, in str
        raise RuntimeError, s
    RuntimeError: unparse(sage5::InputForm)

       >> Fortran translation error:
       No corresponding Fortran structure for:

       (y - x) :: Polynomial Integer

       >> Fortran translation error:
       No corresponding Fortran structure for:

         4      3    2 2    3     4
       (y  + x y  + x y  + x y + x ) :: Polynomial Integer

       (23)  "-primeFactor(,1)*primeFactor(,1)"
                                                                                                                                                                                                                                             Type: String

**********************************************************************
File "axiom.py", line 365:
    sage: b < a                                       # optional
Expected:
    False
Got:
    True
**********************************************************************
File "axiom.py", line 367:
    sage: b > a                                       # optional
Expected:
    True
Got:
    False
**********************************************************************
File "axiom.py", line 438:
    sage: len(v)                                      # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_9[1]>", line 1, in <module>
        len(v)                                      # optional###line 438:
    sage: len(v)                                      # optional
      File "/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py", line 444, in __len__
        return int(s[:i-1])
    ValueError: invalid literal for int() with base 10: ''
**********************************************************************
4 items had failures:
  12 of  18 in __main__.example_0
   4 of   4 in __main__.example_10
   3 of   8 in __main__.example_7
   1 of   2 in __main__.example_9
***Test Failed*** 20 failures.
For whitespace errors, see the file .doctest_axiom.py
         [3.8 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:


        sage -t --optional axiom.py
Total time for all tests: 3.8 seconds

```



---

Comment by was created at 2007-10-20 23:49:29

Changing component from algebraic geometry to interfaces.


---

Comment by cwitty created at 2007-10-21 00:35:30

My results on my laptop and on sage.math are much better.  Here are the doctest failures I get:

```
sage -t -optional el/sage-bday2/sage/interfaces/axiom.py    **********************************************************************
File "axiom.py", line 56:
    sage: F = axiom.factor('x^5 - y^5'); F      # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/cwitty/sage/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[5]>", line 1, in <module>
        F = axiom.factor('x^5 - y^5'); F      # optional###line 56:
    sage: F = axiom.factor('x^5 - y^5'); F      # optional
      File "/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/axiom.py", line 417, in __repr__
        return self.str()
      File "/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/axiom.py", line 404, in str
        raise RuntimeError, s
    RuntimeError: unparse(sage2::InputForm)

    unparse(sage2::InputForm)
�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C

     

       >> Fortran translation error:

       No corresponding Fortran structure for:

    

       (y - x) :: Polynomial Integer

     

       >> Fortran translation error:

       No corresponding Fortran structure for:

    

         4      3    2 2    3     4

       (y  + x y  + x y  + x y + x ) :: Polynomial Integer

    

       (10)  "-primeFactor(,1)*primeFactor(,1)"

                                                                                                                                                                                                                                             Type: String


**********************************************************************
File "axiom.py", line 69:
    sage: a = axiom('2/3'); a          # optional
Expected:
    2
    -
    3
Got:
    2/3
**********************************************************************
File "axiom.py", line 73:
    sage: str(a)                       # optional
Expected:
    '2/3'
Got:
    '  2\r\n  -\r\n  3'
**********************************************************************
File "axiom.py", line 76:
    sage: str(a)                       # optional
Expected:
    'x*x+3/7'
Got:
    '   2   3\r\n  x  + -\r\n       7'
**********************************************************************
File "axiom.py", line 94:
    sage: f^2                                     # optional
Expected:
     10     5 5    10
    y   - 2x y  + x
Got:
    y**10+(-2*x**5*y**5)+x**10
**********************************************************************
File "axiom.py", line 97:
    sage: f.factor()                              # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/cwitty/sage/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[15]>", line 1, in <module>
        f.factor()                              # optional###line 97:
    sage: f.factor()                              # optional
      File "/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/axiom.py", line 417, in __repr__
        return self.str()
      File "/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/axiom.py", line 404, in str
        raise RuntimeError, s
    RuntimeError: unparse(sage5::InputForm)
�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C�[C

     

       >> Fortran translation error:

       No corresponding Fortran structure for:

    

       (y - x) :: Polynomial Integer

     

       >> Fortran translation error:

       No corresponding Fortran structure for:

    

         4      3    2 2    3     4

       (y  + x y  + x y  + x y + x ) :: Polynomial Integer

    

       (23)  "-primeFactor(,1)*primeFactor(,1)"

                                                                                                                                                                                                                                             Type: String


**********************************************************************
File "axiom.py", line 110:
    sage: axiom('1/100 + 1/101')                  # optional
Expected:
       201
      -----
      10100
Got:
    201/10100
**********************************************************************
File "axiom.py", line 115:
    sage: a = axiom('(1 + sqrt(2))^5'); a         # optional
Expected:
         +-+
      29\|2  + 41
Got:
      Cannot convert from type AlgebraicNumber to InputForm for value     +-+  29\|2  + 41
    <BLANKLINE>
**********************************************************************
File "axiom.py", line 458:
    sage: v = axiom('[i*x^i for i in 0..5]'); v          # optional
Expected:
           2   3   4   5
    [0,x,2x ,3x ,4x ,5x ]
Got:
    [0,x,2*x*x,3*x**3,4*x**4,5*x**5]
**********************************************************************
File "axiom.py", line 461:
    sage: v[4]                                           # optional
Expected:
      3
    3x
Got:
    3*x**3
**********************************************************************
2 items had failures:
   8 of  18 in __main__.example_0
   2 of   4 in __main__.example_10
***Test Failed*** 10 failures.
For whitespace errors, see the file .doctest_axiom.py
	 [2.9 s]
exit code: 256
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -optional el/sage-bday2/sage/interfaces/axiom.py
Total time for all tests: 2.9 seconds
```



---

Comment by mhansen created at 2007-10-21 02:16:17

Patch attached.


---

Attachment


---

Comment by was created at 2007-10-21 02:20:39

Resolution: fixed

# Issue 953: the axiom / sage interface is currently totally broken, at least on 64-bit linux

archive/issues_000953.json:
```json
{
    "body": "Assignee: @williamstein\n\nWith  axiom4sage-0.3.1 installed:\n\nThis is terrible.  \n\n\n```\nwas@ubuntu:~/d/sage/sage/interfaces$ sage -t --optional axiom.py\nsage -t --optional axiom.py                                 **********************************************************************\nFile \"axiom.py\", line 38:\n    sage: axiom('3 * 5')                     # optional\nExpected:\n    15\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"axiom.py\", line 40:\n    sage: a = axiom(3) * axiom(5); a         # optional\nExpected:\n    15\nGot:\n    <BLANKLINE>\n      5                                                                                                                                                                                                                          Type: PositiveInteger\n**********************************************************************\nFile \"axiom.py\", line 56:\n    sage: F = axiom.factor('x^5 - y^5'); F      # optional\nExpected:\n               4      3    2 2    3     4\n    - (y - x)(y  + x y  + x y  + x y + x )\nGot:\n    15\n**********************************************************************\nFile \"axiom.py\", line 61:\n    sage: F.type()                              # optional\nExpected:\n    Factored Polynomial Integer\nGot:\n    PositiveInteger\n**********************************************************************\nFile \"axiom.py\", line 69:\n    sage: a = axiom('2/3'); a          # optional\nExpected:\n    2\n    -\n    3\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"axiom.py\", line 73:\n    sage: str(a)                       # optional\nExpected:\n    '2/3'\nGot:\n    '             4      3    2 2    3     4\\r\\n  - (y - x)(y  + x y  + x y  + x y + x )'\n**********************************************************************\nFile \"axiom.py\", line 76:\n    sage: str(a)                       # optional\nExpected:\n    'x*x+3/7'\nGot:\n    ''\n**********************************************************************\nFile \"axiom.py\", line 84:\n    sage: print axiom.eval('factor(x^5 - y^5)')   # optional\nExpected:\n               4      3    2 2    3     4\n    - (y - x)(y  + x y  + x y  + x y + x )\n    <BLANKLINE>\n    Type: Factored Polynomial Integer\nGot:\n    unparse(sage2::InputForm)\n\n       >> Fortran translation error:\n       No corresponding Fortran structure for:\n\n       (y - x) :: Polynomial Integer\n\n       >> Fortran translation error:\n       No corresponding Fortran structure for:\n\n         4      3    2 2    3     4\n       (y  + x y  + x y  + x y + x ) :: Polynomial Integer\n\n       (10)  \"-primeFactor(,1)*primeFactor(,1)\"\n                                                                                                                                                                                                                                             Type: String\n    <BLANKLINE>\n**********************************************************************\nFile \"axiom.py\", line 94:\n    sage: f^2                                     # optional\nExpected:\n     10     5 5    10\n    y   - 2x y  + x\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"axiom.py\", line 97:\n    sage: f.factor()                              # optional\nExpected:\n               4      3    2 2    3     4\n    - (y - x)(y  + x y  + x y  + x y + x )\nGot:\n    <BLANKLINE>\n      2  -  3                                                                                                                                                                                                                        Type: Fraction Integer\n**********************************************************************\nFile \"axiom.py\", line 110:\n    sage: axiom('1/100 + 1/101')                  # optional\nExpected:\n       201\n      -----\n      10100\nGot:\n    <BLANKLINE>\n       2   3  x  + -       7                                                                                                                                                                                                             Type: Polynomial Fraction Integer\n**********************************************************************\nFile \"axiom.py\", line 115:\n    sage: a = axiom('(1 + sqrt(2))^5'); a         # optional\nExpected:\n         +-+\n      29\\|2  + 41\nGot:\n                 4      3    2 2    3     4  - (y - x)(y  + x y  + x y  + x y + x )                                                                                                                                                                                                             Type: Factored Polynomial Integer\n**********************************************************************\nFile \"axiom.py\", line 458:\n    sage: v = axiom('[i*x^i for i in 0..5]'); v          # optional\nExpected:\n           2   3   4   5\n    [0,x,2x ,3x ,4x ,5x ]\nGot:\n    <BLANKLINE>\n      2                                                                                                                                                                                                                         Type: PositiveInteger\n**********************************************************************\nFile \"axiom.py\", line 461:\n    sage: v[4]                                           # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/s/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[1]>\", line 1, in <module>\n        v[Integer(4)]                                           # optional###line 461:\n    sage: v[4]                                           # optional\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py\", line 472, in __getitem__\n        if n <= 0 or n > len(self):\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py\", line 444, in __len__\n        return int(s[:i-1])\n    ValueError: invalid literal for int() with base 10: '10     5 5    10\\r\\n  y   - 2x y  + x\\r\\n                                                                                                                                                                   '\n**********************************************************************\nFile \"axiom.py\", line 464:\n    sage: v[1]                                           # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/s/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[2]>\", line 1, in <module>\n        v[Integer(1)]                                           # optional###line 464:\n    sage: v[1]                                           # optional\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py\", line 472, in __getitem__\n        if n <= 0 or n > len(self):\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py\", line 444, in __len__\n        return int(s[:i-1])\n    ValueError: invalid literal for int() with base 10: ''\n**********************************************************************\nFile \"axiom.py\", line 466:\n    sage: v[10]                                          # optional\nExpected:\n    Traceback (most recent call last):\n    ...\n    IndexError: index out of range\nGot:\n    Traceback (most recent call last):\n      File \"/home/was/s/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[3]>\", line 1, in <module>\n        v[Integer(10)]                                          # optional###line 466:\n    sage: v[10]                                          # optional\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py\", line 472, in __getitem__\n        if n <= 0 or n > len(self):\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py\", line 444, in __len__\n        return int(s[:i-1])\n    ValueError: invalid literal for int() with base 10: ''\n**********************************************************************\nFile \"axiom.py\", line 359:\n    sage: a == b                                      # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/s/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_7[1]>\", line 1, in <module>\n        a == b                                      # optional###line 359:\n    sage: a == b                                      # optional\n      File \"element.pyx\", line 623, in element.Element.__richcmp__\n      File \"element.pyx\", line 595, in element.Element._richcmp\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py\", line 381, in __cmp__\n        elif P('%s > %s'%(self.name(), other.name())).__repr__().strip() == t:\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py\", line 417, in __repr__\n        return self.str()\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py\", line 404, in str\n        raise RuntimeError, s\n    RuntimeError: unparse(sage5::InputForm)\n\n       >> Fortran translation error:\n       No corresponding Fortran structure for:\n\n       (y - x) :: Polynomial Integer\n\n       >> Fortran translation error:\n       No corresponding Fortran structure for:\n\n         4      3    2 2    3     4\n       (y  + x y  + x y  + x y + x ) :: Polynomial Integer\n\n       (23)  \"-primeFactor(,1)*primeFactor(,1)\"\n                                                                                                                                                                                                                                             Type: String\n\n**********************************************************************\nFile \"axiom.py\", line 365:\n    sage: b < a                                       # optional\nExpected:\n    False\nGot:\n    True\n**********************************************************************\nFile \"axiom.py\", line 367:\n    sage: b > a                                       # optional\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"axiom.py\", line 438:\n    sage: len(v)                                      # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/s/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_9[1]>\", line 1, in <module>\n        len(v)                                      # optional###line 438:\n    sage: len(v)                                      # optional\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/axiom.py\", line 444, in __len__\n        return int(s[:i-1])\n    ValueError: invalid literal for int() with base 10: ''\n**********************************************************************\n4 items had failures:\n  12 of  18 in __main__.example_0\n   4 of   4 in __main__.example_10\n   3 of   8 in __main__.example_7\n   1 of   2 in __main__.example_9\n***Test Failed*** 20 failures.\nFor whitespace errors, see the file .doctest_axiom.py\n         [3.8 s]\nexit code: 256\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t --optional axiom.py\nTotal time for all tests: 3.8 seconds\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/953\n\n",
    "created_at": "2007-10-20T23:49:20Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "the axiom / sage interface is currently totally broken, at least on 64-bit linux",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/953",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

With  axiom4sage-0.3.1 installed:

This is terrible.  


```
was@ubuntu:~/d/sage/sage/interfaces$ sage -t --optional axiom.py
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


Issue created by migration from https://trac.sagemath.org/ticket/953





---

archive/issue_comments_005785.json:
```json
{
    "body": "Changing component from algebraic geometry to interfaces.",
    "created_at": "2007-10-20T23:49:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/953#issuecomment-5785",
    "user": "https://github.com/williamstein"
}
```

Changing component from algebraic geometry to interfaces.



---

archive/issue_comments_005786.json:
```json
{
    "body": "My results on my laptop and on sage.math are much better.  Here are the doctest failures I get:\n\n```\nsage -t -optional el/sage-bday2/sage/interfaces/axiom.py    **********************************************************************\nFile \"axiom.py\", line 56:\n    sage: F = axiom.factor('x^5 - y^5'); F      # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/cwitty/sage/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[5]>\", line 1, in <module>\n        F = axiom.factor('x^5 - y^5'); F      # optional###line 56:\n    sage: F = axiom.factor('x^5 - y^5'); F      # optional\n      File \"/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/axiom.py\", line 417, in __repr__\n        return self.str()\n      File \"/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/axiom.py\", line 404, in str\n        raise RuntimeError, s\n    RuntimeError: unparse(sage2::InputForm)\n\n    unparse(sage2::InputForm)\n\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\n\n     \n\n       >> Fortran translation error:\n\n       No corresponding Fortran structure for:\n\n    \n\n       (y - x) :: Polynomial Integer\n\n     \n\n       >> Fortran translation error:\n\n       No corresponding Fortran structure for:\n\n    \n\n         4      3    2 2    3     4\n\n       (y  + x y  + x y  + x y + x ) :: Polynomial Integer\n\n    \n\n       (10)  \"-primeFactor(,1)*primeFactor(,1)\"\n\n                                                                                                                                                                                                                                             Type: String\n\n\n**********************************************************************\nFile \"axiom.py\", line 69:\n    sage: a = axiom('2/3'); a          # optional\nExpected:\n    2\n    -\n    3\nGot:\n    2/3\n**********************************************************************\nFile \"axiom.py\", line 73:\n    sage: str(a)                       # optional\nExpected:\n    '2/3'\nGot:\n    '  2\\r\\n  -\\r\\n  3'\n**********************************************************************\nFile \"axiom.py\", line 76:\n    sage: str(a)                       # optional\nExpected:\n    'x*x+3/7'\nGot:\n    '   2   3\\r\\n  x  + -\\r\\n       7'\n**********************************************************************\nFile \"axiom.py\", line 94:\n    sage: f^2                                     # optional\nExpected:\n     10     5 5    10\n    y   - 2x y  + x\nGot:\n    y**10+(-2*x**5*y**5)+x**10\n**********************************************************************\nFile \"axiom.py\", line 97:\n    sage: f.factor()                              # optional\nException raised:\n    Traceback (most recent call last):\n      File \"/home/cwitty/sage/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[15]>\", line 1, in <module>\n        f.factor()                              # optional###line 97:\n    sage: f.factor()                              # optional\n      File \"/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/axiom.py\", line 417, in __repr__\n        return self.str()\n      File \"/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/axiom.py\", line 404, in str\n        raise RuntimeError, s\n    RuntimeError: unparse(sage5::InputForm)\n\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\ufffd[C\n\n     \n\n       >> Fortran translation error:\n\n       No corresponding Fortran structure for:\n\n    \n\n       (y - x) :: Polynomial Integer\n\n     \n\n       >> Fortran translation error:\n\n       No corresponding Fortran structure for:\n\n    \n\n         4      3    2 2    3     4\n\n       (y  + x y  + x y  + x y + x ) :: Polynomial Integer\n\n    \n\n       (23)  \"-primeFactor(,1)*primeFactor(,1)\"\n\n                                                                                                                                                                                                                                             Type: String\n\n\n**********************************************************************\nFile \"axiom.py\", line 110:\n    sage: axiom('1/100 + 1/101')                  # optional\nExpected:\n       201\n      -----\n      10100\nGot:\n    201/10100\n**********************************************************************\nFile \"axiom.py\", line 115:\n    sage: a = axiom('(1 + sqrt(2))^5'); a         # optional\nExpected:\n         +-+\n      29\\|2  + 41\nGot:\n      Cannot convert from type AlgebraicNumber to InputForm for value     +-+  29\\|2  + 41\n    <BLANKLINE>\n**********************************************************************\nFile \"axiom.py\", line 458:\n    sage: v = axiom('[i*x^i for i in 0..5]'); v          # optional\nExpected:\n           2   3   4   5\n    [0,x,2x ,3x ,4x ,5x ]\nGot:\n    [0,x,2*x*x,3*x**3,4*x**4,5*x**5]\n**********************************************************************\nFile \"axiom.py\", line 461:\n    sage: v[4]                                           # optional\nExpected:\n      3\n    3x\nGot:\n    3*x**3\n**********************************************************************\n2 items had failures:\n   8 of  18 in __main__.example_0\n   2 of   4 in __main__.example_10\n***Test Failed*** 10 failures.\nFor whitespace errors, see the file .doctest_axiom.py\n\t [2.9 s]\nexit code: 256\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -optional el/sage-bday2/sage/interfaces/axiom.py\nTotal time for all tests: 2.9 seconds\n```\n",
    "created_at": "2007-10-21T00:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/953#issuecomment-5786",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

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

archive/issue_comments_005787.json:
```json
{
    "body": "Patch attached.",
    "created_at": "2007-10-21T02:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/953#issuecomment-5787",
    "user": "https://github.com/mwhansen"
}
```

Patch attached.



---

archive/issue_comments_005788.json:
```json
{
    "body": "Attachment [axiom.patch](tarball://root/attachments/some-uuid/ticket953/axiom.patch) by @mwhansen created at 2007-10-21 02:16:51",
    "created_at": "2007-10-21T02:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/953#issuecomment-5788",
    "user": "https://github.com/mwhansen"
}
```

Attachment [axiom.patch](tarball://root/attachments/some-uuid/ticket953/axiom.patch) by @mwhansen created at 2007-10-21 02:16:51



---

archive/issue_comments_005789.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-21T02:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/953#issuecomment-5789",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_001073.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-10-21T02:20:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/953",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/953#event-1073"
}
```

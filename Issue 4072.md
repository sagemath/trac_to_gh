# Issue 4072: Fix issue in trait_names in the sage0 interface

Issue created by migration from https://trac.sagemath.org/ticket/4072

Original creator: mhansen

Original creation time: 2008-09-07 18:23:43

Assignee: was


```
File "/Users/mhansen/sage-3.1.2.rc0/tmp/sage0.py", line 164:
    sage: t = sage0.trait_names()
Exception raised:
    Traceback (most recent call last):
      File "/Users/mhansen/sage-3.1.2.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[2]>", line 1, in <module>
        t = sage0.trait_names()###line 164:
    sage: t = sage0.trait_names()
      File "/Users/mhansen/sage-3.1.2.rc0/local/lib/python2.5/site-packages/sage/interfaces/sage0.py", line 171, in trait_names
        return eval(self.eval('globals().keys()'))
      File "<string>", line 408
         'cosh',
^              
     SyntaxError: invalid syntax
**********************************************************************
File "/Users/mhansen/sage-3.1.2.rc0/tmp/sage0.py", line 165:
    sage: len(t) > 100
Exception raised:
    Traceback (most recent call last):
      File "/Users/mhansen/sage-3.1.2.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        len(t) > Integer(100)###line 165:
    sage: len(t) > 100
    NameError: name 't' is not defined
**********************************************************************
File "/Users/mhansen/sage-3.1.2.rc0/tmp/sage0.py", line 167:
    sage: 'gcd' in t
Exception raised:
    Traceback (most recent call last):
      File "/Users/mhansen/sage-3.1.2.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[4]>", line 1, in <module>
        'gcd' in t###line 167:
    sage: 'gcd' in t
    NameError: name 't' is not defined
**********************************************************************
1 items had failures:
   3 of   5 in __main__.example_4
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/mhansen/sage-3.1.2.rc0/tmp/.doctest_sage0.py
         [81.0 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:

```



---

Attachment


---

Comment by mhansen created at 2008-09-07 18:30:34

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2008-09-07 18:30:34

Changing status from new to assigned.


---

Comment by malb created at 2008-09-07 19:01:12

I seem to have another (unrelated?) problem which isn't fixed in rc0 + this patch:


```
sage -t  devel/sage/sage/interfaces/sage0.py                **********************************************************************
File "/usr/local/sage-3.1.2.rc0/tmp/sage0.py", line 276:
    sage: sage0.eval('2+2')
Expected:
    '4'
Got:
    '\x1b[0;31m\x1b[0m4'
**********************************************************************
File "/usr/local/sage-3.1.2.rc0/tmp/sage0.py", line 317:
    sage: sage0.get('x')
Expected:
    "...NameError: name 'x' is not defined"
Got:
    "\x1b[0;31m---------------------------------------------------------------------------\x1b[0m\n\x1b[0;31mNameError\x1b[0m                                 Traceback (most recent call last)\n\n\x1b[0;32m/usr/local/sage-3.1.2.rc0/data/extcode/sage/<ipython console>\x1b[0m in \x1b[0;36m<module>\x1b[0;34m()\x1b[0m\n\n\x1b[0;31mNameError\x1b[0m: name 'x' is not defined"
**********************************************************************
File "/usr/local/sage-3.1.2.rc0/tmp/sage0.py", line 326:
    sage: sage0._contains('2', 'QQ')
Expected:
    True
Got:
    False
**********************************************************************
File "/usr/local/sage-3.1.2.rc0/tmp/sage0.py", line 432:
    sage: sage0(4).gcd
Expected:
    <built-in method gcd of sage.rings.integer.Integer object at 0x...>
Got:
    <built-in method gcd of sage.rings.integer.Integer object at 0x33f2d80>
**********************************************************************
File "/usr/local/sage-3.1.2.rc0/tmp/sage0.py", line 177:
    sage: s.eval('2+2')
Expected:
    '4'
Got:
    '\x1b[0;31m\x1b[0m4'
**********************************************************************
5 items had failures:
   1 of   3 in __main__.example_10
   1 of   6 in __main__.example_13
   1 of   3 in __main__.example_14
   1 of   3 in __main__.example_22
   1 of   5 in __main__.example_5
***Test Failed*** 5 failures.
For whitespace errors, see the file /usr/local/sage-3.1.2.rc0/tmp/.doctest_sage0.py
         [8.4 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage/sage/interfaces/sage0.py
```



---

Comment by malb created at 2008-09-07 19:06:46


```
[20:02] <mabshoff> malb: The failure you are seeing with http://trac.sagemath.org/sage_trac/ticket/4072 is related to ipython and its color handling on the shell.
```


So I disabled colors in iPython and all is good.


---

Comment by mabshoff created at 2008-09-07 23:06:08

Resolution: fixed


---

Comment by mabshoff created at 2008-09-07 23:06:08

Merged in Sage 3.1.2.rc1

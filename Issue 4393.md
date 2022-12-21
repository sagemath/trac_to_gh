# Issue 4393: Sage 3.1.4: magma related optional doctest failure in sage/structure/element.pyx

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-10-30 16:35:36

Assignee: mabshoff


```
mabshoff`@`iras:~/build-3.2.a1/sage-3.2.alpha1-iras> ./sage -t -long -optional devel/sage/sage/structure/element.pyx
sage -t -long -optional devel/sage/sage/structure/element.pyx
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py", line 1566:
    sage: mv = magma(v); mv                     # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_58[3]>", line 1, in <module>
        mv = magma(v); mv                     # optional###line 1566:
    sage: mv = magma(v); mv                     # optional
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 993, in _coerce_from_special_method
        return self(x._interface_init_())
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 965, in __call__
        return cls(self, x, name=name)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1293, in __init__
        raise TypeError, x
    TypeError: Error evaluating Magma code.
    IN:
[1] := (1, 2, 3);
    OUT:
    >> _sage_[1] := (1, 2, 3);
                    ^
    Runtime error in elt< ... >: No permutation group context in which to create cycle

**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py", line 1568:
    sage: mv.Type()                             # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_58[4]>", line 1, in <module>
        mv.Type()                             # optional###line 1568:
    sage: mv.Type()                             # optional
    NameError: name 'mv' is not defined
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py", line 1570:
    sage: mv.Parent()                           # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_58[5]>", line 1, in <module>
        mv.Parent()                           # optional###line 1570:
    sage: mv.Parent()                           # optional
    NameError: name 'mv' is not defined
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py", line 1574:
    sage: mv = magma(v); mv                     # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_58[7]>", line 1, in <module>
        mv = magma(v); mv                     # optional###line 1574:
    sage: mv = magma(v); mv                     # optional
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 993, in _coerce_from_special_method
        return self(x._interface_init_())
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 965, in __call__
        return cls(self, x, name=name)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1293, in __init__
        raise TypeError, x
    TypeError: Error evaluating Magma code.
    IN:
[2] := (1/2, 3/4, 5/6);
    OUT:
    >> _sage_[2] := (1/2, 3/4, 5/6);
                    ^
    Runtime error in elt< ... >: Bad arguments

**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py", line 1576:
    sage: mv.Type()                             # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_58[8]>", line 1, in <module>
        mv.Type()                             # optional###line 1576:
    sage: mv.Type()                             # optional
    NameError: name 'mv' is not defined
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/element.py", line 1578:
    sage: mv.Parent()                           # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_58[9]>", line 1, in <module>
        mv.Parent()                           # optional###line 1578:
    sage: mv.Parent()                           # optional
    NameError: name 'mv' is not defined
**********************************************************************
1 items had failures:
   6 of  10 in __main__.example_58
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/.doctest_element.py
	 [14.7 s]
exit code: 1024
```



---

Comment by mabshoff created at 2008-10-30 16:52:15

Changing assignee from mabshoff to was.


---

Attachment


---

Comment by mabshoff created at 2008-10-31 20:24:02

Positive review. The doctests now pass:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.3.final$ 
./sage -t -long -optional devel/sage/sage/structure/element.pyx
sage -t -long -optional devel/sage/sage/structure/element.pyx
	 [7.0 s]
 
----------------------------------------------------------------------
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-10-31 20:24:41

Resolution: fixed


---

Comment by mabshoff created at 2008-10-31 20:24:41

Merged in Sage 3.2.alpha2

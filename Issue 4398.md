# Issue 4398: Sage 3.1.4: magma related optional doctest failure in sage/sage/modules/free_module.py

Issue created by migration from https://trac.sagemath.org/ticket/4398

Original creator: mabshoff

Original creation time: 2008-10-30 17:08:26

Assignee: was


```
mabshoff@iras:~/build-3.2.a1/sage-3.2.alpha1-iras> ./sage -t -long -optional devel/sage/sage/modules/free_module.py
sage -t -long -optional devel/sage/sage/modules/free_module.py
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/free_module.py", line 1554:
    sage: magma(FreeModule(Integers(8), 2))             # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_52[2]>", line 1, in <module>
        magma(FreeModule(Integers(Integer(8)), Integer(2)))             # optional###line 1554:
    sage: magma(FreeModule(Integers(8), 2))             # optional
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
[1] := Ambient free module of rank 2 over Ring of integers modulo 8;
    OUT:
    >> _sage_[1] := Ambient free module of rank 2 over Ring of integers modulo 8;
                            ^
    User error: bad syntax
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/free_module.py", line 1557:
    sage: magma(FreeModule(QQ, 9))                      # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_52[3]>", line 1, in <module>
        magma(FreeModule(QQ, Integer(9)))                      # optional###line 1557:
    sage: magma(FreeModule(QQ, 9))                      # optional
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
[2] := Vector space of dimension 9 over Rational Field;
    OUT:
    >> _sage_[2] := Vector space of dimension 9 over Rational Field;
                           ^
    User error: bad syntax
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/free_module.py", line 1560:
    sage: magma(FreeModule(QQ['x'], 2))                 # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_52[4]>", line 1, in <module>
        magma(FreeModule(QQ['x'], Integer(2)))                 # optional###line 1560:
    sage: magma(FreeModule(QQ['x'], 2))                 # optional
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
[3] := Ambient free module of rank 2 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field;
    OUT:
    In file "/home/mabshoff/.sage//temp/iras/20303//interface//tmp20303", line 1, column 22:
    >> _sage_[3] := Ambient free module of rank 2 over the principal ideal domain 
                            ^
    User error: bad syntax
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/free_module.py", line 1565:
    sage: magma(M)                                      # optional
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_52[7]>", line 1, in <module>
        magma(M)                                      # optional###line 1565:
    sage: magma(M)                                      # optional
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 991, in _coerce_from_special_method
        return (x.__getattribute__(s))(self)
      File "sage_object.pyx", line 370, in sage.structure.sage_object.SageObject._magma_ (sage/structure/sage_object.c:3379)
      File "sage_object.pyx", line 415, in sage.structure.sage_object.SageObject._magma_convert_ (sage/structure/sage_object.c:3509)
      File "sage_object.pyx", line 246, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2186)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 965, in __call__
        return cls(self, x, name=name)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1293, in __init__
        raise TypeError, x
    TypeError: Error evaluating Magma code.
    IN:
[4] := RSpace(IntegerRing(), 2, [ 1  0]
    [ 0 -1]);
    OUT:
    >> _sage_[4] := RSpace(IntegerRing(), 2, [ 1  0]
                                                  ^
    User error: bad syntax

    >> [ 0 -1]);
              ^
    User error: bad syntax
**********************************************************************
```



---

Attachment


---

Comment by mabshoff created at 2008-10-31 20:15:41

Positive review since the patch fixes the Magma optional doctests.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-31 20:20:38

Merged in Sage 3.2.alpha2


---

Comment by mabshoff created at 2008-10-31 20:20:38

Resolution: fixed

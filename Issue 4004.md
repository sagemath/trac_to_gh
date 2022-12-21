# Issue 4004: [with patch, needs review] increase coverage of sage/interfaces/gap.py and sage/interfaces/gp.py

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-08-30 18:00:40

Assignee: was




---

Attachment


---

Comment by mabshoff created at 2008-08-30 19:10:13

This patch creates some problems:

```
        sage -t -long devel/sage/sage/interfaces/lisp.py # 1 doctests failed
        sage -t -long devel/sage/sage/interfaces/gp.py # 1 doctests failed
        sage -t -long devel/sage/sage/groups/matrix_gps/matrix_group.py # 2 doctests failed
```

Specifically: matrix_group.py:

```
sage -t -long devel/sage/sage/groups/matrix_gps/matrix_group.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/tmp/matrix_group.py", line 313:
    sage: G.order()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[11]>", line 1, in <module>
        G.order()###line 313:
    sage: G.order()
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py", line 316, in order
        g = self._gap_()
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py", line 177, in _gap_
        raise NotImplementedError, "Matrix group over %s not implemented."%self.__R
    NotImplementedError: Matrix group over Integer Ring not implemented.
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/tmp/matrix_group.py", line 475:
    sage: G.order()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_17[11]>", line 1, in <module>
        G.order()###line 475:
    sage: G.order()
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py", line 316, in order
        g = self._gap_()
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/groups/matrix_gps/matrix_group.py", line 177, in _gap_
        raise NotImplementedError, "Matrix group over %s not implemented."%self.__R
    NotImplementedError: Matrix group over Integer Ring not implemented.
**********************************************************************
```

interfaces/gp.py:

```
sage -t -long devel/sage/sage/interfaces/gp.py              **********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/tmp/gp.py", line 583:
    sage: bool(gp(2))
Expected:
    True
Got:
    False
**********************************************************************
```

interfaces/lisp.py:

```
sage -t -long devel/sage/sage/interfaces/lisp.py            
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/tmp/lisp.py", line 460:
    sage: a^3
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_28[3]>", line 1, in <module>
        a**Integer(3)###line 460:
    sage: a^3
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/lisp.py", line 463, in __pow__
        return RingElement.__pow__(self, n)
      File "element.pyx", line 1469, in sage.structure.element.RingElement.__pow__ (sage/structure/element.c:9721)
      File "element.pyx", line 2866, in sage.structure.element.generic_power_c (sage/structure/element.c:18642)
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1458, in __nonzero__
        return self.bool()
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1447, in bool
        cmd = '%s %s %s'%(self._name, P._equality_symbol(), t)
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/lisp.py", line 351, in _equality_symbol
        "Please report this as a bug.")
    NotImplementedError: We should never reach here in the Lisp interface. Please report this as a bug.
**********************************************************************
```


Cheers,

Michael


---

Attachment

I renamed the clear method to unbind (which is what it is in GAP) because the garbage collector was calling the deallocation routine which called clear and caused problems in the matrix_group.py doctest.


---

Comment by mabshoff created at 2008-08-31 06:02:34

Resolution: fixed


---

Comment by mabshoff created at 2008-08-31 06:02:34

With the second patch doctests do pass again. Positive review.

Cheers,

Michael

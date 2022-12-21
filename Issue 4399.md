# Issue 4399: Sage 3.1.4: magma related optional doctest failure in sage/matrix/matrix1.pyx

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-10-30 17:19:20

Assignee: was


```
sage -t -long -optional devel/sage/sage/matrix/matrix1.pyx  
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/matrix1.py", line 222:
    sage: magma(M)                             # optional -- requires magma
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[19]>", line 1, in <module>
        magma(M)                             # optional -- requires magma###line 222:
    sage: magma(M)                             # optional -- requires magma
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 991, in _coerce_from_special_method
        return (x.__getattribute__(s))(self)
      File "matrix1.pyx", line 237, in sage.matrix.matrix1.Matrix._magma_ (sage/matrix/matrix1.c:2559)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 965, in __call__
        return cls(self, x, name=name)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1293, in __init__
        raise TypeError, x
    TypeError: Error evaluating Magma code.
    IN:
[13] := MatrixAlgebra(_sage_[14], 3)![0,1,3,zeta9,zeta9^4,zeta9 - 1,-zeta9^5 - zeta9^2,1,0];
    OUT:
    >> _sage_[13] := MatrixAlgebra(_sage_[14], 3)![0,1,3,zeta9,zeta9^4,zeta9 - 1,-
                                                         ^
    User error: Identifier 'zeta9' has not been declared or assigned
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/tmp/matrix1.py", line 226:
    sage: magma(M**2) == magma(M)**2           # optional -- requires magma
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[20]>", line 1, in <module>
        magma(M**Integer(2)) == magma(M)**Integer(2)           # optional -- requires magma###line 226:
    sage: magma(M**2) == magma(M)**2           # optional -- requires magma
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 967, in __call__
        return self._coerce_from_special_method(x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 991, in _coerce_from_special_method
        return (x.__getattribute__(s))(self)
      File "matrix1.pyx", line 237, in sage.matrix.matrix1.Matrix._magma_ (sage/matrix/matrix1.c:2559)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 509, in __call__
        return Expect.__call__(self, x)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 965, in __call__
        return cls(self, x, name=name)
      File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-iras/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1293, in __init__
        raise TypeError, x
    TypeError: Error evaluating Magma code.
    IN:
[9] := MatrixAlgebra(_sage_[14], 3)![-3*zeta9^5 - 3*zeta9^2 + zeta9,zeta9^4 + 3,zeta9 - 1,2*zeta9^5 + zeta9^2 + 1,-zeta9^5 - zeta9^2 + 2*zeta9 - 1,zeta9^5 - zeta9^4 + 3*zeta9,zeta9,-zeta9^5 + zeta9^4 - zeta9^2,-3*zeta9^5 - 3*zeta9^2 + zeta9 - 1];
    OUT:
    In file "/home/mabshoff/.sage//temp/iras/20404//interface//tmp20404", line 1, column 47:
    >> _sage_[9] := MatrixAlgebra(_sage_[14], 3)![-3*zeta9^5 - 3*zeta9^2 + zeta9,z
                                                     ^
    User error: Identifier 'zeta9' has not been declared or assigned
**********************************************************************
```



---

Comment by mabshoff created at 2008-10-30 23:49:39

The two extcode patches were not merged from #2169, but I have now merged them. So these two patches should be ignored.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-31 20:27:49

I deleted the two extcode patches to less the potential confusion when a new patch is posted here.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-24 22:52:52

Resolution: fixed


---

Comment by mabshoff created at 2008-11-24 22:52:52

Fixed in Sage 3.2.1.alpha1 via #4601.

Cheers,

Michael

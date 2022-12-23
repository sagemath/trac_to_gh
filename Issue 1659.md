# Issue 1659: Add a complex128 method for conversion of symbolic (and other?) expressions to numpy's 128-bit complex type

Issue created by migration from https://trac.sagemath.org/ticket/1659

Original creator: was

Original creation time: 2008-01-02 19:33:21

Assignee: robertwb


```
rishi_: I use scipy very often. To use complex number I have to use the following statement:  sage: a=numpy.complex128(complex(2+3*I)). Is it not possible to avoid 2 conversions?
[12:29pm] mabshoff: hungry? *ducks*
[12:29pm] ondrej: mabshoff - like a small dog?
[12:29pm] mabshoff: yes. a young dog.
[12:29pm] wstein-1658: We could add a method (2+3*I).complex128().
[12:29pm] wstein-1658: Want that?
[12:29pm] wstein-1658: Is I symbolic, by the way?
[12:29pm] rishi_: yes
[12:30pm] wstein-1658: Do you want to avoid two conversions because of speed or code cleaness?
[12:30pm] wstein-1658: Probably clean-ness.
[12:30pm] rishi_: cleaness
```



---

Comment by was created at 2008-01-02 19:36:59

A temporary workaround (and almost the fix):


```
sage: import sage.calculus.calculus
sage: def complex128(self): import numpy; return numpy.complex128(complex(self))
....: 
sage: sage.calculus.calculus.SymbolicExpression.complex128 = complex128
sage: 
sage: (3 + 2*I).complex128()
(3+2j)
```



---

Comment by mhansen created at 2010-08-26 20:16:48

Resolution: worksforme


---

Comment by mhansen created at 2010-08-26 20:16:48

This now works:


```

----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: combinat
sage: import numpy
sage: a = numpy.complex128(2+3*I); a
(2+3j)
sage: type(a)
<type 'numpy.complex128'>
```


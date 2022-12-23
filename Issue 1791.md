# Issue 1791: Sage 2.10.alpha3: numerical noise doctest failure with gcc 4.2.2/x86

Issue created by migration from https://trac.sagemath.org/ticket/1791

Original creator: mabshoff

Original creation time: 2008-01-16 01:42:28

Assignee: failure

As reported by Kate in https://groups.google.com/group/sage-devel/t/1cd682b8f3e49748

```
sage -t  devel/sage-main/sage/rings/polynomial/
polynomial_element.pyx
**********************************************************************
File "polynomial_element.pyx", line 2549:
    sage: f.roots(multiplicities=False)
Expected:
    [...1.00000000000000...*I, 1.00000000000000...*I]
Got:
    [1.00000000000000 + 1.11022302462516e-16*I, 1.12045416424138e-16 +
1.00000000000000*I] 
```



---

Comment by mabshoff created at 2008-01-16 03:40:21

Merged in Sage 2.10.alpha4


---

Comment by mabshoff created at 2008-01-16 03:40:21

Resolution: fixed

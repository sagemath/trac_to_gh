# Issue 3146: (latex(a\v), a) gives an error about calling something with too many arguments.

Issue created by migration from https://trac.sagemath.org/ticket/3146

Original creator: jason

Original creation time: 2008-05-09 20:13:03

Assignee: was


```
a=matrix(QQ,3,3,range(9))
v=matrix(QQ,3,1,range(3))
(latex(a\v), a)
```


gives an error.

I think it has to do with the parsing of latex(a\v); it seems to try doing "(latex(a._backslash_(v), a)" (note the missing parenthesis in the call to latex.

You see this parsing in the error from:


```
@interact
def _(a=matrix(QQ,3,3,range(9)), v=matrix(QQ,3,1,range(3))):
    html('$$%s %s = %s$$'%(latex(a), latex(a\v), latex(v)))
```


with the patch from #3121




---

Comment by mhansen created at 2009-06-04 22:57:37

This now works (most likely with the change to how the backslash operator is implemented)


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: a=matrix(QQ,3,3,range(9))
sage: v=matrix(QQ,3,1,range(3))
sage: (latex(a\v), a)
| Sage Version 4.0.1.rc1, Release Date: 2009-06-04                   |
| Type notebook() for the GUI, and license() for information.        |
(\left(\begin{array}{r}
\frac{1}{3} \\
0 \\
0
\end{array}\right),
 [0 1 2]
[3 4 5]
[6 7 8])
```



---

Comment by mhansen created at 2009-06-04 22:57:37

Resolution: invalid

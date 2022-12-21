# Issue 671: Solaris 10: interfaces/singular.py doctests failure

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-17 00:32:29

Assignee: malb or was

Keywords: Solaris 10, doctest, singular


```
sage -t  interfaces/singular.py                             **********************************************************************
File "singular.py", line 337:
    sage: singular.eval('2 > 1')
Expected:
    '1'
Got:
    '2'
**********************************************************************
File "singular.py", line 339:
    sage: singular.eval('2 + 2')
Expected:
    '4'
Got:
    '1'
**********************************************************************
```


Running the same commands directly via Singular:

```
-bash-3.00$ Singular-3-0-3
                     SINGULAR                             /  Development
 A Computer Algebra System for Polynomial Computations   /   version 3-0-3
                                                       0<
     by: G.-M. Greuel, G. Pfister, H. Schoenemann        \   May 2007
FB Mathematik der Universitaet, D-67653 Kaiserslautern    \
> 2+2
. ;
4
> 1<2;
1
> 2<1;
0
```



---

Comment by mabshoff created at 2007-09-17 01:24:00

Changing component from packages to doctest.


---

Comment by mabshoff created at 2007-09-17 09:53:25

Another interesting data point:

```
./sage -t -verbose devel/sage/sage/rings/polynomial/toy_buchberger.py
<SNIP>
Trying:
    Ideal(g1).basis_is_groebner()###line 44:_sage_    >>> Ideal(g1).basis_is_groebner()
Expecting:
    True
```

Result: hang

And:

```
./sage -t -verbose devel/sage/sage/rings/polynomial/multi_polynomial_element.py
Trying:
    k.factor()###line 1035:_sage_    >>> k.factor()
Expecting:
    (s^2 + 2/3) * (x + s*y)^2 * (x + (-s)*y)^5 * (x^2 + s*x*y + s^2*y^2)^5
```

Result: hang  

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-26 06:34:55

Resolution: fixed


---

Comment by mabshoff created at 2008-06-26 06:34:55

This has been fixed by #3405.

Cheers,

Michael

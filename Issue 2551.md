# Issue 2551: `__getitem__` for relative number field elements is ... surprising

Issue created by migration from https://trac.sagemath.org/ticket/2551

Original creator: craigcitro

Original creation time: 2008-03-16 21:10:56

Assignee: was

Indexing into a relative number field element does unexpected things:


```
sage: K
 Number Field in b with defining polynomial x^3 - 5 over its base field
sage: K([1,2,3])
 3*b^2 + (-6*a + 2)*b - 2*a + 7
sage: K([1,2,3])[0]
 1
sage: K([1,2,3])[1]
 2

sage: K([1,2,3]).list()
 [-2*a + 7, -6*a + 2, 3]
sage: K([1,2,3]).list()[0]
 -2*a + 7

sage: K([1,2,3]).polynomial()
 3*x^2 + 2*x + 1
```


The issue is that it's giving you the entries in the representation of the element as an *absolute* number field element. It should be fixed.


---

Comment by fwclarke created at 2009-03-13 18:54:57

This is sorted out by the patch in #5508, in particular the changes  there to `__getitem__` for the class `NumberFieldElement_relative` in `sage/rings/number_field/number_field_element.pyx`.


---

Comment by mabshoff created at 2009-03-25 08:55:53

To close this we would need a doctest.

Cheers,

Michael


---

Comment by fwclarke created at 2009-03-26 08:59:20

Replying to [comment:2 mabshoff]:
> To close this we would need a doctest.

See lines 2421 to 2445 of sage/rings/number_field/number_field_element.pyx as patched by #5508:

```
        EXAMPLES::
        
            sage: K.<a, b> = NumberField([x^3 - 5, x^2 + 3])
            sage: c = (a + b)^3; c
            3*b*a^2 - 9*a - 3*b + 5
            sage: c[0]
            -3*b + 5
        
        We illustrate bounds checking::
        
            sage: c[-1]
            Traceback (most recent call last):
            ...
            IndexError: index must be between 0 and the relative degree minus 1.
            sage: c[4]
            Traceback (most recent call last):
            ...
            IndexError: index must be between 0 and the relative degree minus 1.
        
        The list method implicitly calls ``__getitem__``::
        
            sage: list(c)
            [-3*b + 5, -9, 3*b]
            sage: K(list(c)) == c
            True
```



---

Comment by mabshoff created at 2009-03-26 20:35:27

Fixed in Sage 3.4.1.alpha0 via #5508. Thanks Francis :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-26 20:35:27

Resolution: fixed

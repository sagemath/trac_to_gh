# Issue 3024: notebook -- parses tracebacks in the output of docstrings of help command

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-25 17:32:45

Assignee: boothby

The Traceback thing gets all messed up by worksheet.py or cell.py below:


```
sage: help(VectorSpace)
          	

Help on function VectorSpace in module sage.modules.free_module:

VectorSpace(K, dimension, sparse=False, inner_product_matrix=None)
    EXAMPLES:
    The base can be complicated, as long as it is a field. 
        sage: V = VectorSpace(FractionField(PolynomialRing(ZZ,'x')),3)
        sage: V
        Vector space of dimension 3 over Fraction Field of Univariate
Polynomial Ring in x over Integer Ring
        sage: V.basis()
        [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
        ]
    
    The base must be a field or a \code{TypeError} is raised.
        sage: VectorSpace(ZZ,5)
Traceback (click to the left for traceback)
...
        TypeError: K must be a field

```



---

Attachment


---

Comment by boothby created at 2008-05-12 05:58:13

works for me


---

Comment by mabshoff created at 2008-05-17 19:55:49

Resolution: fixed


---

Comment by mabshoff created at 2008-05-17 19:55:49

Merged in Sage 3.0.2.alpha1

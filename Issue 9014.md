# Issue 9014: Implement a repr_prod

Issue created by migration from https://trac.sagemath.org/ticket/9014

Original creator: nborie

Original creation time: 2010-05-22 09:29:33

Assignee: jason

CC:  nthiery

Keywords: repr product

As for linear combinaison, implement a method in misc 'repr_prod' to represent products. 


```
def repr_prodcomb(symbols, coeffs, is_latex=False):
    r"""
    Compute a string representation of a product combination of some
    formal symbols
    """
    bla bla bla

sage: repr_prodcomb(['a','b','c'], [1,-2,-3])
'a * b^-2 * c^-3'
sage: repr_prodcomb([],[])
'1'
```


There is already a such function in sage/rings/polynomial/polynomial_element_generic.py

With categories will come FreeGroups(Gens), FreeMonoid(Gens), Free... Such futurs features motivate the need of this function.


---

Comment by nborie created at 2010-05-22 09:30:40

Feel free to sugest a better name (still sorry for my english...) and a better description.

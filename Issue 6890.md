# Issue 6890: No help for is_SymbolicVariable ?

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-09-04 18:55:24

Assignee: tba

Keywords: partial, help, doc

Help for is_SymbolicVariable and is_SymbolicExpressionRing is nonexistent, for Python reasons, apparently:

```
sage: is_SymbolicExpressionRing??
Error getting source: could not find class definition
Type: partial
...
partial(func, *args, **keywords) - new function with partial application of the given arguments and keywords.
```

Notice that these functions do have useful docstrings, they just aren't showing up.  This was originally reported in #2562.


---

Comment by mhansen created at 2013-07-23 15:31:47

This works fine now after an explicit import:


```
sage: is_SymbolicExpressionRing??
Type:       builtin_function_or_method
String Form:<built-in function is_SymbolicExpressionRing>
Definition: is_SymbolicExpressionRing(R)
Source:
def is_SymbolicExpressionRing(R):
    """
    Returns True if *R* is the symbolic expression ring.

    EXAMPLES::

        sage: from sage.symbolic.ring import is_SymbolicExpressionRing
        sage: is_SymbolicExpressionRing(ZZ)
        False
        sage: is_SymbolicExpressionRing(SR)
        True
    """
    return R is SR
```



---

Comment by mhansen created at 2013-07-23 15:31:47

Resolution: invalid

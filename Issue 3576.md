# Issue 3576: stupid bug in RDF

Issue created by migration from https://trac.sagemath.org/ticket/3576

Original creator: was

Original creation time: 2008-07-06 22:22:32

Assignee: somebody

This is sad:


```
sage: RDF(-1).nth_root(2)
```


Look at the dumb code in real_double.pyx:

```
    def nth_root(self, int n):
        """
        Returns the $n^{th}$ root of self.
        EXAMPLES:
            sage: r = RDF(-125.0); r.nth_root(3)
            -5.0
            sage: r.nth_root(5)
            -2.6265278044
        """
        if n == 0:
            return RealDoubleElement(float('nan'))
        if self._value < 0 and GSL_IS_EVEN(n):
            pass #return self._complex_double_().pow(1.0/n)
        else:
            return RealDoubleElement(self.__nth_root(n))
```


Amazingly this was introduced in the very first patch by Tom Boothby in 2006 and nobody ever noticed!!


---

Comment by was created at 2008-07-06 23:07:19

This is also bad, bad, bad:

```
sage: RDF(-1).nth_root(5)^(5)
-1.35861063971
```



---

Attachment


---

Comment by mhansen created at 2008-07-06 23:20:32

The code is definitely much better style and correctness-wise after the patch.

+1


---

Comment by mabshoff created at 2008-07-07 02:03:45

Merged in Sage 3.0.4.alpha2


---

Comment by mabshoff created at 2008-07-07 02:03:45

Resolution: fixed


---

Comment by boothby created at 2008-07-07 03:21:17

wow I'm dumb!

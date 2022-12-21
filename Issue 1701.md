# Issue 1701: attempt to clean up currRing if deallocated

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-01-06 13:23:05

Assignee: malb

This patch used to be attached to #1541 but logically doesn't belong there.


---

Attachment

I am under the impression that this patch already got merged, but I will investigate.

Cheers,

Michael


---

Comment by malb created at 2008-01-06 16:17:56

I just checked, it is not merged yet:

multi_polynomial_libsingular.pyx in Sage 2.9.2:


```
    def __dealloc__(self):
        """
        """
        cdef ring *oldRing = NULL
        if currRing != self._ring:
            oldRing = currRing
            rChangeCurrRing(self._ring)
        rDelete(self._ring)
        if oldRing != NULL:
            rChangeCurrRing(oldRing)
```



---

Comment by mabshoff created at 2008-01-07 17:28:14

Resolution: fixed


---

Comment by mabshoff created at 2008-01-07 17:28:14

Looks good to me, Merged in Sage 2.10.alpha0.

Cheers,

Michael

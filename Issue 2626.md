# Issue 2626: useless __list__ methods

Issue created by migration from https://trac.sagemath.org/ticket/2626

Original creator: cwitty

Original creation time: 2008-03-21 02:28:51

Assignee: cwitty

Sage 2.10.4 contains 5 `__list__` methods, which are never called.  Apparently the authors of these methods thought that list(x) would call `x.__list__()`, but it does not; the Python source code contains no instance of the string "`__list__`".

list(x) does call `x.__iter__()`, which is how the doctests on these methods manage to work.

The methods should be removed, so as not to mislead future developers into thinking they do something.


```
sage: search_src('__list__')
----------------------------------------------------------------------
----------------------------------------------------------------------
crypto/mq/mpolynomialsystem.py:    def __list__(self):
crypto/mq/mpolynomialsystem.py:    def __list__(self):
crypto/mq/sbox.py:    def __list__(self):
schemes/elliptic_curves/ell_point.py:    def __list__(self):
schemes/generic/morphism.py:    def __list__(self):
```



---

Comment by malb created at 2008-03-21 11:11:15

fixes the issue for crypto.mq


---

Attachment

fixes the issue for elliptic curve points over fields


---

Attachment


---

Comment by malb created at 2008-03-21 11:21:02

The attached patches remove all `__list__` instances mentioned above. I don't know how I got the idea that there is a special method called `__list__` in the first place. 

PS: I refuse to write a doctest for `SchemeMorphism_coordinates` because I don't even know how to construct such a thing! This class doesn't have a single line of documentation (though it is short to be fair).


---

Comment by mabshoff created at 2008-03-22 09:47:43

Nice patches, all the doctests pass [with known exception]. malb is correct in skipping doctests for `SchemeMorphism_coordinates` - hopefully somebody else will take care of that in a subsequent patch. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-22 09:48:11

Resolution: fixed


---

Comment by mabshoff created at 2008-03-22 09:48:11

Merged in Sage 2.11.alpha1

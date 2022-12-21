# Issue 263: CyclomicField elements do not pickle

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2007-02-15 22:26:27

Assignee: somebody


```
sage: I=CyclotomicField(4).gen()
sage: import pickle
sage: pickle.dumps(I)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)
```


The traceback is through a bunch of non-SAGE code.  It was not clear to me where to begin to look.


---

Comment by was created at 2007-02-16 07:24:25

This is not a bug.  Almost *NO* SAGE objects will pickle with the
Pure-python defeault pickle module, which simply can't support
the sort of sophisticated things needed for pickling SAGE objects.
Instead use either the save method, or dumps or loads, which uses
cPickle in mode 2. 

```
sage: I=CyclotomicField(4).gen()
sage: loads(dumps(I))
zeta4
```



---

Comment by was created at 2007-02-16 07:24:25

Resolution: fixed

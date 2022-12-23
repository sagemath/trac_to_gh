# Issue 281: Errors in matrix for extensions of NumberFields

Issue created by migration from https://trac.sagemath.org/ticket/281

Original creator: ncalexan

Original creation time: 2007-02-23 20:01:46

Assignee: somebody

Keywords: extension numberfield matrix polynomial

The following is incorrect:


```
sage: K.<a> = NumberField(ZZ['x'].0^3 - 5)

sage: L.<b> = K.extension(K['x'].0^2 - 3)

sage: b.matrix()
 
[0 1]
[0 0]

sage: M.<c> = NumberField(ZZ['x'].0^2 - 3)

sage: c.matrix()
 
[0 1]
[3 0]
```



---

Comment by was created at 2007-08-18 20:54:35

This is simply not implemented, and will be hard to do without rewriting number fields completely :-)
David Roe?

Anyway, in sAge-2.8 it raises a notimplementederror, so I've changed this from bug to enhancement.

William


```
sage: K.<a> = NumberField(ZZ['x'].0^3 - 5)
sage: L.<b> = K.extension(K['x'].0^2 - 3)
sage: b.matrix()
...    
Traceback (most recent call last):
...
NotImplementedError
```



---

Comment by was created at 2007-08-18 20:54:35

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2007-10-21 13:55:55

It works with Sage 2.8.8:

```
mabshoff@sage:/tmp/Work-mabshoff/sage-2.8.8$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.8, Release Date: 2007-10-20                       |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: K.<a> = NumberField(ZZ['x'].0^3 - 5)
sage: sage: L.<b> = K.extension(K['x'].0^2 - 3)
sage: sage: b.matrix()

[0 1]
[3 0]
sage: 
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-10-24 03:34:35

I would actually say that this was fixed by roed's rewrite. So it would be "fixed" in my book.

Cheers,

Michael


---

Comment by was created at 2007-10-24 03:38:14

Resolution: fixed


---

Comment by was created at 2007-10-24 03:38:14

yep, fixed by my rewrite (not david's).

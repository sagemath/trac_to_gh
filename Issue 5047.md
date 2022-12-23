# Issue 5047: comparing complex i raises error

Issue created by migration from https://trac.sagemath.org/ticket/5047

Original creator: burcin

Original creation time: 2009-01-21 07:57:23

Assignee: somebody


```
sage: cmp(i,0)

TypeError                                 Traceback (most recent call last)
/home/burcin/sage/sage-3.2.3/local/lib/python2.5/site-packages/sage/functions/functions.pyc in __cmp__(self, right)
    267             return 0
    268         R = RealField()
--> 269         c = cmp(R(self), R(right))
    270         if c: return c
    271         try:

...
/home/burcin/sage/sage-3.2.3/local/lib/python2.5/site-packages/sage/functions/constants.pyc in _mpfr_(self, R)
    865             TypeError
    866         """
--> 867         raise TypeError
    868 
    869     def _real_rqdf_(self, R):

TypeError: 
```



---

Comment by SimonKing created at 2009-01-23 20:03:59

I believe this ticket is close to being invalid, because Sage is nearly consistent with Python.

In Python, one gets

```
>>> cmp(1j,0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: no ordering relation is defined for complex numbers
```


Only I would say that the error message in Sage could be clearer. So, I suggest to catch the error and reraise a TypeError with an appropriate error message.


---

Comment by SimonKing created at 2009-01-23 20:23:42

raise a proper error message when using cmp on non-real constants


---

Attachment

Replying to [comment:1 SimonKing]:
> In Python, one gets
> {{{
> >>> cmp(1j,0)
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> TypeError: no ordering relation is defined for complex numbers
> }}}

With the patch, one gets

```
sage: cmp(i,0)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/king/.sage/temp/mpc739/25379/_home_king__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/home/king/SAGE/devel/sage-3.2.1/local/lib/python2.5/site-packages/sage/functions/functions.pyc in __cmp__(self, right)
    270             c = cmp(R(self), R(right))
    271         except TypeError:
--> 272             raise TypeError, "these objects are not comparable"
    273         if c: return c
    274         try:

TypeError: these objects are not comparable
```

which, I believe, is consistent with python.

Other comparisons still work:

```
sage: cmp(i^2,0)
-1
sage: cmp(e,0)
1
```



---

Comment by burcin created at 2009-01-23 21:13:16

I ran into this when testing new printing code in pynac. ATM, pynac uses the sign function, which is defined to be cmp(x, 0), to determine if it should print a minus sign. Thus, we have the following:


```
sage: var('x',ns=1)
sage: i*x
<boom>
```


I somehow thought that the cmp function was not supposed to raise exceptions, but googling shortly didn't turn up any evidence to support this argument.

I would be ok to live with this fact, and try to figure out a better way to handle the sign function, or printing in pynac.

BTW, the sign function is also mentioned here: #777


I give the attached patch a positive review, provided that doctests are added to test for the new error message.


---

Attachment


---

Comment by SimonKing created at 2009-01-23 22:44:36

The second patch `cmp_doc.patch` (to be applied after the first patch) adds more documentation.

Replying to [comment:3 burcin]:
> I ran into this when testing new printing code in pynac. ATM, pynac uses the sign function, which is defined to be cmp(x, 0), to determine if it should print a minus sign. Thus, we have the following:
> 
> {{{
> sage: var('x',ns=1)
> sage: i*x
> <boom>
> }}}

Ok, but I think there should be a different approach for determining the sign when printing an imaginary number. 
However, personally I believe that `sign(I)` should raise an error.

> I somehow thought that the cmp function was not supposed to raise exceptions, but googling shortly didn't turn up any evidence to support this argument.

... and, as I mentioned above, `cmp` does raise an exception in Python.

> BTW, the sign function is also mentioned here: #777

The `sign` function defined in #777 would simply return 0 on non-real constants, because it tests `bool(x > 0)`. Indeed, we have

```
sage: bool(I > 0)
False
sage: bool(I < 0)
False
```

so, at least it does not go boom (which it _should_, though!).


---

Comment by burcin created at 2009-01-23 23:29:43

Positive review, both patches should be applied.


---

Comment by mabshoff created at 2009-01-24 16:28:25

Merged in Sage 3.3.alpha2


---

Comment by mabshoff created at 2009-01-24 16:28:25

Resolution: fixed

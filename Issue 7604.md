# Issue 7604: Bug in continued fractions module (contfrac).  Patch attached

Issue created by migration from https://trac.sagemath.org/ticket/7604

Original creator: solevillar

Original creation time: 2009-12-04 16:37:52

Assignee: AlexGhitza

CC:  solevillar@gmail.com

Keywords: contfrac

I've found this bug in the contfrac module:


```
sage: a=continued_fraction(sqrt(2))
sage: a.qn(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_4.py", line 5, in <module>
    a.qn(_sage_const_0 )
  File "", line 1, in <module>
    
  File "/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/contfrac.py", line 461, in qn
    if len(self.__qn) < n+3:
AttributeError: 'ContinuedFraction' object has no attribute '_ContinuedFraction__qn'
```


But this actually works:

```
sage: a=continued_fraction(sqrt(2))
sage: b=a.pn(0)
sage: a.qn(0)
1
```



That's because the method contfrac.pn initializes the attributes pn and qn so if you call contfrac.qn before calling contfrac.pn the attribute qn wont be initialized and that's why it doesn't work in the first snippet.

I wrote a patch that solves this problem (minor changes, very easy to solve). I'm attaching that patch.



---

Comment by solevillar created at 2009-12-04 16:39:53

patch for contfrac module


---

Comment by solevillar created at 2009-12-04 16:42:14

Changing status from new to needs_review.


---

Attachment


---

Comment by fwclarke created at 2009-12-05 12:48:31

There are several problems:

1.  The attachment is not actually a patch but a new version of the `contfrac.py` file.

2.  The change to `is_field` to remove the optional parameter `proof=True` is unhelpful since every other instance of `is_field` has the argument proof, and Sage contains code which uses this argument and will crash without it.

3.  At lines 456-457 the line n = ZZ(n) has been duplicated.  In fact this line is not needed at all.

4.  The correction of the bug is a bit more complicated than necessary.

I have attached a patch which deals with the bug, and have made a minor change to a doctest so that it would have detected the bug.


---

Comment by fwclarke created at 2009-12-05 12:49:55

Use instead


---

Attachment

Looks good to me.

solevillar`@`gmail.com, could we get your name for the release notes?  Or, you could updated the Authors field on this ticket.  Thanks!


---

Comment by mhansen created at 2009-12-07 08:12:11

Resolution: fixed

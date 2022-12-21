# Issue 5997: deprecate the "order" method on elements of rings.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-05-06 17:55:43

Assignee: tbd

There was a vote in sage-devel in the thread entitled "order of elements in the field" to deprecate the order method on ring elements, and keep just the additive_order and multiplicative_order methods.  The order method is too ambiguous in the context of rings, and does cause regular confusion.  

This should be officially deprecated, and only removed after >= 6 months. 


---

Comment by jhpalmieri created at 2009-05-06 19:30:34

Here's a very simple patch.


---

Comment by mabshoff created at 2009-05-06 21:30:31

Shouldn't this patch add a doctest while adding the deprecation warning? Otherwise it isn't obvious that the function is depreacted from looking at "order?"

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-05-07 05:23:45

> Shouldn't this patch add a doctest while adding the deprecation warning?

No, I don't think so... Just kidding.  Here's a new patch with a doctest.


---

Attachment

reviewer patch; fix trivial typo


---

Comment by mvngu created at 2009-05-08 00:23:56

REFEREE REPORT



The patch `trac_5997.patch` applies OK against the "post-final" sage-3.4.2 and all doctests pass with the options `-t -long`. Now say we create an element in `Z/12Z` like so:

```
sage: a = Integers(12)(5)
```

Then both `a.order()` and ` a.additive_order()` return the same result, but `a.order()` additionally gives a deprecation warning:

```
sage: a.order()
/scratch/mvngu/sage-3.4.2-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/IPython/iplib.py:2073: DeprecationWarning: The function order is deprecated for ring elements; use additive_order or multiplicative_order instead.
  exec code_obj in self.user_global_ns, self.user_ns
12
```




However, there's one trivial typo in the patch. This is fixed in the reviewer patch `trac_5997-reviewer.patch`. Basically, I give positive review to John's patch. Only my patch needs to be reviewed.


---

Comment by mabshoff created at 2009-05-08 00:38:06

Rubber stamp. We don't need no stinkin' review for trivial review patches fixing an obvious typo ;)

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-13 18:27:56

Resolution: fixed


---

Comment by mabshoff created at 2009-05-13 18:27:56

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael

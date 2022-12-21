# Issue 1578: [with patch, with bundle] Make polynomial .diff() accept optional argument times for repeated differentiation.

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2007-12-21 03:53:30

Assignee: malb

Keywords: polynomial diff times repeat

Make polynomial .diff() accept optional argument times for repeated differentiation.

Makes diff do its thing multiple time if requested.

```
-    def diff(self, MPolynomial_libsingular variable, have_ring=True):
+    def diff(self, MPolynomial_libsingular variable, times=1, have_ring=True):
```



---

Comment by ncalexan created at 2007-12-21 03:55:00

Hmm, bundle and patch might need to be rebased.  Sorry.


---

Comment by mabshoff created at 2007-12-21 08:54:56

Changing priority from minor to major.


---

Comment by mhansen created at 2007-12-22 21:33:59

The failures are okay, since they just have redundant information.  I tested things out and all tests passed.


---

Attachment

This should be the final version; use this over the two earlier bundles and one earlier patch.


---

Comment by mabshoff created at 2008-01-13 02:04:29

I deleted the older patches and bundles.

Cheers,

Michael


---

Comment by robertwb created at 2008-01-13 08:25:47

'times' seems like an odd name for the argument--it returns the "times-th derivative"?


---

Comment by malb created at 2008-01-13 11:45:31

How about accepting monomials instead of variables only. Then x<sup>2</sup> would encode 2-times x, and x<sup>2</sup>y<sup>3</sup> would mean 3-times y and 2-times x.


---

Comment by robertwb created at 2008-01-14 18:04:36

I don't know if we implement any, but there are functions such that `d^2f/dxdy != d^2 f/dydx`. 

However, I think the ability to pass in a monomial is an excellent idea. Perhaps beyond the scope of this patch though.


---

Comment by malb created at 2008-01-18 16:29:13

Changing assignee from malb to ncalexan.


---

Comment by jason created at 2008-02-04 17:08:04

In mathematica, you can pass a list to the differentiate command and the function will be differentiated with respect to successive elements of the list.  So maybe something like:

f.diff([x,y,y,x])

could specify differentiating first wrt x, then y, then y, and then x again.

The command in the patch could be invoked as:

f.diff([x]*3)

I agree that f.diff(x,3) looks better, though.


---

Comment by jason created at 2008-02-04 17:28:32

We should probably note that this is supported by symbolic polynomials already.


```
sage: x,y=var('x y')
sage: f=exp(2*x*y)
sage: f.diff(x)
2*y*e^(2*x*y)
sage: f.diff(x,x)
4*y^2*e^(2*x*y)
sage: f.diff(x,2)
4*y^2*e^(2*x*y)
sage: f.diff(x,2,y)
8*x*y^2*e^(2*x*y) + 8*y*e^(2*x*y)
sage: f.diff(x,2,y,y)
16*x^2*y^2*e^(2*x*y) + 32*x*y*e^(2*x*y) + 8*e^(2*x*y)
sage: f.diff(x,2,y,2)
16*x^2*y^2*e^(2*x*y) + 32*x*y*e^(2*x*y) + 8*e^(2*x*y)
```



---

Comment by cremona created at 2008-02-16 17:20:32

The patch looks ok to me, looking at the diffs (I have not tried applying it).


---

Comment by dmharvey created at 2008-02-28 03:10:28

there is action on this at #753


---

Comment by dmharvey created at 2008-03-03 14:32:10

I am closing this since it has been superseded by #753.


---

Comment by dmharvey created at 2008-03-03 14:32:10

Resolution: duplicate


---

Comment by mabshoff created at 2008-03-03 16:13:50

Resolution changed from duplicate to 


---

Comment by mabshoff created at 2008-03-03 16:13:50

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-03-03 16:13:58

This isn't really a duplicate and I consider this fixed. It looks like a borderline case, so I tend to call those tickets fixed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-03 16:13:58

Resolution: fixed

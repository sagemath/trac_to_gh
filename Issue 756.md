# Issue 756: modify how foo.derivative(...) works

Issue created by migration from https://trac.sagemath.org/ticket/756

Original creator: was

Original creation time: 2007-09-26 20:48:58

Assignee: somebody


```
On 9/26/07, David Joyner <wdjoyner@gmail.com> wrote:
> I'm not sure if this is a bug or not but just in case,
> here is the way diff is behaving for me.
>
> - David Joyner
>
> sage: version()
> 'SAGE Version 2.8.5, Release Date: 2007-09-21'
> sage: R1.<a> = PolynomialRing(QQ)
> sage: R2.<x> = PowerSeriesRing(R1)
> sage: y = a*x
> sage: y.derivative()
> a
> sage: diff(y,x)
> ---------------------------------------------------------------------------
> <type 'exceptions.TypeError'>             Traceback (most recent call last)
>
> /mnt/hd200/sagefiles/sage-2.8.3.rc3/<ipython console> in <module>()


One should slightly rewrite the derivative function for
polynomials (and power series) to take
an optional argument (the variable).  If the
innput variable is the same as the parent
gen, then differentiate as before; otherwise
attempt to call derivative on the coefficients -- if
that works, good; if not, return 0.

 -- William
```



---

Comment by AlexGhitza created at 2008-02-16 20:52:43

Made the changes suggested above by William, see the patch.


---

Comment by dmharvey created at 2008-02-18 00:21:22

Few minor issues to sort out.

In the `polynomial_element_generic.py` version, some indentation has gone awry (the `if d.has_key(-1):` block is indented more than it used to be).

As a general rule please use `if x is None` instead of `if x == None`, because it's 100x faster:

```
sage: x = 5

sage: timeit if x is None: y = 6
1000000 loops, best of 3: 239 ns per loop

sage: timeit if x == None: y = 6
10000 loops, best of 3: 31.9 µs per loop
```


The phrase "if the latter is absent" is a bit confusing; the first time I read it I thought it meant "if the object being differentiated doesn't have the latter", which is completely wrong. Maybe something like "if no var is supplied"?


---

Attachment


---

Comment by AlexGhitza created at 2008-02-18 02:07:40

Excellent points from David.  I've made the changes and uploaded a new patch.


---

Attachment


---

Comment by dmharvey created at 2008-02-18 03:22:30

I've attached a patch (should be applied on top of alex's patch) which adds some more doctests. The last doctest in the power series case currently fails; I think it should  pass.


---

Attachment


---

Comment by AlexGhitza created at 2008-02-18 13:43:59

Again, excellent catch by David.  I've fixed the problem with the power series doctest (which by the way should give 2+y+..., not y+2+... :)

Apply 756-derivative-wrt-new.patch instead of the others (it includes them and the fixes).


---

Comment by dmharvey created at 2008-02-18 15:51:59

With `756-derivative-wrt-new.patch` I'm getting doctest failures for `sage/schemes/elliptic_curves/padics.py`, involving the power series case. I think the problem is it's calling the underlying polynomial type's `derivative` function with an argument, but for some reason that underlying derivative function doesn't accept an argument. This is a shame, the whole issue is becoming more complicated than it should have been. Note there are possible interactions with #753 and #1578. We really need a standardised solution for this across all polynomial, power series (univariate/multivariate) and symbolic objects.


---

Comment by dmharvey created at 2008-02-18 16:15:17

Here's a possible plan of action. Someone needs to audit all polynomial, power series, symbolic classes, and produce a list of currently existing `derivative` and `diff` (and `differentiate`?) methods, and what parameters they accept. This needs to be summarised and presented to sage-devel. Discussion will ensue, and we'll agree on a uniform solution. Then someone needs to go and implement it. The main objectives should be: (i) consistency from a programmatic point of view, (ii) ease of use for new users (they shouldn't need to learn how to differentiate more than once).

I'm happy to lead the charge, but I won't get around to it for at least a week. Alex, if you're interested, go right ahead (although I realise that you probably didn't intend to get so deeply into this issue when you posted the first patch for this ticket....)


---

Comment by AlexGhitza created at 2008-02-19 16:47:43

I agree with David's comments and with the need for cleaning up the derivative methods.  This should be done carefully, so it doesn't lend itself very well to the 15-minute spurts that I can dedicate to Sage these days.  I can try to think about it and rummage throught the code on Saturday, but if someone else feels energetic, by all means, go for it!

One related remark: there are also integrate() methods for polys and power series, and they should benefit from the same treatment.


---

Comment by dmharvey created at 2008-02-28 03:09:55

currently there is action on this at #753


---

Comment by dmharvey created at 2008-03-03 14:31:28

Resolution: duplicate


---

Comment by dmharvey created at 2008-03-03 14:31:28

I am closing this since it has been superseded by #753.


---

Comment by mabshoff created at 2008-03-03 16:11:15

Resolution changed from duplicate to 


---

Comment by mabshoff created at 2008-03-03 16:11:15

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-03-03 16:11:22

Resolution: fixed


---

Comment by mabshoff created at 2008-03-03 16:13:38

This isn't really a duplicate and I consider this fixed. It looks like a borderline case, so I tend to call those tickets fixed.

Cheers,

Michael

# Issue 75: specify charpoly polynomial ring

Issue created by migration from https://trac.sagemath.org/ticket/75

Original creator: was

Original creation time: 2006-09-22 13:04:13

Assignee: somebody

Joe Wetherell's idea:

On Fri, 22 Sep 2006 00:51:17 -0700, Joseph L Wetherell <jlwether`@`alum.mit.edu> wrote:

>> I really want to agree with you, but I also want to know: what do we
>> do in the situations I outlined before? For example, if you do

```
>>
>> sage: M = Matrix(QQ, 2, 2, range(4))
>> sage: f = M.charpoly()
>> sage: g = M.charpoly()
```

>> Now f and g have different parents, but you *can't* coerce g to the
>> parent of f (or vice versa), because you can't assume the generators
>> match up.
>
> OK, so perhaps the problem is that charpoly needs another argument
> -- namely the variable in which the characteristic polynomial
> is to be expressed.

That's a great idea.  Having an optional

```
   f = M.charpoly(x)
```

and/or

```
   f = M.charpoly(PolynomialRing(ZZ))
```

wouldn't break anything (it's optional), and would be easy 
to implement, and really just makes sense.  I like it. 


---

Comment by was created at 2006-09-22 13:22:41


```
> I like this idea. What you're really saying is: evaluate charpoly on
> some ring element that I hand you. If that ring element is the
> generator of some polynomial ring, then the charpoly code should be
> smart enough to work in that ring from the beginning. You can
> actually do something like this already, with pretty neat notation,
> at the loss of some efficiency:
>
> sage: M = Matrix(QQ, 2, 2, range(4))
> sage: f = M.charpoly()
> sage: f
>   x^2 - 3*x - 2
> sage: R.<y> = PolynomialRing(QQ)
> sage: f.parent() is R
> False
> sage: f(y)
>   y^2 - 3*y - 2
> sage: f(y).parent() is R
> True
>
> Actually the efficiency loss maybe isn't too bad, if the __call__
> method is smart enough to recognise when it's passed the ring
> generator, it can just copy the coefficients (faster than computing
> charpoly!! at least for large degree).

In fact, we could make
    M.charpoly(z)
work for any z in any ring at all.

> But you're right, it would be good if you could supply the variable
> directly. Should we put this on trac?

```



---

Comment by was created at 2006-09-22 14:16:08


```
Say I'm doing some calculations in a power series ring with default
precision = N. Then I call some subroutine that happens to do some
power series ring calculations too. It's possible that the subroutine
will change the precision for its own purposes. When it returns, my
precision has mysteriously changed to M. This can lead to all kinds
of subtle bugs. Basically it would mean that if you use the
globalised ring, then you don't have any assurances that its
precision won't change from one step to the next. Unless you mean to
store a separate ring for each possible precision? Or maybe you mean
to force the precision to remain constant for the globalised ring?
 
Globalized rings should be immutable, so all defining properties such
as default precision, variable print name, etc., should be fixed.
SAGE currently doesn't have any mutability stuff for rings yet, but it
should, exactly for this reason.
 }}}


Default precision shouldn't be changeable anyways, though. (It is, but
it shouldn't be.)
It would suck if you call a function and suddenly the default precision
of your ring gets changed.
 
William


---

Comment by was created at 2007-12-01 17:40:11

Resolution: fixed


---

Comment by cwitty created at 2007-12-01 17:43:32

In current Sage, you can already set the name of the variable (although not the ring).  Also, the problem in the original description ("f and g have different parents") is no longer true; in current Sage, f and g have the same parent.

So we're closing this ticket.

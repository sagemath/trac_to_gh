# Issue 9046: missing documentation and bug in collect

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-05-25 12:02:04

Assignee: burcin

CC:  kcrisman

the documentation from `collect` does not say what this function
does. It should be documented.

Also, if it does what its name suggests, i.e., collect terms with
same exponent in 's', the following example shows that it seems that
the user should call `expand` before, since terms in `x^3`
are not properly collected:

```
sage: (x^2+(y-x^2)*(y+x)).collect(x)
-(x + y - 1)*x^2 + x^3 - (x^2 - y)*x + y^2
sage: (x^2+(y-x^2)*(y+x)).expand().collect(x)
-(y - 1)*x^2 - x^3 + x*y + y^2
```


Finally this seems a bug (note the instances of `-x^2` and
`x^2`):

```
var('a b x y z')
sage: p = -a*x^3 - a*x*y^2 + 2*b*x^2*y + 2*y^3 + x^2*z + y^2*z + x^2 + y^2 + a*x
sage: p.collect(x)
-a*x^3 + (2*b*y + z + 1)*x^2 - x^2 - (a*y^2 - a)*x + x^2 + 2*y^3 + y^2*z + y^2


---

Comment by burcin created at 2010-05-26 11:07:10

Here is the same session using GiNaC directly via `ginsh`:


```
> t= -a*x^3 - a*x*y^2 + 2*b*x^2*y + 2*y^3 + x^2*z + y^2*z + x^2 + y^2 + a*x;
x^2+2*y*b*x^2+y^2+y^2*z+a*x+2*y^3-a*x^3-y^2*a*x+z*x^2
> t;
x^2+2*y*b*x^2+y^2+y^2*z+a*x+2*y^3-a*x^3-y^2*a*x+z*x^2
> collect(t, x);
(1+2*y*b+z)*x^2+y^2+y^2*z+2*y^3-a*x^3-(y^2*a-a)*x
> u = (x^2+(y-x^2)*(y+x));
x^2-(y+x)*(x^2-y)
> collect(u, x);
x^3-(x^2-y)*x+y^2-(-1+y+x)*x^2
```


It seems that one needs to call `expand()` explicitly before calling `collect()`. I think this should just be documented in the docstring.

The problem with `-x^2 + x^2` appearing in the output is probably a bug I introduced while playing with the ordering of the terms. I will take a look at it when I find a chance. It's likely to be later than a week though.


---

Comment by burcin created at 2010-05-26 11:07:10

Changing keywords from "" to "pynac".


---

Comment by kcrisman created at 2011-03-16 15:32:55

Changing priority from critical to minor.


---

Comment by kcrisman created at 2011-03-16 15:32:55

This is not critical.


---

Comment by kcrisman created at 2012-07-07 02:52:53

Changing component from calculus to symbolics.


---

Comment by kcrisman created at 2012-07-07 02:52:53

It turns out that #11839 was opened and did the first part of this ticket, including documenting the `expand()` issue.

However, the bug remains, so I'll just change this ticket to be about it.


---

Comment by burcin created at 2012-07-07 07:22:40

With the new description, this is probably a duplicate of #9880. I will check if the pynac changes for that ticket fix this one.


---

Comment by zimmerma created at 2012-07-09 12:50:39

bug still present in Sage 5.0.

Paul


---

Comment by burcin created at 2012-07-10 09:15:30

This is a duplicate of #9880. With [the Pynac patch queue](https://bitbucket.org/burcin/pynac-patches/src) and patches listed on #9880, I get:


```
sage: var('a b x y z')
(a, b, x, y, z)
sage: p = -a*x^3 - a*x*y^2 + 2*b*x^2*y + 2*y^3 + x^2*z + y^2*z + x^2 + y^2 + a>
sage: p.collect(x)
-a*x^3 + (2*b*y + z + 1)*x^2 + 2*y^3 + y^2*z - (a*y^2 - a)*x + y^2
```


We should close this after adding it as a doctest to #9880.


---

Comment by burcin created at 2012-07-10 09:15:30

Changing status from new to needs_review.


---

Comment by burcin created at 2012-07-27 13:00:49

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2012-07-27 13:00:49

Doctest is in attachment:trac_9880-doctest_for_9046.patch:ticket:9880. This can be closed now.


---

Comment by zimmerma created at 2012-07-27 13:13:45

Burcin,

first the ticket number is wrong (13107 instead of 9046) then the input p was mangled
(ends with `a>` instead of `a*x`).

Paul


---

Comment by zimmerma created at 2012-07-27 13:13:45

Changing status from positive_review to needs_work.


---

Comment by burcin created at 2012-11-21 21:31:39

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2012-11-21 21:31:39

I replaced the patch attached to #9880:

attachment:trac_9880-doctest_for_9046.patch:ticket:9880

I hope I got it right this time. Sorry for the noise.


---

Comment by zimmerma created at 2012-11-22 08:11:04

the patch is ok now. But since #9880 is not yet fixed, the doctest will fail. Thus we should wait for #9880 to review this one...

Paul


---

Comment by kcrisman created at 2013-06-18 19:57:29

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2013-06-18 19:57:29

That ticket has been merged, so I think this can be closed.


---

Comment by jdemeyer created at 2013-06-19 12:17:29

Resolution: duplicate

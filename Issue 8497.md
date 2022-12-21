# Issue 8497: bug in simplify_rational

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-03-11 10:33:15

Assignee: burcin

CC:  kcrisman burcin jason mhansen

Keywords: simplify, radical, sqrt

the documentation of `simplify_radical` says:

```
sage: x.simplify_radical?
...
       Simplifies this symbolic expression, which can contain logs,
       exponentials, and radicals, by converting it into a form which is
       canonical over a large class of expressions and a given ordering of
       variables
```

however if indeed it is able to recognize zero:

```
sage: a=1/(sqrt(5)+sqrt(2))-(sqrt(5)-sqrt(2))/3
sage: a.simplify_radical()
0
```

it does *not* return a canonical expression:

```
sage: a1=1/(sqrt(5)+sqrt(2))
sage: a2=(sqrt(5)-sqrt(2))/3
sage: a1.simplify_radical()
1/(sqrt(2) + sqrt(5))
sage: a2.simplify_radical()
-1/3*sqrt(2) + 1/3*sqrt(5)
sage: (a1-a2).simplify_radical()
0
```



---

Comment by zimmerma created at 2010-03-11 10:38:08

Note the original question posed to me was: how to multiply say 1/(1+sqrt(2)+sqrt(3)) by the
conjugate expression?


---

Comment by mhansen created at 2010-03-11 17:56:59

This is the full docstring from Maxima:


```
Simplifies expr, which can contain logs, exponentials, and radicals, by converting it into a form which is canonical over a large class of expressions and a given ordering of variables; that is, all functionally equivalent forms are mapped into a unique form. For a somewhat larger class of expressions, radcan produces a regular form. Two equivalent expressions in this class do not necessarily have the same appearance, but their difference can be simplified by radcan to zero.

    For some expressions radcan is quite time consuming. This is the cost of exploring certain relationships among the components of the expression for simplifications based on factoring and partial-fraction expansions of exponents. 
```


Perhaps we should include this


---

Comment by zimmerma created at 2010-03-11 19:29:08

> Perhaps we should include this 

yes (unless of course upstream finds a way to get a real canonical form).
And maybe adding an example showing the difference when checking for 0.


---

Comment by kcrisman created at 2011-09-23 14:46:56

What is really going on here is that `simplify_radical` uses `radcan` under the hood, which treats things as symbolic expressions, not functions, and just chooses a branch - consistently, but arbitrarily.  At least I think that is what is going on here.  See [the Maxima list thread starting here](http://www.math.utexas.edu/pipermail/maxima/2011/026097.html).


---

Comment by zimmerma created at 2011-09-23 14:57:38

then should we simply change the documentation, in saying that `simplify_radical` gives a
canonical expression for zero, but if a and b are two identical expressions, they might not
be "simplified" to the same expression?

Paul


---

Comment by kcrisman created at 2011-09-23 14:59:21

You are correct.  I was just updating, though, at this point.  

It gets worse, because some expressions that are definitely not 1 will simplify to just 1, because that is the branch that was picked.  See [this ask.sagemath.org question](http://ask.sagemath.org/question/767/simplification-errors-in-simple-expressions), and Fateman's accurate response.


---

Comment by zimmerma created at 2011-09-23 15:05:30

then I suggest to simply remove this function from Sage, unless there are ideas how to fix it.

Paul


---

Comment by kcrisman created at 2011-09-23 15:20:32

Well, in Fateman's eyes (and I would remind that he is an expert, if not THE expert, in this), the only bug is in users who treat these _expressions_ as _functions_.  At least, that's how I interpret it.  So updating the documentation may be the better way.

But this shouldn't be a duologue; hopefully some others will have ideas.  Cc:ing a few others who have thought about at least one or two of these things, just in case they have thoughts at this time.  Otherwise it will sit - I simply don't have time to deal with it right now, because it needs to be part of a general overhaul of simplification if we don't just change documentation.


---

Comment by kcrisman created at 2011-09-23 15:20:58

I mean change documentation to give examples in prominent places, both in `simplify_radical` and `simplify_full`.


---

Comment by zimmerma created at 2011-09-24 07:21:37

I believe we should at least add such examples to the documentation, to warn the user that in some
cases no canonical form is returned.

Paul


---

Comment by kcrisman created at 2011-09-24 14:56:48

Okay.  So whoever does this ticket will do that :)

(Incidentally, mentioning that they _are_ canonical, but in Fateman's sense of expressions, not in the way we would think of them as functions.)


---

Attachment


---

Comment by zimmerma created at 2011-09-25 21:06:01

Changing status from new to needs_review.


---

Comment by zimmerma created at 2011-09-25 21:06:01

the attached patch implements what I suggest in comment [comment:11].

Paul


---

Comment by burcin created at 2011-10-07 09:38:05

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2011-10-07 09:38:05

Looks good to me.


---

Comment by jdemeyer created at 2011-10-07 12:32:00

Fixed some formatting of the documentation, needs review.


---

Comment by jdemeyer created at 2011-10-07 12:32:00

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-10-07 12:32:06

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2011-10-07 13:21:05

Fixed doc formatting, apply only this


---

Attachment

I feel that we should at least ask on the Maxima list about whether this is truly "not canonical".  My understanding is that Fateman would say it is canonical as an _expression_, not as a _function_.   If I'm the only one who feels this way, I'll let it slide.   But I figure we would want him to give us benefit of the doubt in our areas of expertise.


---

Comment by kcrisman created at 2011-10-07 16:52:47

Changing status from needs_review to needs_info.


---

Comment by zimmerma created at 2011-10-08 09:23:03

For me, a "canonical expression" means that two mathematically identical expressions simplify to
the *exactly same* expression. Thus it is clearly not canonical. Feel free to ask on the Maxima
list, but this should not delay this ticket.

Paul


---

Comment by jdemeyer created at 2011-10-08 09:40:08

Changing status from needs_info to needs_review.


---

Comment by jdemeyer created at 2011-10-08 09:40:08

Replying to [comment:18 zimmerma]:
> this should not delay this ticket.

I agree but somebody needs to review my reformatting of the documentation.


---

Comment by burcin created at 2011-10-10 08:58:32

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2011-10-10 08:58:32

I am not well versed in ReST, but AFAICT, Jeroen's changes make sense.

Maxima documentation on `radcan()` (below) is rather vague. Based on this text, we shouldn't make bold claims about canonical results in the Sage documentation. I am switching this back to positive review.


```
Simplifies expr, which can contain logs, exponentials, and radicals, by
converting it into a form which is canonical over a large class of expressions
and a given ordering of variables; that is, all functionally equivalent forms
are mapped into a unique form. For a somewhat larger class of expressions,
radcan produces a regular form. Two equivalent expressions in this class do
not necessarily have the same appearance, but their difference can be
simplified by radcan to zero.

For some expressions radcan is quite time consuming. This is the cost of
exploring certain relationships among the components of the expression for
simplifications based on factoring and partial-fraction expansions of
exponents. 
```


We can open an enhancement ticket to clarify what 
 * _ a large class of expressions_
 * _functionally equivalent_
 * _ regular form_
mean in the text above, and how the ordering of the variables effect the final result. Ideally, we should have references to a description of the underlying algorithm as well.


---

Comment by kcrisman created at 2011-10-10 12:46:30

Okay, that's now #11912.


---

Comment by jdemeyer created at 2011-10-10 20:19:59

Resolution: fixed

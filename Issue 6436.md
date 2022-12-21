# Issue 6436: ideal([]) gives unhelpful error message

Issue created by migration from Trac.

Original creator: broune

Original creation time: 2009-06-27 22:55:50

Assignee: tbd

When I type "ideal([])" in Sage 4.0.1 I get an error message intended for a different case:


```
sage: ideal([])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: unable to find common ring into which all ideal generators map
```


This error message is incorrect since, trivially, the empty set of generators will map into any ring at all. The attached patch changes this to


```
sage: ideal([])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: unable to determine which ring to embed the ideal in
```


By the way, the function ideal in ideal.py has a documentation section named TESTS with doctests in it. As far as I can determine, these doctests do not get run.


---

Attachment

> By the way, the function ideal in ideal.py has a documentation section named TESTS with doctests in it. As far as I can determine, these doctests do not get run.

I'm not sure why you say this.  If you add lines like

```
sage: 3+5
9
```

to that section, you get a doctest failure.  At least, I do.  I think that your addition to that section doesn't produce an error because it starts with `Sage:`, not `sage:`.  Since you already test this failure earlier, I'm adding a referee's patch deleting this non-doctest from the TESTS section, and also fixing a small reST issue.


---

Attachment


---

Comment by rlm created at 2009-07-04 01:22:22

Resolution: fixed

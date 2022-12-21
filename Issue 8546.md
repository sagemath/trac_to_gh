# Issue 8546: add section on deprecating functions to developer's guide

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2010-03-16 03:37:21

Assignee: mvngu

CC:  kcrisman

Many functions in the Sage library are deprecated, and we seem to have a standard framework in place for informing users that functions are deprecated, but there is no documentation of this in the developers' guide.

It seems like the proper way to deprecate a function is like this: if we start with

```
def f(x):
  body of function
  return something
```

then one should change it like so to deprecate it:

```
def f(x)
  from sage.misc.misc import deprecation
  deprecation("f() is deprecated and will be removed in a future version of Sage. Use g() instead.")
  body of function
  return something 
```

One should also change doctests appropriately; if one had

```
sage: f(1)
'foo'
```

then it should get changed to

```
sage: f(1)
doctest:...: DeprecationWarning: f() is deprecated and will be removed in a future version of Sage. Use g() instead.
'foo'
```

Also, the documentation should be changed to reflect this! It's a good idea to describe what users should do instead of using the deprecated function, so that it is easy for them to change their code.

Ideally we would also have a policy about how long deprecated functions stay in Sage before being removed, but AFAIK no strong consensus on a time period or specific policy exists. If there is one, it should be put into the developer's guide!

In any case, it is probably a good idea to specify the date or Sage version in which a function was deprecated (even if it's just "March 2010") to give users an idea of how "stale" a function is and how close to removal it is. 


---

Comment by ddrake created at 2010-03-16 08:28:15

On sage-devel, Florent Hivert recommends looking at tickets #7515, #7559, and #8073 for information related to this ticket.


---

Comment by ddrake created at 2010-03-16 08:34:54

BTW, the thread on sage-devel is http://groups.google.com/group/sage-devel/browse_thread/thread/b809aff6e97085b9


---

Comment by kcrisman created at 2012-06-14 14:40:42

Changing status from new to needs_review.


---

Comment by kcrisman created at 2012-06-14 14:40:42

This is superseded by #13109.


---

Comment by kcrisman created at 2012-06-14 14:41:12

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-06-28 08:34:42

Resolution: duplicate

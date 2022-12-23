# Issue 8707: view(x) calls x._latex_() 5 times!

Issue created by migration from https://trac.sagemath.org/ticket/8707

Original creator: nthiery

Original creation time: 2010-04-17 21:52:29

Assignee: AlexGhitza

CC:  sage-combinat

Keywords: latex

latex(x) calls x._latex_() twice, and view(x) 5 times!!!

For small objects, that's fine, but when x is a graph, and latex'ing it requires calling graphviz, dot2tex, ... it is not reasonable!


```
sage: class blah():
....:     def _latex_(x):
....:         print "coucou"
....:         return "x"
....: 
sage: latex(blah())
coucou
coucou
x
sage: view(blah())
coucou
coucou
coucou
coucou
coucou
```


Analysis:
 - latex makes use of has_latex_expr which makes a call to _latex_ but discards the result

 - latex_file does not reuse its calls to latex(x)


---

Attachment


---

Comment by nthiery created at 2010-04-17 22:12:22

Changing component from algebra to misc.


---

Comment by nthiery created at 2010-04-17 22:12:22

Now, e.g.

```
sage: g = sage.categories.category.category_graph()
sage: g.set_latex_options(format = "dot2tex")
sage: view(g, viewer="pdf", tightpage = True)
```

takes 6 seconds instead of .5 minutes, which makes it finally usable!


---

Comment by nthiery created at 2010-04-17 22:12:22

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-04-17 23:24:04

Changing status from needs_review to positive_review.


---

Comment by novoselt created at 2010-04-17 23:24:04

Looks good, passes all doctests!


---

Comment by jhpalmieri created at 2010-04-18 02:52:11

Do we know for sure that types are the only sorts of objects which have this problem (that is, which seem to inherit a `_latex_` method according to hasattr, but which actually don't when you try to call it)?


---

Comment by novoselt created at 2010-04-18 03:44:47

I thought about it, but it seems to me that such objects should be "special" rather than "usual". Then it makes sense to check if x is in one of the special classes and hope that everything is good otherwise, i.e. return True. If it will turn out that there are other special cases, we can add tests for them and document them!


---

Comment by jhpalmieri created at 2010-04-19 05:18:02

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-19 05:18:02

Merged into 4.4.alpha1.

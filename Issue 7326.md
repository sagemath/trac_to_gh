# Issue 7326: html.table should run jsmath on the resulting table

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-10-27 22:02:22

Assignee: cwitty

CC:  whuss rbeezer kcrisman

It would be *really* nice if you could include latex code in a table, like this:


```
var('t')
density=t^2
html.table([
["Density $\delta(x,y)$", density]
])
```


and have it do the jsmath magic on the $\delta(x,y)$ part.


---

Comment by jason created at 2009-10-27 22:03:08

Changing type from defect to enhancement.


---

Comment by whuss created at 2009-10-28 08:13:22

As a workaround this already works:


```
var('t')
density=t^2
html.table([
['Density <span class="math">\delta(x,y)</span>', density]
])
```


I am not sure why jsmath does not pick up the $$s in this case.


---

Attachment


---

Comment by jason created at 2009-10-28 08:44:55

This is a very easy patch to review.


---

Comment by jason created at 2009-10-28 08:44:55

Changing status from new to needs_review.


---

Comment by jason created at 2009-10-28 08:58:43

Replying to [comment:2 whuss]:
> As a workaround this already works:
> 
> {{{
> var('t')
> density=t^2
> html.table([
> ['Density <span class="math">\delta(x,y)</span>', density]
> ])
> }}}


so does html.table([This is the Trac macro *sage.misc.html.math_parse* that was inherited from the migration called with arguments ('hi $x^2$'))](https://trac.sagemath.org/wiki/WikiMacros#sage.misc.html.math_parse-macro))

Maybe what is going on is jsmath seems to be not set up to try to find dollar signs, but to only pay attention to class="math" spans and divs.


---

Comment by whuss created at 2009-10-28 12:52:58

Replying to [comment:3 jason]:
> This is a very easy patch to review.

It works, and passes the tests. Positiv review.


---

Comment by whuss created at 2009-10-28 12:52:58

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-31 15:57:29

Resolution: fixed

# Issue 4983: replace subdivisions attribute for matrices with a function

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-01-16 00:30:50

Assignee: was

I do not like this:


```
sage: sage: a = matrix(ZZ,4,[1, 0, 0, 0, 0, 1, 0, 0, 1, -1, 1, 0, 1, -1, 1, 2])
sage: sage: b=a.jordan_form()
sage: b.subdivisions
([0, 1, 3, 4], [0, 1, 3, 4])
sage: b.subdivisions = 10
sage: b.subdivisions
10
```


Notice that you can make the subdivisions nonsense because it can be changed.
Also, of course,

```
sage: b.subdivisions?
...     The Integer class represents arbitrary precision
        integers.  It derives from the Element class, so
[other useless stuff]
```



I don't like that at all either.  I wish that subdivisions were a method with a proper docstring, doctests, etc., and that variable were hidden.


Then one would do:

```
   sage: b.subdivisions?
   useful stuff (and also it would be in the reference manual)
and
   sage: b.subdivisions()
   ([0, 1, 3, 4], [0, 1, 3, 4])
```



---

Comment by robertwb created at 2009-01-16 00:38:15

The method is 


```
sage: b.get_subdivisions()
([1, 3], [1, 3])
```


but this should probably be changed to have an attribute _subdivisions and a method subdivisions() for consistency.


---

Comment by AlexGhitza created at 2009-01-23 02:45:16

Changing type from defect to enhancement.


---

Comment by jhpalmieri created at 2011-03-21 20:16:58

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2011-03-21 20:16:58

Here's patch.  This keeps `get_subdivisions` as a synonym for `subdivisions`.


---

Comment by jhpalmieri created at 2011-03-21 20:16:58

Changing priority from major to minor.


---

Comment by rbeezer created at 2011-03-22 17:21:28

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2011-03-22 17:21:28

This looks real good.  Passes long tests.  I'm glad to see a "get_" go away.

This means I should mildly change #10974, so I'll go make the changes necessary there and have it depend on this.


---

Comment by jason created at 2011-03-22 22:30:02

This probably conflicts with #10847 too.


---

Comment by jason created at 2011-03-22 22:31:04

(where "conflicts" means that #10847 probably needs to be changed after this patch too.)


---

Comment by kcrisman created at 2011-03-22 23:54:03

It would be nice if a patch that has had positive review for over a week did not have to be rebased for a patch that has had positive review for seven hours.  Could this patch not be based on that instead?


---

Comment by jhpalmieri created at 2011-03-23 00:20:52

kcrisman: I just posted a fix for #10847.  (The issue was, the patches at #10847 used the attribute `matrix.subdivisions` instead of using the method `matrix.get_subdivisions()`.)


---

Comment by kcrisman created at 2011-03-23 11:42:12

Replying to [comment:8 jhpalmieri]:
> kcrisman: I just posted a fix for #10847.  (The issue was, the patches at #10847 used the attribute `matrix.subdivisions` instead of using the method `matrix.get_subdivisions()`.)
Thanks, I appreciate it.  I was aware of the incompatibility, just didn't have time to take care of it myself the next few days.


---

Attachment


---

Comment by jhpalmieri created at 2011-03-23 17:52:49

I just uploaded a new patch; the only difference is I added the comment

```
    # 'get_subdivisions' is kept for backwards compatibility: see #4983. 
```

right before `get_subdivisions = subdivisions`.


---

Comment by jdemeyer created at 2011-04-04 09:40:27

This patch conflicts with #10974.


---

Comment by jdemeyer created at 2011-04-04 09:40:27

Changing status from positive_review to needs_work.


---

Comment by jhpalmieri created at 2011-04-04 19:23:15

Here's a patch rebased against #10974.  Does this need review or not?


---

Comment by jhpalmieri created at 2011-04-04 19:23:15

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by kcrisman created at 2011-04-04 19:47:17

If it's literally a fairly trivial rebase and nothing changed in terms of testing, I think it would be okay to just post a diff of what had to be rebased (since the patch is fairly large) and set back to positive review.  If there are some actual nontrivial changes in the code then I guess someone would have to review it.


---

Comment by rbeezer created at 2011-04-04 19:49:50

Replying to [comment:12 jhpalmieri]:
> Here's a patch rebased against #10974.  

Thanks, John.

> Does this need review or not?

Normally, I'd say "not."  But I have two or three  other rebase tasks for later this afternoon, so I can give it a quick test then.

Rob


---

Comment by jhpalmieri created at 2011-04-04 19:56:03

I just rebased it, I didn't change anything else, but if Rob has time to run tests on it, that would be great.  (I've already done this, but it's good to double-check it.)


---

Comment by jdemeyer created at 2011-04-04 20:16:44

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-04-04 20:16:44

Replying to [comment:14 kcrisman]:
> I think it would be okay to [...] set back to positive review.
Done.


---

Comment by rbeezer created at 2011-04-04 23:37:27

Replying to [comment:16 jhpalmieri]:
>  (I've already done this, but it's good to double-check it.)

Double-check shows everything is fine on 4.7.alpha3: applies, builds, passes long tests.

Thanks again, John, for sparing me the work on #10974.  As a bonus I upgraded the depends/apply block to Jeroen's new formatting.  ;-)


---

Comment by jdemeyer created at 2011-04-05 11:59:51

Resolution: fixed

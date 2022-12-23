# Issue 9109: Fast cython class for maps between finite sets.

Issue created by migration from https://trac.sagemath.org/ticket/9109

Original creator: hivert

Original creation time: 2010-06-01 17:08:23

Assignee: sage-combinat

Keywords: finite sets map

A class for dealing with maps between finite sets.

The patch is in preparation os sage-combinat-queue


---

Comment by hivert created at 2010-06-15 10:26:31

Changing status from new to needs_review.


---

Comment by hivert created at 2010-10-24 09:48:07

I just uploaded a new version after some changes in #8702


---

Comment by hivert created at 2010-10-24 09:48:07

Changing assignee from sage-combinat to hivert.


---

Attachment


---

Comment by hivert created at 2011-04-02 17:54:41

This should now be ready for review


---

Comment by hivert created at 2011-04-02 21:54:40

They are still a few glitches remaining. Setting status back to need work


---

Comment by hivert created at 2011-04-02 21:54:40

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2011-04-03 15:26:04

The submitted patch should fix all remaining problem. Please review.


---

Comment by hivert created at 2011-04-03 15:26:04

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2011-04-05 11:35:51

We discussed the design quite some with Florent, and used the code intensively over the last month. It's a useful addition! Thanks!

Florent: please check the small reviewer patch on the Sage-Combinat queue. If the changes are ok with you, you can fold/upload and set a positive review on my behalf.


---

Comment by hivert created at 2011-04-05 19:13:25

> Florent: please check the small reviewer patch on the Sage-Combinat
> queue. If the changes are ok with you, you can fold/upload and set a
> positive review on my behalf.

Hi Nicolas ! Thanks a lot for the numerous English corrections. The doc is
much better now ! I'm perfectly ok with all your changes, except for the
following wrong ReST markup:


```
diff --git a/sage/sets/finite_set_map_cy.pyx b/sage/sets/finite_set_map_cy.pyx
--- a/sage/sets/finite_set_map_cy.pyx
+++ b/sage/sets/finite_set_map_cy.pyx
@@ -86,7 +86,7 @@ cpdef fibers(f, domain):
         {1: {1}}
 
     .. seealso:: :func:`fibers_args` if one needs to pass extra
-    arguments to ``f``.
+       arguments to ``f``.
     """
     result = {}
     for x in domain:
```


I folded your patch and added this small change. It is a rather trivial change
but, in order to follow the rules, someone has to look at it. So it's now your
job to set the positive review :-)


---

Attachment


---

Comment by nthiery created at 2011-04-05 21:38:53

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-04-13 07:42:50

Resolution: fixed

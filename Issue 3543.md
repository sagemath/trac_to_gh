# Issue 3543: Unify jquery libraries in devel/sage and data/extcode

Issue created by migration from https://trac.sagemath.org/ticket/3543

Original creator: mabshoff

Original creation time: 2008-07-03 04:29:24

Assignee: was

CC:  jason timdumol

We currently ship two copies of the jquery javascript library:

 * jQuery 1.2.6 - New Wave Javascript - $Rev: 5685 $ in devel/sage-main/sage/dsage/web/static/jquery.js
 * jQuery 1.2.3 - New Wave Javascript - $Rev: 4663 $ in data/extcode/notebook/javascript/jquery/jquery.js

But we should on ship one copy.

Cheers,

Michael


---

Comment by jason created at 2008-10-10 23:34:47

Changing assignee from was to jason.


---

Comment by jason created at 2008-10-10 23:34:47

Changing status from new to assigned.


---

Comment by jason created at 2008-12-05 10:55:59

Changing status from assigned to new.


---

Comment by jason created at 2008-12-05 10:55:59

Remove assignee jason.


---

Comment by jason created at 2008-12-05 10:56:35

I'm not sure what is going on with dsage; someone familiar with dsage will have to look at that.


---

Comment by jason created at 2009-01-22 18:01:35

Changing type from defect to enhancement.


---

Comment by jason created at 2009-01-22 18:01:35

All that is needed is that dsage needs to change its /static directory to point to local/notebook/javascript/<appropriate directory>.  I'm making this minor since:

  1. the small space wasted with duplicated code is not worth the risk of breaking dsage, especially since
  2. it seems that the future of dsage is uncertain.

Things work now.


---

Comment by jason created at 2009-01-22 18:01:35

Changing priority from major to minor.


---

Comment by jason created at 2010-05-11 05:12:44

Tim,

Can you comment on this ticket?  You probably know more about this than anyone at this point.


---

Comment by timdumol created at 2010-05-11 05:33:52

dsage is gone, so that doesn't matter. The files in `data/extcode/...` are used by the old notebook (in sage.server.notebook). Since the old notebook isn't used anymore except in migration to the new one, the files should be safe to delete.


---

Comment by jdemeyer created at 2015-04-22 09:42:10

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-04-22 09:42:10

The Sage library doesn't ship `jquery`. Various packages do, in particular `sagenb`, `Sphinx`, `matplotlib`, `ppl`, `jsmol`, `IPython` and `WerkZeug`. I don't think it's feasible to unify them, so close this ticket as "wontfix".


---

Comment by jdemeyer created at 2015-04-22 09:42:14

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-04-23 01:43:16

Resolution: wontfix

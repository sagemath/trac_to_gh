# Issue 8759: Make the Sass css_dir be /data instead of /data/sage/css so that other components can use Sass

Issue created by migration from https://trac.sagemath.org/ticket/8759

Original creator: acleone

Original creation time: 2010-04-24 23:19:58

Assignee: acleone

CC:  acleone was timdumol

Sass is the templating engine Sage uses for it's CSS.


---

Comment by acleone created at 2010-04-24 23:22:30

Changes the Sass css_dir to /data instead of /data/sage/css and moves the files accordingly in src.


---

Comment by acleone created at 2010-04-24 23:22:43

Changing status from new to needs_review.


---

Attachment


---

Attachment

Replaces earlier patch.  Now in git-format so that files are just renamed instead of removed/added


---

Comment by timdumol created at 2010-07-05 10:08:45

I don't think any of the other components under /data are developed by us (except sage3d, which uses no CSS), so I'm not sure how useful this is.


---

Comment by timdumol created at 2010-07-05 10:08:45

Changing status from needs_review to needs_info.


---

Comment by kcrisman created at 2014-12-11 15:26:09

Agreed.  If there is truly a need for this, should be opened on https://github.com/sagemath/sagenb/ and clarified.


---

Comment by kcrisman created at 2014-12-11 15:26:09

Changing status from needs_info to positive_review.


---

Comment by vbraun created at 2014-12-11 18:36:35

Resolution: invalid

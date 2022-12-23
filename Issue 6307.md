# Issue 6307: Move javascript out of python-land

Issue created by migration from https://trac.sagemath.org/ticket/6307

Original creator: boothby

Original creation time: 2009-06-16 05:42:28

Assignee: tbd

As Mike Hansen noted in #5564, the javascript shouldn't be in a python file in triple-quoted strings.  Unfortunately, the patch he submitted to do this bitrotted. 


---

Comment by boothby created at 2009-06-16 05:47:03

Changing component from algebra to notebook.


---

Comment by boothby created at 2009-06-16 05:47:03

Changing assignee from tbd to boothby.


---

Comment by ddrake created at 2009-06-18 00:09:02

In #5564, mhansen mentioned that this patch breaks history; if anyone really cares about preserving history, it's easy enough with `hg cp`. I made a version of this patch which does exactly the same thing with respect to file contents, but also tells Mercurial about the history: http://sage.math.washington.edu/home/drake/6307bis.patch

(It's rather bigger than the patch on this ticket because it's diffing the new .js files against js.py, instead of /dev/null.)


---

Attachment

Very nice, I didn't know that functionality existed.


---

Comment by boothby created at 2009-06-20 18:42:25

doctest failure in psage.py


---

Comment by boothby created at 2009-07-09 19:18:56

I can't reproduce the error in psage.py... I'm re-marking this as a positive review.


---

Comment by mvngu created at 2009-07-16 11:25:36

reviewer patch; fixes typos


---

Attachment


---

Comment by mvngu created at 2009-07-16 11:53:12

Once this ticket is closed, ticket #5564 should also be closed as a consequence of the patches on this ticket. Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(


---

Comment by mvngu created at 2009-07-16 21:22:24

Resolution: fixed


---

Comment by mvngu created at 2009-07-22 17:16:30

This ticket results in a corrupt repository. After merging this ticket in Sage 4.1.1.alpha0, I created a source distribution with `sage -sdist 4.1.1.alpha0`. Now compile that source distribution, then cd to `SAGE_ROOT/devel/sage-main` and do:

```
[mvngu@sage sage-main]$ hg st
! sage/server/notebook/templates/async_lib.js
! sage/server/notebook/templates/jmol_lib.js
! sage/server/notebook/templates/notebook_lib.js
```

I'm marking this ticket as "needs work" and reverting it in my merge tree.


---

Comment by mvngu created at 2009-07-22 17:16:39

Changing status from closed to reopened.


---

Comment by mvngu created at 2009-07-22 17:16:39

Resolution changed from fixed to 


---

Comment by rlm created at 2009-07-22 17:24:33

Working on a fix for this right now...


---

Comment by rlm created at 2009-07-22 17:41:38

Rather, I have a fix, but the sdist command is taking a long time. Once that is done I can confirm that it worked.


---

Attachment

It works!


```
[rlm-book templates]$ pwd
/Users/rlmill/sage-4.1.1.alpha0.6307/dist/sage-4.1.1.alpha0.fix.test/spkg/standard/sage-4.1.1.alpha0.fix.test/sage/server/notebook/templates
[rlm-book templates]$ ls
total 208K
-rw-r--r-- 1 rlmill  786 2009-07-22 10:23 account_recovery.html
-rw-r--r-- 1 rlmill 1.5K 2009-07-22 10:23 account_settings.html
-rw-r--r-- 1 rlmill  729 2009-07-22 10:23 async_lib.js
-rw-r--r-- 1 rlmill  448 2009-07-22 10:23 banner.html
-rw-r--r-- 1 rlmill  467 2009-07-22 10:23 base.html
-rw-r--r-- 1 rlmill  440 2009-07-22 10:23 base_authenticated.html
-rw-r--r-- 1 rlmill 2.8K 2009-07-22 10:23 docs.html
-rw-r--r-- 1 rlmill  324 2009-07-22 10:23 error_message.html
-rw-r--r-- 1 rlmill  534 2009-07-22 10:23 history.html
-rw-r--r-- 1 rlmill 1.2K 2009-07-22 10:23 jmol_lib.js
-rw-r--r-- 1 rlmill  385 2009-07-22 10:23 list_top.html
-rw-r--r-- 1 rlmill 2.8K 2009-07-22 10:23 login.html
-rw-r--r-- 1 rlmill 117K 2009-07-22 10:23 notebook_lib.js
-rw-r--r-- 1 rlmill 2.3K 2009-07-22 10:23 registration.html
-rw-r--r-- 1 rlmill  284 2009-07-22 10:23 search.html
-rw-r--r-- 1 rlmill  780 2009-07-22 10:23 source_code.html
-rw-r--r-- 1 rlmill  220 2009-07-22 10:23 template_error.html
-rw-r--r-- 1 rlmill 1.3K 2009-07-22 10:23 top_bar.html
-rw-r--r-- 1 rlmill 1.2K 2009-07-22 10:23 upload.html
-rw-r--r-- 1 rlmill  324 2009-07-22 10:23 user_management.html
-rw-r--r-- 1 rlmill 6.7K 2009-07-22 10:23 worksheet_listing.html
-rw-r--r-- 1 rlmill  280 2009-07-22 10:23 yes_no.html
```



---

Comment by jhpalmieri created at 2009-07-22 18:52:35

The new patch should fix the repository issues.


---

Comment by mvngu created at 2009-07-23 09:16:17

Resolution: fixed

# Issue 7447: SageNB version and install date / time

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-11-12 20:19:39

Assignee: boothby

CC:  was timdumol

On occasion, it's useful to get the installed SageNB version from inside a Sage process.  Here's a possible API:

```python
sage: import sagenb.version
sage: sagenb.version.version
0.4.3
sage: sagenb.version.date
'2009-11-12 11:56:53'
```

This is similar to `sage.version`, except this `date` also has the install / package build time.  This could be useful to developers.

Reminder: If this merges, update #7390's test report generator, which has a notebook version field.


---

Attachment

Add version and date to new sagenb source distributions.


---

Comment by mpatel created at 2009-11-13 21:36:09

Changing status from new to needs_review.


---

Comment by mpatel created at 2009-11-13 21:53:54

Can `distutils` or `setuptools` can do this more simply?


---

Comment by mpatel created at 2009-11-15 08:20:42

See #7467 for a `setuptools` alternative.


---

Comment by mpatel created at 2009-11-24 08:19:20

Changing status from needs_review to needs_info.


---

Comment by mpatel created at 2009-12-06 00:16:15

Cleaner `setuptools` version.  Depends on #7467.  This patch only.  sagenb repo.


---

Comment by mpatel created at 2009-12-06 00:21:49

Changing status from needs_info to needs_review.


---

Attachment

V2 follows (and depends on) the simpler, `setuptools`-based approach of #7467.  The [attachment:trac_7447-sagenb_version_v2.patch new patch] also adds the Sage Notebook version to HTML test reports.

For what it's worth, the local queue is

```
trac_7390-sagenb_test_report_A.patch
trac_7390-sagenb_test_report_B_v2.patch
trac_7390-sagenb_test_report_referee.patch
trac_7402-pkg_resources.patch
trac_7428-publish_last_edited_v2.patch
trac_7444-search_after_publish.patch
trac_7376-search_by_username_v2.patch
trac_1321-sagenb_graphed.patch
sagenb_7483.patch
sagenb_7482.patch
sagenb-7495.patch
sagenb_3849.patch
trac_7467-setuptools.2.patch
trac_7447-sagenb_version_v2.patch
trac_4714-sagenb_jsmath_init.patch
trac_6855-published_interacts.patch
```

But please let me know if I should rebase any patch(es).


---

Attachment


---

Comment by was created at 2009-12-09 00:11:52

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-09 00:11:52

Nice.  I had to rebase it, but that's fine.


---

Comment by was created at 2009-12-09 01:11:51

Resolution: fixed


---

Comment by was created at 2009-12-09 01:11:51

I merged this patch into sagenb-0.4.6.

# Issue 7937: Add SASS files to MANIFEST.in

Issue created by migration from https://trac.sagemath.org/ticket/7937

Original creator: mpatel

Original creation time: 2010-01-15 18:49:44

Assignee: was

CC:  timdumol was

The SASS source files from ticket #7269 are missing from [sagenb-0.5.spkg](http://boxen.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.5.spkg):

```sh
hg stat
! sass/config.rb
! sass/readme.txt
! sass/src/account_settings.sass
! sass/src/main.sass
! sass/src/master.sass
! sass/src/partials/_mixins.sass
! sass/src/registration.sass
! sass/src/test_report.sass
! sass/src/typography/_base.sass
! sass/src/user_management.sass
? release_notes.txt
? setup.cfg
```

I think we just need to patch the `MANIFEST.in`.


---

Comment by mpatel created at 2010-01-15 19:18:54

Updates `MANIFEST.in` for #7269.  Does _not_ include the missing files.  sagenb repo.


---

Attachment


---

Comment by mpatel created at 2010-01-15 19:20:11

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-01-17 09:09:19

LGTM. Nice catch.


---

Comment by timdumol created at 2010-01-17 09:09:19

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-17 09:09:19

Changing priority from minor to critical.


---

Comment by rlm created at 2010-01-19 05:04:16

Resolution: fixed

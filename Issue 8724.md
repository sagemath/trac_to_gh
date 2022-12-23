# Issue 8724: Notebook redirects use wrong HTTP Status Code (301 Moved Permanently)

Issue created by migration from https://trac.sagemath.org/ticket/8724

Original creator: timdumol

Original creation time: 2010-04-20 12:10:30

Assignee: jason, was

CC:  mpatel

Notebook redirects use status code 301 to redirect to new pages, when they should use code 303 See Other. Because of this, Google Chrome caches the redirect, leading to problems with creating new worksheets, emptying trash, etc. If the redirect is cached, the requested action will not be performed, as the browser will redirect directly to the original url.

For example, if you are to click the "New Worksheet" link twice, you would expect to create two new worksheets. However, the second click redirects you directly to the first created worksheet.

Thanks to mpatel for spotting this.


---

Attachment

Changes status code of redirects to 303. Also fixes a bunch of Selenium tests. Apply to sagenb repo.


---

Comment by timdumol created at 2010-04-20 12:13:23

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-04-23 04:39:59

(I'm not changing any notebook code in Sage 4.4.)


---

Comment by was created at 2010-04-24 19:27:08

This looks great!


---

Comment by was created at 2010-04-24 19:27:17

Changing status from needs_review to positive_review.


---

Comment by acleone created at 2010-04-24 19:59:50

Apply after first patch


---

Attachment


---

Comment by was created at 2010-04-29 04:56:39

Resolution: fixed

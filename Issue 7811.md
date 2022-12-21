# Issue 7811: Worksheet list CSS: Account for special characters in login names

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-01-01 22:47:15

Assignee: was

CC:  robert.marik timdumol was

We need to account for this difference

```
$ grep compile twist.py template.py
twist.py:re_valid_username = re.compile('[a-z|A-Z|0-9|_|.|`@`]*')
template.py:css_illegal_re = re.compile(r'[^-A-Za-z_0-9]')
```

when processing the checkboxes in a worksheet listing.  Otherwise, the Archive, Stop, and Delete buttons will not work for users whose login names contain dots (`.`) or [at signs](http://en.wikipedia.org/wiki/At_sign) (``@``).

This is a follow-up to #7332.  See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/9da7dd211fe5570b) for the bug report.


---

Comment by mpatel created at 2010-01-01 23:03:03

Escape /, `@`, and . in worksheet list CSS IDs.  sagenb repo.


---

Comment by mpatel created at 2010-01-01 23:05:52

Changing status from new to needs_review.


---

Attachment

Please let me know if I've missed any other characters.


---

Comment by timdumol created at 2010-01-02 07:12:05

Why not use /[^-A-Za-z_0-9]/g ? If the regexp for usernames is updated for all valid emails, then '+' will be allowed for usernames, which is illegal as a CSS id.


---

Comment by mpatel created at 2010-01-02 08:42:32

Excellent point.  I'll update the patch.


---

Attachment

More general RegExp.  Replaces previous.


---

Comment by robert.marik created at 2010-01-02 09:59:51

Works for me. Is it neceassary to run ./sage -t even when upgrading spkg package?


---

Comment by mpatel created at 2010-01-02 10:07:12

If you mean `sage -b` --- it's necessary only for changes to the main Sage library, under `SAGE_ROOT/devel/sage`, but not if you're just installing a spkg.


---

Comment by timdumol created at 2010-01-02 10:08:58

Ideally this should be tested with `sage -t -sagenb` when #7650 comes in, or with a Selenium test (sagenb.testing), specifically in `sagenb.testing.tests.test_accounts`.


---

Comment by robert.marik created at 2010-01-02 11:37:38

Replying to [comment:5 mpatel]:
> If you mean `sage -b` --- it's necessary only for changes to the main Sage library, under `SAGE_ROOT/devel/sage`, but not if you're just installing a spkg.

No, I meant actually sage -t. I wondered, if I can give positive review without doctesting.


---

Comment by robert.marik created at 2010-01-03 13:47:13

Changing status from needs_review to positive_review.


---

Comment by robert.marik created at 2010-01-03 13:47:13

Wors fine. Tests passed. Doctests are not meaningful for this patch. Positive review.


---

Comment by was created at 2010-01-04 06:57:53

Resolution: fixed


---

Comment by was created at 2010-01-04 06:57:53

merged into sagenb-0.4.8

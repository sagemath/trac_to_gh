# Issue 7833: r-2.9.2 - fix compilation on FreeBSD

Issue created by migration from Trac.

Original creator: pjeremy

Original creation time: 2010-01-03 10:39:43

Assignee: pjeremy

CC:  jason was

Pass CFLAGS, CPPFLAGS and LDFLAGS from the environment into the build process.  This also corrects a typo in CPPFLAGS.

Note that FreeBSD needs the path to libiconv to be explicitly specified.  In theory, --with-libiconv-prefix should work but configure script is broken and ignores that path when looking for libiconv.  Hard-wire /usr/local/include and /usr/local/lib via xxFLAGS.  Without this change, you get:

```
checking iconv.h usability... no
checking iconv.h presence... no
checking for iconv.h... no
checking for iconv... no
checking for iconvlist... no
configure: error: --with-iconv=yes (default) and a suitable iconv is not available
Error configuring R.
```




---

Attachment


---

Comment by pjeremy created at 2010-01-03 10:40:43

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-01-04 15:05:55

Is #6532 relevant here?  Is it possible to update this patch for that spkg - it looks like it should be fairly trivial.  You could review that one first if that makes it easier; unfortunately, I don't have access to a FreeBSD machine to return the favor :(


---

Comment by drkirkby created at 2010-01-13 22:59:33

I don't have a FreeBSD machine, but this patch looks fine to me. The previous spkg-install was clearly written incorrectly. The issues at #6532 are something quite separate. So a positive review from me. 

Dave


---

Comment by drkirkby created at 2010-01-13 22:59:33

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-01-13 23:00:22

PS, 
Don't forget to report this upstream!


---

Comment by kcrisman created at 2010-01-15 19:36:52

This needs a link to an spkg to be reviewed.  However, I have incorporated it in the spkg at #6532, so hopefully that will be sufficient!


---

Comment by kcrisman created at 2010-01-25 19:19:05

Can someone check that #6532 would resolve this?


---

Comment by mvngu created at 2010-01-25 23:30:46

Resolution: fixed


---

Comment by mvngu created at 2010-01-25 23:30:46

Ticket #6532 incorporates the patch on this ticket, so no need to merge the patch here.

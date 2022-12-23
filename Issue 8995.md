# Issue 8995: @ sign in notebook username prevents TinyMCE from working

Issue created by migration from https://trac.sagemath.org/ticket/8995

Original creator: jason

Original creation time: 2010-05-19 23:35:25

Assignee: jason, was

CC:  dimpase

See the thread by Dennis Watson here:

http://groups.google.com/group/sage-support/browse_frm/thread/2acd499a566efce1

In particular, some tinymce javascript files were trying to download from a URL that included the username, like:

http://sagenb.org/home/usernamewith`@`/javascript/tiny_mce/langs/en.js


---

Comment by ddrake created at 2010-05-20 02:50:42

#8996 is a duplicate of this (just beaten by Jason!). Robert there says:

> If it's not to hard, I have a strong preference for allowing `@` in usernames, as I often use my email address as a username because it's both easy to remember and likely to be unique.

...which I agree with.


---

Comment by kcrisman created at 2011-09-29 13:06:13

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-09-29 13:06:13

dimpase just pointed out that #11343 is a dup of this.  However, there is a lot more discussion there, as well as a patch, so I'm recommending this be the one closed.  I'm copying the description material above there.


---

Comment by kcrisman created at 2011-09-29 13:06:29

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-10-05 08:10:09

Resolution: duplicate

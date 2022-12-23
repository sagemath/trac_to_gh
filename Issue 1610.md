# Issue 1610: hg record / cherry picking -- add something to the programming guide

Issue created by migration from https://trac.sagemath.org/ticket/1610

Original creator: was

Original creation time: 2007-12-27 09:05:13

Assignee: tba

This tick will be *very* easy for somebody to close. 


```
> I noticed that Mercurial 0.9.5 has a "record" extension that mimics the
> darcs record functionality of interactively asking what changes you want
> to commit out of a file.  I know there was discussion of this a while ago.
>
> Reference:
>
> http://www.selenic.com/pipermail/mercurial/2007-October/015150.html
> under the New extensions heading.  See also
> http://www.selenic.com/mercurial/wiki/index.cgi/RecordExtension
>
> Anyways, I'm just posting this as an FYI.  It might be nice to expose
> this functionality to sage, if we haven't already.
>

Cool!

And, this is already in Sage.   Just put

[extensions]
record=

in your .hgrc file, and do

   hg record

and you'll get to cherry pick.

This should be documented in the programming guide.
```



---

Comment by was created at 2007-12-27 09:05:21

Changing priority from major to minor.


---

Comment by mvngu created at 2010-02-09 03:17:22

Ticket #8206 adds some pointers about "hg record". Maybe we could expand on that with the information here.


---

Comment by rbeezer created at 2010-02-09 04:51:20

Changing status from new to needs_review.


---

Attachment

Apply #8206 before applying the "cherry picking" patch.


---

Comment by mvngu created at 2010-02-14 15:28:52

Looks good to me. The idea here is to provide pointers to *record as an advanced tool for patch management.


---

Comment by mvngu created at 2010-02-14 15:28:52

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-15 03:45:07

Resolution: fixed

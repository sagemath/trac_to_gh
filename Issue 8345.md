# Issue 8345: cannot convert symbolic functions back from maxima

Issue created by migration from https://trac.sagemath.org/ticket/8345

Original creator: burcin

Original creation time: 2010-02-24 11:36:28

Assignee: was

CC:  kcrisman

From sage-devel:


```
On Mon, 22 Feb 2010 07:02:21 -0800 (PST)
Håkan Granath <hakan.granath@googlemail.com> wrote:

> Typesetting conjugates of variables (that has been passed to
> Maxima and back?) is strange. In e.g. Sage 4.2 this did not
> happen.
> 
> ----------------------------------------------------------------------
> | Sage Version 4.3.3, Release Date: 2010-02-21                       |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> sage: assume(x,'complex')
> sage: latex(x.conjugate())
> \overline{x}
> sage: latex(x.conjugate().factor())
> {\rm conjugate}\left(x\right)
```


Somehow we don't recognize the conjugate function in the string we get back from maxima, and create a new one. The last line above is the default latex typesetting for symbolic functions.


The thread is here:

http://groups.google.com/group/sage-devel/t/cd43a14bee6e9be


---

Comment by burcin created at 2011-06-01 14:12:15

This seems to be fixed in the meanwhile. attachment:trac_8345-doctest.patch adds a doctest.


---

Comment by burcin created at 2011-06-01 14:12:15

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-06-08 19:58:17

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2011-06-08 19:58:17

This patch does not apply to 4.7.1.alpha1 because of a blank line someone must have removed earlier.  Unfortunately, I can't figure out how to fix the patch easily (so that Burcin remains the author of the patch), so it will have to be rebased.  Hopefully that won't be too much trouble :(

This also exposes a different problem - that our variables are assumed to be real.  This is known elsewhere.

```
sage: latex(x.conjugate())
\overline{x}
sage: latex(x.conjugate().simplify())
x
```


Not sure if that needs to be addressed on this ticket, though.


---

Comment by burcin created at 2011-06-09 11:17:47

Changing status from needs_work to needs_review.


---

Attachment

Replying to [comment:3 kcrisman]:
> This patch does not apply to 4.7.1.alpha1 because of a blank line someone must have removed earlier.  Unfortunately, I can't figure out how to fix the patch easily (so that Burcin remains the author of the patch), so it will have to be rebased.  Hopefully that won't be too much trouble :(

I uploaded a rebased patch with the same name.

If you `qimport` a patch which already has mercurial headers, make changes, then `qrefresh` and `export`, the author shouldn't change. In this case, it wouldn't matter even if you changed it. :)

> This also exposes a different problem - that our variables are assumed to be real.  This is known elsewhere.
> {{{
> sage: latex(x.conjugate())
> \overline{x}
> sage: latex(x.conjugate().simplify())
> x
> }}}
> 
> Not sure if that needs to be addressed on this ticket, though.

That is #6882, well beyond the scope of this ticket.


---

Comment by kcrisman created at 2011-06-09 13:28:20

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-06-09 13:28:20

Okay, thanks - and thanks for the tip, in the last few months I've finally started using queues.

I already tried several things yesterday, so all is well.  Positive review.

Incidentally, this has been fixed for a _while_:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: hackbranch
sage: assume(x,'complex')
sage: latex(x.conjugate().simplify())
\overline{x}
sage: 
```

| Sage Version 4.4.4, Release Date: 2010-06-23                       |
| Type notebook() for the GUI, and license() for information.        |
----
Apply [attachment:trac_8345-doctest.patch].


---

Comment by jdemeyer created at 2011-06-15 20:12:38

Resolution: fixed

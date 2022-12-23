# Issue 8297: extra parenthesis when typesetting QQ arguments to symbolic functions

Issue created by migration from https://trac.sagemath.org/ticket/8297

Original creator: burcin

Original creation time: 2010-02-18 09:30:19

Assignee: burcin

Keywords: pynac

From sage-devel:


```
On Wed, 17 Feb 2010 23:16:13 -0800 (PST)
Håkan Granath <hakan.granath@googlemail.com> wrote:

> A minor inconvenience is the extra set of parentheses that appear
> when typesetting QQ elements as arguments of functions, e.g.
> 
> ----------------------------------------------------------------------
> | Sage Version 4.3.2, Release Date: 2010-02-06                       |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> sage: latex(gamma(1/4))
> \Gamma\left(\left(\frac{1}{4}\right)\right)
> 
> 
> Unfortunately I can not create a patch myself to fix this since
> I could not figure out where the problem comes from.
> 
> /Håkan
```


Here is the thread:

http://groups.google.com/group/sage-devel/t/d068d2fd544eadde


---

Attachment


---

Comment by burcin created at 2010-04-02 16:11:58

Changing status from new to needs_review.


---

Comment by burcin created at 2010-04-02 16:11:58

Changing keywords from "pynac" to "".


---

Comment by burcin created at 2010-04-02 16:11:58

The fix for this was much easier than I expected. It didn't require any changes in pynac. :)


---

Comment by hgranath created at 2010-04-11 12:22:32

The patch works, I have checked that it passes all tests, and html and
pdf manual builds. This is my first attempt to review a ticket
however, and I stumbled upon 2 problems:

Is the documentation for these functions actually in the reference
manual? I wanted to check that the newly generated files looked good,
but could not find the place. Maybe I am just blind...

Typing sage.functions.log.Function_log? + TAB in the notebook (Linux
box with Firefox 3.6.3) the TESTS section (where some of the
documentation of the patch appear) is messed up. This also happens for
me without this patch, though.


---

Attachment

apply only this patch


---

Comment by burcin created at 2010-04-11 12:42:31

The docstring was messed up because of the missing `r` before starting the string. attachment:trac_8297-sfunction_extra_paranthesis.take2.patch fixes this.

I don't know why the documentation for these functions don't show up in the reference manual. I suggest opening a new ticket for that.


---

Comment by hgranath created at 2010-04-11 13:26:45

Great, now sage.functions.log.Function_log? + TAB works well.


---

Comment by hgranath created at 2010-04-11 13:26:45

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 23:43:57

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-15 23:43:57

Merged "trac_8297-sfunction_extra_paranthesis.take2.patch" into 4.4.alpha0

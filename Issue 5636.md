# Issue 5636: [with patch; needs review] jsmath is broken in sage-3.4

Issue created by migration from https://trac.sagemath.org/ticket/5636

Original creator: was

Original creation time: 2009-03-29 23:22:53

Assignee: cwitty


```
On Sun, Mar 29, 2009 at 3:39 PM, John H Palmieri wrote:
>
> 1. In sage-3.4, it looks like %jsmath is broken.  Can anyone reproduce
> this?
>
> Since I haven't seen anyone mention this, either I missed it or no one
> uses %jsmath any more.  So is it worth fixing, or should we scrap it
> (and just use tinyMCE, %html, %latex, etc.)?

I just fixed it.  It took me 1 minute (since it was my fault it was broken in the first place -- I broke this in 3.3).
```



---

Attachment


---

Comment by jhpalmieri created at 2009-03-30 00:40:11

Fixes the problem, simple code, all tests pass.  Positive review.


---

Comment by mabshoff created at 2009-03-31 08:41:13

Merged in Sage 3.4.1.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-31 08:41:13

Resolution: fixed

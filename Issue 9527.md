# Issue 9527: improve "sage -sh" prompt so it doesn't confuse everybody

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-07-17 11:55:26

Assignee: jason

CC:  malb

When doing `sage -sh`, the result is very, very confusing, since it has the SAGE_ROOT path displayed unlabeled, which causes confusion, and does not show the current path, which also causes confusion.  This patch adds a label and the current path, to help reduce confusion some.


---

Comment by was created at 2010-07-17 12:04:03

Changing status from new to needs_review.


---

Attachment

fix SAGE_ROOT (a separate bug, I guess)


---

Comment by malb created at 2010-07-17 13:09:59

Changing status from needs_review to positive_review.


---

Comment by malb created at 2010-07-17 13:09:59

The patch looks fine. I'd have preferred to have my PS1 to be embedded in the new PS1, i.e. something like this:


```
this_is_my_prompt$ sage -sh
SAGE_ROOT=/usr/local/sage-4.3
(sage subshell) this_is_my_prompt$


```

But it seems this just doesn't work (I tried). This new one is definitely an improvement thus I'll give it a positive review.


---

Comment by was created at 2010-07-17 13:15:38

Replying to [comment:2 malb]:
> The patch looks fine. I'd have preferred to have my PS1 to be embedded in the new PS1, i.e. something like this:
> 
> {{{
> this_is_my_prompt$ sage -sh
> SAGE_ROOT=/usr/local/sage-4.3
> (sage subshell) this_is_my_prompt$
> 
> 
> }}}
> But it seems this just doesn't work (I tried). 

I tried too, but couldn't figure it out. This patch is meant to be a big improvement, that's all.


---

Comment by ddrake created at 2010-07-22 23:42:14

Resolution: fixed

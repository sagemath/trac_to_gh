# Issue 6210: docs for the property option of graphs() should include a pointer to the docs for the augment parameter

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-06-04 19:48:38

Assignee: tba

A sentence in the docs for the property parameter should say something about possibly missing graphs, due to the reasons explained in the docs for the augment parameter.  See http://groups.google.com/group/sage-devel/browse_thread/thread/e8516faf818a6fb7


---

Attachment

I just got bitten by this..


---

Comment by dsm created at 2011-03-10 05:24:53

Changing status from new to needs_review.


---

Comment by ncohen created at 2011-05-02 13:50:04

Hello !!!

It's true that this part's tricky, but what about just saying after 

```
``property`` -- (default: ``lambda x: True``) any property to be tested on graphs before generation
```


Something like "The property must fill an inheritance property to work as intended. Please refer to the help of parameter ``augment``" ?

Otherwise the explanations are given twice and we're sure users will read them `:-)`

Nathann


---

Comment by ncohen created at 2011-05-02 13:50:04

Changing status from needs_review to needs_info.


---

Comment by kini created at 2011-10-14 04:20:37

We got bitten too, in our undergrad course :) I think I agree with Nathann.


---

Comment by dimpase created at 2011-10-15 06:59:15

Replying to [comment:4 kini]:
> We got bitten too, in our undergrad course :) I think I agree with Nathann.

better more, than less...


---

Comment by dimpase created at 2011-10-15 06:59:15

Changing status from needs_info to needs_review.


---

Comment by dimpase created at 2011-10-15 06:59:32

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-10-17 07:50:51

Resolution: fixed

# Issue 7996: Invisible Text With Dark Theme (White on White Text)

Issue created by migration from https://trac.sagemath.org/ticket/7996

Original creator: acleone

Original creation time: 2010-01-19 08:14:39

Assignee: acleone

Editing cells with a dark theme makes the text invisible (white text on a white background).


---

Comment by acleone created at 2010-01-19 08:18:39

Removes the background-color:white from the css


---

Comment by acleone created at 2010-01-19 08:37:47

Changing status from new to needs_review.


---

Attachment


---

Comment by timdumol created at 2010-01-19 08:55:10

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-19 08:55:10

LGTM.


---

Comment by mpatel created at 2010-01-25 01:01:43

Resolution: fixed


---

Comment by mpatel created at 2010-01-25 02:18:49

With the default color settings in IE8, this makes an active cell's background bluish-grey (lower contrast) but an inactive cell's background is white (higher contrast).  Many users may expect the opposite.  We may get comments.

I'm leaving this closed and will merge it into SageNB 0.7.


---

Comment by acleone created at 2010-01-25 02:43:01

Perhaps a better patch would be to leave the "background-color" white and set the "color" to black.

See trac_7996-invisible_text.v2.patch - (apply it after the first patch).


---

Comment by acleone created at 2010-01-25 02:43:26

Apply after the first patch


---

Comment by acleone created at 2010-01-25 02:43:59

Resolution changed from fixed to 


---

Comment by acleone created at 2010-01-25 02:43:59

Changing status from closed to new.


---

Attachment


---

Comment by acleone created at 2010-01-25 02:44:06

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-25 03:09:13

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-01-25 03:09:13

Great!  Now it just happens in Opera 10 (with with or without V2).

I'll merge the pair.


---

Comment by mpatel created at 2010-01-25 03:40:07

Feel free to post a fix for O10 or simply leave it for the future.  My main motivation here is that I _think_ that significantly more notebook users connect with IE than with O.  But I may be wrong.


---

Comment by mpatel created at 2010-01-25 03:40:07

Resolution: fixed

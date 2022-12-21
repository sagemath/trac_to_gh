# Issue 9000: sage notebook: change default interact color selector

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-05-20 19:37:34

Assignee: jason, was

People voted yes to the following:


```
Would anybody be opposed to me changing the default for 
color_select from 'farbtastic' to 'colorpicker'.  The 
farbtastic color picker is *HUGE*, whereas the 'colorpicker' 
one is much smaller and more usable.
```



---

Comment by was created at 2010-08-11 18:58:15

I ended up changing it to jpicker instead of colorpicker, since after trying it out, frankly colorpicker sucks, whereas jpicker is very nice.


---

Comment by was created at 2010-08-11 18:58:15

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-08-12 06:01:34

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2010-08-12 06:01:34

I think you may have accidentally changed the wrong function (`html_color_selector` instead of `color_selector`).


---

Attachment

new version that fixes the (valid) issue that tim pointed out.


---

Comment by was created at 2010-08-14 02:23:19

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2010-08-14 03:19:07

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-08-14 03:19:07

Looks good to me. Doctests pass. Positive review.


---

Comment by mpatel created at 2010-10-04 01:34:43

Resolution: fixed


---

Comment by kcrisman created at 2014-10-01 15:54:26

Apparently this never quite got changed, or maybe it just was changed back or something.  See [this commit](https://github.com/sagemath/sagenb/commit/ece3ebf2c5a5e4389013988182609501d9332121), which I accidentally put in without review, sigh...

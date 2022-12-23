# Issue 7625: include new version of sagenb (0.4.5)

Issue created by migration from https://trac.sagemath.org/ticket/7625

Original creator: was

Original creation time: 2009-12-08 18:03:08

Assignee: was

It's here:

  http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.5.spkg


---

Comment by was created at 2009-12-08 18:03:26

Changing status from new to needs_review.


---

Comment by was created at 2009-12-08 18:03:47


```
#7495: William Stein and Mitesh Patel: notebook: fix massive security vulnerability and get rid of all possible "internal server errors" when doing "Data --> Upload or attach file [Reviewed by Mitesh Patel]
#3619: William Stein: notebook -- record date & time each user logs in [Reviewed by Tim Dumol]
#3849: William Stein and Mitesh Patel: notebook --get rid of internal server errors when uploading a worksheet [Reviewed by Tim Dumol]
#7402: Tim Dumol: notebook -- Use `pkg_resources` to locate `DATA` directory [Reviwed by Mitesh Patel]
#7428: Mitesh Patel: worksheets listed on published list only after they are republished, but not after initial publication [Reviewed by Tim Dumol]
#7444: Mitesh Patel: Broken: searching published worksheets after publishing a worksheet for the first time [Reviewed by Tim Dumol]
#7467: Tim Dumol: Make SageNB use `setuptools` instead of `distutils` [Reviewed by Mitesh Patel]
#7390: Mitesh Patel: HTML notebook test report [Reviewed by Tim Dumol]
#7470: Tim Dumol: SageNB -- Minor docstring fixes for `js.py` [Reviewed by Mitesh Patel]
```



---

Comment by was created at 2009-12-08 18:04:59

I just posted the release notes for this above.


---

Comment by mpatel created at 2009-12-08 21:48:34

This looks good to me, apart from the comedy of errors that is the notebook settings page.  Also, 14 out of 15 Selenium tests still pass (cf. #7455).

I think Dr. Palmieri reviewed #7470.

Positive review, pending Tim's confirmation?


---

Comment by was created at 2009-12-09 01:48:48

Hi, 

I merged in 9 more patches to make sagenb-0.4.6, which does fix the notebook settings page issues.  We should release sagenb-0.4.6 instead: 

   http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.5.spkg


```
#5100: Tim Dumol: worksheets: can't empty the trash (safari only?) [Reviewed by John Palmieri and William Stein]
#3733: William Stein: document notebook.css; I also sphinxified the notebook? docstring [Reviewed by Tim Dumol]
#7433: Tim Dumol: Changing title of worksheet changes title of corresponding published worksheet [Reviewed by William Stein]
#7455: Tim Dumol: Searching on Log page does not work [Reviewed by William Stein]
#4714: Mitesh Patel: use easy/load.js when loading jsmath in the notebook [Reviewed by William Stein]
#7267: Mitesh Patel: Add a compact color picker to SageNB [Reviewed by William Stein and Tim Dumol]
#7376: Mitesh Patel: searching published worksheets does not work to just search for username [Reviewed by William Stein]
#7447: Mitesh Patel: SageNB version and install date / time [Reviewed by William Stein]
#7611: Tim Dumol: Minor ReST improvements for the notebook object documentation [Reviewed by William Stein]
```



---

Comment by was created at 2009-12-09 01:49:12

Here I meant  http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.6.spkg of course.


---

Comment by mpatel created at 2009-12-09 02:24:46

All Se tests now pass.  But I'm a bit too tired right now to do further checking.

Potential feature for the log page: A check box next to each cell, so the user can select a subset for a new worksheet?


---

Comment by timdumol created at 2009-12-09 11:29:39

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2009-12-09 11:29:39

Se tests pass on my machine as well. Nothing broke in my worksheets either.

Since Patel also agrees, I'll mark this with a positive review.


---

Comment by mhansen created at 2009-12-10 03:23:48

Resolution: fixed


---

Comment by timdumol created at 2009-12-10 14:01:31

Correct me if I'm mistaken, but is #7467 actually included? I cannot find it in the merge log.


---

Comment by was created at 2009-12-10 19:47:07

Resolution changed from fixed to 


---

Comment by was created at 2009-12-10 19:47:07

Changing status from closed to new.


---

Comment by was created at 2009-12-10 19:47:07

Replying to [comment:10 timdumol]:
> Correct me if I'm mistaken, but is #7467 actually included? I cannot find it in the merge log.

Oh crap, you're right.  I don't know how I made that mistake.  Here's a sagenb-0.4.7 that includes that and one other patch I merged:

  http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.7.spkg


```
SAGENB-0.4.7
#7467: Tim Dumol: Make SageNB use `setuptools` instead of `distutils` [Reviewed by Mitesh Patel]
#7628: Mitesh Patel: Error on account creation still creates (half of) an account [Reviewed by William Stein]
```



---

Comment by was created at 2009-12-10 19:47:17

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-12-11 02:51:03

Looks good.


---

Comment by mhansen created at 2009-12-11 02:51:03

Resolution: fixed

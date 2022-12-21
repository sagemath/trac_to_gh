# Issue 1861: better document sage.el

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-20 02:41:36

Assignee: was

The page here http://www.sagemath.org/emacs has a file sage.el that is slightly modified from the ipython.el file.   The documentation of this fact should be clearly stated in the file sage.el, along with some instructions about how to use it and the above URL. 

Somebody could fix this and attach the fixed sage.el to this ticket. 


---

Comment by was created at 2008-01-20 02:41:53

By the way, this bug was reported by Dan Grayson.


---

Comment by AlexGhitza created at 2009-01-23 07:09:33

Changing type from defect to enhancement.


---

Comment by iandrus created at 2012-05-25 18:52:25

Changing status from new to needs_review.


---

Comment by iandrus created at 2012-05-25 18:52:25

This has been superseded by the optional sage-mode spkg.


---

Comment by kcrisman created at 2012-06-28 13:54:24

Plus, there isn't even an emacs page at sagemath.org any more.  [http://wiki.sagemath.org/sage-mode](http://wiki.sagemath.org/sage-mode) is the new place to go.  It does have a lot better documentation.

To be pedantic, I _would_ point out that the current (0.6) spkg doesn't actually say that this is inherited from ipython.el.  It is sort of implied in sage-mode-0.6/old/README.txt; is that enough?


---

Comment by iandrus created at 2012-06-28 16:07:53

Since we don't use the old directory anymore (I'm planning to remove it in the next release), and I'm pretty sure the new stuff isn't derived from ipython.el I think this should be closed as won't fix.


---

Comment by kcrisman created at 2012-06-28 16:10:14

Okay, I'll say that's okay as long as (to honor this ticket) _somewhere_ in the documentation, wiki, bitbucket, whatever, there is a place that says this was inspired by ipython.el originally.  Sound good?  I'll put that on #13176, which is for upgrading to 0.7.


---

Comment by kcrisman created at 2012-06-28 16:10:14

Changing status from needs_review to positive_review.


---

Comment by iandrus created at 2012-06-29 11:28:39

I updated the wiki, and SPKG.txt.


---

Comment by kcrisman created at 2012-06-29 12:44:47

Great, this is an immediate improvement on the wiki, and 0.8 has this as well.  Putting back to a "normal" milestone since #13176 is slightly more complex.


---

Comment by kcrisman created at 2012-06-29 12:44:47

Changing priority from major to minor.


---

Comment by jdemeyer created at 2012-06-29 14:01:51

Replying to [comment:8 kcrisman]:
> Great, this is an immediate improvement on the wiki, and 0.8 has this as well.  Putting back to a "normal" milestone since #13176 is slightly more complex.

So, this has positive_review but no patch and not a duplicate?  What is it then?


---

Comment by kcrisman created at 2012-06-29 14:57:26

It's sort of like when someone opens a ticket to do something on Trac itself (create a new report, let's say).  Here, updating [the wiki](http://wiki.sagemath.org/sage-mode) and having [upstream](https://bitbucket.org/gvol/sage-mode/changeset/b08a6d64faea) incorporate this last thing in all future versions was sufficient.  After all, the original ticket was just to change a webpage - no patch was really required there.  

If you'd really like, I can make a patch _from_ the changeset and [these](https://bitbucket.org/gvol/sage-mode/changeset/63452ed4dee9) [others](https://bitbucket.org/gvol/sage-mode/changeset/5d9ae431a7c7), attach them here, and we can wait until Ivan actually releases another one or something, but according to the _original_ issue, the changes at the wiki are already more than sufficient.  Basically, I figure that the person who actually makes things easier to figure out deserves at least some credit.


---

Comment by jdemeyer created at 2012-06-29 15:27:48

Okay, that's clear.


---

Comment by jdemeyer created at 2012-06-29 15:35:26

Resolution: fixed

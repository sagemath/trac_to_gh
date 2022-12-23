# Issue 7524: frame axes are lost when saving a graphic to a file

Issue created by migration from https://trac.sagemath.org/ticket/7524

Original creator: jason

Original creation time: 2009-11-24 08:28:25

Assignee: was

CC:  novoselt jason

Notice that the frame axes are shown when using "show", but are missing when using "save"


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: var('x,y')                
(x, y)
sage: a=plot_vector_field((x,-y),(x,-1,1),(y,-1,1))
sage: a.show()
sage: a.save('test.png')
```

| Sage Version 4.2.1, Release Date: 2009-11-14                       |
| Type notebook() for the GUI, and license() for information.        |


---

Comment by jason created at 2010-01-19 04:47:47

Changing status from new to needs_review.


---

Comment by jason created at 2010-01-19 04:47:47

This is fixed with #7981


---

Comment by rossk created at 2010-01-31 05:46:27

Changing status from needs_review to needs_work.


---

Comment by rossk created at 2010-01-31 05:46:27

Got the following on applying  trac-7981-show_options.patch to sage-4.3.2-alpha

~/sage-4.3.2.alpha0/devel/sage-main$ hg qpush
applying trac-7981-show_options.patch
patching file sage/plot/plot.py
Hunk #3 FAILED at 1913
1 out of 5 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac-7981-show_options.patch


---

Comment by kcrisman created at 2011-01-17 20:23:03

Might be worth trying this again, now that #7981 has positive review.  Would need a patch to document.


---

Comment by kcrisman created at 2011-01-17 21:09:00

I can confirm that this works after #7981.


---

Comment by kcrisman created at 2011-01-17 21:16:33

This test checks that it works.  Passes relevant test, plot looks good.


---

Attachment


---

Comment by kcrisman created at 2011-01-17 21:22:00

This definitely depends on #7981, #8632, and #10244.  It's conceivable, but unlikely, that it depends on #10143, and might also depend on #2100.  All in that order.  This is because it applies to the very popular file `plot.py`.


---

Comment by kcrisman created at 2011-01-17 21:22:00

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2011-01-20 05:58:49

Changing status from needs_review to positive_review.


---

Comment by novoselt created at 2011-01-20 05:58:49

Let's say it depends on #10143, since it has positive review already. The patch looks and applies fine, positive review!


---

Comment by kcrisman created at 2011-01-21 13:31:12

I've set #2100 to 'needs work', but this still applies fine after #7981, #8632, #10244, and #10143 on 4.6.2.alpha1, so still should be included in the next alpha.


---

Comment by jdemeyer created at 2011-01-27 13:14:28

Resolution: fixed

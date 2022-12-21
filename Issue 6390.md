# Issue 6390: Implement elliptic logarithms (complex case)

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2009-06-23 19:59:32

Assignee: was

CC:  robertwb rlm

Keywords: elliptic curve logarithm

As of 4.0.2 we only have elliptic logs for curves defined over the reals (including curves over number fields with a real embedding).  We also need the complex case, which can be implemented using the complex AGM.  I expect to be adding this during June/July 2009.


---

Comment by davidloeffler created at 2009-07-21 08:16:13

Changing component from number theory to elliptic curves.


---

Comment by davidloeffler created at 2009-07-21 08:16:13

Changing assignee from was to davidloeffler.


---

Comment by cremona created at 2009-07-21 08:56:55

Update 2009-07-21: I still have this only half done, the gap being proof of a theorem rather than any coding issue, and other responsibilities mean that it is likely to be August rather than July: sorry.


---

Comment by davidloeffler created at 2009-10-09 09:11:52

Remove assignee davidloeffler.


---

Comment by cremona created at 2010-03-16 14:19:18

Replying to [comment:2 cremona]:
> Update 2009-07-21: I still have this only half done, the gap being proof of a theorem rather than any coding issue, and other responsibilities mean that it is likely to be August rather than July: sorry.

March 2010:  it was clearly a mistake to put in a time estimate.  We now have a preprint explaining all the relevant theory:

J. E. Cremona and T. Thongjunthug, "On computing complex elliptic logarithms" (provisional title) 

which I am now going to implement i nSage (my coauthor has already implemented it in Magma).


---

Comment by cremona created at 2010-03-20 20:48:13

Applies to 4.3.4


---

Attachment

The patch implements complex elliptic logs as promised, and makes a few minor improvements to the periods & elliptic log code generally.

The new code works fine for real embeddings too, and is almost as fast:  for the database curves up to conductor 1000 (and with the optional database installed so that all generators are pre-installed) the new code takes 183 seconds to find all logs of all generators (for the optimal curves) while the old code takes 154s.  The new code is also rather simpler.  I have left in the old code.  Reviewers wishing to test this can do so by switching lines 1243 and 1244 of period_lattice.py: doctests almost all succeed, with a tiny amount of fuzz in some elliptic exponential computations.

I am CC'ing rlm since after installing the optional database of curves (and generators) and testing all of sage/schemes/elliptic_curves, I found that there were some failures in heegner.py, mainly caused by E.gens() sometimes now producing different generators.  I fixed almost all of these (since I think that as a matter of principle these doctests should not be dependent on the database not being installed!) but there are two I cannot fix (lines 1409 and 1415 of heegner.py) and I am hoping that Robert M will be able to.


---

Comment by cremona created at 2010-03-20 20:55:27

Set assignee to cremona.


---

Comment by cremona created at 2010-03-20 20:55:37

Changing status from new to needs_review.


---

Attachment


---

Comment by rlm created at 2010-03-23 15:41:46

Replying to [comment:5 cremona]:
> I am CC'ing rlm since after installing the optional database of curves (and generators) and testing all of sage/schemes/elliptic_curves, I found that there were some failures in heegner.py, mainly caused by E.gens() sometimes now producing different generators.  I fixed almost all of these (since I think that as a matter of principle these doctests should not be dependent on the database not being installed!) but there are two I cannot fix (lines 1409 and 1415 of heegner.py) and I am hoping that Robert M will be able to.

The following change fixes this, but I can't vouch for its advisability.

```
--- a/sage/schemes/elliptic_curves/heegner.py	Sat Mar 20 15:52:55 2010 +0000
+++ b/sage/schemes/elliptic_curves/heegner.py	Tue Mar 23 08:39:11 2010 -0700
`@``@` -4165,7 +4165,7 `@``@`
         # etc" mentioned in Watkins' article... which involves local
         # heights.
         E = self.curve()  # over Q
-        v = sum([list(n*w) for w in E.gens()] + [list(w) for w in E.torsion_points()], [])
+        v = sum([list(n*w) for w in E.gens(use_database=False)] + [list(w) for w in E.torsion_points()], [])
         # note -- we do not claim to prove anything, so making up a factor of 100 is fine.
         max_denominator = 100*max([z.denominator() for z in v])
         try:
```


When testing on my laptop, I came across another doctest error, and I've included a patch for it.


---

Comment by cremona created at 2010-03-23 16:29:17

Thanks, Robert.  With luck soem else will referee the main part of the patch, but I'm in no great hurry as I'll be on holiday for a week from tomorrow!


---

Comment by wuthrich created at 2010-03-24 11:26:32

Changing status from needs_review to needs_work.


---

Comment by wuthrich created at 2010-03-24 11:26:32

I wanted to review it, then I noticed from a problem in the documentation that the first patch has many tabulators in it. Unfortunately, I can not just replace all tabs by 4 spaces in the patch as then it makes a mess out of the code. So I guess that John can do the replacement faster than me.

(Most editors allow the setting that all tabulators are replaces by 4 spaces automatically, this would avoid these problems automatically.)

It is a shame that the tabs are not visible here.


---

Attachment

exported against 4.3.4, replaces the previous patches


---

Comment by wuthrich created at 2010-03-28 19:10:07

I uploaded a new patch that incorporates the previous two changes, switches the tabs to spaces and also solves the two remaining doctest problems in heegner.py (using random and only testing the squares, admittedly ugly), and it fixes a problem in the documentation (a missing ::).

I start testing now. Unless the author claims that I made an error in the indentation of the new patch (when removing the tabs), I will give it a positive review after the test.


---

Comment by wuthrich created at 2010-03-28 22:17:47

All tests passed. I wish to give a positive review, but the button for it has disappeared ??


---

Comment by wuthrich created at 2010-03-28 22:18:18

Changing status from needs_work to needs_review.


---

Comment by wuthrich created at 2010-03-28 22:18:38

Changing status from needs_review to positive_review.


---

Comment by wuthrich created at 2010-03-28 22:18:38

Here we go !!!


---

Comment by cremona created at 2010-03-30 19:21:52

Many thanks, Chris, and sorry for not responding earlier but I was on holiday for a few days.

Sorry too for the tab/space issue.  I just don't see to be able to set up emacs correctly on all the machines I use... but I'll try not to do it again.


---

Comment by jhpalmieri created at 2010-04-15 05:20:56

Merged trac_6390.patch in 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-15 05:20:56

Resolution: fixed


---

Comment by robertwb created at 2011-09-01 17:56:28

When #11761 gets approved, we can move using `# distutils: language = c++` which is understood by Cython and can be used to specify any Extension options.


---

Comment by robertwb created at 2011-09-01 17:56:50

Oops, forgot the link: http://wiki.cython.org/enhancements/distutils_preprocessing


---

Comment by robertwb created at 2011-09-01 17:57:49

(Argh--too many trac tabs open. Wrong ticket. Think before hitting submit...)

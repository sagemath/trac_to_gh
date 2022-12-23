# Issue 7112: os x 10.5 powerpc -- there are many many doctest failures all over

Issue created by migration from https://trac.sagemath.org/ticket/7112

Original creator: was

Original creation time: 2009-10-04 17:28:34

Assignee: tbd


```
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage/sage/calculus/calculus.py"
        sage -t -long "devel/sage/sage/misc/latex.py"
        sage -t -long "devel/sage/sage/rings/number_field/totallyreal_rel.py"
        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
        sage -t -long "devel/sage/sage/server/notebook/notebook.py"
        sage -t -long "devel/sage/sage/server/simple/twist.py"
        sage -t -long "devel/sage/sage/symbolic/expression.pyx"
Total time for all tests: 23343.5 seconds
pdlc424:~ wstein$  
```


The complete testlog is here:

http://sage.math.washington.edu/home/wstein/patches/testlong-os10.5-ppc.log


---

Attachment

with this patch applied all doctest pass for me on OS X 10.5 PPC


---

Comment by was created at 2009-10-07 12:33:53

I attached a patch trac_7112.patch that fixes all doctest issues:

  * I couldn't reproduce the weird maxima-related solve doctest failure in the original log.

  * I changed `sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session)) ` to use a larger timeout, since on OS X 10.5 PPC the default timeout isn't enough for Sage to even startup.

  * There is a numerical noise in ell_rational_field.py

  * The output of totallyreal_rel.py was not deterministic so I sorted it.

  * This `dict_function({x/2: y^2, "hallo": "world"})` test latex.py is *impossible* to do right with more than one dictionary entry, since dictionaries are by definition in a random platform dependent order.  So I made it a dictionary of length 1.

  * The html output for the notebook.py test is a bit different on OS X. It doesn't matter so much since that code is deprecated in sage-4.1.2.


---

Comment by was created at 2009-10-07 12:56:47

needed so that all tests also pass on sage.math.


---

Attachment

(Note that I already merged this in sage-4.1.2.rc1.alpha3.  However, it awaits review before I'll release sage-4.1.2.)


---

Comment by was created at 2009-10-07 12:57:28

Changing status from new to needs_review.


---

Comment by was created at 2009-10-08 15:41:27

Old habits die hard...


---

Comment by kcrisman created at 2009-10-08 15:54:31

For reference for # 6642: the numerical noise issue in calculus.py was also noticed on #6642.


---

Comment by kcrisman created at 2009-10-08 18:31:26

I hate to tell you this...

For some reason on PPC X.4, I actually got a different answer, forget the sorting, on the item in part2.  I don't know why, but '5'  did not show up in the list.   Indeed, it must not have Same running the commands separately.  Even more aggravating, doctests pass now BUT if I do it "by hand", I still don't get 5, no matter what I do.  And it looks like that must be the case on your X.5 PPC as well, since you removed the five in the first patch.

But on Macintel X.5, I get the 5, as I also do on sagenb.org.  So I assume that the '5' is right, BUT the answer is definitely different on PPC.  What now?  Is there a way to mark this test as being dependent?  Or should there be a ... in the test?  Or is there a bug in the code for integral_elements_in_box?  

On the plus side, everything else is great!


---

Comment by kcrisman created at 2009-10-08 18:31:26

Changing status from needs_review to needs_work.


---

Comment by GeorgSWeber created at 2009-10-10 20:58:54

Changing status from needs_work to needs_review.


---

Comment by GeorgSWeber created at 2009-10-10 20:58:54

From just reading the patch(es), this is a positive review. The

```
sage -t -long devel/sage/sage/rings/number_field/totallyreal_rel.py
```

will still fail however, there is a deeper problem lurking in that one point of a certain lattice sitting in a certain rectangle is missed in the computations on a PPC platform --- but that would be another ticket. Let the doctest fail for the time being, the enhancements by the patch(es) for this ticket here are needed anyway, I guess.

All I need is to really test the whole patch(es) on my PPC, but #7186 was holding me up (the very first file, calculus.py, did show a very nasty doctest output ...), so I have to postpone this for yet another day (i.e. night, sigh ...).


---

Comment by GeorgSWeber created at 2009-10-12 06:06:38

Changing status from needs_review to positive_review.


---

Comment by GeorgSWeber created at 2009-10-12 15:41:38

Do I need to change both the title and press the button? Hmm, I'll check the Wiki.


---

Comment by was created at 2009-10-14 16:11:20

Resolution: fixed

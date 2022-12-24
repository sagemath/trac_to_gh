# Issue 7112: os x 10.5 powerpc -- there are many many doctest failures all over

archive/issues_007112.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long \"devel/sage/sage/calculus/calculus.py\"\n        sage -t -long \"devel/sage/sage/misc/latex.py\"\n        sage -t -long \"devel/sage/sage/rings/number_field/totallyreal_rel.py\"\n        sage -t -long \"devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\"\n        sage -t -long \"devel/sage/sage/server/notebook/notebook.py\"\n        sage -t -long \"devel/sage/sage/server/simple/twist.py\"\n        sage -t -long \"devel/sage/sage/symbolic/expression.pyx\"\nTotal time for all tests: 23343.5 seconds\npdlc424:~ wstein$  \n```\n\n\nThe complete testlog is here:\n\nhttp://sage.math.washington.edu/home/wstein/patches/testlong-os10.5-ppc.log\n\nIssue created by migration from https://trac.sagemath.org/ticket/7112\n\n",
    "created_at": "2009-10-04T17:28:34Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "os x 10.5 powerpc -- there are many many doctest failures all over",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7112",
    "user": "was"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/7112





---

archive/issue_comments_058942.json:
```json
{
    "body": "Attachment [trac_7112.patch](tarball://root/attachments/some-uuid/ticket7112/trac_7112.patch) by was created at 2009-10-07 12:15:31\n\nwith this patch applied all doctest pass for me on OS X 10.5 PPC",
    "created_at": "2009-10-07T12:15:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7112#issuecomment-58942",
    "user": "was"
}
```

Attachment [trac_7112.patch](tarball://root/attachments/some-uuid/ticket7112/trac_7112.patch) by was created at 2009-10-07 12:15:31

with this patch applied all doctest pass for me on OS X 10.5 PPC



---

archive/issue_comments_058943.json:
```json
{
    "body": "I attached a patch trac_7112.patch that fixes all doctest issues:\n\n* I couldn't reproduce the weird maxima-related solve doctest failure in the original log.\n\n* I changed `sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session)) ` to use a larger timeout, since on OS X 10.5 PPC the default timeout isn't enough for Sage to even startup.\n\n* There is a numerical noise in ell_rational_field.py\n\n* The output of totallyreal_rel.py was not deterministic so I sorted it.\n\n* This `dict_function({x/2: y^2, \"hallo\": \"world\"})` test latex.py is *impossible* to do right with more than one dictionary entry, since dictionaries are by definition in a random platform dependent order.  So I made it a dictionary of length 1.\n\n* The html output for the notebook.py test is a bit different on OS X. It doesn't matter so much since that code is deprecated in sage-4.1.2.",
    "created_at": "2009-10-07T12:33:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7112#issuecomment-58943",
    "user": "was"
}
```

I attached a patch trac_7112.patch that fixes all doctest issues:

* I couldn't reproduce the weird maxima-related solve doctest failure in the original log.

* I changed `sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session)) ` to use a larger timeout, since on OS X 10.5 PPC the default timeout isn't enough for Sage to even startup.

* There is a numerical noise in ell_rational_field.py

* The output of totallyreal_rel.py was not deterministic so I sorted it.

* This `dict_function({x/2: y^2, "hallo": "world"})` test latex.py is *impossible* to do right with more than one dictionary entry, since dictionaries are by definition in a random platform dependent order.  So I made it a dictionary of length 1.

* The html output for the notebook.py test is a bit different on OS X. It doesn't matter so much since that code is deprecated in sage-4.1.2.



---

archive/issue_comments_058944.json:
```json
{
    "body": "needed so that all tests also pass on sage.math.",
    "created_at": "2009-10-07T12:56:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7112#issuecomment-58944",
    "user": "was"
}
```

needed so that all tests also pass on sage.math.



---

archive/issue_comments_058945.json:
```json
{
    "body": "Attachment [trac_7112-part2.patch](tarball://root/attachments/some-uuid/ticket7112/trac_7112-part2.patch) by was created at 2009-10-07 12:57:20\n\n(Note that I already merged this in sage-4.1.2.rc1.alpha3.  However, it awaits review before I'll release sage-4.1.2.)",
    "created_at": "2009-10-07T12:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7112#issuecomment-58945",
    "user": "was"
}
```

Attachment [trac_7112-part2.patch](tarball://root/attachments/some-uuid/ticket7112/trac_7112-part2.patch) by was created at 2009-10-07 12:57:20

(Note that I already merged this in sage-4.1.2.rc1.alpha3.  However, it awaits review before I'll release sage-4.1.2.)



---

archive/issue_comments_058946.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-07T12:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7112#issuecomment-58946",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058947.json:
```json
{
    "body": "Old habits die hard...",
    "created_at": "2009-10-08T15:41:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7112#issuecomment-58947",
    "user": "was"
}
```

Old habits die hard...



---

archive/issue_comments_058948.json:
```json
{
    "body": "For reference for # 6642: the numerical noise issue in calculus.py was also noticed on #6642.",
    "created_at": "2009-10-08T15:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7112#issuecomment-58948",
    "user": "kcrisman"
}
```

For reference for # 6642: the numerical noise issue in calculus.py was also noticed on #6642.



---

archive/issue_comments_058949.json:
```json
{
    "body": "I hate to tell you this...\n\nFor some reason on PPC X.4, I actually got a different answer, forget the sorting, on the item in part2.  I don't know why, but '5'  did not show up in the list.   Indeed, it must not have Same running the commands separately.  Even more aggravating, doctests pass now BUT if I do it \"by hand\", I still don't get 5, no matter what I do.  And it looks like that must be the case on your X.5 PPC as well, since you removed the five in the first patch.\n\nBut on Macintel X.5, I get the 5, as I also do on sagenb.org.  So I assume that the '5' is right, BUT the answer is definitely different on PPC.  What now?  Is there a way to mark this test as being dependent?  Or should there be a ... in the test?  Or is there a bug in the code for integral_elements_in_box?  \n\nOn the plus side, everything else is great!",
    "created_at": "2009-10-08T18:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7112#issuecomment-58949",
    "user": "kcrisman"
}
```

I hate to tell you this...

For some reason on PPC X.4, I actually got a different answer, forget the sorting, on the item in part2.  I don't know why, but '5'  did not show up in the list.   Indeed, it must not have Same running the commands separately.  Even more aggravating, doctests pass now BUT if I do it "by hand", I still don't get 5, no matter what I do.  And it looks like that must be the case on your X.5 PPC as well, since you removed the five in the first patch.

But on Macintel X.5, I get the 5, as I also do on sagenb.org.  So I assume that the '5' is right, BUT the answer is definitely different on PPC.  What now?  Is there a way to mark this test as being dependent?  Or should there be a ... in the test?  Or is there a bug in the code for integral_elements_in_box?  

On the plus side, everything else is great!



---

archive/issue_comments_058950.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-08T18:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7112#issuecomment-58950",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_058951.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-10T20:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7112#issuecomment-58951",
    "user": "GeorgSWeber"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_058952.json:
```json
{
    "body": "From just reading the patch(es), this is a positive review. The\n\n```\nsage -t -long devel/sage/sage/rings/number_field/totallyreal_rel.py\n```\n\nwill still fail however, there is a deeper problem lurking in that one point of a certain lattice sitting in a certain rectangle is missed in the computations on a PPC platform --- but that would be another ticket. Let the doctest fail for the time being, the enhancements by the patch(es) for this ticket here are needed anyway, I guess.\n\nAll I need is to really test the whole patch(es) on my PPC, but #7186 was holding me up (the very first file, calculus.py, did show a very nasty doctest output ...), so I have to postpone this for yet another day (i.e. night, sigh ...).",
    "created_at": "2009-10-10T20:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7112#issuecomment-58952",
    "user": "GeorgSWeber"
}
```

From just reading the patch(es), this is a positive review. The

```
sage -t -long devel/sage/sage/rings/number_field/totallyreal_rel.py
```

will still fail however, there is a deeper problem lurking in that one point of a certain lattice sitting in a certain rectangle is missed in the computations on a PPC platform --- but that would be another ticket. Let the doctest fail for the time being, the enhancements by the patch(es) for this ticket here are needed anyway, I guess.

All I need is to really test the whole patch(es) on my PPC, but #7186 was holding me up (the very first file, calculus.py, did show a very nasty doctest output ...), so I have to postpone this for yet another day (i.e. night, sigh ...).



---

archive/issue_comments_058953.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-12T06:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7112#issuecomment-58953",
    "user": "GeorgSWeber"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058954.json:
```json
{
    "body": "Do I need to change both the title and press the button? Hmm, I'll check the Wiki.",
    "created_at": "2009-10-12T15:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7112#issuecomment-58954",
    "user": "GeorgSWeber"
}
```

Do I need to change both the title and press the button? Hmm, I'll check the Wiki.



---

archive/issue_comments_058955.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-14T16:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7112#issuecomment-58955",
    "user": "was"
}
```

Resolution: fixed

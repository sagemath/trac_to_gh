# Issue 7524: frame axes are lost when saving a graphic to a file

archive/issues_007524.json:
```json
{
    "body": "Assignee: was\n\nCC:  novoselt jason\n\nNotice that the frame axes are shown when using \"show\", but are missing when using \"save\"\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: var('x,y')                \n(x, y)\nsage: a=plot_vector_field((x,-y),(x,-1,1),(y,-1,1))\nsage: a.show()\nsage: a.save('test.png')\n```\n\n| Sage Version 4.2.1, Release Date: 2009-11-14                       |\n| Type notebook() for the GUI, and license() for information.        |\n\nIssue created by migration from https://trac.sagemath.org/ticket/7524\n\n",
    "created_at": "2009-11-24T08:28:25Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "frame axes are lost when saving a graphic to a file",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7524",
    "user": "jason"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/7524





---

archive/issue_comments_063773.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T04:47:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7524#issuecomment-63773",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063774.json:
```json
{
    "body": "This is fixed with #7981",
    "created_at": "2010-01-19T04:47:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7524#issuecomment-63774",
    "user": "jason"
}
```

This is fixed with #7981



---

archive/issue_comments_063775.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-31T05:46:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7524#issuecomment-63775",
    "user": "rossk"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063776.json:
```json
{
    "body": "Got the following on applying  trac-7981-show_options.patch to sage-4.3.2-alpha\n\n~/sage-4.3.2.alpha0/devel/sage-main$ hg qpush\napplying trac-7981-show_options.patch\npatching file sage/plot/plot.py\nHunk #3 FAILED at 1913\n1 out of 5 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac-7981-show_options.patch",
    "created_at": "2010-01-31T05:46:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7524#issuecomment-63776",
    "user": "rossk"
}
```

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

archive/issue_comments_063777.json:
```json
{
    "body": "Might be worth trying this again, now that #7981 has positive review.  Would need a patch to document.",
    "created_at": "2011-01-17T20:23:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7524#issuecomment-63777",
    "user": "kcrisman"
}
```

Might be worth trying this again, now that #7981 has positive review.  Would need a patch to document.



---

archive/issue_comments_063778.json:
```json
{
    "body": "I can confirm that this works after #7981.",
    "created_at": "2011-01-17T21:09:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7524#issuecomment-63778",
    "user": "kcrisman"
}
```

I can confirm that this works after #7981.



---

archive/issue_comments_063779.json:
```json
{
    "body": "This test checks that it works.  Passes relevant test, plot looks good.",
    "created_at": "2011-01-17T21:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7524#issuecomment-63779",
    "user": "kcrisman"
}
```

This test checks that it works.  Passes relevant test, plot looks good.



---

archive/issue_comments_063780.json:
```json
{
    "body": "Attachment [trac_7524-options-save.patch](tarball://root/attachments/some-uuid/ticket7524/trac_7524-options-save.patch) by kcrisman created at 2011-01-17 21:18:35",
    "created_at": "2011-01-17T21:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7524#issuecomment-63780",
    "user": "kcrisman"
}
```

Attachment [trac_7524-options-save.patch](tarball://root/attachments/some-uuid/ticket7524/trac_7524-options-save.patch) by kcrisman created at 2011-01-17 21:18:35



---

archive/issue_comments_063781.json:
```json
{
    "body": "This definitely depends on #7981, #8632, and #10244.  It's conceivable, but unlikely, that it depends on #10143, and might also depend on #2100.  All in that order.  This is because it applies to the very popular file `plot.py`.",
    "created_at": "2011-01-17T21:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7524#issuecomment-63781",
    "user": "kcrisman"
}
```

This definitely depends on #7981, #8632, and #10244.  It's conceivable, but unlikely, that it depends on #10143, and might also depend on #2100.  All in that order.  This is because it applies to the very popular file `plot.py`.



---

archive/issue_comments_063782.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-17T21:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7524#issuecomment-63782",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063783.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-20T05:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7524#issuecomment-63783",
    "user": "novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063784.json:
```json
{
    "body": "Let's say it depends on #10143, since it has positive review already. The patch looks and applies fine, positive review!",
    "created_at": "2011-01-20T05:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7524#issuecomment-63784",
    "user": "novoselt"
}
```

Let's say it depends on #10143, since it has positive review already. The patch looks and applies fine, positive review!



---

archive/issue_comments_063785.json:
```json
{
    "body": "I've set #2100 to 'needs work', but this still applies fine after #7981, #8632, #10244, and #10143 on 4.6.2.alpha1, so still should be included in the next alpha.",
    "created_at": "2011-01-21T13:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7524#issuecomment-63785",
    "user": "kcrisman"
}
```

I've set #2100 to 'needs work', but this still applies fine after #7981, #8632, #10244, and #10143 on 4.6.2.alpha1, so still should be included in the next alpha.



---

archive/issue_comments_063786.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-27T13:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7524#issuecomment-63786",
    "user": "jdemeyer"
}
```

Resolution: fixed

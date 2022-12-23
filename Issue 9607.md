# Issue 9607: Doctest failure in latex.rst

archive/issues_009607.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  ddrake jhpalmieri mvngu rbeezer\n\nSeen on sage.math and bsd.math with Sage 4.5.2.alpha1:\n\n```python\nsage -t -long  devel/sage/doc/en/tutorial/latex.rst\n**********************************************************************\nFile \"/Users/mpatel/apps/sage-4.5.2.alpha1/devel/sage-main/doc/en/tutorial/latex\n.rst\", line 459:\n    sage: latex.extra_preamble()\nExpected:\n    '\\\\usepackage{tikz}\\n\\\\usepackage{tkz-graph}\\n\\\\usepackage{tkz-berge}\\n'\nGot:\n    '\\\\usepackage{tikz}\\n'\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_11\n***Test Failed*** 1 failures.\n```\n\n\nThis may be caused by #9027.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9607\n\n",
    "created_at": "2010-07-27T07:00:47Z",
    "labels": [
        "documentation",
        "blocker",
        "bug"
    ],
    "title": "Doctest failure in latex.rst",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9607",
    "user": "mpatel"
}
```
Assignee: mvngu

CC:  ddrake jhpalmieri mvngu rbeezer

Seen on sage.math and bsd.math with Sage 4.5.2.alpha1:

```python
sage -t -long  devel/sage/doc/en/tutorial/latex.rst
**********************************************************************
File "/Users/mpatel/apps/sage-4.5.2.alpha1/devel/sage-main/doc/en/tutorial/latex
.rst", line 459:
    sage: latex.extra_preamble()
Expected:
    '\\usepackage{tikz}\n\\usepackage{tkz-graph}\n\\usepackage{tkz-berge}\n'
Got:
    '\\usepackage{tikz}\n'
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_11
***Test Failed*** 1 failures.
```


This may be caused by #9027.

Issue created by migration from https://trac.sagemath.org/ticket/9607





---

archive/issue_comments_093060.json:
```json
{
    "body": "Almost certainly due to #9027.  I have two builds going and will investigate in the morning.",
    "created_at": "2010-07-27T07:32:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9607#issuecomment-93060",
    "user": "rbeezer"
}
```

Almost certainly due to #9027.  I have two builds going and will investigate in the morning.



---

archive/issue_comments_093061.json:
```json
{
    "body": "Ah, note that in latex.rst, it does `setup_latex_preamble()`. Here's that entire function:\n\n```\nlatex.add_package_to_preamble_if_available(\"tikz\")\nlatex.add_package_to_preamble_if_available(\"tkz-graph\")\nlatex.add_package_to_preamble_if_available(\"tkz-berge\")\n```\n\nSo on sage.math, it looks like tkz-graph and tkz-berge are not getting added because they're not available.",
    "created_at": "2010-07-27T07:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9607#issuecomment-93061",
    "user": "ddrake"
}
```

Ah, note that in latex.rst, it does `setup_latex_preamble()`. Here's that entire function:

```
latex.add_package_to_preamble_if_available("tikz")
latex.add_package_to_preamble_if_available("tkz-graph")
latex.add_package_to_preamble_if_available("tkz-berge")
```

So on sage.math, it looks like tkz-graph and tkz-berge are not getting added because they're not available.



---

archive/issue_comments_093062.json:
```json
{
    "body": "It seems that none of the three packages is available on t2:\n\n```python\nExpected:\n    '\\\\usepackage{tikz}\\n\\\\usepackage{tkz-graph}\\n\\\\usepackage{tkz-berge}\\n'\nGot:\n    ''\n```\n",
    "created_at": "2010-07-27T08:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9607#issuecomment-93062",
    "user": "mpatel"
}
```

It seems that none of the three packages is available on t2:

```python
Expected:
    '\\usepackage{tikz}\n\\usepackage{tkz-graph}\n\\usepackage{tkz-berge}\n'
Got:
    ''
```




---

archive/issue_comments_093063.json:
```json
{
    "body": "Attachment\n\nPatch marks the test as random, which I think is the right thing to do, not just an expedient.\n\nThere is no way to know what extra packages a system will have, and this block of code is meant more as an illustration than as a test.  So in particular, the line in question could even be removed, but then there would be less of the behavior documented.",
    "created_at": "2010-07-27T15:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9607#issuecomment-93063",
    "user": "rbeezer"
}
```

Attachment

Patch marks the test as random, which I think is the right thing to do, not just an expedient.

There is no way to know what extra packages a system will have, and this block of code is meant more as an illustration than as a test.  So in particular, the line in question could even be removed, but then there would be less of the behavior documented.



---

archive/issue_comments_093064.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-27T15:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9607#issuecomment-93064",
    "user": "rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093065.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-27T17:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9607#issuecomment-93065",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093066.json:
```json
{
    "body": "This looks good to me.\n\nSorry, I should have caught this when I reviewed the original ticket.",
    "created_at": "2010-07-27T17:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9607#issuecomment-93066",
    "user": "jhpalmieri"
}
```

This looks good to me.

Sorry, I should have caught this when I reviewed the original ticket.



---

archive/issue_comments_093067.json:
```json
{
    "body": "> Sorry, I should have caught this when I reviewed the original ticket.\n\nWell, I know better, it shouldn't have been there.  I have a latex-free system available at the moment, and I suspect #9074 could meet the same fate (I'll check shortly).\n\nThanks for the quick look at this one.\n\nRob",
    "created_at": "2010-07-27T17:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9607#issuecomment-93067",
    "user": "rbeezer"
}
```

> Sorry, I should have caught this when I reviewed the original ticket.

Well, I know better, it shouldn't have been there.  I have a latex-free system available at the moment, and I suspect #9074 could meet the same fate (I'll check shortly).

Thanks for the quick look at this one.

Rob



---

archive/issue_comments_093068.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-29T04:49:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9607#issuecomment-93068",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_093069.json:
```json
{
    "body": "I'll put the ticket number in the commit string before I make 4.5.2.rc0.",
    "created_at": "2010-07-29T05:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9607#issuecomment-93069",
    "user": "mpatel"
}
```

I'll put the ticket number in the commit string before I make 4.5.2.rc0.



---

archive/issue_comments_093070.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-07-29T06:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9607#issuecomment-93070",
    "user": "rbeezer"
}
```

Attachment



---

archive/issue_comments_093071.json:
```json
{
    "body": "Replying to [comment:8 mpatel]:\n> I'll put the ticket number in the commit string before I make 4.5.2.rc0.\n\nSorry!  New v2 patch has a real commit message, if it is not too late.",
    "created_at": "2010-07-29T06:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9607#issuecomment-93071",
    "user": "rbeezer"
}
```

Replying to [comment:8 mpatel]:
> I'll put the ticket number in the commit string before I make 4.5.2.rc0.

Sorry!  New v2 patch has a real commit message, if it is not too late.



---

archive/issue_comments_093072.json:
```json
{
    "body": "Replying to [comment:9 rbeezer]:\n> Replying to [comment:8 mpatel]:\n> > I'll put the ticket number in the commit string before I make 4.5.2.rc0.\n> Sorry!  New v2 patch has a real commit message, if it is not too late.\n\nNo problem.  I'm merging V2, instead.",
    "created_at": "2010-07-29T06:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9607#issuecomment-93072",
    "user": "mpatel"
}
```

Replying to [comment:9 rbeezer]:
> Replying to [comment:8 mpatel]:
> > I'll put the ticket number in the commit string before I make 4.5.2.rc0.
> Sorry!  New v2 patch has a real commit message, if it is not too late.

No problem.  I'm merging V2, instead.

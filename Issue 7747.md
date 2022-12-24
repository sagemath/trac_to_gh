# Issue 7747: miscellaneous documentation fixes

archive/issues_007747.json:
```json
{
    "body": "Assignee: mvngu\n\nWith Sage 4.3.rc0, I get a few doctest failures from sage/doc, at least one of which is related to #7406.  The attached patch fixes them.  It also reinstates some doctests which were disabled until #5338 was fixed.\n\nI'm marking this as a blocker since without it, there are doctest failures.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7747\n\n",
    "created_at": "2009-12-21T22:40:57Z",
    "labels": [
        "documentation",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "miscellaneous documentation fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7747",
    "user": "jhpalmieri"
}
```
Assignee: mvngu

With Sage 4.3.rc0, I get a few doctest failures from sage/doc, at least one of which is related to #7406.  The attached patch fixes them.  It also reinstates some doctests which were disabled until #5338 was fixed.

I'm marking this as a blocker since without it, there are doctest failures.

Issue created by migration from https://trac.sagemath.org/ticket/7747





---

archive/issue_comments_066687.json:
```json
{
    "body": "Attachment [trac_7747-doc.patch](tarball://root/attachments/some-uuid/ticket7747/trac_7747-doc.patch) by jhpalmieri created at 2009-12-21 22:41:29",
    "created_at": "2009-12-21T22:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7747#issuecomment-66687",
    "user": "jhpalmieri"
}
```

Attachment [trac_7747-doc.patch](tarball://root/attachments/some-uuid/ticket7747/trac_7747-doc.patch) by jhpalmieri created at 2009-12-21 22:41:29



---

archive/issue_comments_066688.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-21T22:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7747#issuecomment-66688",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066689.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-22T08:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7747#issuecomment-66689",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066690.json:
```json
{
    "body": "Doctesting Sage 4.3.rc0 on `sage.math` results in the following failures:\n\n```\nsage -t -long devel/sage/doc/en/constructions/calculus.rst\n**********************************************************************\nFile \"/scratch/mvngu/sandbox/sage-4.3.rc0-7747-doc/devel/sage-main/doc/en/constructions/calculus.rst\", line 29:\n    sage: latex(f.diff(x))\nExpected:\n    k x^{3} e^{k x} \\sin\\left(w x\\right) + w x^{3} e^{k x} \\cos\\left(w x\\right) + 3 \\, x^{2} e^{k x} \\sin\\left(w x\\right)\nGot:\n    k x^{3} e^{\\left(k x\\right)} \\sin\\left(w x\\right) + w x^{3} e^{\\left(k x\\right)} \\cos\\left(w x\\right) + 3 \\, x^{2} e^{\\left(k x\\right)} \\sin\\left(w x\\right)\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /tmp/mvngu/tmp/.doctest_calculus.py\n         [5.6 s]\n\nsage -t -long devel/sage/doc/en/bordeaux_2008/nf_introduction.rst\n**********************************************************************\nFile \"/scratch/mvngu/sandbox/sage-4.3.rc0-7747-doc/devel/sage-main/doc/en/bordeaux_2008/nf_introduction.rst\", line 300:\n    sage: latex(a)\nExpected:\n    -\\frac{1}{2} \\, {(I \\, \\sqrt{3} + 1)} ...\nGot:\n    -\\frac{1}{2} \\, {\\left(I \\, \\sqrt{3} + 1\\right)} {\\left(\\frac{1}{18} \\, \\sqrt{8 \\, \\sqrt{2} + 675} \\sqrt{3} - \\frac{5}{2}\\right)}^{\\left(\\frac{1}{3}\\right)} + \\frac{1}{6} \\, \\frac{{\\left(-I \\, \\sqrt{3} + 1\\right)} \\sqrt{2}\\\n}{{\\left(\\frac{1}{18} \\, \\sqrt{8 \\, \\sqrt{2} + 675} \\sqrt{3} - \\frac{5}{2}\\right)}^{\\left(\\frac{1}{3}\\right)}}\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_10\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /tmp/mvngu/tmp/.doctest_nf_introduction.py\n         [3.6 s]\n```\n\nThe patch `trac_7747-doc.patch` fixes both of these failures. All doctests now pass on sage.math.",
    "created_at": "2009-12-22T08:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7747#issuecomment-66690",
    "user": "mvngu"
}
```

Doctesting Sage 4.3.rc0 on `sage.math` results in the following failures:

```
sage -t -long devel/sage/doc/en/constructions/calculus.rst
**********************************************************************
File "/scratch/mvngu/sandbox/sage-4.3.rc0-7747-doc/devel/sage-main/doc/en/constructions/calculus.rst", line 29:
    sage: latex(f.diff(x))
Expected:
    k x^{3} e^{k x} \sin\left(w x\right) + w x^{3} e^{k x} \cos\left(w x\right) + 3 \, x^{2} e^{k x} \sin\left(w x\right)
Got:
    k x^{3} e^{\left(k x\right)} \sin\left(w x\right) + w x^{3} e^{\left(k x\right)} \cos\left(w x\right) + 3 \, x^{2} e^{\left(k x\right)} \sin\left(w x\right)
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /tmp/mvngu/tmp/.doctest_calculus.py
         [5.6 s]

sage -t -long devel/sage/doc/en/bordeaux_2008/nf_introduction.rst
**********************************************************************
File "/scratch/mvngu/sandbox/sage-4.3.rc0-7747-doc/devel/sage-main/doc/en/bordeaux_2008/nf_introduction.rst", line 300:
    sage: latex(a)
Expected:
    -\frac{1}{2} \, {(I \, \sqrt{3} + 1)} ...
Got:
    -\frac{1}{2} \, {\left(I \, \sqrt{3} + 1\right)} {\left(\frac{1}{18} \, \sqrt{8 \, \sqrt{2} + 675} \sqrt{3} - \frac{5}{2}\right)}^{\left(\frac{1}{3}\right)} + \frac{1}{6} \, \frac{{\left(-I \, \sqrt{3} + 1\right)} \sqrt{2}\
}{{\left(\frac{1}{18} \, \sqrt{8 \, \sqrt{2} + 675} \sqrt{3} - \frac{5}{2}\right)}^{\left(\frac{1}{3}\right)}}
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_10
***Test Failed*** 1 failures.
For whitespace errors, see the file /tmp/mvngu/tmp/.doctest_nf_introduction.py
         [3.6 s]
```

The patch `trac_7747-doc.patch` fixes both of these failures. All doctests now pass on sage.math.



---

archive/issue_comments_066691.json:
```json
{
    "body": "This is a duplicate of #7659, but the patch here does a little more.  Can we use this patch instead of that one?",
    "created_at": "2009-12-22T19:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7747#issuecomment-66691",
    "user": "jhpalmieri"
}
```

This is a duplicate of #7659, but the patch here does a little more.  Can we use this patch instead of that one?



---

archive/issue_comments_066692.json:
```json
{
    "body": "I've merged the patch here instead of the one at #7659.",
    "created_at": "2009-12-23T13:28:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7747#issuecomment-66692",
    "user": "mhansen"
}
```

I've merged the patch here instead of the one at #7659.



---

archive/issue_comments_066693.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-23T13:28:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7747#issuecomment-66693",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_066694.json:
```json
{
    "body": "Could you please make sure that burcin also gets author credit for this (for his work on #7659)?  Thanks.",
    "created_at": "2009-12-23T15:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7747#issuecomment-66694",
    "user": "jhpalmieri"
}
```

Could you please make sure that burcin also gets author credit for this (for his work on #7659)?  Thanks.



---

archive/issue_comments_066695.json:
```json
{
    "body": "Done.",
    "created_at": "2009-12-23T17:40:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7747#issuecomment-66695",
    "user": "mhansen"
}
```

Done.

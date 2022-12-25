# Issue 7604: Bug in continued fractions module (contfrac).  Patch attached

archive/issues_007604.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  solevillar@gmail.com\n\nKeywords: contfrac\n\nI've found this bug in the contfrac module:\n\n\n```\nsage: a=continued_fraction(sqrt(2))\nsage: a.qn(0)\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"_sage_input_4.py\", line 5, in <module>\n    a.qn(_sage_const_0 )\n  File \"\", line 1, in <module>\n    \n  File \"/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/contfrac.py\", line 461, in qn\n    if len(self.__qn) < n+3:\nAttributeError: 'ContinuedFraction' object has no attribute '_ContinuedFraction__qn'\n```\n\n\nBut this actually works:\n\n```\nsage: a=continued_fraction(sqrt(2))\nsage: b=a.pn(0)\nsage: a.qn(0)\n1\n```\n\n\n\nThat's because the method contfrac.pn initializes the attributes pn and qn so if you call contfrac.qn before calling contfrac.pn the attribute qn wont be initialized and that's why it doesn't work in the first snippet.\n\nI wrote a patch that solves this problem (minor changes, very easy to solve). I'm attaching that patch.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7604\n\n",
    "created_at": "2009-12-04T16:37:52Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Bug in continued fractions module (contfrac).  Patch attached",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7604",
    "user": "https://trac.sagemath.org/admin/accounts/users/solevillar"
}
```
Assignee: @aghitza

CC:  solevillar@gmail.com

Keywords: contfrac

I've found this bug in the contfrac module:


```
sage: a=continued_fraction(sqrt(2))
sage: a.qn(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_4.py", line 5, in <module>
    a.qn(_sage_const_0 )
  File "", line 1, in <module>
    
  File "/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/contfrac.py", line 461, in qn
    if len(self.__qn) < n+3:
AttributeError: 'ContinuedFraction' object has no attribute '_ContinuedFraction__qn'
```


But this actually works:

```
sage: a=continued_fraction(sqrt(2))
sage: b=a.pn(0)
sage: a.qn(0)
1
```



That's because the method contfrac.pn initializes the attributes pn and qn so if you call contfrac.qn before calling contfrac.pn the attribute qn wont be initialized and that's why it doesn't work in the first snippet.

I wrote a patch that solves this problem (minor changes, very easy to solve). I'm attaching that patch.


Issue created by migration from https://trac.sagemath.org/ticket/7604





---

archive/issue_comments_064758.json:
```json
{
    "body": "patch for contfrac module",
    "created_at": "2009-12-04T16:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7604#issuecomment-64758",
    "user": "https://trac.sagemath.org/admin/accounts/users/solevillar"
}
```

patch for contfrac module



---

archive/issue_comments_064759.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-04T16:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7604#issuecomment-64759",
    "user": "https://trac.sagemath.org/admin/accounts/users/solevillar"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064760.json:
```json
{
    "body": "Attachment [contfrac.py](tarball://root/attachments/some-uuid/ticket7604/contfrac.py) by solevillar created at 2009-12-04 16:42:14",
    "created_at": "2009-12-04T16:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7604#issuecomment-64760",
    "user": "https://trac.sagemath.org/admin/accounts/users/solevillar"
}
```

Attachment [contfrac.py](tarball://root/attachments/some-uuid/ticket7604/contfrac.py) by solevillar created at 2009-12-04 16:42:14



---

archive/issue_comments_064761.json:
```json
{
    "body": "There are several problems:\n\n1.  The attachment is not actually a patch but a new version of the `contfrac.py` file.\n\n2.  The change to `is_field` to remove the optional parameter `proof=True` is unhelpful since every other instance of `is_field` has the argument proof, and Sage contains code which uses this argument and will crash without it.\n\n3.  At lines 456-457 the line n = ZZ(n) has been duplicated.  In fact this line is not needed at all.\n\n4.  The correction of the bug is a bit more complicated than necessary.\n\nI have attached a patch which deals with the bug, and have made a minor change to a doctest so that it would have detected the bug.",
    "created_at": "2009-12-05T12:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7604#issuecomment-64761",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

There are several problems:

1.  The attachment is not actually a patch but a new version of the `contfrac.py` file.

2.  The change to `is_field` to remove the optional parameter `proof=True` is unhelpful since every other instance of `is_field` has the argument proof, and Sage contains code which uses this argument and will crash without it.

3.  At lines 456-457 the line n = ZZ(n) has been duplicated.  In fact this line is not needed at all.

4.  The correction of the bug is a bit more complicated than necessary.

I have attached a patch which deals with the bug, and have made a minor change to a doctest so that it would have detected the bug.



---

archive/issue_comments_064762.json:
```json
{
    "body": "Use instead",
    "created_at": "2009-12-05T12:49:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7604#issuecomment-64762",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Use instead



---

archive/issue_comments_064763.json:
```json
{
    "body": "Attachment [trac_7604.patch](tarball://root/attachments/some-uuid/ticket7604/trac_7604.patch) by @mwhansen created at 2009-12-07 08:12:11\n\nLooks good to me.\n\nsolevillar`@`gmail.com, could we get your name for the release notes?  Or, you could updated the Authors field on this ticket.  Thanks!",
    "created_at": "2009-12-07T08:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7604#issuecomment-64763",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7604.patch](tarball://root/attachments/some-uuid/ticket7604/trac_7604.patch) by @mwhansen created at 2009-12-07 08:12:11

Looks good to me.

solevillar`@`gmail.com, could we get your name for the release notes?  Or, you could updated the Authors field on this ticket.  Thanks!



---

archive/issue_comments_064764.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-07T08:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7604#issuecomment-64764",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed

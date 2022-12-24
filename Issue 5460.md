# Issue 5460: [with patch, needs review] deprecate 'invert' in matrix_rational_dense

archive/issues_005460.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nSee [this thread on sage-devel](http://groups.google.com/group/sage-support/browse_frm/thread/215ae58d5a3e900f).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5460\n\n",
    "created_at": "2009-03-09T20:17:51Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] deprecate 'invert' in matrix_rational_dense",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5460",
    "user": "@jhpalmieri"
}
```
Assignee: @jhpalmieri

See [this thread on sage-devel](http://groups.google.com/group/sage-support/browse_frm/thread/215ae58d5a3e900f).


Issue created by migration from https://trac.sagemath.org/ticket/5460





---

archive/issue_comments_042396.json:
```json
{
    "body": "Replying to [ticket:5460 jhpalmieri]:\nI get the deprecation warning with a singular matrix, but not with a nonsingular matrix.  Is this the desired/expected behavior?  Otherwise, it looks good, passed tests, etc.\n\n\n\n```\nsage: a=matrix(QQ, [[1,2],[3,6]])\nsage: a.invert()\n/opt/sage-dev/local/lib/python2.5/site-packages/IPython/iplib.py:2073: DeprecationWarning: 'invert' is deprecated; use 'inverse' instead.\n  exec code_obj in self.user_global_ns, self.user_ns\n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last)\n<snip>\n```\n\n\n\n```\nsage: b=matrix(QQ, [[1,2],[3,7]])\nsage: b.invert()\n\n[ 7 -2]\n[-3  1]\n```\n\n\n\n```",
    "created_at": "2009-03-10T04:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5460#issuecomment-42396",
    "user": "@rbeezer"
}
```

Replying to [ticket:5460 jhpalmieri]:
I get the deprecation warning with a singular matrix, but not with a nonsingular matrix.  Is this the desired/expected behavior?  Otherwise, it looks good, passed tests, etc.



```
sage: a=matrix(QQ, [[1,2],[3,6]])
sage: a.invert()
/opt/sage-dev/local/lib/python2.5/site-packages/IPython/iplib.py:2073: DeprecationWarning: 'invert' is deprecated; use 'inverse' instead.
  exec code_obj in self.user_global_ns, self.user_ns
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<snip>
```



```
sage: b=matrix(QQ, [[1,2],[3,7]])
sage: b.invert()

[ 7 -2]
[-3  1]
```



```



---

archive/issue_comments_042397.json:
```json
{
    "body": "As far as I can tell, the deprecation function produces a warning message the first time you use the deprecated code, but not after that.  If you restart Sage and try the nonsingular matrix, you should get a warning for that one, too.",
    "created_at": "2009-03-10T04:26:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5460#issuecomment-42397",
    "user": "@jhpalmieri"
}
```

As far as I can tell, the deprecation function produces a warning message the first time you use the deprecated code, but not after that.  If you restart Sage and try the nonsingular matrix, you should get a warning for that one, too.



---

archive/issue_comments_042398.json:
```json
{
    "body": "Replying to [comment:2 jhpalmieri]:\nRight.  I tested it twice, with a restart inbetween, but both times in the same order.  ;-)\n\nLooks ready to go.",
    "created_at": "2009-03-10T04:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5460#issuecomment-42398",
    "user": "@rbeezer"
}
```

Replying to [comment:2 jhpalmieri]:
Right.  I tested it twice, with a restart inbetween, but both times in the same order.  ;-)

Looks ready to go.



---

archive/issue_comments_042399.json:
```json
{
    "body": "Good work!\n\nDo the doctests pass for the invert function?  If so, I'm surprised; I thought that the doctest output would have to include the deprecation statement.\n\nRegardless, the documentation for the invert function should include a sentence about the deprecation too.\n\nPositive review (based on rbeezer's positive review) pending the changes to documentation and possibly doctests mentioned above.",
    "created_at": "2009-03-10T09:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5460#issuecomment-42399",
    "user": "@jasongrout"
}
```

Good work!

Do the doctests pass for the invert function?  If so, I'm surprised; I thought that the doctest output would have to include the deprecation statement.

Regardless, the documentation for the invert function should include a sentence about the deprecation too.

Positive review (based on rbeezer's positive review) pending the changes to documentation and possibly doctests mentioned above.



---

archive/issue_comments_042400.json:
```json
{
    "body": "Replying to [comment:4 jason]:\n\n> Do the doctests pass for the invert function?  If so, I'm surprised; I thought that the doctest output would have to include the deprecation statement.\n\nI'd have assumed the same.  But doctests on the one source file passed, and  `sage -testall` only gave spurious unrelated errors in one file, and I'd seen those recently, so they should be unrelated.",
    "created_at": "2009-03-10T14:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5460#issuecomment-42400",
    "user": "@rbeezer"
}
```

Replying to [comment:4 jason]:

> Do the doctests pass for the invert function?  If so, I'm surprised; I thought that the doctest output would have to include the deprecation statement.

I'd have assumed the same.  But doctests on the one source file passed, and  `sage -testall` only gave spurious unrelated errors in one file, and I'd seen those recently, so they should be unrelated.



---

archive/issue_comments_042401.json:
```json
{
    "body": "The one doctest involves a Traceback and \"...\", and I'm guessing that the \"...\" captures the deprecation error.  I agree, we should add a comment about deprecation to the documentation, and I'll get to that later today.",
    "created_at": "2009-03-10T15:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5460#issuecomment-42401",
    "user": "@jhpalmieri"
}
```

The one doctest involves a Traceback and "...", and I'm guessing that the "..." captures the deprecation error.  I agree, we should add a comment about deprecation to the documentation, and I'll get to that later today.



---

archive/issue_comments_042402.json:
```json
{
    "body": "Attachment [deprecate-invert.patch](tarball://root/attachments/some-uuid/ticket5460/deprecate-invert.patch) by @jhpalmieri created at 2009-03-10 18:43:45\n\nHere's a new patch; the only difference is the documentation for 'invert'.",
    "created_at": "2009-03-10T18:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5460#issuecomment-42402",
    "user": "@jhpalmieri"
}
```

Attachment [deprecate-invert.patch](tarball://root/attachments/some-uuid/ticket5460/deprecate-invert.patch) by @jhpalmieri created at 2009-03-10 18:43:45

Here's a new patch; the only difference is the documentation for 'invert'.



---

archive/issue_comments_042403.json:
```json
{
    "body": "Replying to [comment:7 jhpalmieri]:\n> Here's a new patch; the only difference is the documentation for 'invert'.\n\nLooks like its all ready now.",
    "created_at": "2009-03-10T19:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5460#issuecomment-42403",
    "user": "@rbeezer"
}
```

Replying to [comment:7 jhpalmieri]:
> Here's a new patch; the only difference is the documentation for 'invert'.

Looks like its all ready now.



---

archive/issue_comments_042404.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-23T21:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5460#issuecomment-42404",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_042405.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-23T21:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5460",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5460#issuecomment-42405",
    "user": "mabshoff"
}
```

Resolution: fixed

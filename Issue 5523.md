# Issue 5523: [with patch, positive review] odd primary steenrod algebra fixes

archive/issues_005523.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nI'm attaching a patch to this and also giving it a positive review.  Here's why:\n\nCharlie Odenthal (University of Toledo) sent email to me saying that he had found a few bugs in the Steenrod algebra component of Sage, and he sent me new .py files fixing the bugs. I tested his fixes, and had they been submitted as a patch file for a ticket, I would have given them a mostly positive review.  I fixed a few bugs in his new code, added some doctests, and cleaned up one thing.  Then I sent the results back to him, and he said that he was happy with my changes.  I'm attaching a patch containing our combined work, although he should get the credit, and my work should be viewed as a reviewer's patch.\n\nI suppose I should describe the problems: computing antipodes in the odd primary Steenrod algebra was giving the wrong answers for some elements (because I had implemented it incorrectly) and was very slow for some other elements (because of the choice of algorithm).  Also, some elements which should have been equal weren't (because of a bug in multiplication).  These have now all been fixed, with doctests demonstrating that.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5523\n\n",
    "created_at": "2009-03-15T03:16:30Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, positive review] odd primary steenrod algebra fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5523",
    "user": "@jhpalmieri"
}
```
Assignee: @jhpalmieri

I'm attaching a patch to this and also giving it a positive review.  Here's why:

Charlie Odenthal (University of Toledo) sent email to me saying that he had found a few bugs in the Steenrod algebra component of Sage, and he sent me new .py files fixing the bugs. I tested his fixes, and had they been submitted as a patch file for a ticket, I would have given them a mostly positive review.  I fixed a few bugs in his new code, added some doctests, and cleaned up one thing.  Then I sent the results back to him, and he said that he was happy with my changes.  I'm attaching a patch containing our combined work, although he should get the credit, and my work should be viewed as a reviewer's patch.

I suppose I should describe the problems: computing antipodes in the odd primary Steenrod algebra was giving the wrong answers for some elements (because I had implemented it incorrectly) and was very slow for some other elements (because of the choice of algorithm).  Also, some elements which should have been equal weren't (because of a bug in multiplication).  These have now all been fixed, with doctests demonstrating that.


Issue created by migration from https://trac.sagemath.org/ticket/5523





---

archive/issue_comments_042973.json:
```json
{
    "body": "Attachment [steenrod_odd.patch](tarball://root/attachments/some-uuid/ticket5523/steenrod_odd.patch) by @jhpalmieri created at 2009-03-15 03:16:42",
    "created_at": "2009-03-15T03:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5523#issuecomment-42973",
    "user": "@jhpalmieri"
}
```

Attachment [steenrod_odd.patch](tarball://root/attachments/some-uuid/ticket5523/steenrod_odd.patch) by @jhpalmieri created at 2009-03-15 03:16:42



---

archive/issue_comments_042974.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-25T08:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5523#issuecomment-42974",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_042975.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T08:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5523#issuecomment-42975",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael

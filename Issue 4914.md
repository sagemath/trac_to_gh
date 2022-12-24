# Issue 4914: convert sage.groups.* docstrings to Sphinx

archive/issues_004914.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4914\n\n",
    "created_at": "2009-01-01T22:52:03Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "convert sage.groups.* docstrings to Sphinx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4914",
    "user": "@mwhansen"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/4914





---

archive/issue_comments_037288.json:
```json
{
    "body": "Attachment [trac_4914.patch](tarball://root/attachments/some-uuid/ticket4914/trac_4914.patch) by @mwhansen created at 2009-01-02 02:54:31",
    "created_at": "2009-01-02T02:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4914#issuecomment-37288",
    "user": "@mwhansen"
}
```

Attachment [trac_4914.patch](tarball://root/attachments/some-uuid/ticket4914/trac_4914.patch) by @mwhansen created at 2009-01-02 02:54:31



---

archive/issue_comments_037289.json:
```json
{
    "body": "(1) This does not implement the docstring changes in\nhttp://trac.sagemath.org/sage_trac/ticket/3749\n\n(2) The only conversion problem is see is \n\n* in abelian_group:\n\n\n```\n \t129\t- [C2] ----, A course in computational algebraic number theory, \n \t130\t  Springer, 1996. [R] J. Rotman, An introduction to the theory of \n \t131\t  groups, 4th ed, Springer, 1995. \n \t132\t \n```\n\nshould be\n\n\n```\n \t129\t- [C2] ----, A course in computational algebraic number theory, \n \t130\t  Springer, 1996. \n        131       [R] J. Rotman, An introduction to the theory of \n \t132\t  groups, 4th ed, Springer, 1995. \n \t133\n```\n\n\t \n(3) What is the purpose of linear.py?? (Open a separate trac ticket?)",
    "created_at": "2009-01-02T11:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4914#issuecomment-37289",
    "user": "@wdjoyner"
}
```

(1) This does not implement the docstring changes in
http://trac.sagemath.org/sage_trac/ticket/3749

(2) The only conversion problem is see is 

* in abelian_group:


```
 	129	- [C2] ----, A course in computational algebraic number theory, 
 	130	  Springer, 1996. [R] J. Rotman, An introduction to the theory of 
 	131	  groups, 4th ed, Springer, 1995. 
 	132	 
```

should be


```
 	129	- [C2] ----, A course in computational algebraic number theory, 
 	130	  Springer, 1996. 
        131       [R] J. Rotman, An introduction to the theory of 
 	132	  groups, 4th ed, Springer, 1995. 
 	133
```

	 
(3) What is the purpose of linear.py?? (Open a separate trac ticket?)



---

archive/issue_comments_037290.json:
```json
{
    "body": "Regarding (1), those changes haven't been merged into Sage.\n\nI'll post a patch for (2).\n\nFor (3), I think all of the linear groups stuff was there before they got moved out into their own files.",
    "created_at": "2009-01-02T20:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4914#issuecomment-37290",
    "user": "@mwhansen"
}
```

Regarding (1), those changes haven't been merged into Sage.

I'll post a patch for (2).

For (3), I think all of the linear groups stuff was there before they got moved out into their own files.



---

archive/issue_comments_037291.json:
```json
{
    "body": "Attachment [trac_4914-2.patch](tarball://root/attachments/some-uuid/ticket4914/trac_4914-2.patch) by @mwhansen created at 2009-01-02 20:25:47",
    "created_at": "2009-01-02T20:25:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4914#issuecomment-37291",
    "user": "@mwhansen"
}
```

Attachment [trac_4914-2.patch](tarball://root/attachments/some-uuid/ticket4914/trac_4914-2.patch) by @mwhansen created at 2009-01-02 20:25:47



---

archive/issue_comments_037292.json:
```json
{
    "body": "Replying to [comment:3 mhansen]:\n> Regarding (1), those changes haven't been merged into Sage.\n\nYes, anything not in Sage will likely need to be rebased. The fast that the ReST conversion is coming has been known for *many weeks* and was mentioned numerous times on sage-devel.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-02T20:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4914#issuecomment-37292",
    "user": "mabshoff"
}
```

Replying to [comment:3 mhansen]:
> Regarding (1), those changes haven't been merged into Sage.

Yes, anything not in Sage will likely need to be rebased. The fast that the ReST conversion is coming has been known for *many weeks* and was mentioned numerous times on sage-devel.

Cheers,

Michael



---

archive/issue_comments_037293.json:
```json
{
    "body": "That being said, I'll make a signup list for people who would like new files converted over / patches to be rebased to help ease the transition.",
    "created_at": "2009-01-02T20:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4914#issuecomment-37293",
    "user": "@mwhansen"
}
```

That being said, I'll make a signup list for people who would like new files converted over / patches to be rebased to help ease the transition.



---

archive/issue_comments_037294.json:
```json
{
    "body": "Replying to [comment:5 mhansen]:\n> That being said, I'll make a signup list for people who would like new files converted over / patches to be rebased to help ease the transition.\n\nAbsolutely, but given the wide publicity this received no one can reading sage-devel can claim to be surprised by this. And this shows exactly why people need to be behind their patches to get them reviewed so that they don't bitrot.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-02T20:40:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4914#issuecomment-37294",
    "user": "mabshoff"
}
```

Replying to [comment:5 mhansen]:
> That being said, I'll make a signup list for people who would like new files converted over / patches to be rebased to help ease the transition.

Absolutely, but given the wide publicity this received no one can reading sage-devel can claim to be surprised by this. And this shows exactly why people need to be behind their patches to get them reviewed so that they don't bitrot.

Cheers,

Michael



---

archive/issue_comments_037295.json:
```json
{
    "body": "Re: http://trac.sagemath.org/sage_trac/ticket/3749\n\nIt was my fault. I posted the patch following the referee's suggestions but simply forgot to relabel the ticket \"needs review\".",
    "created_at": "2009-01-02T20:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4914#issuecomment-37295",
    "user": "@wdjoyner"
}
```

Re: http://trac.sagemath.org/sage_trac/ticket/3749

It was my fault. I posted the patch following the referee's suggestions but simply forgot to relabel the ticket "needs review".



---

archive/issue_comments_037296.json:
```json
{
    "body": "Attachment [latex-fix-4914.patch](tarball://root/attachments/some-uuid/ticket4914/latex-fix-4914.patch) by cwitty created at 2009-01-23 08:11:40\n\nlatex-fix-4914.patch is a one-character change that's necessary to allow generation of the PDF docs.  Note that this is not in any way a review of the original patch; I haven't even looked at it.",
    "created_at": "2009-01-23T08:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4914#issuecomment-37296",
    "user": "cwitty"
}
```

Attachment [latex-fix-4914.patch](tarball://root/attachments/some-uuid/ticket4914/latex-fix-4914.patch) by cwitty created at 2009-01-23 08:11:40

latex-fix-4914.patch is a one-character change that's necessary to allow generation of the PDF docs.  Note that this is not in any way a review of the original patch; I haven't even looked at it.



---

archive/issue_comments_037297.json:
```json
{
    "body": "For the purpose of review, could you post somewhere the output of the html and/or pdf after all the patches are applied, please?",
    "created_at": "2009-01-24T16:40:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4914#issuecomment-37297",
    "user": "@wdjoyner"
}
```

For the purpose of review, could you post somewhere the output of the html and/or pdf after all the patches are applied, please?



---

archive/issue_comments_037298.json:
```json
{
    "body": "You can find them\n\nhttp://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/\n\nand \n\nhttp://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/pdf/en/reference/",
    "created_at": "2009-01-25T02:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4914#issuecomment-37298",
    "user": "@mwhansen"
}
```

You can find them

http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/

and 

http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/pdf/en/reference/



---

archive/issue_comments_037299.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-25T02:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4914#issuecomment-37299",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_037300.json:
```json
{
    "body": "Changing assignee from tba to @mwhansen.",
    "created_at": "2009-01-25T02:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4914#issuecomment-37300",
    "user": "@mwhansen"
}
```

Changing assignee from tba to @mwhansen.



---

archive/issue_comments_037301.json:
```json
{
    "body": "Thank you.\n\nLooks good to me!",
    "created_at": "2009-01-25T04:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4914#issuecomment-37301",
    "user": "@wdjoyner"
}
```

Thank you.

Looks good to me!



---

archive/issue_comments_037302.json:
```json
{
    "body": "Attachment [sage.groups-final.patch](tarball://root/attachments/some-uuid/ticket4914/sage.groups-final.patch) by mabshoff created at 2009-02-24 18:47:00\n\nMerged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T18:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4914#issuecomment-37302",
    "user": "mabshoff"
}
```

Attachment [sage.groups-final.patch](tarball://root/attachments/some-uuid/ticket4914/sage.groups-final.patch) by mabshoff created at 2009-02-24 18:47:00

Merged in Sage 3.4.alpha0.

Cheers,

Michael



---

archive/issue_comments_037303.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T18:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4914#issuecomment-37303",
    "user": "mabshoff"
}
```

Resolution: fixed

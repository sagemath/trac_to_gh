# Issue 5541: [with patch, positive review] more formatting fixes for quaternion_algebra.py docstring

archive/issues_005541.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: quaternion_algebra.py, sphinx, docstring\n\nWhile reviewing ticket #5531 I noticed some further formatting issues in the docstring of `quaternion_algebra.py`. The objective is to make the docstring of that module look even prettier.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5541\n\n",
    "closed_at": "2009-04-18T01:07:43Z",
    "created_at": "2009-03-17T03:43:08Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, positive review] more formatting fixes for quaternion_algebra.py docstring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5541",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tba

Keywords: quaternion_algebra.py, sphinx, docstring

While reviewing ticket #5531 I noticed some further formatting issues in the docstring of `quaternion_algebra.py`. The objective is to make the docstring of that module look even prettier.

Issue created by migration from https://trac.sagemath.org/ticket/5541





---

archive/issue_comments_043020.json:
```json
{
    "body": "Make quaternion_algebra.py more prettier",
    "created_at": "2009-03-17T04:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43020",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Make quaternion_algebra.py more prettier



---

archive/issue_comments_043021.json:
```json
{
    "body": "Attachment [trac_5541-docstring-fixes.patch](tarball://root/attachments/some-uuid/ticket5541/trac_5541-docstring-fixes.patch) by mvngu created at 2009-03-17 04:46:39\n\nThe patch **trac_5541-docstring-fixes.patch** fixes some more docstring formatting problems in `sage/algebras/quaternion_algebra.py`. It also resolves this indentation warning:\n\n```\nWARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.\n```\nwhich I received after applying the patch for ticket #5531 and building the reference manual.",
    "created_at": "2009-03-17T04:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43021",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_5541-docstring-fixes.patch](tarball://root/attachments/some-uuid/ticket5541/trac_5541-docstring-fixes.patch) by mvngu created at 2009-03-17 04:46:39

The patch **trac_5541-docstring-fixes.patch** fixes some more docstring formatting problems in `sage/algebras/quaternion_algebra.py`. It also resolves this indentation warning:

```
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
```
which I received after applying the patch for ticket #5531 and building the reference manual.



---

archive/issue_comments_043022.json:
```json
{
    "body": "I should mention that this ticket depends on #5531.",
    "created_at": "2009-03-17T04:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43022",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I should mention that this ticket depends on #5531.



---

archive/issue_comments_043023.json:
```json
{
    "body": "Looks good to me except for two very minor issues, which are taken care of in the referee's patch.\n\n(By the way, see #5632 for a somewhat related ticket.)",
    "created_at": "2009-03-29T16:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43023",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me except for two very minor issues, which are taken care of in the referee's patch.

(By the way, see #5632 for a somewhat related ticket.)



---

archive/issue_comments_043024.json:
```json
{
    "body": "Attachment [5541-referee.patch](tarball://root/attachments/some-uuid/ticket5541/5541-referee.patch) by @jhpalmieri created at 2009-03-29 16:27:32",
    "created_at": "2009-03-29T16:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43024",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [5541-referee.patch](tarball://root/attachments/some-uuid/ticket5541/5541-referee.patch) by @jhpalmieri created at 2009-03-29 16:27:32



---

archive/issue_comments_043025.json:
```json
{
    "body": "Replying to [comment:3 jhpalmieri]:\n> Looks good to me except for two very minor issues, which are taken care of in the referee's patch.\n\n\n\nYep, looks good to me. Thanks for pointing that out.",
    "created_at": "2009-03-30T06:34:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43025",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:3 jhpalmieri]:
> Looks good to me except for two very minor issues, which are taken care of in the referee's patch.



Yep, looks good to me. Thanks for pointing that out.



---

archive/issue_comments_043026.json:
```json
{
    "body": "This patch needs to be rebased due to #5520:\n\n```\nsage-3.4.1.rc0/devel/sage$ patch -p1 --dry-run < trac_5541-docstring-fixes.patch \npatching file sage/algebras/quatalg/quaternion_algebra.py\nHunk #1 FAILED at 58.\nHunk #2 succeeded at 101 (offset 6 lines).\nHunk #3 FAILED at 125.\nHunk #4 succeeded at 152 (offset 6 lines).\nHunk #5 succeeded at 183 (offset 6 lines).\nHunk #6 succeeded at 195 (offset 6 lines).\nHunk #7 FAILED at 203.\nHunk #8 succeeded at 228 (offset 6 lines).\nHunk #9 succeeded at 242 (offset 6 lines).\nHunk #10 succeeded at 255 (offset 6 lines).\nHunk #11 succeeded at 268 (offset 6 lines).\nHunk #12 succeeded at 296 (offset 6 lines).\nHunk #13 succeeded at 305 (offset 6 lines).\nHunk #14 succeeded at 326 (offset 6 lines).\nHunk #15 succeeded at 348 (offset 6 lines).\nHunk #16 succeeded at 366 (offset 6 lines).\nHunk #17 succeeded at 379 (offset 6 lines).\nHunk #18 succeeded at 397 (offset 6 lines).\nHunk #19 succeeded at 424 (offset 6 lines).\nHunk #20 succeeded at 436 (offset 6 lines).\nHunk #21 succeeded at 454 (offset 6 lines).\nHunk #22 succeeded at 463 (offset 6 lines).\nHunk #23 succeeded at 476 (offset 6 lines).\nHunk #24 succeeded at 486 (offset 5 lines).\nHunk #25 succeeded at 518 (offset 5 lines).\nHunk #26 succeeded at 569 (offset 25 lines).\nHunk #27 succeeded at 606 (offset 43 lines).\nHunk #28 succeeded at 623 (offset 43 lines).\nHunk #29 succeeded at 640 with fuzz 1 (offset 43 lines).\nHunk #30 succeeded at 657 (offset 43 lines).\nHunk #31 succeeded at 683 (offset 43 lines).\nHunk #32 succeeded at 694 (offset 43 lines).\nHunk #33 FAILED at 742.\n4 out of 33 hunks FAILED -- saving rejects to file sage/algebras/quatalg/quaternion_algebra.py.rej\n```\nNote that the file has moved from sage/algebras to sage/algebras/quatalg\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T07:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43026",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch needs to be rebased due to #5520:

```
sage-3.4.1.rc0/devel/sage$ patch -p1 --dry-run < trac_5541-docstring-fixes.patch 
patching file sage/algebras/quatalg/quaternion_algebra.py
Hunk #1 FAILED at 58.
Hunk #2 succeeded at 101 (offset 6 lines).
Hunk #3 FAILED at 125.
Hunk #4 succeeded at 152 (offset 6 lines).
Hunk #5 succeeded at 183 (offset 6 lines).
Hunk #6 succeeded at 195 (offset 6 lines).
Hunk #7 FAILED at 203.
Hunk #8 succeeded at 228 (offset 6 lines).
Hunk #9 succeeded at 242 (offset 6 lines).
Hunk #10 succeeded at 255 (offset 6 lines).
Hunk #11 succeeded at 268 (offset 6 lines).
Hunk #12 succeeded at 296 (offset 6 lines).
Hunk #13 succeeded at 305 (offset 6 lines).
Hunk #14 succeeded at 326 (offset 6 lines).
Hunk #15 succeeded at 348 (offset 6 lines).
Hunk #16 succeeded at 366 (offset 6 lines).
Hunk #17 succeeded at 379 (offset 6 lines).
Hunk #18 succeeded at 397 (offset 6 lines).
Hunk #19 succeeded at 424 (offset 6 lines).
Hunk #20 succeeded at 436 (offset 6 lines).
Hunk #21 succeeded at 454 (offset 6 lines).
Hunk #22 succeeded at 463 (offset 6 lines).
Hunk #23 succeeded at 476 (offset 6 lines).
Hunk #24 succeeded at 486 (offset 5 lines).
Hunk #25 succeeded at 518 (offset 5 lines).
Hunk #26 succeeded at 569 (offset 25 lines).
Hunk #27 succeeded at 606 (offset 43 lines).
Hunk #28 succeeded at 623 (offset 43 lines).
Hunk #29 succeeded at 640 with fuzz 1 (offset 43 lines).
Hunk #30 succeeded at 657 (offset 43 lines).
Hunk #31 succeeded at 683 (offset 43 lines).
Hunk #32 succeeded at 694 (offset 43 lines).
Hunk #33 FAILED at 742.
4 out of 33 hunks FAILED -- saving rejects to file sage/algebras/quatalg/quaternion_algebra.py.rej
```
Note that the file has moved from sage/algebras to sage/algebras/quatalg

Cheers,

Michael



---

archive/issue_comments_043027.json:
```json
{
    "body": "Please see [my most recent comment on #5632](http://trac.sagemath.org/sage_trac/ticket/5632#comment:6) for a reference manual issue which is also relevant here.",
    "created_at": "2009-03-31T15:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43027",
    "user": "https://github.com/jhpalmieri"
}
```

Please see [my most recent comment on #5632](http://trac.sagemath.org/sage_trac/ticket/5632#comment:6) for a reference manual issue which is also relevant here.



---

archive/issue_comments_043028.json:
```json
{
    "body": "Here's a rebased version, plus more.  This includes all of mvngu's work, so he should obviously get a lot of credit for this; this covers the file up to line 700 or so. #5520 added a lot of code to this file with many of the same issues, so starting at line 741, there are new fixes.",
    "created_at": "2009-04-01T02:54:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43028",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a rebased version, plus more.  This includes all of mvngu's work, so he should obviously get a lot of credit for this; this covers the file up to line 700 or so. #5520 added a lot of code to this file with many of the same issues, so starting at line 741, there are new fixes.



---

archive/issue_comments_043029.json:
```json
{
    "body": "Attachment [5541-rebased.patch](tarball://root/attachments/some-uuid/ticket5541/5541-rebased.patch) by @jhpalmieri created at 2009-04-01 02:55:19\n\n(this replaces both of the earlier patches)",
    "created_at": "2009-04-01T02:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43029",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [5541-rebased.patch](tarball://root/attachments/some-uuid/ticket5541/5541-rebased.patch) by @jhpalmieri created at 2009-04-01 02:55:19

(this replaces both of the earlier patches)



---

archive/issue_comments_043030.json:
```json
{
    "body": "mvngu: the first half of my patch is just a rebased version of yours, and it already has a positive review.  If you are willing to review the second half, then that should do it for this ticket.",
    "created_at": "2009-04-05T22:48:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43030",
    "user": "https://github.com/jhpalmieri"
}
```

mvngu: the first half of my patch is just a rebased version of yours, and it already has a positive review.  If you are willing to review the second half, then that should do it for this ticket.



---

archive/issue_comments_043031.json:
```json
{
    "body": "Replying to [comment:8 jhpalmieri]:\n> mvngu: the first half of my patch is just a rebased version of yours, and it already has a positive review.  If you are willing to review the second half, then that should do it for this ticket.\n\n\n\njhpalmieri: I've read through the rebased patch. But I also want to (re)build at least the HTML version of the reference to make sure that the rebased patch fixes the problems it claims to fix. I'll give this patch a formal review sometime today.",
    "created_at": "2009-04-05T23:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43031",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:8 jhpalmieri]:
> mvngu: the first half of my patch is just a rebased version of yours, and it already has a positive review.  If you are willing to review the second half, then that should do it for this ticket.



jhpalmieri: I've read through the rebased patch. But I also want to (re)build at least the HTML version of the reference to make sure that the rebased patch fixes the problems it claims to fix. I'll give this patch a formal review sometime today.



---

archive/issue_comments_043032.json:
```json
{
    "body": "REFEREE REPORT:\n\n\n\nThe following lines result in something weird when viewing the HTML version of the reference manual:\n\n```\n486\tclass QuaternionAlgebra_ab(QuaternionAlgebra_abstract): \n487\t    \"\"\" \n488\t    The quaternion algebra of the form `(a, b/K)`, where `i^2=a`, `j^2 = b`, \n489\t    and `j*i = -i*j`.  ``K`` is a field not of characteristic 2 and ``a``, \n490\t    ``b`` are nonzero elements of ``K``. \n491\t \n492\t    EXAMPLES:: \n493\t \n494\t    \"\"\" \n495\t    def __init__(self, base_ring, a, b, names='i,j,k'):\n```\nSee the [HTML version](http://sage.math.washington.edu/home/mvngu/reference/sage/algebras/quatalg/quaternion_algebra.html#sage.algebras.quatalg.quaternion_algebra.QuaternionAlgebra_ab) I've generated after applying the rebased patch. I think the problem is that there's a \"EXAMPLES::\" tag, which is not followed by any examples at all. Now by alphabetic order, the method `sage.algebras.quatalg.quaternion_algebra.QuaternionAlgebra_ab.QuaternionAlgebra_ab.discriminant()` is thus formatted in a weird way as\n\n```\n.. method:: QuaternionAlgebra_ab.discriminant()\n```\nin the HTML version.\n\n\n\nHow about some documentation for \n\n```\n627\t    def gen(self, i=0):\n```\nto explain what it does. At the moment, there are examples, but no explanation of what this method is supposed to do.\n\n\n\nI think the maths expression in the following lines are typeset in a weird way:\n\n```\n1069\t    def discriminant(self): \n1070\t        r\"\"\" \n1071\t        Return the discriminant of this order, which we define as \n1046\t \t        $\\sqrt( det ( Tr(e_i \\bar(e_j) ) ) )$, where $\\{e_i\\}$ is the \n1072\t        `\\sqrt( det ( Tr(e_i \\bar(e_j) ) ) )`, where `\\{e_i\\}` is the \n1073\n```\nSee the [HTML version](http://sage.math.washington.edu/home/mvngu/reference/sage/algebras/quatalg/quaternion_algebra.html#sage.algebras.quatalg.quaternion_algebra.QuaternionOrder.discriminant) of the reference manual for a visual.\n\n\n\nThe maths expression in these lines\n\n```\n1481\t        The normalized theta series is by definition \n1442\t1482\t \n1443\t1483\t        .. math: \n1444\t1484\t \n1445\t \t        \\theta_I(q)=\\sum_{x \\in I} q^{\\frac{N(x)}{N(I)}} \n1446\t \t         \n \t1485\t            \\theta_I(q)=\\sum_{x \\in I} q^{\\frac{N(x)}{N(I)}}\n```\ndoesn't show up in the [HTML version](http://sage.math.washington.edu/home/mvngu/reference/sage/algebras/quatalg/quaternion_algebra.html#sage.algebras.quatalg.quaternion_algebra.QuaternionFractionalIdeal_rational.theta_series).",
    "created_at": "2009-04-17T02:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43032",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

REFEREE REPORT:



The following lines result in something weird when viewing the HTML version of the reference manual:

```
486	class QuaternionAlgebra_ab(QuaternionAlgebra_abstract): 
487	    """ 
488	    The quaternion algebra of the form `(a, b/K)`, where `i^2=a`, `j^2 = b`, 
489	    and `j*i = -i*j`.  ``K`` is a field not of characteristic 2 and ``a``, 
490	    ``b`` are nonzero elements of ``K``. 
491	 
492	    EXAMPLES:: 
493	 
494	    """ 
495	    def __init__(self, base_ring, a, b, names='i,j,k'):
```
See the [HTML version](http://sage.math.washington.edu/home/mvngu/reference/sage/algebras/quatalg/quaternion_algebra.html#sage.algebras.quatalg.quaternion_algebra.QuaternionAlgebra_ab) I've generated after applying the rebased patch. I think the problem is that there's a "EXAMPLES::" tag, which is not followed by any examples at all. Now by alphabetic order, the method `sage.algebras.quatalg.quaternion_algebra.QuaternionAlgebra_ab.QuaternionAlgebra_ab.discriminant()` is thus formatted in a weird way as

```
.. method:: QuaternionAlgebra_ab.discriminant()
```
in the HTML version.



How about some documentation for 

```
627	    def gen(self, i=0):
```
to explain what it does. At the moment, there are examples, but no explanation of what this method is supposed to do.



I think the maths expression in the following lines are typeset in a weird way:

```
1069	    def discriminant(self): 
1070	        r""" 
1071	        Return the discriminant of this order, which we define as 
1046	 	        $\sqrt( det ( Tr(e_i \bar(e_j) ) ) )$, where $\{e_i\}$ is the 
1072	        `\sqrt( det ( Tr(e_i \bar(e_j) ) ) )`, where `\{e_i\}` is the 
1073
```
See the [HTML version](http://sage.math.washington.edu/home/mvngu/reference/sage/algebras/quatalg/quaternion_algebra.html#sage.algebras.quatalg.quaternion_algebra.QuaternionOrder.discriminant) of the reference manual for a visual.



The maths expression in these lines

```
1481	        The normalized theta series is by definition 
1442	1482	 
1443	1483	        .. math: 
1444	1484	 
1445	 	        \theta_I(q)=\sum_{x \in I} q^{\frac{N(x)}{N(I)}} 
1446	 	         
 	1485	            \theta_I(q)=\sum_{x \in I} q^{\frac{N(x)}{N(I)}}
```
doesn't show up in the [HTML version](http://sage.math.washington.edu/home/mvngu/reference/sage/algebras/quatalg/quaternion_algebra.html#sage.algebras.quatalg.quaternion_algebra.QuaternionFractionalIdeal_rational.theta_series).



---

archive/issue_comments_043033.json:
```json
{
    "body": "Attachment [5541-second.patch](tarball://root/attachments/some-uuid/ticket5541/5541-second.patch) by @jhpalmieri created at 2009-04-17 03:23:56\n\napply on top of 5541-rebased.patch",
    "created_at": "2009-04-17T03:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43033",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [5541-second.patch](tarball://root/attachments/some-uuid/ticket5541/5541-second.patch) by @jhpalmieri created at 2009-04-17 03:23:56

apply on top of 5541-rebased.patch



---

archive/issue_comments_043034.json:
```json
{
    "body": "Oh, and mabshoff: this should fix the warnings for this file when building the reference manual.",
    "created_at": "2009-04-17T03:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43034",
    "user": "https://github.com/jhpalmieri"
}
```

Oh, and mabshoff: this should fix the warnings for this file when building the reference manual.



---

archive/issue_comments_043035.json:
```json
{
    "body": "REFEREE REPORT\n\n\n\nI applied patches against sage-3.4.1.rc3 in this order:\n\n1. First, `5541-rebased.patch`\n2. Followed by `5541-second.patch`\n\nAll doctests passed with options `-t -long`. I rebuilt the HTML version of the reference manual and noticed that `5541-second.patch` has addressed all of my concerns above. Positive review.",
    "created_at": "2009-04-17T05:53:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43035",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

REFEREE REPORT



I applied patches against sage-3.4.1.rc3 in this order:

1. First, `5541-rebased.patch`
2. Followed by `5541-second.patch`

All doctests passed with options `-t -long`. I rebuilt the HTML version of the reference manual and noticed that `5541-second.patch` has addressed all of my concerns above. Positive review.



---

archive/issue_comments_043036.json:
```json
{
    "body": "Ok, this should go into 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-17T06:14:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43036",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, this should go into 3.4.1.

Cheers,

Michael



---

archive/issue_events_013004.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-17T06:14:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5541#event-13004"
}
```



---

archive/issue_comments_043037.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-18T01:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43037",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_013005.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-18T01:07:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5541#event-13005"
}
```



---

archive/issue_comments_043038.json:
```json
{
    "body": "Merged  5541-rebased.patch and 5541-second.patch in Sage 3.4.1.rc4.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T01:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5541#issuecomment-43038",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged  5541-rebased.patch and 5541-second.patch in Sage 3.4.1.rc4.

Cheers,

Michael

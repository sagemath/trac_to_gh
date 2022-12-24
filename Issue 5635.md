# Issue 5635: plot method on lattice polytopes gives something ridiculous

archive/issues_005635.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nThe plot method on an object should return either a 2d plot or raise NotImplementedError (or not be defined).  On LatticePolytope's it returns a 3d Tachyon object.\n\n\n```\nsage: p = LatticePolytope(random_matrix(ZZ, 3,6, x=7)).plot()\nsage: type(p)\n<class 'sage.plot.tachyon.Tachyon'>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5635\n\n",
    "created_at": "2009-03-29T20:25:02Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "plot method on lattice polytopes gives something ridiculous",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5635",
    "user": "was"
}
```
Assignee: mhansen

CC:  sage-combinat

The plot method on an object should return either a 2d plot or raise NotImplementedError (or not be defined).  On LatticePolytope's it returns a 3d Tachyon object.


```
sage: p = LatticePolytope(random_matrix(ZZ, 3,6, x=7)).plot()
sage: type(p)
<class 'sage.plot.tachyon.Tachyon'>
```


Issue created by migration from https://trac.sagemath.org/ticket/5635





---

archive/issue_comments_044014.json:
```json
{
    "body": "Attachment [11803.patch](tarball://root/attachments/some-uuid/ticket5635/11803.patch) by novoselt created at 2009-03-31 04:26:55\n\nThe patch removes plot() method and fixes the documentation. I also changed show() to show3d(), which shows the plot without axes.",
    "created_at": "2009-03-31T04:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5635#issuecomment-44014",
    "user": "novoselt"
}
```

Attachment [11803.patch](tarball://root/attachments/some-uuid/ticket5635/11803.patch) by novoselt created at 2009-03-31 04:26:55

The patch removes plot() method and fixes the documentation. I also changed show() to show3d(), which shows the plot without axes.



---

archive/issue_comments_044015.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-01T01:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5635#issuecomment-44015",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044016.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-01T01:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5635#issuecomment-44016",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc0.

Cheers,

Michael

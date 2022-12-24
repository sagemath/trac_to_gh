# Issue 4757: eigenspaces_right over CDF gives total nonsense

archive/issues_004757.json:
```json
{
    "body": "Assignee: was\n\nI don't care what anybody says, this is a BUG.  Either the command should immediately raise a NotImplementedError, or it should give meaningful output (e.g., not vector spaces of dimension 0!)\n\n\n```\nsage: a = random_matrix(CDF,2)\nsage: a.eigenspaces_right()\n\n[\n(1.68954005899 + 0.570924387184*I, Vector space of degree 2 and dimension 0 over Complex Double Field\nUser basis matrix:\n[]),\n(-0.0345737707895 + 0.485480056628*I, Vector space of degree 2 and dimension 0 over Complex Double Field\nUser basis matrix:\n[])\n]\n```\n\n\nWe easily and quickly have the eigenvectors and eigenvalues in this case, so I don't see what the problem is:\n\n```\nsage: a.eigenvectors_right()\n\n([1.68954005899 + 0.570924387184*I, -0.0345737707895 + 0.485480056628*I],\n [                    0.800587795941                     0.758354735061]\n[  0.545800288485 - 0.24730795798*I -0.194687766428 + 0.622089036565*I])\n```\n\n\nSame comments for eigenspaces_left.\n\nNote that oddly a.eigenspaces() gives a sensible answer though neither left nor right does.\n\n```\nsage: a.eigenspaces_right()\n[\n(1.68954005899 + 0.570924387184*I, Vector space of degree 2 and dimension 0 over Complex Double Field\nUser basis matrix:\n[]),\n(-0.0345737707895 + 0.485480056628*I, Vector space of degree 2 and dimension 0 over Complex Double Field\nUser basis matrix:\n[])\n]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4757\n\n",
    "created_at": "2008-12-11T05:17:47Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "eigenspaces_right over CDF gives total nonsense",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4757",
    "user": "was"
}
```
Assignee: was

I don't care what anybody says, this is a BUG.  Either the command should immediately raise a NotImplementedError, or it should give meaningful output (e.g., not vector spaces of dimension 0!)


```
sage: a = random_matrix(CDF,2)
sage: a.eigenspaces_right()

[
(1.68954005899 + 0.570924387184*I, Vector space of degree 2 and dimension 0 over Complex Double Field
User basis matrix:
[]),
(-0.0345737707895 + 0.485480056628*I, Vector space of degree 2 and dimension 0 over Complex Double Field
User basis matrix:
[])
]
```


We easily and quickly have the eigenvectors and eigenvalues in this case, so I don't see what the problem is:

```
sage: a.eigenvectors_right()

([1.68954005899 + 0.570924387184*I, -0.0345737707895 + 0.485480056628*I],
 [                    0.800587795941                     0.758354735061]
[  0.545800288485 - 0.24730795798*I -0.194687766428 + 0.622089036565*I])
```


Same comments for eigenspaces_left.

Note that oddly a.eigenspaces() gives a sensible answer though neither left nor right does.

```
sage: a.eigenspaces_right()
[
(1.68954005899 + 0.570924387184*I, Vector space of degree 2 and dimension 0 over Complex Double Field
User basis matrix:
[]),
(-0.0345737707895 + 0.485480056628*I, Vector space of degree 2 and dimension 0 over Complex Double Field
User basis matrix:
[])
]
```


Issue created by migration from https://trac.sagemath.org/ticket/4757





---

archive/issue_comments_036041.json:
```json
{
    "body": "This has to do with the naming and aliases of methods in this and the parent class.\n\nNote that the eigenspaces method is now inherited from the parent class, and does the right thing by giving a deprecation warning and calling the eigenspaces_left method.",
    "created_at": "2008-12-11T08:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4757#issuecomment-36041",
    "user": "mhansen"
}
```

This has to do with the naming and aliases of methods in this and the parent class.

Note that the eigenspaces method is now inherited from the parent class, and does the right thing by giving a deprecation warning and calling the eigenspaces_left method.



---

archive/issue_comments_036042.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2008-12-11T08:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4757#issuecomment-36042",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_036043.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-11T08:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4757#issuecomment-36043",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036044.json:
```json
{
    "body": "Attachment [trac_4757.patch](tarball://root/attachments/some-uuid/ticket4757/trac_4757.patch) by mhansen created at 2008-12-11 08:07:05",
    "created_at": "2008-12-11T08:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4757#issuecomment-36044",
    "user": "mhansen"
}
```

Attachment [trac_4757.patch](tarball://root/attachments/some-uuid/ticket4757/trac_4757.patch) by mhansen created at 2008-12-11 08:07:05



---

archive/issue_comments_036045.json:
```json
{
    "body": "The patch code looks good, but I haven't tested it (I should be able to get to this by the weekend, though).\n\nThis was due to be looked at during the Christmas holiday as part of the overhaul of linear algebra interfaces (see http://wiki.sagemath.org/LinearAlgebraSEP; there it lists the methods as okay, but I'm aware that problems exist in the different eig* functions of different data types, so each of those implementations was going to be looked at.  For example, I believe the SR eig* functions don't conform to the correct interface right now either).\n\nThanks for catching and taking care of this.",
    "created_at": "2008-12-11T09:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4757#issuecomment-36045",
    "user": "jason"
}
```

The patch code looks good, but I haven't tested it (I should be able to get to this by the weekend, though).

This was due to be looked at during the Christmas holiday as part of the overhaul of linear algebra interfaces (see http://wiki.sagemath.org/LinearAlgebraSEP; there it lists the methods as okay, but I'm aware that problems exist in the different eig* functions of different data types, so each of those implementations was going to be looked at.  For example, I believe the SR eig* functions don't conform to the correct interface right now either).

Thanks for catching and taking care of this.



---

archive/issue_comments_036046.json:
```json
{
    "body": "Also looks good to me, and I've played around with it for a little while.  However, should there be a new doctest along the lines of William's example?",
    "created_at": "2008-12-11T09:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4757#issuecomment-36046",
    "user": "AlexGhitza"
}
```

Also looks good to me, and I've played around with it for a little while.  However, should there be a new doctest along the lines of William's example?



---

archive/issue_comments_036047.json:
```json
{
    "body": "apply on top of previous patches",
    "created_at": "2008-12-12T21:04:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4757#issuecomment-36047",
    "user": "jason"
}
```

apply on top of previous patches



---

archive/issue_comments_036048.json:
```json
{
    "body": "Attachment [trac_4757_review.patch](tarball://root/attachments/some-uuid/ticket4757/trac_4757_review.patch) by jason created at 2008-12-12 21:08:14\n\nThere already is a doctest which I think adequately covers the issue, but numerical error makes it so that it is marked #random.\n\nErring on the side of caution, my review patch probably ought to also be reviewed, as it changes code.",
    "created_at": "2008-12-12T21:08:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4757#issuecomment-36048",
    "user": "jason"
}
```

Attachment [trac_4757_review.patch](tarball://root/attachments/some-uuid/ticket4757/trac_4757_review.patch) by jason created at 2008-12-12 21:08:14

There already is a doctest which I think adequately covers the issue, but numerical error makes it so that it is marked #random.

Erring on the side of caution, my review patch probably ought to also be reviewed, as it changes code.



---

archive/issue_comments_036049.json:
```json
{
    "body": "Replying to [comment:4 jason]:\n> There already is a doctest which I think adequately covers the issue, but numerical error makes it so that it is marked #random.\n\nI am not sure that doctest should be random - if the result truly is #random, i.e. more than the last couple digits, there is something seriously wrong here.\n\n> Erring on the side of caution, my review patch probably ought to also be reviewed, as it changes code.\n\nYep\n\nCheers,\n\nMichael",
    "created_at": "2008-12-13T01:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4757#issuecomment-36049",
    "user": "mabshoff"
}
```

Replying to [comment:4 jason]:
> There already is a doctest which I think adequately covers the issue, but numerical error makes it so that it is marked #random.

I am not sure that doctest should be random - if the result truly is #random, i.e. more than the last couple digits, there is something seriously wrong here.

> Erring on the side of caution, my review patch probably ought to also be reviewed, as it changes code.

Yep

Cheers,

Michael



---

archive/issue_comments_036050.json:
```json
{
    "body": "It's not digits that is the problem, it's that the number is on the order of 1e-15, I believe.  However, we should be able to construct the printing of the data to deal with this.",
    "created_at": "2008-12-13T03:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4757#issuecomment-36050",
    "user": "jason"
}
```

It's not digits that is the problem, it's that the number is on the order of 1e-15, I believe.  However, we should be able to construct the printing of the data to deal with this.



---

archive/issue_comments_036051.json:
```json
{
    "body": "There is a test that the eigenvalues returned are of suitably small magnitude, so I'm not worried by the # random flag.  Positive review!2",
    "created_at": "2009-01-21T08:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4757#issuecomment-36051",
    "user": "ncalexan"
}
```

There is a test that the eigenvalues returned are of suitably small magnitude, so I'm not worried by the # random flag.  Positive review!2



---

archive/issue_comments_036052.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T07:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4757#issuecomment-36052",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1



---

archive/issue_comments_036053.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T07:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4757#issuecomment-36053",
    "user": "mabshoff"
}
```

Resolution: fixed

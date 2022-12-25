# Issue 9801: Add random diagonalizable matrix to matrix/constructor.py

archive/issues_009801.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @rbeezer @wdjoyner\n\nThis depends on #9720, so first apply the v3 patch from there.  This method generates random diagonalizable matrices whose eigenvectors, if computed by hand, have only integer values. This routine is designed as educational tool, generating exam and homework problems, and problem generating interacts.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9802\n\n",
    "created_at": "2010-08-25T18:45:05Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Add random diagonalizable matrix to matrix/constructor.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9801",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```
Assignee: jason, was

CC:  @rbeezer @wdjoyner

This depends on #9720, so first apply the v3 patch from there.  This method generates random diagonalizable matrices whose eigenvectors, if computed by hand, have only integer values. This routine is designed as educational tool, generating exam and homework problems, and problem generating interacts.

Issue created by migration from https://trac.sagemath.org/ticket/9802





---

archive/issue_comments_096138.json:
```json
{
    "body": "Attachment [trac_9802-random-diagonalizable-matrix.patch](tarball://root/attachments/some-uuid/ticket9802/trac_9802-random-diagonalizable-matrix.patch) by bwonderly created at 2010-08-25 18:47:30",
    "created_at": "2010-08-25T18:47:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9801#issuecomment-96138",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Attachment [trac_9802-random-diagonalizable-matrix.patch](tarball://root/attachments/some-uuid/ticket9802/trac_9802-random-diagonalizable-matrix.patch) by bwonderly created at 2010-08-25 18:47:30



---

archive/issue_comments_096139.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-25T18:47:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9801#issuecomment-96139",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096140.json:
```json
{
    "body": "Attachment [trac_9802-random-diagonalizable-matrix-v2.patch](tarball://root/attachments/some-uuid/ticket9802/trac_9802-random-diagonalizable-matrix-v2.patch) by bwonderly created at 2010-08-28 02:39:04\n\nrevised to fit generalization of random_matrix constructor. Apply v4 from #9720 and v2 from #9803 and go from there. This patch is independent from #9754, but will be rebased as soon as either one gets a positive review",
    "created_at": "2010-08-28T02:39:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9801#issuecomment-96140",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

Attachment [trac_9802-random-diagonalizable-matrix-v2.patch](tarball://root/attachments/some-uuid/ticket9802/trac_9802-random-diagonalizable-matrix-v2.patch) by bwonderly created at 2010-08-28 02:39:04

revised to fit generalization of random_matrix constructor. Apply v4 from #9720 and v2 from #9803 and go from there. This patch is independent from #9754, but will be rebased as soon as either one gets a positive review



---

archive/issue_comments_096141.json:
```json
{
    "body": "The v2 patch is independent of #9754. There are revisions to the documentation of the random_diagonalizable_matrix routine, as well as to the random_matrix routine.  The code is revised to fit with the generalization of the random_matrix constructor.  First apply v4 from #9720, and then v2 from #9803 and go from there.",
    "created_at": "2010-08-28T17:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9801#issuecomment-96141",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

The v2 patch is independent of #9754. There are revisions to the documentation of the random_diagonalizable_matrix routine, as well as to the random_matrix routine.  The code is revised to fit with the generalization of the random_matrix constructor.  First apply v4 from #9720, and then v2 from #9803 and go from there.



---

archive/issue_comments_096142.json:
```json
{
    "body": "This (with the other patches, as indicated above) applied fine to 4.5.1 and passed sage -testall.\n\nPositive review, as far as I am concerned (and will be useful for me teaching linear algebra later in the semester!). Perhaps Mike Hansen should have the final say?\n\nThanks Rob and bwonderly!",
    "created_at": "2010-08-28T21:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9801#issuecomment-96142",
    "user": "https://github.com/wdjoyner"
}
```

This (with the other patches, as indicated above) applied fine to 4.5.1 and passed sage -testall.

Positive review, as far as I am concerned (and will be useful for me teaching linear algebra later in the semester!). Perhaps Mike Hansen should have the final say?

Thanks Rob and bwonderly!



---

archive/issue_comments_096143.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-02T02:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9801#issuecomment-96143",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096144.json:
```json
{
    "body": "Mike Hansen looked in on #9803, so I've marked this as ready to go based on comments above.  Thanks, David.",
    "created_at": "2010-09-02T02:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9801#issuecomment-96144",
    "user": "https://github.com/rbeezer"
}
```

Mike Hansen looked in on #9803, so I've marked this as ready to go based on comments above.  Thanks, David.



---

archive/issue_comments_096145.json:
```json
{
    "body": "## Release Manager\n\n#9720, #9803, #9802, #9754 is each dependent on the predecessor, merge in this\norder.",
    "created_at": "2010-09-03T06:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9801#issuecomment-96145",
    "user": "https://trac.sagemath.org/admin/accounts/users/bwonderly"
}
```

## Release Manager

#9720, #9803, #9802, #9754 is each dependent on the predecessor, merge in this
order.



---

archive/issue_comments_096146.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T09:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9801#issuecomment-96146",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed

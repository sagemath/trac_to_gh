# Issue 9069: weak popov form

archive/issues_009069.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @burcin @koffie minz\n\nImplement weak Popov form for a matrix over a rational function field k(t)\n\nIssue created by migration from https://trac.sagemath.org/ticket/9069\n\n",
    "created_at": "2010-05-28T00:25:47Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "weak popov form",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9069",
    "user": "https://trac.sagemath.org/admin/accounts/users/cjh"
}
```
Assignee: jason, was

CC:  @burcin @koffie minz

Implement weak Popov form for a matrix over a rational function field k(t)

Issue created by migration from https://trac.sagemath.org/ticket/9069





---

archive/issue_comments_084024.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-28T00:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9069#issuecomment-84024",
    "user": "https://trac.sagemath.org/admin/accounts/users/cjh"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084025.json:
```json
{
    "body": "My student David Roberts implemented  this in Magma, following the Mulders & Storjohann paper, and used it in the implementation of a lattice-based method for point-finding on curves over function fields F_q(T).  So I am familiar with the algorithm.  But when I gave a talk about the method in Leiden in 2006, I found that Hendrik Lenstra had never heard of Weak Popov Form, though his brother Arjen Lenstra's thesis (which dates back to the original LLL paper, so they could factor multivariate polynomials) had something entirely equivalent under another name.  From what I remember, the upshot is that for most constant fields one might be better off using theory to bound degrees and then using linear algebra over the ground field.\n\nThe patch applies fine to 4.4.3 and long tests in the two files touched pass.\n\n1. line 4545: typo, C should be N?  Same i nthe other file & docstring.\n2. In lines 99-105, why not just use an identity matrix?\n3. There is a slight inconsistency in the output for input a zero matrix, since it only has two components.  For consistency, also output the third thing, even if it is just a tuple of -Infinity's.\n\nOtherwise it looks ok to me, given that the tests work, but I have not had time to go through the important part of the code in great detail and have no more time right now.",
    "created_at": "2010-06-05T15:42:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9069#issuecomment-84025",
    "user": "https://github.com/JohnCremona"
}
```

My student David Roberts implemented  this in Magma, following the Mulders & Storjohann paper, and used it in the implementation of a lattice-based method for point-finding on curves over function fields F_q(T).  So I am familiar with the algorithm.  But when I gave a talk about the method in Leiden in 2006, I found that Hendrik Lenstra had never heard of Weak Popov Form, though his brother Arjen Lenstra's thesis (which dates back to the original LLL paper, so they could factor multivariate polynomials) had something entirely equivalent under another name.  From what I remember, the upshot is that for most constant fields one might be better off using theory to bound degrees and then using linear algebra over the ground field.

The patch applies fine to 4.4.3 and long tests in the two files touched pass.

1. line 4545: typo, C should be N?  Same i nthe other file & docstring.
2. In lines 99-105, why not just use an identity matrix?
3. There is a slight inconsistency in the output for input a zero matrix, since it only has two components.  For consistency, also output the third thing, even if it is just a tuple of -Infinity's.

Otherwise it looks ok to me, given that the tests work, but I have not had time to go through the important part of the code in great detail and have no more time right now.



---

archive/issue_comments_084026.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-05T15:42:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9069#issuecomment-84026",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_084027.json:
```json
{
    "body": "Attachment [trac_9069.patch](tarball://root/attachments/some-uuid/ticket9069/trac_9069.patch) by cjh created at 2010-06-07 10:11:50",
    "created_at": "2010-06-07T10:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9069#issuecomment-84027",
    "user": "https://trac.sagemath.org/admin/accounts/users/cjh"
}
```

Attachment [trac_9069.patch](tarball://root/attachments/some-uuid/ticket9069/trac_9069.patch) by cjh created at 2010-06-07 10:11:50



---

archive/issue_comments_084028.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-07T10:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9069#issuecomment-84028",
    "user": "https://trac.sagemath.org/admin/accounts/users/cjh"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084029.json:
```json
{
    "body": "Latest version of the patch incorporates minor changes made in response to Cremona's comments.  Specifically, responses to his respective comments are:\n\n1. Yes, C should be N.  Both docstrings corrected.\n2. We now construct N using an identity matrix.  Note, the rest of the code expects N to be a list of tuples, hence N isn't an actual matrix.\n3. The output for a zero matrix is now consistent with the documentation.",
    "created_at": "2010-06-07T10:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9069#issuecomment-84029",
    "user": "https://trac.sagemath.org/admin/accounts/users/cjh"
}
```

Latest version of the patch incorporates minor changes made in response to Cremona's comments.  Specifically, responses to his respective comments are:

1. Yes, C should be N.  Both docstrings corrected.
2. We now construct N using an identity matrix.  Note, the rest of the code expects N to be a list of tuples, hence N isn't an actual matrix.
3. The output for a zero matrix is now consistent with the documentation.



---

archive/issue_comments_084030.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-23T16:22:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9069#issuecomment-84030",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084031.json:
```json
{
    "body": "Fine!  Patch applies fine to 4.4.4.alpha1.",
    "created_at": "2010-06-23T16:22:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9069#issuecomment-84031",
    "user": "https://github.com/JohnCremona"
}
```

Fine!  Patch applies fine to 4.4.4.alpha1.



---

archive/issue_events_009220.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-07-20T08:20:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9069",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9069#event-9220"
}
```



---

archive/issue_comments_084032.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T08:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9069#issuecomment-84032",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_084033.json:
```json
{
    "body": "unique name please",
    "created_at": "2017-07-19T08:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9069#issuecomment-84033",
    "user": "https://github.com/fchapoton"
}
```

unique name please

# Issue 5827: crypto: subset sum problem for super-increasing sequences

archive/issues_005827.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: knapsack cryptosystem, subset sum\n\nThe Merkle-Hellman knapsack public-key cryptosystem makes use of the subset sum problem for super-increasing sequences. The goal of this ticket is to first implement a class for solving the subset sum problem for super-increasing sequences. The long-term goal is to implement a module for knapsack cryptosystems. So the implementation contained on this ticket would be subsumed within the module.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5827\n\n",
    "created_at": "2009-04-20T03:15:33Z",
    "labels": [
        "cryptography",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "crypto: subset sum problem for super-increasing sequences",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5827",
    "user": "mvngu"
}
```
Assignee: somebody

Keywords: knapsack cryptosystem, subset sum

The Merkle-Hellman knapsack public-key cryptosystem makes use of the subset sum problem for super-increasing sequences. The goal of this ticket is to first implement a class for solving the subset sum problem for super-increasing sequences. The long-term goal is to implement a module for knapsack cryptosystems. So the implementation contained on this ticket would be subsumed within the module.

Issue created by migration from https://trac.sagemath.org/ticket/5827





---

archive/issue_comments_045803.json:
```json
{
    "body": "The patch implements an algorithm for solving the subset sum problem for super-increasing sequences. This is useful in the Merkle-Hellman knapsack cryptosystem, which I plan to work on later.",
    "created_at": "2009-04-20T03:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45803",
    "user": "mvngu"
}
```

The patch implements an algorithm for solving the subset sum problem for super-increasing sequences. This is useful in the Merkle-Hellman knapsack cryptosystem, which I plan to work on later.



---

archive/issue_comments_045804.json:
```json
{
    "body": "based on Sage 3.4.1",
    "created_at": "2009-04-24T09:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45804",
    "user": "mvngu"
}
```

based on Sage 3.4.1



---

archive/issue_comments_045805.json:
```json
{
    "body": "Attachment [trac_5827-subset-sum.patch](tarball://root/attachments/some-uuid/ticket5827/trac_5827-subset-sum.patch) by mvngu created at 2009-05-09 06:02:46\n\nOnly apply `trac_5827-subset-sum.2.patch`.",
    "created_at": "2009-05-09T06:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45805",
    "user": "mvngu"
}
```

Attachment [trac_5827-subset-sum.patch](tarball://root/attachments/some-uuid/ticket5827/trac_5827-subset-sum.patch) by mvngu created at 2009-05-09 06:02:46

Only apply `trac_5827-subset-sum.2.patch`.



---

archive/issue_comments_045806.json:
```json
{
    "body": "Attachment [trac_5827-subset-sum.2.patch](tarball://root/attachments/some-uuid/ticket5827/trac_5827-subset-sum.2.patch) by mvngu created at 2009-06-01 08:09:01\n\nbased on Sage 4.0",
    "created_at": "2009-06-01T08:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45806",
    "user": "mvngu"
}
```

Attachment [trac_5827-subset-sum.2.patch](tarball://root/attachments/some-uuid/ticket5827/trac_5827-subset-sum.2.patch) by mvngu created at 2009-06-01 08:09:01

based on Sage 4.0



---

archive/issue_comments_045807.json:
```json
{
    "body": "Only apply `trac_5827-subset-sum.2.patch`. This patch depends on the patch at #6176.",
    "created_at": "2009-06-01T08:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45807",
    "user": "mvngu"
}
```

Only apply `trac_5827-subset-sum.2.patch`. This patch depends on the patch at #6176.



---

archive/issue_comments_045808.json:
```json
{
    "body": "Changing component from cryptography to numerical.",
    "created_at": "2009-06-01T08:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45808",
    "user": "mvngu"
}
```

Changing component from cryptography to numerical.



---

archive/issue_comments_045809.json:
```json
{
    "body": "Changing keywords from \"knapsack cryptosystem, subset sum\" to \"knapsack problems, subset sum\".",
    "created_at": "2009-06-01T08:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45809",
    "user": "mvngu"
}
```

Changing keywords from "knapsack cryptosystem, subset sum" to "knapsack problems, subset sum".



---

archive/issue_comments_045810.json:
```json
{
    "body": "Changing assignee from somebody to jkantor.",
    "created_at": "2009-06-01T08:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45810",
    "user": "mvngu"
}
```

Changing assignee from somebody to jkantor.



---

archive/issue_comments_045811.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T18:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45811",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_045812.json:
```json
{
    "body": "Looks good to me.\n\nMerged in 4.0.1.rc1.",
    "created_at": "2009-06-04T18:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45812",
    "user": "mhansen"
}
```

Looks good to me.

Merged in 4.0.1.rc1.



---

archive/issue_comments_045813.json:
```json
{
    "body": "I notice some typos in the code. This is addressed by #6222.",
    "created_at": "2009-06-05T05:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45813",
    "user": "mvngu"
}
```

I notice some typos in the code. This is addressed by #6222.

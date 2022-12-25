# Issue 5827: crypto: subset sum problem for super-increasing sequences

archive/issues_005827.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: knapsack cryptosystem, subset sum\n\nThe Merkle-Hellman knapsack public-key cryptosystem makes use of the subset sum problem for super-increasing sequences. The goal of this ticket is to first implement a class for solving the subset sum problem for super-increasing sequences. The long-term goal is to implement a module for knapsack cryptosystems. So the implementation contained on this ticket would be subsumed within the module.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5827\n\n",
    "created_at": "2009-04-20T03:15:33Z",
    "labels": [
        "component: cryptography"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "crypto: subset sum problem for super-increasing sequences",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5827",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: somebody

Keywords: knapsack cryptosystem, subset sum

The Merkle-Hellman knapsack public-key cryptosystem makes use of the subset sum problem for super-increasing sequences. The goal of this ticket is to first implement a class for solving the subset sum problem for super-increasing sequences. The long-term goal is to implement a module for knapsack cryptosystems. So the implementation contained on this ticket would be subsumed within the module.

Issue created by migration from https://trac.sagemath.org/ticket/5827





---

archive/issue_comments_045716.json:
```json
{
    "body": "The patch implements an algorithm for solving the subset sum problem for super-increasing sequences. This is useful in the Merkle-Hellman knapsack cryptosystem, which I plan to work on later.",
    "created_at": "2009-04-20T03:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45716",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch implements an algorithm for solving the subset sum problem for super-increasing sequences. This is useful in the Merkle-Hellman knapsack cryptosystem, which I plan to work on later.



---

archive/issue_events_013693.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-04-21T06:55:11Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5827#event-13693"
}
```



---

archive/issue_events_013694.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-04-22T05:06:46Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5827#event-13694"
}
```



---

archive/issue_events_013695.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-04-22T05:06:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5827#event-13695"
}
```



---

archive/issue_comments_045717.json:
```json
{
    "body": "based on Sage 3.4.1",
    "created_at": "2009-04-24T09:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45717",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

based on Sage 3.4.1



---

archive/issue_comments_045718.json:
```json
{
    "body": "Attachment [trac_5827-subset-sum.patch](tarball://root/attachments/some-uuid/ticket5827/trac_5827-subset-sum.patch) by mvngu created at 2009-05-09 06:02:46\n\nOnly apply `trac_5827-subset-sum.2.patch`.",
    "created_at": "2009-05-09T06:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45718",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_5827-subset-sum.patch](tarball://root/attachments/some-uuid/ticket5827/trac_5827-subset-sum.patch) by mvngu created at 2009-05-09 06:02:46

Only apply `trac_5827-subset-sum.2.patch`.



---

archive/issue_comments_045719.json:
```json
{
    "body": "Attachment [trac_5827-subset-sum.2.patch](tarball://root/attachments/some-uuid/ticket5827/trac_5827-subset-sum.2.patch) by mvngu created at 2009-06-01 08:09:01\n\nbased on Sage 4.0",
    "created_at": "2009-06-01T08:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45719",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_5827-subset-sum.2.patch](tarball://root/attachments/some-uuid/ticket5827/trac_5827-subset-sum.2.patch) by mvngu created at 2009-06-01 08:09:01

based on Sage 4.0



---

archive/issue_comments_045720.json:
```json
{
    "body": "Only apply `trac_5827-subset-sum.2.patch`. This patch depends on the patch at #6176.",
    "created_at": "2009-06-01T08:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45720",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Only apply `trac_5827-subset-sum.2.patch`. This patch depends on the patch at #6176.



---

archive/issue_comments_045721.json:
```json
{
    "body": "Changing component from cryptography to numerical.",
    "created_at": "2009-06-01T08:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45721",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing component from cryptography to numerical.



---

archive/issue_comments_045722.json:
```json
{
    "body": "Changing keywords from \"knapsack cryptosystem, subset sum\" to \"knapsack problems, subset sum\".",
    "created_at": "2009-06-01T08:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45722",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing keywords from "knapsack cryptosystem, subset sum" to "knapsack problems, subset sum".



---

archive/issue_comments_045723.json:
```json
{
    "body": "Changing assignee from somebody to jkantor.",
    "created_at": "2009-06-01T08:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45723",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing assignee from somebody to jkantor.



---

archive/issue_events_013696.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-04T18:52:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5827#event-13696"
}
```



---

archive/issue_comments_045724.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T18:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45724",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_045725.json:
```json
{
    "body": "Looks good to me.\n\nMerged in 4.0.1.rc1.",
    "created_at": "2009-06-04T18:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45725",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.

Merged in 4.0.1.rc1.



---

archive/issue_comments_045726.json:
```json
{
    "body": "I notice some typos in the code. This is addressed by #6222.",
    "created_at": "2009-06-05T05:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5827#issuecomment-45726",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I notice some typos in the code. This is addressed by #6222.

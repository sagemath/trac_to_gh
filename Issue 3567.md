# Issue 3567: optimize startup of sage -- don't import global transaction module

archive/issues_003567.json:
```json
{
    "body": "Assignee: tbd\n\nBEFORE:\n\n```\nteragon-2:databases was$ sage -startuptime |grep transaction\n        transaction: 0.104 (sage.databases.db)\n         transaction._transaction: 0.103 (transaction)\n          logging: 0.004 (transaction._transaction)\n          zope: 0.096 (transaction._transaction)\n         transaction._manager: 0.000 (transaction)\n             transaction.interfaces: 0.000 (ZODB.Connection)\n0.104 transaction (sage.databases.db)\n0.103 transaction._transaction (transaction)\n0.096 zope (transaction._transaction)\n```\n\nand that's *with* disk caching (on os x though). \n\nAFTER this patch:\n\n```\nteragon-2:databases was$ sage -startuptime |grep transaction\n             transaction.interfaces: 0.004 (ZODB.Connection)\n              transaction._transaction: 0.003 (transaction.interfaces)\n               zope: 0.000 (transaction._transaction)\n               transaction: 0.001 (transaction._transaction)\n              transaction._manager: 0.000 (transaction.interfaces)\n```\n\n\nSweet!\n\nIssue created by migration from https://trac.sagemath.org/ticket/3567\n\n",
    "created_at": "2008-07-06T19:48:57Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "optimize startup of sage -- don't import global transaction module",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3567",
    "user": "was"
}
```
Assignee: tbd

BEFORE:

```
teragon-2:databases was$ sage -startuptime |grep transaction
        transaction: 0.104 (sage.databases.db)
         transaction._transaction: 0.103 (transaction)
          logging: 0.004 (transaction._transaction)
          zope: 0.096 (transaction._transaction)
         transaction._manager: 0.000 (transaction)
             transaction.interfaces: 0.000 (ZODB.Connection)
0.104 transaction (sage.databases.db)
0.103 transaction._transaction (transaction)
0.096 zope (transaction._transaction)
```

and that's *with* disk caching (on os x though). 

AFTER this patch:

```
teragon-2:databases was$ sage -startuptime |grep transaction
             transaction.interfaces: 0.004 (ZODB.Connection)
              transaction._transaction: 0.003 (transaction.interfaces)
               zope: 0.000 (transaction._transaction)
               transaction: 0.001 (transaction._transaction)
              transaction._manager: 0.000 (transaction.interfaces)
```


Sweet!

Issue created by migration from https://trac.sagemath.org/ticket/3567





---

archive/issue_comments_025200.json:
```json
{
    "body": "Attachment [sage-3567.patch](tarball://root/attachments/some-uuid/ticket3567/sage-3567.patch) by was created at 2008-07-06 19:50:48",
    "created_at": "2008-07-06T19:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3567#issuecomment-25200",
    "user": "was"
}
```

Attachment [sage-3567.patch](tarball://root/attachments/some-uuid/ticket3567/sage-3567.patch) by was created at 2008-07-06 19:50:48



---

archive/issue_comments_025201.json:
```json
{
    "body": "Changing component from algebra to misc.",
    "created_at": "2008-07-06T19:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3567#issuecomment-25201",
    "user": "was"
}
```

Changing component from algebra to misc.



---

archive/issue_comments_025202.json:
```json
{
    "body": "Changing assignee from tbd to cwitty.",
    "created_at": "2008-07-06T19:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3567#issuecomment-25202",
    "user": "was"
}
```

Changing assignee from tbd to cwitty.



---

archive/issue_comments_025203.json:
```json
{
    "body": "+1",
    "created_at": "2008-07-06T19:53:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3567#issuecomment-25203",
    "user": "mhansen"
}
```

+1



---

archive/issue_comments_025204.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-06T20:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3567#issuecomment-25204",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha2



---

archive/issue_comments_025205.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-06T20:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3567#issuecomment-25205",
    "user": "mabshoff"
}
```

Resolution: fixed

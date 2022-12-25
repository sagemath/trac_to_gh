# Issue 1652: length of DAGs with loops calculation runs infinite

archive/issues_001652.json:
```json
{
    "body": "Assignee: @rlmill\n\nG4 has a loop: 2->4 and 4->2\n\n\n\n```\nG4 = DiGraph({1:[2,2,3,5], 2:[3,4], 3:[4], 4:[2,5,7], 5:[6]}, multiedges=True)\nG4_path.count()\n\nRuntimeError: maximum recursion depth exceeded\n```\n\n\n\nThere are related issues calulating *incoming_paths* and possibly more in *sage.combinat.graph_path*!\n\nIssue created by migration from https://trac.sagemath.org/ticket/1652\n\n",
    "created_at": "2008-01-01T19:23:44Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "length of DAGs with loops calculation runs infinite",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1652",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: @rlmill

G4 has a loop: 2->4 and 4->2



```
G4 = DiGraph({1:[2,2,3,5], 2:[3,4], 3:[4], 4:[2,5,7], 5:[6]}, multiedges=True)
G4_path.count()

RuntimeError: maximum recursion depth exceeded
```



There are related issues calulating *incoming_paths* and possibly more in *sage.combinat.graph_path*!

Issue created by migration from https://trac.sagemath.org/ticket/1652





---

archive/issue_comments_010488.json:
```json
{
    "body": "ah, solution is very simple: just check if **G4.is_directed_acyclic()** is true ;)",
    "created_at": "2008-01-01T19:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1652#issuecomment-10488",
    "user": "https://github.com/haraldschilly"
}
```

ah, solution is very simple: just check if **G4.is_directed_acyclic()** is true ;)



---

archive/issue_comments_010489.json:
```json
{
    "body": "Could you be more specific? I have no idea what G4_path is. Also, could you post a full traceback?",
    "created_at": "2008-01-01T23:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1652#issuecomment-10489",
    "user": "https://github.com/rlmill"
}
```

Could you be more specific? I have no idea what G4_path is. Also, could you post a full traceback?



---

archive/issue_comments_010490.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-19T19:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1652#issuecomment-10490",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010491.json:
```json
{
    "body": "Changing assignee from @rlmill to @mwhansen.",
    "created_at": "2008-01-19T19:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1652#issuecomment-10491",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @rlmill to @mwhansen.



---

archive/issue_comments_010492.json:
```json
{
    "body": "Attachment [1652.patch](tarball://root/attachments/some-uuid/ticket1652/1652.patch) by @mwhansen created at 2008-01-20 00:41:12",
    "created_at": "2008-01-20T00:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1652#issuecomment-10492",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1652.patch](tarball://root/attachments/some-uuid/ticket1652/1652.patch) by @mwhansen created at 2008-01-20 00:41:12



---

archive/issue_comments_010493.json:
```json
{
    "body": "Code looks good, docstrings and tests seem appropriate.",
    "created_at": "2008-01-20T03:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1652#issuecomment-10493",
    "user": "https://github.com/ncalexan"
}
```

Code looks good, docstrings and tests seem appropriate.



---

archive/issue_comments_010494.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T05:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1652#issuecomment-10494",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1



---

archive/issue_comments_010495.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T05:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1652#issuecomment-10495",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

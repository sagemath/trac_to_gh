# Issue 1652: length of DAGs with loops calculation runs infinite

archive/issues_001652.json:
```json
{
    "body": "Assignee: rlm\n\nG4 has a loop: 2->4 and 4->2\n\n\n\n```\nG4 = DiGraph({1:[2,2,3,5], 2:[3,4], 3:[4], 4:[2,5,7], 5:[6]}, multiedges=True)\nG4_path.count()\n\nRuntimeError: maximum recursion depth exceeded\n```\n\n\n\nThere are related issues calulating *incoming_paths* and possibly more in *sage.combinat.graph_path*!\n\nIssue created by migration from https://trac.sagemath.org/ticket/1652\n\n",
    "created_at": "2008-01-01T19:23:44Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "length of DAGs with loops calculation runs infinite",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1652",
    "user": "schilly"
}
```
Assignee: rlm

G4 has a loop: 2->4 and 4->2



```
G4 = DiGraph({1:[2,2,3,5], 2:[3,4], 3:[4], 4:[2,5,7], 5:[6]}, multiedges=True)
G4_path.count()

RuntimeError: maximum recursion depth exceeded
```



There are related issues calulating *incoming_paths* and possibly more in *sage.combinat.graph_path*!

Issue created by migration from https://trac.sagemath.org/ticket/1652





---

archive/issue_comments_010515.json:
```json
{
    "body": "ah, solution is very simple: just check if **G4.is_directed_acyclic()** is true ;)",
    "created_at": "2008-01-01T19:25:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1652#issuecomment-10515",
    "user": "schilly"
}
```

ah, solution is very simple: just check if **G4.is_directed_acyclic()** is true ;)



---

archive/issue_comments_010516.json:
```json
{
    "body": "Could you be more specific? I have no idea what G4_path is. Also, could you post a full traceback?",
    "created_at": "2008-01-01T23:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1652#issuecomment-10516",
    "user": "rlm"
}
```

Could you be more specific? I have no idea what G4_path is. Also, could you post a full traceback?



---

archive/issue_comments_010517.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-19T19:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1652#issuecomment-10517",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010518.json:
```json
{
    "body": "Changing assignee from rlm to mhansen.",
    "created_at": "2008-01-19T19:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1652#issuecomment-10518",
    "user": "mhansen"
}
```

Changing assignee from rlm to mhansen.



---

archive/issue_comments_010519.json:
```json
{
    "body": "Attachment [1652.patch](tarball://root/attachments/some-uuid/ticket1652/1652.patch) by mhansen created at 2008-01-20 00:41:12",
    "created_at": "2008-01-20T00:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1652#issuecomment-10519",
    "user": "mhansen"
}
```

Attachment [1652.patch](tarball://root/attachments/some-uuid/ticket1652/1652.patch) by mhansen created at 2008-01-20 00:41:12



---

archive/issue_comments_010520.json:
```json
{
    "body": "Code looks good, docstrings and tests seem appropriate.",
    "created_at": "2008-01-20T03:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1652#issuecomment-10520",
    "user": "ncalexan"
}
```

Code looks good, docstrings and tests seem appropriate.



---

archive/issue_comments_010521.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T05:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1652#issuecomment-10521",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha1



---

archive/issue_comments_010522.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T05:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1652#issuecomment-10522",
    "user": "mabshoff"
}
```

Resolution: fixed

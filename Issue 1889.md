# Issue 1889: 2.10.1.alpha2 doctest failure in crypto/mq/sr.py

archive/issues_001889.json:
```json
{
    "body": "Assignee: malb\n\nThis is probably related to merging #1817:\n\n```\nsage -t  devel/sage-main/sage/crypto/mq/sr.py\n**********************************************************************\nFile \"sr.py\", line 1364:\n    sage: F.groebner_basis()[:4]\nExpected:\n    [k003 + 1, k001, k000 + k001 + 1, s003 + k002]\nGot:\n    [k003 + 1, k001, k000 + 1, s003 + k002]\n**********************************************************************\nFile \"sr.py\", line 1500:\n    sage: _= A = sr.random_state_array(); A\nExpected nothing\nGot:\n    [a^3 + 1]\n**********************************************************************\nFile \"sr.py\", line 1874:\n    sage: _= A = sr.random_state_array(); A\nExpected nothing\nGot:\n    [a^3]\n**********************************************************************\n3 items had failures:\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1889\n\n",
    "created_at": "2008-01-23T07:47:30Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "2.10.1.alpha2 doctest failure in crypto/mq/sr.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1889",
    "user": "mabshoff"
}
```
Assignee: malb

This is probably related to merging #1817:

```
sage -t  devel/sage-main/sage/crypto/mq/sr.py
**********************************************************************
File "sr.py", line 1364:
    sage: F.groebner_basis()[:4]
Expected:
    [k003 + 1, k001, k000 + k001 + 1, s003 + k002]
Got:
    [k003 + 1, k001, k000 + 1, s003 + k002]
**********************************************************************
File "sr.py", line 1500:
    sage: _= A = sr.random_state_array(); A
Expected nothing
Got:
    [a^3 + 1]
**********************************************************************
File "sr.py", line 1874:
    sage: _= A = sr.random_state_array(); A
Expected nothing
Got:
    [a^3]
**********************************************************************
3 items had failures:
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1889





---

archive/issue_comments_011965.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-23T17:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1889#issuecomment-11965",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_011966.json:
```json
{
    "body": "Yes, it was related to #1817",
    "created_at": "2008-01-23T17:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1889#issuecomment-11966",
    "user": "malb"
}
```

Yes, it was related to #1817



---

archive/issue_comments_011967.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-23T17:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1889#issuecomment-11967",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011968.json:
```json
{
    "body": "Patch looks good to me.",
    "created_at": "2008-01-23T22:11:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1889#issuecomment-11968",
    "user": "mabshoff"
}
```

Patch looks good to me.



---

archive/issue_comments_011969.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-23T22:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1889#issuecomment-11969",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha2



---

archive/issue_comments_011970.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-23T22:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1889",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1889#issuecomment-11970",
    "user": "mabshoff"
}
```

Resolution: fixed

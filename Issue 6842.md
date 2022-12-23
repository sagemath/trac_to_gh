# Issue 6842: [with patch, needs review] ordinal_str giving wrong answers for 111, 112, 113

archive/issues_006842.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: ordinals\n\nThe following is incorrect, if I am not mistaken (but I am not a native speaker):\n\n```\nsage: n = 113\nsage: n.ordinal_str()\n'113rd'\nsage: n = 112\nsage: n.ordinal_str()\n'112nd'\nsage: n = 111\nsage: n.ordinal_str()\n'111st'\n```\n\n\nWith my patch, one gets\n\n```\nsage: n = 111\nsage: n.ordinal_str()\n'111th'\nsage: n = 112\nsage: n.ordinal_str()\n'112th'\nsage: n = 113\nsage: n.ordinal_str()\n'113th'\n```\n\nwhile one still has\n\n```\nsage: n = 121\nsage: n.ordinal_str()\n'121st'\nsage: n = 122\nsage: n.ordinal_str()\n'122nd'\nsage: n = 123\nsage: n.ordinal_str()\n'123rd'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6842\n\n",
    "created_at": "2009-08-29T11:29:59Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] ordinal_str giving wrong answers for 111, 112, 113",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6842",
    "user": "SimonKing"
}
```
Assignee: somebody

Keywords: ordinals

The following is incorrect, if I am not mistaken (but I am not a native speaker):

```
sage: n = 113
sage: n.ordinal_str()
'113rd'
sage: n = 112
sage: n.ordinal_str()
'112nd'
sage: n = 111
sage: n.ordinal_str()
'111st'
```


With my patch, one gets

```
sage: n = 111
sage: n.ordinal_str()
'111th'
sage: n = 112
sage: n.ordinal_str()
'112th'
sage: n = 113
sage: n.ordinal_str()
'113th'
```

while one still has

```
sage: n = 121
sage: n.ordinal_str()
'121st'
sage: n = 122
sage: n.ordinal_str()
'122nd'
sage: n = 123
sage: n.ordinal_str()
'123rd'
```


Issue created by migration from https://trac.sagemath.org/ticket/6842





---

archive/issue_comments_056443.json:
```json
{
    "body": "Fixing ordinal_str for numbers of the form n*100+11, n*100+12, n*100+13",
    "created_at": "2009-08-29T11:30:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6842#issuecomment-56443",
    "user": "SimonKing"
}
```

Fixing ordinal_str for numbers of the form n*100+11, n*100+12, n*100+13



---

archive/issue_comments_056444.json:
```json
{
    "body": "Attachment\n\nLooks good to me. It passes unit tests and the documentation builds correctly. \n\nAdam",
    "created_at": "2009-08-29T12:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6842#issuecomment-56444",
    "user": "awebb"
}
```

Attachment

Looks good to me. It passes unit tests and the documentation builds correctly. 

Adam



---

archive/issue_comments_056445.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-30T07:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6842#issuecomment-56445",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_056446.json:
```json
{
    "body": "I came along to review this only to find that I was too late.  Thanks for fixing the bug (which was mine).",
    "created_at": "2009-08-30T10:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6842#issuecomment-56446",
    "user": "cremona"
}
```

I came along to review this only to find that I was too late.  Thanks for fixing the bug (which was mine).

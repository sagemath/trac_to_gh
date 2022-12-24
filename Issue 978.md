# Issue 978: bug in Sequence __str__ method

archive/issues_000978.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nAndrey Novoseltsev \t \nDear William,\n\nI have printing issues with sequences, cr parameter is not processed correctly\nwhen it is False:\n\nsage: s = Sequence([1,2,3], cr=False)\nsage: s\n[1, 2, 3]\nsage: print s, str(s), repr(s)\n[\n1,\n2,\n3\n] [\n1,\n2,\n3\n] [1, 2, 3]\nsage: s = Sequence([1,2,3], cr=True)\nsage: s\n[\n1,\n2,\n3\n]\nsage: print s, str(s), repr(s)\n[\n1,\n2,\n3\n] [\n1,\n2,\n3\n] [\n1,\n2,\n3\n]\n\nI get this both under notebook and command line and it is somewhat unpleasant.\n\nThank you,\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/978\n\n",
    "created_at": "2007-10-24T02:27:44Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "bug in Sequence __str__ method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/978",
    "user": "was"
}
```
Assignee: somebody


```
Andrey Novoseltsev 	 
Dear William,

I have printing issues with sequences, cr parameter is not processed correctly
when it is False:

sage: s = Sequence([1,2,3], cr=False)
sage: s
[1, 2, 3]
sage: print s, str(s), repr(s)
[
1,
2,
3
] [
1,
2,
3
] [1, 2, 3]
sage: s = Sequence([1,2,3], cr=True)
sage: s
[
1,
2,
3
]
sage: print s, str(s), repr(s)
[
1,
2,
3
] [
1,
2,
3
] [
1,
2,
3
]

I get this both under notebook and command line and it is somewhat unpleasant.

Thank you,
```


Issue created by migration from https://trac.sagemath.org/ticket/978





---

archive/issue_comments_005967.json:
```json
{
    "body": "Attachment [7085.patch](tarball://root/attachments/some-uuid/ticket978/7085.patch) by was created at 2007-10-24 02:29:57",
    "created_at": "2007-10-24T02:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/978#issuecomment-5967",
    "user": "was"
}
```

Attachment [7085.patch](tarball://root/attachments/some-uuid/ticket978/7085.patch) by was created at 2007-10-24 02:29:57



---

archive/issue_comments_005968.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-24T19:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/978#issuecomment-5968",
    "user": "malb"
}
```

Resolution: fixed



---

archive/issue_comments_005969.json:
```json
{
    "body": "applied to 2.8.9.alpha1",
    "created_at": "2007-10-24T19:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/978#issuecomment-5969",
    "user": "malb"
}
```

applied to 2.8.9.alpha1

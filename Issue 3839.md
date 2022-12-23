# Issue 3839: Element access for RElement

archive/issues_003839.json:
```json
{
    "body": "Assignee: SimonKing\n\nKeywords: r interface, element access\n\nOn [http://groups.google.com/group/sage-support/browse_thread/thread/4868d601510e9642?hl=en](http://groups.google.com/group/sage-support/browse_thread/thread/4868d601510e9642?hl=en), Alexandr Batalshikov pointed out that\n\n```\n> v = c(3,5,9,1)\n> v[c(2,3)]\n[1] 5 9 \n```\n\nworks in R, but the corresponding statement in Sage does not:\n\n```\nsage: v = r.c(3,5,9,1)\nsage: n = r.c(2,3)\nsage: v[n]\n[1] 3\n```\n\n\nI believe this is a defect. With the attached patch, the following works:\n\n```\nsage: v = r.c(3,5,9,1)\nsage: n = r.c(2,3)\nsage: v[n]\n[1] 5 9\nsage: v[-2]\n[1] 3 9 1\nsage: v['c(2,3)']\n[1] 5 9\nsage: v[2,4,3]\n[1] 5 1 9\nsage: v[2]\n[1] 5\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3839\n\n",
    "created_at": "2008-08-13T17:29:17Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "Element access for RElement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3839",
    "user": "SimonKing"
}
```
Assignee: SimonKing

Keywords: r interface, element access

On [http://groups.google.com/group/sage-support/browse_thread/thread/4868d601510e9642?hl=en](http://groups.google.com/group/sage-support/browse_thread/thread/4868d601510e9642?hl=en), Alexandr Batalshikov pointed out that

```
> v = c(3,5,9,1)
> v[c(2,3)]
[1] 5 9 
```

works in R, but the corresponding statement in Sage does not:

```
sage: v = r.c(3,5,9,1)
sage: n = r.c(2,3)
sage: v[n]
[1] 3
```


I believe this is a defect. With the attached patch, the following works:

```
sage: v = r.c(3,5,9,1)
sage: n = r.c(2,3)
sage: v[n]
[1] 5 9
sage: v[-2]
[1] 3 9 1
sage: v['c(2,3)']
[1] 5 9
sage: v[2,4,3]
[1] 5 1 9
sage: v[2]
[1] 5
```



Issue created by migration from https://trac.sagemath.org/ticket/3839





---

archive/issue_comments_027301.json:
```json
{
    "body": "Attachment\n\nPatch relative to 3.1.alpha0",
    "created_at": "2008-08-13T17:29:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3839#issuecomment-27301",
    "user": "SimonKing"
}
```

Attachment

Patch relative to 3.1.alpha0



---

archive/issue_comments_027302.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-08-13T17:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3839#issuecomment-27302",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_027303.json:
```json
{
    "body": "This is a dupe of #3838.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-13T17:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3839#issuecomment-27303",
    "user": "mabshoff"
}
```

This is a dupe of #3838.

Cheers,

Michael

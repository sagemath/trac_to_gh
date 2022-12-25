# Issue 3886: Plotting of digraphs is broken

archive/issues_003886.json:
```json
{
    "body": "Assignee: @rlmill\n\nKeywords: digraphs, graphs, graphics\n\nSee the attached images for the results of these commands (images produced by sagenb.org).\n\n\n```\nDiGraph({0:[1]}).show()\n```\n\n\n\n```\nDiGraph({0:[1], 1:[2]}).show()\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3886\n\n",
    "created_at": "2008-08-18T03:53:19Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Plotting of digraphs is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3886",
    "user": "https://github.com/saliola"
}
```
Assignee: @rlmill

Keywords: digraphs, graphs, graphics

See the attached images for the results of these commands (images produced by sagenb.org).


```
DiGraph({0:[1]}).show()
```



```
DiGraph({0:[1], 1:[2]}).show()
```


Issue created by migration from https://trac.sagemath.org/ticket/3886





---

archive/issue_comments_027668.json:
```json
{
    "body": "Attachment [sage0.png](tarball://root/attachments/some-uuid/ticket3886/sage0.png) by @saliola created at 2008-08-18 03:53:45\n\nFirst example.",
    "created_at": "2008-08-18T03:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3886#issuecomment-27668",
    "user": "https://github.com/saliola"
}
```

Attachment [sage0.png](tarball://root/attachments/some-uuid/ticket3886/sage0.png) by @saliola created at 2008-08-18 03:53:45

First example.



---

archive/issue_comments_027669.json:
```json
{
    "body": "Second example",
    "created_at": "2008-08-18T03:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3886#issuecomment-27669",
    "user": "https://github.com/saliola"
}
```

Second example



---

archive/issue_comments_027670.json:
```json
{
    "body": "Attachment [sage1.png](tarball://root/attachments/some-uuid/ticket3886/sage1.png) by @rlmill created at 2008-08-18 14:39:24\n\nFranco,\n\nThis is caused by/related to #3877 and #3880.",
    "created_at": "2008-08-18T14:39:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3886#issuecomment-27670",
    "user": "https://github.com/rlmill"
}
```

Attachment [sage1.png](tarball://root/attachments/some-uuid/ticket3886/sage1.png) by @rlmill created at 2008-08-18 14:39:24

Franco,

This is caused by/related to #3877 and #3880.



---

archive/issue_comments_027671.json:
```json
{
    "body": "rlm: are you saying that fixing #3877 and #3880 should fix the problem?",
    "created_at": "2008-08-18T20:47:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3886#issuecomment-27671",
    "user": "https://github.com/jasongrout"
}
```

rlm: are you saying that fixing #3877 and #3880 should fix the problem?



---

archive/issue_comments_027672.json:
```json
{
    "body": "Fixed by the patch at #3880.",
    "created_at": "2008-08-19T01:22:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3886#issuecomment-27672",
    "user": "https://github.com/rlmill"
}
```

Fixed by the patch at #3880.



---

archive/issue_comments_027673.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-19T01:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3886#issuecomment-27673",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027674.json:
```json
{
    "body": "Fixed by merging #3880.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-19T01:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3886#issuecomment-27674",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed by merging #3880.

Cheers,

Michael

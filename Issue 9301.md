# Issue 9301: Modified check_edge_label in the sparse graph backend to consider equals the same objects rather than objects with the same contents

archive/issues_009301.json:
```json
{
    "body": "Assignee: jason, mvngu, ncohen, rlm\n\nCC:  nathann.cohen@gmail.com\n\nKeywords: graph,label\n\nModified check_edge_label in the sparse graph backend to consider equals the same objects rather than objects with the same contents. Discussion and example here: http://groups.google.com/group/sage-devel/browse_thread/thread/310fba4f1c119e63#\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9301\n\n",
    "created_at": "2010-06-21T23:11:15Z",
    "labels": [
        "graph theory",
        "minor",
        "bug"
    ],
    "title": "Modified check_edge_label in the sparse graph backend to consider equals the same objects rather than objects with the same contents",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9301",
    "user": "comick"
}
```
Assignee: jason, mvngu, ncohen, rlm

CC:  nathann.cohen@gmail.com

Keywords: graph,label

Modified check_edge_label in the sparse graph backend to consider equals the same objects rather than objects with the same contents. Discussion and example here: http://groups.google.com/group/sage-devel/browse_thread/thread/310fba4f1c119e63#


Issue created by migration from https://trac.sagemath.org/ticket/9301





---

archive/issue_comments_087610.json:
```json
{
    "body": "Attachment\n\nPatch",
    "created_at": "2010-06-21T23:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87610",
    "user": "comick"
}
```

Attachment

Patch



---

archive/issue_comments_087611.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-21T23:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87611",
    "user": "comick"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087612.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-17T14:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87612",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087613.json:
```json
{
    "body": "Since this is a bug fix, you need to include a doctest which illustrates the bug you are fixing.",
    "created_at": "2010-07-17T14:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87613",
    "user": "rlm"
}
```

Since this is a bug fix, you need to include a doctest which illustrates the bug you are fixing.



---

archive/issue_comments_087614.json:
```json
{
    "body": "Doctest for bad behavior.",
    "created_at": "2010-08-21T22:59:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87614",
    "user": "comick"
}
```

Doctest for bad behavior.



---

archive/issue_comments_087615.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-21T23:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87615",
    "user": "comick"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_087616.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-08-21T23:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87616",
    "user": "comick"
}
```

Attachment



---

archive/issue_comments_087617.json:
```json
{
    "body": "Attachment\n\nReplaces previous patch - added trac # to commit message.",
    "created_at": "2010-08-31T17:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87617",
    "user": "rlm"
}
```

Attachment

Replaces previous patch - added trac # to commit message.



---

archive/issue_comments_087618.json:
```json
{
    "body": "There is a fly in the ointment:\n\nDuring one of the last NetworkX upgrades, many common Sage graph constructors were modified to give empty dictionaries as labels instead of None. I have been intending to fix many of Sage's graph generators not to depend on NetworkX (since simply constructing a CGraph would be much quicker), and revert the edge situation back to having labels equal to `None`. But until that happens, this patch causes several failures:\n\n\n```\nsage -t -long \"devel/sage-main/sage/graphs/generic_graph.py\"\nsage -t -long \"devel/sage-main/sage/graphs/base/sparse_graph.pyx\"\nsage -t -long \"devel/sage-main/sage/graphs/graph.py\"\n```\n\n\nAlso, I've changed the \"Report Upstream\" since here we *are* the upstream.",
    "created_at": "2010-08-31T17:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87618",
    "user": "rlm"
}
```

There is a fly in the ointment:

During one of the last NetworkX upgrades, many common Sage graph constructors were modified to give empty dictionaries as labels instead of None. I have been intending to fix many of Sage's graph generators not to depend on NetworkX (since simply constructing a CGraph would be much quicker), and revert the edge situation back to having labels equal to `None`. But until that happens, this patch causes several failures:


```
sage -t -long "devel/sage-main/sage/graphs/generic_graph.py"
sage -t -long "devel/sage-main/sage/graphs/base/sparse_graph.pyx"
sage -t -long "devel/sage-main/sage/graphs/graph.py"
```


Also, I've changed the "Report Upstream" since here we *are* the upstream.



---

archive/issue_comments_087619.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-31T17:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87619",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087620.json:
```json
{
    "body": "It seems that this issue has been fixed long time ago. So I propose to close this ticket.",
    "created_at": "2021-10-19T12:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87620",
    "user": "dcoudert"
}
```

It seems that this issue has been fixed long time ago. So I propose to close this ticket.



---

archive/issue_comments_087621.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2021-10-19T12:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87621",
    "user": "dcoudert"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_087622.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-10-25T15:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9301",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9301#issuecomment-87622",
    "user": "mkoeppe"
}
```

Resolution: invalid

# Issue 4054: [with patch, needs review] shorten doctesting in graph_generators.py

archive/issues_004054.json:
```json
{
    "body": "Assignee: tbd\n\nOn my MacBook Pro, before this patch:\n\n```\nsage -t  devel/sage-main/sage/graphs/graph_generators.py    \n\t [117.4 s]\nsage -t -long devel/sage-main/sage/graphs/graph_generators.py\n\t [242.7 s]\n```\n\n\nAnd after this patch:\n\n```\nsage -t  devel/sage-main/sage/graphs/graph_generators.py    \n\t [20.7 s]\nsage -t -long devel/sage-main/sage/graphs/graph_generators.py\n\t [86.9 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4054\n\n",
    "created_at": "2008-09-03T22:53:32Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] shorten doctesting in graph_generators.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4054",
    "user": "rlm"
}
```
Assignee: tbd

On my MacBook Pro, before this patch:

```
sage -t  devel/sage-main/sage/graphs/graph_generators.py    
	 [117.4 s]
sage -t -long devel/sage-main/sage/graphs/graph_generators.py
	 [242.7 s]
```


And after this patch:

```
sage -t  devel/sage-main/sage/graphs/graph_generators.py    
	 [20.7 s]
sage -t -long devel/sage-main/sage/graphs/graph_generators.py
	 [86.9 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/4054





---

archive/issue_comments_029221.json:
```json
{
    "body": "Changing assignee from tbd to rlm.",
    "created_at": "2008-09-03T23:25:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4054#issuecomment-29221",
    "user": "rlm"
}
```

Changing assignee from tbd to rlm.



---

archive/issue_comments_029222.json:
```json
{
    "body": "Hi,\n\nI would make the \"not tested\" \"long\" since one day we will have a framework that compares expected with actual plotting output. Other than that positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T00:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4054#issuecomment-29222",
    "user": "mabshoff"
}
```

Hi,

I would make the "not tested" "long" since one day we will have a framework that compares expected with actual plotting output. Other than that positive review.

Cheers,

Michael



---

archive/issue_comments_029223.json:
```json
{
    "body": "Attachment [trac_4054-long_docs.patch](tarball://root/attachments/some-uuid/ticket4054/trac_4054-long_docs.patch) by rlm created at 2008-09-04 22:54:41",
    "created_at": "2008-09-04T22:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4054#issuecomment-29223",
    "user": "rlm"
}
```

Attachment [trac_4054-long_docs.patch](tarball://root/attachments/some-uuid/ticket4054/trac_4054-long_docs.patch) by rlm created at 2008-09-04 22:54:41



---

archive/issue_comments_029224.json:
```json
{
    "body": "Positive review now that the \"not tested\" have been converted.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T23:02:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4054#issuecomment-29224",
    "user": "mabshoff"
}
```

Positive review now that the "not tested" have been converted.

Cheers,

Michael



---

archive/issue_comments_029225.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-04T23:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4054#issuecomment-29225",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029226.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc0",
    "created_at": "2008-09-04T23:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4054#issuecomment-29226",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc0

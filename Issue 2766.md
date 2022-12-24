# Issue 2766: graph adjacency matrix defaults to sparse

archive/issues_002766.json:
```json
{
    "body": "Assignee: rlm\n\nWhen a graph is small or dense, the adjacency matrix should be a dense matrix.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2766\n\n",
    "created_at": "2008-04-02T02:24:18Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "graph adjacency matrix defaults to sparse",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2766",
    "user": "jason"
}
```
Assignee: rlm

When a graph is small or dense, the adjacency matrix should be a dense matrix.

Issue created by migration from https://trac.sagemath.org/ticket/2766





---

archive/issue_comments_018996.json:
```json
{
    "body": "This is the ONLY patch---ignore all others.",
    "created_at": "2008-04-02T03:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2766#issuecomment-18996",
    "user": "jason"
}
```

This is the ONLY patch---ignore all others.



---

archive/issue_comments_018997.json:
```json
{
    "body": "Attachment [trac-2766-graph-am-dense.patch](tarball://root/attachments/some-uuid/ticket2766/trac-2766-graph-am-dense.patch) by jason created at 2008-04-02 03:14:47\n\nIgnore the .2.patch file---it contains unrelated changes by accident.",
    "created_at": "2008-04-02T03:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2766#issuecomment-18997",
    "user": "jason"
}
```

Attachment [trac-2766-graph-am-dense.patch](tarball://root/attachments/some-uuid/ticket2766/trac-2766-graph-am-dense.patch) by jason created at 2008-04-02 03:14:47

Ignore the .2.patch file---it contains unrelated changes by accident.



---

archive/issue_comments_018998.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-02T07:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2766#issuecomment-18998",
    "user": "rlm"
}
```

Looks good to me.



---

archive/issue_comments_018999.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-02T19:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2766#issuecomment-18999",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha1



---

archive/issue_comments_019000.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-02T19:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2766#issuecomment-19000",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019001.json:
```json
{
    "body": "Please mention the fact that you didn't doctest:\n\n```\nsage -t -long devel/sage-main/sage/graphs/graph.py\n*********************************************************************\nFile \"graph.py\", line 505:\n    sage: m = matrix(G); m.parent()\nExpected:\n    Full MatrixSpace of 5 by 5 sparse matrices over Integer Ring\nGot:\n    Full MatrixSpace of 5 by 5 dense matrices over Integer Ring\n```\n\nand \n\n```\nsage -t -long devel/sage-main/sage/matrix/constructor.py \n**********************************************************************\nFile \"constructor.py\", line 136:\n    sage: m = matrix(g); m; m.parent()\nExpected:\n    [0 1 0 0 1 1 0 0 0 0]\n    [1 0 1 0 0 0 1 0 0 0]\n    [0 1 0 1 0 0 0 1 0 0]\n    [0 0 1 0 1 0 0 0 1 0]\n    [1 0 0 1 0 0 0 0 0 1]\n    [1 0 0 0 0 0 0 1 1 0]\n    [0 1 0 0 0 0 0 0 1 1]\n    [0 0 1 0 0 1 0 0 0 1]\n    [0 0 0 1 0 1 1 0 0 0]\n    [0 0 0 0 1 0 1 1 0 0]\n    Full MatrixSpace of 10 by 10 sparse matrices over Integer Ring\nGot:\n    [0 1 0 0 1 1 0 0 0 0]\n    [1 0 1 0 0 0 1 0 0 0]\n    [0 1 0 1 0 0 0 1 0 0]\n    [0 0 1 0 1 0 0 0 1 0]\n    [1 0 0 1 0 0 0 0 0 1]\n    [1 0 0 0 0 0 0 1 1 0]\n    [0 1 0 0 0 0 0 0 1 1]\n    [0 0 1 0 0 1 0 0 0 1]\n    [0 0 0 1 0 1 1 0 0 0]\n    [0 0 0 0 1 0 1 1 0 0]\n    Full MatrixSpace of 10 by 10 dense matrices over Integer Ring\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-04-02T20:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2766#issuecomment-19001",
    "user": "mabshoff"
}
```

Please mention the fact that you didn't doctest:

```
sage -t -long devel/sage-main/sage/graphs/graph.py
*********************************************************************
File "graph.py", line 505:
    sage: m = matrix(G); m.parent()
Expected:
    Full MatrixSpace of 5 by 5 sparse matrices over Integer Ring
Got:
    Full MatrixSpace of 5 by 5 dense matrices over Integer Ring
```

and 

```
sage -t -long devel/sage-main/sage/matrix/constructor.py 
**********************************************************************
File "constructor.py", line 136:
    sage: m = matrix(g); m; m.parent()
Expected:
    [0 1 0 0 1 1 0 0 0 0]
    [1 0 1 0 0 0 1 0 0 0]
    [0 1 0 1 0 0 0 1 0 0]
    [0 0 1 0 1 0 0 0 1 0]
    [1 0 0 1 0 0 0 0 0 1]
    [1 0 0 0 0 0 0 1 1 0]
    [0 1 0 0 0 0 0 0 1 1]
    [0 0 1 0 0 1 0 0 0 1]
    [0 0 0 1 0 1 1 0 0 0]
    [0 0 0 0 1 0 1 1 0 0]
    Full MatrixSpace of 10 by 10 sparse matrices over Integer Ring
Got:
    [0 1 0 0 1 1 0 0 0 0]
    [1 0 1 0 0 0 1 0 0 0]
    [0 1 0 1 0 0 0 1 0 0]
    [0 0 1 0 1 0 0 0 1 0]
    [1 0 0 1 0 0 0 0 0 1]
    [1 0 0 0 0 0 0 1 1 0]
    [0 1 0 0 0 0 0 0 1 1]
    [0 0 1 0 0 1 0 0 0 1]
    [0 0 0 1 0 1 1 0 0 0]
    [0 0 0 0 1 0 1 1 0 0]
    Full MatrixSpace of 10 by 10 dense matrices over Integer Ring
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_019002.json:
```json
{
    "body": "Reviewer asleep? :)",
    "created_at": "2008-04-02T20:52:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2766#issuecomment-19002",
    "user": "mabshoff"
}
```

Reviewer asleep? :)



---

archive/issue_comments_019003.json:
```json
{
    "body": "Attachment [trac_2766-fix-doctests.patch](tarball://root/attachments/some-uuid/ticket2766/trac_2766-fix-doctests.patch) by mabshoff created at 2008-04-02 20:52:33\n\nMerged trac_2766-fix-doctests.patch in Sage 3.0.alpha1",
    "created_at": "2008-04-02T20:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2766#issuecomment-19003",
    "user": "mabshoff"
}
```

Attachment [trac_2766-fix-doctests.patch](tarball://root/attachments/some-uuid/ticket2766/trac_2766-fix-doctests.patch) by mabshoff created at 2008-04-02 20:52:33

Merged trac_2766-fix-doctests.patch in Sage 3.0.alpha1

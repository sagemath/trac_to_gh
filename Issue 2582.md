# Issue 2582: [with patch, needs review] fix bug in PermutationGroupElement

archive/issues_002582.json:
```json
{
    "body": "Assignee: robertwb\n\n\n```\nsage: PermutationGroupElement([1,2,4,3,5])\n---------------------------------------------------------------------------\n<type 'exceptions.AssertionError'>        Traceback (most recent call last)\n\n/Users/rlmill/sage-2.10.4/<ipython console> in <module>()\n\n/Users/rlmill/sage-2.10.4/permgroup_element.pyx in sage.groups.perm_gps.permgroup_element.PermutationGroupElement.__init__()\n\n<type 'exceptions.AssertionError'>: \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2582\n\n",
    "created_at": "2008-03-18T07:29:53Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] fix bug in PermutationGroupElement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2582",
    "user": "rlm"
}
```
Assignee: robertwb


```
sage: PermutationGroupElement([1,2,4,3,5])
---------------------------------------------------------------------------
<type 'exceptions.AssertionError'>        Traceback (most recent call last)

/Users/rlmill/sage-2.10.4/<ipython console> in <module>()

/Users/rlmill/sage-2.10.4/permgroup_element.pyx in sage.groups.perm_gps.permgroup_element.PermutationGroupElement.__init__()

<type 'exceptions.AssertionError'>: 
```


Issue created by migration from https://trac.sagemath.org/ticket/2582





---

archive/issue_comments_017670.json:
```json
{
    "body": "Attachment [2582-perm-gp-elt-list.patch](tarball://root/attachments/some-uuid/ticket2582/2582-perm-gp-elt-list.patch) by rlm created at 2008-03-18 07:37:35",
    "created_at": "2008-03-18T07:37:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2582#issuecomment-17670",
    "user": "rlm"
}
```

Attachment [2582-perm-gp-elt-list.patch](tarball://root/attachments/some-uuid/ticket2582/2582-perm-gp-elt-list.patch) by rlm created at 2008-03-18 07:37:35



---

archive/issue_comments_017671.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0.",
    "created_at": "2008-03-18T10:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2582#issuecomment-17671",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha0.



---

archive/issue_comments_017672.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-18T10:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2582#issuecomment-17672",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017673.json:
```json
{
    "body": "For the record: You posted a GNU patch and not a mercurial patch, so I ended up with credit in the hg log :). I need to start looking at patches before I merge so that this doesn't happen again. Note: you can export mercurial patches from mercurial ques.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-18T10:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2582#issuecomment-17673",
    "user": "mabshoff"
}
```

For the record: You posted a GNU patch and not a mercurial patch, so I ended up with credit in the hg log :). I need to start looking at patches before I merge so that this doesn't happen again. Note: you can export mercurial patches from mercurial ques.

Cheers,

Michael

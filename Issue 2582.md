# Issue 2582: [with patch, needs review] fix bug in PermutationGroupElement

archive/issues_002582.json:
```json
{
    "body": "Assignee: @robertwb\n\n\n```\nsage: PermutationGroupElement([1,2,4,3,5])\n---------------------------------------------------------------------------\n<type 'exceptions.AssertionError'>        Traceback (most recent call last)\n\n/Users/rlmill/sage-2.10.4/<ipython console> in <module>()\n\n/Users/rlmill/sage-2.10.4/permgroup_element.pyx in sage.groups.perm_gps.permgroup_element.PermutationGroupElement.__init__()\n\n<type 'exceptions.AssertionError'>: \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2582\n\n",
    "created_at": "2008-03-18T07:29:53Z",
    "labels": [
        "component: group theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch, needs review] fix bug in PermutationGroupElement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2582",
    "user": "https://github.com/rlmill"
}
```
Assignee: @robertwb


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

archive/issue_comments_017632.json:
```json
{
    "body": "Attachment [2582-perm-gp-elt-list.patch](tarball://root/attachments/some-uuid/ticket2582/2582-perm-gp-elt-list.patch) by @rlmill created at 2008-03-18 07:37:35",
    "created_at": "2008-03-18T07:37:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2582#issuecomment-17632",
    "user": "https://github.com/rlmill"
}
```

Attachment [2582-perm-gp-elt-list.patch](tarball://root/attachments/some-uuid/ticket2582/2582-perm-gp-elt-list.patch) by @rlmill created at 2008-03-18 07:37:35



---

archive/issue_comments_017633.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0.",
    "created_at": "2008-03-18T10:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2582#issuecomment-17633",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha0.



---

archive/issue_comments_017634.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-18T10:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2582#issuecomment-17634",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017635.json:
```json
{
    "body": "For the record: You posted a GNU patch and not a mercurial patch, so I ended up with credit in the hg log :). I need to start looking at patches before I merge so that this doesn't happen again. Note: you can export mercurial patches from mercurial ques.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-18T10:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2582#issuecomment-17635",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the record: You posted a GNU patch and not a mercurial patch, so I ended up with credit in the hg log :). I need to start looking at patches before I merge so that this doesn't happen again. Note: you can export mercurial patches from mercurial ques.

Cheers,

Michael

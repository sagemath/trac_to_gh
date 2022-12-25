# Issue 4239: [with patch, needs review] fix for problems with zero kernel and images

archive/issues_004239.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: kernel, image\n\nComputation of kernels and images of linear transformations over `GF(p)` (`p` odd) and `CC` fails when the result is zero.\nThe patch solves the problem by adjusting `FreeModule_submodule_with_basis_pid` so that a `tuple` of generators gets changed into a `list` (something that happens anyway if `check == True`).  New doctests have been included.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4239\n\n",
    "created_at": "2008-10-03T07:17:57Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with patch, needs review] fix for problems with zero kernel and images",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4239",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```
Assignee: tbd

Keywords: kernel, image

Computation of kernels and images of linear transformations over `GF(p)` (`p` odd) and `CC` fails when the result is zero.
The patch solves the problem by adjusting `FreeModule_submodule_with_basis_pid` so that a `tuple` of generators gets changed into a `list` (something that happens anyway if `check == True`).  New doctests have been included.

Issue created by migration from https://trac.sagemath.org/ticket/4239





---

archive/issue_comments_030749.json:
```json
{
    "body": "Attachment [sage-4239.patch](tarball://root/attachments/some-uuid/ticket4239/sage-4239.patch) by GeorgSWeber created at 2008-10-05 20:10:20\n\nThumbs up!\n\nLetting the new doctests run without the patch shows horrible behaviour indeed.\n\nPlease get this patch into 3.1.3.",
    "created_at": "2008-10-05T20:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4239#issuecomment-30749",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [sage-4239.patch](tarball://root/attachments/some-uuid/ticket4239/sage-4239.patch) by GeorgSWeber created at 2008-10-05 20:10:20

Thumbs up!

Letting the new doctests run without the patch shows horrible behaviour indeed.

Please get this patch into 3.1.3.



---

archive/issue_comments_030750.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha3",
    "created_at": "2008-10-07T21:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4239#issuecomment-30750",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha3



---

archive/issue_comments_030751.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-07T21:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4239#issuecomment-30751",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

# Issue 5848: [with patch, needs review] untabify Sage

archive/issues_005848.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nCC:  @roed314\n\nThe attached patch removes all of the TABs I could find in .py and .pyx files in the Sage library.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5848\n\n",
    "created_at": "2009-04-21T23:51:34Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "[with patch, needs review] untabify Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5848",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

CC:  @roed314

The attached patch removes all of the TABs I could find in .py and .pyx files in the Sage library.


Issue created by migration from https://trac.sagemath.org/ticket/5848





---

archive/issue_comments_046055.json:
```json
{
    "body": "Attachment [untabify.patch](tarball://root/attachments/some-uuid/ticket5848/untabify.patch) by @rbeezer created at 2009-04-22 04:45:07\n\nPatch choked twice on `modular/dirichlet.py`, which seems odd, given how fresh it is, and I can't really tell why.  I was applying it to an upgraded 3.4.1.rc4   Maybe it will patch better under mabshoff's firm guidance.\n\nBuilds just fine.  Passes `sage -testall`, except some unpickling errors in `structure/sage_object.pyx` and `algebras/quaternion_algebra_element.py` concerning `QuaternionAlgebraElements`, but the changes to these files don't appear implicated in these errors,\n\nDocumentation builds fine as well (PDF of reference manual) with no TeX errors.\n\nPositive review, subject to the business above about patching `modular/dirichlet.py`.",
    "created_at": "2009-04-22T04:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5848#issuecomment-46055",
    "user": "https://github.com/rbeezer"
}
```

Attachment [untabify.patch](tarball://root/attachments/some-uuid/ticket5848/untabify.patch) by @rbeezer created at 2009-04-22 04:45:07

Patch choked twice on `modular/dirichlet.py`, which seems odd, given how fresh it is, and I can't really tell why.  I was applying it to an upgraded 3.4.1.rc4   Maybe it will patch better under mabshoff's firm guidance.

Builds just fine.  Passes `sage -testall`, except some unpickling errors in `structure/sage_object.pyx` and `algebras/quaternion_algebra_element.py` concerning `QuaternionAlgebraElements`, but the changes to these files don't appear implicated in these errors,

Documentation builds fine as well (PDF of reference manual) with no TeX errors.

Positive review, subject to the business above about patching `modular/dirichlet.py`.



---

archive/issue_comments_046056.json:
```json
{
    "body": "I am not sure which rejects Rob saw, but it is applying fine for me.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T20:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5848#issuecomment-46056",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am not sure which rejects Rob saw, but it is applying fine for me.

Cheers,

Michael



---

archive/issue_comments_046057.json:
```json
{
    "body": "Replying to [comment:2 mabshoff]:\n> I am not sure which rejects Rob saw, but it is applying fine for me.\n\nSuperior Merge-Fu.  ;-)",
    "created_at": "2009-04-22T20:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5848#issuecomment-46057",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:2 mabshoff]:
> I am not sure which rejects Rob saw, but it is applying fine for me.

Superior Merge-Fu.  ;-)



---

archive/issue_comments_046058.json:
```json
{
    "body": "Ok, the patch still applies modulo three the diff for three files \n\n* sage/algebras/algebra_order.py\n* sage/algebras/algebra_order.py\n* sage/algebras/algebra_order_ideal.py\n\nthat no longer exist. This patch besides the latex one I just merged at #5610 has high risks for rejects, but since I merged the other one I might as well merge this one.\n\nDavid: Some of the padics files are touched, so if you rebase your patch bomb in the morning please also apply the patch I will post in a minute.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T09:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5848#issuecomment-46058",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, the patch still applies modulo three the diff for three files 

* sage/algebras/algebra_order.py
* sage/algebras/algebra_order.py
* sage/algebras/algebra_order_ideal.py

that no longer exist. This patch besides the latex one I just merged at #5610 has high risks for rejects, but since I merged the other one I might as well merge this one.

David: Some of the padics files are touched, so if you rebase your patch bomb in the morning please also apply the patch I will post in a minute.

Cheers,

Michael



---

archive/issue_comments_046059.json:
```json
{
    "body": "John's patch with the changes for three no longer existing files removed.",
    "created_at": "2009-04-24T09:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5848#issuecomment-46059",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

John's patch with the changes for three no longer existing files removed.



---

archive/issue_comments_046060.json:
```json
{
    "body": "Attachment [trac_5848_untabify.patch](tarball://root/attachments/some-uuid/ticket5848/trac_5848_untabify.patch) by mabshoff created at 2009-04-24 09:27:49\n\nMerged trac_5848_untabify.patch in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T09:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5848#issuecomment-46060",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5848_untabify.patch](tarball://root/attachments/some-uuid/ticket5848/trac_5848_untabify.patch) by mabshoff created at 2009-04-24 09:27:49

Merged trac_5848_untabify.patch in Sage 3.4.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_046061.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-24T09:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5848#issuecomment-46061",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

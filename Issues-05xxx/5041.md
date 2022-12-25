# Issue 5041: [with patch; positive review] make it so the magma .sig files in extcode don't get written there by magma

archive/issues_005041.json:
```json
{
    "body": "Assignee: @williamstein\n\nIf one installs sage sytem wide, and a user tries to run any magma commands, and the .sig files aren't written in data/extcode/magma, then BOOM!  This is a total show stopper for any \"normal users\" to use the sage magma interface for anything serious.  This must be FIXED!\n\nTo fix this, when the magma interface is first run, make sure to copy the .m files over to $DOT_SAGE/magma first and load from there.   One will have to do the copy the first time the magma interface is started in any magma session.   alternatively, one could try: except: the magma.load command, and if it fails, then try to copy and load from /tmp/, say or DOT_SAGE/temp/.  Maybe the second idea is cleaner. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5041\n\n",
    "closed_at": "2009-01-23T08:03:42Z",
    "created_at": "2009-01-20T23:34:43Z",
    "labels": [
        "component: interfaces",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch; positive review] make it so the magma .sig files in extcode don't get written there by magma",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5041",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

If one installs sage sytem wide, and a user tries to run any magma commands, and the .sig files aren't written in data/extcode/magma, then BOOM!  This is a total show stopper for any "normal users" to use the sage magma interface for anything serious.  This must be FIXED!

To fix this, when the magma interface is first run, make sure to copy the .m files over to $DOT_SAGE/magma first and load from there.   One will have to do the copy the first time the magma interface is started in any magma session.   alternatively, one could try: except: the magma.load command, and if it fails, then try to copy and load from /tmp/, say or DOT_SAGE/temp/.  Maybe the second idea is cleaner. 

Issue created by migration from https://trac.sagemath.org/ticket/5041





---

archive/issue_comments_038322.json:
```json
{
    "body": "The attached patch does the following:\n\n(1) Deletes magma/ell_padic and magma/padic_height which were only there for p-adic height computations before sage got its own much better native code.   Also, deletes the file SAGE_ROOT/devel/sage/sage/schemes/elliptic_curves/ell_padic.py, which was slated for deprecation officially several months ago, and just wraps those files.\n\nAND\n\n(2) The first (and only first) time a Magma interface is started in a given session, it copies over data/extcode/magma to a temp directory.   This directory is only 52 kilobytes, so this is fast and easy.  It will not grow much, since it is all hand written.    This is new code in magma.py.  It's just a few lines.  By doing this, all extcode code for mamga that we ever write can easily be attached without permission issues. \n\nTO TEST:\n(0) Apply all patches\n\n(1) doctest elliptic curves to make sure my removal of deprecated code didn't break anything:\n\n```\n$ sage -tp 3 devel/sage/sage/schemes/elliptic_curves/\n```\n\n(2) doctest the entire magma interface optional test code to make sure I didn't break anything:\n\n```\n$ ./sage -t -only_optional=magma devel/sage/sage/\n```\n\n(3) Read the source code modified in my patch to magma.py.",
    "created_at": "2009-01-22T11:33:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5041#issuecomment-38322",
    "user": "https://github.com/williamstein"
}
```

The attached patch does the following:

(1) Deletes magma/ell_padic and magma/padic_height which were only there for p-adic height computations before sage got its own much better native code.   Also, deletes the file SAGE_ROOT/devel/sage/sage/schemes/elliptic_curves/ell_padic.py, which was slated for deprecation officially several months ago, and just wraps those files.

AND

(2) The first (and only first) time a Magma interface is started in a given session, it copies over data/extcode/magma to a temp directory.   This directory is only 52 kilobytes, so this is fast and easy.  It will not grow much, since it is all hand written.    This is new code in magma.py.  It's just a few lines.  By doing this, all extcode code for mamga that we ever write can easily be attached without permission issues. 

TO TEST:
(0) Apply all patches

(1) doctest elliptic curves to make sure my removal of deprecated code didn't break anything:

```
$ sage -tp 3 devel/sage/sage/schemes/elliptic_curves/
```

(2) doctest the entire magma interface optional test code to make sure I didn't break anything:

```
$ ./sage -t -only_optional=magma devel/sage/sage/
```

(3) Read the source code modified in my patch to magma.py.



---

archive/issue_comments_038323.json:
```json
{
    "body": "Attachment [trac_5041-extcode_repo.patch](tarball://root/attachments/some-uuid/ticket5041/trac_5041-extcode_repo.patch) by @williamstein created at 2009-01-22 12:01:43",
    "created_at": "2009-01-22T12:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5041#issuecomment-38323",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5041-extcode_repo.patch](tarball://root/attachments/some-uuid/ticket5041/trac_5041-extcode_repo.patch) by @williamstein created at 2009-01-22 12:01:43



---

archive/issue_comments_038324.json:
```json
{
    "body": "> (0) Apply all patches\n\n\nWorks.\n \n> (1) doctest elliptic curves to make sure my removal of deprecated code didn't break anything:\n\n\nWorks.\n\n> (2) doctest the entire magma interface optional test code to make sure I didn't break anything:\n\n\nWorks. Also no .sig files are created in the extcode directory.\n\n> (3) Read the source code modified in my patch to magma.py.\n\n\nLooks good.",
    "created_at": "2009-01-22T20:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5041#issuecomment-38324",
    "user": "https://github.com/malb"
}
```

> (0) Apply all patches


Works.
 
> (1) doctest elliptic curves to make sure my removal of deprecated code didn't break anything:


Works.

> (2) doctest the entire magma interface optional test code to make sure I didn't break anything:


Works. Also no .sig files are created in the extcode directory.

> (3) Read the source code modified in my patch to magma.py.


Looks good.



---

archive/issue_comments_038325.json:
```json
{
    "body": "Merged both patches in Sage 3.3.alpha1",
    "created_at": "2009-01-23T08:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5041#issuecomment-38325",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.3.alpha1



---

archive/issue_comments_038326.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T08:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5041",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5041#issuecomment-38326",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_011620.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T08:03:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5041",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5041#event-11620"
}
```

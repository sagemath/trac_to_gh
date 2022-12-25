# Issue 4556: [with patch, needs review] nth_root for finite fields: document the fact that 'extend' is not implemented

archive/issues_004556.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: finite field, nth_root\n\nFrom a discussion on [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/a01375b02a8a65a0):\n\nThe documentation for the nth_root method for finite fields (repeated\nin each of the files sage/structure/element.pyx, sage/rings/\nfinite_field_element.py, and sage/rings/finite_field_givaro.pyx) says\nthis:\n\n```\n        INPUT:\n            n -- integer >= 1 (must fit in C int type)\n            extend -- bool (default: True); if True, return a square\n                 root in an extension ring, if necessary. Otherwise,\n                 raise a ValueError if the square is not in the base\n                 ring.\n            all -- bool (default: False); if True, return all square\n                 roots of self, instead of just one.\n\n        OUTPUT:\n           If self has an nth root, returns one (if all == False) or a list of\n           all of them (if all == True).  Otherwise, raises a ValueError (if\n           extend = False) or a NotImplementedError (if extend = True).\n```\nThe entirety of the code dealing with 'extend' is this:\n\n```\n        if extend:\n            raise NotImplementedError\n```\nThe non-implementation of the 'extend' option needs to be documented.  I've changed the docstrings to reflect this.  Also, \"square root\" needs to be changed to \"nth root\" several times.\n\n(The 'extend' issue also applies to the square_root method in finite_field_element.py.\nThe code for the sqrt method in finite_field_givaro.pyx is similar,\nbut the extend option, while present, isn't documented.)\n\nI'm attaching a patch to deal with these issues.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4556\n\n",
    "created_at": "2008-11-19T22:21:10Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "[with patch, needs review] nth_root for finite fields: document the fact that 'extend' is not implemented",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4556",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: somebody

Keywords: finite field, nth_root

From a discussion on [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/a01375b02a8a65a0):

The documentation for the nth_root method for finite fields (repeated
in each of the files sage/structure/element.pyx, sage/rings/
finite_field_element.py, and sage/rings/finite_field_givaro.pyx) says
this:

```
        INPUT:
            n -- integer >= 1 (must fit in C int type)
            extend -- bool (default: True); if True, return a square
                 root in an extension ring, if necessary. Otherwise,
                 raise a ValueError if the square is not in the base
                 ring.
            all -- bool (default: False); if True, return all square
                 roots of self, instead of just one.

        OUTPUT:
           If self has an nth root, returns one (if all == False) or a list of
           all of them (if all == True).  Otherwise, raises a ValueError (if
           extend = False) or a NotImplementedError (if extend = True).
```
The entirety of the code dealing with 'extend' is this:

```
        if extend:
            raise NotImplementedError
```
The non-implementation of the 'extend' option needs to be documented.  I've changed the docstrings to reflect this.  Also, "square root" needs to be changed to "nth root" several times.

(The 'extend' issue also applies to the square_root method in finite_field_element.py.
The code for the sqrt method in finite_field_givaro.pyx is similar,
but the extend option, while present, isn't documented.)

I'm attaching a patch to deal with these issues.


Issue created by migration from https://trac.sagemath.org/ticket/4556





---

archive/issue_comments_034074.json:
```json
{
    "body": "Attachment [nth_root.patch](tarball://root/attachments/some-uuid/ticket4556/nth_root.patch) by @jhpalmieri created at 2008-11-19 22:21:18",
    "created_at": "2008-11-19T22:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4556#issuecomment-34074",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [nth_root.patch](tarball://root/attachments/some-uuid/ticket4556/nth_root.patch) by @jhpalmieri created at 2008-11-19 22:21:18



---

archive/issue_comments_034075.json:
```json
{
    "body": "Just glancing at it it looks good.",
    "created_at": "2008-11-20T01:30:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4556#issuecomment-34075",
    "user": "https://github.com/robertwb"
}
```

Just glancing at it it looks good.



---

archive/issue_comments_034076.json:
```json
{
    "body": "Got a chance to look at it more. Thanks.",
    "created_at": "2008-11-21T06:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4556#issuecomment-34076",
    "user": "https://github.com/robertwb"
}
```

Got a chance to look at it more. Thanks.



---

archive/issue_comments_034077.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T09:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4556#issuecomment-34077",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034078.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-21T09:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4556#issuecomment-34078",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha0



---

archive/issue_events_010389.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-21T09:37:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4556",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4556#event-10389"
}
```

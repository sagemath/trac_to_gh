# Issue 4175: [with patch, needs review] cpdef arithmatic functions

archive/issues_004175.json:
```json
{
    "body": "Assignee: somebody\n\nRather than the `_xxx_, _xxx_c, _xxx_c_impl` stuff we have now. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4175\n\n",
    "created_at": "2008-09-23T07:17:14Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with patch, needs review] cpdef arithmatic functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4175",
    "user": "https://github.com/robertwb"
}
```
Assignee: somebody

Rather than the `_xxx_, _xxx_c, _xxx_c_impl` stuff we have now. 

Issue created by migration from https://trac.sagemath.org/ticket/4175





---

archive/issue_comments_030226.json:
```json
{
    "body": "Attachment [4175-no-impl.patch](tarball://root/attachments/some-uuid/ticket4175/4175-no-impl.patch) by @robertwb created at 2008-09-23 07:24:11\n\nThis gets rid of a lot of cruft and hundreds of lines of unneeded code now that we have cpdef functions (as well as hundreds of lines of ever .c function that cimports Element). \n\nAll tests pass with sage -testall.",
    "created_at": "2008-09-23T07:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4175#issuecomment-30226",
    "user": "https://github.com/robertwb"
}
```

Attachment [4175-no-impl.patch](tarball://root/attachments/some-uuid/ticket4175/4175-no-impl.patch) by @robertwb created at 2008-09-23 07:24:11

This gets rid of a lot of cruft and hundreds of lines of unneeded code now that we have cpdef functions (as well as hundreds of lines of ever .c function that cimports Element). 

All tests pass with sage -testall.



---

archive/issue_comments_030227.json:
```json
{
    "body": "I've looked over this code, and it looks good to me.  This is definitely way better than what we had before.  mabshoff, do you want to see if applies to your current tree / passes tests?",
    "created_at": "2008-09-23T22:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4175#issuecomment-30227",
    "user": "https://github.com/mwhansen"
}
```

I've looked over this code, and it looks good to me.  This is definitely way better than what we had before.  mabshoff, do you want to see if applies to your current tree / passes tests?



---

archive/issue_comments_030228.json:
```json
{
    "body": "The patch goes into my current merge tree with slight offsets here and there and I am building and testing now, but that will be a while. Before I import it: Are any of the coercion changes impacted by this patch, i.e. do the rebased patches still apply with this patch applied? Or should we wait to merge the coercion tickets first and then apply this patch?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-23T22:49:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4175#issuecomment-30228",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch goes into my current merge tree with slight offsets here and there and I am building and testing now, but that will be a while. Before I import it: Are any of the coercion changes impacted by this patch, i.e. do the rebased patches still apply with this patch applied? Or should we wait to merge the coercion tickets first and then apply this patch?

Cheers,

Michael



---

archive/issue_comments_030229.json:
```json
{
    "body": "They should be fairly orthogonal--I tried to keep them that way.\n\nThe Dickman's function patch you just merged will need the _impl_c methods renamed though.",
    "created_at": "2008-09-23T22:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4175#issuecomment-30229",
    "user": "https://github.com/robertwb"
}
```

They should be fairly orthogonal--I tried to keep them that way.

The Dickman's function patch you just merged will need the _impl_c methods renamed though.



---

archive/issue_comments_030230.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> They should be fairly orthogonal--I tried to keep them that way.\n\nGood, let's hope for the best.\n\n> The Dickman's function patch you just merged will need the _impl_c methods renamed though. \n\nCan you throw a patch on top for that function then? Should doctests and build pass I will merge this patch and the Diekman fix now.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-23T22:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4175#issuecomment-30230",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:4 robertwb]:
> They should be fairly orthogonal--I tried to keep them that way.

Good, let's hope for the best.

> The Dickman's function patch you just merged will need the _impl_c methods renamed though. 

Can you throw a patch on top for that function then? Should doctests and build pass I will merge this patch and the Diekman fix now.

Cheers,

Michael



---

archive/issue_comments_030231.json:
```json
{
    "body": "Attachment [4175-no-impl-RRx.patch](tarball://root/attachments/some-uuid/ticket4175/4175-no-impl-RRx.patch) by @robertwb created at 2008-09-23 23:08:15",
    "created_at": "2008-09-23T23:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4175#issuecomment-30231",
    "user": "https://github.com/robertwb"
}
```

Attachment [4175-no-impl-RRx.patch](tarball://root/attachments/some-uuid/ticket4175/4175-no-impl-RRx.patch) by @robertwb created at 2008-09-23 23:08:15



---

archive/issue_comments_030232.json:
```json
{
    "body": "OK, there's the patch. Yes, all doctests should pass.",
    "created_at": "2008-09-23T23:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4175#issuecomment-30232",
    "user": "https://github.com/robertwb"
}
```

OK, there's the patch. Yes, all doctests should pass.



---

archive/issue_comments_030233.json:
```json
{
    "body": "Merged both patches in Sage 3.1.3.alpha1. All doctests pass with the two patches applied.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T00:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4175#issuecomment-30233",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.1.3.alpha1. All doctests pass with the two patches applied.

Cheers,

Michael



---

archive/issue_comments_030234.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-24T00:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4175#issuecomment-30234",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004412.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-09-24T00:12:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4175",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4175#event-4412"
}
```

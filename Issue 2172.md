# Issue 2172: sage -sdist loses debian build infrastructure

archive/issues_002172.json:
```json
{
    "body": "Assignee: @timabbott\n\n$SAGE_ROOT/devel/sage/spkg-dist currently does not copy the debian directory as well as `spkg-debian-maybe`. It is easily fixed in `spkg-dist`, patch coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2172\n\n",
    "created_at": "2008-02-15T17:50:39Z",
    "labels": [
        "component: debian-package",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "sage -sdist loses debian build infrastructure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2172",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @timabbott

$SAGE_ROOT/devel/sage/spkg-dist currently does not copy the debian directory as well as `spkg-debian-maybe`. It is easily fixed in `spkg-dist`, patch coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2172





---

archive/issue_comments_014233.json:
```json
{
    "body": "Changing assignee from @timabbott to mabshoff.",
    "created_at": "2008-02-15T17:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2172#issuecomment-14233",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @timabbott to mabshoff.



---

archive/issue_comments_014234.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-15T17:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2172#issuecomment-14234",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014235.json:
```json
{
    "body": "Attachment [Sage-2.10.2.alpha1-trac_2172.patch](tarball://root/attachments/some-uuid/ticket2172/Sage-2.10.2.alpha1-trac_2172.patch) by mabshoff created at 2008-02-15 21:48:14",
    "created_at": "2008-02-15T21:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2172#issuecomment-14235",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.10.2.alpha1-trac_2172.patch](tarball://root/attachments/some-uuid/ticket2172/Sage-2.10.2.alpha1-trac_2172.patch) by mabshoff created at 2008-02-15 21:48:14



---

archive/issue_comments_014236.json:
```json
{
    "body": "If you need to work with 2.10.1, do this:\n\n\n```\n[5:02pm] ncalexan: mabshoff: I have files missing in sage-2.10.1.  All related to debian.\n[5:02pm] ncalexan: It means I can't apply that import patch.\n[5:02pm] ncalexan: Any ideas?\n[5:02pm] mabshoff: #2172\n[5:03pm] mabshoff: I fixed it in my alpha1, but the files will only show up once I do another sdist.\n[5:03pm] ncalexan: kk.\n[5:03pm] mabshoff: But the plan is to do that \"tonight\" and use 2.10.2.alpha1 as basis fir BD10.\n[5:03pm] mabshoff: \"-sdist\" is all magic and voodoo \n[5:04pm] mabshoff: Let's just say somebody ought to rewrite that POS properly down the road \n[5:04pm] ncalexan: So how do I use this for developing?  I can't commit anything right now.\n[5:04pm] mabshoff: ok, let me post a tarball with the missing files then.\n[5:05pm] ncalexan: Can I copy from my old tree?\n[5:08pm] mabshoff: Nick: http://sage.math.washington.edu/home/mabshoff/missing-debian.tar.gz\n[5:08pm] mabshoff: Move the files inside that dir into SAGE_ROOT/devel/sage\n[5:08pm] mabshoff: The files aren't in any old tree.\n```\n",
    "created_at": "2008-02-16T01:15:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2172#issuecomment-14236",
    "user": "https://github.com/ncalexan"
}
```

If you need to work with 2.10.1, do this:


```
[5:02pm] ncalexan: mabshoff: I have files missing in sage-2.10.1.  All related to debian.
[5:02pm] ncalexan: It means I can't apply that import patch.
[5:02pm] ncalexan: Any ideas?
[5:02pm] mabshoff: #2172
[5:03pm] mabshoff: I fixed it in my alpha1, but the files will only show up once I do another sdist.
[5:03pm] ncalexan: kk.
[5:03pm] mabshoff: But the plan is to do that "tonight" and use 2.10.2.alpha1 as basis fir BD10.
[5:03pm] mabshoff: "-sdist" is all magic and voodoo 
[5:04pm] mabshoff: Let's just say somebody ought to rewrite that POS properly down the road 
[5:04pm] ncalexan: So how do I use this for developing?  I can't commit anything right now.
[5:04pm] mabshoff: ok, let me post a tarball with the missing files then.
[5:05pm] ncalexan: Can I copy from my old tree?
[5:08pm] mabshoff: Nick: http://sage.math.washington.edu/home/mabshoff/missing-debian.tar.gz
[5:08pm] mabshoff: Move the files inside that dir into SAGE_ROOT/devel/sage
[5:08pm] mabshoff: The files aren't in any old tree.
```




---

archive/issue_comments_014237.json:
```json
{
    "body": "This needs to be applied.",
    "created_at": "2008-02-17T04:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2172#issuecomment-14237",
    "user": "https://github.com/ncalexan"
}
```

This needs to be applied.



---

archive/issue_events_005193.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-17T04:35:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2172",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2172#event-5193"
}
```



---

archive/issue_comments_014238.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-17T04:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2172#issuecomment-14238",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014239.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-17T04:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2172",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2172#issuecomment-14239",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha1

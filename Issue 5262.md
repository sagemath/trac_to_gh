# Issue 5262: L-series attached to modular forms has a major bug in how it computes the sign of the functional equation

archive/issues_005262.json:
```json
{
    "body": "Assignee: craigcitro\n\nThis is wrong:\n\n\n```\n\nThe following computation should produce identical values in the last\nline:\n\nE=EllipticCurve('37b2')\nh=E.modular_form()\nLh = h.cuspform_lseries()\nLE=E.lseries()\nh.elliptic_curve()==E, Lh(1), LE(1)\n\nThe output is:\n\n(True, 0, 0.725681061936153)\n```\n\n\nThis is because the Atkin-Lehner sign is computed wrong in sage/modular/modform/element.py.  In fact, there one finds the code:\n\n```\n            m = ModularSymbols(N,l,sign=1)\n            n = m.cuspidal_subspace().new_subspace()\n            e = (-1)**(l/2)*n.atkin_lehner_operator().matrix()[0,0]\n```\n\n\nNotice that m has absolutely nothing to do with the modular form! \n\nThe right fix is to implement an atkin_lehner_eigenvalue(...) function for modularforms, and that should in turn be implemented correctly, and should be called from the cuspform_lseries command.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5262\n\n",
    "created_at": "2009-02-14T00:47:10Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "L-series attached to modular forms has a major bug in how it computes the sign of the functional equation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5262",
    "user": "was"
}
```
Assignee: craigcitro

This is wrong:


```

The following computation should produce identical values in the last
line:

E=EllipticCurve('37b2')
h=E.modular_form()
Lh = h.cuspform_lseries()
LE=E.lseries()
h.elliptic_curve()==E, Lh(1), LE(1)

The output is:

(True, 0, 0.725681061936153)
```


This is because the Atkin-Lehner sign is computed wrong in sage/modular/modform/element.py.  In fact, there one finds the code:

```
            m = ModularSymbols(N,l,sign=1)
            n = m.cuspidal_subspace().new_subspace()
            e = (-1)**(l/2)*n.atkin_lehner_operator().matrix()[0,0]
```


Notice that m has absolutely nothing to do with the modular form! 

The right fix is to implement an atkin_lehner_eigenvalue(...) function for modularforms, and that should in turn be implemented correctly, and should be called from the cuspform_lseries command.

Issue created by migration from https://trac.sagemath.org/ticket/5262





---

archive/issue_comments_040393.json:
```json
{
    "body": "I already opened #5247 for this as I mentioned in the email, but I am closing that one as a dupe since this ticket has the better description.\n\nThis is not a ReST ticket, so bumping it to 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T02:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5262#issuecomment-40393",
    "user": "mabshoff"
}
```

I already opened #5247 for this as I mentioned in the email, but I am closing that one as a dupe since this ticket has the better description.

This is not a ReST ticket, so bumping it to 3.4.1.

Cheers,

Michael



---

archive/issue_comments_040394.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-01T08:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5262#issuecomment-40394",
    "user": "davidloeffler"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040395.json:
```json
{
    "body": "Changing assignee from craigcitro to davidloeffler.",
    "created_at": "2009-05-01T08:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5262#issuecomment-40395",
    "user": "davidloeffler"
}
```

Changing assignee from craigcitro to davidloeffler.



---

archive/issue_comments_040396.json:
```json
{
    "body": "patch against 3.4.2.rc0",
    "created_at": "2009-05-01T11:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5262#issuecomment-40396",
    "user": "davidloeffler"
}
```

patch against 3.4.2.rc0



---

archive/issue_comments_040397.json:
```json
{
    "body": "Attachment [trac_5262.patch](tarball://root/attachments/some-uuid/ticket5262/trac_5262.patch) by davidloeffler created at 2009-05-01 11:24:58\n\nTurns out there were actually two separate bugs: one for level 1 forms (which came up whenever the weight was not a multiple of 4) and one for forms of higher level. I've fixed both, and added doctests to check that they're fixed.",
    "created_at": "2009-05-01T11:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5262#issuecomment-40397",
    "user": "davidloeffler"
}
```

Attachment [trac_5262.patch](tarball://root/attachments/some-uuid/ticket5262/trac_5262.patch) by davidloeffler created at 2009-05-01 11:24:58

Turns out there were actually two separate bugs: one for level 1 forms (which came up whenever the weight was not a multiple of 4) and one for forms of higher level. I've fixed both, and added doctests to check that they're fixed.



---

archive/issue_comments_040398.json:
```json
{
    "body": "So I think this patch looks pretty good by eye ... but I tried to apply it to a clean 3.4.2.rc0 tree, and I got some merge failures. David, could you just check to make sure you've got the right version posted and I'll go ahead and review this? (The merge failures don't seem too hard to sort out, but it'll probably still be faster for David than me.)",
    "created_at": "2009-05-07T09:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5262#issuecomment-40398",
    "user": "craigcitro"
}
```

So I think this patch looks pretty good by eye ... but I tried to apply it to a clean 3.4.2.rc0 tree, and I got some merge failures. David, could you just check to make sure you've got the right version posted and I'll go ahead and review this? (The merge failures don't seem too hard to sort out, but it'll probably still be faster for David than me.)



---

archive/issue_comments_040399.json:
```json
{
    "body": "The merge failures are because the patch depends on my patch for #4357; I forgot to mention this in the description. Sorry. (This was because I independently implemented an \"atkin_lehner_eigenvalue\" function for newforms as part of fixing 4357, and then realised that this could be used to fix this one as well.)",
    "created_at": "2009-05-07T10:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5262#issuecomment-40399",
    "user": "davidloeffler"
}
```

The merge failures are because the patch depends on my patch for #4357; I forgot to mention this in the description. Sorry. (This was because I independently implemented an "atkin_lehner_eigenvalue" function for newforms as part of fixing 4357, and then realised that this could be used to fix this one as well.)



---

archive/issue_comments_040400.json:
```json
{
    "body": "Two thumbs up! I don't even see anything to nitpick about. Merge away!",
    "created_at": "2009-05-08T07:48:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5262#issuecomment-40400",
    "user": "craigcitro"
}
```

Two thumbs up! I don't even see anything to nitpick about. Merge away!



---

archive/issue_comments_040401.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T08:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5262#issuecomment-40401",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040402.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T08:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5262",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5262#issuecomment-40402",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael

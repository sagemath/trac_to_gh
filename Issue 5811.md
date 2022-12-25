# Issue 5811: Sage 3.4.1.rc3: Fedora 10/64 - type_reducible.py doctest failure due to '__cmp__"

archive/issues_005811.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @dwbump sage-combinat\n\nThis is also observable with FC9/64 bit with gcc 4.3.3 on SkyNet\n\n```\nsage -t -long \"devel/sage/sage/combinat/root_system/type_reducible.py\"\n**********************************************************************\nFile \"/space/wstein/farm/sage-3.4.1.rc3/devel/sage/sage/combinat/root_system/type_reducible.py\", line 53:\n    sage: [[x.__cmp__(y) for x in ct] for y in ct]\nExpected:\n    [[0, 1, -1], [-1, 0, -1], [1, 1, 0]]\nGot:\n    [[0, 1, 1], [-1, 0, 1], [1, 1, 0]]\n**********************************************************************\nFile \"/space/wstein/farm/sage-3.4.1.rc3/devel/sage/sage/combinat/root_system/type_reducible.py\", line 55:\n    sage: sorted(ct)\nExpected:\n    [['A', 4], A1xB2, B2xA1]\nGot:\n    [A1xB2, B2xA1, ['A', 4]]\n**********************************************************************\n```\n\n\nMaybe '__cmp__' is broken?\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5811\n\n",
    "created_at": "2009-04-17T11:29:02Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Sage 3.4.1.rc3: Fedora 10/64 - type_reducible.py doctest failure due to '__cmp__\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5811",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @dwbump sage-combinat

This is also observable with FC9/64 bit with gcc 4.3.3 on SkyNet

```
sage -t -long "devel/sage/sage/combinat/root_system/type_reducible.py"
**********************************************************************
File "/space/wstein/farm/sage-3.4.1.rc3/devel/sage/sage/combinat/root_system/type_reducible.py", line 53:
    sage: [[x.__cmp__(y) for x in ct] for y in ct]
Expected:
    [[0, 1, -1], [-1, 0, -1], [1, 1, 0]]
Got:
    [[0, 1, 1], [-1, 0, 1], [1, 1, 0]]
**********************************************************************
File "/space/wstein/farm/sage-3.4.1.rc3/devel/sage/sage/combinat/root_system/type_reducible.py", line 55:
    sage: sorted(ct)
Expected:
    [['A', 4], A1xB2, B2xA1]
Got:
    [A1xB2, B2xA1, ['A', 4]]
**********************************************************************
```


Maybe '__cmp__' is broken?

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5811





---

archive/issue_comments_045551.json:
```json
{
    "body": "Changing assignee from mabshoff to @mwhansen.",
    "created_at": "2009-04-18T06:22:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5811#issuecomment-45551",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from mabshoff to @mwhansen.



---

archive/issue_comments_045552.json:
```json
{
    "body": "Attachment [trac_5811.patch](tarball://root/attachments/some-uuid/ticket5811/trac_5811.patch) by @mwhansen created at 2009-04-18 06:22:10\n\n\n```\n<mhansen> mabs: Yep\n<mabs> Have you seen #5811 ?  [17:12]\n<mabs> It can be reproduced on the farm, i.e. the FC10 test box.\n<mabs> wstein can create you an account. \n<mhansen> Actually, it don't think we need that.  [17:14]\n<mhansen> It most likely comes from this line in cartan_type.py\n<mhansen>         if other.__class__ != self.__class__:\n<mhansen>             return cmp(self.__class__, other.__class__)\n<mhansen> \n<mabs> So you think it is a bug?  [17:15]\n<mhansen> Well, I think there are no guarantees on the results of class\n          comparisons.\n<mhansen> I would be fine with just changing that doctest since the order of\n          the types doesn't really matter.  [17:17]\n<mhansen> What matters most is deciding if they are equal or not.\n```\n",
    "created_at": "2009-04-18T06:22:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5811#issuecomment-45552",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5811.patch](tarball://root/attachments/some-uuid/ticket5811/trac_5811.patch) by @mwhansen created at 2009-04-18 06:22:10


```
<mhansen> mabs: Yep
<mabs> Have you seen #5811 ?  [17:12]
<mabs> It can be reproduced on the farm, i.e. the FC10 test box.
<mabs> wstein can create you an account. 
<mhansen> Actually, it don't think we need that.  [17:14]
<mhansen> It most likely comes from this line in cartan_type.py
<mhansen>         if other.__class__ != self.__class__:
<mhansen>             return cmp(self.__class__, other.__class__)
<mhansen> 
<mabs> So you think it is a bug?  [17:15]
<mhansen> Well, I think there are no guarantees on the results of class
          comparisons.
<mhansen> I would be fine with just changing that doctest since the order of
          the types doesn't really matter.  [17:17]
<mhansen> What matters most is deciding if they are equal or not.
```




---

archive/issue_comments_045553.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-18T06:22:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5811#issuecomment-45553",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045554.json:
```json
{
    "body": "Dan, \n\nsince this is in your back yard I figure it is worth CCing you.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T06:59:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5811#issuecomment-45554",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Dan, 

since this is in your back yard I figure it is worth CCing you.

Cheers,

Michael



---

archive/issue_comments_045555.json:
```json
{
    "body": "Ok, having read up on `__cmp___` I agree with Mike's patch. It also fixes the problem observed, so I am giving it a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-19T00:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5811#issuecomment-45555",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, having read up on `__cmp___` I agree with Mike's patch. It also fixes the problem observed, so I am giving it a positive review.

Cheers,

Michael



---

archive/issue_events_013639.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-19T00:12:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5811",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5811#event-13639"
}
```



---

archive/issue_comments_045556.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-19T00:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5811#issuecomment-45556",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_045557.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc4.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-19T00:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5811",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5811#issuecomment-45557",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc4.

Cheers,

Michael

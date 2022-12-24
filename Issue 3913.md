# Issue 3913: order function not defined for ideal classes

archive/issues_003913.json:
```json
{
    "body": "Assignee: was\n\nCC:  alexghitza\n\nIn 3.1 you can't ask for the order of an ideal class.  Example:\n\n```\nsage: K.<w>=QuadraticField(-23)\nsage: OK=K.ring_of_integers()\nsage: C=OK.class_group()\nsage: h=C.order()\nsage: P2a,P2b=[P for P,e in (2*OK).factor()]\nsage: c=C(P2a); c\nFractional ideal class (2, 1/2*w - 1/2)\nsage: c.order()\n#boom\n```\n\n\nThis is easily provided:\n\n```\nsage: sage.groups.generic.order_from_multiple(c,c.parent().order(),operation='*')\n3\n```\n\n\nPatch coming up.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3913\n\n",
    "created_at": "2008-08-20T16:36:43Z",
    "labels": [
        "number theory",
        "minor",
        "enhancement"
    ],
    "title": "order function not defined for ideal classes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3913",
    "user": "cremona"
}
```
Assignee: was

CC:  alexghitza

In 3.1 you can't ask for the order of an ideal class.  Example:

```
sage: K.<w>=QuadraticField(-23)
sage: OK=K.ring_of_integers()
sage: C=OK.class_group()
sage: h=C.order()
sage: P2a,P2b=[P for P,e in (2*OK).factor()]
sage: c=C(P2a); c
Fractional ideal class (2, 1/2*w - 1/2)
sage: c.order()
#boom
```


This is easily provided:

```
sage: sage.groups.generic.order_from_multiple(c,c.parent().order(),operation='*')
3
```


Patch coming up.


Issue created by migration from https://trac.sagemath.org/ticket/3913





---

archive/issue_comments_027988.json:
```json
{
    "body": "Attachment [sage-trac3913.patch](tarball://root/attachments/some-uuid/ticket3913/sage-trac3913.patch) by cremona created at 2008-08-20 17:02:04\n\nThe patch implements this, and adds doctests to some other functions.  Based on 3.1.1, and all doctests in sage/rings/number_fields pass.",
    "created_at": "2008-08-20T17:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3913#issuecomment-27988",
    "user": "cremona"
}
```

Attachment [sage-trac3913.patch](tarball://root/attachments/some-uuid/ticket3913/sage-trac3913.patch) by cremona created at 2008-08-20 17:02:04

The patch implements this, and adds doctests to some other functions.  Based on 3.1.1, and all doctests in sage/rings/number_fields pass.



---

archive/issue_comments_027989.json:
```json
{
    "body": "Looks good and passes doctests.  Also, when this gets merged, #1400 should be closed as a duplicate (note btw that John's patch addresses precisely Nick's objection on #1400).",
    "created_at": "2008-08-27T07:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3913#issuecomment-27989",
    "user": "AlexGhitza"
}
```

Looks good and passes doctests.  Also, when this gets merged, #1400 should be closed as a duplicate (note btw that John's patch addresses precisely Nick's objection on #1400).



---

archive/issue_comments_027990.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-27T07:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3913#issuecomment-27990",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027991.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha1",
    "created_at": "2008-08-27T07:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3913#issuecomment-27991",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha1



---

archive/issue_comments_027992.json:
```json
{
    "body": "Replying to [comment:3 AlexGhitza]:\n> Looks good and passes doctests.  Also, when this gets merged, #1400 should be closed as a duplicate (note btw that John's patch addresses precisely Nick's objection on #1400).\n\nThanks -- sorry to have opened a new ticket unnecessarily (I did look, honest).  In any case this patch is more efficient, and shows how useful the generic algorithms I implemented are!",
    "created_at": "2008-08-27T08:10:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3913#issuecomment-27992",
    "user": "cremona"
}
```

Replying to [comment:3 AlexGhitza]:
> Looks good and passes doctests.  Also, when this gets merged, #1400 should be closed as a duplicate (note btw that John's patch addresses precisely Nick's objection on #1400).

Thanks -- sorry to have opened a new ticket unnecessarily (I did look, honest).  In any case this patch is more efficient, and shows how useful the generic algorithms I implemented are!

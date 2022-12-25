# Issue 2480: problem parsing arguments to NumberField.order()

archive/issues_002480.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  @ncalexan @robertwb @mwhansen\n\nKeywords: number field order arguments\n\n```\nsage: y = ZZ['y'].0; K = NumberField(y^4 + 4*y^2 + 2, 'a'); K\nNumber Field in a with defining polynomial y^4 + 4*y^2 + 2\nsage: B = K.integral_basis()\nsage: B\n[1, a, a^2, a^3]\nsage: K.order(B)\nOrder in Number Field in a with defining polynomial y^4 + 4*y^2 + 2\nsage: K.order(gens=B)\n+Infinity\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2480\n\n",
    "closed_at": "2010-01-24T03:22:20Z",
    "created_at": "2008-03-12T03:19:59Z",
    "labels": [
        "component: number fields",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "problem parsing arguments to NumberField.order()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2480",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @loefflerd

CC:  @ncalexan @robertwb @mwhansen

Keywords: number field order arguments

```
sage: y = ZZ['y'].0; K = NumberField(y^4 + 4*y^2 + 2, 'a'); K
Number Field in a with defining polynomial y^4 + 4*y^2 + 2
sage: B = K.integral_basis()
sage: B
[1, a, a^2, a^3]
sage: K.order(B)
Order in Number Field in a with defining polynomial y^4 + 4*y^2 + 2
sage: K.order(gens=B)
+Infinity
```

Issue created by migration from https://trac.sagemath.org/ticket/2480





---

archive/issue_comments_016770.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T19:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2480#issuecomment-16770",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_016771.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-20T19:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2480#issuecomment-16771",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_016772.json:
```json
{
    "body": "This wasn't so bad -- the problem was that `gens=` put the list of gens in the `kwds` dict, instead of in the `*`-argument. I've attached a fix, but I'd love for someone to tell me if deleting `gens` out of the `kwds` dict is sufficiently pythonic. (If you don't, the call to `absolute_order_from_ring_generators` rightfully complains that `gens` is specified twice.) Another option would be to reassign `kwds['dict']` at the end, but I don't think that's any nicer. (In fact, that might be epsilon slower, since it's another argument to unpack from the dictionary on the other side.)\n\nAlso, the comment block in the docstring **really** looks like something was accidentally cut off at some point. Amusingly, this isn't the case: I actually dug through the hg logs, and it was really committed just like that.",
    "created_at": "2010-01-20T06:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2480#issuecomment-16772",
    "user": "https://github.com/craigcitro"
}
```

This wasn't so bad -- the problem was that `gens=` put the list of gens in the `kwds` dict, instead of in the `*`-argument. I've attached a fix, but I'd love for someone to tell me if deleting `gens` out of the `kwds` dict is sufficiently pythonic. (If you don't, the call to `absolute_order_from_ring_generators` rightfully complains that `gens` is specified twice.) Another option would be to reassign `kwds['dict']` at the end, but I don't think that's any nicer. (In fact, that might be epsilon slower, since it's another argument to unpack from the dictionary on the other side.)

Also, the comment block in the docstring **really** looks like something was accidentally cut off at some point. Amusingly, this isn't the case: I actually dug through the hg logs, and it was really committed just like that.



---

archive/issue_comments_016773.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T06:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2480#issuecomment-16773",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_016774.json:
```json
{
    "body": "Mike and Robert, I'm adding you on the cc so that you can tell me if I'm being sufficiently pythonic. `:)`",
    "created_at": "2010-01-20T06:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2480#issuecomment-16774",
    "user": "https://github.com/craigcitro"
}
```

Mike and Robert, I'm adding you on the cc so that you can tell me if I'm being sufficiently pythonic. `:)`



---

archive/issue_comments_016775.json:
```json
{
    "body": "Hey Craig,\n\n```\ngens = kwds.pop('gens')\n```\n\nis probably better.",
    "created_at": "2010-01-20T07:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2480#issuecomment-16775",
    "user": "https://github.com/mwhansen"
}
```

Hey Craig,

```
gens = kwds.pop('gens')
```

is probably better.



---

archive/issue_comments_016776.json:
```json
{
    "body": "Err,\n\n```\ngens = kwds.pop('gens', args)\n```",
    "created_at": "2010-01-20T07:05:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2480#issuecomment-16776",
    "user": "https://github.com/mwhansen"
}
```

Err,

```
gens = kwds.pop('gens', args)
```



---

archive/issue_comments_016777.json:
```json
{
    "body": "Attachment [trac_2480.patch](tarball://root/attachments/some-uuid/ticket2480/trac_2480.patch) by @craigcitro created at 2010-01-20 07:07:39\n\nNice. New patch with Mike's suggestion incorporated posted.",
    "created_at": "2010-01-20T07:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2480#issuecomment-16777",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_2480.patch](tarball://root/attachments/some-uuid/ticket2480/trac_2480.patch) by @craigcitro created at 2010-01-20 07:07:39

Nice. New patch with Mike's suggestion incorporated posted.



---

archive/issue_comments_016778.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T07:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2480#issuecomment-16778",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_005857.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-24T03:22:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2480",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2480#event-5857"
}
```



---

archive/issue_comments_016779.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-24T03:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2480",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2480#issuecomment-16779",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed

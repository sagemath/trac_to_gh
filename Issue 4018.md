# Issue 4018: casting of non t_INT pari integers

archive/issues_004018.json:
```json
{
    "body": "Assignee: @robertwb\n\n\n```\nsage: t = pari(0*ZZ[x].0); t\n 0\n\nsage: ZZ(t)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/robertwb/<ipython console> in <module>()\n\n/home/robertwb/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__ (sage/rings/integer_ring.c:4902)()\n\n/home/robertwb/integer.pyx in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:5812)()\n\n/home/robertwb/gen.pyx in sage.libs.pari.gen.gen.__hex__ (sage/libs/pari/gen.c:5840)()\n\nTypeError: gen must be of PARI type t_INT\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4018\n\n",
    "created_at": "2008-08-31T08:28:22Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "casting of non t_INT pari integers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4018",
    "user": "@robertwb"
}
```
Assignee: @robertwb


```
sage: t = pari(0*ZZ[x].0); t
 0

sage: ZZ(t)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/robertwb/<ipython console> in <module>()

/home/robertwb/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__ (sage/rings/integer_ring.c:4902)()

/home/robertwb/integer.pyx in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:5812)()

/home/robertwb/gen.pyx in sage.libs.pari.gen.gen.__hex__ (sage/libs/pari/gen.c:5840)()

TypeError: gen must be of PARI type t_INT
```


Issue created by migration from https://trac.sagemath.org/ticket/4018





---

archive/issue_comments_028980.json:
```json
{
    "body": "Attachment [4018-pari-to-zz.patch](tarball://root/attachments/some-uuid/ticket4018/4018-pari-to-zz.patch) by @robertwb created at 2008-08-31 08:43:30",
    "created_at": "2008-08-31T08:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4018#issuecomment-28980",
    "user": "@robertwb"
}
```

Attachment [4018-pari-to-zz.patch](tarball://root/attachments/some-uuid/ticket4018/4018-pari-to-zz.patch) by @robertwb created at 2008-08-31 08:43:30



---

archive/issue_comments_028981.json:
```json
{
    "body": "Looks good to me (tested it against 3.1.1).",
    "created_at": "2008-09-01T10:33:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4018#issuecomment-28981",
    "user": "@aghitza"
}
```

Looks good to me (tested it against 3.1.1).



---

archive/issue_comments_028982.json:
```json
{
    "body": "Line 358 in the patch needs to be changed to \n\n```\nsage: t = pari(0*ZZ[x].0 + 3)\n```\n\nWith that change the doctests for integer.pyx actually pass :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T13:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4018#issuecomment-28982",
    "user": "mabshoff"
}
```

Line 358 in the patch needs to be changed to 

```
sage: t = pari(0*ZZ[x].0 + 3)
```

With that change the doctests for integer.pyx actually pass :)

Cheers,

Michael



---

archive/issue_comments_028983.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-01T13:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4018#issuecomment-28983",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028984.json:
```json
{
    "body": "Merged in sage 3.1.2.alpha4",
    "created_at": "2008-09-01T13:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4018",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4018#issuecomment-28984",
    "user": "mabshoff"
}
```

Merged in sage 3.1.2.alpha4

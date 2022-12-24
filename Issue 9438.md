# Issue 9438: IntegerMod_int.log has side-effect in Pari

archive/issues_009438.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nKeywords: log finite field pari\n\nMotivated by a bug hunt for #2420, I found:\n\n```\nsage: R.<a, b> = QQ[]\nsage: b._pari_()\nb\nsage: GF(7)(5).log()\n5\nsage: b._pari_()\nMod(3, 7)\n```\n\n\nThe reason is that in the `log` method, the string\n\n```\n'b=Mod(%s,%s); if(znorder(b)!=eulerphi(%s),-1,znlog(%s,b))'%(b, self.__modulus.sageInteger,\n                                                                           self.__modulus.sageInteger, self)\n```\n\nis evaluated in `pari`, so that afterwards `pari('b')` isn't doing what it should.\n\nSince this bug is triggered whenever a GAP representation of a finite field element is created, I mark this ticket \"critical\". I hope \"basic arithmetic\" is the right component.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9438\n\n",
    "created_at": "2010-07-06T15:34:02Z",
    "labels": [
        "basic arithmetic",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "IntegerMod_int.log has side-effect in Pari",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9438",
    "user": "SimonKing"
}
```
Assignee: AlexGhitza

Keywords: log finite field pari

Motivated by a bug hunt for #2420, I found:

```
sage: R.<a, b> = QQ[]
sage: b._pari_()
b
sage: GF(7)(5).log()
5
sage: b._pari_()
Mod(3, 7)
```


The reason is that in the `log` method, the string

```
'b=Mod(%s,%s); if(znorder(b)!=eulerphi(%s),-1,znlog(%s,b))'%(b, self.__modulus.sageInteger,
                                                                           self.__modulus.sageInteger, self)
```

is evaluated in `pari`, so that afterwards `pari('b')` isn't doing what it should.

Since this bug is triggered whenever a GAP representation of a finite field element is created, I mark this ticket "critical". I hope "basic arithmetic" is the right component.

Issue created by migration from https://trac.sagemath.org/ticket/9438





---

archive/issue_comments_090354.json:
```json
{
    "body": "The patch seems to fix the bug. The string that is evaluated by PARI defines a variable 'b' and uses it exactly twice. The definition of 'b' is not so long: It is `b=Mod(m,n)`. OK, m and n can be large numbers. But still, I think the cleanest solution is to expand the definition and insert `Mod(m,n)` twice in the string.\n\nsage -t \"devel/sage/sage/rings/finite_rings/integer_mod.pyx\" passes, I now do sage -testall\n\nOf course, I added a doctest against the bug.",
    "created_at": "2010-07-06T17:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9438#issuecomment-90354",
    "user": "SimonKing"
}
```

The patch seems to fix the bug. The string that is evaluated by PARI defines a variable 'b' and uses it exactly twice. The definition of 'b' is not so long: It is `b=Mod(m,n)`. OK, m and n can be large numbers. But still, I think the cleanest solution is to expand the definition and insert `Mod(m,n)` twice in the string.

sage -t "devel/sage/sage/rings/finite_rings/integer_mod.pyx" passes, I now do sage -testall

Of course, I added a doctest against the bug.



---

archive/issue_comments_090355.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-06T17:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9438#issuecomment-90355",
    "user": "SimonKing"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090356.json:
```json
{
    "body": "`sage -testall` passes!",
    "created_at": "2010-07-06T18:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9438#issuecomment-90356",
    "user": "SimonKing"
}
```

`sage -testall` passes!



---

archive/issue_comments_090357.json:
```json
{
    "body": "This modifies exactly the same code as #9205 (which already has a positive review). Sadly I didn't spot this problem when I wrote that patch. Can you check to see if your patch applies OK on top of #9205, and if not, rebase it?\n\nDavid",
    "created_at": "2010-07-06T19:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9438#issuecomment-90357",
    "user": "davidloeffler"
}
```

This modifies exactly the same code as #9205 (which already has a positive review). Sadly I didn't spot this problem when I wrote that patch. Can you check to see if your patch applies OK on top of #9205, and if not, rebase it?

David



---

archive/issue_comments_090358.json:
```json
{
    "body": "Attachment [trac_9438_IntegerMod_log_vs_PARI.patch](tarball://root/attachments/some-uuid/ticket9438/trac_9438_IntegerMod_log_vs_PARI.patch) by SimonKing created at 2010-07-07 11:48:43\n\nFixes a side effect of log on PARI",
    "created_at": "2010-07-07T11:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9438#issuecomment-90358",
    "user": "SimonKing"
}
```

Attachment [trac_9438_IntegerMod_log_vs_PARI.patch](tarball://root/attachments/some-uuid/ticket9438/trac_9438_IntegerMod_log_vs_PARI.patch) by SimonKing created at 2010-07-07 11:48:43

Fixes a side effect of log on PARI



---

archive/issue_comments_090359.json:
```json
{
    "body": "Replying to [comment:3 davidloeffler]:\n> This modifies exactly the same code as #9205 (which already has a positive review). Sadly I \n> didn't spot this problem when I wrote that patch. Can you check to see if your patch applies OK \n> on top of #9205, and if not, rebase it?\n\nIt did not apply on top of #9205. So, I replaced the original patch by one that is to be applied after the two patches from #9205.\n\nCheers,\n\nSimon",
    "created_at": "2010-07-07T11:50:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9438#issuecomment-90359",
    "user": "SimonKing"
}
```

Replying to [comment:3 davidloeffler]:
> This modifies exactly the same code as #9205 (which already has a positive review). Sadly I 
> didn't spot this problem when I wrote that patch. Can you check to see if your patch applies OK 
> on top of #9205, and if not, rebase it?

It did not apply on top of #9205. So, I replaced the original patch by one that is to be applied after the two patches from #9205.

Cheers,

Simon



---

archive/issue_comments_090360.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-07T15:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9438#issuecomment-90360",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090361.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T09:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9438",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9438#issuecomment-90361",
    "user": "mpatel"
}
```

Resolution: fixed

# Issue 9384: descend_to method for elliptic curves

archive/issues_009384.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  adeines @JohnCremona jeremywest\n\nKeywords: descend, subfield, isomorphic, elliptic curve\n\nGiven a subfield K and an elliptic curve E defined over a field L, this function determines whether there exists an elliptic curve over K which is isomorphic over L to E. If one exists, it finds it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9384\n\n",
    "created_at": "2010-06-29T22:24:01Z",
    "labels": [
        "component: elliptic curves",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "descend_to method for elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9384",
    "user": "https://trac.sagemath.org/admin/accounts/users/ebeyerstedt"
}
```
Assignee: @JohnCremona

CC:  adeines @JohnCremona jeremywest

Keywords: descend, subfield, isomorphic, elliptic curve

Given a subfield K and an elliptic curve E defined over a field L, this function determines whether there exists an elliptic curve over K which is isomorphic over L to E. If one exists, it finds it.

Issue created by migration from https://trac.sagemath.org/ticket/9384





---

archive/issue_comments_089084.json:
```json
{
    "body": "This has been implemented in the patch. Please review.",
    "created_at": "2010-06-29T23:46:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9384#issuecomment-89084",
    "user": "https://trac.sagemath.org/admin/accounts/users/ebeyerstedt"
}
```

This has been implemented in the patch. Please review.



---

archive/issue_comments_089085.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-29T23:46:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9384#issuecomment-89085",
    "user": "https://trac.sagemath.org/admin/accounts/users/ebeyerstedt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089086.json:
```json
{
    "body": "Note: This function does not yet work when j = 0, 1728.",
    "created_at": "2010-06-30T02:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9384#issuecomment-89086",
    "user": "https://trac.sagemath.org/admin/accounts/users/ebeyerstedt"
}
```

Note: This function does not yet work when j = 0, 1728.



---

archive/issue_comments_089087.json:
```json
{
    "body": "Attachment [trac_9384.patch](tarball://root/attachments/some-uuid/ticket9384/trac_9384.patch) by ebeyerstedt created at 2010-06-30 03:00:59",
    "created_at": "2010-06-30T03:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9384#issuecomment-89087",
    "user": "https://trac.sagemath.org/admin/accounts/users/ebeyerstedt"
}
```

Attachment [trac_9384.patch](tarball://root/attachments/some-uuid/ticket9384/trac_9384.patch) by ebeyerstedt created at 2010-06-30 03:00:59



---

archive/issue_comments_089088.json:
```json
{
    "body": "The update handles the cases for j=0,1728.",
    "created_at": "2010-06-30T03:46:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9384#issuecomment-89088",
    "user": "https://trac.sagemath.org/admin/accounts/users/ebeyerstedt"
}
```

The update handles the cases for j=0,1728.



---

archive/issue_comments_089089.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-30T04:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9384#issuecomment-89089",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089090.json:
```json
{
    "body": "The code for handling j=0,1728 needs to be cleaned up a little. Also, this function currently does not properly handle the following case\n\nF.<b> = QuadraticField(23)\nK.<a> = F.extension(x^3+5)\nE = EllipticCurve(j = 1728*b).change_ring(K)\nE.descend_to(F)\n\nIt returns none when it should descend to the subfield F.",
    "created_at": "2010-06-30T04:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9384#issuecomment-89090",
    "user": "https://github.com/adeines"
}
```

The code for handling j=0,1728 needs to be cleaned up a little. Also, this function currently does not properly handle the following case

F.<b> = QuadraticField(23)
K.<a> = F.extension(x^3+5)
E = EllipticCurve(j = 1728*b).change_ring(K)
E.descend_to(F)

It returns none when it should descend to the subfield F.



---

archive/issue_comments_089091.json:
```json
{
    "body": "It looks to me as though the curve returned is (sometimes) a twist of the original, rather than isomorphic -- but I have been flying all night so am not reliable!\n\nYou can check if there is an embedding of K in self.base_ring() like this:\n\n```\nsage: X = polygen(QQ)\nsage: K.<a> = NumberField(X^4 - X^3 + 2*X^2 + X + 1)\nsage: QQ.embeddings(K)\n[Ring Coercion morphism:\n  From: Rational Field\n  To:   Number Field in a with defining polynomial x^4 - x^3 + 2*x^2 + x + 1]\n```\n",
    "created_at": "2010-06-30T11:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9384#issuecomment-89091",
    "user": "https://github.com/JohnCremona"
}
```

It looks to me as though the curve returned is (sometimes) a twist of the original, rather than isomorphic -- but I have been flying all night so am not reliable!

You can check if there is an embedding of K in self.base_ring() like this:

```
sage: X = polygen(QQ)
sage: K.<a> = NumberField(X^4 - X^3 + 2*X^2 + X + 1)
sage: QQ.embeddings(K)
[Ring Coercion morphism:
  From: Rational Field
  To:   Number Field in a with defining polynomial x^4 - x^3 + 2*x^2 + x + 1]
```




---

archive/issue_comments_089092.json:
```json
{
    "body": "This new patch should work in general. It uses the newly implemented preimage function for number field homomorphisms. Be sure to apply the patch from #9403 first.",
    "created_at": "2010-07-02T05:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9384#issuecomment-89092",
    "user": "https://trac.sagemath.org/admin/accounts/users/ebeyerstedt"
}
```

This new patch should work in general. It uses the newly implemented preimage function for number field homomorphisms. Be sure to apply the patch from #9403 first.



---

archive/issue_comments_089093.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-02T05:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9384#issuecomment-89093",
    "user": "https://trac.sagemath.org/admin/accounts/users/ebeyerstedt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089094.json:
```json
{
    "body": "Attachment [trac_9384_update.patch](tarball://root/attachments/some-uuid/ticket9384/trac_9384_update.patch) by ebeyerstedt created at 2010-07-02 18:49:43\n\nReplaces previous patch.",
    "created_at": "2010-07-02T18:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9384#issuecomment-89094",
    "user": "https://trac.sagemath.org/admin/accounts/users/ebeyerstedt"
}
```

Attachment [trac_9384_update.patch](tarball://root/attachments/some-uuid/ticket9384/trac_9384_update.patch) by ebeyerstedt created at 2010-07-02 18:49:43

Replaces previous patch.



---

archive/issue_comments_089095.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-02T19:57:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9384#issuecomment-89095",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009539.json:
```json
{
    "actor": "https://github.com/dandrake",
    "created_at": "2010-07-27T00:51:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9384",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9384#event-9539"
}
```



---

archive/issue_comments_089096.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-27T00:51:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9384#issuecomment-89096",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_comments_089097.json:
```json
{
    "body": "I'm entering a guess for the Reviewer(s) field.  Please correct me if I'm wrong.",
    "created_at": "2010-07-27T04:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9384#issuecomment-89097",
    "user": "https://github.com/qed777"
}
```

I'm entering a guess for the Reviewer(s) field.  Please correct me if I'm wrong.



---

archive/issue_comments_089098.json:
```json
{
    "body": "See follow-up ticket at #16456 where it is explained why the implementation here is deficient and needs fixing.",
    "created_at": "2014-06-07T17:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9384",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9384#issuecomment-89098",
    "user": "https://github.com/JohnCremona"
}
```

See follow-up ticket at #16456 where it is explained why the implementation here is deficient and needs fixing.

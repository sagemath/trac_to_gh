# Issue 8349: bug in isogenies

archive/issues_008349.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nKeywords: isogeny, elliptic curves\n\nSomething is wrong with the post_isomorphism of isogenies of elliptic curves :\n\n\n```\nsage: E = EllipticCurve(GF(17), [0,-1,0,-3,-1])\nsage: P = E([16,0])\nsage: phi = E.isogeny(P,codomain=E)\nsage: phi(P)\n(9 : 11 : 1)\nsage: phi(P) in E\nFalse\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8349\n\n",
    "created_at": "2010-02-24T17:38:51Z",
    "labels": [
        "component: elliptic curves",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "bug in isogenies",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8349",
    "user": "https://github.com/categorie"
}
```
Assignee: @JohnCremona

Keywords: isogeny, elliptic curves

Something is wrong with the post_isomorphism of isogenies of elliptic curves :


```
sage: E = EllipticCurve(GF(17), [0,-1,0,-3,-1])
sage: P = E([16,0])
sage: phi = E.isogeny(P,codomain=E)
sage: phi(P)
(9 : 11 : 1)
sage: phi(P) in E
False
```



Issue created by migration from https://trac.sagemath.org/ticket/8349





---

archive/issue_comments_074430.json:
```json
{
    "body": "Attachment [trac_8349.patch](tarball://root/attachments/some-uuid/ticket8349/trac_8349.patch) by @craigcitro created at 2010-02-24 18:35:48",
    "created_at": "2010-02-24T18:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8349#issuecomment-74430",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_8349.patch](tarball://root/attachments/some-uuid/ticket8349/trac_8349.patch) by @craigcitro created at 2010-02-24 18:35:48



---

archive/issue_comments_074431.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-24T18:36:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8349#issuecomment-74431",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074432.json:
```json
{
    "body": "Attached a quick fix -- I'm happy to let it be ignored if there's something classier to be done.",
    "created_at": "2010-02-24T18:36:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8349#issuecomment-74432",
    "user": "https://github.com/craigcitro"
}
```

Attached a quick fix -- I'm happy to let it be ignored if there's something classier to be done.



---

archive/issue_comments_074433.json:
```json
{
    "body": "Wow. That was **very** quick. But maybe a bit too quick.\n\n\n```\nsage: E = EllipticCurve('11a1')\nsage: phi = E.isogeny(None,codomain=EllipticCurve('11a2'),degree=5)\nsage: [phi(P) for P in E.torsion_points()]\n[(0 : 1 : 0), (1/3 : 1/2 : 1), (1/3 : 1/2 : 1), (1/3 : 1/2 : 1), (1/3 : 1/2 : 1)]\n```\n\n\nagain the images are not even on the `codomain()`. I.e. there is probably a second spot that needs a small change.",
    "created_at": "2010-02-24T18:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8349#issuecomment-74433",
    "user": "https://github.com/categorie"
}
```

Wow. That was **very** quick. But maybe a bit too quick.


```
sage: E = EllipticCurve('11a1')
sage: phi = E.isogeny(None,codomain=EllipticCurve('11a2'),degree=5)
sage: [phi(P) for P in E.torsion_points()]
[(0 : 1 : 0), (1/3 : 1/2 : 1), (1/3 : 1/2 : 1), (1/3 : 1/2 : 1), (1/3 : 1/2 : 1)]
```


again the images are not even on the `codomain()`. I.e. there is probably a second spot that needs a small change.



---

archive/issue_comments_074434.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-24T18:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8349#issuecomment-74434",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074435.json:
```json
{
    "body": "Attachment [trac_8349.2.patch](tarball://root/attachments/some-uuid/ticket8349/trac_8349.2.patch) by @categorie created at 2010-02-24 19:02:53",
    "created_at": "2010-02-24T19:02:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8349#issuecomment-74435",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_8349.2.patch](tarball://root/attachments/some-uuid/ticket8349/trac_8349.2.patch) by @categorie created at 2010-02-24 19:02:53



---

archive/issue_comments_074436.json:
```json
{
    "body": "I think that should do it also for the kohel part.",
    "created_at": "2010-02-24T19:04:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8349#issuecomment-74436",
    "user": "https://github.com/categorie"
}
```

I think that should do it also for the kohel part.



---

archive/issue_comments_074437.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-24T19:04:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8349#issuecomment-74437",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074438.json:
```json
{
    "body": "What about lines 981, 1002, in the patched file?  They both say \n {{{\n           return self.__E2(0)\n}}}\nso shouldn't they also be changed to return 0 on the correct codomain?",
    "created_at": "2010-02-24T20:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8349#issuecomment-74438",
    "user": "https://github.com/JohnCremona"
}
```

What about lines 981, 1002, in the patched file?  They both say 
 {{{
           return self.__E2(0)
}}}
so shouldn't they also be changed to return 0 on the correct codomain?



---

archive/issue_comments_074439.json:
```json
{
    "body": "No, these two lines must stay as they are. They do the right thing.",
    "created_at": "2010-02-24T22:35:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8349#issuecomment-74439",
    "user": "https://github.com/categorie"
}
```

No, these two lines must stay as they are. They do the right thing.



---

archive/issue_comments_074440.json:
```json
{
    "body": "Replying to [comment:5 wuthrich]:\n> No, these two lines must stay as they are. They do the right thing.\n\nOK, I trust you -- I tried to find an example where they did not do the right thing, and could not.\n\nI'm happy -- patch (just the 2nd one) applies to 4.3.3 and test pass.",
    "created_at": "2010-02-24T22:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8349#issuecomment-74440",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:5 wuthrich]:
> No, these two lines must stay as they are. They do the right thing.

OK, I trust you -- I tried to find an example where they did not do the right thing, and could not.

I'm happy -- patch (just the 2nd one) applies to 4.3.3 and test pass.



---

archive/issue_comments_074441.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-24T22:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8349#issuecomment-74441",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074442.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T14:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8349#issuecomment-74442",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_074443.json:
```json
{
    "body": "Merged [trac_8349.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8349/trac_8349.2.patch).",
    "created_at": "2010-03-03T14:06:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8349",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8349#issuecomment-74443",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac_8349.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8349/trac_8349.2.patch).

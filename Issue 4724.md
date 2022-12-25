# Issue 4724: expose pari's galois and finer number field interfaces

archive/issues_004724.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: pari number field nf galois\n\nI would like to use pari's galois computations (such as nfgaloisconj) and finer number field functions (such as nfroots).  The interface (in sage.libs.pari.gen) needs to be upgraded.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4724\n\n",
    "created_at": "2008-12-06T04:05:45Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "expose pari's galois and finer number field interfaces",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4724",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

Keywords: pari number field nf galois

I would like to use pari's galois computations (such as nfgaloisconj) and finer number field functions (such as nfroots).  The interface (in sage.libs.pari.gen) needs to be upgraded.

Issue created by migration from https://trac.sagemath.org/ticket/4724





---

archive/issue_comments_035589.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T07:07:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35589",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_035590.json:
```json
{
    "body": "A valuable improvement would be to use polisirreducible and nfroots for polynomials defined over number fields.",
    "created_at": "2009-02-11T00:07:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35590",
    "user": "https://github.com/ncalexan"
}
```

A valuable improvement would be to use polisirreducible and nfroots for polynomials defined over number fields.



---

archive/issue_comments_035591.json:
```json
{
    "body": "This is a step in the right direction -- exposes nfgaloisconj and nfroots, and adds automorphisms/updates embeddings to be much faster for number fields.\n\nTry it with a large degree number field -- you couldn't compute K.embeddings(K) for suff. large K, but now you can.",
    "created_at": "2009-02-13T02:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35591",
    "user": "https://github.com/ncalexan"
}
```

This is a step in the right direction -- exposes nfgaloisconj and nfroots, and adds automorphisms/updates embeddings to be much faster for number fields.

Try it with a large degree number field -- you couldn't compute K.embeddings(K) for suff. large K, but now you can.



---

archive/issue_comments_035592.json:
```json
{
    "body": "Attachment [4724-ncalexan-pari-galois-functions.patch](tarball://root/attachments/some-uuid/ticket4724/4724-ncalexan-pari-galois-functions.patch) by @ncalexan created at 2009-02-13 02:47:03",
    "created_at": "2009-02-13T02:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35592",
    "user": "https://github.com/ncalexan"
}
```

Attachment [4724-ncalexan-pari-galois-functions.patch](tarball://root/attachments/some-uuid/ticket4724/4724-ncalexan-pari-galois-functions.patch) by @ncalexan created at 2009-02-13 02:47:03



---

archive/issue_comments_035593.json:
```json
{
    "body": "This looks really really useful, great code!  But it needs to be rebased to 3.4: at present the patch does not merge.",
    "created_at": "2009-03-15T22:19:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35593",
    "user": "https://github.com/JohnCremona"
}
```

This looks really really useful, great code!  But it needs to be rebased to 3.4: at present the patch does not merge.



---

archive/issue_comments_035594.json:
```json
{
    "body": "Nick, did you get the message about rebasing this?  John",
    "created_at": "2009-04-08T09:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35594",
    "user": "https://github.com/JohnCremona"
}
```

Nick, did you get the message about rebasing this?  John



---

archive/issue_comments_035595.json:
```json
{
    "body": "Yes I got messages about this but it is not a priority for me.  I will try to rebase it sometime soon.",
    "created_at": "2009-04-12T19:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35595",
    "user": "https://github.com/ncalexan"
}
```

Yes I got messages about this but it is not a priority for me.  I will try to rebase it sometime soon.



---

archive/issue_comments_035596.json:
```json
{
    "body": "replaces the previous patch",
    "created_at": "2009-04-13T08:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35596",
    "user": "https://github.com/aghitza"
}
```

replaces the previous patch



---

archive/issue_comments_035597.json:
```json
{
    "body": "Attachment [4724_rebased.patch](tarball://root/attachments/some-uuid/ticket4724/4724_rebased.patch) by @aghitza created at 2009-04-13 08:43:09\n\nAll I did was rebase Nick's patch against 3.4.1.rc2.  (ok, I also rest-ified a couple of his docstrings.)\n\nOne issue was that the original patch seems to have had a lot of things in double.  This is now fixed, hence the difference in size.\n\nThe code looks good to me and is nicely documented.  Positive review.",
    "created_at": "2009-04-13T08:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35597",
    "user": "https://github.com/aghitza"
}
```

Attachment [4724_rebased.patch](tarball://root/attachments/some-uuid/ticket4724/4724_rebased.patch) by @aghitza created at 2009-04-13 08:43:09

All I did was rebase Nick's patch against 3.4.1.rc2.  (ok, I also rest-ified a couple of his docstrings.)

One issue was that the original patch seems to have had a lot of things in double.  This is now fixed, hence the difference in size.

The code looks good to me and is nicely documented.  Positive review.



---

archive/issue_events_004969.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-04-13T09:02:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4724#event-4969"
}
```



---

archive/issue_comments_035598.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T09:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35598",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035599.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T09:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35599",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael

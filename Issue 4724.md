# Issue 4724: expose pari's galois and finer number field interfaces

archive/issues_004724.json:
```json
{
    "body": "Assignee: was\n\nKeywords: pari number field nf galois\n\nI would like to use pari's galois computations (such as nfgaloisconj) and finer number field functions (such as nfroots).  The interface (in sage.libs.pari.gen) needs to be upgraded.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4724\n\n",
    "created_at": "2008-12-06T04:05:45Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "expose pari's galois and finer number field interfaces",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4724",
    "user": "ncalexan"
}
```
Assignee: was

Keywords: pari number field nf galois

I would like to use pari's galois computations (such as nfgaloisconj) and finer number field functions (such as nfroots).  The interface (in sage.libs.pari.gen) needs to be upgraded.

Issue created by migration from https://trac.sagemath.org/ticket/4724





---

archive/issue_comments_035659.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T07:07:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35659",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_035660.json:
```json
{
    "body": "A valuable improvement would be to use polisirreducible and nfroots for polynomials defined over number fields.",
    "created_at": "2009-02-11T00:07:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35660",
    "user": "ncalexan"
}
```

A valuable improvement would be to use polisirreducible and nfroots for polynomials defined over number fields.



---

archive/issue_comments_035661.json:
```json
{
    "body": "This is a step in the right direction -- exposes nfgaloisconj and nfroots, and adds automorphisms/updates embeddings to be much faster for number fields.\n\nTry it with a large degree number field -- you couldn't compute K.embeddings(K) for suff. large K, but now you can.",
    "created_at": "2009-02-13T02:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35661",
    "user": "ncalexan"
}
```

This is a step in the right direction -- exposes nfgaloisconj and nfroots, and adds automorphisms/updates embeddings to be much faster for number fields.

Try it with a large degree number field -- you couldn't compute K.embeddings(K) for suff. large K, but now you can.



---

archive/issue_comments_035662.json:
```json
{
    "body": "Attachment [4724-ncalexan-pari-galois-functions.patch](tarball://root/attachments/some-uuid/ticket4724/4724-ncalexan-pari-galois-functions.patch) by ncalexan created at 2009-02-13 02:47:03",
    "created_at": "2009-02-13T02:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35662",
    "user": "ncalexan"
}
```

Attachment [4724-ncalexan-pari-galois-functions.patch](tarball://root/attachments/some-uuid/ticket4724/4724-ncalexan-pari-galois-functions.patch) by ncalexan created at 2009-02-13 02:47:03



---

archive/issue_comments_035663.json:
```json
{
    "body": "This looks really really useful, great code!  But it needs to be rebased to 3.4: at present the patch does not merge.",
    "created_at": "2009-03-15T22:19:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35663",
    "user": "cremona"
}
```

This looks really really useful, great code!  But it needs to be rebased to 3.4: at present the patch does not merge.



---

archive/issue_comments_035664.json:
```json
{
    "body": "Nick, did you get the message about rebasing this?  John",
    "created_at": "2009-04-08T09:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35664",
    "user": "cremona"
}
```

Nick, did you get the message about rebasing this?  John



---

archive/issue_comments_035665.json:
```json
{
    "body": "Yes I got messages about this but it is not a priority for me.  I will try to rebase it sometime soon.",
    "created_at": "2009-04-12T19:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35665",
    "user": "ncalexan"
}
```

Yes I got messages about this but it is not a priority for me.  I will try to rebase it sometime soon.



---

archive/issue_comments_035666.json:
```json
{
    "body": "replaces the previous patch",
    "created_at": "2009-04-13T08:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35666",
    "user": "AlexGhitza"
}
```

replaces the previous patch



---

archive/issue_comments_035667.json:
```json
{
    "body": "Attachment [4724_rebased.patch](tarball://root/attachments/some-uuid/ticket4724/4724_rebased.patch) by AlexGhitza created at 2009-04-13 08:43:09\n\nAll I did was rebase Nick's patch against 3.4.1.rc2.  (ok, I also rest-ified a couple of his docstrings.)\n\nOne issue was that the original patch seems to have had a lot of things in double.  This is now fixed, hence the difference in size.\n\nThe code looks good to me and is nicely documented.  Positive review.",
    "created_at": "2009-04-13T08:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35667",
    "user": "AlexGhitza"
}
```

Attachment [4724_rebased.patch](tarball://root/attachments/some-uuid/ticket4724/4724_rebased.patch) by AlexGhitza created at 2009-04-13 08:43:09

All I did was rebase Nick's patch against 3.4.1.rc2.  (ok, I also rest-ified a couple of his docstrings.)

One issue was that the original patch seems to have had a lot of things in double.  This is now fixed, hence the difference in size.

The code looks good to me and is nicely documented.  Positive review.



---

archive/issue_comments_035668.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T09:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35668",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035669.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T09:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4724#issuecomment-35669",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael

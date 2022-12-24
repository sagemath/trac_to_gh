# Issue 6830: [with patch, needs review] Ideals of a Hecke Algebra

archive/issues_006830.json:
```json
{
    "body": "Assignee: craigcitro\n\nCC:  robharron\n\nKeywords: ideal, hecke\n\nAdded code for ideals of a Hecke algebra.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6830\n\n",
    "created_at": "2009-08-26T22:20:44Z",
    "labels": [
        "modular forms",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] Ideals of a Hecke Algebra",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6830",
    "user": "wakep"
}
```
Assignee: craigcitro

CC:  robharron

Keywords: ideal, hecke

Added code for ideals of a Hecke algebra.

Issue created by migration from https://trac.sagemath.org/ticket/6830





---

archive/issue_comments_056329.json:
```json
{
    "body": "This patch depends on the basis of a Hecke algebra code from ticket #6768",
    "created_at": "2009-08-26T22:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6830#issuecomment-56329",
    "user": "wakep"
}
```

This patch depends on the basis of a Hecke algebra code from ticket #6768



---

archive/issue_comments_056330.json:
```json
{
    "body": "Attachment [ideal.patch](tarball://root/attachments/some-uuid/ticket6830/ideal.patch) by wakep created at 2009-08-27 15:33:49",
    "created_at": "2009-08-27T15:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6830#issuecomment-56330",
    "user": "wakep"
}
```

Attachment [ideal.patch](tarball://root/attachments/some-uuid/ticket6830/ideal.patch) by wakep created at 2009-08-27 15:33:49



---

archive/issue_comments_056331.json:
```json
{
    "body": "The patch is now visible;  I don't have time to test it very soon , sorry.",
    "created_at": "2009-08-27T20:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6830#issuecomment-56331",
    "user": "cremona"
}
```

The patch is now visible;  I don't have time to test it very soon , sorry.



---

archive/issue_comments_056332.json:
```json
{
    "body": "Could you rebase this to apply to 4.3.alpha1?  As it stands the patch does not apply, but I expect it will be an easy fix.\n\nGenerally the code looks good to me (though there is at least one functions with no doctests at present).\n\nOnce rebased, I'll test it properly.",
    "created_at": "2009-12-10T21:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6830#issuecomment-56332",
    "user": "cremona"
}
```

Could you rebase this to apply to 4.3.alpha1?  As it stands the patch does not apply, but I expect it will be an easy fix.

Generally the code looks good to me (though there is at least one functions with no doctests at present).

Once rebased, I'll test it properly.



---

archive/issue_comments_056333.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-10T21:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6830#issuecomment-56333",
    "user": "cremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_056334.json:
```json
{
    "body": "Just discovered this moribund ticket. I might actually find this useful! Does anyone intend to revisit this?",
    "created_at": "2016-08-16T19:36:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6830#issuecomment-56334",
    "user": "kedlaya"
}
```

Just discovered this moribund ticket. I might actually find this useful! Does anyone intend to revisit this?



---

archive/issue_comments_056335.json:
```json
{
    "body": "To quote an email from wakep:\n\"I wrote that code as part of an undergraduate summer research program. I was not particularly savvy with Sage development then (and even less-so now). As far as I understand, the reason that it became moribund is that it took some time to get an initial review, and by the time it got one, Sage was on to a new version. I was asked to \"rebase\" it to the new version, but I didn't know how to do that. (I had started graduate school by then and had no time to play with Sage.)\n\nThe upshot is that I have no particular intention to revisit the code, but I think that it wouldn't take much to get it working. I'd be happy to work on it, but I wouldn't know what to do.\"\n\nSo I (kedlaya) took the liberty of manually rebasing the patch. I haven't even tried to build this yet; probably that will reveal some other issues.\n\n----\nNew commits:",
    "created_at": "2016-08-19T23:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6830#issuecomment-56335",
    "user": "kedlaya"
}
```

To quote an email from wakep:
"I wrote that code as part of an undergraduate summer research program. I was not particularly savvy with Sage development then (and even less-so now). As far as I understand, the reason that it became moribund is that it took some time to get an initial review, and by the time it got one, Sage was on to a new version. I was asked to "rebase" it to the new version, but I didn't know how to do that. (I had started graduate school by then and had no time to play with Sage.)

The upshot is that I have no particular intention to revisit the code, but I think that it wouldn't take much to get it working. I'd be happy to work on it, but I wouldn't know what to do."

So I (kedlaya) took the liberty of manually rebasing the patch. I haven't even tried to build this yet; probably that will reveal some other issues.

----
New commits:



---

archive/issue_comments_056336.json:
```json
{
    "body": "robharron points out that it would be more robust to create the Hecke algebra as an abstract ring (represented internally as a quotient of a polynomial ring over Z) plus maps back and forth (e.g., given N, turn the N-th Hecke operator into an abstract ring element). Then one could deal with ideals on the ring side, which would give access to all existing commutative algebra functionality.",
    "created_at": "2016-08-20T03:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6830#issuecomment-56336",
    "user": "kedlaya"
}
```

robharron points out that it would be more robust to create the Hecke algebra as an abstract ring (represented internally as a quotient of a polynomial ring over Z) plus maps back and forth (e.g., given N, turn the N-th Hecke operator into an abstract ring element). Then one could deal with ideals on the ring side, which would give access to all existing commutative algebra functionality.



---

archive/issue_comments_056337.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-08-20T21:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6830",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6830#issuecomment-56337",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:

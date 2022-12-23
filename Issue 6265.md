# Issue 6265: fix toy_d_basis.py

archive/issues_006265.json:
```json
{
    "body": "Assignee: malb\n\nCC:  malb tscrim kedlaya simonking\n\nAs discussed at #6051.  Line 91 of sage/rings/polynomial/toy_d_basis.py needs to be unrandomed when this is fixed.\n\n\n```\nHowever, when we compute the Groebner basis of I (defined over `\\ZZ`), we note that there is a certain integer in the ideal which is not 1.::\n\n    sage: d_basis(I) # random -- waiting on upstream singular fixes at #6051\n    [x + 170269749119, y + 2149906854, z + ..., 282687803443]                                \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6265\n\n",
    "created_at": "2009-06-12T08:01:59Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "fix toy_d_basis.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6265",
    "user": "ncalexan"
}
```
Assignee: malb

CC:  malb tscrim kedlaya simonking

As discussed at #6051.  Line 91 of sage/rings/polynomial/toy_d_basis.py needs to be unrandomed when this is fixed.


```
However, when we compute the Groebner basis of I (defined over `\ZZ`), we note that there is a certain integer in the ideal which is not 1.::

    sage: d_basis(I) # random -- waiting on upstream singular fixes at #6051
    [x + 170269749119, y + 2149906854, z + ..., 282687803443]                                
```


Issue created by migration from https://trac.sagemath.org/ticket/6265





---

archive/issue_comments_050019.json:
```json
{
    "body": "New commits:",
    "created_at": "2017-03-30T20:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50019",
    "user": "chapoton"
}
```

New commits:



---

archive/issue_comments_050020.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-03-30T20:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50020",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050021.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-03-30T20:31:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50021",
    "user": "chapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_050022.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-03-30T20:40:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50022",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_050023.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-03-30T20:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50023",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050024.json:
```json
{
    "body": "It doesn't seem like the problem is fixed if you have to use `...` in the doctest. So I'm not sure we should remove the comment, but I haven't looked to deep into this.",
    "created_at": "2017-03-30T22:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50024",
    "user": "tscrim"
}
```

It doesn't seem like the problem is fixed if you have to use `...` in the doctest. So I'm not sure we should remove the comment, but I haven't looked to deep into this.



---

archive/issue_comments_050025.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2017-03-31T06:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50025",
    "user": "chapoton"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_050026.json:
```json
{
    "body": "Indeed, I also have some doubts. Let us check \"needs_info\"\n\nThe `...` are there to replace *huge* numbers. Maybe we should keep the top few digits ?",
    "created_at": "2017-03-31T06:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50026",
    "user": "chapoton"
}
```

Indeed, I also have some doubts. Let us check "needs_info"

The `...` are there to replace *huge* numbers. Maybe we should keep the top few digits ?



---

archive/issue_comments_050027.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-04-01T16:45:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50027",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_050028.json:
```json
{
    "body": "Here is another try, with green bot. I changed the term order so that the Groebner basis has much smaller coefficients. Maybe this should be tested on diverse machines.",
    "created_at": "2017-04-01T19:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50028",
    "user": "chapoton"
}
```

Here is another try, with green bot. I changed the term order so that the Groebner basis has much smaller coefficients. Maybe this should be tested on diverse machines.



---

archive/issue_comments_050029.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2017-04-01T19:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50029",
    "user": "chapoton"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_050030.json:
```json
{
    "body": "maybe this is good enough, I don't know..",
    "created_at": "2017-04-04T19:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50030",
    "user": "chapoton"
}
```

maybe this is good enough, I don't know..



---

archive/issue_comments_050031.json:
```json
{
    "body": "Hmm...I'm now not so sure what the point of the doctest is. From the description above it looks more like the minimal integer that is in the ideal is the important point rather than the integers that are part of the binomial generators. I'm cc-ing Simon to see if he has a thought on this. Yet, this was last touched in 2009, so maybe we can just `...` the binomial term integers and be done with it.",
    "created_at": "2017-04-04T19:23:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50031",
    "user": "tscrim"
}
```

Hmm...I'm now not so sure what the point of the doctest is. From the description above it looks more like the minimal integer that is in the ideal is the important point rather than the integers that are part of the binomial generators. I'm cc-ing Simon to see if he has a thought on this. Yet, this was last touched in 2009, so maybe we can just `...` the binomial term integers and be done with it.



---

archive/issue_comments_050032.json:
```json
{
    "body": "Replying to [comment:15 tscrim]:\n> Hmm...I'm now not so sure what the point of the doctest is. From the description above it looks more like the minimal integer that is in the ideal is the important point rather than the integers that are part of the binomial generators. I'm cc-ing Simon to see if he has a thought on this.\n\nI don't know anything about the theory of d-Gr\u00f6bner bases. However, from the explanation in the doctest, it seems to me that the integers in the binomial generators do not matter (at least not for the test). It seems to me that the point of the example is to show that\n- there is an integer in the d_basis, and\n- the prime factors of that integer have the property that the original system has solutions modulo that prime.",
    "created_at": "2017-04-04T19:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50032",
    "user": "SimonKing"
}
```

Replying to [comment:15 tscrim]:
> Hmm...I'm now not so sure what the point of the doctest is. From the description above it looks more like the minimal integer that is in the ideal is the important point rather than the integers that are part of the binomial generators. I'm cc-ing Simon to see if he has a thought on this.

I don't know anything about the theory of d-Gröbner bases. However, from the explanation in the doctest, it seems to me that the integers in the binomial generators do not matter (at least not for the test). It seems to me that the point of the example is to show that
- there is an integer in the d_basis, and
- the prime factors of that integer have the property that the original system has solutions modulo that prime.



---

archive/issue_comments_050033.json:
```json
{
    "body": "Thanks Simon.\n\nSo shall we revert back to 716ac65?",
    "created_at": "2017-04-05T16:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50033",
    "user": "tscrim"
}
```

Thanks Simon.

So shall we revert back to 716ac65?



---

archive/issue_comments_050034.json:
```json
{
    "body": "IMHO, the current branch should be just as good. I would rather try to let this in and see if the buildbots of Volker report any failure on apples and oranges.",
    "created_at": "2017-04-05T18:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50034",
    "user": "chapoton"
}
```

IMHO, the current branch should be just as good. I would rather try to let this in and see if the buildbots of Volker report any failure on apples and oranges.



---

archive/issue_comments_050035.json:
```json
{
    "body": "Okay, then if you break the long line into each of the generators, you can set a positive review on my behalf.",
    "created_at": "2017-04-05T21:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50035",
    "user": "tscrim"
}
```

Okay, then if you break the long line into each of the generators, you can set a positive review on my behalf.



---

archive/issue_comments_050036.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-04-06T06:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50036",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_050037.json:
```json
{
    "body": "ok, done. Thanks. Setting to positive",
    "created_at": "2017-04-06T06:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50037",
    "user": "chapoton"
}
```

ok, done. Thanks. Setting to positive



---

archive/issue_comments_050038.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-04-06T06:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50038",
    "user": "chapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050039.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-04-07T22:24:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6265#issuecomment-50039",
    "user": "vbraun"
}
```

Resolution: fixed

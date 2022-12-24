# Issue 8506: Inefficient hash for homsets

archive/issues_008506.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nThis ends up affecting, in particular, hashing of elliptic curves and their point sets. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8506\n\n",
    "created_at": "2010-03-12T01:39:09Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Inefficient hash for homsets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8506",
    "user": "@robertwb"
}
```
Assignee: @JohnCremona

This ends up affecting, in particular, hashing of elliptic curves and their point sets. 

Issue created by migration from https://trac.sagemath.org/ticket/8506





---

archive/issue_comments_076805.json:
```json
{
    "body": "As I side effect, I changed __ainvs to be stored as a tuple, rather than being converted at each request.",
    "created_at": "2010-03-12T01:41:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8506#issuecomment-76805",
    "user": "@robertwb"
}
```

As I side effect, I changed __ainvs to be stored as a tuple, rather than being converted at each request.



---

archive/issue_comments_076806.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-12T02:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8506#issuecomment-76806",
    "user": "@robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076807.json:
```json
{
    "body": "Attachment [8506-homset-hashing.patch](tarball://root/attachments/some-uuid/ticket8506/8506-homset-hashing.patch) by @robertwb created at 2010-03-12 02:36:46",
    "created_at": "2010-03-12T02:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8506#issuecomment-76807",
    "user": "@robertwb"
}
```

Attachment [8506-homset-hashing.patch](tarball://root/attachments/some-uuid/ticket8506/8506-homset-hashing.patch) by @robertwb created at 2010-03-12 02:36:46



---

archive/issue_comments_076808.json:
```json
{
    "body": "Replying to [comment:2 robertwb]:\n\nHi robert, \n\nThe problem is not only for homset ! See #8119\n\n```\nsage: h = Hom(ZZ, QQ)\nsage: hash(h)\n-8106914618552251573\nsage: h.rename(\"toto\")\nsage: hash(h)\n2314052222105390764\n```\n\nI don't know exactly what would be a generic solution of this problem. There is one if the parent inherits from `UniqueRepresentation` (see ##8120) instead of using one of the at least three other mechanisms I've seen troughout sage library. Not that as I said in that ticket, I'm not sure how robust my solution is I've a proposal for a better option. If you have any comment, please do not hesitate.\n\nCheers,\n\nFlorent",
    "created_at": "2010-03-12T08:34:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8506#issuecomment-76808",
    "user": "@hivert"
}
```

Replying to [comment:2 robertwb]:

Hi robert, 

The problem is not only for homset ! See #8119

```
sage: h = Hom(ZZ, QQ)
sage: hash(h)
-8106914618552251573
sage: h.rename("toto")
sage: hash(h)
2314052222105390764
```

I don't know exactly what would be a generic solution of this problem. There is one if the parent inherits from `UniqueRepresentation` (see ##8120) instead of using one of the at least three other mechanisms I've seen troughout sage library. Not that as I said in that ticket, I'm not sure how robust my solution is I've a proposal for a better option. If you have any comment, please do not hesitate.

Cheers,

Florent



---

archive/issue_comments_076809.json:
```json
{
    "body": "My original concern was that hashing the parents I was using was way to expensive. In particular, it was using the Parent as a key in the coercion model, and the dict lookup was many times more expensive than the actual arithmetic (or anything else I was doing in that function...) `UniqueRepresentation` is special, as one doesn't have to worry about hashes being unequal for equal objects.",
    "created_at": "2010-03-12T09:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8506#issuecomment-76809",
    "user": "@robertwb"
}
```

My original concern was that hashing the parents I was using was way to expensive. In particular, it was using the Parent as a key in the coercion model, and the dict lookup was many times more expensive than the actual arithmetic (or anything else I was doing in that function...) `UniqueRepresentation` is special, as one doesn't have to worry about hashes being unequal for equal objects.



---

archive/issue_comments_076810.json:
```json
{
    "body": "I am not competent to comment on the hashing issues.  But I applied the patch to 4.3.4.alpha1 and had the following test failures (I only tested sage/schemes/elliptic_curves, and without -long):\n\n```\nsage -t  sage/schemes/elliptic_curves/heegner.py\n**********************************************************************\nFile \"/storage/jec/sage-4.3.4.alpha1/devel/sage-8505/sage/schemes/elliptic_curves/heegner.py\", line 2588:\n    sage: hash(y)\nExpected:\n    -5236815264926108755       \nGot:\n    -756867903203770682\n**********************************************************************\nFile \"/storage/jec/sage-4.3.4.alpha1/devel/sage-8505/sage/schemes/elliptic_curves/heegner.py\", line 2893:\n    sage: hash(EllipticCurve('389a').heegner_point(-7,5))\nExpected:\n    -5236815264926108755             \nGot:\n    -756867903203770682\n**********************************************************************\n2 items had failures:\n   1 of   4 in __main__.example_107\n   1 of   3 in __main__.example_121\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/jec/.sage//tmp/.doctest_heegner.py\n\t [83.6 s]\n```\n",
    "created_at": "2010-03-13T15:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8506#issuecomment-76810",
    "user": "@JohnCremona"
}
```

I am not competent to comment on the hashing issues.  But I applied the patch to 4.3.4.alpha1 and had the following test failures (I only tested sage/schemes/elliptic_curves, and without -long):

```
sage -t  sage/schemes/elliptic_curves/heegner.py
**********************************************************************
File "/storage/jec/sage-4.3.4.alpha1/devel/sage-8505/sage/schemes/elliptic_curves/heegner.py", line 2588:
    sage: hash(y)
Expected:
    -5236815264926108755       
Got:
    -756867903203770682
**********************************************************************
File "/storage/jec/sage-4.3.4.alpha1/devel/sage-8505/sage/schemes/elliptic_curves/heegner.py", line 2893:
    sage: hash(EllipticCurve('389a').heegner_point(-7,5))
Expected:
    -5236815264926108755             
Got:
    -756867903203770682
**********************************************************************
2 items had failures:
   1 of   4 in __main__.example_107
   1 of   3 in __main__.example_121
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/jec/.sage//tmp/.doctest_heegner.py
	 [83.6 s]
```




---

archive/issue_comments_076811.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-13T15:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8506#issuecomment-76811",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076812.json:
```json
{
    "body": "Looks like this is once again a case where the alpha differs enough from the latest release to cause issues. The changes above look innocuous enough, I'll make a new patch.",
    "created_at": "2010-03-13T19:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8506#issuecomment-76812",
    "user": "@robertwb"
}
```

Looks like this is once again a case where the alpha differs enough from the latest release to cause issues. The changes above look innocuous enough, I'll make a new patch.



---

archive/issue_comments_076813.json:
```json
{
    "body": "Attachment [8506-homset-hashing-take2.patch](tarball://root/attachments/some-uuid/ticket8506/8506-homset-hashing-take2.patch) by @robertwb created at 2010-03-15 19:47:13",
    "created_at": "2010-03-15T19:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8506#issuecomment-76813",
    "user": "@robertwb"
}
```

Attachment [8506-homset-hashing-take2.patch](tarball://root/attachments/some-uuid/ticket8506/8506-homset-hashing-take2.patch) by @robertwb created at 2010-03-15 19:47:13



---

archive/issue_comments_076814.json:
```json
{
    "body": "OK, I ran all tests against the latest alpha, and those two were the only failures I got as well. I've posted a new patch fixing them. As for the hashing issues, I just changed the hash to not rely on the string representation (e.g. hashing an elliptic curve now hashes the basering and a-invariants).",
    "created_at": "2010-03-15T19:50:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8506#issuecomment-76814",
    "user": "@robertwb"
}
```

OK, I ran all tests against the latest alpha, and those two were the only failures I got as well. I've posted a new patch fixing them. As for the hashing issues, I just changed the hash to not rely on the string representation (e.g. hashing an elliptic curve now hashes the basering and a-invariants).



---

archive/issue_comments_076815.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-15T19:50:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8506#issuecomment-76815",
    "user": "@robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076816.json:
```json
{
    "body": "New patch applies to 4.3.5 OK.  Now testing on both 32- and 64-bit...",
    "created_at": "2010-04-02T16:41:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8506#issuecomment-76816",
    "user": "@JohnCremona"
}
```

New patch applies to 4.3.5 OK.  Now testing on both 32- and 64-bit...



---

archive/issue_comments_076817.json:
```json
{
    "body": "Replying to [comment:8 cremona]:\n> New patch applies to 4.3.5 OK.  Now testing on both 32- and 64-bit...\n\nAll tests pass on both -- positive review!",
    "created_at": "2010-04-02T19:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8506#issuecomment-76817",
    "user": "@JohnCremona"
}
```

Replying to [comment:8 cremona]:
> New patch applies to 4.3.5 OK.  Now testing on both 32- and 64-bit...

All tests pass on both -- positive review!



---

archive/issue_comments_076818.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-02T19:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8506#issuecomment-76818",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076819.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8506#issuecomment-76819",
    "user": "@jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_076820.json:
```json
{
    "body": "Merged \"8506-homset-hashing-take2.patch\" in 4.4.alpha0.",
    "created_at": "2010-04-16T18:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8506#issuecomment-76820",
    "user": "@jhpalmieri"
}
```

Merged "8506-homset-hashing-take2.patch" in 4.4.alpha0.

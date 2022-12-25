# Issue 8238: heegner_index_bound may be incorrect for curves with rational torsion

archive/issues_008238.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  @williamstein\n\nResult of a recent conversation with William Stein.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8238\n\n",
    "created_at": "2010-02-11T19:10:09Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "heegner_index_bound may be incorrect for curves with rational torsion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8238",
    "user": "https://github.com/rlmill"
}
```
Assignee: @JohnCremona

CC:  @williamstein

Result of a recent conversation with William Stein.

Issue created by migration from https://trac.sagemath.org/ticket/8238





---

archive/issue_comments_072658.json:
```json
{
    "body": "I need to fix this to use `two_torsion_rank` instead of `torsion_order`... tomorrow!",
    "created_at": "2010-02-12T09:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72658",
    "user": "https://github.com/rlmill"
}
```

I need to fix this to use `two_torsion_rank` instead of `torsion_order`... tomorrow!



---

archive/issue_comments_072659.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-14T20:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72659",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072660.json:
```json
{
    "body": "I wouldn't mind reviewing this, but I am probably not the right person to do so, since I don't really understand what it changes. Would it be good to have a test example included to illustrate the change.\n\nAlso in 4.3.3.alpha0 I get a test error in heegner.py, which wuld make my review useless.Sorry.",
    "created_at": "2010-02-15T12:50:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72660",
    "user": "https://github.com/categorie"
}
```

I wouldn't mind reviewing this, but I am probably not the right person to do so, since I don't really understand what it changes. Would it be good to have a test example included to illustrate the change.

Also in 4.3.3.alpha0 I get a test error in heegner.py, which wuld make my review useless.Sorry.



---

archive/issue_comments_072661.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-19T06:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72661",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072662.json:
```json
{
    "body": "Robert,\n\nI think the point of this patch is to change the function so it is no longer off by factors of 2 by default. \nNote that the documentation, even after applying your patch, says:\n\n```\n    r\"\"\"\n    Return an interval that contains the index of the Heegner\n    point `y_K` in the group of `K`-rational points modulo torsion\n    on this elliptic curve, computed using the Gross-Zagier\n    formula and/or a point search, or the index divided by `2`.\n\n    .. note::\n\n       If ``min_p`` is bigger than 2 then the index can be off by\n       any prime less than ``min_p``. This function returns the\n       index divided by `2` exactly when the rank of `E(K)` is\n       greater than 1 and `E(\\QQ)_{/tor} \\oplus E^D(\\QQ)_{/tor}`\n       has index `2` in `E(K)_{/tor}`, where the second factor\n       undergoes a twist.\n```\n\n\nIf you've really fixed the \"factor of 2\" issue, as it seems you have, then the documentation should be changed to reflect this.  Moreover, this is an enhancement, rather than a bug fix.",
    "created_at": "2010-04-19T06:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72662",
    "user": "https://github.com/williamstein"
}
```

Robert,

I think the point of this patch is to change the function so it is no longer off by factors of 2 by default. 
Note that the documentation, even after applying your patch, says:

```
    r"""
    Return an interval that contains the index of the Heegner
    point `y_K` in the group of `K`-rational points modulo torsion
    on this elliptic curve, computed using the Gross-Zagier
    formula and/or a point search, or the index divided by `2`.

    .. note::

       If ``min_p`` is bigger than 2 then the index can be off by
       any prime less than ``min_p``. This function returns the
       index divided by `2` exactly when the rank of `E(K)` is
       greater than 1 and `E(\QQ)_{/tor} \oplus E^D(\QQ)_{/tor}`
       has index `2` in `E(K)_{/tor}`, where the second factor
       undergoes a twist.
```


If you've really fixed the "factor of 2" issue, as it seems you have, then the documentation should be changed to reflect this.  Moreover, this is an enhancement, rather than a bug fix.



---

archive/issue_events_019706.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-04-19T06:38:13Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "milestone": "sage-4.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8238#event-19706"
}
```



---

archive/issue_comments_072663.json:
```json
{
    "body": "I was able to fix the output for rank 0 and 1 curves, but not in general. Note it says\n\"This function returns the index divided by `2` exactly when the rank of `E(K)` is greater than 1 and ...\"",
    "created_at": "2010-04-19T14:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72663",
    "user": "https://github.com/rlmill"
}
```

I was able to fix the output for rank 0 and 1 curves, but not in general. Note it says
"This function returns the index divided by `2` exactly when the rank of `E(K)` is greater than 1 and ..."



---

archive/issue_comments_072664.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-04-19T14:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72664",
    "user": "https://github.com/rlmill"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_072665.json:
```json
{
    "body": "Ping! This ticket still needs a review...",
    "created_at": "2010-05-25T23:24:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72665",
    "user": "https://github.com/rlmill"
}
```

Ping! This ticket still needs a review...



---

archive/issue_comments_072666.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-25T23:24:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72666",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072667.json:
```json
{
    "body": "I applied the patch to 4.4.3 and it worked fine (patch applies cleanly, all long tests in heegner.py pass, \n\nSome minor quibbles:\n1. on line 6365:  instead of \"an interval that contains the index, or the index over 2\" say \"... or half the index\".\n2. line 6454++:  this code is reached whe then rank is 0 (or it appears to be) but then F.gens()[0] would fail.  If it is the case that the rank would never be 0 here. I would prefer a comment to that effect and change the test to if F.rank() == 1.  (I assume that in this context calling F.rank() and F.gens() is not expensive?)\n3. After setting a=2 in line 6460 the loop should break.  (OK, so there will not be that many torsion points o nEK, but still.)  Even better would be to first compute EK.torsion_points() and only run the loop at all if it has even length?  (But still test if z itself can be divided by 2).  I'm sure I once wrote a function which returned a list of points generating torsion modulo 2*torsion....if you did\n\n```\nsage: for T in EK.torsion_subgroup().gens():\n....:     if T.order()%2==0:\n```\n\nyou would have at most 2 points to check.\n\nI'll give this a positive review once these have been fixed.",
    "created_at": "2010-06-05T15:06:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72667",
    "user": "https://github.com/JohnCremona"
}
```

I applied the patch to 4.4.3 and it worked fine (patch applies cleanly, all long tests in heegner.py pass, 

Some minor quibbles:
1. on line 6365:  instead of "an interval that contains the index, or the index over 2" say "... or half the index".
2. line 6454++:  this code is reached whe then rank is 0 (or it appears to be) but then F.gens()[0] would fail.  If it is the case that the rank would never be 0 here. I would prefer a comment to that effect and change the test to if F.rank() == 1.  (I assume that in this context calling F.rank() and F.gens() is not expensive?)
3. After setting a=2 in line 6460 the loop should break.  (OK, so there will not be that many torsion points o nEK, but still.)  Even better would be to first compute EK.torsion_points() and only run the loop at all if it has even length?  (But still test if z itself can be divided by 2).  I'm sure I once wrote a function which returned a list of points generating torsion modulo 2*torsion....if you did

```
sage: for T in EK.torsion_subgroup().gens():
....:     if T.order()%2==0:
```

you would have at most 2 points to check.

I'll give this a positive review once these have been fixed.



---

archive/issue_comments_072668.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-05T15:06:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72668",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072669.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-05T15:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72669",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072670.json:
```json
{
    "body": "I think I've addressed each of the above concerns. Thank you for the review!",
    "created_at": "2010-06-05T15:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72670",
    "user": "https://github.com/rlmill"
}
```

I think I've addressed each of the above concerns. Thank you for the review!



---

archive/issue_comments_072671.json:
```json
{
    "body": "Great -- positive review now.",
    "created_at": "2010-06-05T21:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72671",
    "user": "https://github.com/JohnCremona"
}
```

Great -- positive review now.



---

archive/issue_comments_072672.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-05T21:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72672",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072673.json:
```json
{
    "body": "very sorry, my mistake -- if there are 2 torsion gens of even order you still needs to also trying adding their sum (i.e. if T/2T has order 4 there should be 4 tests).",
    "created_at": "2010-06-05T21:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72673",
    "user": "https://github.com/JohnCremona"
}
```

very sorry, my mistake -- if there are 2 torsion gens of even order you still needs to also trying adding their sum (i.e. if T/2T has order 4 there should be 4 tests).



---

archive/issue_comments_072674.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-06-05T21:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72674",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_072675.json:
```json
{
    "body": "Attachment [trac_8238.patch](tarball://root/attachments/some-uuid/ticket8238/trac_8238.patch) by @rlmill created at 2010-06-05 22:08:28",
    "created_at": "2010-06-05T22:08:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72675",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_8238.patch](tarball://root/attachments/some-uuid/ticket8238/trac_8238.patch) by @rlmill created at 2010-06-05 22:08:28



---

archive/issue_comments_072676.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-05T22:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72676",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072677.json:
```json
{
    "body": "OK!",
    "created_at": "2010-06-06T10:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72677",
    "user": "https://github.com/JohnCremona"
}
```

OK!



---

archive/issue_comments_072678.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-06T10:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72678",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072679.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-07T05:24:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8238#issuecomment-72679",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_019707.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-07T05:24:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8238",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8238#event-19707"
}
```

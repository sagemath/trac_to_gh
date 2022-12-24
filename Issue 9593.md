# Issue 9593: spring layout does not converge on some graphs

archive/issues_009593.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  @rlmill @fchapoton\n\nTry the following in 4.5.2.alpha0 (or after applying #9532):\n\n```\nsage: G = graphs.PetersenGraph()\nsage: set_random_seed(0); G.plot(layout='spring', iterations=10000)\nsage: set_random_seed(0); G.plot(layout='spring', iterations=10001)\n```\n\nI get very different-looking graphs.  (If you go back and try with iterations=10000 again, you get the same graph again, showing that #9532 did make it reproducible, at least.)\n\nMaybe some constants need tweaking?\n\nI think this may be causing the problem reported in the first comment on #9584.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9593\n\n",
    "created_at": "2010-07-24T18:32:43Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "spring layout does not converge on some graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9593",
    "user": "cwitty"
}
```
Assignee: jason, ncohen, rlm

CC:  @rlmill @fchapoton

Try the following in 4.5.2.alpha0 (or after applying #9532):

```
sage: G = graphs.PetersenGraph()
sage: set_random_seed(0); G.plot(layout='spring', iterations=10000)
sage: set_random_seed(0); G.plot(layout='spring', iterations=10001)
```

I get very different-looking graphs.  (If you go back and try with iterations=10000 again, you get the same graph again, showing that #9532 did make it reproducible, at least.)

Maybe some constants need tweaking?

I think this may be causing the problem reported in the first comment on #9584.

Issue created by migration from https://trac.sagemath.org/ticket/9593





---

archive/issue_comments_092813.json:
```json
{
    "body": "Replying to [ticket:9593 cwitty]:\n> I think this may be causing the problem reported in the first comment on #9584.\n\nCarl, should we fix that one here (numeric noise causing doctest failure)?",
    "created_at": "2010-07-24T20:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9593#issuecomment-92813",
    "user": "@nexttime"
}
```

Replying to [ticket:9593 cwitty]:
> I think this may be causing the problem reported in the first comment on #9584.

Carl, should we fix that one here (numeric noise causing doctest failure)?



---

archive/issue_comments_092814.json:
```json
{
    "body": "The story so far: #9532 tried to make spring layout reproducible (and added tests to see that it was reproducible), but it wasn't enough and so the layout is actually not reproducible across platforms.  Before #9532, spring layout was totally non-reproducible.\n\nSo in my opinion, the correct thing to do for the next release is just to remove the failing doctest.  Spring layout wasn't reproducible before, so nobody can be depending on it being reproducible; and it isn't now, so there's no point in a test that verifies that it is reproducible.  The patch that removes the doctest should not go on this ticket (removing the doctest is not part of fixing layout convergence).  When this ticket is fixed, the doctest (or a similar one) should be added, to show that spring layout then does become reproducible.",
    "created_at": "2010-07-24T22:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9593#issuecomment-92814",
    "user": "cwitty"
}
```

The story so far: #9532 tried to make spring layout reproducible (and added tests to see that it was reproducible), but it wasn't enough and so the layout is actually not reproducible across platforms.  Before #9532, spring layout was totally non-reproducible.

So in my opinion, the correct thing to do for the next release is just to remove the failing doctest.  Spring layout wasn't reproducible before, so nobody can be depending on it being reproducible; and it isn't now, so there's no point in a test that verifies that it is reproducible.  The patch that removes the doctest should not go on this ticket (removing the doctest is not part of fixing layout convergence).  When this ticket is fixed, the doctest (or a similar one) should be added, to show that spring layout then does become reproducible.



---

archive/issue_comments_092815.json:
```json
{
    "body": "Ok, I'll open a new ticket that simply adds a `# random` to that doctest.",
    "created_at": "2010-07-24T22:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9593#issuecomment-92815",
    "user": "@nexttime"
}
```

Ok, I'll open a new ticket that simply adds a `# random` to that doctest.



---

archive/issue_comments_092816.json:
```json
{
    "body": "Replying to [comment:3 leif]:\n> Ok, I'll open a new ticket that simply adds a `# random` to that doctest.\n\nOh, I completely forgot to add this here: The related *doctest error* in Sage 4.5.2.alpha0 is now #9594, which already has positive review. (The comment in the patch links back to *this* ticket, which I found more appropriate, since the `# random` tag can hopefully be removed again once we have *reproducible* spring layout.)",
    "created_at": "2010-07-25T19:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9593#issuecomment-92816",
    "user": "@nexttime"
}
```

Replying to [comment:3 leif]:
> Ok, I'll open a new ticket that simply adds a `# random` to that doctest.

Oh, I completely forgot to add this here: The related *doctest error* in Sage 4.5.2.alpha0 is now #9594, which already has positive review. (The comment in the patch links back to *this* ticket, which I found more appropriate, since the `# random` tag can hopefully be removed again once we have *reproducible* spring layout.)



---

archive/issue_comments_092817.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-07-15T20:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9593#issuecomment-92817",
    "user": "@jm58660"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092818.json:
```json
{
    "body": "I think that this one has just forgotten to be closed. Fr\u00e9d\u00e9ric, please click positive_review if you agree.",
    "created_at": "2016-07-15T20:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9593#issuecomment-92818",
    "user": "@jm58660"
}
```

I think that this one has just forgotten to be closed. Frédéric, please click positive_review if you agree.



---

archive/issue_comments_092819.json:
```json
{
    "body": "ok, let us close that",
    "created_at": "2016-07-15T20:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9593#issuecomment-92819",
    "user": "@fchapoton"
}
```

ok, let us close that



---

archive/issue_comments_092820.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-07-15T20:57:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9593#issuecomment-92820",
    "user": "@fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092821.json:
```json
{
    "body": "Determined to be invalid/duplicate/wontfix (closing as \"wontfix\" as a catch-all resolution).",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9593#issuecomment-92821",
    "user": "@embray"
}
```

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).



---

archive/issue_comments_092822.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9593#issuecomment-92822",
    "user": "@embray"
}
```

Resolution: wontfix

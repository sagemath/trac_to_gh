# Issue 8732: bug in new HMM code

archive/issues_008732.json:
```json
{
    "body": "Assignee: amhou\n\nCC:  mhampton boothby @jasongrout\n\nCrap, there is a bug in the new HMM code (#8547) that just went into sage-4.4.alpha0:\n\nTry this:\n\n\n```\nsage: m = hmm.DiscreteHiddenMarkovModel([[1/3]*3]*3, [ [5]*5 ]*3, [1/3]*3, 'abcde'); m\nsage: v = list('a'*100); v\nsage: m.baum_welch(v)\nsage: m.sample(10)\n['e', 'a', 'e', 'e', 'a', 'c', 'c', 'c', 'c', 'a']\nsage: m\nDiscrete Hidden Markov Model with 3 States and 5 Emissions\nTransition matrix:\n[0.333333333333 0.333333333333 0.333333333333]\n[0.333333333333 0.333333333333 0.333333333333]\n[0.333333333333 0.333333333333 0.333333333333]\nEmission matrix:\n[1.0 0.0 0.0 0.0 0.0]\n[1.0 0.0 0.0 0.0 0.0]\n[1.0 0.0 0.0 0.0 0.0]\nInitial probabilities: [0.3333, 0.3333, 0.3333]\n```\n\n\nNotice above that it is impossible for the model to emit anything except 'a'.  Yet in the sample it does!  \n\nThis bug wasn't in the previous HMM code, of course.  I'll fix this ASAP for sage-4.4. \n\n\nWilliam\n\nIssue created by migration from https://trac.sagemath.org/ticket/8732\n\n",
    "created_at": "2010-04-20T20:48:47Z",
    "labels": [
        "component: statistics",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "bug in new HMM code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8732",
    "user": "https://github.com/williamstein"
}
```
Assignee: amhou

CC:  mhampton boothby @jasongrout

Crap, there is a bug in the new HMM code (#8547) that just went into sage-4.4.alpha0:

Try this:


```
sage: m = hmm.DiscreteHiddenMarkovModel([[1/3]*3]*3, [ [5]*5 ]*3, [1/3]*3, 'abcde'); m
sage: v = list('a'*100); v
sage: m.baum_welch(v)
sage: m.sample(10)
['e', 'a', 'e', 'e', 'a', 'c', 'c', 'c', 'c', 'a']
sage: m
Discrete Hidden Markov Model with 3 States and 5 Emissions
Transition matrix:
[0.333333333333 0.333333333333 0.333333333333]
[0.333333333333 0.333333333333 0.333333333333]
[0.333333333333 0.333333333333 0.333333333333]
Emission matrix:
[1.0 0.0 0.0 0.0 0.0]
[1.0 0.0 0.0 0.0 0.0]
[1.0 0.0 0.0 0.0 0.0]
Initial probabilities: [0.3333, 0.3333, 0.3333]
```


Notice above that it is impossible for the model to emit anything except 'a'.  Yet in the sample it does!  

This bug wasn't in the previous HMM code, of course.  I'll fix this ASAP for sage-4.4. 


William

Issue created by migration from https://trac.sagemath.org/ticket/8732





---

archive/issue_comments_079683.json:
```json
{
    "body": "Attachment [trac_8732.patch](tarball://root/attachments/some-uuid/ticket8732/trac_8732.patch) by @williamstein created at 2010-04-20 21:46:04",
    "created_at": "2010-04-20T21:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8732#issuecomment-79683",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8732.patch](tarball://root/attachments/some-uuid/ticket8732/trac_8732.patch) by @williamstein created at 2010-04-20 21:46:04



---

archive/issue_comments_079684.json:
```json
{
    "body": "I had a C array index backwards.",
    "created_at": "2010-04-20T21:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8732#issuecomment-79684",
    "user": "https://github.com/williamstein"
}
```

I had a C array index backwards.



---

archive/issue_comments_079685.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-20T21:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8732#issuecomment-79685",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079686.json:
```json
{
    "body": "I'm cc'ing some possible reviewers...",
    "created_at": "2010-04-20T23:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8732#issuecomment-79686",
    "user": "https://github.com/jhpalmieri"
}
```

I'm cc'ing some possible reviewers...



---

archive/issue_comments_079687.json:
```json
{
    "body": "OK, patch looks good.  Passes tests and coverage, change makes sense, and I did some random testing so I am giving this a positive review.",
    "created_at": "2010-04-21T03:11:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8732#issuecomment-79687",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

OK, patch looks good.  Passes tests and coverage, change makes sense, and I did some random testing so I am giving this a positive review.



---

archive/issue_comments_079688.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-21T03:11:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8732#issuecomment-79688",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079689.json:
```json
{
    "body": "Merged into 4.4.alpha2.",
    "created_at": "2010-04-23T17:09:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8732#issuecomment-79689",
    "user": "https://github.com/jhpalmieri"
}
```

Merged into 4.4.alpha2.



---

archive/issue_comments_079690.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-23T17:09:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8732#issuecomment-79690",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_events_021209.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-23T17:09:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8732",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8732#event-21209"
}
```

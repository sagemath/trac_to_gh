# Issue 2693: Sage should have generic resultant implementation for multivariate polynomials

archive/issues_002693.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @tscrim @videlec @vinklein\n\nConsider this example, which fails:\n\n```\nR.<x,y> = RR[]\np = x + y\nq = x*y\np.resultant(q)\n```\n(as reported here: http://groups.google.com/group/sage-support/browse_thread/thread/1d6289cead33d063#)\n\nThis is because multivariate resultants are implemented using the Singular pexpect interface, which does not support RR.\n\nA workaround for this particular problem (and a possible basis for an improved version) is:\n\n```\np.polynomial(x).resultant(q.polynomial(x)) \n```\nThat is, fall back to univariate resultants, which are implemented using Pari and are somewhat more generic.  (This is still not truly generic, though, since there are Sage rings which have no Pari equivalent.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/2693\n\n",
    "created_at": "2008-03-28T02:21:37Z",
    "labels": [
        "component: algebraic geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.8",
    "title": "Sage should have generic resultant implementation for multivariate polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2693",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

CC:  @tscrim @videlec @vinklein

Consider this example, which fails:

```
R.<x,y> = RR[]
p = x + y
q = x*y
p.resultant(q)
```
(as reported here: http://groups.google.com/group/sage-support/browse_thread/thread/1d6289cead33d063#)

This is because multivariate resultants are implemented using the Singular pexpect interface, which does not support RR.

A workaround for this particular problem (and a possible basis for an improved version) is:

```
p.polynomial(x).resultant(q.polynomial(x)) 
```
That is, fall back to univariate resultants, which are implemented using Pari and are somewhat more generic.  (This is still not truly generic, though, since there are Sage rings which have no Pari equivalent.)

Issue created by migration from https://trac.sagemath.org/ticket/2693





---

archive/issue_events_006279.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2693#event-6279"
}
```



---

archive/issue_events_006280.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2693#event-6280"
}
```



---

archive/issue_events_006281.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2693#event-6281"
}
```



---

archive/issue_events_006282.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2693#event-6282"
}
```



---

archive/issue_events_006283.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2693#event-6283"
}
```



---

archive/issue_events_006284.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2693#event-6284"
}
```



---

archive/issue_events_006285.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2693#event-6285"
}
```



---

archive/issue_comments_018489.json:
```json
{
    "body": "In fact, singular resultants are slow compared to other methods, so it would really be a good idea to write specific sage code for resultants.\n\nSee #16749 and #12174 for ideas about it.\n\nJust something like:\n\n```\ndef resultant(self, other, variable):\n    m = self.sylvester_matrix(other, variable)\n    return m.determinant()\n```\n\nWould be both general for any polynomial ring, and faster than the current implementation. And of course, there could be a lot of cases where things can be done much faster, using specific backends where they are better.",
    "created_at": "2014-08-25T08:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18489",
    "user": "https://github.com/miguelmarco"
}
```

In fact, singular resultants are slow compared to other methods, so it would really be a good idea to write specific sage code for resultants.

See #16749 and #12174 for ideas about it.

Just something like:

```
def resultant(self, other, variable):
    m = self.sylvester_matrix(other, variable)
    return m.determinant()
```

Would be both general for any polynomial ring, and faster than the current implementation. And of course, there could be a lot of cases where things can be done much faster, using specific backends where they are better.



---

archive/issue_comments_018490.json:
```json
{
    "body": "Changing keywords from \"\" to \"resultant\".",
    "created_at": "2019-05-01T14:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18490",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "resultant".



---

archive/issue_comments_018491.json:
```json
{
    "body": "New commits:",
    "created_at": "2019-05-01T15:04:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18491",
    "user": "https://github.com/fchapoton"
}
```

New commits:



---

archive/issue_events_006286.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2019-05-01T15:04:51Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2693#event-6286"
}
```



---

archive/issue_events_006287.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2019-05-01T15:04:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "milestone": "sage-8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2693#event-6287"
}
```



---

archive/issue_comments_018492.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2019-05-01T15:04:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18492",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_018493.json:
```json
{
    "body": "green bot, please review",
    "created_at": "2019-05-01T18:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18493",
    "user": "https://github.com/fchapoton"
}
```

green bot, please review



---

archive/issue_comments_018494.json:
```json
{
    "body": "hmm, the second doctest is more about univariate polynomials. Maybe it should go there ?",
    "created_at": "2019-05-02T06:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18494",
    "user": "https://github.com/fchapoton"
}
```

hmm, the second doctest is more about univariate polynomials. Maybe it should go there ?



---

archive/issue_comments_018495.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2019-05-06T15:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18495",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_018496.json:
```json
{
    "body": "ok, test is now at the right place.",
    "created_at": "2019-05-06T15:47:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18496",
    "user": "https://github.com/fchapoton"
}
```

ok, test is now at the right place.



---

archive/issue_comments_018497.json:
```json
{
    "body": "and the bot is green.",
    "created_at": "2019-05-06T17:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18497",
    "user": "https://github.com/fchapoton"
}
```

and the bot is green.



---

archive/issue_comments_018498.json:
```json
{
    "body": "LGTM.",
    "created_at": "2019-05-07T00:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18498",
    "user": "https://github.com/tscrim"
}
```

LGTM.



---

archive/issue_comments_018499.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2019-05-07T00:56:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18499",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_018500.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2019-05-12T21:34:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2693#issuecomment-18500",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_006288.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2019-05-12T21:34:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2693",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2693#event-6288"
}
```

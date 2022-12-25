# Issue 9169: cygwin: a cachefunc.py doctest hangs seemingly forever

archive/issues_009169.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jpflori @dimpase @kcrisman\n\nOn Cygwin, the following test hangs:\n\n```\n\n            sage: @cached_function\n            ... def oddprime_factors(n):\n            ...     l = [p for p,e in factor(n) if p != 2]\n            ...     return len(l)\n            sage: oddprime_factors.precompute(range(1,100), 4)\n```\n\nThe above is very fast on any other platform. \n\nThis results in a doctest file failure:\n\n```\nsage -t  \"devel/sage/sage/misc/cachefunc.py\"                \n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n\t [361.6 s]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9169\n\n",
    "created_at": "2010-06-07T04:32:34Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cygwin: a cachefunc.py doctest hangs seemingly forever",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9169",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  jpflori @dimpase @kcrisman

On Cygwin, the following test hangs:

```

            sage: @cached_function
            ... def oddprime_factors(n):
            ...     l = [p for p,e in factor(n) if p != 2]
            ...     return len(l)
            sage: oddprime_factors.precompute(range(1,100), 4)
```

The above is very fast on any other platform. 

This results in a doctest file failure:

```
sage -t  "devel/sage/sage/misc/cachefunc.py"                
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
	 [361.6 s]
```

Issue created by migration from https://trac.sagemath.org/ticket/9169





---

archive/issue_comments_085595.json:
```json
{
    "body": "FWIW, this file is now `cachefunc.pyx`.",
    "created_at": "2013-01-15T15:20:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9169#issuecomment-85595",
    "user": "https://github.com/kcrisman"
}
```

FWIW, this file is now `cachefunc.pyx`.



---

archive/issue_comments_085596.json:
```json
{
    "body": "This same test still fails, though for me it is because of forking errors and an inability to start Singular at times (presumably for that reason).",
    "created_at": "2013-01-15T15:46:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9169#issuecomment-85596",
    "user": "https://github.com/kcrisman"
}
```

This same test still fails, though for me it is because of forking errors and an inability to start Singular at times (presumably for that reason).



---

archive/issue_comments_085597.json:
```json
{
    "body": "On my install (64bits Windows 7 + sage 5.6.rc0) the test passes.",
    "created_at": "2013-01-15T18:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9169#issuecomment-85597",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

On my install (64bits Windows 7 + sage 5.6.rc0) the test passes.



---

archive/issue_comments_085598.json:
```json
{
    "body": "That's good to hear.  I am frustrated by this forking business.  A complete rebase just shifts the error to a different random file that won't be remapped.  So I can never tell whether things are really a problem or not.",
    "created_at": "2013-01-15T18:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9169#issuecomment-85598",
    "user": "https://github.com/kcrisman"
}
```

That's good to hear.  I am frustrated by this forking business.  A complete rebase just shifts the error to a different random file that won't be remapped.  So I can never tell whether things are really a problem or not.



---

archive/issue_comments_085599.json:
```json
{
    "body": "Replying to [comment:5 kcrisman]:\n> That's good to hear.  I am frustrated by this forking business.  A complete rebase just shifts the error to a different random file that won't be remapped.  So I can never tell whether things are really a problem or not.\n\n\nAre you working on a 32-bit Windows? I've given up on attempting to use Cygwin on 32-bit systems.\n\nAnyhow, this test works for me too. Let's close this one.",
    "created_at": "2013-01-27T10:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9169#issuecomment-85599",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:5 kcrisman]:
> That's good to hear.  I am frustrated by this forking business.  A complete rebase just shifts the error to a different random file that won't be remapped.  So I can never tell whether things are really a problem or not.


Are you working on a 32-bit Windows? I've given up on attempting to use Cygwin on 32-bit systems.

Anyhow, this test works for me too. Let's close this one.



---

archive/issue_comments_085600.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-01-27T10:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9169#issuecomment-85600",
    "user": "https://github.com/dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085601.json:
```json
{
    "body": "I'd feel best if we were able to try on 32-bit XP... though I recognize this may be impossible unless my box stops acting up.",
    "created_at": "2013-01-28T02:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9169#issuecomment-85601",
    "user": "https://github.com/kcrisman"
}
```

I'd feel best if we were able to try on 32-bit XP... though I recognize this may be impossible unless my box stops acting up.



---

archive/issue_comments_085602.json:
```json
{
    "body": "When the status on my 64 bits Windows 7 looks good enough (which looks close), I'll dig up an old 32 bits install and give it a try.",
    "created_at": "2013-01-30T10:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9169#issuecomment-85602",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

When the status on my 64 bits Windows 7 looks good enough (which looks close), I'll dig up an old 32 bits install and give it a try.



---

archive/issue_comments_085603.json:
```json
{
    "body": "This is ok on 32 bits Windows 7, so I'll close it.",
    "created_at": "2013-02-08T12:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9169#issuecomment-85603",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

This is ok on 32 bits Windows 7, so I'll close it.



---

archive/issue_comments_085604.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-08T12:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9169#issuecomment-85604",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022556.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/jpflori",
    "created_at": "2013-02-08T12:41:16Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9169",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9169#event-22556"
}
```



---

archive/issue_events_022557.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-02-08T13:21:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9169",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9169#event-22557"
}
```



---

archive/issue_comments_085605.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-02-08T13:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9169#issuecomment-85605",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme

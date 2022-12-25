# Issue 959: errors building sage because singular gets confused by system-wide boost

archive/issues_000959.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\n> It looks like maybe there is an issue with the system-wide boost\n> you have installed.\n\nThanks William. Moving /usr/include/boost to /usr/include/boost.old and\ntyping again make in SAGE_ROOT did it. You can recommend it to users who\nencounter the same problem.\n```\n\n\nSo, can we turn off Singular using boost at all, by default?\n\nIssue created by migration from https://trac.sagemath.org/ticket/959\n\n",
    "created_at": "2007-10-21T12:41:12Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "errors building sage because singular gets confused by system-wide boost",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/959",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
> It looks like maybe there is an issue with the system-wide boost
> you have installed.

Thanks William. Moving /usr/include/boost to /usr/include/boost.old and
typing again make in SAGE_ROOT did it. You can recommend it to users who
encounter the same problem.
```


So, can we turn off Singular using boost at all, by default?

Issue created by migration from https://trac.sagemath.org/ticket/959





---

archive/issue_comments_005824.json:
```json
{
    "body": "Well, we should fix the bug upstream by fixing the boost detection code or alternatively introducing a switch to turn off boost.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-21T13:43:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/959#issuecomment-5824",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Well, we should fix the bug upstream by fixing the boost detection code or alternatively introducing a switch to turn off boost.

Cheers,

Michael



---

archive/issue_comments_005825.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-21T22:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/959#issuecomment-5825",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005826.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2007-10-21T22:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/959#issuecomment-5826",
    "user": "https://github.com/malb"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_comments_005827.json:
```json
{
    "body": "We can't just turn it off because they don't have an option for that for their configure script. Also, fiddling with that script is tricky because it is created from a configure.in newer autoconfs don't understand. I'll report this upstream.",
    "created_at": "2007-10-23T21:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/959#issuecomment-5827",
    "user": "https://github.com/malb"
}
```

We can't just turn it off because they don't have an option for that for their configure script. Also, fiddling with that script is tricky because it is created from a configure.in newer autoconfs don't understand. I'll report this upstream.



---

archive/issue_comments_005828.json:
```json
{
    "body": "I reported this upstream and a fix will be available in the next point release of Singular. In the meantime Hans recommends to comment out this code\n\n\n```\n#ifdef HAVE_BOOST_DYNAMIC_BITSET_HPP\n#define  HAVE_BOOST 1\n#endif\n```\n\n\nin `kernel/tgb_internal.h`.",
    "created_at": "2007-10-30T14:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/959#issuecomment-5828",
    "user": "https://github.com/malb"
}
```

I reported this upstream and a fix will be available in the next point release of Singular. In the meantime Hans recommends to comment out this code


```
#ifdef HAVE_BOOST_DYNAMIC_BITSET_HPP
#define  HAVE_BOOST 1
#endif
```


in `kernel/tgb_internal.h`.



---

archive/issue_comments_005829.json:
```json
{
    "body": "The code stated above was commented out in the most recent singular spkg found at: http://sage.math.washington.edu/home/malb/pkgs/singular-3-0-3-2-20071031.spkg",
    "created_at": "2007-10-31T12:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/959#issuecomment-5829",
    "user": "https://github.com/malb"
}
```

The code stated above was commented out in the most recent singular spkg found at: http://sage.math.washington.edu/home/malb/pkgs/singular-3-0-3-2-20071031.spkg



---

archive/issue_comments_005830.json:
```json
{
    "body": "applied to 2.8.11.alpha0: this should have been fixed via the new Singular.spkg from #948.",
    "created_at": "2007-11-01T10:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/959#issuecomment-5830",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.11.alpha0: this should have been fixed via the new Singular.spkg from #948.



---

archive/issue_comments_005831.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-01T10:36:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/959",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/959#issuecomment-5831",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

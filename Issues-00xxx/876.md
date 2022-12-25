# Issue 876: Implement or wrap Braid Groups

archive/issues_000876.json:
```json
{
    "body": "Assignee: @robertwb\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/876\n\n",
    "closed_at": "2012-07-17T08:34:38Z",
    "created_at": "2007-10-13T09:03:20Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Implement or wrap Braid Groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/876",
    "user": "https://github.com/robertwb"
}
```
Assignee: @robertwb



Issue created by migration from https://trac.sagemath.org/ticket/876





---

archive/issue_comments_005400.json:
```json
{
    "body": "Changing assignee from @williamstein to @robertwb.",
    "created_at": "2007-10-13T09:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/876#issuecomment-5400",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @williamstein to @robertwb.



---

archive/issue_events_002443.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-13T12:12:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/876",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/876#event-2443"
}
```



---

archive/issue_events_002444.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-05T22:25:12Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/876",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/876#event-2444"
}
```



---

archive/issue_events_002445.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-05T22:25:12Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/876",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/876#event-2445"
}
```



---

archive/issue_comments_005401.json:
```json
{
    "body": "This looks very much like a wish list item. Moved.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T22:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/876#issuecomment-5401",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This looks very much like a wish list item. Moved.

Cheers,

Michael



---

archive/issue_comments_005402.json:
```json
{
    "body": "BTW, in gap_packages there is a GPL'd package called braid that might help here. It was packaged before GPLv3 came out (I actually did the packaging but did not write any of the code).",
    "created_at": "2008-12-05T22:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/876#issuecomment-5402",
    "user": "https://github.com/wdjoyner"
}
```

BTW, in gap_packages there is a GPL'd package called braid that might help here. It was packaged before GPLv3 came out (I actually did the packaging but did not write any of the code).



---

archive/issue_comments_005403.json:
```json
{
    "body": "Incidentally, apparently the braid package is now autoloaded, though it doesn't seem to be used anywhere.  This is improperly documented in interfaces/gap.py, though:\n\n```\n    The packages sonata, guava, factint, gapdoc, grape, design, toric,\n    and laguna are loaded in all cases before the workspace is saved,\n    if they are available.\n```\n\n```\n    g = Gap(use_workspace_cache=False, max_workspace_size=None)\n    for pkg in ['ctbllib', 'sonata', 'guava', 'factint', \\\n                'gapdoc', 'grape', 'design', \\\n                'toric', 'laguna', 'braid']:   # NOTE: Do *not* autoload hap - it screws up PolynomialRing(Rationals,2)\n        try:\n            g.load_package(pkg, verbose=verbose)\n```",
    "created_at": "2009-12-30T05:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/876#issuecomment-5403",
    "user": "https://github.com/kcrisman"
}
```

Incidentally, apparently the braid package is now autoloaded, though it doesn't seem to be used anywhere.  This is improperly documented in interfaces/gap.py, though:

```
    The packages sonata, guava, factint, gapdoc, grape, design, toric,
    and laguna are loaded in all cases before the workspace is saved,
    if they are available.
```

```
    g = Gap(use_workspace_cache=False, max_workspace_size=None)
    for pkg in ['ctbllib', 'sonata', 'guava', 'factint', \
                'gapdoc', 'grape', 'design', \
                'toric', 'laguna', 'braid']:   # NOTE: Do *not* autoload hap - it screws up PolynomialRing(Rationals,2)
        try:
            g.load_package(pkg, verbose=verbose)
```



---

archive/issue_comments_005404.json:
```json
{
    "body": "Replying to [comment:5 kcrisman]:\n> Incidentally, apparently the braid package is now autoloaded, though it doesn't seem to be used anywhere.  This is improperly documented in interfaces/gap.py, though:\n> \n> ```\n>     The packages sonata, guava, factint, gapdoc, grape, design, toric,\n>     and laguna are loaded in all cases before the workspace is saved,\n>     if they are available.\n> ```\n> \n> ```\n>     g = Gap(use_workspace_cache=False, max_workspace_size=None)\n>     for pkg in ['ctbllib', 'sonata', 'guava', 'factint', \\\n>                 'gapdoc', 'grape', 'design', \\\n>                 'toric', 'laguna', 'braid']:   # NOTE: Do *not* autoload hap - it screws up PolynomialRing(Rationals,2)\n>         try:\n>             g.load_package(pkg, verbose=verbose)\n> ```\n\n\nI think this problem with HAP was fixed long ago.\n\nAlso, I think I had to repackage braid recently because of some loading problems it had. I don't remember the details. Maybe it was because of a problem with gap 4.4.12 and since we use 4.4.10, it is not an issue?",
    "created_at": "2009-12-30T12:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/876#issuecomment-5404",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:5 kcrisman]:
> Incidentally, apparently the braid package is now autoloaded, though it doesn't seem to be used anywhere.  This is improperly documented in interfaces/gap.py, though:
> 
> ```
>     The packages sonata, guava, factint, gapdoc, grape, design, toric,
>     and laguna are loaded in all cases before the workspace is saved,
>     if they are available.
> ```
> 
> ```
>     g = Gap(use_workspace_cache=False, max_workspace_size=None)
>     for pkg in ['ctbllib', 'sonata', 'guava', 'factint', \
>                 'gapdoc', 'grape', 'design', \
>                 'toric', 'laguna', 'braid']:   # NOTE: Do *not* autoload hap - it screws up PolynomialRing(Rationals,2)
>         try:
>             g.load_package(pkg, verbose=verbose)
> ```


I think this problem with HAP was fixed long ago.

Also, I think I had to repackage braid recently because of some loading problems it had. I don't remember the details. Maybe it was because of a problem with gap 4.4.12 and since we use 4.4.10, it is not an issue?



---

archive/issue_events_002446.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2012-07-07T03:01:18Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/876",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/876#event-2446"
}
```



---

archive/issue_events_002447.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2012-07-07T03:01:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/876",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/876#event-2447"
}
```



---

archive/issue_comments_005405.json:
```json
{
    "body": "Looks like this is now much further along at #12339.",
    "created_at": "2012-07-07T03:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/876#issuecomment-5405",
    "user": "https://github.com/kcrisman"
}
```

Looks like this is now much further along at #12339.



---

archive/issue_comments_005406.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-07-07T03:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/876#issuecomment-5406",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_005407.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-07-07T03:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/876#issuecomment-5407",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_002448.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-07-17T08:34:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/876",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/876#event-2448"
}
```



---

archive/issue_comments_005408.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-07-17T08:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/876#issuecomment-5408",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate

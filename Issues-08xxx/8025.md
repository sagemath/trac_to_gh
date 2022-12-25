# Issue 8025: artificially bump the version number of the scipy and scipy_sandbox spkg's

archive/issues_008025.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8025\n\n",
    "closed_at": "2010-06-03T03:57:22Z",
    "created_at": "2010-01-21T16:05:00Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "artificially bump the version number of the scipy and scipy_sandbox spkg's",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8025",
    "user": "https://github.com/williamstein"
}
```
Assignee: GeorgSWeber



Issue created by migration from https://trac.sagemath.org/ticket/8025





---

archive/issue_comments_069988.json:
```json
{
    "body": "Definitely \"sage -upgrade\" doesn't work right now (from 4.3 to 4.3.1).  \nDefinitely doing\n\n```\n  sage -f spkg/standard/scipy_sandbox-20071020.p4.spkg\n  sage -f spkg/standard/scipy-0.7.p3.spkg\n```\nfixes the problem.  But I'm confused since scipy and scipy_sandbox depend on fortran, so they should be forced to be rebuilt anyways.  Hmm..",
    "created_at": "2010-01-21T16:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8025#issuecomment-69988",
    "user": "https://github.com/williamstein"
}
```

Definitely "sage -upgrade" doesn't work right now (from 4.3 to 4.3.1).  
Definitely doing

```
  sage -f spkg/standard/scipy_sandbox-20071020.p4.spkg
  sage -f spkg/standard/scipy-0.7.p3.spkg
```
fixes the problem.  But I'm confused since scipy and scipy_sandbox depend on fortran, so they should be forced to be rebuilt anyways.  Hmm..



---

archive/issue_events_019224.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-01-21T16:08:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8025",
    "milestone": "sage-4.3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8025#event-19224"
}
```



---

archive/issue_comments_069989.json:
```json
{
    "body": "More precisely, the following fixes the problem:\n\n```\n./sage -f numpy-1.3.0.p2.spkg scipy_sandbox-20071020.p4.spkg scipy-0.7.p3.spkg\n```",
    "created_at": "2010-01-21T16:20:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8025#issuecomment-69989",
    "user": "https://github.com/williamstein"
}
```

More precisely, the following fixes the problem:

```
./sage -f numpy-1.3.0.p2.spkg scipy_sandbox-20071020.p4.spkg scipy-0.7.p3.spkg
```



---

archive/issue_comments_069990.json:
```json
{
    "body": "Deferred to Sage 5.0 since I don't see a patch or new spkg's.",
    "created_at": "2010-04-23T04:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8025#issuecomment-69990",
    "user": "https://github.com/jhpalmieri"
}
```

Deferred to Sage 5.0 since I don't see a patch or new spkg's.



---

archive/issue_events_019225.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-23T04:57:06Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8025",
    "milestone": "sage-4.3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8025#event-19225"
}
```



---

archive/issue_events_019226.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-23T04:57:06Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8025",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8025#event-19226"
}
```



---

archive/issue_events_019227.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-27T14:23:25Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8025",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8025#event-19227"
}
```



---

archive/issue_events_019228.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-27T14:23:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8025",
    "milestone": "sage-4.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8025#event-19228"
}
```



---

archive/issue_events_019229.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-06-03T03:57:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8025",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8025#event-19229"
}
```



---

archive/issue_comments_069991.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-03T03:57:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8025#issuecomment-69991",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_069992.json:
```json
{
    "body": "I've bumped both spkg version numbers, as requested, for sage-4.4.3.alpha2.",
    "created_at": "2010-06-03T03:57:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8025",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8025#issuecomment-69992",
    "user": "https://github.com/williamstein"
}
```

I've bumped both spkg version numbers, as requested, for sage-4.4.3.alpha2.

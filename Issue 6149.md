# Issue 6149: Fix ReST glitches

archive/issues_006149.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @JohnCremona\n\nBuilding the documentation currently raises something like 50 errors because of incorrect ReST formatting in docstrings (mostly \"unexpected indent\" or similar). We should probably have a policy of not merging patches that cause documentation building errors, just as we don't merge patches that cause doctest failures.\n\nI have found and fixed most of the errors in 4.0.rc1 (some with great difficulty, because the ReST parser is very unreliable at telling you where the error is arising in a given file).\n\nI know this is a bit last-minute, but the patch below doesn't actually change any code at all, so it might not be too late to include it in the final 4.0 release.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6149\n\n",
    "created_at": "2009-05-28T13:05:02Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Fix ReST glitches",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6149",
    "user": "https://github.com/loefflerd"
}
```
Assignee: tba

CC:  @JohnCremona

Building the documentation currently raises something like 50 errors because of incorrect ReST formatting in docstrings (mostly "unexpected indent" or similar). We should probably have a policy of not merging patches that cause documentation building errors, just as we don't merge patches that cause doctest failures.

I have found and fixed most of the errors in 4.0.rc1 (some with great difficulty, because the ReST parser is very unreliable at telling you where the error is arising in a given file).

I know this is a bit last-minute, but the patch below doesn't actually change any code at all, so it might not be too late to include it in the final 4.0 release.

Issue created by migration from https://trac.sagemath.org/ticket/6149





---

archive/issue_comments_048984.json:
```json
{
    "body": "Attachment [trac_6149.patch](tarball://root/attachments/some-uuid/ticket6149/trac_6149.patch) by @loefflerd created at 2009-05-28 13:15:25\n\npatch against 4.0.rc1",
    "created_at": "2009-05-28T13:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-48984",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_6149.patch](tarball://root/attachments/some-uuid/ticket6149/trac_6149.patch) by @loefflerd created at 2009-05-28 13:15:25

patch against 4.0.rc1



---

archive/issue_comments_048985.json:
```json
{
    "body": "With the above patch applied, the documentation should build fine.\n\nJohn: I've cced you here, since you say you have suffered from this too :-) Any chance you could review this one quickly, since it would be good to get it into 4.0?",
    "created_at": "2009-05-28T13:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-48985",
    "user": "https://github.com/loefflerd"
}
```

With the above patch applied, the documentation should build fine.

John: I've cced you here, since you say you have suffered from this too :-) Any chance you could review this one quickly, since it would be good to get it into 4.0?



---

archive/issue_comments_048986.json:
```json
{
    "body": "Attachment [trac_6149-2.patch](tarball://root/attachments/some-uuid/ticket6149/trac_6149-2.patch) by @mwhansen created at 2009-05-28 16:31:29",
    "created_at": "2009-05-28T16:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-48986",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6149-2.patch](tarball://root/attachments/some-uuid/ticket6149/trac_6149-2.patch) by @mwhansen created at 2009-05-28 16:31:29



---

archive/issue_comments_048987.json:
```json
{
    "body": "David's patch looks good to me.\n\nCould someone take a quick look at my patch?",
    "created_at": "2009-05-28T16:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-48987",
    "user": "https://github.com/mwhansen"
}
```

David's patch looks good to me.

Could someone take a quick look at my patch?



---

archive/issue_comments_048988.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-28T16:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-48988",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_048989.json:
```json
{
    "body": "Changing assignee from tba to @mwhansen.",
    "created_at": "2009-05-28T16:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-48989",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from tba to @mwhansen.



---

archive/issue_comments_048990.json:
```json
{
    "body": "Looks fine to me - docs build OK, and the dsage page looks good.\n\nDavid",
    "created_at": "2009-05-28T17:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-48990",
    "user": "https://github.com/loefflerd"
}
```

Looks fine to me - docs build OK, and the dsage page looks good.

David



---

archive/issue_events_014469.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-05-28T17:51:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6149#event-14469"
}
```



---

archive/issue_comments_048991.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-28T17:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-48991",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_048992.json:
```json
{
    "body": "Merged both patches in 4.0.rc2.",
    "created_at": "2009-05-28T17:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-48992",
    "user": "https://github.com/mwhansen"
}
```

Merged both patches in 4.0.rc2.



---

archive/issue_comments_048993.json:
```json
{
    "body": "This got refereed too quickly for me!  See #6152 for a few more fixes -- should be quick to referee.",
    "created_at": "2009-05-28T18:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-48993",
    "user": "https://github.com/jhpalmieri"
}
```

This got refereed too quickly for me!  See #6152 for a few more fixes -- should be quick to referee.

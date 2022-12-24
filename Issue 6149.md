# Issue 6149: Fix ReST glitches

archive/issues_006149.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @JohnCremona\n\nBuilding the documentation currently raises something like 50 errors because of incorrect ReST formatting in docstrings (mostly \"unexpected indent\" or similar). We should probably have a policy of not merging patches that cause documentation building errors, just as we don't merge patches that cause doctest failures.\n\nI have found and fixed most of the errors in 4.0.rc1 (some with great difficulty, because the ReST parser is very unreliable at telling you where the error is arising in a given file).\n\nI know this is a bit last-minute, but the patch below doesn't actually change any code at all, so it might not be too late to include it in the final 4.0 release.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6149\n\n",
    "created_at": "2009-05-28T13:05:02Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Fix ReST glitches",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6149",
    "user": "@loefflerd"
}
```
Assignee: tba

CC:  @JohnCremona

Building the documentation currently raises something like 50 errors because of incorrect ReST formatting in docstrings (mostly "unexpected indent" or similar). We should probably have a policy of not merging patches that cause documentation building errors, just as we don't merge patches that cause doctest failures.

I have found and fixed most of the errors in 4.0.rc1 (some with great difficulty, because the ReST parser is very unreliable at telling you where the error is arising in a given file).

I know this is a bit last-minute, but the patch below doesn't actually change any code at all, so it might not be too late to include it in the final 4.0 release.

Issue created by migration from https://trac.sagemath.org/ticket/6149





---

archive/issue_comments_049079.json:
```json
{
    "body": "Attachment [trac_6149.patch](tarball://root/attachments/some-uuid/ticket6149/trac_6149.patch) by @loefflerd created at 2009-05-28 13:15:25\n\npatch against 4.0.rc1",
    "created_at": "2009-05-28T13:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-49079",
    "user": "@loefflerd"
}
```

Attachment [trac_6149.patch](tarball://root/attachments/some-uuid/ticket6149/trac_6149.patch) by @loefflerd created at 2009-05-28 13:15:25

patch against 4.0.rc1



---

archive/issue_comments_049080.json:
```json
{
    "body": "With the above patch applied, the documentation should build fine.\n\nJohn: I've cced you here, since you say you have suffered from this too :-) Any chance you could review this one quickly, since it would be good to get it into 4.0?",
    "created_at": "2009-05-28T13:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-49080",
    "user": "@loefflerd"
}
```

With the above patch applied, the documentation should build fine.

John: I've cced you here, since you say you have suffered from this too :-) Any chance you could review this one quickly, since it would be good to get it into 4.0?



---

archive/issue_comments_049081.json:
```json
{
    "body": "Attachment [trac_6149-2.patch](tarball://root/attachments/some-uuid/ticket6149/trac_6149-2.patch) by @mwhansen created at 2009-05-28 16:31:29",
    "created_at": "2009-05-28T16:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-49081",
    "user": "@mwhansen"
}
```

Attachment [trac_6149-2.patch](tarball://root/attachments/some-uuid/ticket6149/trac_6149-2.patch) by @mwhansen created at 2009-05-28 16:31:29



---

archive/issue_comments_049082.json:
```json
{
    "body": "David's patch looks good to me.\n\nCould someone take a quick look at my patch?",
    "created_at": "2009-05-28T16:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-49082",
    "user": "@mwhansen"
}
```

David's patch looks good to me.

Could someone take a quick look at my patch?



---

archive/issue_comments_049083.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-28T16:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-49083",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049084.json:
```json
{
    "body": "Changing assignee from tba to @mwhansen.",
    "created_at": "2009-05-28T16:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-49084",
    "user": "@mwhansen"
}
```

Changing assignee from tba to @mwhansen.



---

archive/issue_comments_049085.json:
```json
{
    "body": "Looks fine to me - docs build OK, and the dsage page looks good.\n\nDavid",
    "created_at": "2009-05-28T17:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-49085",
    "user": "@loefflerd"
}
```

Looks fine to me - docs build OK, and the dsage page looks good.

David



---

archive/issue_comments_049086.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-28T17:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-49086",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_049087.json:
```json
{
    "body": "Merged both patches in 4.0.rc2.",
    "created_at": "2009-05-28T17:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-49087",
    "user": "@mwhansen"
}
```

Merged both patches in 4.0.rc2.



---

archive/issue_comments_049088.json:
```json
{
    "body": "This got refereed too quickly for me!  See #6152 for a few more fixes -- should be quick to referee.",
    "created_at": "2009-05-28T18:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6149#issuecomment-49088",
    "user": "@jhpalmieri"
}
```

This got refereed too quickly for me!  See #6152 for a few more fixes -- should be quick to referee.

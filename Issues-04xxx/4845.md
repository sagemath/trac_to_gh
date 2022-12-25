# Issue 4845: [with patch, positive review] sage 3.2.2 crashes on startup when init.sage present

archive/issues_004845.json:
```json
{
    "body": "Assignee: @craigcitro\n\nI think the title says it all -- sage seems to crash on start whenever the file `~/.sage/init.sage` is present, at least on my Mac. The attached patch fixes the issue.\n\nI'm listing this as a blocker, partially because the fix is so short. I think that this bug has been lurking quite a while -- I think it was the fix for #4792 that exposed it ...\n\nIssue created by migration from https://trac.sagemath.org/ticket/4845\n\n",
    "closed_at": "2008-12-21T11:58:20Z",
    "created_at": "2008-12-21T09:15:09Z",
    "labels": [
        "component: misc",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "[with patch, positive review] sage 3.2.2 crashes on startup when init.sage present",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4845",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

I think the title says it all -- sage seems to crash on start whenever the file `~/.sage/init.sage` is present, at least on my Mac. The attached patch fixes the issue.

I'm listing this as a blocker, partially because the fix is so short. I think that this bug has been lurking quite a while -- I think it was the fix for #4792 that exposed it ...

Issue created by migration from https://trac.sagemath.org/ticket/4845





---

archive/issue_comments_036665.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-21T09:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36665",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036666.json:
```json
{
    "body": "Attachment [trac-4845.patch](tarball://root/attachments/some-uuid/ticket4845/trac-4845.patch) by @craigcitro created at 2008-12-21 09:16:12",
    "created_at": "2008-12-21T09:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36666",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4845.patch](tarball://root/attachments/some-uuid/ticket4845/trac-4845.patch) by @craigcitro created at 2008-12-21 09:16:12



---

archive/issue_comments_036667.json:
```json
{
    "body": "Nice fix, \"sage -gdb\" and \"sage -valgrind\" keep working :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-21T09:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36667",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nice fix, "sage -gdb" and "sage -valgrind" keep working :)

Cheers,

Michael



---

archive/issue_comments_036668.json:
```json
{
    "body": "I have created #4846 so we are more likely to catch this issue, even though it still doesn't make it 100% fool proof without adding a doctest that starts Sage completely in non-doctest mode.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-21T09:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36668",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I have created #4846 so we are more likely to catch this issue, even though it still doesn't make it 100% fool proof without adding a doctest that starts Sage completely in non-doctest mode.

Cheers,

Michael



---

archive/issue_events_011126.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-21T11:58:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4845#event-11126"
}
```



---

archive/issue_comments_036669.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-21T11:58:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36669",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036670.json:
```json
{
    "body": "Merged in Sage 3.2.3.alpha0",
    "created_at": "2008-12-21T11:58:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36670",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.3.alpha0



---

archive/issue_comments_036671.json:
```json
{
    "body": "for future reference:\n\n```\n17:35 < wstein> I don't like the patch at 4845.\n17:35 < wstein> better would be\n17:35 < wstein> if stripped_line.startswith('#'):\n17:35 < wstein> instead of \n17:36 < wstein> if stripped_line and stripped_line[0] == '#':\n```",
    "created_at": "2008-12-24T01:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36671",
    "user": "https://github.com/williamstein"
}
```

for future reference:

```
17:35 < wstein> I don't like the patch at 4845.
17:35 < wstein> better would be
17:35 < wstein> if stripped_line.startswith('#'):
17:35 < wstein> instead of 
17:36 < wstein> if stripped_line and stripped_line[0] == '#':
```



---

archive/issue_comments_036672.json:
```json
{
    "body": "Attachment [trac-4845-v2.patch](tarball://root/attachments/some-uuid/ticket4845/trac-4845-v2.patch) by mabshoff created at 2008-12-24 04:09:54\n\nI like the cleaner v2.patch. Merged in Sage 3.2.3.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-24T04:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36672",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac-4845-v2.patch](tarball://root/attachments/some-uuid/ticket4845/trac-4845-v2.patch) by mabshoff created at 2008-12-24 04:09:54

I like the cleaner v2.patch. Merged in Sage 3.2.3.alpha0.

Cheers,

Michael



---

archive/issue_comments_036673.json:
```json
{
    "body": "I definitely prefer the v2 patch for the sake of readability. For the sake of it, though, should anyone look at this ticket, I want to note that the original patch seems (at a quick glance, anyway) to be faster:\n\n```\nsage: s = \"\"\nsage: %timeit s.startswith('3')\n1000000 loops, best of 3: 350 ns per loop\nsage: %timeit s and s[0] == '3'\n10000000 loops, best of 3: 72.2 ns per loop\n\nsage: s = \"345\"\nsage: %timeit s.startswith('3')\n1000000 loops, best of 3: 353 ns per loop\nsage: %timeit s and s[0] == '3'\n1000000 loops, best of 3: 208 ns per loop\n\nsage: s = \"678\"\nsage: %timeit s.startswith('3')\n1000000 loops, best of 3: 351 ns per loop\nsage: %timeit s and s[0] == '3'\n1000000 loops, best of 3: 212 ns per loop\n```",
    "created_at": "2008-12-24T04:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36673",
    "user": "https://github.com/craigcitro"
}
```

I definitely prefer the v2 patch for the sake of readability. For the sake of it, though, should anyone look at this ticket, I want to note that the original patch seems (at a quick glance, anyway) to be faster:

```
sage: s = ""
sage: %timeit s.startswith('3')
1000000 loops, best of 3: 350 ns per loop
sage: %timeit s and s[0] == '3'
10000000 loops, best of 3: 72.2 ns per loop

sage: s = "345"
sage: %timeit s.startswith('3')
1000000 loops, best of 3: 353 ns per loop
sage: %timeit s and s[0] == '3'
1000000 loops, best of 3: 208 ns per loop

sage: s = "678"
sage: %timeit s.startswith('3')
1000000 loops, best of 3: 351 ns per loop
sage: %timeit s and s[0] == '3'
1000000 loops, best of 3: 212 ns per loop
```

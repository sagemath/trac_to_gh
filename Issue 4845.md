# Issue 4845: [with patch, needs review] sage 3.2.2 crashes on startup when init.sage present

archive/issues_004845.json:
```json
{
    "body": "Assignee: craigcitro\n\nI think the title says it all -- sage seems to crash on start whenever the file `~/.sage/init.sage` is present, at least on my Mac. The attached patch fixes the issue.\n\nI'm listing this as a blocker, partially because the fix is so short. I think that this bug has been lurking quite a while -- I think it was the fix for #4792 that exposed it ...\n\nIssue created by migration from https://trac.sagemath.org/ticket/4845\n\n",
    "created_at": "2008-12-21T09:15:09Z",
    "labels": [
        "misc",
        "blocker",
        "bug"
    ],
    "title": "[with patch, needs review] sage 3.2.2 crashes on startup when init.sage present",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4845",
    "user": "craigcitro"
}
```
Assignee: craigcitro

I think the title says it all -- sage seems to crash on start whenever the file `~/.sage/init.sage` is present, at least on my Mac. The attached patch fixes the issue.

I'm listing this as a blocker, partially because the fix is so short. I think that this bug has been lurking quite a while -- I think it was the fix for #4792 that exposed it ...

Issue created by migration from https://trac.sagemath.org/ticket/4845





---

archive/issue_comments_036737.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-21T09:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36737",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036738.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-12-21T09:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36738",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_036739.json:
```json
{
    "body": "Nice fix, \"sage -gdb\" and \"sage -valgrind\" keep working :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-21T09:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36739",
    "user": "mabshoff"
}
```

Nice fix, "sage -gdb" and "sage -valgrind" keep working :)

Cheers,

Michael



---

archive/issue_comments_036740.json:
```json
{
    "body": "I have created #4846 so we are more likely to catch this issue, even though it still doesn't make it 100% fool proof without adding a doctest that starts Sage completely in non-doctest mode.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-21T09:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36740",
    "user": "mabshoff"
}
```

I have created #4846 so we are more likely to catch this issue, even though it still doesn't make it 100% fool proof without adding a doctest that starts Sage completely in non-doctest mode.

Cheers,

Michael



---

archive/issue_comments_036741.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-21T11:58:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36741",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036742.json:
```json
{
    "body": "Merged in Sage 3.2.3.alpha0",
    "created_at": "2008-12-21T11:58:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36742",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.3.alpha0



---

archive/issue_comments_036743.json:
```json
{
    "body": "for future reference:\n\n```\n17:35 < wstein> I don't like the patch at 4845.\n17:35 < wstein> better would be\n17:35 < wstein> if stripped_line.startswith('#'):\n17:35 < wstein> instead of \n17:36 < wstein> if stripped_line and stripped_line[0] == '#':\n```\n",
    "created_at": "2008-12-24T01:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36743",
    "user": "was"
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

archive/issue_comments_036744.json:
```json
{
    "body": "Attachment\n\nI like the cleaner v2.patch. Merged in Sage 3.2.3.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-24T04:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36744",
    "user": "mabshoff"
}
```

Attachment

I like the cleaner v2.patch. Merged in Sage 3.2.3.alpha0.

Cheers,

Michael



---

archive/issue_comments_036745.json:
```json
{
    "body": "I definitely prefer the v2 patch for the sake of readability. For the sake of it, though, should anyone look at this ticket, I want to note that the original patch seems (at a quick glance, anyway) to be faster:\n\n\n```\nsage: s = \"\"\nsage: %timeit s.startswith('3')\n1000000 loops, best of 3: 350 ns per loop\nsage: %timeit s and s[0] == '3'\n10000000 loops, best of 3: 72.2 ns per loop\n\nsage: s = \"345\"\nsage: %timeit s.startswith('3')\n1000000 loops, best of 3: 353 ns per loop\nsage: %timeit s and s[0] == '3'\n1000000 loops, best of 3: 208 ns per loop\n\nsage: s = \"678\"\nsage: %timeit s.startswith('3')\n1000000 loops, best of 3: 351 ns per loop\nsage: %timeit s and s[0] == '3'\n1000000 loops, best of 3: 212 ns per loop\n```\n",
    "created_at": "2008-12-24T04:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4845#issuecomment-36745",
    "user": "craigcitro"
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


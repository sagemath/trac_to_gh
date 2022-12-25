# Issue 2394: Wrap Cremona's newforms class

archive/issues_002394.json:
```json
{
    "body": "Assignee: boothby\n\nWrap the newforms class in eclib\n\nIssue created by migration from https://trac.sagemath.org/ticket/2394\n\n",
    "created_at": "2008-03-05T07:19:41Z",
    "labels": [
        "component: modular forms",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Wrap Cremona's newforms class",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2394",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: boothby

Wrap the newforms class in eclib

Issue created by migration from https://trac.sagemath.org/ticket/2394





---

archive/issue_events_005647.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-05T14:11:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "milestone": "sage-2.10.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2394#event-5647"
}
```



---

archive/issue_comments_016109.json:
```json
{
    "body": "Three remarks:\n\n* I am splitting the updated eclib.spkg off into its own ticket #2347\n* doctests seems to be missing\n* It would be interesting to see if this conflicts with wstein's mwrank rewrite\n\nCheers,\n\nMichael",
    "created_at": "2008-03-09T06:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2394#issuecomment-16109",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Three remarks:

* I am splitting the updated eclib.spkg off into its own ticket #2347
* doctests seems to be missing
* It would be interesting to see if this conflicts with wstein's mwrank rewrite

Cheers,

Michael



---

archive/issue_comments_016110.json:
```json
{
    "body": "I fail to see any difference to eclib-20080127.p0 in the hg log, so can somebody enlighten me what is different?\n\nCheers,\n\nMichael",
    "created_at": "2008-03-09T06:50:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2394#issuecomment-16110",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I fail to see any difference to eclib-20080127.p0 in the hg log, so can somebody enlighten me what is different?

Cheers,

Michael



---

archive/issue_comments_016111.json:
```json
{
    "body": "mabshoff is right -- this is the same as eclib-20080127.    I think boothby forgot to check in his changes?",
    "created_at": "2008-03-09T16:25:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2394#issuecomment-16111",
    "user": "https://github.com/JohnCremona"
}
```

mabshoff is right -- this is the same as eclib-20080127.    I think boothby forgot to check in his changes?



---

archive/issue_comments_016112.json:
```json
{
    "body": "Yep. Checking the repo I see:\n\n```\neclib-20080304/src$ hg status\nM g0n/Makefile\nM g0n/hecketest.cc\nM g0n/homspace.cc\nM g0n/homspace.h\nM g0n/newforms.cc\nM g0n/newforms.h\nM g0n/nftest.cc\nM procs/rat.h\n? g0n/ecnf.cc\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-03-09T16:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2394#issuecomment-16112",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yep. Checking the repo I see:

```
eclib-20080304/src$ hg status
M g0n/Makefile
M g0n/hecketest.cc
M g0n/homspace.cc
M g0n/homspace.h
M g0n/newforms.cc
M g0n/newforms.h
M g0n/nftest.cc
M procs/rat.h
? g0n/ecnf.cc
```

Cheers,

Michael



---

archive/issue_comments_016113.json:
```json
{
    "body": "I didn't change the title of this ticket for a reason!  Nothing here is ready for review.  The eclib spkg has *bad* changes, like I made some private class members public, etc.  The patch (as noted) doesn't have doctests, and doesn't work.  I put this up as a preliminary version for William to work with.  Later this week, I'll make it all kosher.",
    "created_at": "2008-03-09T22:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2394#issuecomment-16113",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

I didn't change the title of this ticket for a reason!  Nothing here is ready for review.  The eclib spkg has *bad* changes, like I made some private class members public, etc.  The patch (as noted) doesn't have doctests, and doesn't work.  I put this up as a preliminary version for William to work with.  Later this week, I'll make it all kosher.



---

archive/issue_events_005648.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2008-03-09T22:59:12Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "milestone": "sage-2.10.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2394#event-5648"
}
```



---

archive/issue_events_005649.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2008-03-09T22:59:12Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2394#event-5649"
}
```



---

archive/issue_comments_016114.json:
```json
{
    "body": "See #2437 (not 2347)",
    "created_at": "2008-03-10T00:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2394#issuecomment-16114",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

See #2437 (not 2347)



---

archive/issue_comments_016115.json:
```json
{
    "body": "Attachment [2394-newforms.patch](tarball://root/attachments/some-uuid/ticket2394/2394-newforms.patch) by boothby created at 2008-03-13 06:45:34",
    "created_at": "2008-03-13T06:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2394#issuecomment-16115",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [2394-newforms.patch](tarball://root/attachments/some-uuid/ticket2394/2394-newforms.patch) by boothby created at 2008-03-13 06:45:34



---

archive/issue_events_005650.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2008-03-13T06:46:21Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2394#event-5650"
}
```



---

archive/issue_events_005651.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2008-03-13T06:46:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2394#event-5651"
}
```



---

archive/issue_comments_016116.json:
```json
{
    "body": "patch looks good, except:\n* newly created files don't have file level documentation\n* newly created files don't have copyright statement (do they need one?)\n* Does it make sense to add doctests to `class ECModularSymbol` ?",
    "created_at": "2008-04-05T23:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2394#issuecomment-16116",
    "user": "https://github.com/malb"
}
```

patch looks good, except:
* newly created files don't have file level documentation
* newly created files don't have copyright statement (do they need one?)
* Does it make sense to add doctests to `class ECModularSymbol` ?



---

archive/issue_comments_016117.json:
```json
{
    "body": "I also think the patch looks good, though I agree with malb's points.  Also I have no experience myself in wrapping code (even my own ;)) so the fact that it looks ok to me does not count for much.\n\nSince this patch has required a little tinkering with eclib itself, I think I need to download that, compare with the latest version of my own, and check that nothing is broken...",
    "created_at": "2008-04-06T20:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2394#issuecomment-16117",
    "user": "https://github.com/JohnCremona"
}
```

I also think the patch looks good, though I agree with malb's points.  Also I have no experience myself in wrapping code (even my own ;)) so the fact that it looks ok to me does not count for much.

Since this patch has required a little tinkering with eclib itself, I think I need to download that, compare with the latest version of my own, and check that nothing is broken...



---

archive/issue_comments_016118.json:
```json
{
    "body": "Attachment [2394-license.patch](tarball://root/attachments/some-uuid/ticket2394/2394-license.patch) by boothby created at 2008-04-11 21:03:46\n\n2394-license.patch adds a copyright statement.  File-level documentation would be redundant since the file only has a single class, and the class is documented.  Also, ECModularSymbol has doctests on every function.  Should we add more?  If so, what?  Modulo any further complaints, we should add this in to avoid bitrot.",
    "created_at": "2008-04-11T21:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2394#issuecomment-16118",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [2394-license.patch](tarball://root/attachments/some-uuid/ticket2394/2394-license.patch) by boothby created at 2008-04-11 21:03:46

2394-license.patch adds a copyright statement.  File-level documentation would be redundant since the file only has a single class, and the class is documented.  Also, ECModularSymbol has doctests on every function.  Should we add more?  If so, what?  Modulo any further complaints, we should add this in to avoid bitrot.



---

archive/issue_comments_016119.json:
```json
{
    "body": "```\n[22:00] <boothby> Please look at my comments on #2394\n[22:01] <boothby> valid/invalid?\n[22:02] <malb> I'm still in favour of module level docs but that is taste I reckon\n```\n\nI say apply.",
    "created_at": "2008-04-11T21:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2394#issuecomment-16119",
    "user": "https://github.com/malb"
}
```

```
[22:00] <boothby> Please look at my comments on #2394
[22:01] <boothby> valid/invalid?
[22:02] <malb> I'm still in favour of module level docs but that is taste I reckon
```

I say apply.



---

archive/issue_events_005652.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-12T00:10:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2394#event-5652"
}
```



---

archive/issue_comments_016120.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-12T00:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2394#issuecomment-16120",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016121.json:
```json
{
    "body": "Merged both patches in Sage 3.0.alpha4",
    "created_at": "2008-04-12T00:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2394#issuecomment-16121",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.0.alpha4

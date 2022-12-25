# Issue 2435: Fix memory leak from #1337 workaround

archive/issues_002435.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @garyfurnish\n\nThe workaround for the double free in #1337 causes memory leaks if the integer pool is full\n\nIssue created by migration from https://trac.sagemath.org/ticket/2435\n\n",
    "created_at": "2008-03-09T05:32:17Z",
    "labels": [
        "component: memleak",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "Fix memory leak from #1337 workaround",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2435",
    "user": "https://github.com/robertwb"
}
```
Assignee: mabshoff

CC:  @garyfurnish

The workaround for the double free in #1337 causes memory leaks if the integer pool is full

Issue created by migration from https://trac.sagemath.org/ticket/2435





---

archive/issue_comments_016436.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2008-03-10T07:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2435#issuecomment-16436",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_016437.json:
```json
{
    "body": "This actually causes massive memory leaks. I tried enlarging the mempool to 1024*1024 elements, but that seems like a rather crude band aid any may have performance implications.\n\nRobert - can you have a look if you can fix this?\n\nCheers,\n\nMichael",
    "created_at": "2008-03-10T07:01:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2435#issuecomment-16437",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This actually causes massive memory leaks. I tried enlarging the mempool to 1024*1024 elements, but that seems like a rather crude band aid any may have performance implications.

Robert - can you have a look if you can fix this?

Cheers,

Michael



---

archive/issue_comments_016438.json:
```json
{
    "body": "I should have some time to look at this tonight. I you were busy working on 1337 and wanted to jump in but had a pile of things I couldn't put off this weekend. \n\nCould one or both of you post a comment here bringing things up to date with what you figured out with #1337, I've read the patch but have to admit it's not very informative on what exactly is going on. \n\nIn justification of the integer pool--the main performance gain is because integers are ephemeral objects, so even a pool of 100 integers is a huge gain as most of the time you have new/delete/new/delete/new/delete...",
    "created_at": "2008-03-10T17:51:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2435#issuecomment-16438",
    "user": "https://github.com/robertwb"
}
```

I should have some time to look at this tonight. I you were busy working on 1337 and wanted to jump in but had a pile of things I couldn't put off this weekend. 

Could one or both of you post a comment here bringing things up to date with what you figured out with #1337, I've read the patch but have to admit it's not very informative on what exactly is going on. 

In justification of the integer pool--the main performance gain is because integers are ephemeral objects, so even a pool of 100 integers is a huge gain as most of the time you have new/delete/new/delete/new/delete...



---

archive/issue_events_005746.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-11T01:14:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2435",
    "milestone": "sage-2.10.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2435#event-5746"
}
```



---

archive/issue_comments_016439.json:
```json
{
    "body": "Line 3209 of integer.pyx\n\n```\nONE = Integer(1)\n```\n\nIt has refcount 2 when one quits. It gets overwritten in two dictionaries one dictionary, then two separate dictionaries that refer to it get deleted. \n\nAny easy fix is to cdef it or incref it, but that isn't what the real problem is.",
    "created_at": "2008-03-11T10:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2435#issuecomment-16439",
    "user": "https://github.com/robertwb"
}
```

Line 3209 of integer.pyx

```
ONE = Integer(1)
```

It has refcount 2 when one quits. It gets overwritten in two dictionaries one dictionary, then two separate dictionaries that refer to it get deleted. 

Any easy fix is to cdef it or incref it, but that isn't what the real problem is.



---

archive/issue_comments_016440.json:
```json
{
    "body": "OK, this is due to some voodoo that Python does trying to clean up after itself. `_PyImport_Fini` gets called twice at the end, which tried to deallocate the (copy of) the module's dictionary. Somehow, after the first deallocation, it is still hanging around for a second round of deallocation. But the integer `ONE` does not have a high enough refcount (after all, it's only in two dictionaries) to be deallocated 3 times. \n\nI suspect we're running into this problem here because of some circular import issue that prevents it from being completely cleaned up the first time around.",
    "created_at": "2008-03-11T11:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2435#issuecomment-16440",
    "user": "https://github.com/robertwb"
}
```

OK, this is due to some voodoo that Python does trying to clean up after itself. `_PyImport_Fini` gets called twice at the end, which tried to deallocate the (copy of) the module's dictionary. Somehow, after the first deallocation, it is still hanging around for a second round of deallocation. But the integer `ONE` does not have a high enough refcount (after all, it's only in two dictionaries) to be deallocated 3 times. 

I suspect we're running into this problem here because of some circular import issue that prevents it from being completely cleaned up the first time around.



---

archive/issue_comments_016441.json:
```json
{
    "body": "Here is a fix--it doesn't crash any more for me (filling up the pool, whatever) or leak memory. \n\nInterestingly enough, David Roe increfs `ONE` in his `_val_unit` function (integer.pyx:1749) for no apparent reason. Hmm...",
    "created_at": "2008-03-11T11:32:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2435#issuecomment-16441",
    "user": "https://github.com/robertwb"
}
```

Here is a fix--it doesn't crash any more for me (filling up the pool, whatever) or leak memory. 

Interestingly enough, David Roe increfs `ONE` in his `_val_unit` function (integer.pyx:1749) for no apparent reason. Hmm...



---

archive/issue_events_005747.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-03-11T15:41:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2435",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2435#event-5747"
}
```



---

archive/issue_comments_016442.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-11T15:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2435#issuecomment-16442",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_016443.json:
```json
{
    "body": "Attachment [2435-integer-fix.patch](tarball://root/attachments/some-uuid/ticket2435/2435-integer-fix.patch) by @williamstein created at 2008-03-11 15:41:39",
    "created_at": "2008-03-11T15:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2435#issuecomment-16443",
    "user": "https://github.com/williamstein"
}
```

Attachment [2435-integer-fix.patch](tarball://root/attachments/some-uuid/ticket2435/2435-integer-fix.patch) by @williamstein created at 2008-03-11 15:41:39



---

archive/issue_comments_016444.json:
```json
{
    "body": "Nice catch Robert. Looking at the patch I can only say \"D'oh\" since it is so obvious. But hindsight is always 20/20 - congratulations nonetheless.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-11T19:27:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2435#issuecomment-16444",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nice catch Robert. Looking at the patch I can only say "D'oh" since it is so obvious. But hindsight is always 20/20 - congratulations nonetheless.

Cheers,

Michael



---

archive/issue_comments_016445.json:
```json
{
    "body": "Merged in Sage 2.10.3.final",
    "created_at": "2008-03-11T20:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2435#issuecomment-16445",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.final



---

archive/issue_comments_016446.json:
```json
{
    "body": "Some more info: the extra Py_INCREF is not needed if `ONE` is created after the dummy integer (even if it's before the fast `tp_*` functions are hooked in).",
    "created_at": "2008-03-12T00:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2435#issuecomment-16446",
    "user": "https://github.com/robertwb"
}
```

Some more info: the extra Py_INCREF is not needed if `ONE` is created after the dummy integer (even if it's before the fast `tp_*` functions are hooked in).

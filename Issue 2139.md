# Issue 2139: set partitions iterator not working

archive/issues_002139.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nHello,\n\nI'm doing some work with complete matchings, and I'm dealing with them\nas set partitions. I just need to iterate over matchings, not make\nlists, so it seems like I shouldn't run out of memory (I have 1.5 gigs\ninstalled), but I am. I'm using Sage 2.10.1 on Linux.\n\nIf I do something like the following, memory usage climbs and climbs:\n\n n = 0\n for m in SetPartitions(range(16), [2, 2, 2, 2, 2, 2, 2, 2]):\n   n += 1\n\nThis seems weird, since there's a set partitions iterator, and it\nshouldn't take a lot of memory.\n\nOn the other hand, here's an iterator for complete matchings that I\nwrote that works just fine:\n\n def matchings(n):\n   for m in matchingsset(range(1, n+1)): yield m\n\n def matchingsset(L):\n   if len(L) == 0:\n     yield []\n   else:\n     for k in range(1,len(L)):\n       for m in matchingsset(L[1:k] + L[k+1:]):\n         yield m + [[L[0], L[k]]]\n   return\n\nNow running the same counting loop works, with no extra memory usage:\n\n n = 0\n for m in matchings(16):\n   n += 1\n\nSage seems to have an iterator for set partitions; it is working? Do I\nneed to use something else to get a memory-efficient iterator?\n\nThanks for the help,\n\nDan\n\nIssue created by migration from https://trac.sagemath.org/ticket/2139\n\n",
    "created_at": "2008-02-11T06:39:11Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "set partitions iterator not working",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2139",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @mwhansen

CC:  sage-combinat

Hello,

I'm doing some work with complete matchings, and I'm dealing with them
as set partitions. I just need to iterate over matchings, not make
lists, so it seems like I shouldn't run out of memory (I have 1.5 gigs
installed), but I am. I'm using Sage 2.10.1 on Linux.

If I do something like the following, memory usage climbs and climbs:

 n = 0
 for m in SetPartitions(range(16), [2, 2, 2, 2, 2, 2, 2, 2]):
   n += 1

This seems weird, since there's a set partitions iterator, and it
shouldn't take a lot of memory.

On the other hand, here's an iterator for complete matchings that I
wrote that works just fine:

 def matchings(n):
   for m in matchingsset(range(1, n+1)): yield m

 def matchingsset(L):
   if len(L) == 0:
     yield []
   else:
     for k in range(1,len(L)):
       for m in matchingsset(L[1:k] + L[k+1:]):
         yield m + [[L[0], L[k]]]
   return

Now running the same counting loop works, with no extra memory usage:

 n = 0
 for m in matchings(16):
   n += 1

Sage seems to have an iterator for set partitions; it is working? Do I
need to use something else to get a memory-efficient iterator?

Thanks for the help,

Dan

Issue created by migration from https://trac.sagemath.org/ticket/2139





---

archive/issue_comments_013993.json:
```json
{
    "body": "Attachment [set_partition.patch](tarball://root/attachments/some-uuid/ticket2139/set_partition.patch) by @mwhansen created at 2008-02-11 06:40:56",
    "created_at": "2008-02-11T06:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2139#issuecomment-13993",
    "user": "https://github.com/mwhansen"
}
```

Attachment [set_partition.patch](tarball://root/attachments/some-uuid/ticket2139/set_partition.patch) by @mwhansen created at 2008-02-11 06:40:56



---

archive/issue_comments_013994.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-11T06:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2139#issuecomment-13994",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013995.json:
```json
{
    "body": "Again, I say apply.  Again, there are no doctests!",
    "created_at": "2008-02-15T03:45:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2139#issuecomment-13995",
    "user": "https://github.com/ncalexan"
}
```

Again, I say apply.  Again, there are no doctests!



---

archive/issue_comments_013996.json:
```json
{
    "body": "I don't know the best way to doctest memory usage, but this is a \"reimplementation\" of something that already has doctests.  So, it's already being doctested for correctness, just not memory consumption.",
    "created_at": "2008-02-15T03:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2139#issuecomment-13996",
    "user": "https://github.com/mwhansen"
}
```

I don't know the best way to doctest memory usage, but this is a "reimplementation" of something that already has doctests.  So, it's already being doctested for correctness, just not memory consumption.



---

archive/issue_comments_013997.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-15T04:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2139#issuecomment-13997",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013998.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-15T04:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2139#issuecomment-13998",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha0



---

archive/issue_events_002301.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-15T04:57:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2139",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2139#event-2301"
}
```

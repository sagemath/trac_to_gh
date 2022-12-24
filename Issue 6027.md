# Issue 6027: get_memory_usage() sucks performance wise on OSX

archive/issues_006027.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  rdingman\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: timeit('get_memory_usage()')\n5 loops, best of 3: 486 ms per loop\n```\n\nThis causes sage/rings/tests.py to take forever in -long doctesting mode.\n| Sage Version 3.4.2, Release Date: 2009-05-04                       |\n| Type notebook() for the GUI, and license() for information.        |\nSee http://blog.kuriositaet.de/?p=257 for a more efficient way to get the current memory used.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/6027\n\n",
    "created_at": "2009-05-12T07:13:49Z",
    "labels": [
        "porting",
        "critical",
        "bug"
    ],
    "title": "get_memory_usage() sucks performance wise on OSX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6027",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  rdingman


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: timeit('get_memory_usage()')
5 loops, best of 3: 486 ms per loop
```

This causes sage/rings/tests.py to take forever in -long doctesting mode.
| Sage Version 3.4.2, Release Date: 2009-05-04                       |
| Type notebook() for the GUI, and license() for information.        |
See http://blog.kuriositaet.de/?p=257 for a more efficient way to get the current memory used.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/6027





---

archive/issue_comments_047989.json:
```json
{
    "body": "Attachment [trac_6027_get_memory_usage_darwin.patch](tarball://root/attachments/some-uuid/ticket6027/trac_6027_get_memory_usage_darwin.patch) by rdingman created at 2009-05-22 18:15:04\n\nI've added a patch to get the memory usage of Sage on Darwin without spawning top and parsing the output. With this patch, get_memory_usage() will still report the same result that top reports for VSIZE (the link above doesn't do this).\n\nBefore patch:\n\nsage: timeit('get_memory_usage()')\n5 loops, best of 3: 156 ms per loop\n\nAfter patch:\n\nsage: timeit('get_memory_usage()')\n125 loops, best of 3: 2.62 ms per loop\n\nThis has only been tested on OS X 10.5, Intel, 64-bit. It will likely work for PPC and 32-bit (still 10.5), but I'm not sure about 10.4 and earlier. I don't have access to hardware right now to test (and fix) this patch on all these other configurations. I'd be happy to finish up this patch if someone has machines to test on.",
    "created_at": "2009-05-22T18:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6027#issuecomment-47989",
    "user": "rdingman"
}
```

Attachment [trac_6027_get_memory_usage_darwin.patch](tarball://root/attachments/some-uuid/ticket6027/trac_6027_get_memory_usage_darwin.patch) by rdingman created at 2009-05-22 18:15:04

I've added a patch to get the memory usage of Sage on Darwin without spawning top and parsing the output. With this patch, get_memory_usage() will still report the same result that top reports for VSIZE (the link above doesn't do this).

Before patch:

sage: timeit('get_memory_usage()')
5 loops, best of 3: 156 ms per loop

After patch:

sage: timeit('get_memory_usage()')
125 loops, best of 3: 2.62 ms per loop

This has only been tested on OS X 10.5, Intel, 64-bit. It will likely work for PPC and 32-bit (still 10.5), but I'm not sure about 10.4 and earlier. I don't have access to hardware right now to test (and fix) this patch on all these other configurations. I'd be happy to finish up this patch if someone has machines to test on.



---

archive/issue_comments_047990.json:
```json
{
    "body": "Also, for other platforms calling the underlying darwin_memory_usage() will just raise NotImplementeError. I also have not tested this patch on non-darwin to make sure the c code conditionally compiles correctly and that the behavior is reasonable.",
    "created_at": "2009-05-22T18:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6027#issuecomment-47990",
    "user": "rdingman"
}
```

Also, for other platforms calling the underlying darwin_memory_usage() will just raise NotImplementeError. I also have not tested this patch on non-darwin to make sure the c code conditionally compiles correctly and that the behavior is reasonable.



---

archive/issue_comments_047991.json:
```json
{
    "body": "I have no doubt it will compile, so mark it for \"needs review\". Otherwise no one will look at this any time soon since those tickets tend to stay rotten in trac ;)\n\nOnce I have made it home I will look at this. I have some analog code for Solaris more or less ready to go and will extend this code as needed then.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-22T18:20:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6027#issuecomment-47991",
    "user": "mabshoff"
}
```

I have no doubt it will compile, so mark it for "needs review". Otherwise no one will look at this any time soon since those tickets tend to stay rotten in trac ;)

Once I have made it home I will look at this. I have some analog code for Solaris more or less ready to go and will extend this code as needed then.

Cheers,

Michael



---

archive/issue_comments_047992.json:
```json
{
    "body": "This isn't critical for 4.0.  This would be very nice to get into 4.0.1.",
    "created_at": "2009-05-28T06:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6027#issuecomment-47992",
    "user": "was"
}
```

This isn't critical for 4.0.  This would be very nice to get into 4.0.1.



---

archive/issue_comments_047993.json:
```json
{
    "body": "Applies clean, tested fine on sage.math.  After patch on OS X 10.5:\n\n\n```\nsage: sage.misc.getusage.get_memory_usage()\n141.22265625\nsage: %timeit sage.misc.getusage.get_memory_usage()\n100 loops, best of 3: 5.24 ms per loop\nsage: sage.misc.darwin_utilities\nsage.misc.darwin_utilities\nsage: sage.misc.darwin_utilities.darwin_memory_usage()\n148082688L\nsage: %timeit sage.misc.darwin_utilities.darwin_memory_usage()\n100 loops, best of 3: 5.22 ms per loop\n```\n",
    "created_at": "2009-06-15T19:17:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6027#issuecomment-47993",
    "user": "ncalexan"
}
```

Applies clean, tested fine on sage.math.  After patch on OS X 10.5:


```
sage: sage.misc.getusage.get_memory_usage()
141.22265625
sage: %timeit sage.misc.getusage.get_memory_usage()
100 loops, best of 3: 5.24 ms per loop
sage: sage.misc.darwin_utilities
sage.misc.darwin_utilities
sage: sage.misc.darwin_utilities.darwin_memory_usage()
148082688L
sage: %timeit sage.misc.darwin_utilities.darwin_memory_usage()
100 loops, best of 3: 5.22 ms per loop
```




---

archive/issue_comments_047994.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T09:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6027#issuecomment-47994",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_047995.json:
```json
{
    "body": "Attachment [trac_6027-osx104.patch](tarball://root/attachments/some-uuid/ticket6027/trac_6027-osx104.patch) by rlm created at 2009-06-25 17:13:53\n\nPositive review on William's additional patch, which is merged in sage-4.1.alpha1.",
    "created_at": "2009-06-25T17:13:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6027#issuecomment-47995",
    "user": "rlm"
}
```

Attachment [trac_6027-osx104.patch](tarball://root/attachments/some-uuid/ticket6027/trac_6027-osx104.patch) by rlm created at 2009-06-25 17:13:53

Positive review on William's additional patch, which is merged in sage-4.1.alpha1.



---

archive/issue_comments_047996.json:
```json
{
    "body": "If someone has machines with OSX <= 10.4 that I can access I could port the code I wrote.",
    "created_at": "2009-06-25T18:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6027#issuecomment-47996",
    "user": "rdingman"
}
```

If someone has machines with OSX <= 10.4 that I can access I could port the code I wrote.

# Issue 3150: Memory leak in combinat/matrices/dancing_links.pyx

archive/issues_003150.json:
```json
{
    "body": "Assignee: carlohamalainen\n\nCC:  sage-combinat\n\nThe wrapper for the C++ class dancing_links in dancing_links.pyx does not deallocate all memory resulting in a leak.\n\n\nRunning valgrind on dlxcpp.py:\n\n\n```\n==23234== LEAK SUMMARY:\n==23234==    definitely lost: 64 bytes in 2 blocks.\n==23234==    indirectly lost: 368 bytes in 12 blocks.\n==23234==      possibly lost: 201,979 bytes in 708 blocks.\n==23234==    still reachable: 28,370,716 bytes in 19,122 blocks.\n==23234==         suppressed: 0 bytes in 0 blocks.\n```\n\n\nAfter applying the patch:\n\n\n```\n==26826== LEAK SUMMARY:\n==26826==    definitely lost: 0 bytes in 0 blocks.\n==26826==      possibly lost: 202,323 bytes in 709 blocks.\n==26826==    still reachable: 28,370,372 bytes in 19,121 blocks.\n==26826==         suppressed: 0 bytes in 0 blocks.\n```\n\n\nAs another test I ran the following Sage program and watched the memory usage in top. Before the memory usage of the python process would grow rapidly, with the patch it seems to stabilise quickly (about 10% memory on my 2Gb laptop).\n\n\n```\nfrom sage.combinat.matrices.dancing_links import dlx_solver\n\nrows = [[0,1,2]]\nrows+= [[0,2]]\nrows+= [[1]]\nrows+= [[3]]\n\nfor _ in range(10000000):\n    x = sage.combinat.matrices.dancing_links.dlx_solver(rows) \n    x.search()\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3150\n\n",
    "created_at": "2008-05-10T19:10:02Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "Memory leak in combinat/matrices/dancing_links.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3150",
    "user": "https://trac.sagemath.org/admin/accounts/users/carlohamalainen"
}
```
Assignee: carlohamalainen

CC:  sage-combinat

The wrapper for the C++ class dancing_links in dancing_links.pyx does not deallocate all memory resulting in a leak.


Running valgrind on dlxcpp.py:


```
==23234== LEAK SUMMARY:
==23234==    definitely lost: 64 bytes in 2 blocks.
==23234==    indirectly lost: 368 bytes in 12 blocks.
==23234==      possibly lost: 201,979 bytes in 708 blocks.
==23234==    still reachable: 28,370,716 bytes in 19,122 blocks.
==23234==         suppressed: 0 bytes in 0 blocks.
```


After applying the patch:


```
==26826== LEAK SUMMARY:
==26826==    definitely lost: 0 bytes in 0 blocks.
==26826==      possibly lost: 202,323 bytes in 709 blocks.
==26826==    still reachable: 28,370,372 bytes in 19,121 blocks.
==26826==         suppressed: 0 bytes in 0 blocks.
```


As another test I ran the following Sage program and watched the memory usage in top. Before the memory usage of the python process would grow rapidly, with the patch it seems to stabilise quickly (about 10% memory on my 2Gb laptop).


```
from sage.combinat.matrices.dancing_links import dlx_solver

rows = [[0,1,2]]
rows+= [[0,2]]
rows+= [[1]]
rows+= [[3]]

for _ in range(10000000):
    x = sage.combinat.matrices.dancing_links.dlx_solver(rows) 
    x.search()
```



Issue created by migration from https://trac.sagemath.org/ticket/3150





---

archive/issue_comments_021802.json:
```json
{
    "body": "Attachment [dlxmem.patch](tarball://root/attachments/some-uuid/ticket3150/dlxmem.patch) by mabshoff created at 2008-05-10 21:09:39",
    "created_at": "2008-05-10T21:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3150#issuecomment-21802",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [dlxmem.patch](tarball://root/attachments/some-uuid/ticket3150/dlxmem.patch) by mabshoff created at 2008-05-10 21:09:39



---

archive/issue_comments_021803.json:
```json
{
    "body": "I haven't done doctests with this patch, but I'm familiar with this file, and it looks right. Tom Boothby should probably confirm.",
    "created_at": "2008-05-10T21:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3150#issuecomment-21803",
    "user": "https://github.com/rlmill"
}
```

I haven't done doctests with this patch, but I'm familiar with this file, and it looks right. Tom Boothby should probably confirm.



---

archive/issue_comments_021804.json:
```json
{
    "body": "The patch is good and valgrinds clean to me. I am doctesting with only that patch applied to make sure everything still works, so if nothing pops up it will be merged :)\n\nCheers,\n\nMichael",
    "created_at": "2008-05-11T10:30:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3150#issuecomment-21804",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch is good and valgrinds clean to me. I am doctesting with only that patch applied to make sure everything still works, so if nothing pops up it will be merged :)

Cheers,

Michael



---

archive/issue_comments_021805.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-11T10:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3150#issuecomment-21805",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021806.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-11T10:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3150#issuecomment-21806",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha0



---

archive/issue_events_003366.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-05-11T10:44:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3150",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3150#event-3366"
}
```

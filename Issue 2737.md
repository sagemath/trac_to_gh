# Issue 2737: add balanced_sum to Sage

archive/issues_002737.json:
```json
{
    "body": "Assignee: somebody\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2737\n\n",
    "created_at": "2008-03-31T11:49:00Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "add balanced_sum to Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2737",
    "user": "https://github.com/mwhansen"
}
```
Assignee: somebody



Issue created by migration from https://trac.sagemath.org/ticket/2737





---

archive/issue_comments_018779.json:
```json
{
    "body": "Attachment [2737.patch](tarball://root/attachments/some-uuid/ticket2737/2737.patch) by @mwhansen created at 2008-03-31 11:50:03",
    "created_at": "2008-03-31T11:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2737#issuecomment-18779",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2737.patch](tarball://root/attachments/some-uuid/ticket2737/2737.patch) by @mwhansen created at 2008-03-31 11:50:03



---

archive/issue_comments_018780.json:
```json
{
    "body": "I've added my initial patch.  There is **major** code duplication through.",
    "created_at": "2008-03-31T11:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2737#issuecomment-18780",
    "user": "https://github.com/mwhansen"
}
```

I've added my initial patch.  There is **major** code duplication through.



---

archive/issue_comments_018781.json:
```json
{
    "body": "Can you post some timings? For most types summation won't be helped by balancing it (compared to say multiplication) because the basic algorithm is already linear. Unless there are non-trivial improvements, I don't think it's worth the code duplication.",
    "created_at": "2008-03-31T16:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2737#issuecomment-18781",
    "user": "https://github.com/robertwb"
}
```

Can you post some timings? For most types summation won't be helped by balancing it (compared to say multiplication) because the basic algorithm is already linear. Unless there are non-trivial improvements, I don't think it's worth the code duplication.



---

archive/issue_comments_018782.json:
```json
{
    "body": "I don't know of any good benchmarks (since I don't have any personal interest in this).  However, this is from Joel:\n\n```\n\nAbout a month ago, I mailed sage-devel with a related issue:\n\nsage: N=1000\nsage: R.<x,y>=QQ[]\nsage: L2=[x^i for i in range(N)]\nsage: sum(L2)\n...\n\nThe above sum behaves quadratically since it appears that singular goes\nthrough it's whole list of monomials when it adds a single monomial.  This\nwas much improved by a divide and conquer sum approach.  I didn't bother to\nwrite the generic function though.\n\nI'm just noting that if you've written the generic code, I think it should be\nincluded because there are some types for which the small additions are\nexpensive.  Whether or not this should replace 'sum' in the sage global\nnamespace, I'm not so certain.\n```",
    "created_at": "2008-03-31T16:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2737#issuecomment-18782",
    "user": "https://github.com/mwhansen"
}
```

I don't know of any good benchmarks (since I don't have any personal interest in this).  However, this is from Joel:

```

About a month ago, I mailed sage-devel with a related issue:

sage: N=1000
sage: R.<x,y>=QQ[]
sage: L2=[x^i for i in range(N)]
sage: sum(L2)
...

The above sum behaves quadratically since it appears that singular goes
through it's whole list of monomials when it adds a single monomial.  This
was much improved by a divide and conquer sum approach.  I didn't bother to
write the generic function though.

I'm just noting that if you've written the generic code, I think it should be
included because there are some types for which the small additions are
expensive.  Whether or not this should replace 'sum' in the sage global
namespace, I'm not so certain.
```



---

archive/issue_comments_018783.json:
```json
{
    "body": "I fixed a bug, added some documentation, and rebased the patch to 4.1.  I think my changes are minor enough that I can still review the patch.  Positive review.\n\nMike is right, though.  There is some major code duplication that eventually should be factored out.",
    "created_at": "2009-07-19T05:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2737#issuecomment-18783",
    "user": "https://github.com/jasongrout"
}
```

I fixed a bug, added some documentation, and rebased the patch to 4.1.  I think my changes are minor enough that I can still review the patch.  Positive review.

Mike is right, though.  There is some major code duplication that eventually should be factored out.



---

archive/issue_comments_018784.json:
```json
{
    "body": "Some timing info for the tour, comparing balanced sum with the builtin sum.\n\n```\nsage: a=range(10e6)          \nsage: %timeit sum(a)         \n10 loops, best of 3: 2.58 s per loop\nsage: %timeit balanced_sum(a)\n10 loops, best of 3: 891 ms per loop\nsage: balanced_sum(a)==sum(a)\nTrue\n```",
    "created_at": "2009-07-19T05:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2737#issuecomment-18784",
    "user": "https://github.com/jasongrout"
}
```

Some timing info for the tour, comparing balanced sum with the builtin sum.

```
sage: a=range(10e6)          
sage: %timeit sum(a)         
10 loops, best of 3: 2.58 s per loop
sage: %timeit balanced_sum(a)
10 loops, best of 3: 891 ms per loop
sage: balanced_sum(a)==sum(a)
True
```



---

archive/issue_comments_018785.json:
```json
{
    "body": "A more drastic example:\n\n```\nsage: a=[[i] for i in range(10e4)]                    \nsage: %time b=sum(a,[])                                       \nCPU times: user 209.95 s, sys: 0.57 s, total: 210.51 s\nWall time: 245.69 s\nsage: a==[[i] for i in range(10e4)]  \nTrue\nsage: b==range(10e4)                 \nTrue\nsage: %time c=balanced_sum(a, [])\nCPU times: user 0.11 s, sys: 0.00 s, total: 0.11 s\nWall time: 0.12 s\nsage: a==[[i] for i in range(10e4)]\nTrue\nsage: c==range(10e4)               \nTrue\n```\n\nHowever, I also uncovered a bug because the function does not copy its arguments (it modified the lists it was using, giving an incorrect sum).  I'm posting a revised patch.  This revised patch should be reviewed.",
    "created_at": "2009-07-19T06:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2737#issuecomment-18785",
    "user": "https://github.com/jasongrout"
}
```

A more drastic example:

```
sage: a=[[i] for i in range(10e4)]                    
sage: %time b=sum(a,[])                                       
CPU times: user 209.95 s, sys: 0.57 s, total: 210.51 s
Wall time: 245.69 s
sage: a==[[i] for i in range(10e4)]  
True
sage: b==range(10e4)                 
True
sage: %time c=balanced_sum(a, [])
CPU times: user 0.11 s, sys: 0.00 s, total: 0.11 s
Wall time: 0.12 s
sage: a==[[i] for i in range(10e4)]
True
sage: c==range(10e4)               
True
```

However, I also uncovered a bug because the function does not copy its arguments (it modified the lists it was using, giving an incorrect sum).  I'm posting a revised patch.  This revised patch should be reviewed.



---

archive/issue_comments_018786.json:
```json
{
    "body": "Apply just the trac-2737-balancedsum-rebased-bug-fixed.patch patch.",
    "created_at": "2009-07-19T06:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2737#issuecomment-18786",
    "user": "https://github.com/jasongrout"
}
```

Apply just the trac-2737-balancedsum-rebased-bug-fixed.patch patch.



---

archive/issue_comments_018787.json:
```json
{
    "body": "apply instead of previous patch",
    "created_at": "2009-07-19T06:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2737#issuecomment-18787",
    "user": "https://github.com/jasongrout"
}
```

apply instead of previous patch



---

archive/issue_comments_018788.json:
```json
{
    "body": "Attachment [trac-2737-balancedsum-rebased-bug-fixed.patch](tarball://root/attachments/some-uuid/ticket2737/trac-2737-balancedsum-rebased-bug-fixed.patch) by @robertwb created at 2009-07-25 22:56:59\n\nPositive review to the second patch. I don't see an easy way to get rid of code duplication, so I think this is worth it.",
    "created_at": "2009-07-25T22:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2737#issuecomment-18788",
    "user": "https://github.com/robertwb"
}
```

Attachment [trac-2737-balancedsum-rebased-bug-fixed.patch](tarball://root/attachments/some-uuid/ticket2737/trac-2737-balancedsum-rebased-bug-fixed.patch) by @robertwb created at 2009-07-25 22:56:59

Positive review to the second patch. I don't see an easy way to get rid of code duplication, so I think this is worth it.



---

archive/issue_events_006365.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-25T23:28:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2737",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2737#event-6365"
}
```



---

archive/issue_comments_018789.json:
```json
{
    "body": "Merged `trac-2737-balancedsum-rebased-bug-fixed.patch`.",
    "created_at": "2009-07-25T23:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2737#issuecomment-18789",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged `trac-2737-balancedsum-rebased-bug-fixed.patch`.



---

archive/issue_comments_018790.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-25T23:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2737#issuecomment-18790",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_018791.json:
```json
{
    "body": "Replying to [comment:6 jason]:\n> Some timing info for the tour, comparing balanced sum with the builtin sum.\n> \n\n{{{\nsage: a=range(10e6)          \nsage: %timeit sum(a)         \n10 loops, best of 3: 2.58 s per loop\nsage: %timeit balanced_sum(a)\n10 loops, best of 3: 891 ms per loop\nsage: balanced_sum(a)==sum(a)\nTrue\n}}}\nThis is what I get on sage.math:\n\n```\nsage: L = range(10e6)\nsage: %time sum(L);\nCPU times: user 0.51 s, sys: 0.00 s, total: 0.51 s\nWall time: 0.51 s\nsage: %time balanced_sum(L);\nCPU times: user 0.78 s, sys: 0.00 s, total: 0.78 s\nWall time: 0.79 s\nsage: %timeit sum(L);\n10 loops, best of 3: 504 ms per loop\nsage: %timeit balanced_sum(L);\n10 loops, best of 3: 753 ms per loop\n```\nLooks like `balanced_sum()` is worse off than the built-in `sum()` for this particular example.",
    "created_at": "2009-08-20T05:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2737#issuecomment-18791",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:6 jason]:
> Some timing info for the tour, comparing balanced sum with the builtin sum.
> 

{{{
sage: a=range(10e6)          
sage: %timeit sum(a)         
10 loops, best of 3: 2.58 s per loop
sage: %timeit balanced_sum(a)
10 loops, best of 3: 891 ms per loop
sage: balanced_sum(a)==sum(a)
True
}}}
This is what I get on sage.math:

```
sage: L = range(10e6)
sage: %time sum(L);
CPU times: user 0.51 s, sys: 0.00 s, total: 0.51 s
Wall time: 0.51 s
sage: %time balanced_sum(L);
CPU times: user 0.78 s, sys: 0.00 s, total: 0.78 s
Wall time: 0.79 s
sage: %timeit sum(L);
10 loops, best of 3: 504 ms per loop
sage: %timeit balanced_sum(L);
10 loops, best of 3: 753 ms per loop
```
Looks like `balanced_sum()` is worse off than the built-in `sum()` for this particular example.



---

archive/issue_comments_018792.json:
```json
{
    "body": "So I guess my computer is slow.  The builtin sum is *fast*.  However, when it costs a fixed high cost to add two elements together (like the lists above), I think the balanced sum is a clear, clear winner.  The list example above should show great improvement, even on sage.math.",
    "created_at": "2009-08-20T06:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2737#issuecomment-18792",
    "user": "https://github.com/jasongrout"
}
```

So I guess my computer is slow.  The builtin sum is *fast*.  However, when it costs a fixed high cost to add two elements together (like the lists above), I think the balanced sum is a clear, clear winner.  The list example above should show great improvement, even on sage.math.

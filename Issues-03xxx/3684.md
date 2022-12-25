# Issue 3684: linear algebra -- optimize computation of kernel for matrices over GF(2)

archive/issues_003684.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\n\n\nOn Sat, Jul 19, 2008 at 11:49 PM, Simon King <king@mathematik.uni-jena.de> wrote:\n>\n> Dear Sage team,\n>\n> I don't know whether this post should better go to sage-devel or sage-\n> support.\n>\n> I understood that recently the implementation of matrices over GF(2)\n> was considerably improved. Therefore i am very surprised that the\n> computation of the (left) kernel is still very slow:\n>\n> sage: version()\n> 'SAGE Version 3.0.5, Release Date: 2008-07-11'\n> sage: M=MatrixSpace(GF(2),1000,500).random_element()\n> sage: time K=M.kernel()\n> CPU times: user 21.60 s, sys: 0.06 s, total: 21.66 s\n> Wall time: 40.87 s\n> sage: time K.matrix()\n> CPU times: user 15.06 s, sys: 0.03 s, total: 15.09 s\n> Wall time: 27.71 s\n> 500 x 1000 dense matrix over Finite Field of size 2\n>\n>\n> Version 2.2.3 of C-MeatAxe (for which i have a wrapper) does much\n> better:\n>\n> sage: m=MTX(2,[M[i].list() for i in range(1000)]) # Now, m is \"the\n> same\" as M\n> sage: time k=m.nullspace()\n> CPU times: user 0.18 s, sys: 0.00 s, total: 0.18 s\n> Wall time: 0.18 s\n> sage: time k\n> CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\n> Wall time: 0.00 s\n> (500 x 1000) MTX matrix over GF(2)\n>\n> Hence, we have an improvement from 21.60+15.06 CPU-seconds to 0.18\n> seconds.\n> And the result is right:\n> sage: K.matrix()*M == 0\n> True\n> sage: k*m == MTX(2,500,500)   # this is a zero-matrix\n> True\n>\n> Did i do something wrong? Is M.kernel() not what i should use here? Or\n> is the kernel computation not optimised yet?\n\nComputation of the kernel is done in two steps in Sage:\n\n1. Compute the reduced row echelon form of the matrix.\n2. Read off the kernel.\n3. Create the kernel as a vector space.\n\nIn theory 1 takes most of the time and 2-3 are trivial.\nIn this particular case Sage is using 100% slow generic\ncode (over any base ring, etc.) to do 2-3, but superfast\ncode for 1:\n\nsage: M=MatrixSpace(GF(2),1000,500).random_element()\nsage: time E=M.echelon_form()\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\nsage: time K=M.kernel()\nCPU times: user 13.02 s, sys: 0.82 s, total: 13.84 s\nWall time: 14.54 s\n\nWriting a version of the generic code that is optimized\nfor gf2 mr4i matrices would make it so the second step\nabove would take 0.00 seconds.  Really it would \nprobably take about 10 ms, since\n\nsage: M=MatrixSpace(GF(2),1000,500).random_element()\nsage: timeit('M[0,0]=0; M.echelon_form()')\n125 loops, best of 3: 3.46 ms per loop\n\nSo with proper optimization Sage should be at least an order\nof magnitude than your meataxe benchmarks above. \n\n -- William\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3684\n\n",
    "closed_at": "2009-12-19T21:32:46Z",
    "created_at": "2008-07-20T11:45:22Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "linear algebra -- optimize computation of kernel for matrices over GF(2)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3684",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```


On Sat, Jul 19, 2008 at 11:49 PM, Simon King <king@mathematik.uni-jena.de> wrote:
>
> Dear Sage team,
>
> I don't know whether this post should better go to sage-devel or sage-
> support.
>
> I understood that recently the implementation of matrices over GF(2)
> was considerably improved. Therefore i am very surprised that the
> computation of the (left) kernel is still very slow:
>
> sage: version()
> 'SAGE Version 3.0.5, Release Date: 2008-07-11'
> sage: M=MatrixSpace(GF(2),1000,500).random_element()
> sage: time K=M.kernel()
> CPU times: user 21.60 s, sys: 0.06 s, total: 21.66 s
> Wall time: 40.87 s
> sage: time K.matrix()
> CPU times: user 15.06 s, sys: 0.03 s, total: 15.09 s
> Wall time: 27.71 s
> 500 x 1000 dense matrix over Finite Field of size 2
>
>
> Version 2.2.3 of C-MeatAxe (for which i have a wrapper) does much
> better:
>
> sage: m=MTX(2,[M[i].list() for i in range(1000)]) # Now, m is "the
> same" as M
> sage: time k=m.nullspace()
> CPU times: user 0.18 s, sys: 0.00 s, total: 0.18 s
> Wall time: 0.18 s
> sage: time k
> CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
> Wall time: 0.00 s
> (500 x 1000) MTX matrix over GF(2)
>
> Hence, we have an improvement from 21.60+15.06 CPU-seconds to 0.18
> seconds.
> And the result is right:
> sage: K.matrix()*M == 0
> True
> sage: k*m == MTX(2,500,500)   # this is a zero-matrix
> True
>
> Did i do something wrong? Is M.kernel() not what i should use here? Or
> is the kernel computation not optimised yet?

Computation of the kernel is done in two steps in Sage:

1. Compute the reduced row echelon form of the matrix.
2. Read off the kernel.
3. Create the kernel as a vector space.

In theory 1 takes most of the time and 2-3 are trivial.
In this particular case Sage is using 100% slow generic
code (over any base ring, etc.) to do 2-3, but superfast
code for 1:

sage: M=MatrixSpace(GF(2),1000,500).random_element()
sage: time E=M.echelon_form()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: time K=M.kernel()
CPU times: user 13.02 s, sys: 0.82 s, total: 13.84 s
Wall time: 14.54 s

Writing a version of the generic code that is optimized
for gf2 mr4i matrices would make it so the second step
above would take 0.00 seconds.  Really it would 
probably take about 10 ms, since

sage: M=MatrixSpace(GF(2),1000,500).random_element()
sage: timeit('M[0,0]=0; M.echelon_form()')
125 loops, best of 3: 3.46 ms per loop

So with proper optimization Sage should be at least an order
of magnitude than your meataxe benchmarks above. 

 -- William
```

Issue created by migration from https://trac.sagemath.org/ticket/3684





---

archive/issue_comments_026050.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-16T10:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3684#issuecomment-26050",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_026051.json:
```json
{
    "body": "With attached patch things are a little bit better (I didn't touch the vectors yet):\n\n```\nsage: M=MatrixSpace(GF(2),1000,500).random_element()\nsage: %time K=M.kernel()\nCPU times: user 5.89 s, sys: 0.00 s, total: 5.90 s\nWall time: 5.99 s\n\nsage: %time K.matrix()\nCPU times: user 3.36 s, sys: 0.49 s, total: 3.86 s\nWall time: 3.95 s\n500 x 1000 dense matrix over Finite Field of size 2\n```",
    "created_at": "2009-12-16T10:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3684#issuecomment-26051",
    "user": "https://github.com/malb"
}
```

With attached patch things are a little bit better (I didn't touch the vectors yet):

```
sage: M=MatrixSpace(GF(2),1000,500).random_element()
sage: %time K=M.kernel()
CPU times: user 5.89 s, sys: 0.00 s, total: 5.90 s
Wall time: 5.99 s

sage: %time K.matrix()
CPU times: user 3.36 s, sys: 0.49 s, total: 3.86 s
Wall time: 3.95 s
500 x 1000 dense matrix over Finite Field of size 2
```



---

archive/issue_comments_026052.json:
```json
{
    "body": "Attachment [mzd_kernel.patch](tarball://root/attachments/some-uuid/ticket3684/mzd_kernel.patch) by @mwhansen created at 2009-12-19 21:32:46\n\nLooks good to me.",
    "created_at": "2009-12-19T21:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3684#issuecomment-26052",
    "user": "https://github.com/mwhansen"
}
```

Attachment [mzd_kernel.patch](tarball://root/attachments/some-uuid/ticket3684/mzd_kernel.patch) by @mwhansen created at 2009-12-19 21:32:46

Looks good to me.



---

archive/issue_comments_026053.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T21:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3684#issuecomment-26053",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_008443.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-19T21:32:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3684",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3684#event-8443"
}
```



---

archive/issue_events_008444.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-20T07:46:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3684",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3684#event-8444"
}
```

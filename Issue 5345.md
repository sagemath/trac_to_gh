# Issue 5345: Optimize transpose for dense matrices

archive/issues_005345.json:
```json
{
    "body": "Assignee: rbeezer\n\nKeywords: transpose\n\nThis patch has two changes to the transpose method in matrix_dense.pyx to provide about a 15% speedup.  If this is accepted, I'll look into the other non-sparse routines for transpose and antitranspose.\n\n1.  A double loop indexes into the list of matrix entries using multiplication to create a reordered list for the transpose.  The effect of the multiplications is replaced by repeated additions.\n\n2.  Retrieving the list in the original matrix makes a copy with list().  This has been replaced by the internal _list() to just reference the original.\n\nPasses  sage -t  for  matrix2.pyx  and  matrix_dense.pyx\n\n```\nm = identity_matrix(5000)\ntime m.transpose()\n```\n\nTimings (user + system):\n\n11.94s : Stock 3.3\n\n11.20s : No multiplication\n\n10.18s : No multiplication, with _list()\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5345\n\n",
    "created_at": "2009-02-23T02:02:11Z",
    "labels": [
        "linear algebra",
        "trivial",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "Optimize transpose for dense matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5345",
    "user": "rbeezer"
}
```
Assignee: rbeezer

Keywords: transpose

This patch has two changes to the transpose method in matrix_dense.pyx to provide about a 15% speedup.  If this is accepted, I'll look into the other non-sparse routines for transpose and antitranspose.

1.  A double loop indexes into the list of matrix entries using multiplication to create a reordered list for the transpose.  The effect of the multiplications is replaced by repeated additions.

2.  Retrieving the list in the original matrix makes a copy with list().  This has been replaced by the internal _list() to just reference the original.

Passes  sage -t  for  matrix2.pyx  and  matrix_dense.pyx

```
m = identity_matrix(5000)
time m.transpose()
```

Timings (user + system):

11.94s : Stock 3.3

11.20s : No multiplication

10.18s : No multiplication, with _list()


Issue created by migration from https://trac.sagemath.org/ticket/5345





---

archive/issue_comments_041170.json:
```json
{
    "body": "Attachment [trac-5345-transpose-optimize.patch](tarball://root/attachments/some-uuid/ticket5345/trac-5345-transpose-optimize.patch) by rbeezer created at 2009-02-23 02:03:28",
    "created_at": "2009-02-23T02:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41170",
    "user": "rbeezer"
}
```

Attachment [trac-5345-transpose-optimize.patch](tarball://root/attachments/some-uuid/ticket5345/trac-5345-transpose-optimize.patch) by rbeezer created at 2009-02-23 02:03:28



---

archive/issue_comments_041171.json:
```json
{
    "body": "Changing priority from trivial to major.",
    "created_at": "2009-02-23T07:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41171",
    "user": "mabshoff"
}
```

Changing priority from trivial to major.



---

archive/issue_comments_041172.json:
```json
{
    "body": "A 18% speed improvement is never \"trivial\" for something like a basic operation like this :)\n\nCheers,\n\nMichael",
    "created_at": "2009-02-23T07:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41172",
    "user": "mabshoff"
}
```

A 18% speed improvement is never "trivial" for something like a basic operation like this :)

Cheers,

Michael



---

archive/issue_comments_041173.json:
```json
{
    "body": "I think we can obtain a much bigger speedup if we replace the inner loop:\n\n```\n...\n    for i in xrange(nr):\n        f.append(e[i*nc+j])\n...\n```\n\nwith\n\n```\n...\n    f.extend(e[j::nc])\n...\n```\n\n\nand we should do just the same thing for antitranspose a few lines further",
    "created_at": "2009-02-23T20:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41173",
    "user": "ylchapuy"
}
```

I think we can obtain a much bigger speedup if we replace the inner loop:

```
...
    for i in xrange(nr):
        f.append(e[i*nc+j])
...
```

with

```
...
    f.extend(e[j::nc])
...
```


and we should do just the same thing for antitranspose a few lines further



---

archive/issue_comments_041174.json:
```json
{
    "body": "Yann - I like it.  And yes, the antitranspose definitely needs a similar treatment.\n\nI swapped out the inner loop for the suggested slicing.  Same test run as listed above, and I got a total time of 10.14s.  So not a major speedup, but still a gain.\n\nI'll get back to this in the next couple of days and maybe try to do some more timings with multiple runs with the cache'ing of the list turned off.",
    "created_at": "2009-02-24T05:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41174",
    "user": "rbeezer"
}
```

Yann - I like it.  And yes, the antitranspose definitely needs a similar treatment.

I swapped out the inner loop for the suggested slicing.  Same test run as listed above, and I got a total time of 10.14s.  So not a major speedup, but still a gain.

I'll get back to this in the next couple of days and maybe try to do some more timings with multiple runs with the cache'ing of the list turned off.



---

archive/issue_comments_041175.json:
```json
{
    "body": "This transpose function has another problem, it copies the entries multiple times which is very bad for memory usage. For example I can't transpose a 5000x5000 matrix on my laptop.\nI suggest something like this (but maybe I'm missing something here?)\n\n```\n        (nc, nr) = (self.ncols(), self.nrows())\n        trans = self.new_matrix(nrows = nc, ncols = nr,\n                                copy=False,\n                                coerce=False)\n        for j in xrange(nc):\n            for i in xrange(nr):\n                trans[j,i]=self[i,j]\n\n        if self.subdivisions is not None:\n            row_divs, col_divs = self.get_subdivisions()\n            trans.subdivide(col_divs, row_divs)\n        return trans\n```\n\n(sorry, no time to do a proper patch right now)\n\nPS: I also think that there should be an optimized version af transpose in matrix_integer_dense.pyx, but it's probably for another ticket.",
    "created_at": "2009-02-24T18:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41175",
    "user": "ylchapuy"
}
```

This transpose function has another problem, it copies the entries multiple times which is very bad for memory usage. For example I can't transpose a 5000x5000 matrix on my laptop.
I suggest something like this (but maybe I'm missing something here?)

```
        (nc, nr) = (self.ncols(), self.nrows())
        trans = self.new_matrix(nrows = nc, ncols = nr,
                                copy=False,
                                coerce=False)
        for j in xrange(nc):
            for i in xrange(nr):
                trans[j,i]=self[i,j]

        if self.subdivisions is not None:
            row_divs, col_divs = self.get_subdivisions()
            trans.subdivide(col_divs, row_divs)
        return trans
```

(sorry, no time to do a proper patch right now)

PS: I also think that there should be an optimized version af transpose in matrix_integer_dense.pyx, but it's probably for another ticket.



---

archive/issue_comments_041176.json:
```json
{
    "body": "Attachment [trac-5345-transpose-matrix-dense.patch](tarball://root/attachments/some-uuid/ticket5345/trac-5345-transpose-matrix-dense.patch) by ylchapuy created at 2009-02-24 21:26:12",
    "created_at": "2009-02-24T21:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41176",
    "user": "ylchapuy"
}
```

Attachment [trac-5345-transpose-matrix-dense.patch](tarball://root/attachments/some-uuid/ticket5345/trac-5345-transpose-matrix-dense.patch) by ylchapuy created at 2009-02-24 21:26:12



---

archive/issue_comments_041177.json:
```json
{
    "body": "I had no time to do it, but of course I did it... Patch added implementing the idea above, plus unsafe access. It's a standalone patch (no need to apply yours) based on sage-3.3.\n\nsage -testall successful.\n\nAnd some statistics:\n\n```\nBefore:\n\nsage: m=identity_matrix(3000)\nsage: time m2=m.transpose(); m3=m.antitranspose()\nCPU times: user 14.13 s, sys: 1.11 s, total: 15.44 s\nWall time: 15.44 s\nsage: get_memory_usage()\n1254.28125\n\nAfter:\n\nsage: m=identity_matrix(3000)\nsage: time m2=m.transpose(); m3=m.antitranspose()\nCPU times: user 2.92 s, sys: 0.46 s, total: 3.38 s\nWall time: 3.38 s\nsage: get_memory_usage()\n835.6171875\n```\n\n\nI hope it's not too rude to make a patch for your ticket...\n\nCheers,\n      Yann",
    "created_at": "2009-02-24T21:27:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41177",
    "user": "ylchapuy"
}
```

I had no time to do it, but of course I did it... Patch added implementing the idea above, plus unsafe access. It's a standalone patch (no need to apply yours) based on sage-3.3.

sage -testall successful.

And some statistics:

```
Before:

sage: m=identity_matrix(3000)
sage: time m2=m.transpose(); m3=m.antitranspose()
CPU times: user 14.13 s, sys: 1.11 s, total: 15.44 s
Wall time: 15.44 s
sage: get_memory_usage()
1254.28125

After:

sage: m=identity_matrix(3000)
sage: time m2=m.transpose(); m3=m.antitranspose()
CPU times: user 2.92 s, sys: 0.46 s, total: 3.38 s
Wall time: 3.38 s
sage: get_memory_usage()
835.6171875
```


I hope it's not too rude to make a patch for your ticket...

Cheers,
      Yann



---

archive/issue_comments_041178.json:
```json
{
    "body": "Yann,\n\nNo problem with working up a patch.  I'm learning my way around Sage, and I've got plenty else to keep me busy.\n\nYes, I think the original worked with four copies of the matrix entries, so this version will just access the original and make the new transposed version, cutting out two copies.\n\nFor the record:  5000 x 5000 identity matrix as above, on same hardware.  Your changes result in 2.46s total time for me, so I'm seeing almost a 5x speedup.\n\nI can't find a transpose() in matrix_integer_dense.pyx.  But if there's more like this to be done, would you like to do it on a new ticket (and cc me)?  I didn't see any other matrix classes that might benefit from this sort of speedup - most seemed cython-ized already, both dense and sparse.\n\nI'm going to give this a positive review for the logic, but I don't feel qualified to comment on the cython-ization, since I'm not at all familiar with that, and I'm not sure about policy for the \"unsafe\" methods.  So I'll change the summary to needing a second look.\n\nRob",
    "created_at": "2009-02-25T05:07:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41178",
    "user": "rbeezer"
}
```

Yann,

No problem with working up a patch.  I'm learning my way around Sage, and I've got plenty else to keep me busy.

Yes, I think the original worked with four copies of the matrix entries, so this version will just access the original and make the new transposed version, cutting out two copies.

For the record:  5000 x 5000 identity matrix as above, on same hardware.  Your changes result in 2.46s total time for me, so I'm seeing almost a 5x speedup.

I can't find a transpose() in matrix_integer_dense.pyx.  But if there's more like this to be done, would you like to do it on a new ticket (and cc me)?  I didn't see any other matrix classes that might benefit from this sort of speedup - most seemed cython-ized already, both dense and sparse.

I'm going to give this a positive review for the logic, but I don't feel qualified to comment on the cython-ization, since I'm not at all familiar with that, and I'm not sure about policy for the "unsafe" methods.  So I'll change the summary to needing a second look.

Rob



---

archive/issue_comments_041179.json:
```json
{
    "body": "(if someone is interested, a patch for matrix_integer_dense is proposed in #5369)",
    "created_at": "2009-02-25T10:09:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41179",
    "user": "ylchapuy"
}
```

(if someone is interested, a patch for matrix_integer_dense is proposed in #5369)



---

archive/issue_comments_041180.json:
```json
{
    "body": "Looks good.  Apply only trac-5345-transpose-matrix-dense.patch",
    "created_at": "2009-02-25T18:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41180",
    "user": "mhansen"
}
```

Looks good.  Apply only trac-5345-transpose-matrix-dense.patch



---

archive/issue_comments_041181.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-28T21:03:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41181",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041182.json:
```json
{
    "body": "Merged trac-5345-transpose-matrix-dense.patch in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T21:03:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41182",
    "user": "mabshoff"
}
```

Merged trac-5345-transpose-matrix-dense.patch in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_comments_041183.json:
```json
{
    "body": "Replying to [comment:6 ylchapuy]:\n> And some statistics:\n> {{{\n> Before:\n> \n> sage: m=identity_matrix(3000)\n> sage: time m2=m.transpose(); m3=m.antitranspose()\n> CPU times: user 14.13 s, sys: 1.11 s, total: 15.44 s\n> Wall time: 15.44 s\n> sage: get_memory_usage()\n> 1254.28125\n> \n> After:\n> \n> sage: m=identity_matrix(3000)\n> sage: time m2=m.transpose(); m3=m.antitranspose()\n> CPU times: user 2.92 s, sys: 0.46 s, total: 3.38 s\n> Wall time: 3.38 s\n> sage: get_memory_usage()\n> 835.6171875\n> }}}\nIs it possible for you to provide some information on the computer/system architecture that you used to get the above statistics? The improved performance is great news and I'll include this in the release tour at\n[http://wiki.sagemath.org/sage-3.4](http://wiki.sagemath.org/sage-3.4)\nAnd it would also be good to have some info about the hardware under which you arrived at the above statistics.",
    "created_at": "2009-03-01T05:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41183",
    "user": "mvngu"
}
```

Replying to [comment:6 ylchapuy]:
> And some statistics:
> {{{
> Before:
> 
> sage: m=identity_matrix(3000)
> sage: time m2=m.transpose(); m3=m.antitranspose()
> CPU times: user 14.13 s, sys: 1.11 s, total: 15.44 s
> Wall time: 15.44 s
> sage: get_memory_usage()
> 1254.28125
> 
> After:
> 
> sage: m=identity_matrix(3000)
> sage: time m2=m.transpose(); m3=m.antitranspose()
> CPU times: user 2.92 s, sys: 0.46 s, total: 3.38 s
> Wall time: 3.38 s
> sage: get_memory_usage()
> 835.6171875
> }}}
Is it possible for you to provide some information on the computer/system architecture that you used to get the above statistics? The improved performance is great news and I'll include this in the release tour at
[http://wiki.sagemath.org/sage-3.4](http://wiki.sagemath.org/sage-3.4)
And it would also be good to have some info about the hardware under which you arrived at the above statistics.



---

archive/issue_comments_041184.json:
```json
{
    "body": "Replying to [comment:11 mvngu]:\n> Replying to [comment:6 ylchapuy]:\n> > And some statistics:\n> > {{{\n> > Before:\n> > \n> > sage: m=identity_matrix(3000)\n> > sage: time m2=m.transpose(); m3=m.antitranspose()\n> > CPU times: user 14.13 s, sys: 1.11 s, total: 15.44 s\n> > Wall time: 15.44 s\n> > sage: get_memory_usage()\n> > 1254.28125\n> > \n> > After:\n> > \n> > sage: m=identity_matrix(3000)\n> > sage: time m2=m.transpose(); m3=m.antitranspose()\n> > CPU times: user 2.92 s, sys: 0.46 s, total: 3.38 s\n> > Wall time: 3.38 s\n> > sage: get_memory_usage()\n> > 835.6171875\n> > }}}\n> Is it possible for you to provide some information on the computer/system architecture that you used to get the above statistics? The improved performance is great news and I'll include this in the release tour at\n> [http://wiki.sagemath.org/sage-3.4](http://wiki.sagemath.org/sage-3.4)\n> And it would also be good to have some info about the hardware under which you arrived at the above statistics.\n\nIt was on my laptop:\n\n```\nIntel(R) Core(TM)2 Duo CPU     T5450  @ 1.66GHz\nMemTotal:      2066004 kB\nLinux my-laptop 2.6.24-23-generic #1 SMP Thu Feb 5 15:00:25 UTC 2009 i686 GNU/Linux\n```\n",
    "created_at": "2009-03-01T09:51:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41184",
    "user": "ylchapuy"
}
```

Replying to [comment:11 mvngu]:
> Replying to [comment:6 ylchapuy]:
> > And some statistics:
> > {{{
> > Before:
> > 
> > sage: m=identity_matrix(3000)
> > sage: time m2=m.transpose(); m3=m.antitranspose()
> > CPU times: user 14.13 s, sys: 1.11 s, total: 15.44 s
> > Wall time: 15.44 s
> > sage: get_memory_usage()
> > 1254.28125
> > 
> > After:
> > 
> > sage: m=identity_matrix(3000)
> > sage: time m2=m.transpose(); m3=m.antitranspose()
> > CPU times: user 2.92 s, sys: 0.46 s, total: 3.38 s
> > Wall time: 3.38 s
> > sage: get_memory_usage()
> > 835.6171875
> > }}}
> Is it possible for you to provide some information on the computer/system architecture that you used to get the above statistics? The improved performance is great news and I'll include this in the release tour at
> [http://wiki.sagemath.org/sage-3.4](http://wiki.sagemath.org/sage-3.4)
> And it would also be good to have some info about the hardware under which you arrived at the above statistics.

It was on my laptop:

```
Intel(R) Core(TM)2 Duo CPU     T5450  @ 1.66GHz
MemTotal:      2066004 kB
Linux my-laptop 2.6.24-23-generic #1 SMP Thu Feb 5 15:00:25 UTC 2009 i686 GNU/Linux
```




---

archive/issue_comments_041185.json:
```json
{
    "body": "Replying to [comment:11 mvngu]:\n> Is it possible for you to provide some information on the computer/system architecture that you used to get the above statistics? The improved performance is great news and I'll include this in the release tour at\n> [http://wiki.sagemath.org/sage-3.4](http://wiki.sagemath.org/sage-3.4)\n> And it would also be good to have some info about the hardware under which you arrived at the above statistics.\n\nMinh,\n\nTimings for size 5000 identity matrix (at very top, then buried in the middle of comment 7 are on stock KUbuntu 8.10 with 3 GHz dual-core processor (Intel(R) Core(TM)2 Duo CPU  E8500 `@` 3.16GHz) with 8 GB memory.\n\nRob",
    "created_at": "2009-03-01T19:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41185",
    "user": "rbeezer"
}
```

Replying to [comment:11 mvngu]:
> Is it possible for you to provide some information on the computer/system architecture that you used to get the above statistics? The improved performance is great news and I'll include this in the release tour at
> [http://wiki.sagemath.org/sage-3.4](http://wiki.sagemath.org/sage-3.4)
> And it would also be good to have some info about the hardware under which you arrived at the above statistics.

Minh,

Timings for size 5000 identity matrix (at very top, then buried in the middle of comment 7 are on stock KUbuntu 8.10 with 3 GHz dual-core processor (Intel(R) Core(TM)2 Duo CPU  E8500 `@` 3.16GHz) with 8 GB memory.

Rob



---

archive/issue_comments_041186.json:
```json
{
    "body": "Thanks to Rob and Yann for the architecture info. For future reference, any optimization is very welcome. But for people who don't live on trac, a summary including timing and memory statistics as well as system architectures can be very useful. Of course any developer who has an account on sage.math can get the timing and memory statistics. But sage.math is not a regular PC or laptop; it's a powerful multi-core (over 20 cores, I think) machine with over *100* GB of RAM.",
    "created_at": "2009-03-02T01:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41186",
    "user": "mvngu"
}
```

Thanks to Rob and Yann for the architecture info. For future reference, any optimization is very welcome. But for people who don't live on trac, a summary including timing and memory statistics as well as system architectures can be very useful. Of course any developer who has an account on sage.math can get the timing and memory statistics. But sage.math is not a regular PC or laptop; it's a powerful multi-core (over 20 cores, I think) machine with over *100* GB of RAM.



---

archive/issue_comments_041187.json:
```json
{
    "body": "Replying to [comment:14 mvngu]:\n\nHi Minh,\n\n> Thanks to Rob and Yann for the architecture info. For future reference, any optimization is very welcome. But for people who don't live on trac, a summary including timing and memory statistics as well as system architectures can be very useful. Of course any developer who has an account on sage.math can get the timing and memory statistics. But sage.math is not a regular PC or laptop; it's a powerful multi-core (over 20 cores, I think) machine with over *100* GB of RAM.\n\nThe relative improvement will be identical, i.e. the fact that there are many core and a lot of RAM does have zero impact on CPU bound improvements like this. Indeed, due to the nature of the CPU and memory topology sage.math might actually see less of an improvement in certain cases.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T01:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41187",
    "user": "mabshoff"
}
```

Replying to [comment:14 mvngu]:

Hi Minh,

> Thanks to Rob and Yann for the architecture info. For future reference, any optimization is very welcome. But for people who don't live on trac, a summary including timing and memory statistics as well as system architectures can be very useful. Of course any developer who has an account on sage.math can get the timing and memory statistics. But sage.math is not a regular PC or laptop; it's a powerful multi-core (over 20 cores, I think) machine with over *100* GB of RAM.

The relative improvement will be identical, i.e. the fact that there are many core and a lot of RAM does have zero impact on CPU bound improvements like this. Indeed, due to the nature of the CPU and memory topology sage.math might actually see less of an improvement in certain cases.

Cheers,

Michael



---

archive/issue_comments_041188.json:
```json
{
    "body": "Replying to [comment:11 mvngu]:\n> The improved performance is great news and I'll include this in the release tour at\n> [http://wiki.sagemath.org/sage-3.4](http://wiki.sagemath.org/sage-3.4)\n> And it would also be good to have some info about the hardware under which you arrived at the above statistics.\n\nAs you can see 15.44s --> 3.38s on my machine, or 11.94s --> 2.46s on Rob's one represent more than a 15% improved performance :). You should change the release tour accordingly.",
    "created_at": "2009-03-04T19:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41188",
    "user": "ylchapuy"
}
```

Replying to [comment:11 mvngu]:
> The improved performance is great news and I'll include this in the release tour at
> [http://wiki.sagemath.org/sage-3.4](http://wiki.sagemath.org/sage-3.4)
> And it would also be good to have some info about the hardware under which you arrived at the above statistics.

As you can see 15.44s --> 3.38s on my machine, or 11.94s --> 2.46s on Rob's one represent more than a 15% improved performance :). You should change the release tour accordingly.



---

archive/issue_comments_041189.json:
```json
{
    "body": "Replying to [comment:16 ylchapuy]:\n> As you can see 15.44s --> 3.38s on my machine, or 11.94s --> 2.46s on \n> Rob's one represent more than a 15% improved performance :). You should\n> change the release tour accordingly.\nThis might be a stupid question: For the record, can you please provide a mathematical formula for calculating the percentage improvement in time/memory? For example, if p1 is the previous performance time and p2 is the new and improved performance time, how do I calculate the percentage improvement? This assumes that both p1 and p2 are both expressed in the same unit of measurement, e.g. seconds.",
    "created_at": "2009-03-05T03:32:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41189",
    "user": "mvngu"
}
```

Replying to [comment:16 ylchapuy]:
> As you can see 15.44s --> 3.38s on my machine, or 11.94s --> 2.46s on 
> Rob's one represent more than a 15% improved performance :). You should
> change the release tour accordingly.
This might be a stupid question: For the record, can you please provide a mathematical formula for calculating the percentage improvement in time/memory? For example, if p1 is the previous performance time and p2 is the new and improved performance time, how do I calculate the percentage improvement? This assumes that both p1 and p2 are both expressed in the same unit of measurement, e.g. seconds.



---

archive/issue_comments_041190.json:
```json
{
    "body": "Replying to [comment:17 mvngu]:\n> This might be a stupid question: For the record, can you please provide a mathematical formula for calculating the percentage improvement in time/memory? For example, if p1 is the previous performance time and p2 is the new and improved performance time, how do I calculate the percentage improvement? This assumes that both p1 and p2 are both expressed in the same unit of measurement, e.g. seconds.\n\nMinh,\n\nFor small changes, I'd quote (p1-p2)/p1 as a percentage.  So 10 seconds down to 8 seconds would be a 20% improvement.  When that percentage gets close to 100%, (like over 50%, 60%, 70%) I'd switch to a factor as a \"speedup\" given by p1/p2.  From 10 seconds down to 1 seconds would be an 90% improvement, but I'd quote a 10x (10 times) factor.  So for the release tour, I'd just quote a 5x or a \"factor of 5\" improvement for these results.  The really curious can come see the exact numbers for themselves.  Hope this helps.\n\nRob",
    "created_at": "2009-03-05T05:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41190",
    "user": "rbeezer"
}
```

Replying to [comment:17 mvngu]:
> This might be a stupid question: For the record, can you please provide a mathematical formula for calculating the percentage improvement in time/memory? For example, if p1 is the previous performance time and p2 is the new and improved performance time, how do I calculate the percentage improvement? This assumes that both p1 and p2 are both expressed in the same unit of measurement, e.g. seconds.

Minh,

For small changes, I'd quote (p1-p2)/p1 as a percentage.  So 10 seconds down to 8 seconds would be a 20% improvement.  When that percentage gets close to 100%, (like over 50%, 60%, 70%) I'd switch to a factor as a "speedup" given by p1/p2.  From 10 seconds down to 1 seconds would be an 90% improvement, but I'd quote a 10x (10 times) factor.  So for the release tour, I'd just quote a 5x or a "factor of 5" improvement for these results.  The really curious can come see the exact numbers for themselves.  Hope this helps.

Rob



---

archive/issue_comments_041191.json:
```json
{
    "body": "Replying to [comment:18 rbeezer]:\n> For small changes, I'd quote (p1-p2)/p1 as a percentage.  So 10 seconds down to\n> 8 seconds would be a 20% improvement.  When that percentage gets close to 100%,\n> (like over 50%, 60%, 70%) I'd switch to a factor as a \"speedup\" given by p1/p2. \n> From 10 seconds down to 1 seconds would be an 90% improvement, but I'd quote a \n> 10x (10 times) factor.  So for the release tour, I'd just quote a 5x or a \"factor\n> of 5\" improvement for these results.  The really curious can come see the exact\n> numbers for themselves.  Hope this helps.\nThanks, Rob. That certainly helps.",
    "created_at": "2009-03-05T06:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5345#issuecomment-41191",
    "user": "mvngu"
}
```

Replying to [comment:18 rbeezer]:
> For small changes, I'd quote (p1-p2)/p1 as a percentage.  So 10 seconds down to
> 8 seconds would be a 20% improvement.  When that percentage gets close to 100%,
> (like over 50%, 60%, 70%) I'd switch to a factor as a "speedup" given by p1/p2. 
> From 10 seconds down to 1 seconds would be an 90% improvement, but I'd quote a 
> 10x (10 times) factor.  So for the release tour, I'd just quote a 5x or a "factor
> of 5" improvement for these results.  The really curious can come see the exact
> numbers for themselves.  Hope this helps.
Thanks, Rob. That certainly helps.

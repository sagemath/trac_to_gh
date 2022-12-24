# Issue 5402: Sparse determinants are slow

archive/issues_005402.json:
```json
{
    "body": "Assignee: was\n\nCC:  jbandlow\n\nKeywords: determinant\n\nThe following timings should be able to be improved.\n\n```\n       sage: dd = {(0,0):1}\n       sage: %timeit matrix(8,dd).det()\n       10 loops, best of 3: 213 ms per loop\n       sage: %timeit matrix(8,dd,sparse = False).det()\n       100 loops, best of 3: 629 \u00b5s per loop\n```\n\nWilliam suggested:\nLikely the fix will be to implement\na 1-line function that is just\n\n```\n  return self.dense_matrix().det(*args, **kwds)\n```\n\nuntil there is somebody who wants to implement a sparse algorithm.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5402\n\n",
    "created_at": "2009-02-28T20:16:47Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.6",
    "title": "Sparse determinants are slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5402",
    "user": "jbandlow"
}
```
Assignee: was

CC:  jbandlow

Keywords: determinant

The following timings should be able to be improved.

```
       sage: dd = {(0,0):1}
       sage: %timeit matrix(8,dd).det()
       10 loops, best of 3: 213 ms per loop
       sage: %timeit matrix(8,dd,sparse = False).det()
       100 loops, best of 3: 629 µs per loop
```

William suggested:
Likely the fix will be to implement
a 1-line function that is just

```
  return self.dense_matrix().det(*args, **kwds)
```

until there is somebody who wants to implement a sparse algorithm.

Issue created by migration from https://trac.sagemath.org/ticket/5402





---

archive/issue_comments_041719.json:
```json
{
    "body": "I would tend to avoid converting to a dense matrix by default since one often uses sparse matrices because they don't have enough memory to store the dense ones.",
    "created_at": "2009-02-28T20:34:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41719",
    "user": "mhansen"
}
```

I would tend to avoid converting to a dense matrix by default since one often uses sparse matrices because they don't have enough memory to store the dense ones.



---

archive/issue_comments_041720.json:
```json
{
    "body": "Sure, but as of right now, I've been waiting over fifteen minutes for \n\n```\n       sage: dd = {(0,0):1}\n       sage: %time matrix(100,dd).det()\n```\n\nwhereas\n\n```\n       sage: %time matrix(100,dd,sparse=False).det()\n       CPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s\n       Wall time: 0.08 s\n```\n\n\nSo, currently, for a matrix large enough to have memory issues, determinants are already completely infeasible.  So I don't think anything would be lost by the one-line change proposed by William.  Of course, writing a sparse algorithm that is competitive speed-wise, or could be used only for very large matrices, would be ideal.  But it took me some time today to figure out why computing ~1000 determinants of 8x8 sparse matrices was taking so long, and if there could be a quick fix to spare others from my pain, it would be nice. :)",
    "created_at": "2009-02-28T22:49:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41720",
    "user": "jbandlow"
}
```

Sure, but as of right now, I've been waiting over fifteen minutes for 

```
       sage: dd = {(0,0):1}
       sage: %time matrix(100,dd).det()
```

whereas

```
       sage: %time matrix(100,dd,sparse=False).det()
       CPU times: user 0.06 s, sys: 0.00 s, total: 0.06 s
       Wall time: 0.08 s
```


So, currently, for a matrix large enough to have memory issues, determinants are already completely infeasible.  So I don't think anything would be lost by the one-line change proposed by William.  Of course, writing a sparse algorithm that is competitive speed-wise, or could be used only for very large matrices, would be ideal.  But it took me some time today to figure out why computing ~1000 determinants of 8x8 sparse matrices was taking so long, and if there could be a quick fix to spare others from my pain, it would be nice. :)



---

archive/issue_comments_041721.json:
```json
{
    "body": "Yep, I agree with Jason's position.\n\nWe are doing the same for some other LA bits where the sparse methods takes longer **and** uses more memory than the dense method for many cases.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T06:26:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41721",
    "user": "mabshoff"
}
```

Yep, I agree with Jason's position.

We are doing the same for some other LA bits where the sparse methods takes longer **and** uses more memory than the dense method for many cases.

Cheers,

Michael



---

archive/issue_comments_041722.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-01-03T14:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41722",
    "user": "Bouillaguet"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_041723.json:
```json
{
    "body": "Apparently, this issue has been fixed. The determinant that used to take 15 minutes now takes 0.05s...",
    "created_at": "2013-01-03T14:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41723",
    "user": "Bouillaguet"
}
```

Apparently, this issue has been fixed. The determinant that used to take 15 minutes now takes 0.05s...



---

archive/issue_comments_041724.json:
```json
{
    "body": "I wouldn't say that it's fixed.  Note the comparison is better but still they are not that close.\n\n```\nsage: dd = {(0,0):1}\nsage: %timeit matrix(8,dd).det()\n5 loops, best of 3: 2.83 ms per loop\nsage: %timeit matrix(8,dd,sparse = False).det()\n625 loops, best of 3: 147 \u00b5s per loop\nsage: %timeit matrix(100,dd).det()\n5 loops, best of 3: 228 ms per loop\nsage: %timeit matrix(100,dd,sparse = False).det()\n25 loops, best of 3: 15.2 ms per loop\n```\n\nIt's just that everything is faster now.  How much faster would Moore's law say these should be after four years?",
    "created_at": "2013-01-03T15:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41724",
    "user": "kcrisman"
}
```

I wouldn't say that it's fixed.  Note the comparison is better but still they are not that close.

```
sage: dd = {(0,0):1}
sage: %timeit matrix(8,dd).det()
5 loops, best of 3: 2.83 ms per loop
sage: %timeit matrix(8,dd,sparse = False).det()
625 loops, best of 3: 147 µs per loop
sage: %timeit matrix(100,dd).det()
5 loops, best of 3: 228 ms per loop
sage: %timeit matrix(100,dd,sparse = False).det()
25 loops, best of 3: 15.2 ms per loop
```

It's just that everything is faster now.  How much faster would Moore's law say these should be after four years?



---

archive/issue_comments_041725.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-01-03T15:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41725",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_041726.json:
```json
{
    "body": "Replying to [comment:5 kcrisman]:\n> {{{\n> sage: %timeit matrix(100,dd).det()\n> 5 loops, best of 3: 228 ms per loop\n> sage: %timeit matrix(100,dd,sparse = False).det()\n> 25 loops, best of 3: 15.2 ms per loop\n> }}}\n> It's just that everything is faster now.  How much faster would Moore's law say these should be after four years?\n\nIn comment 2, someone complains about this test running for 15 minutes. On your machine, it runs in 228ms (sparse case). This is about 4000x times faster. Moore's law tell you that the number of transistor on a chip doubles every 18 months, so that in 4 years we would have at the very maximum a 10x speedup.\n\nSo, there was clearly some improvement. \n\nHowever, if you look into it a bit deeper, then you'll see that in the sparse case, computing the determinant triggers the computation of the charpoly(), and the computation of the charpoly creates a dense version of the matrix, then runs the dense charpoly algorithm. I thus agree that this is suboptimal (in particular because linbox has fancy iterative methods for this kind of computation on sparse matrices).\n\nAnyway, why don't we : a) close this ticket, considering that it is outdated and that the situation has changed, and b) open a \"feature request\" ticket related to sparse matrices over exact rings? I would be happy to look into this.",
    "created_at": "2013-01-04T10:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41726",
    "user": "Bouillaguet"
}
```

Replying to [comment:5 kcrisman]:
> {{{
> sage: %timeit matrix(100,dd).det()
> 5 loops, best of 3: 228 ms per loop
> sage: %timeit matrix(100,dd,sparse = False).det()
> 25 loops, best of 3: 15.2 ms per loop
> }}}
> It's just that everything is faster now.  How much faster would Moore's law say these should be after four years?

In comment 2, someone complains about this test running for 15 minutes. On your machine, it runs in 228ms (sparse case). This is about 4000x times faster. Moore's law tell you that the number of transistor on a chip doubles every 18 months, so that in 4 years we would have at the very maximum a 10x speedup.

So, there was clearly some improvement. 

However, if you look into it a bit deeper, then you'll see that in the sparse case, computing the determinant triggers the computation of the charpoly(), and the computation of the charpoly creates a dense version of the matrix, then runs the dense charpoly algorithm. I thus agree that this is suboptimal (in particular because linbox has fancy iterative methods for this kind of computation on sparse matrices).

Anyway, why don't we : a) close this ticket, considering that it is outdated and that the situation has changed, and b) open a "feature request" ticket related to sparse matrices over exact rings? I would be happy to look into this.



---

archive/issue_comments_041727.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-01-04T10:42:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41727",
    "user": "Bouillaguet"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_041728.json:
```json
{
    "body": "> > It's just that everything is faster now.  How much faster would Moore's law say these should be after four years?\n> \n> In comment 2, someone complains about this test running for 15 minutes. On your machine, it runs in 228ms (sparse case). This is about 4000x times faster. Moore's law tell you that the number of transistor on a chip doubles every 18 months, so that in 4 years we would have at the very maximum a 10x speedup.\nInterestingly, other than that one, the rest indeed show a 4-10x speedup.\n\n> However, if you look into it a bit deeper, then you'll see that in the sparse case, computing the determinant triggers the computation of the charpoly(), and the computation of the charpoly creates a dense version of the matrix, then runs the dense charpoly algorithm. I thus agree that this is suboptimal (in particular because linbox has fancy iterative methods for this kind of computation on sparse matrices).\n> \n> Anyway, why don't we : a) close this ticket, considering that it is outdated and that the situation has changed, and b) open a \"feature request\" ticket related to sparse matrices over exact rings? I would be happy to look into this.\nWell, given that we *already* create the dense matrix, then William's fix seems like it would speed things up at least a little, or be no worse?  I don't see why we (by which I mean you and other people who compute such determinants!) couldn't try it out, *as well as* of course creating a new ticket to use fancy methods.  Seem reasonable?",
    "created_at": "2013-01-04T14:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41728",
    "user": "kcrisman"
}
```

> > It's just that everything is faster now.  How much faster would Moore's law say these should be after four years?
> 
> In comment 2, someone complains about this test running for 15 minutes. On your machine, it runs in 228ms (sparse case). This is about 4000x times faster. Moore's law tell you that the number of transistor on a chip doubles every 18 months, so that in 4 years we would have at the very maximum a 10x speedup.
Interestingly, other than that one, the rest indeed show a 4-10x speedup.

> However, if you look into it a bit deeper, then you'll see that in the sparse case, computing the determinant triggers the computation of the charpoly(), and the computation of the charpoly creates a dense version of the matrix, then runs the dense charpoly algorithm. I thus agree that this is suboptimal (in particular because linbox has fancy iterative methods for this kind of computation on sparse matrices).
> 
> Anyway, why don't we : a) close this ticket, considering that it is outdated and that the situation has changed, and b) open a "feature request" ticket related to sparse matrices over exact rings? I would be happy to look into this.
Well, given that we *already* create the dense matrix, then William's fix seems like it would speed things up at least a little, or be no worse?  I don't see why we (by which I mean you and other people who compute such determinants!) couldn't try it out, *as well as* of course creating a new ticket to use fancy methods.  Seem reasonable?



---

archive/issue_comments_041729.json:
```json
{
    "body": "Fair enough. I'll post a patch this week-end.",
    "created_at": "2013-01-04T15:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41729",
    "user": "Bouillaguet"
}
```

Fair enough. I'll post a patch this week-end.



---

archive/issue_comments_041730.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-01-04T15:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41730",
    "user": "Bouillaguet"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_041731.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-01-04T17:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41731",
    "user": "Bouillaguet"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_041732.json:
```json
{
    "body": "Attachment [5402_faster_dumber_det.patch](tarball://root/attachments/some-uuid/ticket5402/5402_faster_dumber_det.patch) by Bouillaguet created at 2013-01-04 17:26:04\n\nWith patch applied:\n\n```\nsage: dd = {(0,0):1}\nsage: %timeit matrix(100,dd).det()\n125 loops, best of 3: 7.04 ms per loop\nsage: %timeit matrix(100,dd,sparse = False).det()\n25 loops, best of 3: 16.3 ms per loop\n```\n\n\nSo that now the sparse case is faster! I really don't understand why tough, because it converts the matrix to a dense representation before computing the (dense) det...",
    "created_at": "2013-01-04T17:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41732",
    "user": "Bouillaguet"
}
```

Attachment [5402_faster_dumber_det.patch](tarball://root/attachments/some-uuid/ticket5402/5402_faster_dumber_det.patch) by Bouillaguet created at 2013-01-04 17:26:04

With patch applied:

```
sage: dd = {(0,0):1}
sage: %timeit matrix(100,dd).det()
125 loops, best of 3: 7.04 ms per loop
sage: %timeit matrix(100,dd,sparse = False).det()
25 loops, best of 3: 16.3 ms per loop
```


So that now the sparse case is faster! I really don't understand why tough, because it converts the matrix to a dense representation before computing the (dense) det...



---

archive/issue_comments_041733.json:
```json
{
    "body": "I get the same thing.  With a heavy load on the same computer (accounting for non-sparse slowdown),\n\n```\nsage: dd = {(0,0):1}\nsage: %timeit matrix(8,dd).det()\n5 loops, best of 3: 207 \u00b5s per loop\nsage: %timeit matrix(8,dd,sparse = False).det()\n625 loops, best of 3: 240 \u00b5s per loop\nsage: %timeit matrix(100,dd).det()\n25 loops, best of 3: 11.2 ms per loop\nsage: %timeit matrix(100,dd,sparse = False).det()\n25 loops, best of 3: 23.3 ms per loop\n```\n\nMaybe the way we make dictionary-defined matrices dense with `sparse=False` is suboptimal?\n\nI like the patch, though it would be nice if you could find someone who has worked with caching before just to check that that code is correct - I haven't really used it in the past and don't have time to find similar examples in the code now, my apologies.",
    "created_at": "2013-01-04T17:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41733",
    "user": "kcrisman"
}
```

I get the same thing.  With a heavy load on the same computer (accounting for non-sparse slowdown),

```
sage: dd = {(0,0):1}
sage: %timeit matrix(8,dd).det()
5 loops, best of 3: 207 µs per loop
sage: %timeit matrix(8,dd,sparse = False).det()
625 loops, best of 3: 240 µs per loop
sage: %timeit matrix(100,dd).det()
25 loops, best of 3: 11.2 ms per loop
sage: %timeit matrix(100,dd,sparse = False).det()
25 loops, best of 3: 23.3 ms per loop
```

Maybe the way we make dictionary-defined matrices dense with `sparse=False` is suboptimal?

I like the patch, though it would be nice if you could find someone who has worked with caching before just to check that that code is correct - I haven't really used it in the past and don't have time to find similar examples in the code now, my apologies.



---

archive/issue_comments_041734.json:
```json
{
    "body": "There is an example of caching (the one I just mimicked...) in matrix_sparse.pyx in the definition of charpoly().\n\nI checked that caching works by computing a large sparse determinant twice : the first call takes a few seconds, while the second call returns instantly.\n\nFor the sake of easy reviewing :-) here is the code of charpoly() :\n\n\n```python\ndef charpoly(self, var='x', **kwds):\n        f = self.fetch('charpoly')\n        if f is not None:\n            return f.change_variable_name(var)\n        f = self.dense_matrix().charpoly(var=var, **kwds)\n        self.cache('charpoly', f)\n        return f\n```\n",
    "created_at": "2013-01-04T17:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41734",
    "user": "Bouillaguet"
}
```

There is an example of caching (the one I just mimicked...) in matrix_sparse.pyx in the definition of charpoly().

I checked that caching works by computing a large sparse determinant twice : the first call takes a few seconds, while the second call returns instantly.

For the sake of easy reviewing :-) here is the code of charpoly() :


```python
def charpoly(self, var='x', **kwds):
        f = self.fetch('charpoly')
        if f is not None:
            return f.change_variable_name(var)
        f = self.dense_matrix().charpoly(var=var, **kwds)
        self.cache('charpoly', f)
        return f
```




---

archive/issue_comments_041735.json:
```json
{
    "body": "Well, there you have it.  And the way to test it worked was perfect.\n\nOkay, open that other ticket, and then you have yourself a positive review.  Still unclear as to why it's *faster* than the dense case...",
    "created_at": "2013-01-04T18:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41735",
    "user": "kcrisman"
}
```

Well, there you have it.  And the way to test it worked was perfect.

Okay, open that other ticket, and then you have yourself a positive review.  Still unclear as to why it's *faster* than the dense case...



---

archive/issue_comments_041736.json:
```json
{
    "body": "http://trac.sagemath.org/sage_trac/ticket/13915 is opened",
    "created_at": "2013-01-06T09:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41736",
    "user": "Bouillaguet"
}
```

http://trac.sagemath.org/sage_trac/ticket/13915 is opened



---

archive/issue_comments_041737.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-07T14:02:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41737",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_041738.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-01-09T09:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5402#issuecomment-41738",
    "user": "jdemeyer"
}
```

Resolution: fixed

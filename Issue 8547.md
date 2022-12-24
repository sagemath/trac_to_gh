# Issue 8547: implement hidden markov models in Cython from scratch (so can remove the GHMM standard package from Sage)

archive/issues_008547.json:
```json
{
    "body": "Assignee: amhou\n\nCC:  jason mhampton\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8547\n\n",
    "created_at": "2010-03-16T08:08:50Z",
    "labels": [
        "statistics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "implement hidden markov models in Cython from scratch (so can remove the GHMM standard package from Sage)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8547",
    "user": "was"
}
```
Assignee: amhou

CC:  jason mhampton



Issue created by migration from https://trac.sagemath.org/ticket/8547





---

archive/issue_comments_077272.json:
```json
{
    "body": "apply this. Then look at devel/sage/sage/stats/intlist.pyx, devel/sage/sage/stats/hmm (which is entirely new code), and look at the few minor bug fixes to finance/time_series.pyx",
    "created_at": "2010-03-20T12:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77272",
    "user": "was"
}
```

apply this. Then look at devel/sage/sage/stats/intlist.pyx, devel/sage/sage/stats/hmm (which is entirely new code), and look at the few minor bug fixes to finance/time_series.pyx



---

archive/issue_comments_077273.json:
```json
{
    "body": "Attachment [trac_8547.patch](tarball://root/attachments/some-uuid/ticket8547/trac_8547.patch) by was created at 2010-03-20 12:49:50",
    "created_at": "2010-03-20T12:49:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77273",
    "user": "was"
}
```

Attachment [trac_8547.patch](tarball://root/attachments/some-uuid/ticket8547/trac_8547.patch) by was created at 2010-03-20 12:49:50



---

archive/issue_comments_077274.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-20T12:49:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77274",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077275.json:
```json
{
    "body": "This is now ready for review.  Some notes:\n\n1. Don't bother looking at the diff, except for time_series.pyx and module_list.py.  Just look at at the files in stats/hmm, which are all new, and stats/intlist.pyx.\n\n2. There are a number of very small API changes (for the better).   This technically violates our DeprecationPolicy.  However, frankly, the current code was -- upon inspection -- so bad, that there is no way anybody was actually using it for anything serious.  (As was evidenced by the response on sage-devel.)  And the API is only a tiny bit changed now. \n\n3. I do have a long list of possible followup projects. However, I wanted to make a first solid release that at least has enough to replace the existing HMM functionality in Sage, before adding lots of new stuff.",
    "created_at": "2010-03-20T12:53:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77275",
    "user": "was"
}
```

This is now ready for review.  Some notes:

1. Don't bother looking at the diff, except for time_series.pyx and module_list.py.  Just look at at the files in stats/hmm, which are all new, and stats/intlist.pyx.

2. There are a number of very small API changes (for the better).   This technically violates our DeprecationPolicy.  However, frankly, the current code was -- upon inspection -- so bad, that there is no way anybody was actually using it for anything serious.  (As was evidenced by the response on sage-devel.)  And the API is only a tiny bit changed now. 

3. I do have a long list of possible followup projects. However, I wanted to make a first solid release that at least has enough to replace the existing HMM functionality in Sage, before adding lots of new stuff.



---

archive/issue_comments_077276.json:
```json
{
    "body": "Changing assignee from amhou to mhampton.",
    "created_at": "2010-03-21T17:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77276",
    "user": "mhampton"
}
```

Changing assignee from amhou to mhampton.



---

archive/issue_comments_077277.json:
```json
{
    "body": "Changing assignee from mhampton to amhou.",
    "created_at": "2010-03-21T17:05:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77277",
    "user": "mhampton"
}
```

Changing assignee from mhampton to amhou.



---

archive/issue_comments_077278.json:
```json
{
    "body": "This patch touches matrix2.pyx which results in failures of a number of doctests.  Example:\n\n\n```\nsage -t  devel/sage/sage/matrix/matrix2.pyx\n**********************************************************************\nFile \"/mnt/usb1/scratch/boothby/sage-4.3.4/devel/sage-main/sage/matrix/matrix2.pyx\", line 3142:\n    sage: A.restrict(W2, check=True)\nExpected:\n    Traceback (most recent call last):\n    ...\n    ArithmeticError: subspace is not invariant under matrix\nGot:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/boothby/sage-4.3.4/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/boothby/sage-4.3.4/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/boothby/sage-4.3.4/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_48[10]>\", line 1, in <module>\n        A.restrict(W2, check=True)###line 3142:\n    sage: A.restrict(W2, check=True)\n      File \"matrix2.pyx\", line 3167, in sage.matrix.matrix2.Matrix.restrict (sage/matrix/matrix2.c:19470)\n        raise ArithmeticError, \"subspace is not invariant under matrix (%s)\"%msg\n    ArithmeticError: subspace is not invariant under matrix (vector is not in free module)\n**********************************************************************\n```\n\n\nThat should be easy to fix.",
    "created_at": "2010-03-28T20:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77278",
    "user": "boothby"
}
```

This patch touches matrix2.pyx which results in failures of a number of doctests.  Example:


```
sage -t  devel/sage/sage/matrix/matrix2.pyx
**********************************************************************
File "/mnt/usb1/scratch/boothby/sage-4.3.4/devel/sage-main/sage/matrix/matrix2.pyx", line 3142:
    sage: A.restrict(W2, check=True)
Expected:
    Traceback (most recent call last):
    ...
    ArithmeticError: subspace is not invariant under matrix
Got:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/boothby/sage-4.3.4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/boothby/sage-4.3.4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/boothby/sage-4.3.4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_48[10]>", line 1, in <module>
        A.restrict(W2, check=True)###line 3142:
    sage: A.restrict(W2, check=True)
      File "matrix2.pyx", line 3167, in sage.matrix.matrix2.Matrix.restrict (sage/matrix/matrix2.c:19470)
        raise ArithmeticError, "subspace is not invariant under matrix (%s)"%msg
    ArithmeticError: subspace is not invariant under matrix (vector is not in free module)
**********************************************************************
```


That should be easy to fix.



---

archive/issue_comments_077279.json:
```json
{
    "body": "this completely replaces the previous patch",
    "created_at": "2010-03-28T21:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77279",
    "user": "was"
}
```

this completely replaces the previous patch



---

archive/issue_comments_077280.json:
```json
{
    "body": "Attachment [trac-8547-take2.patch](tarball://root/attachments/some-uuid/ticket8547/trac-8547-take2.patch) by boothby created at 2010-03-30 23:47:50\n\nOk, doctests run clean now.  I've tested the code out and read it over, and it works for me.  I'm a little cautious giving this a positive review because I know very little about this area of math.  However, given that it's replacing something that barely worked and used memory like toilet paper, I'm willing to throw caution to the wind if mhampton or jason are willing to sign off on the idea.",
    "created_at": "2010-03-30T23:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77280",
    "user": "boothby"
}
```

Attachment [trac-8547-take2.patch](tarball://root/attachments/some-uuid/ticket8547/trac-8547-take2.patch) by boothby created at 2010-03-30 23:47:50

Ok, doctests run clean now.  I've tested the code out and read it over, and it works for me.  I'm a little cautious giving this a positive review because I know very little about this area of math.  However, given that it's replacing something that barely worked and used memory like toilet paper, I'm willing to throw caution to the wind if mhampton or jason are willing to sign off on the idea.



---

archive/issue_comments_077281.json:
```json
{
    "body": "I've been wanting to review this but I just haven't had the time.  I might this weekend, but its unclear.",
    "created_at": "2010-03-31T03:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77281",
    "user": "mhampton"
}
```

I've been wanting to review this but I just haven't had the time.  I might this weekend, but its unclear.



---

archive/issue_comments_077282.json:
```json
{
    "body": "Some notes from reading through the code looking at stylistic issues.\u00a0 I really wish we had line-by-line commenting like rietveld for this sort of thing.\n\n1. Lots of cdef'd functions do not have doctests.\u00a0 I thought the policy from discussions on sage-devel was that *every* function (including cdef functions) should have doctests (but, of course, these doctests would have to either indirectly test the cdef'd function or would have to test a wrapper of the cdef function).\u00a0 Some functions (_baum_welch_gamma, for example) don't even have docstrings.\n2. I'm curious why IntList.!__getitem!__ does not use the sage.misc.misc_c.normalize_index function to deal with slices.\u00a0 How much of a performance penalty is there?\u00a0 Can this \"python semantics\" part be extracted out to be a more general cdef'd counterpart to normalize_index, so that matrices, vectors, and other types can use it better to implement !__getitem!__?\u00a0 Also, as a future enhancement, it doesn't seem that much harder for !__setitem!__ to also support slices.\u00a0 At the very least, the doctests for normalize_index probably ought to be run on the !__getitem!__ function, as they exercise a number of corner cases for the python semantics.\n3. IntList.sum() does not have a doctest for the overflow case",
    "created_at": "2010-03-31T03:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77282",
    "user": "jason"
}
```

Some notes from reading through the code looking at stylistic issues.  I really wish we had line-by-line commenting like rietveld for this sort of thing.

1. Lots of cdef'd functions do not have doctests.  I thought the policy from discussions on sage-devel was that *every* function (including cdef functions) should have doctests (but, of course, these doctests would have to either indirectly test the cdef'd function or would have to test a wrapper of the cdef function).  Some functions (_baum_welch_gamma, for example) don't even have docstrings.
2. I'm curious why IntList.!__getitem!__ does not use the sage.misc.misc_c.normalize_index function to deal with slices.  How much of a performance penalty is there?  Can this "python semantics" part be extracted out to be a more general cdef'd counterpart to normalize_index, so that matrices, vectors, and other types can use it better to implement !__getitem!__?  Also, as a future enhancement, it doesn't seem that much harder for !__setitem!__ to also support slices.  At the very least, the doctests for normalize_index probably ought to be run on the !__getitem!__ function, as they exercise a number of corner cases for the python semantics.
3. IntList.sum() does not have a doctest for the overflow case



---

archive/issue_comments_077283.json:
```json
{
    "body": "Replying to [comment:10 jason]:\n> Some notes from reading through the code looking at stylistic issues.\u00a0 I really wish we had\n>  line-by-line commenting like rietveld for this sort of thing.\n> \n>  1. Lots of cdef'd functions do not have doctests.\u00a0 I thought the policy from discussions on sage-devel \n> was that *every* function (including cdef functions) should have doctests (but, of course, these doctests\n>  would have to either indirectly test the cdef'd function or would have to test a wrapper of the cdef function).\u00a0 \n\nWe definitely do not require doctests for cdef'd methods.   The requirement is that \"sage -coverage\" returns a score of 100%.  This is clearly stated in the patch reviewers guide.    I did seriously consider them in this case, but literally every single one of these doctests would just be a literal *exact* copy of a doctest from elsewhere (!) but with # indirect doctest next to it.  There's just no value in that.   I could also make the methods cpdef, but that does incur a performance penalty -- in this case, it would be huge (which is totally unacceptable). \n\n> Some functions (_baum_welch_gamma, for example) don't even have docstrings.\n\nI do think that all cdef'd methods should have docstrings, and will add docstrings to any that don't have them (in a part 2 patch). \n\n>  1. I'm curious why IntList.!__getitem!__ does not use the sage.misc.misc_c.normalize_index function to deal with slices.\u00a0 \n> How much of a performance penalty is there?\u00a0\n\nI'll switch to using normalize_index, since I'm not concerned with performance for list indexing, since everywhere that performance matters, I'm directly accessing the memory buffer (which is the only way to really compete with tightly coded C libraries).   So my updated patch will change to use normalize_index, unless there is a serious problem with doing so. \n\n>  Can this \"python semantics\" part be extracted out to be a more general \n> cdef'd counterpart to normalize_index, so that matrices, vectors, and other types can use it better to implement \n> !__getitem!__?\u00a0 \n\nPerhaps.  I'm certainly not doing so for this patch. \n\n> Also, as a future enhancement, it doesn't seem that much harder for !__setitem!__ to also \n> support slices.\u00a0 At the very least, the doctests for normalize_index probably ought to be \n> run on the !__getitem!__ function, as they exercise a number of corner cases for the python semantics.\n\nFortunately this won't be necessary since I'm switching to it. \n\n>  1. IntList.sum() does not have a doctest for the overflow case\n\nI can add that.   I like testing all corner cases.\n\nThanks for your helpful review of style...\n\n- William",
    "created_at": "2010-04-03T08:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77283",
    "user": "was"
}
```

Replying to [comment:10 jason]:
> Some notes from reading through the code looking at stylistic issues.  I really wish we had
>  line-by-line commenting like rietveld for this sort of thing.
> 
>  1. Lots of cdef'd functions do not have doctests.  I thought the policy from discussions on sage-devel 
> was that *every* function (including cdef functions) should have doctests (but, of course, these doctests
>  would have to either indirectly test the cdef'd function or would have to test a wrapper of the cdef function).  

We definitely do not require doctests for cdef'd methods.   The requirement is that "sage -coverage" returns a score of 100%.  This is clearly stated in the patch reviewers guide.    I did seriously consider them in this case, but literally every single one of these doctests would just be a literal *exact* copy of a doctest from elsewhere (!) but with # indirect doctest next to it.  There's just no value in that.   I could also make the methods cpdef, but that does incur a performance penalty -- in this case, it would be huge (which is totally unacceptable). 

> Some functions (_baum_welch_gamma, for example) don't even have docstrings.

I do think that all cdef'd methods should have docstrings, and will add docstrings to any that don't have them (in a part 2 patch). 

>  1. I'm curious why IntList.!__getitem!__ does not use the sage.misc.misc_c.normalize_index function to deal with slices.  
> How much of a performance penalty is there? 

I'll switch to using normalize_index, since I'm not concerned with performance for list indexing, since everywhere that performance matters, I'm directly accessing the memory buffer (which is the only way to really compete with tightly coded C libraries).   So my updated patch will change to use normalize_index, unless there is a serious problem with doing so. 

>  Can this "python semantics" part be extracted out to be a more general 
> cdef'd counterpart to normalize_index, so that matrices, vectors, and other types can use it better to implement 
> !__getitem!__?  

Perhaps.  I'm certainly not doing so for this patch. 

> Also, as a future enhancement, it doesn't seem that much harder for !__setitem!__ to also 
> support slices.  At the very least, the doctests for normalize_index probably ought to be 
> run on the !__getitem!__ function, as they exercise a number of corner cases for the python semantics.

Fortunately this won't be necessary since I'm switching to it. 

>  1. IntList.sum() does not have a doctest for the overflow case

I can add that.   I like testing all corner cases.

Thanks for your helpful review of style...

- William



---

archive/issue_comments_077284.json:
```json
{
    "body": "I got one numerical noise doctest failure on OS X 10.5.8:\n\nsage -t  devel/sage-t2/sage/stats/hmm/util.pyx\n**********************************************************************\nFile \"/Users/mh/sagestuff/sage-4.3.5/devel/sage-t2/sage/stats/hmm/util.pyx\", line 55:\n    sage: T.sum()\nExpected:\n    1.0                   \nGot:\n    0.99999999999999978\n\nI used this code in class yesterday (see http://wiki.sagemath.org/interact/stats#HiddenMarkovModel.3ATheOccasionallyDishonestCasino) and for that limited purpose it seemed fine.\n\nIt would be nice to have the forward and backward algorithms more exposed, but I don't think that needs to go into this ticket unless you feel like it.\n\nApart from the noise issue  I think can give this a positive review.",
    "created_at": "2010-04-03T14:37:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77284",
    "user": "mhampton"
}
```

I got one numerical noise doctest failure on OS X 10.5.8:

sage -t  devel/sage-t2/sage/stats/hmm/util.pyx
**********************************************************************
File "/Users/mh/sagestuff/sage-4.3.5/devel/sage-t2/sage/stats/hmm/util.pyx", line 55:
    sage: T.sum()
Expected:
    1.0                   
Got:
    0.99999999999999978

I used this code in class yesterday (see http://wiki.sagemath.org/interact/stats#HiddenMarkovModel.3ATheOccasionallyDishonestCasino) and for that limited purpose it seemed fine.

It would be nice to have the forward and backward algorithms more exposed, but I don't think that needs to go into this ticket unless you feel like it.

Apart from the noise issue  I think can give this a positive review.



---

archive/issue_comments_077285.json:
```json
{
    "body": "* I've attached a part 2 patch.   I made sure all cdef's methods have docstrings and also that doctests are properly sphinx formated (some weren't since they were copied from the old code). \n\n* Jason said above that IntList.sum doesn't have a doctest for the overflow case... but it does, so I don't know what he meant. \n \n* I read the source code for `sage.misc.misc_c.normalize_index` and cannot bring myself to use that in this situation.  That  function actually returns a Python *list* of Python ints for every single index into the list that is being sliced!  That would easily lead to factor of 50-100 slowdowns on realistic operations:\n\n```\nsage: timeit('z = sage.misc.misc_c.normalize_index(slice(1,10^5),10^5)')   # slow because constructions a big python list\n125 loops, best of 3: 2.17 ms per loop\nsage: a = stats.IntList([1..10^5])\nsage: timeit('a[1:10^5]')                       # slice is just a memcpy\n625 loops, best of 3: 48.4 \u00b5s per loop\nsage: 2.17/0.0484\n44.8347107438017\n```\n\nHere's an example with a step:\n\n```\nsage: a = stats.IntList([1..10^5])\nsage: timeit('a[1:10^5:2]')\n625 loops, best of 3: 92.2 \u00b5s per loop\nsage: timeit('z = sage.misc.misc_c.normalize_index(slice(1,10^5,2),10^5)')\n625 loops, best of 3: 772 \u00b5s per loop\n```\n\nand that 772 microseconds is *before* we do the actual iteration through the returned list of python ints, convert them to c ints, copy stuff around in memory, etc. \n\nThis stats code I'm writing is really meant to be industrial strength -- the sort of code maybe somebody would use in \"realtime\" processing of large datastreams.    I don't want slow functions anywhere in there. \n\n -- William",
    "created_at": "2010-04-08T21:47:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77285",
    "user": "was"
}
```

* I've attached a part 2 patch.   I made sure all cdef's methods have docstrings and also that doctests are properly sphinx formated (some weren't since they were copied from the old code). 

* Jason said above that IntList.sum doesn't have a doctest for the overflow case... but it does, so I don't know what he meant. 
 
* I read the source code for `sage.misc.misc_c.normalize_index` and cannot bring myself to use that in this situation.  That  function actually returns a Python *list* of Python ints for every single index into the list that is being sliced!  That would easily lead to factor of 50-100 slowdowns on realistic operations:

```
sage: timeit('z = sage.misc.misc_c.normalize_index(slice(1,10^5),10^5)')   # slow because constructions a big python list
125 loops, best of 3: 2.17 ms per loop
sage: a = stats.IntList([1..10^5])
sage: timeit('a[1:10^5]')                       # slice is just a memcpy
625 loops, best of 3: 48.4 µs per loop
sage: 2.17/0.0484
44.8347107438017
```

Here's an example with a step:

```
sage: a = stats.IntList([1..10^5])
sage: timeit('a[1:10^5:2]')
625 loops, best of 3: 92.2 µs per loop
sage: timeit('z = sage.misc.misc_c.normalize_index(slice(1,10^5,2),10^5)')
625 loops, best of 3: 772 µs per loop
```

and that 772 microseconds is *before* we do the actual iteration through the returned list of python ints, convert them to c ints, copy stuff around in memory, etc. 

This stats code I'm writing is really meant to be industrial strength -- the sort of code maybe somebody would use in "realtime" processing of large datastreams.    I don't want slow functions anywhere in there. 

 -- William



---

archive/issue_comments_077286.json:
```json
{
    "body": "part 2; apply this and the previous patch",
    "created_at": "2010-04-08T21:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77286",
    "user": "was"
}
```

part 2; apply this and the previous patch



---

archive/issue_comments_077287.json:
```json
{
    "body": "Attachment [trac_8547-take2-part2.patch](tarball://root/attachments/some-uuid/ticket8547/trac_8547-take2-part2.patch) by jason created at 2010-04-08 22:29:13\n\nReplying to [comment:13 was]:\n\n\n\n> * Jason said above that IntList.sum doesn't have a doctest for the overflow case... but it does, so I don't know what he meant. \n\n\nI meant that the doctest looks like this:\n\n\n```\nNote that there can be overflow, since the entries are C ints:: \n    sage: a = stats.IntList([2^30,2^30]); a \n    [1073741824, 1073741824] \n\n```\n\n\nThat's it.  There's no test there; you're just creating a list, not summing anything.\n\n\n>  \n> * I read the source code for `sage.misc.misc_c.normalize_index` and cannot bring myself to use that in this situation.  That  function actually returns a Python *list* of Python ints for every single index into the list that is being sliced!  That would easily lead to factor of 50-100 slowdowns on realistic operations:\n\n> This stats code I'm writing is really meant to be industrial strength -- the sort of code maybe somebody would use in \"realtime\" processing of large datastreams.    I don't want slow functions anywhere in there. \n\n\nI agree.",
    "created_at": "2010-04-08T22:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77287",
    "user": "jason"
}
```

Attachment [trac_8547-take2-part2.patch](tarball://root/attachments/some-uuid/ticket8547/trac_8547-take2-part2.patch) by jason created at 2010-04-08 22:29:13

Replying to [comment:13 was]:



> * Jason said above that IntList.sum doesn't have a doctest for the overflow case... but it does, so I don't know what he meant. 


I meant that the doctest looks like this:


```
Note that there can be overflow, since the entries are C ints:: 
    sage: a = stats.IntList([2^30,2^30]); a 
    [1073741824, 1073741824] 

```


That's it.  There's no test there; you're just creating a list, not summing anything.


>  
> * I read the source code for `sage.misc.misc_c.normalize_index` and cannot bring myself to use that in this situation.  That  function actually returns a Python *list* of Python ints for every single index into the list that is being sliced!  That would easily lead to factor of 50-100 slowdowns on realistic operations:

> This stats code I'm writing is really meant to be industrial strength -- the sort of code maybe somebody would use in "realtime" processing of large datastreams.    I don't want slow functions anywhere in there. 


I agree.



---

archive/issue_comments_077288.json:
```json
{
    "body": "Replying to [comment:14 jason]:\n> Replying to [comment:13 was]:\n> \n> \n> \n> > * Jason said above that IntList.sum doesn't have a doctest for the overflow case... but it does, so I don't know what he meant. \n> \n> \n> I meant that the doctest looks like this:\n> \n> {{{\n> Note that there can be overflow, since the entries are C ints:: \n>     sage: a = stats.IntList([2<sup>30,2</sup>30]); a \n>     [1073741824, 1073741824] \n> \n> }}}\n> \n> That's it.  There's no test there; you're just creating a list, not summing anything.\n> \n\nThanks for the clarification -- I was being dense; I've put up a part 3 that addresses this. \n\nSo, can I get a positive review now?",
    "created_at": "2010-04-10T19:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77288",
    "user": "was"
}
```

Replying to [comment:14 jason]:
> Replying to [comment:13 was]:
> 
> 
> 
> > * Jason said above that IntList.sum doesn't have a doctest for the overflow case... but it does, so I don't know what he meant. 
> 
> 
> I meant that the doctest looks like this:
> 
> {{{
> Note that there can be overflow, since the entries are C ints:: 
>     sage: a = stats.IntList([2<sup>30,2</sup>30]); a 
>     [1073741824, 1073741824] 
> 
> }}}
> 
> That's it.  There's no test there; you're just creating a list, not summing anything.
> 

Thanks for the clarification -- I was being dense; I've put up a part 3 that addresses this. 

So, can I get a positive review now?



---

archive/issue_comments_077289.json:
```json
{
    "body": "Attachment [trac_8547-take2-part3.patch](tarball://root/attachments/some-uuid/ticket8547/trac_8547-take2-part3.patch) by was created at 2010-04-10 19:19:10",
    "created_at": "2010-04-10T19:19:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77289",
    "user": "was"
}
```

Attachment [trac_8547-take2-part3.patch](tarball://root/attachments/some-uuid/ticket8547/trac_8547-take2-part3.patch) by was created at 2010-04-10 19:19:10



---

archive/issue_comments_077290.json:
```json
{
    "body": "OK, positive review.  I think this and basic_stats should be added to the reference manual, but that can be another ticket I guess.",
    "created_at": "2010-04-11T21:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77290",
    "user": "mhampton"
}
```

OK, positive review.  I think this and basic_stats should be added to the reference manual, but that can be another ticket I guess.



---

archive/issue_comments_077291.json:
```json
{
    "body": "Changing assignee from amhou to mhampton.",
    "created_at": "2010-04-11T21:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77291",
    "user": "mhampton"
}
```

Changing assignee from amhou to mhampton.



---

archive/issue_comments_077292.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-11T21:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77292",
    "user": "mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077293.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n- trac-8547-take2.patch\n- trac_8547-take2-part2.patch\n- trac_8547-take2-part3.patch",
    "created_at": "2010-04-16T18:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77293",
    "user": "jhpalmieri"
}
```

Merged in 4.4.alpha0:
- trac-8547-take2.patch
- trac_8547-take2-part2.patch
- trac_8547-take2-part3.patch



---

archive/issue_comments_077294.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8547#issuecomment-77294",
    "user": "jhpalmieri"
}
```

Resolution: fixed

# Issue 4973: rewrite the function __getitem__ in matrix0.pyx to not explicitly use the python/C api

archive/issues_004973.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @craigcitro\n\n`__getitem__` in matrix0.pyx uses C Python API and that code should have **never** been merged as is. The C API was used to get maximum speed. If possible rewrite this code to not use the C API, but it should not lose too much speed. This might be impossible or require adding bits to Cython.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4973\n\n",
    "created_at": "2009-01-14T09:30:10Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "rewrite the function __getitem__ in matrix0.pyx to not explicitly use the python/C api",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4973",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @craigcitro

CC:  @craigcitro

`__getitem__` in matrix0.pyx uses C Python API and that code should have **never** been merged as is. The C API was used to get maximum speed. If possible rewrite this code to not use the C API, but it should not lose too much speed. This might be impossible or require adding bits to Cython.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4973





---

archive/issue_comments_037802.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-14T10:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37802",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_037803.json:
```json
{
    "body": "Changing assignee from @craigcitro to @jasongrout.",
    "created_at": "2009-01-14T10:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37803",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @craigcitro to @jasongrout.



---

archive/issue_comments_037804.json:
```json
{
    "body": "Attachment [matrix-getitem.patch](tarball://root/attachments/some-uuid/ticket4973/matrix-getitem.patch) by @jasongrout created at 2009-01-14 12:05:17",
    "created_at": "2009-01-14T12:05:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37804",
    "user": "https://github.com/jasongrout"
}
```

Attachment [matrix-getitem.patch](tarball://root/attachments/some-uuid/ticket4973/matrix-getitem.patch) by @jasongrout created at 2009-01-14 12:05:17



---

archive/issue_comments_037805.json:
```json
{
    "body": "I didn't mean to mark this as needs review.  There are a few additions to the getitem syntax (like allowing negative indices) for which doctests need to be changed.  The main function should be about done, though.  More speed regression testing should be done as well.",
    "created_at": "2009-01-14T15:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37805",
    "user": "https://github.com/jasongrout"
}
```

I didn't mean to mark this as needs review.  There are a few additions to the getitem syntax (like allowing negative indices) for which doctests need to be changed.  The main function should be about done, though.  More speed regression testing should be done as well.



---

archive/issue_comments_037806.json:
```json
{
    "body": "Attachment [matrix-getitem.2.patch](tarball://root/attachments/some-uuid/ticket4973/matrix-getitem.2.patch) by @jasongrout created at 2009-01-15 04:05:55\n\nApply matrix-getitem.2.patch only.  This eliminates the C API calls, but keeps the speed, approximately (some cases are a bit slower, some are a bit faster).  This patch also adds more standard slicing functionality to getitem, which actually changes a few behaviors which went against python convention.  See the changed docstrings, for example.",
    "created_at": "2009-01-15T04:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37806",
    "user": "https://github.com/jasongrout"
}
```

Attachment [matrix-getitem.2.patch](tarball://root/attachments/some-uuid/ticket4973/matrix-getitem.2.patch) by @jasongrout created at 2009-01-15 04:05:55

Apply matrix-getitem.2.patch only.  This eliminates the C API calls, but keeps the speed, approximately (some cases are a bit slower, some are a bit faster).  This patch also adds more standard slicing functionality to getitem, which actually changes a few behaviors which went against python convention.  See the changed docstrings, for example.



---

archive/issue_events_011501.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2009-01-15T04:06:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4973#event-11501"
}
```



---

archive/issue_comments_037807.json:
```json
{
    "body": "Attachment [matrix-getitem.3.patch](tarball://root/attachments/some-uuid/ticket4973/matrix-getitem.3.patch) by @jasongrout created at 2009-01-15 06:19:59\n\napply only matrix-getitem.3.patch.  This patch replaces the call to normalize_slice with a standard python idiom for the same functionality.",
    "created_at": "2009-01-15T06:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37807",
    "user": "https://github.com/jasongrout"
}
```

Attachment [matrix-getitem.3.patch](tarball://root/attachments/some-uuid/ticket4973/matrix-getitem.3.patch) by @jasongrout created at 2009-01-15 06:19:59

apply only matrix-getitem.3.patch.  This patch replaces the call to normalize_slice with a standard python idiom for the same functionality.



---

archive/issue_comments_037808.json:
```json
{
    "body": "So I've reviewed Jason's patch, and everything looks good -- except that for lots of cases, in particular the primary `M[i,j]` use case, things are noticeably slower (on the order of 25%). This is no good on such a basic operation.\n\nThis code actually does **more** than the previous version (i.e. accepts additional types, negative indices, etc), and is still the same speed. \n\nCython doesn't quite do everything we want to get maximal speed out of this call. I'm going to submit another patch that uses it more judiciously, but gets yet more speed, because this is such an important piece of code.",
    "created_at": "2009-01-15T19:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37808",
    "user": "https://github.com/craigcitro"
}
```

So I've reviewed Jason's patch, and everything looks good -- except that for lots of cases, in particular the primary `M[i,j]` use case, things are noticeably slower (on the order of 25%). This is no good on such a basic operation.

This code actually does **more** than the previous version (i.e. accepts additional types, negative indices, etc), and is still the same speed. 

Cython doesn't quite do everything we want to get maximal speed out of this call. I'm going to submit another patch that uses it more judiciously, but gets yet more speed, because this is such an important piece of code.



---

archive/issue_comments_037809.json:
```json
{
    "body": "Attachment [trac-4973-pt2.patch](tarball://root/attachments/some-uuid/ticket4973/trac-4973-pt2.patch) by @craigcitro created at 2009-01-15 22:50:03\n\nNew version of the patch. So this adds one additional Python/C API call, but gets a 10% speedup for the case of `M[i,j]`, which I think is worthwhile. Furthermore, it's only necessary because this is a case where Cython doesn't do enough specific optimization for us -- one day, when Cython gets smarter, we can clean this up more.\n\nAlso fixed a bug in matrix indexing with tuples, and added a doctest for that case.",
    "created_at": "2009-01-15T22:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37809",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4973-pt2.patch](tarball://root/attachments/some-uuid/ticket4973/trac-4973-pt2.patch) by @craigcitro created at 2009-01-15 22:50:03

New version of the patch. So this adds one additional Python/C API call, but gets a 10% speedup for the case of `M[i,j]`, which I think is worthwhile. Furthermore, it's only necessary because this is a case where Cython doesn't do enough specific optimization for us -- one day, when Cython gets smarter, we can clean this up more.

Also fixed a bug in matrix indexing with tuples, and added a doctest for that case.



---

archive/issue_comments_037810.json:
```json
{
    "body": "As a note, the patches to be applied, in order:\n\n* `matrix-getitem.3.patch`\n* `trac-4973-pt2.patch`",
    "created_at": "2009-01-15T22:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37810",
    "user": "https://github.com/craigcitro"
}
```

As a note, the patches to be applied, in order:

* `matrix-getitem.3.patch`
* `trac-4973-pt2.patch`



---

archive/issue_comments_037811.json:
```json
{
    "body": "Doctests pass. I've tried lots of the doc examples and they are faster or the same as the old code, except for the following case.  These commands are each executed in a fresh Sage session.\n\n\n```\n\nAFTER PATCH:\n\nsage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 167 \u00b5s per loop\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 168 \u00b5s per loop\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 166 \u00b5s per loop\n\n\nBEFORE PATCH:\n\nsage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 134 \u00b5s per loop\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 138 \u00b5s per loop\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 143 \u00b5s per loop\n```\n\n\nSo, positive review if this regression is fixed.",
    "created_at": "2009-01-16T01:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37811",
    "user": "https://github.com/jasongrout"
}
```

Doctests pass. I've tried lots of the doc examples and they are faster or the same as the old code, except for the following case.  These commands are each executed in a fresh Sage session.


```

AFTER PATCH:

sage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 167 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 168 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 166 µs per loop


BEFORE PATCH:

sage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 134 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 138 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 143 µs per loop
```


So, positive review if this regression is fixed.



---

archive/issue_comments_037812.json:
```json
{
    "body": "Attachment [trac-4973-pt3.patch](tarball://root/attachments/some-uuid/ticket4973/trac-4973-pt3.patch) by @craigcitro created at 2009-01-16 02:13:06\n\nPatch attached that fixes the regression (at least on my machine).",
    "created_at": "2009-01-16T02:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37812",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4973-pt3.patch](tarball://root/attachments/some-uuid/ticket4973/trac-4973-pt3.patch) by @craigcitro created at 2009-01-16 02:13:06

Patch attached that fixes the regression (at least on my machine).



---

archive/issue_comments_037813.json:
```json
{
    "body": "Okay, pt3 fixes the regression.  Here are my new timings:\n\n\n```\nAFTER PATCH:\n\nsage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 167 \u00b5s per loop\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 168 \u00b5s per loop\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 166 \u00b5s per loop\n\n\nBEFORE PATCH:\n\nsage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 134 \u00b5s per loop\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 138 \u00b5s per loop\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 143 \u00b5s per loop\n```\n\n\nSo we're faster than the original code again.\n\nGreat job. Positive review, with the doctest fix that I'm going to post in a second.  I presume that mabshoff will run all doctests on it to make sure that there are no errors in other code because of the additional capabilities.",
    "created_at": "2009-01-16T02:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37813",
    "user": "https://github.com/jasongrout"
}
```

Okay, pt3 fixes the regression.  Here are my new timings:


```
AFTER PATCH:

sage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 167 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 168 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 166 µs per loop


BEFORE PATCH:

sage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 134 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 138 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 143 µs per loop
```


So we're faster than the original code again.

Great job. Positive review, with the doctest fix that I'm going to post in a second.  I presume that mabshoff will run all doctests on it to make sure that there are no errors in other code because of the additional capabilities.



---

archive/issue_comments_037814.json:
```json
{
    "body": "apply on top of previous patch",
    "created_at": "2009-01-16T02:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37814",
    "user": "https://github.com/jasongrout"
}
```

apply on top of previous patch



---

archive/issue_comments_037815.json:
```json
{
    "body": "Attachment [doctest-fix.patch](tarball://root/attachments/some-uuid/ticket4973/doctest-fix.patch) by @jasongrout created at 2009-01-16 02:24:52",
    "created_at": "2009-01-16T02:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37815",
    "user": "https://github.com/jasongrout"
}
```

Attachment [doctest-fix.patch](tarball://root/attachments/some-uuid/ticket4973/doctest-fix.patch) by @jasongrout created at 2009-01-16 02:24:52



---

archive/issue_comments_037816.json:
```json
{
    "body": "I mean, *here* are my new timings after the regression fix in pt3.patch:\n\n\n```\nAFTER PATCH:\n\nsage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 167 \u00b5s per loop\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 168 \u00b5s per loop\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 166 \u00b5s per loop\n\n\nBEFORE PATCH:\n\nsage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 134 \u00b5s per loop\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 138 \u00b5s per loop\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 143 \u00b5s per loop\n```\n\n\nI copied the wrong thing before.",
    "created_at": "2009-01-16T02:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37816",
    "user": "https://github.com/jasongrout"
}
```

I mean, *here* are my new timings after the regression fix in pt3.patch:


```
AFTER PATCH:

sage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 167 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 168 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 166 µs per loop


BEFORE PATCH:

sage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 134 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 138 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 143 µs per loop
```


I copied the wrong thing before.



---

archive/issue_comments_037817.json:
```json
{
    "body": "Grrr, apparently I again copied the wrong thing.  So much for middle-click vs. ctrl-v.\n\n*here* are the new timings:\n\n\n```\nsage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 125 \u00b5s per loop\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 120 \u00b5s per loop\nsage: timeit('M[[1,2],[0,1,2]]')\n625 loops, best of 3: 124 \u00b5s per loop\n```\n",
    "created_at": "2009-01-16T02:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37817",
    "user": "https://github.com/jasongrout"
}
```

Grrr, apparently I again copied the wrong thing.  So much for middle-click vs. ctrl-v.

*here* are the new timings:


```
sage: m=[(1, -2, -1, -1,9), (1, 8, 6, 2,2), (1, 1, -1, 1,4), (-1, 2, -2, -1,4)];M= matrix(m)
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 125 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 120 µs per loop
sage: timeit('M[[1,2],[0,1,2]]')
625 loops, best of 3: 124 µs per loop
```




---

archive/issue_comments_037818.json:
```json
{
    "body": "BTW, now it's even faster to write\n\n\n```\nrow_index, col_index = key_tuple\n```\n\n\nThen \n\n\n```\nrow_index = key_tuple[0] \ncol_index = key_tuple[1]\n```\n",
    "created_at": "2009-01-16T19:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37818",
    "user": "https://github.com/robertwb"
}
```

BTW, now it's even faster to write


```
row_index, col_index = key_tuple
```


Then 


```
row_index = key_tuple[0] 
col_index = key_tuple[1]
```




---

archive/issue_comments_037819.json:
```json
{
    "body": "Though do either of those keep up with directly using `PyTuple_GET_ITEM`? I didn't think they did based on my timings, but I'd be happy to find out otherwise.",
    "created_at": "2009-01-16T20:00:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37819",
    "user": "https://github.com/craigcitro"
}
```

Though do either of those keep up with directly using `PyTuple_GET_ITEM`? I didn't think they did based on my timings, but I'd be happy to find out otherwise.



---

archive/issue_comments_037820.json:
```json
{
    "body": "Here's the actual generated code for `x,y = t`\n\n\n```\n    if (PyTuple_CheckExact(__pyx_v_t) && PyTuple_GET_SIZE(__pyx_v_t) == 2) {\n    PyObject* tuple = __pyx_v_t;\n    __pyx_2 = PyTuple_GET_ITEM(tuple, 0);\n    Py_INCREF(__pyx_2);\n    Py_DECREF(__pyx_v_x);\n    __pyx_v_x = __pyx_2;\n    __pyx_2 = 0;\n    __pyx_2 = PyTuple_GET_ITEM(tuple, 1);\n    Py_INCREF(__pyx_2);\n    Py_DECREF(__pyx_v_y);\n    __pyx_v_y = __pyx_2;\n    __pyx_2 = 0;\n  }\n  else {\n     [generic code]\n  }\n```\n\n\nIf `t` is declared to be a tuple, half of the first check shouldn't be needed (I don't think this optimization is in place yet). So it should be as fast as type check + length check + PyTuple_GET_ITEM. In any case, it's faster than indexing not using PyTyple_GET_ITEM.",
    "created_at": "2009-01-16T20:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37820",
    "user": "https://github.com/robertwb"
}
```

Here's the actual generated code for `x,y = t`


```
    if (PyTuple_CheckExact(__pyx_v_t) && PyTuple_GET_SIZE(__pyx_v_t) == 2) {
    PyObject* tuple = __pyx_v_t;
    __pyx_2 = PyTuple_GET_ITEM(tuple, 0);
    Py_INCREF(__pyx_2);
    Py_DECREF(__pyx_v_x);
    __pyx_v_x = __pyx_2;
    __pyx_2 = 0;
    __pyx_2 = PyTuple_GET_ITEM(tuple, 1);
    Py_INCREF(__pyx_2);
    Py_DECREF(__pyx_v_y);
    __pyx_v_y = __pyx_2;
    __pyx_2 = 0;
  }
  else {
     [generic code]
  }
```


If `t` is declared to be a tuple, half of the first check shouldn't be needed (I don't think this optimization is in place yet). So it should be as fast as type check + length check + PyTuple_GET_ITEM. In any case, it's faster than indexing not using PyTyple_GET_ITEM.



---

archive/issue_comments_037821.json:
```json
{
    "body": "Ah, excellent. In this particular case, we've just done both of those checks -- the typecheck and the length check -- so I'm going to say we should stick with the `PyTuple_GET_ITEM` (we also raise an explicit exception if the length is wrong), but I'm happy to know that in general, Cython generates such good code.\n\nIt'd be nice if Cython skipped the typecheck when it knew the type -- should a ticket be filed on the Cython trac server?",
    "created_at": "2009-01-17T21:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37821",
    "user": "https://github.com/craigcitro"
}
```

Ah, excellent. In this particular case, we've just done both of those checks -- the typecheck and the length check -- so I'm going to say we should stick with the `PyTuple_GET_ITEM` (we also raise an explicit exception if the length is wrong), but I'm happy to know that in general, Cython generates such good code.

It'd be nice if Cython skipped the typecheck when it knew the type -- should a ticket be filed on the Cython trac server?



---

archive/issue_comments_037822.json:
```json
{
    "body": "Sounds like a good course of action for now. \n\nYes, that should be a ticket on the Cython trac.",
    "created_at": "2009-01-17T21:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37822",
    "user": "https://github.com/robertwb"
}
```

Sounds like a good course of action for now. 

Yes, that should be a ticket on the Cython trac.



---

archive/issue_events_011502.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-18T14:44:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4973#event-11502"
}
```



---

archive/issue_comments_037823.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-18T14:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37823",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037824.json:
```json
{
    "body": "Merged\n\n* matrix-getitem.3.patch\n* trac-4973-pt2.patch\n* trac-4973-pt3.patch\n* doctest-fix.patch \n\nin Sage 3.3.alpha0\n\nCheers,\n\nMichael",
    "created_at": "2009-01-18T14:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4973#issuecomment-37824",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged

* matrix-getitem.3.patch
* trac-4973-pt2.patch
* trac-4973-pt3.patch
* doctest-fix.patch 

in Sage 3.3.alpha0

Cheers,

Michael

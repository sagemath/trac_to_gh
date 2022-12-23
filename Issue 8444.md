# Issue 8444: Memleak in conversion for univariate polynomial rings

archive/issues_008444.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: univariate polynomial ring coercion\n\nAt [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/a145a02c8d379b11), Ben Linowitz reported a problem with memory. Apparently it boils down to the following problem:\n\n\n```\nsage: R.<x> = QQ[]\nsage: M = get_memory_usage()\nsage: for n in range(50000):\n....:     Mnew = get_memory_usage()\n....:     if Mnew > M:\n....:         print n, Mnew-M\n....:         M=Mnew\n....:     a = R(1)\n....:\n0 1.51171875\n6673 0.12890625\n8785 0.12890625\n10897 0.12890625\n13009 0.12890625\n15121 0.12890625\n17233 0.12890625\n19345 0.12890625\n21457 0.12890625\n23569 0.12890625\n25681 0.12890625\n27793 0.12890625\n29905 0.12890625\n32017 0.12890625\n34129 0.12890625\n36241 0.12890625\n38353 0.12890625\n40465 0.12890625\n42577 0.12890625\n44689 0.12890625\n46801 0.12890625\n48913 0.12890625\n```\n\nThis is with sage 4.3.3 on sage.math.\n\nSo, the first 6673 everything is good. Then, after 2112 rounds there is a leak of (if I did not miscompute) 135168 Byte.\n\nThis does not occur for multivariate rings:\n\n\n```\nsage: R.<x,y> = QQ[]\nsage: M = get_memory_usage()\nsage: for n in range(50000):\n....:     Mnew = get_memory_usage()\n....:     if Mnew > M:\n....:         print n, Mnew-M\n....:         M=Mnew\n....:     a = R(1)\n....:\n0 1.5\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8444\n\n",
    "created_at": "2010-03-05T12:41:29Z",
    "labels": [
        "memleak",
        "major",
        "bug"
    ],
    "title": "Memleak in conversion for univariate polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8444",
    "user": "SimonKing"
}
```
Assignee: tbd

Keywords: univariate polynomial ring coercion

At [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/a145a02c8d379b11), Ben Linowitz reported a problem with memory. Apparently it boils down to the following problem:


```
sage: R.<x> = QQ[]
sage: M = get_memory_usage()
sage: for n in range(50000):
....:     Mnew = get_memory_usage()
....:     if Mnew > M:
....:         print n, Mnew-M
....:         M=Mnew
....:     a = R(1)
....:
0 1.51171875
6673 0.12890625
8785 0.12890625
10897 0.12890625
13009 0.12890625
15121 0.12890625
17233 0.12890625
19345 0.12890625
21457 0.12890625
23569 0.12890625
25681 0.12890625
27793 0.12890625
29905 0.12890625
32017 0.12890625
34129 0.12890625
36241 0.12890625
38353 0.12890625
40465 0.12890625
42577 0.12890625
44689 0.12890625
46801 0.12890625
48913 0.12890625
```

This is with sage 4.3.3 on sage.math.

So, the first 6673 everything is good. Then, after 2112 rounds there is a leak of (if I did not miscompute) 135168 Byte.

This does not occur for multivariate rings:


```
sage: R.<x,y> = QQ[]
sage: M = get_memory_usage()
sage: for n in range(50000):
....:     Mnew = get_memory_usage()
....:     if Mnew > M:
....:         print n, Mnew-M
....:         M=Mnew
....:     a = R(1)
....:
0 1.5
```


Issue created by migration from https://trac.sagemath.org/ticket/8444





---

archive/issue_comments_075913.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-03-05T14:32:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8444#issuecomment-75913",
    "user": "mhampton"
}
```

Changing priority from major to critical.



---

archive/issue_comments_075914.json:
```json
{
    "body": "Sage-4.3.3 does not have this problem on my mac running 10.6.2.",
    "created_at": "2010-03-05T22:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8444#issuecomment-75914",
    "user": "mhampton"
}
```

Sage-4.3.3 does not have this problem on my mac running 10.6.2.



---

archive/issue_comments_075915.json:
```json
{
    "body": "For the record:\n\nGonzalo Tornaria stated at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/6de8c4287495d9d3):\n\n  \"I think this is caused by a duplicate _sig_on in the bottom part of\n\npari.`__call__`.\"",
    "created_at": "2010-03-05T23:24:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8444#issuecomment-75915",
    "user": "SimonKing"
}
```

For the record:

Gonzalo Tornaria stated at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/6de8c4287495d9d3):

  "I think this is caused by a duplicate _sig_on in the bottom part of

pari.`__call__`."



---

archive/issue_comments_075916.json:
```json
{
    "body": "Attachment\n\nfix memory leak due to dup call to _sig_on",
    "created_at": "2010-03-11T04:33:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8444#issuecomment-75916",
    "user": "tornaria"
}
```

Attachment

fix memory leak due to dup call to _sig_on



---

archive/issue_comments_075917.json:
```json
{
    "body": "Changing keywords from \"univariate polynomial ring coercion\" to \"univariate polynomial ring coercion, pari, sig_on\".",
    "created_at": "2010-03-11T04:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8444#issuecomment-75917",
    "user": "tornaria"
}
```

Changing keywords from "univariate polynomial ring coercion" to "univariate polynomial ring coercion, pari, sig_on".



---

archive/issue_comments_075918.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-11T04:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8444#issuecomment-75918",
    "user": "tornaria"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075919.json:
```json
{
    "body": "The attached patch seems to fix the memleak. I worked on top of 4.3.3; all tests pass with this patch, and the snippet in the ticket description goes through without extra allocations:\n\n```\nsage: R.<x> = QQ[]\nsage: M = get_memory_usage()\nsage: for n in range(50000):\n....:     Mnew = get_memory_usage()\n....:     if Mnew > M:\n....:         print n, Mnew-M\n....:         M=Mnew\n....:     a = R(1)\n....:     \n0 1.6015625\nsage: \n```\n\n\nHere's the full commit log which explains the patch:\n\n#8444: fix memory leak due to dup call to `_sig_on` in the bottom part of `PariInstance.__call__`\n\nAt the bottom of `PariInstance.__call__` both `_sig_on` (first) and `_sig_str`\n(later) are used. In fact, both count as calls to `_sig_on` (actually `_sig_on` is\nequivalent to `_sig_str(NULL)`) and these are *not* reentrant, i.e. nesting is not\nsupported (anyway, there's only one implicit `_sig_off` in the call to new_gen).\n\nA double `_sig_on`, as defined in `interrupt.h`, is usually equivalent to a single\none -- however, for the pari library these macros are overrided as `_pari_sig_on`\n(defined in `misc.h` and `pari_err.h`) adding a call to pari's own error catching\nfunction.  Calling the `err_catch()` function twice without the corresponding\ncall to `err_leave()` results in a memory leak which is reported in #8444.\n\nThe patch is one-liner: removing the first `_sig_on` fixes the memory leak.\n\nNote: this line was added by changeset `10536:423520e7d069` as part of a large\neffort to add lots of missing calls to `_sig_on` in pari interface. However, I\nthink in this case it was just an oversight because the already existing call to\n`_sig_on` was only implicit in the call to `_sig_str`.",
    "created_at": "2010-03-11T04:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8444#issuecomment-75919",
    "user": "tornaria"
}
```

The attached patch seems to fix the memleak. I worked on top of 4.3.3; all tests pass with this patch, and the snippet in the ticket description goes through without extra allocations:

```
sage: R.<x> = QQ[]
sage: M = get_memory_usage()
sage: for n in range(50000):
....:     Mnew = get_memory_usage()
....:     if Mnew > M:
....:         print n, Mnew-M
....:         M=Mnew
....:     a = R(1)
....:     
0 1.6015625
sage: 
```


Here's the full commit log which explains the patch:

#8444: fix memory leak due to dup call to `_sig_on` in the bottom part of `PariInstance.__call__`

At the bottom of `PariInstance.__call__` both `_sig_on` (first) and `_sig_str`
(later) are used. In fact, both count as calls to `_sig_on` (actually `_sig_on` is
equivalent to `_sig_str(NULL)`) and these are *not* reentrant, i.e. nesting is not
supported (anyway, there's only one implicit `_sig_off` in the call to new_gen).

A double `_sig_on`, as defined in `interrupt.h`, is usually equivalent to a single
one -- however, for the pari library these macros are overrided as `_pari_sig_on`
(defined in `misc.h` and `pari_err.h`) adding a call to pari's own error catching
function.  Calling the `err_catch()` function twice without the corresponding
call to `err_leave()` results in a memory leak which is reported in #8444.

The patch is one-liner: removing the first `_sig_on` fixes the memory leak.

Note: this line was added by changeset `10536:423520e7d069` as part of a large
effort to add lots of missing calls to `_sig_on` in pari interface. However, I
think in this case it was just an oversight because the already existing call to
`_sig_on` was only implicit in the call to `_sig_str`.



---

archive/issue_comments_075920.json:
```json
{
    "body": "Dear Gonzalo,\n\ngreat work! It is very important to fix such issues, thanks a lot.\n\nPaul",
    "created_at": "2010-03-15T21:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8444#issuecomment-75920",
    "user": "zimmerma"
}
```

Dear Gonzalo,

great work! It is very important to fix such issues, thanks a lot.

Paul



---

archive/issue_comments_075921.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-15T21:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8444#issuecomment-75921",
    "user": "zimmerma"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075922.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8444#issuecomment-75922",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_075923.json:
```json
{
    "body": "Merged \"trac_8444.fix_pari_memleak.patch\" into 4.4.alpha0.",
    "created_at": "2010-04-15T23:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8444",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8444#issuecomment-75923",
    "user": "jhpalmieri"
}
```

Merged "trac_8444.fix_pari_memleak.patch" into 4.4.alpha0.

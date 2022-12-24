# Issue 5800: Nice wrapper for bitset

archive/issues_005800.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @robertwb @mwhansen @rlmill mvngu\n\nbitset.pxi provides a set of inline functions for dealing with bitsets. It would be nice to wrap this in a C class with automatic memory management for ease of use as well as testing. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5800\n\n",
    "created_at": "2009-04-16T05:01:03Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Nice wrapper for bitset",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5800",
    "user": "@robertwb"
}
```
Assignee: cwitty

CC:  @robertwb @mwhansen @rlmill mvngu

bitset.pxi provides a set of inline functions for dealing with bitsets. It would be nice to wrap this in a C class with automatic memory management for ease of use as well as testing. 

Issue created by migration from https://trac.sagemath.org/ticket/5800





---

archive/issue_comments_045523.json:
```json
{
    "body": "Also, hopefully it could all be moved into a .pxd rather than a .pxi now that .pxds support inline functions.",
    "created_at": "2009-04-16T05:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45523",
    "user": "@robertwb"
}
```

Also, hopefully it could all be moved into a .pxd rather than a .pxi now that .pxds support inline functions.



---

archive/issue_comments_045524.json:
```json
{
    "body": "I tried to move it all into a pxd, but the default arguments for several functions prevented that.  It's probably not a huge obstacle, though.  It was just the string printing functions, so nothing crucial.",
    "created_at": "2009-04-16T07:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45524",
    "user": "@jasongrout"
}
```

I tried to move it all into a pxd, but the default arguments for several functions prevented that.  It's probably not a huge obstacle, though.  It was just the string printing functions, so nothing crucial.



---

archive/issue_comments_045525.json:
```json
{
    "body": "See http://trac.cython.org/cython_trac/ticket/283",
    "created_at": "2009-04-16T07:35:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45525",
    "user": "@robertwb"
}
```

See http://trac.cython.org/cython_trac/ticket/283



---

archive/issue_comments_045526.json:
```json
{
    "body": "The patch doesn't do automatic memory management yet.",
    "created_at": "2009-05-15T10:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45526",
    "user": "@jasongrout"
}
```

The patch doesn't do automatic memory management yet.



---

archive/issue_comments_045527.json:
```json
{
    "body": "I'd like to see the size be arbitrary, i.e. it acts like an infinite (dense) bitset and grows as needed.",
    "created_at": "2009-05-15T10:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45527",
    "user": "@robertwb"
}
```

I'd like to see the size be arbitrary, i.e. it acts like an infinite (dense) bitset and grows as needed.



---

archive/issue_comments_045528.json:
```json
{
    "body": "Yep, that's part of the reason it is still [needs work]",
    "created_at": "2009-05-15T11:04:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45528",
    "user": "@jasongrout"
}
```

Yep, that's part of the reason it is still [needs work]



---

archive/issue_comments_045529.json:
```json
{
    "body": "Changing assignee from cwitty to @jasongrout.",
    "created_at": "2009-09-29T05:51:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45529",
    "user": "@jasongrout"
}
```

Changing assignee from cwitty to @jasongrout.



---

archive/issue_comments_045530.json:
```json
{
    "body": "doctests need to be added to the functions.",
    "created_at": "2009-09-29T07:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45530",
    "user": "@jasongrout"
}
```

doctests need to be added to the functions.



---

archive/issue_comments_045531.json:
```json
{
    "body": "Timings:\n\n\n```\nsage: a=Bitset([3*i for i in range(100)])\nsage: b=Bitset([4*i for i in range(100)])\nsage: d=set([4*i for i in range(100)])\nsage: c=set([3*i for i in range(100)])\nsage: %timeit a|b\n1000000 loops, best of 3: 1.55 \u00b5s per loop\nsage: %timeit c|d\n100000 loops, best of 3: 17.6 \u00b5s per loop\nsage: %timeit a-b\n100000 loops, best of 3: 1.53 \u00b5s per loop\nsage: %timeit c-d\n100000 loops, best of 3: 10.4 \u00b5s per loop\n```\n\n\nSo I guess we have a pretty good data structure.  And this is even accessing it with python!",
    "created_at": "2009-10-16T11:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45531",
    "user": "@jasongrout"
}
```

Timings:


```
sage: a=Bitset([3*i for i in range(100)])
sage: b=Bitset([4*i for i in range(100)])
sage: d=set([4*i for i in range(100)])
sage: c=set([3*i for i in range(100)])
sage: %timeit a|b
1000000 loops, best of 3: 1.55 µs per loop
sage: %timeit c|d
100000 loops, best of 3: 17.6 µs per loop
sage: %timeit a-b
100000 loops, best of 3: 1.53 µs per loop
sage: %timeit c-d
100000 loops, best of 3: 10.4 µs per loop
```


So I guess we have a pretty good data structure.  And this is even accessing it with python!



---

archive/issue_comments_045532.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-16T11:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45532",
    "user": "@jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_045533.json:
```json
{
    "body": "Okay, this is a big rewrite of this patch.  Things should be good now; timings are great compared to python set/frozenset operations too.\n\nI need this functionality in Sage for some research code I'm writing (and contributing soon), so if you have a minute to review it, that would be fantastic!",
    "created_at": "2009-10-16T11:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45533",
    "user": "@jasongrout"
}
```

Okay, this is a big rewrite of this patch.  Things should be good now; timings are great compared to python set/frozenset operations too.

I need this functionality in Sage for some research code I'm writing (and contributing soon), so if you have a minute to review it, that would be fantastic!



---

archive/issue_comments_045534.json:
```json
{
    "body": "CCing some more people that would be great reviewers.",
    "created_at": "2009-10-16T11:34:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45534",
    "user": "@jasongrout"
}
```

CCing some more people that would be great reviewers.



---

archive/issue_comments_045535.json:
```json
{
    "body": "Attachment [trac-5800-bitset-class.patch](tarball://root/attachments/some-uuid/ticket5800/trac-5800-bitset-class.patch) by @jasongrout created at 2009-10-16 11:45:37",
    "created_at": "2009-10-16T11:45:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45535",
    "user": "@jasongrout"
}
```

Attachment [trac-5800-bitset-class.patch](tarball://root/attachments/some-uuid/ticket5800/trac-5800-bitset-class.patch) by @jasongrout created at 2009-10-16 11:45:37



---

archive/issue_comments_045536.json:
```json
{
    "body": "For the most part looks good. I'd like to see some more examples of binary operations between (much) differently sized operands, and perhaps some greater than word length ones.",
    "created_at": "2009-10-22T03:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45536",
    "user": "@robertwb"
}
```

For the most part looks good. I'd like to see some more examples of binary operations between (much) differently sized operands, and perhaps some greater than word length ones.



---

archive/issue_comments_045537.json:
```json
{
    "body": "The second patch adds lots of doctests with different set sizes (and double-checking with the python builtin set type).  It also adds an iter function that allows one to do list(b) for a bitset b.",
    "created_at": "2009-10-22T22:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45537",
    "user": "@jasongrout"
}
```

The second patch adds lots of doctests with different set sizes (and double-checking with the python builtin set type).  It also adds an iter function that allows one to do list(b) for a bitset b.



---

archive/issue_comments_045538.json:
```json
{
    "body": "apply on top of previous patch",
    "created_at": "2009-10-23T00:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45538",
    "user": "@jasongrout"
}
```

apply on top of previous patch



---

archive/issue_comments_045539.json:
```json
{
    "body": "Attachment [trac-5800-bitset-class-docs.patch](tarball://root/attachments/some-uuid/ticket5800/trac-5800-bitset-class-docs.patch) by @jasongrout created at 2009-10-23 00:47:51\n\nApologies: that last patch had a bit of another unrelated patch in it.  I've just uploaded the corrected patch.",
    "created_at": "2009-10-23T00:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45539",
    "user": "@jasongrout"
}
```

Attachment [trac-5800-bitset-class-docs.patch](tarball://root/attachments/some-uuid/ticket5800/trac-5800-bitset-class-docs.patch) by @jasongrout created at 2009-10-23 00:47:51

Apologies: that last patch had a bit of another unrelated patch in it.  I've just uploaded the corrected patch.



---

archive/issue_comments_045540.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-27T18:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45540",
    "user": "@robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_045541.json:
```json
{
    "body": "Looks good, thanks for finally wrapping this up.",
    "created_at": "2009-10-27T18:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45541",
    "user": "@robertwb"
}
```

Looks good, thanks for finally wrapping this up.



---

archive/issue_comments_045542.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T05:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5800",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5800#issuecomment-45542",
    "user": "@mwhansen"
}
```

Resolution: fixed

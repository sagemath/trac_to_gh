# Issue 6766: faster powers of factorizations

archive/issues_006766.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @JohnCremona\n\nThe patch provides a much faster method for computing powers of commutative factorizations.  This implements a suggestion made by John Cremona in #5188. \nThe speed-up is most marked for factorizations of ideals in number fields.\nBefore:\n\n```\nsage: f = NumberField(x^2 + 23, 'a').factor(47)\nsage: timeit('f^10')\n5 loops, best of 3: 134 ms per loop\n```\n\nAfter:\n\n```\nsage: f = NumberField(x^2 + 23, 'a').factor(47)\nsage: timeit('f^10')\n625 loops, best of 3: 571 \u00b5s per loop\n```\n\n\nIn addition, five redundant lines have been removed from the `__init__` function of the `Factorization` class.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6766\n\n",
    "created_at": "2009-08-16T21:08:14Z",
    "labels": [
        "component: algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "faster powers of factorizations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6766",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```
Assignee: tbd

CC:  @JohnCremona

The patch provides a much faster method for computing powers of commutative factorizations.  This implements a suggestion made by John Cremona in #5188. 
The speed-up is most marked for factorizations of ideals in number fields.
Before:

```
sage: f = NumberField(x^2 + 23, 'a').factor(47)
sage: timeit('f^10')
5 loops, best of 3: 134 ms per loop
```

After:

```
sage: f = NumberField(x^2 + 23, 'a').factor(47)
sage: timeit('f^10')
625 loops, best of 3: 571 µs per loop
```


In addition, five redundant lines have been removed from the `__init__` function of the `Factorization` class.



Issue created by migration from https://trac.sagemath.org/ticket/6766





---

archive/issue_comments_055628.json:
```json
{
    "body": "Attachment [trac_6766.patch](tarball://root/attachments/some-uuid/ticket6766/trac_6766.patch) by mvngu created at 2009-08-16 22:36:52\n\nHi Francis. After uploading a patch for a ticket, you should change the subject to \"[with patch, needs review]\". That way, the ticket can be picked up by the relevant trac report as needing review.",
    "created_at": "2009-08-16T22:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6766#issuecomment-55628",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6766.patch](tarball://root/attachments/some-uuid/ticket6766/trac_6766.patch) by mvngu created at 2009-08-16 22:36:52

Hi Francis. After uploading a patch for a ticket, you should change the subject to "[with patch, needs review]". That way, the ticket can be picked up by the relevant trac report as needing review.



---

archive/issue_comments_055629.json:
```json
{
    "body": "This looks good to me;  it applies fine to 4.1.1.  I only tested the file which was changed.",
    "created_at": "2009-08-18T16:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6766#issuecomment-55629",
    "user": "https://github.com/JohnCremona"
}
```

This looks good to me;  it applies fine to 4.1.1.  I only tested the file which was changed.



---

archive/issue_comments_055630.json:
```json
{
    "body": "It would be nice if there are more code to illustrate timings before and after applying the patch. As I see it, the patch claims to optimize an operation and Francis has provided one example. Is it possible to provide some more examples of before and after timing statistics? Such examples goes very well with release tours, in which features are being showcased.",
    "created_at": "2009-08-18T16:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6766#issuecomment-55630",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

It would be nice if there are more code to illustrate timings before and after applying the patch. As I see it, the patch claims to optimize an operation and Francis has provided one example. Is it possible to provide some more examples of before and after timing statistics? Such examples goes very well with release tours, in which features are being showcased.



---

archive/issue_comments_055631.json:
```json
{
    "body": "Replying to [comment:3 mvngu]:\n> It would be nice if there are more code to illustrate timings before and after applying the patch. As I see it, the patch claims to optimize an operation and Francis has provided one example. Is it possible to provide some more examples of before and after timing statistics? Such examples goes very well with release tours, in which features are being showcased.\n\nI'm not sure this is really worth it in this case.  Before a stupid method was used (by default) while now a sensible one is.  But on the other hand there are not that many situations where one needs to raise a factoization to a power anyway, so I would not want to make a big issue of this in release notes! [This is not to diminish the credit to Francis for bothering to do the job, of course!]",
    "created_at": "2009-08-18T20:21:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6766#issuecomment-55631",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:3 mvngu]:
> It would be nice if there are more code to illustrate timings before and after applying the patch. As I see it, the patch claims to optimize an operation and Francis has provided one example. Is it possible to provide some more examples of before and after timing statistics? Such examples goes very well with release tours, in which features are being showcased.

I'm not sure this is really worth it in this case.  Before a stupid method was used (by default) while now a sensible one is.  But on the other hand there are not that many situations where one needs to raise a factoization to a power anyway, so I would not want to make a big issue of this in release notes! [This is not to diminish the credit to Francis for bothering to do the job, of course!]



---

archive/issue_comments_055632.json:
```json
{
    "body": "I agree with John's comments, but  for the record: before (4.1.1)\n\n```\nsage: f = factor(120)\nsage: for i in range(10): timeit('f^(2^%s)' % i)\n....: \n625 loops, best of 3: 80.1 \u00b5s per loop\n625 loops, best of 3: 538 \u00b5s per loop\n625 loops, best of 3: 1.03 ms per loop\n125 loops, best of 3: 1.5 ms per loop\n125 loops, best of 3: 1.93 ms per loop\n125 loops, best of 3: 2.39 ms per loop\n125 loops, best of 3: 2.81 ms per loop\n125 loops, best of 3: 3.23 ms per loop\n125 loops, best of 3: 3.7 ms per loop\n125 loops, best of 3: 4.12 ms per loop\n```\n\nand after (4.1.1 + patch)\n\n```\nsage: f = factor(120)\nsage: for i in range(10): timeit('f^(2^%s)' % i)\n....: \n625 loops, best of 3: 4.49 \u00b5s per loop\n625 loops, best of 3: 95.1 \u00b5s per loop\n625 loops, best of 3: 95 \u00b5s per loop\n625 loops, best of 3: 95 \u00b5s per loop\n625 loops, best of 3: 95.1 \u00b5s per loop\n625 loops, best of 3: 95 \u00b5s per loop\n625 loops, best of 3: 95.2 \u00b5s per loop\n625 loops, best of 3: 95.2 \u00b5s per loop\n625 loops, best of 3: 95.3 \u00b5s per loop\n625 loops, best of 3: 95.3 \u00b5s per loop\n```\n\nIt might be possible to make this faster still.  But as John points out, it's a fairly obscure function.  I only wrote the patch because I found in the course of doing some calculations that the existing code can't cope at all with factorizations of ideals in moderately sized number fields; what takes all the time is the completely unnecessary check for idempotence in the generic power code.",
    "created_at": "2009-08-18T22:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6766#issuecomment-55632",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

I agree with John's comments, but  for the record: before (4.1.1)

```
sage: f = factor(120)
sage: for i in range(10): timeit('f^(2^%s)' % i)
....: 
625 loops, best of 3: 80.1 µs per loop
625 loops, best of 3: 538 µs per loop
625 loops, best of 3: 1.03 ms per loop
125 loops, best of 3: 1.5 ms per loop
125 loops, best of 3: 1.93 ms per loop
125 loops, best of 3: 2.39 ms per loop
125 loops, best of 3: 2.81 ms per loop
125 loops, best of 3: 3.23 ms per loop
125 loops, best of 3: 3.7 ms per loop
125 loops, best of 3: 4.12 ms per loop
```

and after (4.1.1 + patch)

```
sage: f = factor(120)
sage: for i in range(10): timeit('f^(2^%s)' % i)
....: 
625 loops, best of 3: 4.49 µs per loop
625 loops, best of 3: 95.1 µs per loop
625 loops, best of 3: 95 µs per loop
625 loops, best of 3: 95 µs per loop
625 loops, best of 3: 95.1 µs per loop
625 loops, best of 3: 95 µs per loop
625 loops, best of 3: 95.2 µs per loop
625 loops, best of 3: 95.2 µs per loop
625 loops, best of 3: 95.3 µs per loop
625 loops, best of 3: 95.3 µs per loop
```

It might be possible to make this faster still.  But as John points out, it's a fairly obscure function.  I only wrote the patch because I found in the course of doing some calculations that the existing code can't cope at all with factorizations of ideals in moderately sized number fields; what takes all the time is the completely unnecessary check for idempotence in the generic power code.



---

archive/issue_comments_055633.json:
```json
{
    "body": "Replying to [comment:5 fwclarke]:\n> I agree with John's comments, but  for the record: before (4.1.1)\n\n```\nsage: f = factor(120)\nsage: for i in range(10): timeit('f^(2^%s)' % i)\n....: \n625 loops, best of 3: 80.1 \u00b5s per loop\n625 loops, best of 3: 538 \u00b5s per loop\n625 loops, best of 3: 1.03 ms per loop\n125 loops, best of 3: 1.5 ms per loop\n125 loops, best of 3: 1.93 ms per loop\n125 loops, best of 3: 2.39 ms per loop\n125 loops, best of 3: 2.81 ms per loop\n125 loops, best of 3: 3.23 ms per loop\n125 loops, best of 3: 3.7 ms per loop\n125 loops, best of 3: 4.12 ms per loop\n```\n\n> and after (4.1.1 + patch)\n\n```\nsage: f = factor(120)\nsage: for i in range(10): timeit('f^(2^%s)' % i)\n....: \n625 loops, best of 3: 4.49 \u00b5s per loop\n625 loops, best of 3: 95.1 \u00b5s per loop\n625 loops, best of 3: 95 \u00b5s per loop\n625 loops, best of 3: 95 \u00b5s per loop\n625 loops, best of 3: 95.1 \u00b5s per loop\n625 loops, best of 3: 95 \u00b5s per loop\n625 loops, best of 3: 95.2 \u00b5s per loop\n625 loops, best of 3: 95.2 \u00b5s per loop\n625 loops, best of 3: 95.3 \u00b5s per loop\n625 loops, best of 3: 95.3 \u00b5s per loop\n```\n\nThese are what I was looking for. Thank you for providing more examples. And my apologies since my above request was ambiguous.",
    "created_at": "2009-08-18T22:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6766#issuecomment-55633",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:5 fwclarke]:
> I agree with John's comments, but  for the record: before (4.1.1)

```
sage: f = factor(120)
sage: for i in range(10): timeit('f^(2^%s)' % i)
....: 
625 loops, best of 3: 80.1 µs per loop
625 loops, best of 3: 538 µs per loop
625 loops, best of 3: 1.03 ms per loop
125 loops, best of 3: 1.5 ms per loop
125 loops, best of 3: 1.93 ms per loop
125 loops, best of 3: 2.39 ms per loop
125 loops, best of 3: 2.81 ms per loop
125 loops, best of 3: 3.23 ms per loop
125 loops, best of 3: 3.7 ms per loop
125 loops, best of 3: 4.12 ms per loop
```

> and after (4.1.1 + patch)

```
sage: f = factor(120)
sage: for i in range(10): timeit('f^(2^%s)' % i)
....: 
625 loops, best of 3: 4.49 µs per loop
625 loops, best of 3: 95.1 µs per loop
625 loops, best of 3: 95 µs per loop
625 loops, best of 3: 95 µs per loop
625 loops, best of 3: 95.1 µs per loop
625 loops, best of 3: 95 µs per loop
625 loops, best of 3: 95.2 µs per loop
625 loops, best of 3: 95.2 µs per loop
625 loops, best of 3: 95.3 µs per loop
625 loops, best of 3: 95.3 µs per loop
```

These are what I was looking for. Thank you for providing more examples. And my apologies since my above request was ambiguous.



---

archive/issue_comments_055634.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-25T04:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6766",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6766#issuecomment-55634",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed

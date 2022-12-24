# Issue 1014: there should be an Integer.number_of_digits() function

archive/issues_001014.json:
```json
{
    "body": "Assignee: bober\n\nBoth `log(x,10)` and `len(str(x))` are bad ways to calculate the number of digits of an integer, but there doesn't appear to be a better way to do it right now in sage.\n\nProbably, it would be nice if there were a number_of_digits() (or maybe there is a better name) function in `sage.rings.integer.Integer` that wraps the relevant gmp function to return the number of digits of the integer.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1014\n\n",
    "created_at": "2007-10-27T23:06:26Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "there should be an Integer.number_of_digits() function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1014",
    "user": "bober"
}
```
Assignee: bober

Both `log(x,10)` and `len(str(x))` are bad ways to calculate the number of digits of an integer, but there doesn't appear to be a better way to do it right now in sage.

Probably, it would be nice if there were a number_of_digits() (or maybe there is a better name) function in `sage.rings.integer.Integer` that wraps the relevant gmp function to return the number of digits of the integer.

Issue created by migration from https://trac.sagemath.org/ticket/1014





---

archive/issue_comments_006220.json:
```json
{
    "body": "It should be called ndigits() just as ngens() et al.",
    "created_at": "2007-10-28T16:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1014#issuecomment-6220",
    "user": "malb"
}
```

It should be called ndigits() just as ngens() et al.



---

archive/issue_comments_006221.json:
```json
{
    "body": "This should wrap GMP's `sizeinbase()` function. See\n\nhttp://gmplib.org/manual/Miscellaneous-Integer-Functions.html#Miscellaneous-Integer-Functions",
    "created_at": "2007-11-16T01:22:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1014#issuecomment-6221",
    "user": "dmharvey"
}
```

This should wrap GMP's `sizeinbase()` function. See

http://gmplib.org/manual/Miscellaneous-Integer-Functions.html#Miscellaneous-Integer-Functions



---

archive/issue_comments_006222.json:
```json
{
    "body": "Sorry, my previous comment is wrong. The sizeinbase() function only returns an exact answer if the base is a power of two. Otherwise it can return one digit too much. The problem is that determining the exact number of digits is not a linear time algorithm; I think it's probably around O(n log<sup>2</sup>(n)). I did write an `exact_log()` function at some point which might be relevant, but from memory it wasn't too efficient.",
    "created_at": "2007-11-16T01:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1014#issuecomment-6222",
    "user": "dmharvey"
}
```

Sorry, my previous comment is wrong. The sizeinbase() function only returns an exact answer if the base is a power of two. Otherwise it can return one digit too much. The problem is that determining the exact number of digits is not a linear time algorithm; I think it's probably around O(n log<sup>2</sup>(n)). I did write an `exact_log()` function at some point which might be relevant, but from memory it wasn't too efficient.



---

archive/issue_comments_006223.json:
```json
{
    "body": "I spent a few hours trying to come up with a smart way of doing this, and then I decided to see exactly how bad it is to do log(x,10).  The upshot is that I couldn't come up with an integer large enough that taking the log isn't practically instantaneous.  Hence the patch.\n\nHere's an example:\n\n```\nsage: time n=100000000000000000**10000000+1\nCPU times: user 53.12 s, sys: 0.52 s, total: 53.65 s\nWall time: 53.76\nsage: time n.ndigits()\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n170000001\n```\n\n\nNote that it takes significantly longer to actually compute n than to get the number of digits.",
    "created_at": "2008-01-27T07:48:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1014#issuecomment-6223",
    "user": "AlexGhitza"
}
```

I spent a few hours trying to come up with a smart way of doing this, and then I decided to see exactly how bad it is to do log(x,10).  The upshot is that I couldn't come up with an integer large enough that taking the log isn't practically instantaneous.  Hence the patch.

Here's an example:

```
sage: time n=100000000000000000**10000000+1
CPU times: user 53.12 s, sys: 0.52 s, total: 53.65 s
Wall time: 53.76
sage: time n.ndigits()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
170000001
```


Note that it takes significantly longer to actually compute n than to get the number of digits.



---

archive/issue_comments_006224.json:
```json
{
    "body": "If this is supposed to give the exact number of digits... it doesn't.\n\nThe algorithm correctly says that the first number has 1001 digits; but the next two numbers actually have 1000 digits and the algorithm says 1001.\n\n\n```\nsage: RR(10^1000).abs().log(10).floor() + 1\n1001\nsage: RR(10^1000 - 1).abs().log(10).floor() + 1\n1001\nsage: RR(10^1000 - 10^900).abs().log(10).floor() + 1\n1001\n```\n",
    "created_at": "2008-01-27T08:04:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1014#issuecomment-6224",
    "user": "cwitty"
}
```

If this is supposed to give the exact number of digits... it doesn't.

The algorithm correctly says that the first number has 1001 digits; but the next two numbers actually have 1000 digits and the algorithm says 1001.


```
sage: RR(10^1000).abs().log(10).floor() + 1
1001
sage: RR(10^1000 - 1).abs().log(10).floor() + 1
1001
sage: RR(10^1000 - 10^900).abs().log(10).floor() + 1
1001
```




---

archive/issue_comments_006225.json:
```json
{
    "body": "Attachment [1014-ndigits.patch](tarball://root/attachments/some-uuid/ticket1014/1014-ndigits.patch) by AlexGhitza created at 2008-01-27 23:31:54\n\nrevised patch",
    "created_at": "2008-01-27T23:31:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1014#issuecomment-6225",
    "user": "AlexGhitza"
}
```

Attachment [1014-ndigits.patch](tarball://root/attachments/some-uuid/ticket1014/1014-ndigits.patch) by AlexGhitza created at 2008-01-27 23:31:54

revised patch



---

archive/issue_comments_006226.json:
```json
{
    "body": "Carl: thanks a lot for catching this.  I love this refereeing thing!\n\nI've put up a new patch, hopefully correct this time.\n\nHere's the (again, simple) idea:  Since my one-liner gave the same result as GMP's sizeinbase function, I ditched my earlier try and just called sizeinbase, which gives me a number guess, which is either the correct number of digits, or 1+ that.  To figure out which one is which, we simply need to compare our integer with the integer base**(guess-1).\n\nThat's what the patch does.  I've played around with this for very large numbers and the running time seems to be dominated by computing base**(guess-1); sizeinbase and the comparison are practically instantaneous.  So ndigits() now has roughly the same running time as creating n itself (which, I would guess, is linear in the size of n).  Here are some examples:\n\n\n```\nsage: time n=10^1000\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\nsage: time n.ndigits()\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n1001\nsage: time n=10^1000-1\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\nsage: time n.ndigits()\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n1000\nsage: time n=10^1000-10^900\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\nsage: time n.ndigits()\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00\n1000\nsage: time n=100000000000000000^10000000-1\nCPU times: user 29.66 s, sys: 0.42 s, total: 30.08 s\nWall time: 30.07\nsage: time n.ndigits()\nCPU times: user 29.64 s, sys: 0.40 s, total: 30.03 s\nWall time: 30.03\n170000000\n```\n",
    "created_at": "2008-01-27T23:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1014#issuecomment-6226",
    "user": "AlexGhitza"
}
```

Carl: thanks a lot for catching this.  I love this refereeing thing!

I've put up a new patch, hopefully correct this time.

Here's the (again, simple) idea:  Since my one-liner gave the same result as GMP's sizeinbase function, I ditched my earlier try and just called sizeinbase, which gives me a number guess, which is either the correct number of digits, or 1+ that.  To figure out which one is which, we simply need to compare our integer with the integer base**(guess-1).

That's what the patch does.  I've played around with this for very large numbers and the running time seems to be dominated by computing base**(guess-1); sizeinbase and the comparison are practically instantaneous.  So ndigits() now has roughly the same running time as creating n itself (which, I would guess, is linear in the size of n).  Here are some examples:


```
sage: time n=10^1000
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
sage: time n.ndigits()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
1001
sage: time n=10^1000-1
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
sage: time n.ndigits()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
1000
sage: time n=10^1000-10^900
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
sage: time n.ndigits()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
1000
sage: time n=100000000000000000^10000000-1
CPU times: user 29.66 s, sys: 0.42 s, total: 30.08 s
Wall time: 30.07
sage: time n.ndigits()
CPU times: user 29.64 s, sys: 0.40 s, total: 30.03 s
Wall time: 30.03
170000000
```




---

archive/issue_comments_006227.json:
```json
{
    "body": "This is very similar to the `Integer.exact_log` function. Can we perhaps merge the functionality here?\n\nAlso, I know nobody has time for this, but an even better algorithm would be:\n* as alex suggests, estimate the exponent using mpz_sizeinbase\n* instead of computing the whole power, just estimate the top couple of digits using MPFR (much much much faster than computing the whole power)\n* keep increasing precision until we can distinguish the input from the power.\n\nMaybe this would be easiest to implement using interval arithmetic.\n\nThe point is, for uniform random input, the top couple of digits will almost always give you the right answer straightaway. It's very rare that you need to compute everything. I wish I had more time to think about this, it sounds like a fun problem.",
    "created_at": "2008-01-27T23:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1014#issuecomment-6227",
    "user": "dmharvey"
}
```

This is very similar to the `Integer.exact_log` function. Can we perhaps merge the functionality here?

Also, I know nobody has time for this, but an even better algorithm would be:
* as alex suggests, estimate the exponent using mpz_sizeinbase
* instead of computing the whole power, just estimate the top couple of digits using MPFR (much much much faster than computing the whole power)
* keep increasing precision until we can distinguish the input from the power.

Maybe this would be easiest to implement using interval arithmetic.

The point is, for uniform random input, the top couple of digits will almost always give you the right answer straightaway. It's very rare that you need to compute everything. I wish I had more time to think about this, it sounds like a fun problem.



---

archive/issue_comments_006228.json:
```json
{
    "body": "Attachment [1014-ndigits-and-exact_log.patch](tarball://root/attachments/some-uuid/ticket1014/1014-ndigits-and-exact_log.patch) by AlexGhitza created at 2008-01-29 04:24:34",
    "created_at": "2008-01-29T04:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1014#issuecomment-6228",
    "user": "AlexGhitza"
}
```

Attachment [1014-ndigits-and-exact_log.patch](tarball://root/attachments/some-uuid/ticket1014/1014-ndigits-and-exact_log.patch) by AlexGhitza created at 2008-01-29 04:24:34



---

archive/issue_comments_006229.json:
```json
{
    "body": "Apply *only* the new patch.  It modifies exact_log and makes ndigits wrap it.  Also fixes a couple of typos.\n\nSee the discussion at\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/a17bdc227206638f",
    "created_at": "2008-01-29T04:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1014#issuecomment-6229",
    "user": "AlexGhitza"
}
```

Apply *only* the new patch.  It modifies exact_log and makes ndigits wrap it.  Also fixes a couple of typos.

See the discussion at
http://groups.google.com/group/sage-devel/browse_thread/thread/a17bdc227206638f



---

archive/issue_comments_006230.json:
```json
{
    "body": "Looks good, I say apply.",
    "created_at": "2008-02-15T05:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1014#issuecomment-6230",
    "user": "ncalexan"
}
```

Looks good, I say apply.



---

archive/issue_comments_006231.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-15T05:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1014#issuecomment-6231",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006232.json:
```json
{
    "body": "Merged 1014-ndigits-and-exact_log.patch in Sage 2.10.2.alpha0",
    "created_at": "2008-02-15T05:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1014#issuecomment-6232",
    "user": "mabshoff"
}
```

Merged 1014-ndigits-and-exact_log.patch in Sage 2.10.2.alpha0

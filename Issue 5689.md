# Issue 5689: hitting control c while computing pi results in wrong answers later

archive/issues_005689.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nD-69-91-159-159:~ wstein$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: RealField(10^6).pi()\n^C---------------------------------------------------------------------------\nKeyboardInterrupt                         Traceback (most recent call last)\n| Sage Version 3.4, Release Date: 2009-03-11                         |\n| Type notebook() for the GUI, and license() for information.        |\n/Users/wstein/.sage/temp/D_69_91_159_159.dhcp4.washington.edu/27480/_Users_wstein__sage_init_sage_0.py in <module>()\n\nKeyboardInterrupt: \nsage: RealField(10^3).pi()\n3.14159265358979323851280895940618620443274267017841339111328125000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\n```\n\n\nJeff Blakeslee reported this.\n\nCwitty followed up with:\n\n```\nOh, interesting!  I've always worried about _sig_on/_sig_off, but this\nis the first reproducible bug I've seen them cause.\n\nWhen Sage is computing pi to many digits (and in many other cases), it\nsets up a signal handler; if you press Control-C, then it will longjmp\nout of the signal handler.  This lets you interrupt long-running\ncomputations, but it's a really nasty thing to do... you can easily\nget memory leaks, and I can imagine lots of (somewhat unlikely)\nsituations where you would crash Sage or get wrong answers.\n\nI'm not sure what to do about the problem, though.  The \"right\" fix is\nto go through all the C libraries that Sage calls, and add periodic\nchecks for Control-C; but that's pretty impractical.  Another\npossibility would be to disable _sig_on, so that Control-C doesn't\nwork in long-running C computations.  This would fix the bug, but it\nwould also be vastly annoying.\n\nOne workaround that might fix this particular problem is to catch\nKeyboardInterrupt exceptions in the .pi() method (and in\n.euler_constant(), .catalan_constant(), and .log2()), and call\nmpfr_free_cache() if one is seen.  Hopefully then MPFR would no longer\nbelieve it has a higher precision value computed than it actually does\nhave.\n\nCarl\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5689\n\n",
    "created_at": "2009-04-05T19:06:09Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "hitting control c while computing pi results in wrong answers later",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5689",
    "user": "@williamstein"
}
```
Assignee: somebody


```
D-69-91-159-159:~ wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: RealField(10^6).pi()
^C---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
| Sage Version 3.4, Release Date: 2009-03-11                         |
| Type notebook() for the GUI, and license() for information.        |
/Users/wstein/.sage/temp/D_69_91_159_159.dhcp4.washington.edu/27480/_Users_wstein__sage_init_sage_0.py in <module>()

KeyboardInterrupt: 
sage: RealField(10^3).pi()
3.14159265358979323851280895940618620443274267017841339111328125000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```


Jeff Blakeslee reported this.

Cwitty followed up with:

```
Oh, interesting!  I've always worried about _sig_on/_sig_off, but this
is the first reproducible bug I've seen them cause.

When Sage is computing pi to many digits (and in many other cases), it
sets up a signal handler; if you press Control-C, then it will longjmp
out of the signal handler.  This lets you interrupt long-running
computations, but it's a really nasty thing to do... you can easily
get memory leaks, and I can imagine lots of (somewhat unlikely)
situations where you would crash Sage or get wrong answers.

I'm not sure what to do about the problem, though.  The "right" fix is
to go through all the C libraries that Sage calls, and add periodic
checks for Control-C; but that's pretty impractical.  Another
possibility would be to disable _sig_on, so that Control-C doesn't
work in long-running C computations.  This would fix the bug, but it
would also be vastly annoying.

One workaround that might fix this particular problem is to catch
KeyboardInterrupt exceptions in the .pi() method (and in
.euler_constant(), .catalan_constant(), and .log2()), and call
mpfr_free_cache() if one is seen.  Hopefully then MPFR would no longer
believe it has a higher precision value computed than it actually does
have.

Carl
```


Issue created by migration from https://trac.sagemath.org/ticket/5689





---

archive/issue_comments_044490.json:
```json
{
    "body": "I wrote code to fix this problem in this case.  The following testing code, which I wrote, does not work.  I'm recording it here for posterity:\n\n\n```\n        TESTS::\n\n        We check that trac 5689 is fixed:\n            sage: alarm(1); RealField(10^6).pi()\n            Traceback (most recent call last):\n            ...\n            KeyboardInterrupt: computation timed out because alarm was set for 1 seconds\n            sage: RealField(10^3).pi()\n            3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127\n```\n",
    "created_at": "2009-04-05T19:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5689#issuecomment-44490",
    "user": "@williamstein"
}
```

I wrote code to fix this problem in this case.  The following testing code, which I wrote, does not work.  I'm recording it here for posterity:


```
        TESTS::

        We check that trac 5689 is fixed:
            sage: alarm(1); RealField(10^6).pi()
            Traceback (most recent call last):
            ...
            KeyboardInterrupt: computation timed out because alarm was set for 1 seconds
            sage: RealField(10^3).pi()
            3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127
```




---

archive/issue_comments_044491.json:
```json
{
    "body": "This patch resolves this problem completely, but has a performance penalty:\n\n```\nBEFORE:\nsage: a = RealField(1000)\nsage: timeit('a.pi()')\n625 loops, best of 3: 3.4 \u00b5s per loop\n\nAFTER:\nsage: a = RealField(1000)\nsage: timeit('a.pi()')\n625 loops, best of 3: 64.4 \u00b5s per loop\n```\n\n\nOf course the difference in time is because the answer is being 100% cached in the first place. \n\nI tried catching the interrupt, as carl suggests, but that isn't easy in Cython without writing a whole new sig handler system like Gonzalo T. and I did for the pari gen.pyx file, and that is pretty painful. \n\nNote -- there is one way to defeat the attached patch: (1) hit control c during computation of a constant, then (2) call some other mpfr function that assumes that internally does compute one of these constants.   Thus this patch is not bullet proof.  I'm posting it since it seems better than nothing, resolves the immediate problem, and was totally trivial to write. \n\n -- William",
    "created_at": "2009-04-05T19:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5689#issuecomment-44491",
    "user": "@williamstein"
}
```

This patch resolves this problem completely, but has a performance penalty:

```
BEFORE:
sage: a = RealField(1000)
sage: timeit('a.pi()')
625 loops, best of 3: 3.4 µs per loop

AFTER:
sage: a = RealField(1000)
sage: timeit('a.pi()')
625 loops, best of 3: 64.4 µs per loop
```


Of course the difference in time is because the answer is being 100% cached in the first place. 

I tried catching the interrupt, as carl suggests, but that isn't easy in Cython without writing a whole new sig handler system like Gonzalo T. and I did for the pari gen.pyx file, and that is pretty painful. 

Note -- there is one way to defeat the attached patch: (1) hit control c during computation of a constant, then (2) call some other mpfr function that assumes that internally does compute one of these constants.   Thus this patch is not bullet proof.  I'm posting it since it seems better than nothing, resolves the immediate problem, and was totally trivial to write. 

 -- William



---

archive/issue_comments_044492.json:
```json
{
    "body": "Attachment [trac_5689.patch](tarball://root/attachments/some-uuid/ticket5689/trac_5689.patch) by @williamstein created at 2009-04-05 19:25:33",
    "created_at": "2009-04-05T19:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5689#issuecomment-44492",
    "user": "@williamstein"
}
```

Attachment [trac_5689.patch](tarball://root/attachments/some-uuid/ticket5689/trac_5689.patch) by @williamstein created at 2009-04-05 19:25:33



---

archive/issue_comments_044493.json:
```json
{
    "body": "One small issue: The comments do not mention the mpfr_const_catalan constant and are also not consistently indented. This is nick picking, but what the heck :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T05:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5689#issuecomment-44493",
    "user": "mabshoff"
}
```

One small issue: The comments do not mention the mpfr_const_catalan constant and are also not consistently indented. This is nick picking, but what the heck :)

Cheers,

Michael



---

archive/issue_comments_044494.json:
```json
{
    "body": "> One small issue: The comments do not mention the mpfr_const_catalan constant \n> and are also not consistently indented. This is nick picking, but what the heck :) \n\nThat's because I'm quoting from the MPFR documentation, which is *wrong* in that *it* doesn't mention mpfr_const_catalan. \n\nWilliam",
    "created_at": "2009-04-06T16:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5689#issuecomment-44494",
    "user": "@williamstein"
}
```

> One small issue: The comments do not mention the mpfr_const_catalan constant 
> and are also not consistently indented. This is nick picking, but what the heck :) 

That's because I'm quoting from the MPFR documentation, which is *wrong* in that *it* doesn't mention mpfr_const_catalan. 

William



---

archive/issue_comments_044495.json:
```json
{
    "body": "Attachment [trac_5689-part2.patch](tarball://root/attachments/some-uuid/ticket5689/trac_5689-part2.patch) by @williamstein created at 2009-04-06 16:53:55",
    "created_at": "2009-04-06T16:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5689#issuecomment-44495",
    "user": "@williamstein"
}
```

Attachment [trac_5689-part2.patch](tarball://root/attachments/some-uuid/ticket5689/trac_5689-part2.patch) by @williamstein created at 2009-04-06 16:53:55



---

archive/issue_comments_044496.json:
```json
{
    "body": "This is a 3.4.1 blocker.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T18:32:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5689#issuecomment-44496",
    "user": "mabshoff"
}
```

This is a 3.4.1 blocker.

Cheers,

Michael



---

archive/issue_comments_044497.json:
```json
{
    "body": "Positive review to both patches. I agree that correctness is way more importan than speed in this case.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T22:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5689#issuecomment-44497",
    "user": "mabshoff"
}
```

Positive review to both patches. I agree that correctness is way more importan than speed in this case.

Cheers,

Michael



---

archive/issue_comments_044498.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-06T22:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5689#issuecomment-44498",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044499.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T22:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5689#issuecomment-44499",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc2.

Cheers,

Michael

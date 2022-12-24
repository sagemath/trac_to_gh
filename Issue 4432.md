# Issue 4432: [with patch, needs review] symbolic gamma and factorial

archive/issues_004432.json:
```json
{
    "body": "Assignee: burcin\n\nThis patches adds symbolic gamma and factorial functions.\n\nThe symbolic factorial is named fact for now, so it does not clash with sage.rings.arith.factorial\n\nIssue created by migration from https://trac.sagemath.org/ticket/4432\n\n",
    "created_at": "2008-11-03T19:55:10Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] symbolic gamma and factorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4432",
    "user": "whuss"
}
```
Assignee: burcin

This patches adds symbolic gamma and factorial functions.

The symbolic factorial is named fact for now, so it does not clash with sage.rings.arith.factorial

Issue created by migration from https://trac.sagemath.org/ticket/4432





---

archive/issue_comments_032563.json:
```json
{
    "body": "Changing assignee from burcin to whuss.",
    "created_at": "2008-11-03T20:12:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4432#issuecomment-32563",
    "user": "whuss"
}
```

Changing assignee from burcin to whuss.



---

archive/issue_comments_032564.json:
```json
{
    "body": "See also #4433",
    "created_at": "2008-11-04T07:42:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4432#issuecomment-32564",
    "user": "whuss"
}
```

See also #4433



---

archive/issue_comments_032565.json:
```json
{
    "body": "Some initial comments.\n\nThe first patch still need a lot of doctests added.  The docstring in the second patch just needs to be reformatted.\n\nAlso, this shouldn't go in as is with the function named 'fact'.  #4433 changes this.",
    "created_at": "2008-11-04T21:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4432#issuecomment-32565",
    "user": "mhansen"
}
```

Some initial comments.

The first patch still need a lot of doctests added.  The docstring in the second patch just needs to be reformatted.

Also, this shouldn't go in as is with the function named 'fact'.  #4433 changes this.



---

archive/issue_comments_032566.json:
```json
{
    "body": "The new patch keeps the algorithm keyword for the symbolic factorial.\nIt also keeps the docstrings from the nonsymbolic functions, plus some new doctests.",
    "created_at": "2008-11-06T10:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4432#issuecomment-32566",
    "user": "whuss"
}
```

The new patch keeps the algorithm keyword for the symbolic factorial.
It also keeps the docstrings from the nonsymbolic functions, plus some new doctests.



---

archive/issue_comments_032567.json:
```json
{
    "body": "I added a patch which I think presents a cleaner solution for #4432 _and_ #4433.  What are your thoughts?",
    "created_at": "2008-11-06T21:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4432#issuecomment-32567",
    "user": "mhansen"
}
```

I added a patch which I think presents a cleaner solution for #4432 _and_ #4433.  What are your thoughts?



---

archive/issue_comments_032568.json:
```json
{
    "body": "Attachment [trac_4432-gamma.patch](tarball://root/attachments/some-uuid/ticket4432/trac_4432-gamma.patch) by burcin created at 2008-11-15 11:54:53\n\nimprovements to gamma, apply after Mike's trac_4432.patch",
    "created_at": "2008-11-15T11:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4432#issuecomment-32568",
    "user": "burcin"
}
```

Attachment [trac_4432-gamma.patch](tarball://root/attachments/some-uuid/ticket4432/trac_4432-gamma.patch) by burcin created at 2008-11-15 11:54:53

improvements to gamma, apply after Mike's trac_4432.patch



---

archive/issue_comments_032569.json:
```json
{
    "body": "The call to `RR(x).gamma()` does not match the previous behavior of the gamma function. The following doesn't work with the given patches:\n\n\n```\nsage: gamma(QQbar(I))\n<boom>\n```\n\n\nattachment:trac_4432-gamma.patch fixes this, and adds a few more doctests. \n\nI give Mike's patch a positive review. Mike, can you check my changes?",
    "created_at": "2008-11-15T11:59:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4432#issuecomment-32569",
    "user": "burcin"
}
```

The call to `RR(x).gamma()` does not match the previous behavior of the gamma function. The following doesn't work with the given patches:


```
sage: gamma(QQbar(I))
<boom>
```


attachment:trac_4432-gamma.patch fixes this, and adds a few more doctests. 

I give Mike's patch a positive review. Mike, can you check my changes?



---

archive/issue_comments_032570.json:
```json
{
    "body": "+1 to Burcin's patch.\n\nApply only the last two patches: trac_4432.patch and trac_4432-gamma.patch",
    "created_at": "2008-11-21T14:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4432#issuecomment-32570",
    "user": "mhansen"
}
```

+1 to Burcin's patch.

Apply only the last two patches: trac_4432.patch and trac_4432-gamma.patch



---

archive/issue_comments_032571.json:
```json
{
    "body": "Wilfried,\n\nin the future please make sure to post mercurial patches instead of diffs. This is also an issue with the other patches you have posted that far. I will commit any diff in your name, so that proper credit goes to you.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-23T09:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4432#issuecomment-32571",
    "user": "mabshoff"
}
```

Wilfried,

in the future please make sure to post mercurial patches instead of diffs. This is also an issue with the other patches you have posted that far. I will commit any diff in your name, so that proper credit goes to you.

Cheers,

Michael



---

archive/issue_comments_032572.json:
```json
{
    "body": "There are two doctest failures with this patch:\n\n```\nsage -t -long devel/sage/sage/rings/arith.py                \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/arith.py\", line 3011:\n    sage: falling_factorial(1+I, I)\nExpected:\n    0.652965496420167 + 0.343065839816545*I\nGot:\n    gamma(I + 2)\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/arith.py\", line 3074:\n    sage: rising_factorial(1+I, I)\nExpected:\n    0.266816390637832 + 0.122783354006372*I\nGot:\n    gamma(2*I + 1)/gamma(I + 1)\n**********************************************************************\n```\n\nSounds like this will be easy to fix. I would also like to see if there are any performance regressions with this patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-23T09:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4432#issuecomment-32572",
    "user": "mabshoff"
}
```

There are two doctest failures with this patch:

```
sage -t -long devel/sage/sage/rings/arith.py                
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/arith.py", line 3011:
    sage: falling_factorial(1+I, I)
Expected:
    0.652965496420167 + 0.343065839816545*I
Got:
    gamma(I + 2)
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/arith.py", line 3074:
    sage: rising_factorial(1+I, I)
Expected:
    0.266816390637832 + 0.122783354006372*I
Got:
    gamma(2*I + 1)/gamma(I + 1)
**********************************************************************
```

Sounds like this will be easy to fix. I would also like to see if there are any performance regressions with this patch.

Cheers,

Michael



---

archive/issue_comments_032573.json:
```json
{
    "body": "Michael,\n\nI probably have to read the Mercurial documentation.\n\nI'm not sure if I measure the performance correctly, but if I do\n\n\n```\ndef f(n):\n    s = 0\n    for i in xrange(n):\n        s += factorial(2^i)\n    return s.ndigits()\n\ndef g(n):\n    s = 0\n    for i in xrange(n):\n        s += gamma((1.8)^i)\n    return s\n\ndef h(n):\n    set_random_seed(0)\n    s = 0\n    for i in xrange(n):\n        s += gamma(random())\n    return s\n\ntimeit('f(22)')\ntimeit('g(22)')\ntimeit('h(10^4)')\n```\n\n\nI get the following:\n\non sage-3.2 without the patch\n\n```\n5 loops, best of 3: 10.9 s per loop\n125 loops, best of 3: 4.16 ms per loop\n5 loops, best of 3: 5.38 s per loop\n```\n\n\nwith trac_4432.patch\n\n```\n5 loops, best of 3: 10.9 s per loop\n125 loops, best of 3: 4.18 ms per loop\n5 loops, best of 3: 1.67 s per loop\n```\n\n\nwith trac_4432.patch + trac_4432-gamma.patch\n\n```\n5 loops, best of 3: 10.9 s per loop\n125 loops, best of 3: 4.17 ms per loop\n5 loops, best of 3: 5.45 s per loop\n```\n\n\nSo trac_4432.patch is much faster for small values of the gamma function\nbecause we are not computing over the complex numbers.\n\nAlso only with trac_4432.patch\n\n```\nplot(gamma, 1, 4)\n```\n\nworks. But this also doesn't work with the current code.\n\nGreetings,\n\nWilfried",
    "created_at": "2008-11-24T15:43:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4432#issuecomment-32573",
    "user": "whuss"
}
```

Michael,

I probably have to read the Mercurial documentation.

I'm not sure if I measure the performance correctly, but if I do


```
def f(n):
    s = 0
    for i in xrange(n):
        s += factorial(2^i)
    return s.ndigits()

def g(n):
    s = 0
    for i in xrange(n):
        s += gamma((1.8)^i)
    return s

def h(n):
    set_random_seed(0)
    s = 0
    for i in xrange(n):
        s += gamma(random())
    return s

timeit('f(22)')
timeit('g(22)')
timeit('h(10^4)')
```


I get the following:

on sage-3.2 without the patch

```
5 loops, best of 3: 10.9 s per loop
125 loops, best of 3: 4.16 ms per loop
5 loops, best of 3: 5.38 s per loop
```


with trac_4432.patch

```
5 loops, best of 3: 10.9 s per loop
125 loops, best of 3: 4.18 ms per loop
5 loops, best of 3: 1.67 s per loop
```


with trac_4432.patch + trac_4432-gamma.patch

```
5 loops, best of 3: 10.9 s per loop
125 loops, best of 3: 4.17 ms per loop
5 loops, best of 3: 5.45 s per loop
```


So trac_4432.patch is much faster for small values of the gamma function
because we are not computing over the complex numbers.

Also only with trac_4432.patch

```
plot(gamma, 1, 4)
```

works. But this also doesn't work with the current code.

Greetings,

Wilfried



---

archive/issue_comments_032574.json:
```json
{
    "body": "make plotting of the gamma function work, fix doctests, apply after burchin's trac_4432-gamma.patch",
    "created_at": "2008-11-24T16:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4432#issuecomment-32574",
    "user": "whuss"
}
```

make plotting of the gamma function work, fix doctests, apply after burchin's trac_4432-gamma.patch



---

archive/issue_comments_032575.json:
```json
{
    "body": "Attachment [trac_4432-plot-doc.patch](tarball://root/attachments/some-uuid/ticket4432/trac_4432-plot-doc.patch) by whuss created at 2008-11-24 16:18:56\n\nI fixed the doctests and the plotting of the gamma function, with\nattachment:trac_4432-plot-doc.patch.\n\nAlso\n\n\n```\nsage: timeit('h(10^4)')\n5 loops, best of 3: 1.68 s per loop\n```\n\n\nGreetings,\n\nWilfried",
    "created_at": "2008-11-24T16:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4432#issuecomment-32575",
    "user": "whuss"
}
```

Attachment [trac_4432-plot-doc.patch](tarball://root/attachments/some-uuid/ticket4432/trac_4432-plot-doc.patch) by whuss created at 2008-11-24 16:18:56

I fixed the doctests and the plotting of the gamma function, with
attachment:trac_4432-plot-doc.patch.

Also


```
sage: timeit('h(10^4)')
5 loops, best of 3: 1.68 s per loop
```


Greetings,

Wilfried



---

archive/issue_comments_032576.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-11-28T07:26:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4432#issuecomment-32576",
    "user": "mhansen"
}
```

Looks good.



---

archive/issue_comments_032577.json:
```json
{
    "body": "Apply all of the above patches.",
    "created_at": "2008-11-28T08:05:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4432#issuecomment-32577",
    "user": "mhansen"
}
```

Apply all of the above patches.



---

archive/issue_comments_032578.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-28T08:36:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4432#issuecomment-32578",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032579.json:
```json
{
    "body": "Merged all three patches in Sage 3.2.1.rc0",
    "created_at": "2008-11-28T08:36:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4432#issuecomment-32579",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.2.1.rc0

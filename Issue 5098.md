# Issue 5098: [with patch, needs review] Pollard rho algorithm for generic discrete logarithm

archive/issues_005098.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @JohnCremona\n\nFirst attempt to provide an algorithm using less memory than the \"baby step giant step\" algorithm for generic discrete logarithm.\n\nThis algorithm uses only (small) constant memory. It is about 3 times slower than bsgs on the examples I tested.\n\nI also added an unused optional argument to bsgs to simplify the call in discrete_log.\n\nProposed patch attached, with doctests.\n\n(the attached patch needs #5088 to be applied first)\n\nIssue created by migration from https://trac.sagemath.org/ticket/5098\n\n",
    "created_at": "2009-01-25T15:17:41Z",
    "labels": [
        "component: algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "[with patch, needs review] Pollard rho algorithm for generic discrete logarithm",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5098",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```
Assignee: tbd

CC:  @JohnCremona

First attempt to provide an algorithm using less memory than the "baby step giant step" algorithm for generic discrete logarithm.

This algorithm uses only (small) constant memory. It is about 3 times slower than bsgs on the examples I tested.

I also added an unused optional argument to bsgs to simplify the call in discrete_log.

Proposed patch attached, with doctests.

(the attached patch needs #5088 to be applied first)

Issue created by migration from https://trac.sagemath.org/ticket/5098





---

archive/issue_comments_038811.json:
```json
{
    "body": "Do you know what makes this slower?\n\nI'm not so familiar with this version of Pollard, but this looks well-written.  I'll test it once my build of 3.3.alpha2 has finished.",
    "created_at": "2009-01-25T15:37:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38811",
    "user": "https://github.com/JohnCremona"
}
```

Do you know what makes this slower?

I'm not so familiar with this version of Pollard, but this looks well-written.  I'll test it once my build of 3.3.alpha2 has finished.



---

archive/issue_comments_038812.json:
```json
{
    "body": "I don't really know what makes it slow. I suspect the use of \"hash\" is costly but I see no other way to partition generically a group in approximately equal size chunks.",
    "created_at": "2009-01-25T16:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38812",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

I don't really know what makes it slow. I suspect the use of "hash" is costly but I see no other way to partition generically a group in approximately equal size chunks.



---

archive/issue_comments_038813.json:
```json
{
    "body": "Replying to [comment:2 ylchapuy]:\n> I don't really know what makes it slow. I suspect the use of \"hash\" is costly but I see no other way to partition generically a group in approximately equal size chunks.\n\nThat is probably right.  It might be worth putting in a comment (or a docstring sentence aimed at future developers) saying that the efficiency of the functions depends on having a fast hash.",
    "created_at": "2009-01-25T17:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38813",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:2 ylchapuy]:
> I don't really know what makes it slow. I suspect the use of "hash" is costly but I see no other way to partition generically a group in approximately equal size chunks.

That is probably right.  It might be worth putting in a comment (or a docstring sentence aimed at future developers) saying that the efficiency of the functions depends on having a fast hash.



---

archive/issue_comments_038814.json:
```json
{
    "body": "Replying to [comment:3 cremona]:\n> Replying to [comment:2 ylchapuy]:\n> > I don't really know what makes it slow. I suspect the use of \"hash\" is costly but I see no other way to partition generically a group in approximately equal size chunks.\n> \n> That is probably right.  It might be worth putting in a comment (or a docstring sentence aimed at future developers) saying that the efficiency of the functions depends on having a fast hash.\n\npatch modified to adress the above comment. The hash function is now a parameter of the pollard_rho function to give future developers an easy way to customize it.",
    "created_at": "2009-01-25T18:58:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38814",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Replying to [comment:3 cremona]:
> Replying to [comment:2 ylchapuy]:
> > I don't really know what makes it slow. I suspect the use of "hash" is costly but I see no other way to partition generically a group in approximately equal size chunks.
> 
> That is probably right.  It might be worth putting in a comment (or a docstring sentence aimed at future developers) saying that the efficiency of the functions depends on having a fast hash.

patch modified to adress the above comment. The hash function is now a parameter of the pollard_rho function to give future developers an easy way to customize it.



---

archive/issue_comments_038815.json:
```json
{
    "body": "I just wrote a review for this but trac refused to save it since another comment has been made in between.  How can it do this!!!!  Luckily I was able to use the \"back\" button to revover what I had written.\n\nReview:\n\n* Patch applied fine to 3.3.alpha2.  Doctests in groups/generic pass.\n\n* In the docstring for pollard_rho() I would move the explanation for the partition_size parameter to a NOTE later, not in the description of the paramater;  and that description should say that the default is 16.\n\n* There should be doctests in discrete_log() showing the use of the algorithm parameter.\n\nI also think that it would be helpful to add to this ticket (and perhaps also in doctests) examples showing how the new algorithm is sometimes preferable!\n\nNone of these is at all serious, and think this additoin is basically very good.",
    "created_at": "2009-01-25T19:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38815",
    "user": "https://github.com/JohnCremona"
}
```

I just wrote a review for this but trac refused to save it since another comment has been made in between.  How can it do this!!!!  Luckily I was able to use the "back" button to revover what I had written.

Review:

* Patch applied fine to 3.3.alpha2.  Doctests in groups/generic pass.

* In the docstring for pollard_rho() I would move the explanation for the partition_size parameter to a NOTE later, not in the description of the paramater;  and that description should say that the default is 16.

* There should be doctests in discrete_log() showing the use of the algorithm parameter.

I also think that it would be helpful to add to this ticket (and perhaps also in doctests) examples showing how the new algorithm is sometimes preferable!

None of these is at all serious, and think this additoin is basically very good.



---

archive/issue_comments_038816.json:
```json
{
    "body": "a patch is on the way. I also removed to debug printings I forgot and added my authorship. \n\nConcerning comparison, the benefit of Pollard rho algorithm comes only with quite big examples and I don't think it's a good idea for doctests. Here's one example.\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: yann\nsage: get_memory_usage()\n113.9765625\nsage: F.<a>=GF(2^118)\nsage: g=F.multiplicative_generator()\nsage: u=g^15726718062461913153073925660344578\nsage: time discrete_log(u,g,algorithm=\"rho\")\nCPU times: user 56.06 s, sys: 0.20 s, total: 56.26 s\nWall time: 56.39 s\n15726718062461913153073925660344578\nsage: get_memory_usage()\n116.03515625\nsage: time discrete_log(u,g,algorithm=\"bsgs\")\nCPU times: user 46.74 s, sys: 0.54 s, total: 47.29 s\nWall time: 47.47 s\n15726718062461913153073925660344578\nsage: get_memory_usage()\n392.89453125\n```\n\nactually, Pollard rho is not so slow :)",
    "created_at": "2009-01-26T08:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38816",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

a patch is on the way. I also removed to debug printings I forgot and added my authorship. 

Concerning comparison, the benefit of Pollard rho algorithm comes only with quite big examples and I don't think it's a good idea for doctests. Here's one example.

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: yann
sage: get_memory_usage()
113.9765625
sage: F.<a>=GF(2^118)
sage: g=F.multiplicative_generator()
sage: u=g^15726718062461913153073925660344578
sage: time discrete_log(u,g,algorithm="rho")
CPU times: user 56.06 s, sys: 0.20 s, total: 56.26 s
Wall time: 56.39 s
15726718062461913153073925660344578
sage: get_memory_usage()
116.03515625
sage: time discrete_log(u,g,algorithm="bsgs")
CPU times: user 46.74 s, sys: 0.54 s, total: 47.29 s
Wall time: 47.47 s
15726718062461913153073925660344578
sage: get_memory_usage()
392.89453125
```

actually, Pollard rho is not so slow :)



---

archive/issue_comments_038817.json:
```json
{
    "body": "argh, sorry, trac-5098-review.2.patch are the same trac-5098-review.patch, only one of them needs to be applied",
    "created_at": "2009-01-26T08:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38817",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

argh, sorry, trac-5098-review.2.patch are the same trac-5098-review.patch, only one of them needs to be applied



---

archive/issue_comments_038818.json:
```json
{
    "body": "if someone reviews this patch, he might have a look at #5112 implementing Pollard lambda algorithm",
    "created_at": "2009-01-27T20:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38818",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

if someone reviews this patch, he might have a look at #5112 implementing Pollard lambda algorithm



---

archive/issue_comments_038819.json:
```json
{
    "body": "I am having trouble applying the new patch.  I have a 3.3.alpha2 build, so #5088 is already merged.  I apply trac-5098.patch ok.  Then I apply trac-5098-review.patch but get several hunks failing.\n\nThis might just be me being stupid, so it would be good if someone else tried.\n\nWhile I am here though, you did not quite understand my third point in the original review:  I did not mean that a new doctest should illustrate the greater efficiency (or not) of the new algorithm, but it should at least illustrate how to use the new parameter.  e.g. take one of the existing examples and compute it bothe ways and check that they are equal:\n\n```\n        sage: F.<a>=GF(2^63)\n        sage: g=F.gen()\n        sage: u=g**123456789\n        sage: discrete_log(u,g,algorithm='bsgs') == discrete_log(u,g,algorithm='rho')\n        True\n```\n",
    "created_at": "2009-01-28T20:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38819",
    "user": "https://github.com/JohnCremona"
}
```

I am having trouble applying the new patch.  I have a 3.3.alpha2 build, so #5088 is already merged.  I apply trac-5098.patch ok.  Then I apply trac-5098-review.patch but get several hunks failing.

This might just be me being stupid, so it would be good if someone else tried.

While I am here though, you did not quite understand my third point in the original review:  I did not mean that a new doctest should illustrate the greater efficiency (or not) of the new algorithm, but it should at least illustrate how to use the new parameter.  e.g. take one of the existing examples and compute it bothe ways and check that they are equal:

```
        sage: F.<a>=GF(2^63)
        sage: g=F.gen()
        sage: u=g**123456789
        sage: discrete_log(u,g,algorithm='bsgs') == discrete_log(u,g,algorithm='rho')
        True
```




---

archive/issue_comments_038820.json:
```json
{
    "body": "brand new standalone patch, based on a fresh alpha2 build.\nI hope everything is ok this time :)",
    "created_at": "2009-01-29T11:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38820",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

brand new standalone patch, based on a fresh alpha2 build.
I hope everything is ok this time :)



---

archive/issue_comments_038821.json:
```json
{
    "body": "Attachment [trac-5098-alpha2based.patch](tarball://root/attachments/some-uuid/ticket5098/trac-5098-alpha2based.patch) by @JohnCremona created at 2009-02-01 15:15:54\n\nThanks -- I am quite happy now, and give this a positive review!  Now I will go and look at the lambda patch too.",
    "created_at": "2009-02-01T15:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38821",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac-5098-alpha2based.patch](tarball://root/attachments/some-uuid/ticket5098/trac-5098-alpha2based.patch) by @JohnCremona created at 2009-02-01 15:15:54

Thanks -- I am quite happy now, and give this a positive review!  Now I will go and look at the lambda patch too.



---

archive/issue_comments_038822.json:
```json
{
    "body": "The latest patch causes the following doctest failure: From\n\n```\nFile \"/scratch/mabshoff/sage-3.3.alpha4/devel/sage/sage/rings/integer_mod.pyx\", line 444:\n   sage: sage.groups.generic.discrete_log(a,b)\nExpected:\n   Traceback (most recent call last):\n   ...\n   ZeroDivisionError: Inverse does not exist.\n```\n\nwe get to\n\n```\nArithmeticError: multiplicative order of 4 not defined since it is not a unit modulo 100\n```\n\n\nWilliam doesn't like either one, but he is about to comment himself.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T02:18:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38822",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The latest patch causes the following doctest failure: From

```
File "/scratch/mabshoff/sage-3.3.alpha4/devel/sage/sage/rings/integer_mod.pyx", line 444:
   sage: sage.groups.generic.discrete_log(a,b)
Expected:
   Traceback (most recent call last):
   ...
   ZeroDivisionError: Inverse does not exist.
```

we get to

```
ArithmeticError: multiplicative order of 4 not defined since it is not a unit modulo 100
```


William doesn't like either one, but he is about to comment himself.

Cheers,

Michael



---

archive/issue_comments_038823.json:
```json
{
    "body": "\n```\n William:  Hmm.\nBetter would be a statement that the discrete log doesn't exist.\nOr that it might but the algorithm implemented can't tell.\nI don't like either error.\n me:  Well, I will comment on the ticket and then you can comment there on the record.\n William:  The log does exist.\nso it would be much better to get a NotImplementedError when things go wrong.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T02:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38823",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```


```
 William:  Hmm.
Better would be a statement that the discrete log doesn't exist.
Or that it might but the algorithm implemented can't tell.
I don't like either error.
 me:  Well, I will comment on the ticket and then you can comment there on the record.
 William:  The log does exist.
so it would be much better to get a NotImplementedError when things go wrong.
```


Cheers,

Michael



---

archive/issue_comments_038824.json:
```json
{
    "body": "Hi guys,\n\nthis ticket and #5112 is being held up by the above doctesting issues. The patches should go into 3.3 and rc0 will drop in roughly 48 hours, so there is time to sort this out. We could do two things:\n\n* change the doctest to \"fix\" the problem for now and open a followup ticket to deal with the problem William pointed out. Since the situation doesn't seem to get worst that seems acceptable\n* fix the problem William pointed out :)\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2009-02-08T10:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38824",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi guys,

this ticket and #5112 is being held up by the above doctesting issues. The patches should go into 3.3 and rc0 will drop in roughly 48 hours, so there is time to sort this out. We could do two things:

* change the doctest to "fix" the problem for now and open a followup ticket to deal with the problem William pointed out. Since the situation doesn't seem to get worst that seems acceptable
* fix the problem William pointed out :)

Thoughts?

Cheers,

Michael



---

archive/issue_comments_038825.json:
```json
{
    "body": "I don't have time to look into this and hope that ylchapuy will.  I don't actually think it is the Pollard rho code at fault since by default generic discrete log still uses bsgs, so it is more likely to be the previous (and already merged) improvement to the discrete log which ylchapuy added a week or two ago.\n\nIf I finish all the \"real\" work I must do before tomorrow I'll come back to this but that is not very likely...",
    "created_at": "2009-02-08T10:34:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38825",
    "user": "https://github.com/JohnCremona"
}
```

I don't have time to look into this and hope that ylchapuy will.  I don't actually think it is the Pollard rho code at fault since by default generic discrete log still uses bsgs, so it is more likely to be the previous (and already merged) improvement to the discrete log which ylchapuy added a week or two ago.

If I finish all the "real" work I must do before tomorrow I'll come back to this but that is not very likely...



---

archive/issue_comments_038826.json:
```json
{
    "body": "I would suggest to fix the doctest for the moment, and open a ticket for an enhancement.\nFor the moment, we only allow discrete logarithms computations in groups with known order;\nI think it could be possible quite easily to make pollard rho algorithm to work for unknown order too but it needs some work. I definitely have no time today, and no clean install of recent sage to patch the doctest myself ontime...",
    "created_at": "2009-02-09T17:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38826",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

I would suggest to fix the doctest for the moment, and open a ticket for an enhancement.
For the moment, we only allow discrete logarithms computations in groups with known order;
I think it could be possible quite easily to make pollard rho algorithm to work for unknown order too but it needs some work. I definitely have no time today, and no clean install of recent sage to patch the doctest myself ontime...



---

archive/issue_comments_038827.json:
```json
{
    "body": "Attachment [trac-5098-doctest.patch](tarball://root/attachments/some-uuid/ticket5098/trac-5098-doctest.patch) by ylchapuy created at 2009-02-11 10:12:55\n\nadded a small patch to fix doctest, and return a NotImplementedError explaining the problem which is that we can't get the order of the base (in the example it's not a unit).",
    "created_at": "2009-02-11T10:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38827",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac-5098-doctest.patch](tarball://root/attachments/some-uuid/ticket5098/trac-5098-doctest.patch) by ylchapuy created at 2009-02-11 10:12:55

added a small patch to fix doctest, and return a NotImplementedError explaining the problem which is that we can't get the order of the base (in the example it's not a unit).



---

archive/issue_comments_038828.json:
```json
{
    "body": "the last patch only change the behaviour in case the order of the base can't be computed. If all the patches apply cleanly I think it doesn't need another review (correct me if I'm wrong).",
    "created_at": "2009-02-11T12:27:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38828",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

the last patch only change the behaviour in case the order of the base can't be computed. If all the patches apply cleanly I think it doesn't need another review (correct me if I'm wrong).



---

archive/issue_comments_038829.json:
```json
{
    "body": "I was intending to review this (again), but there are a lot of patches and I do not know which ones to apply.  All?\n\nRegarding the last doctest issue, the function being tested states in its docstring that the arguments should be units, so surely it would be more sensible to test that and return an error if not, rather than go ahead and call any of the generic discrete log functions (which are placed in sage/GROUPS/generic.py for a reason: they require a group and were written that way, so inverses would exist).  Just because 4 happens to be a power of 2 mod 100 does not mean that I should be forced to apologise for not returning an answer in that case.  I know of no reason anyone might ever have for implementing discrete logs for non-units in a non-integral domain.",
    "created_at": "2009-02-14T14:37:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38829",
    "user": "https://github.com/JohnCremona"
}
```

I was intending to review this (again), but there are a lot of patches and I do not know which ones to apply.  All?

Regarding the last doctest issue, the function being tested states in its docstring that the arguments should be units, so surely it would be more sensible to test that and return an error if not, rather than go ahead and call any of the generic discrete log functions (which are placed in sage/GROUPS/generic.py for a reason: they require a group and were written that way, so inverses would exist).  Just because 4 happens to be a power of 2 mod 100 does not mean that I should be forced to apologise for not returning an answer in that case.  I know of no reason anyone might ever have for implementing discrete logs for non-units in a non-integral domain.



---

archive/issue_comments_038830.json:
```json
{
    "body": "First: The patches to apply are the last two only; is there a way to remove the other ones?\n\nSecondly: I do agree, discrete logarithm is intended only for groups. The changes in my last patch might still be useful. I test if we can compute the order of the base, because the algorithms we use for now need them. It's probably not a good idea though to treat in the same way a non unit, and an element of a group where order is not implemented...\n\nWhat should I do to make those patches the right way ?",
    "created_at": "2009-02-14T14:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38830",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

First: The patches to apply are the last two only; is there a way to remove the other ones?

Secondly: I do agree, discrete logarithm is intended only for groups. The changes in my last patch might still be useful. I test if we can compute the order of the base, because the algorithms we use for now need them. It's probably not a good idea though to treat in the same way a non unit, and an element of a group where order is not implemented...

What should I do to make those patches the right way ?



---

archive/issue_comments_038831.json:
```json
{
    "body": "Replying to [comment:22 ylchapuy]:\n> First: The patches to apply are the last two only; is there a way to remove the other ones?\n\nRight now only trac admins can delete patches. I will delete all but the two last patches shortly.\n\nSome times it is interesting for credit and historic purposes to keep old patches around, but in this case it should be no problem to delete them.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T14:57:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38831",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:22 ylchapuy]:
> First: The patches to apply are the last two only; is there a way to remove the other ones?

Right now only trac admins can delete patches. I will delete all but the two last patches shortly.

Some times it is interesting for credit and historic purposes to keep old patches around, but in this case it should be no problem to delete them.

Cheers,

Michael



---

archive/issue_comments_038832.json:
```json
{
    "body": "I have some issues with trac-5098-doctest.patch:\n\n1. There should be a doctest that illustrates every single exception that can be raised.  For example this patch adds\n\n```\nraise NotImplementedError, \"The current implementation of Pollard Rho algorithm needs to have (a multiple of) the order of the base\" \n```\n\non line 543, but there is no doctest that illustrates this.\n\n2. Line 758, The %s\"%base business is bad.  \n\n```\nraise NotImplementedError, \"we currently need to know the order of the base %s\"%(base) }}}\nI used to write a lot of exceptions like this, since for Magma we did that.  But in Magma, they aren't exceptions that can be caught -- any single exception stops the program.  In Sage, exceptions can be caught and occur as part of the normal flow of execution of a program.  Once in 2006 there was a simple calculation David Harvey was doing, and he was very confused because it was taking several minutes to do something trivial.  It turned out this was because in the course of the computation an exception was raised and caught (e.g., because of some coercion model stuff), and the exception was written like the one before -- it was a string that printed the element involved in the coercion, and the str(...) conversion of the element took *minutes*.   That was what dominated the calculation.  As a result I realized that I had completely messed up in using that pattern for implementing exceptions in Sage, and had to go through the whole codebase and rewrite all such exceptions. \n\nJust to hammer this home, consider \n{{{\nsage: a = Mod(16, 100); b = Mod(-4,10^10^7)\nsage: try: w = sage.groups.generic.discrete_log(a,b)\n      except: pass\n[hang forever!]\n}}}\nand if it ever did come back, imagine what that exception would look like!",
    "created_at": "2009-02-15T07:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38832",
    "user": "https://github.com/williamstein"
}
```

I have some issues with trac-5098-doctest.patch:

1. There should be a doctest that illustrates every single exception that can be raised.  For example this patch adds

```
raise NotImplementedError, "The current implementation of Pollard Rho algorithm needs to have (a multiple of) the order of the base" 
```

on line 543, but there is no doctest that illustrates this.

2. Line 758, The %s"%base business is bad.  

```
raise NotImplementedError, "we currently need to know the order of the base %s"%(base) }}}
I used to write a lot of exceptions like this, since for Magma we did that.  But in Magma, they aren't exceptions that can be caught -- any single exception stops the program.  In Sage, exceptions can be caught and occur as part of the normal flow of execution of a program.  Once in 2006 there was a simple calculation David Harvey was doing, and he was very confused because it was taking several minutes to do something trivial.  It turned out this was because in the course of the computation an exception was raised and caught (e.g., because of some coercion model stuff), and the exception was written like the one before -- it was a string that printed the element involved in the coercion, and the str(...) conversion of the element took *minutes*.   That was what dominated the calculation.  As a result I realized that I had completely messed up in using that pattern for implementing exceptions in Sage, and had to go through the whole codebase and rewrite all such exceptions. 

Just to hammer this home, consider 
{{{
sage: a = Mod(16, 100); b = Mod(-4,10^10^7)
sage: try: w = sage.groups.generic.discrete_log(a,b)
      except: pass
[hang forever!]
}}}
and if it ever did come back, imagine what that exception would look like!



---

archive/issue_comments_038833.json:
```json
{
    "body": "Here's some irc chatter about the \"%s\"%base exception business. There are perhaps thousands (?) of instances of this in Sage now.\n\n```\n23:46 < wstein> They can be \"silent killers\" :-)\n23:46 < mabs> wstein: can an opinion on the broken combinat pickles?\n23:47 < mabs> can -> got\n23:48 < wstein> wstein@sage:/space/wstein/sage-3.3.rc0$ ./sage -grep \"raise\" \"%s\" |wc -l\n23:48 < wstein> 6750\n23:48 < mabs> *OUCH*\n23:48 < wstein> It's not always bad.\n23:48 < wstein> wstein@sage:/space/wstein/sage-3.3.rc0$ ./sage -grep \"raise\" \"%s\" |wc -l\n23:48 < wstein> Oops.\n23:49 < wstein> sage: search_src(\"raise\",\"%s\") # also shows them.\n23:49 < wstein> It's only the ones that have elements that could easily be large in the exception that\n23:49 < wstein> are a danger.\n23:49 < wstein> But a quick glance suggests there are probably thousands of these still.\n23:50 < mabs> Yes, I thought the comment was good since I never knew about that problem.\n23:50 < wstein> Especially in the combinat and coding theory code...\n23:50 < mabs> :)\n23:50 < wstein> One can just do search_src(\"raise\",\"%s\")\n23:50 < wstein> look to see which exceptions are funny, and quickly craft examples where\n23:50 < wstein> things seem to hang for stupid reasons instead of raising an exception.\n23:51 < wstein> Where hang = create a base-10 string rep for something in memory, then try to display a bazillion characters to screen.\n```\n",
    "created_at": "2009-02-15T07:57:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38833",
    "user": "https://github.com/williamstein"
}
```

Here's some irc chatter about the "%s"%base exception business. There are perhaps thousands (?) of instances of this in Sage now.

```
23:46 < wstein> They can be "silent killers" :-)
23:46 < mabs> wstein: can an opinion on the broken combinat pickles?
23:47 < mabs> can -> got
23:48 < wstein> wstein@sage:/space/wstein/sage-3.3.rc0$ ./sage -grep "raise" "%s" |wc -l
23:48 < wstein> 6750
23:48 < mabs> *OUCH*
23:48 < wstein> It's not always bad.
23:48 < wstein> wstein@sage:/space/wstein/sage-3.3.rc0$ ./sage -grep "raise" "%s" |wc -l
23:48 < wstein> Oops.
23:49 < wstein> sage: search_src("raise","%s") # also shows them.
23:49 < wstein> It's only the ones that have elements that could easily be large in the exception that
23:49 < wstein> are a danger.
23:49 < wstein> But a quick glance suggests there are probably thousands of these still.
23:50 < mabs> Yes, I thought the comment was good since I never knew about that problem.
23:50 < wstein> Especially in the combinat and coding theory code...
23:50 < mabs> :)
23:50 < wstein> One can just do search_src("raise","%s")
23:50 < wstein> look to see which exceptions are funny, and quickly craft examples where
23:50 < wstein> things seem to hang for stupid reasons instead of raising an exception.
23:51 < wstein> Where hang = create a base-10 string rep for something in memory, then try to display a bazillion characters to screen.
```




---

archive/issue_comments_038834.json:
```json
{
    "body": "A comment by cwitty about my suggestion that every exception should be doctested:\n\n```\n00:07 < cwitty> wstein: re your comment on #5098: I've added exceptions to Sage that I have no idea how \n                to doctest.\n00:07 < wstein> cwitty -- for that patch I think they would all be easy.\n00:07 < wstein> I had that in mind.\n00:07 < cwitty> I sort of suspect that hitting them may require working in a number field of degree \n                several billion, but I'm not positive.\n00:07 < wstein> cwitty -- at least you can give a reason for not doctesting the ones you don't test.\n00:08 < wstein> I don't mean for that to be some absolute rule.\n00:08 < wstein> Just a general guideline.\n00:08 < wstein> But you have a good point.\n00:08 < wstein> I'll paste this to the ticket.\n00:09 < wstein> The last thing I wrote in sage was something involving gap.py and the \"This should \n                never happen\" exception.\n00:09 < wstein> That can't be doctested :-)\n00:09 < wstein> So you're right.\n```\n",
    "created_at": "2009-02-15T08:14:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38834",
    "user": "https://github.com/williamstein"
}
```

A comment by cwitty about my suggestion that every exception should be doctested:

```
00:07 < cwitty> wstein: re your comment on #5098: I've added exceptions to Sage that I have no idea how 
                to doctest.
00:07 < wstein> cwitty -- for that patch I think they would all be easy.
00:07 < wstein> I had that in mind.
00:07 < cwitty> I sort of suspect that hitting them may require working in a number field of degree 
                several billion, but I'm not positive.
00:07 < wstein> cwitty -- at least you can give a reason for not doctesting the ones you don't test.
00:08 < wstein> I don't mean for that to be some absolute rule.
00:08 < wstein> Just a general guideline.
00:08 < wstein> But you have a good point.
00:08 < wstein> I'll paste this to the ticket.
00:09 < wstein> The last thing I wrote in sage was something involving gap.py and the "This should 
                never happen" exception.
00:09 < wstein> That can't be doctested :-)
00:09 < wstein> So you're right.
```




---

archive/issue_comments_038835.json:
```json
{
    "body": "I am cleaning up the 3.3 milestone. If a patch with positive review is put up to this ticket on time it might make it into 3.3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T05:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38835",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am cleaning up the 3.3 milestone. If a patch with positive review is put up to this ticket on time it might make it into 3.3.

Cheers,

Michael



---

archive/issue_comments_038836.json:
```json
{
    "body": "Any movement on this?\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T07:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38836",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Any movement on this?

Cheers,

Michael



---

archive/issue_comments_038837.json:
```json
{
    "body": "Let's try another way. \nThe last patch I uploaded is to be applied instead of the previous ones. It only provide a Pollard rho algorithm for discrete log, without plugin it in the existing discrete log. We can address the other problems about non unit elements for example in another ticket.",
    "created_at": "2009-06-30T16:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38837",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Let's try another way. 
The last patch I uploaded is to be applied instead of the previous ones. It only provide a Pollard rho algorithm for discrete log, without plugin it in the existing discrete log. We can address the other problems about non unit elements for example in another ticket.



---

archive/issue_comments_038838.json:
```json
{
    "body": "This looks ok to me.  It applies fine to 4.1.alpha3 and tests pass.  It might be better to call the function discrete_log_rho instead of pollard_rho_log as that would make it easier to find via tab completion on discrete_*.\n\nThere should also be examples (doctests) to illustrate the use of the parameters partition_size, memory_size, hash_function, check_prime.  For example, one where using a non-default value gives better (i.e. faster) results.  If it is not practical to put those into doctests (for example, if the improvement is only noticeable with very large examples), tehre should still be small examples to illustrate these parameters, with a comment about them being too small to notice, just to show how they are used.\n\nAnd the technical parameters partition_size, memory_size should be listed in the INPUT block rather than in a separate note.\n\nI have left this as \"needs work\" but those things are very small and a positive review is not far away!",
    "created_at": "2009-07-03T14:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38838",
    "user": "https://github.com/JohnCremona"
}
```

This looks ok to me.  It applies fine to 4.1.alpha3 and tests pass.  It might be better to call the function discrete_log_rho instead of pollard_rho_log as that would make it easier to find via tab completion on discrete_*.

There should also be examples (doctests) to illustrate the use of the parameters partition_size, memory_size, hash_function, check_prime.  For example, one where using a non-default value gives better (i.e. faster) results.  If it is not practical to put those into doctests (for example, if the improvement is only noticeable with very large examples), tehre should still be small examples to illustrate these parameters, with a comment about them being too small to notice, just to show how they are used.

And the technical parameters partition_size, memory_size should be listed in the INPUT block rather than in a separate note.

I have left this as "needs work" but those things are very small and a positive review is not far away!



---

archive/issue_comments_038839.json:
```json
{
    "body": "I renamed the function to \"discrete_log_rho\", removed the unnecessary parameters (partition_size and memory_size don't change that much the behavior), added an example of user set hash function, and forgot to add an exemple for check_prime... I will fix this in 2 minutes!",
    "created_at": "2009-09-05T15:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38839",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

I renamed the function to "discrete_log_rho", removed the unnecessary parameters (partition_size and memory_size don't change that much the behavior), added an example of user set hash function, and forgot to add an exemple for check_prime... I will fix this in 2 minutes!



---

archive/issue_comments_038840.json:
```json
{
    "body": "Attachment [trac_5098_standalone.patch](tarball://root/attachments/some-uuid/ticket5098/trac_5098_standalone.patch) by ylchapuy created at 2009-09-05 15:43:40\n\nbased on sage 4.1.1",
    "created_at": "2009-09-05T15:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38840",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac_5098_standalone.patch](tarball://root/attachments/some-uuid/ticket5098/trac_5098_standalone.patch) by ylchapuy created at 2009-09-05 15:43:40

based on sage 4.1.1



---

archive/issue_comments_038841.json:
```json
{
    "body": "I finally choose to remove the parameter check_prime because the complexity of Pollard Rho algorithm is a lot bigger than primality testing.",
    "created_at": "2009-09-05T15:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38841",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

I finally choose to remove the parameter check_prime because the complexity of Pollard Rho algorithm is a lot bigger than primality testing.



---

archive/issue_comments_038842.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-08T09:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38842",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_038843.json:
```json
{
    "body": "This gets a positive review from me with the small changes in the review patch. All tests pass. For transparency I just added one tiny comment on the fall back and completed the type of a raised error.",
    "created_at": "2009-12-08T09:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38843",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

This gets a positive review from me with the small changes in the review patch. All tests pass. For transparency I just added one tiny comment on the fall back and completed the type of a raised error.



---

archive/issue_comments_038844.json:
```json
{
    "body": "Attachment [trac-5098-pollard_review.patch](tarball://root/attachments/some-uuid/ticket5098/trac-5098-pollard_review.patch) by @mwhansen created at 2009-12-20 07:23:32",
    "created_at": "2009-12-20T07:23:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38844",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac-5098-pollard_review.patch](tarball://root/attachments/some-uuid/ticket5098/trac-5098-pollard_review.patch) by @mwhansen created at 2009-12-20 07:23:32



---

archive/issue_comments_038845.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-20T07:23:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5098#issuecomment-38845",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_005344.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-12-20T07:23:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5098",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5098#event-5344"
}
```

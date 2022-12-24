# Issue 5963: 3.4.2.a0: prime_pi returns wrong results on some platforms for large input

archive/issues_005963.json:
```json
{
    "body": "Assignee: was\n\nAlex reports: \n\nI can't get this to segfault. I tried on sage.math and on my laptop (macbook running 32-bit archlinux). The problem is that the two machines get different answers after a while (I hope the table is clear -- the last column is a function that's \"known\" to be a good approximation to prime_pi):\n\n```\nx     prime_pi(x) on sage.math     prime_pi(x) on my laptop     Li(x)-Li(sqrt(x))/2\n2^46   2280998753949                2280998753949               2.28099863535e+12\n2^47   4461632979717                4454203917918               4.46163280359e+12\n2^48   8731188863470                8612800813048               8.73118897751e+12\n2^49  17094432576778               15793194017311               1.70944327138e+13\n2^50  33483379603407               21969300962685               3.34833795774e+13\n```\n\nSo it seems that the problem starts somewhere between 2^46 and 2^47, and that the sage.math output is most likely correct.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5963\n\n",
    "created_at": "2009-05-02T20:15:21Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "3.4.2.a0: prime_pi returns wrong results on some platforms for large input",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5963",
    "user": "mabshoff"
}
```
Assignee: was

Alex reports: 

I can't get this to segfault. I tried on sage.math and on my laptop (macbook running 32-bit archlinux). The problem is that the two machines get different answers after a while (I hope the table is clear -- the last column is a function that's "known" to be a good approximation to prime_pi):

```
x     prime_pi(x) on sage.math     prime_pi(x) on my laptop     Li(x)-Li(sqrt(x))/2
2^46   2280998753949                2280998753949               2.28099863535e+12
2^47   4461632979717                4454203917918               4.46163280359e+12
2^48   8731188863470                8612800813048               8.73118897751e+12
2^49  17094432576778               15793194017311               1.70944327138e+13
2^50  33483379603407               21969300962685               3.34833795774e+13
```

So it seems that the problem starts somewhere between 2^46 and 2^47, and that the sage.math output is most likely correct.

Issue created by migration from https://trac.sagemath.org/ticket/5963





---

archive/issue_comments_047227.json:
```json
{
    "body": "As discussed toward the end in https://groups.google.com/group/sage-devel/t/776d8e0a25735dca \n\n```\nOn May 2, 3:52 pm, William Stein <wst...@gmail.com> wrote: \n<SNIP>\n> Andrew looked into this whole issue a while ago, and told me that the\n> prime_pi he implemented *should* only work up to about 2^40, and the\n> algorithm would take far too long above there.   I thought he had\n> included an error message if the input exceeds 2^40, but I guess not.\n>    So +1 to your suggestion above, but with a smaller bound that 2^48.\n\nCool.\n\n> He told me Mathematica can go up to about 2^45 or so, but not beyond.\n\nAt least for MMA 6.0 on linux x86-64 the limit seems to be around\n2^47:\n\n         MMA        Sage\n\n2^44:   18.04      110.88   (597116381732)\n2^45:   29.98      207.61   (1166746786182)\n2^46:   47.59      389.98   (2280998753949)\n2^47:   89.25      728.84   (4461632979717)\n2^48:   NA :)      about an hour - correct?\n\nAccording to Alex's numbers at least on his laptop 2^46 was correct on\n32 bits, but given the length of the test (~6 minutes on sage.math\nthis isn't really doctestable).\n\n> The algorithm in Mathematica is completely different (and better) than\n> what Andrew implemented for Sage.   As far as I know the situation for\n> computing pi(X) using general purpose math software is thus:\n\n>    * Mathematica -- has the best implementation available\n\n>    * Sage -- now has the second best implementation available\n\nYep, the old implementation was about 1000 times slower than Andrew's\nwhich is about 5 times slower than MMA 6.0 - so great job from\ncatching us up from 5000 times to only 5 times :).\n\n>    * Pari, Maple, Matlab -- \"stupid\" implementations, which all simply\n> enumerate all primes up to x and see how many there are.  Useless, and\n> can't come close to what Sage or Mathematica do.\n\nWell, what should we pick as upper bound? 2^40 seems to be what Andrew\nsuggests, but maybe 2^42 or 2^43? In that range we can actually add\n#long doctests and I would be much more comfortable that we would at\nleast catch potential issues.\n\n>  -- William\n\nCheers,\n\nMichael \n```\n",
    "created_at": "2009-05-03T00:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5963#issuecomment-47227",
    "user": "mabshoff"
}
```

As discussed toward the end in https://groups.google.com/group/sage-devel/t/776d8e0a25735dca 

```
On May 2, 3:52 pm, William Stein <wst...@gmail.com> wrote: 
<SNIP>
> Andrew looked into this whole issue a while ago, and told me that the
> prime_pi he implemented *should* only work up to about 2^40, and the
> algorithm would take far too long above there.   I thought he had
> included an error message if the input exceeds 2^40, but I guess not.
>    So +1 to your suggestion above, but with a smaller bound that 2^48.

Cool.

> He told me Mathematica can go up to about 2^45 or so, but not beyond.

At least for MMA 6.0 on linux x86-64 the limit seems to be around
2^47:

         MMA        Sage

2^44:   18.04      110.88   (597116381732)
2^45:   29.98      207.61   (1166746786182)
2^46:   47.59      389.98   (2280998753949)
2^47:   89.25      728.84   (4461632979717)
2^48:   NA :)      about an hour - correct?

According to Alex's numbers at least on his laptop 2^46 was correct on
32 bits, but given the length of the test (~6 minutes on sage.math
this isn't really doctestable).

> The algorithm in Mathematica is completely different (and better) than
> what Andrew implemented for Sage.   As far as I know the situation for
> computing pi(X) using general purpose math software is thus:

>    * Mathematica -- has the best implementation available

>    * Sage -- now has the second best implementation available

Yep, the old implementation was about 1000 times slower than Andrew's
which is about 5 times slower than MMA 6.0 - so great job from
catching us up from 5000 times to only 5 times :).

>    * Pari, Maple, Matlab -- "stupid" implementations, which all simply
> enumerate all primes up to x and see how many there are.  Useless, and
> can't come close to what Sage or Mathematica do.

Well, what should we pick as upper bound? 2^40 seems to be what Andrew
suggests, but maybe 2^42 or 2^43? In that range we can actually add
#long doctests and I would be much more comfortable that we would at
least catch potential issues.

>  -- William

Cheers,

Michael 
```




---

archive/issue_comments_047228.json:
```json
{
    "body": "Attachment [trac_5963.patch](tarball://root/attachments/some-uuid/ticket5963/trac_5963.patch) by mabshoff created at 2009-05-04 06:13:40\n\nThe attached patch caps the allowed input to `2^40` for now and adds a long doctest to verify the correct value of all n in (30..40) for prime_pi(2**n). The upper allowable limit should be reviewed post Sage 3.4.2.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T06:13:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5963#issuecomment-47228",
    "user": "mabshoff"
}
```

Attachment [trac_5963.patch](tarball://root/attachments/some-uuid/ticket5963/trac_5963.patch) by mabshoff created at 2009-05-04 06:13:40

The attached patch caps the allowed input to `2^40` for now and adds a long doctest to verify the correct value of all n in (30..40) for prime_pi(2**n). The upper allowable limit should be reviewed post Sage 3.4.2.

Cheers,

Michael



---

archive/issue_comments_047229.json:
```json
{
    "body": "Changing assignee from was to mabshoff.",
    "created_at": "2009-05-04T06:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5963#issuecomment-47229",
    "user": "mabshoff"
}
```

Changing assignee from was to mabshoff.



---

archive/issue_comments_047230.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-04T06:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5963#issuecomment-47230",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047231.json:
```json
{
    "body": "Looks good to me.  Michael says that the values in the doctest agree with those from Mathematica.",
    "created_at": "2009-05-04T08:37:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5963#issuecomment-47231",
    "user": "roed"
}
```

Looks good to me.  Michael says that the values in the doctest agree with those from Mathematica.



---

archive/issue_comments_047232.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-04T09:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5963#issuecomment-47232",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_047233.json:
```json
{
    "body": "Merged in Sage 3.4.2.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-04T09:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5963#issuecomment-47233",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.final.

Cheers,

Michael

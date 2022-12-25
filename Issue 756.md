# Issue 756: modify how foo.derivative(...) works

archive/issues_000756.json:
```json
{
    "body": "Assignee: somebody\n\n```\nOn 9/26/07, David Joyner <wdjoyner@gmail.com> wrote:\n> I'm not sure if this is a bug or not but just in case,\n> here is the way diff is behaving for me.\n>\n> - David Joyner\n>\n> sage: version()\n> 'SAGE Version 2.8.5, Release Date: 2007-09-21'\n> sage: R1.<a> = PolynomialRing(QQ)\n> sage: R2.<x> = PowerSeriesRing(R1)\n> sage: y = a*x\n> sage: y.derivative()\n> a\n> sage: diff(y,x)\n> ---------------------------------------------------------------------------\n> <type 'exceptions.TypeError'>             Traceback (most recent call last)\n>\n> /mnt/hd200/sagefiles/sage-2.8.3.rc3/<ipython console> in <module>()\n\n\nOne should slightly rewrite the derivative function for\npolynomials (and power series) to take\nan optional argument (the variable).  If the\ninnput variable is the same as the parent\ngen, then differentiate as before; otherwise\nattempt to call derivative on the coefficients -- if\nthat works, good; if not, return 0.\n\n -- William\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/756\n\n",
    "created_at": "2007-09-26T20:48:58Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "modify how foo.derivative(...) works",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/756",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

```
On 9/26/07, David Joyner <wdjoyner@gmail.com> wrote:
> I'm not sure if this is a bug or not but just in case,
> here is the way diff is behaving for me.
>
> - David Joyner
>
> sage: version()
> 'SAGE Version 2.8.5, Release Date: 2007-09-21'
> sage: R1.<a> = PolynomialRing(QQ)
> sage: R2.<x> = PowerSeriesRing(R1)
> sage: y = a*x
> sage: y.derivative()
> a
> sage: diff(y,x)
> ---------------------------------------------------------------------------
> <type 'exceptions.TypeError'>             Traceback (most recent call last)
>
> /mnt/hd200/sagefiles/sage-2.8.3.rc3/<ipython console> in <module>()


One should slightly rewrite the derivative function for
polynomials (and power series) to take
an optional argument (the variable).  If the
innput variable is the same as the parent
gen, then differentiate as before; otherwise
attempt to call derivative on the coefficients -- if
that works, good; if not, return 0.

 -- William
```

Issue created by migration from https://trac.sagemath.org/ticket/756





---

archive/issue_comments_004454.json:
```json
{
    "body": "Made the changes suggested above by William, see the patch.",
    "created_at": "2008-02-16T20:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4454",
    "user": "https://github.com/aghitza"
}
```

Made the changes suggested above by William, see the patch.



---

archive/issue_comments_004455.json:
```json
{
    "body": "Few minor issues to sort out.\n\nIn the `polynomial_element_generic.py` version, some indentation has gone awry (the `if d.has_key(-1):` block is indented more than it used to be).\n\nAs a general rule please use `if x is None` instead of `if x == None`, because it's 100x faster:\n\n```\nsage: x = 5\n\nsage: timeit if x is None: y = 6\n1000000 loops, best of 3: 239 ns per loop\n\nsage: timeit if x == None: y = 6\n10000 loops, best of 3: 31.9 \u00b5s per loop\n```\n\nThe phrase \"if the latter is absent\" is a bit confusing; the first time I read it I thought it meant \"if the object being differentiated doesn't have the latter\", which is completely wrong. Maybe something like \"if no var is supplied\"?",
    "created_at": "2008-02-18T00:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4455",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Few minor issues to sort out.

In the `polynomial_element_generic.py` version, some indentation has gone awry (the `if d.has_key(-1):` block is indented more than it used to be).

As a general rule please use `if x is None` instead of `if x == None`, because it's 100x faster:

```
sage: x = 5

sage: timeit if x is None: y = 6
1000000 loops, best of 3: 239 ns per loop

sage: timeit if x == None: y = 6
10000 loops, best of 3: 31.9 µs per loop
```

The phrase "if the latter is absent" is a bit confusing; the first time I read it I thought it meant "if the object being differentiated doesn't have the latter", which is completely wrong. Maybe something like "if no var is supplied"?



---

archive/issue_comments_004456.json:
```json
{
    "body": "Attachment [756-derivative-wrt.patch](tarball://root/attachments/some-uuid/ticket756/756-derivative-wrt.patch) by @aghitza created at 2008-02-18 02:06:03",
    "created_at": "2008-02-18T02:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4456",
    "user": "https://github.com/aghitza"
}
```

Attachment [756-derivative-wrt.patch](tarball://root/attachments/some-uuid/ticket756/756-derivative-wrt.patch) by @aghitza created at 2008-02-18 02:06:03



---

archive/issue_comments_004457.json:
```json
{
    "body": "Excellent points from David.  I've made the changes and uploaded a new patch.",
    "created_at": "2008-02-18T02:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4457",
    "user": "https://github.com/aghitza"
}
```

Excellent points from David.  I've made the changes and uploaded a new patch.



---

archive/issue_comments_004458.json:
```json
{
    "body": "Attachment [756-doctests.patch](tarball://root/attachments/some-uuid/ticket756/756-doctests.patch) by dmharvey created at 2008-02-18 03:21:53",
    "created_at": "2008-02-18T03:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4458",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [756-doctests.patch](tarball://root/attachments/some-uuid/ticket756/756-doctests.patch) by dmharvey created at 2008-02-18 03:21:53



---

archive/issue_comments_004459.json:
```json
{
    "body": "I've attached a patch (should be applied on top of alex's patch) which adds some more doctests. The last doctest in the power series case currently fails; I think it should  pass.",
    "created_at": "2008-02-18T03:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4459",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I've attached a patch (should be applied on top of alex's patch) which adds some more doctests. The last doctest in the power series case currently fails; I think it should  pass.



---

archive/issue_comments_004460.json:
```json
{
    "body": "Attachment [756-derivative-wrt-new.patch](tarball://root/attachments/some-uuid/ticket756/756-derivative-wrt-new.patch) by @aghitza created at 2008-02-18 13:40:26",
    "created_at": "2008-02-18T13:40:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4460",
    "user": "https://github.com/aghitza"
}
```

Attachment [756-derivative-wrt-new.patch](tarball://root/attachments/some-uuid/ticket756/756-derivative-wrt-new.patch) by @aghitza created at 2008-02-18 13:40:26



---

archive/issue_comments_004461.json:
```json
{
    "body": "Again, excellent catch by David.  I've fixed the problem with the power series doctest (which by the way should give 2+y+..., not y+2+... :)\n\nApply 756-derivative-wrt-new.patch instead of the others (it includes them and the fixes).",
    "created_at": "2008-02-18T13:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4461",
    "user": "https://github.com/aghitza"
}
```

Again, excellent catch by David.  I've fixed the problem with the power series doctest (which by the way should give 2+y+..., not y+2+... :)

Apply 756-derivative-wrt-new.patch instead of the others (it includes them and the fixes).



---

archive/issue_comments_004462.json:
```json
{
    "body": "With `756-derivative-wrt-new.patch` I'm getting doctest failures for `sage/schemes/elliptic_curves/padics.py`, involving the power series case. I think the problem is it's calling the underlying polynomial type's `derivative` function with an argument, but for some reason that underlying derivative function doesn't accept an argument. This is a shame, the whole issue is becoming more complicated than it should have been. Note there are possible interactions with #753 and #1578. We really need a standardised solution for this across all polynomial, power series (univariate/multivariate) and symbolic objects.",
    "created_at": "2008-02-18T15:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4462",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

With `756-derivative-wrt-new.patch` I'm getting doctest failures for `sage/schemes/elliptic_curves/padics.py`, involving the power series case. I think the problem is it's calling the underlying polynomial type's `derivative` function with an argument, but for some reason that underlying derivative function doesn't accept an argument. This is a shame, the whole issue is becoming more complicated than it should have been. Note there are possible interactions with #753 and #1578. We really need a standardised solution for this across all polynomial, power series (univariate/multivariate) and symbolic objects.



---

archive/issue_comments_004463.json:
```json
{
    "body": "Here's a possible plan of action. Someone needs to audit all polynomial, power series, symbolic classes, and produce a list of currently existing `derivative` and `diff` (and `differentiate`?) methods, and what parameters they accept. This needs to be summarised and presented to sage-devel. Discussion will ensue, and we'll agree on a uniform solution. Then someone needs to go and implement it. The main objectives should be: (i) consistency from a programmatic point of view, (ii) ease of use for new users (they shouldn't need to learn how to differentiate more than once).\n\nI'm happy to lead the charge, but I won't get around to it for at least a week. Alex, if you're interested, go right ahead (although I realise that you probably didn't intend to get so deeply into this issue when you posted the first patch for this ticket....)",
    "created_at": "2008-02-18T16:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4463",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Here's a possible plan of action. Someone needs to audit all polynomial, power series, symbolic classes, and produce a list of currently existing `derivative` and `diff` (and `differentiate`?) methods, and what parameters they accept. This needs to be summarised and presented to sage-devel. Discussion will ensue, and we'll agree on a uniform solution. Then someone needs to go and implement it. The main objectives should be: (i) consistency from a programmatic point of view, (ii) ease of use for new users (they shouldn't need to learn how to differentiate more than once).

I'm happy to lead the charge, but I won't get around to it for at least a week. Alex, if you're interested, go right ahead (although I realise that you probably didn't intend to get so deeply into this issue when you posted the first patch for this ticket....)



---

archive/issue_comments_004464.json:
```json
{
    "body": "I agree with David's comments and with the need for cleaning up the derivative methods.  This should be done carefully, so it doesn't lend itself very well to the 15-minute spurts that I can dedicate to Sage these days.  I can try to think about it and rummage throught the code on Saturday, but if someone else feels energetic, by all means, go for it!\n\nOne related remark: there are also integrate() methods for polys and power series, and they should benefit from the same treatment.",
    "created_at": "2008-02-19T16:47:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4464",
    "user": "https://github.com/aghitza"
}
```

I agree with David's comments and with the need for cleaning up the derivative methods.  This should be done carefully, so it doesn't lend itself very well to the 15-minute spurts that I can dedicate to Sage these days.  I can try to think about it and rummage throught the code on Saturday, but if someone else feels energetic, by all means, go for it!

One related remark: there are also integrate() methods for polys and power series, and they should benefit from the same treatment.



---

archive/issue_comments_004465.json:
```json
{
    "body": "currently there is action on this at #753",
    "created_at": "2008-02-28T03:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4465",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

currently there is action on this at #753



---

archive/issue_comments_004466.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-03T14:31:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4466",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Resolution: duplicate



---

archive/issue_events_002062.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/dmharvey",
    "created_at": "2008-03-03T14:31:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/756#event-2062"
}
```



---

archive/issue_comments_004467.json:
```json
{
    "body": "I am closing this since it has been superseded by #753.",
    "created_at": "2008-03-03T14:31:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4467",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I am closing this since it has been superseded by #753.



---

archive/issue_comments_004468.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2008-03-03T16:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4468",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_004469.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-03-03T16:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4469",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_002063.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-03T16:11:15Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/756#event-2063"
}
```



---

archive/issue_comments_004470.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-03T16:11:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4470",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002064.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-03T16:11:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/756#event-2064"
}
```



---

archive/issue_comments_004471.json:
```json
{
    "body": "This isn't really a duplicate and I consider this fixed. It looks like a borderline case, so I tend to call those tickets fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-03T16:13:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/756#issuecomment-4471",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This isn't really a duplicate and I consider this fixed. It looks like a borderline case, so I tend to call those tickets fixed.

Cheers,

Michael

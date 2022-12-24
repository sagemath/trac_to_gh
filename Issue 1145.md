# Issue 1145: high-level strategy for integer factorization

archive/issues_001145.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jdemeyer jpflori\n\nI propose the following strategy for factor(integer):\n\n1) do trial division by all primes up to say 1000. This can be done efficiently by a single\n   gcd with the product of all those primes.\n2) use GMP-ECM, starting from say B1=100, and increasing B1 by sqrt(B1) at each step, until\n   one reaches the _recommended_B1_list value which corresponds to 1/3 of the size of the\n   number to be factored. Thus for a 90-digit input, one will stop at B1=250000.\n3) try GMP-ECM P-1 and P+1 with respectively 9*B1 and 3*B1 where B1 is the last value tried\n   for ECM. The corresponding cost of those runs will be approximately the same as the last\n   ECM curve, thus this will not slow down the average computation, and might find a few factors.\n4) run MPQS or GNFS. You might want to issue a warning to the user (if called from toplevel) at\n   that time.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1145\n\n",
    "created_at": "2007-11-11T13:26:17Z",
    "labels": [
        "number theory",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "high-level strategy for integer factorization",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1145",
    "user": "@zimmermann6"
}
```
Assignee: @williamstein

CC:  @jdemeyer jpflori

I propose the following strategy for factor(integer):

1) do trial division by all primes up to say 1000. This can be done efficiently by a single
   gcd with the product of all those primes.
2) use GMP-ECM, starting from say B1=100, and increasing B1 by sqrt(B1) at each step, until
   one reaches the _recommended_B1_list value which corresponds to 1/3 of the size of the
   number to be factored. Thus for a 90-digit input, one will stop at B1=250000.
3) try GMP-ECM P-1 and P+1 with respectively 9*B1 and 3*B1 where B1 is the last value tried
   for ECM. The corresponding cost of those runs will be approximately the same as the last
   ECM curve, thus this will not slow down the average computation, and might find a few factors.
4) run MPQS or GNFS. You might want to issue a warning to the user (if called from toplevel) at
   that time.

Issue created by migration from https://trac.sagemath.org/ticket/1145





---

archive/issue_comments_006959.json:
```json
{
    "body": "Comments from some experts:\n\n```\n\nOn 12/11/2007, Robert Bradshaw <robertwb@math.washington.edu> wrote:\n> I don't have much expertise in the area, but it looks like a sound\n> proposal to me. The trial division bound seems a bit low (and perhaps\n> should be adjusted for the size of the input). Is this similar to\n> what Pari does? Would it make sense to parallelize ECM/QS by default\n> on a multi-core system?\n>\n> - Robert\n>\nBill Hart <goodwillhart@googlemail.com>\n\t\n\t\nThis proposal is absolutely correct. It is *exactly* what I would do,\nwith one exception. I would not issue a warning that MPQS is going to\nstart, unless the factorisation is over say 70 digits (~90s).\n\nBill.\n```\n",
    "created_at": "2007-11-12T12:24:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6959",
    "user": "@williamstein"
}
```

Comments from some experts:

```

On 12/11/2007, Robert Bradshaw <robertwb@math.washington.edu> wrote:
> I don't have much expertise in the area, but it looks like a sound
> proposal to me. The trial division bound seems a bit low (and perhaps
> should be adjusted for the size of the input). Is this similar to
> what Pari does? Would it make sense to parallelize ECM/QS by default
> on a multi-core system?
>
> - Robert
>
Bill Hart <goodwillhart@googlemail.com>
	
	
This proposal is absolutely correct. It is *exactly* what I would do,
with one exception. I would not issue a warning that MPQS is going to
start, unless the factorisation is over say 70 digits (~90s).

Bill.
```




---

archive/issue_comments_006960.json:
```json
{
    "body": "I've just discussed this with Paul Zimmerman and here is what we should do (eventually):\n\n1) Trial factoring for primes up to ~1000\n2) SQUFOF for numbers up to ~32-40 bits (use the fast implementation in FLINT - it's 4x faster than anything else)\n3) Pollard Rho if we have an efficient implementation\n4) tinyQS in FLINT *if* the number of digits is small enough, i.e. if that is going to be faster than GMP-ECM (we have to profile this to determine the cutoff)\n5) GMP-ECM with bound up to n^(1/3)\n6) p-1 and p+1 with large bound (it works rarely, but saves MPQS if it happens to work - the runtime compared to MPQS is *tiny*)\n7) MPQS up to ~90 digits if large prime variant, ~100 digits if double large prime variant or ~130 digits if triple large prime variant QS\n8) GNFS \n9) You are the NSA, so you know what to do.",
    "created_at": "2007-11-12T14:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6960",
    "user": "wbhart"
}
```

I've just discussed this with Paul Zimmerman and here is what we should do (eventually):

1) Trial factoring for primes up to ~1000
2) SQUFOF for numbers up to ~32-40 bits (use the fast implementation in FLINT - it's 4x faster than anything else)
3) Pollard Rho if we have an efficient implementation
4) tinyQS in FLINT *if* the number of digits is small enough, i.e. if that is going to be faster than GMP-ECM (we have to profile this to determine the cutoff)
5) GMP-ECM with bound up to n^(1/3)
6) p-1 and p+1 with large bound (it works rarely, but saves MPQS if it happens to work - the runtime compared to MPQS is *tiny*)
7) MPQS up to ~90 digits if large prime variant, ~100 digits if double large prime variant or ~130 digits if triple large prime variant QS
8) GNFS 
9) You are the NSA, so you know what to do.



---

archive/issue_comments_006961.json:
```json
{
    "body": "Steps 2) and 3) of my original proposal might be easily implemented using the \"finer ECM interface\" proposed in #1421.",
    "created_at": "2007-12-17T12:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6961",
    "user": "@zimmermann6"
}
```

Steps 2) and 3) of my original proposal might be easily implemented using the "finer ECM interface" proposed in #1421.



---

archive/issue_comments_006962.json:
```json
{
    "body": "Changing assignee from @williamstein to tbd.",
    "created_at": "2009-07-20T19:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6962",
    "user": "@loefflerd"
}
```

Changing assignee from @williamstein to tbd.



---

archive/issue_comments_006963.json:
```json
{
    "body": "Changing component from number theory to factorization.",
    "created_at": "2009-07-20T19:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6963",
    "user": "@loefflerd"
}
```

Changing component from number theory to factorization.



---

archive/issue_comments_006964.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-02-05T20:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6964",
    "user": "@zimmermann6"
}
```

Resolution: wontfix



---

archive/issue_comments_006965.json:
```json
{
    "body": "since no progress was done in 2 years, I close that ticket.",
    "created_at": "2010-02-05T20:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6965",
    "user": "@zimmermann6"
}
```

since no progress was done in 2 years, I close that ticket.



---

archive/issue_comments_006966.json:
```json
{
    "body": "Make sure you understand the procedure for closing tickets. See [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) of the Developer's Guide for more information.",
    "created_at": "2010-02-05T21:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6966",
    "user": "mvngu"
}
```

Make sure you understand the procedure for closing tickets. See [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) of the Developer's Guide for more information.



---

archive/issue_comments_006967.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-02-05T21:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6967",
    "user": "@robertwb"
}
```

Changing status from closed to new.



---

archive/issue_comments_006968.json:
```json
{
    "body": "This is still an issue--I have code that I need to clean up and post here (though probably won't get around to it 'till this summer).",
    "created_at": "2010-02-05T21:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6968",
    "user": "@robertwb"
}
```

This is still an issue--I have code that I need to clean up and post here (though probably won't get around to it 'till this summer).



---

archive/issue_comments_006969.json:
```json
{
    "body": "Resolution changed from wontfix to ",
    "created_at": "2010-02-05T21:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6969",
    "user": "@robertwb"
}
```

Resolution changed from wontfix to 



---

archive/issue_comments_006970.json:
```json
{
    "body": "> Make sure you understand the procedure for closing tickets. \n\nsorry, I wasn't aware of that.",
    "created_at": "2010-02-07T21:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6970",
    "user": "@zimmermann6"
}
```

> Make sure you understand the procedure for closing tickets. 

sorry, I wasn't aware of that.



---

archive/issue_comments_006971.json:
```json
{
    "body": "Changing assignee from tbd to @a-andre.",
    "created_at": "2010-11-17T16:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6971",
    "user": "@a-andre"
}
```

Changing assignee from tbd to @a-andre.



---

archive/issue_comments_006972.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-19T15:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6972",
    "user": "@a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_006973.json:
```json
{
    "body": "Attachment [evaluate_1145.sage](tarball://root/attachments/some-uuid/ticket1145/evaluate_1145.sage) by @a-andre created at 2010-11-19 15:18:02\n\nApply first: #5945, #5310\n\nPatch makes use of SQUFOF, ecmfactor, cunningham_table and sympy.factorint.\n\nTo pass all tests cunningham database should become a standard package or the warning in cunningham_tables.py should be removed.\n\nTo evalutate run attachment:evaluate_1145.sage\n\nThis should also fix #9463.",
    "created_at": "2010-11-19T15:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6973",
    "user": "@a-andre"
}
```

Attachment [evaluate_1145.sage](tarball://root/attachments/some-uuid/ticket1145/evaluate_1145.sage) by @a-andre created at 2010-11-19 15:18:02

Apply first: #5945, #5310

Patch makes use of SQUFOF, ecmfactor, cunningham_table and sympy.factorint.

To pass all tests cunningham database should become a standard package or the warning in cunningham_tables.py should be removed.

To evalutate run attachment:evaluate_1145.sage

This should also fix #9463.



---

archive/issue_comments_006974.json:
```json
{
    "body": "I have personally been considering moving all the integer factorisation code to a new module.  I think it makes sense because a lot of new code is being added and `sage/rings/integer.pyx` is already large enough.\n\nWhat do you think?",
    "created_at": "2010-11-19T22:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6974",
    "user": "@jdemeyer"
}
```

I have personally been considering moving all the integer factorisation code to a new module.  I think it makes sense because a lot of new code is being added and `sage/rings/integer.pyx` is already large enough.

What do you think?



---

archive/issue_comments_006975.json:
```json
{
    "body": "+1 to moving all the code to a new factor module. I've just very briefly looked at your code. Also, in terms of code structure, there's no need for all the functions to start with an underscore, and it's probably worth making them cpdef functions for ease of testing. (There's no overhead for module-level methods, as they can't be overridden, so the cdef portion is just as fast.) How does sympy.factorint compare to, say, pari's sieves? What about the quadratic sieve from flint?",
    "created_at": "2010-11-19T23:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6975",
    "user": "@robertwb"
}
```

+1 to moving all the code to a new factor module. I've just very briefly looked at your code. Also, in terms of code structure, there's no need for all the functions to start with an underscore, and it's probably worth making them cpdef functions for ease of testing. (There's no overhead for module-level methods, as they can't be overridden, so the cdef portion is just as fast.) How does sympy.factorint compare to, say, pari's sieves? What about the quadratic sieve from flint?



---

archive/issue_comments_006976.json:
```json
{
    "body": "Okay, I will move the code to a new module. How should it be called? Should it stay in `sage/rings`?\n\nsympy.factorint becomes slow very fast but it can handle perfect powers better than other functions.\n\nquadratic sieve from flint is currently not installed, so I couldn't use it.",
    "created_at": "2010-11-20T09:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6976",
    "user": "@a-andre"
}
```

Okay, I will move the code to a new module. How should it be called? Should it stay in `sage/rings`?

sympy.factorint becomes slow very fast but it can handle perfect powers better than other functions.

quadratic sieve from flint is currently not installed, so I couldn't use it.



---

archive/issue_comments_006977.json:
```json
{
    "body": "Replying to [comment:16 aapitzsch]:\n> Okay, I will move the code to a new module. How should it be called? Should it stay in `sage/rings`?\n> \n> sympy.factorint becomes slow very fast but it can handle perfect powers better than other functions.\n\nPersonally, I wouldn't care that much about huge perfect powers.  I agree with the PARI people that this is essentially a non-issue.",
    "created_at": "2010-11-20T09:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6977",
    "user": "@jdemeyer"
}
```

Replying to [comment:16 aapitzsch]:
> Okay, I will move the code to a new module. How should it be called? Should it stay in `sage/rings`?
> 
> sympy.factorint becomes slow very fast but it can handle perfect powers better than other functions.

Personally, I wouldn't care that much about huge perfect powers.  I agree with the PARI people that this is essentially a non-issue.



---

archive/issue_comments_006978.json:
```json
{
    "body": "Replying to [comment:16 aapitzsch]:\n> Okay, I will move the code to a new module. How should it be called? Should it stay in `sage/rings`?\n\nI would call it `sage/rings/factorint.pyx` or so.  It would be nice if you would move *all* the integer factoring code there, not only the newly added code.\n\nI would love to help with this ticket, but I'm already involved in too many tickets...",
    "created_at": "2010-11-20T09:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6978",
    "user": "@jdemeyer"
}
```

Replying to [comment:16 aapitzsch]:
> Okay, I will move the code to a new module. How should it be called? Should it stay in `sage/rings`?

I would call it `sage/rings/factorint.pyx` or so.  It would be nice if you would move *all* the integer factoring code there, not only the newly added code.

I would love to help with this ticket, but I'm already involved in too many tickets...



---

archive/issue_comments_006979.json:
```json
{
    "body": "Perfect power checking doesn't cost that much but it improves considerably the speed if it's a perfect power.",
    "created_at": "2010-11-20T09:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6979",
    "user": "@a-andre"
}
```

Perfect power checking doesn't cost that much but it improves considerably the speed if it's a perfect power.



---

archive/issue_comments_006980.json:
```json
{
    "body": "Replying to [comment:19 aapitzsch]:\n> Perfect power checking doesn't cost that much but it improves considerably the speed if it's a perfect power.\n\nTrial division doesn't cost that much but it improves considerably the speed if it has lots of small factors.\n\nNow guess which is more likely for a random number...",
    "created_at": "2010-11-20T09:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6980",
    "user": "@jdemeyer"
}
```

Replying to [comment:19 aapitzsch]:
> Perfect power checking doesn't cost that much but it improves considerably the speed if it's a perfect power.

Trial division doesn't cost that much but it improves considerably the speed if it has lots of small factors.

Now guess which is more likely for a random number...



---

archive/issue_comments_006981.json:
```json
{
    "body": "Besides, if you want to check for a power, just check for a perfect power.  No need to call sympy.factorint() for that.",
    "created_at": "2010-11-20T09:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6981",
    "user": "@jdemeyer"
}
```

Besides, if you want to check for a power, just check for a perfect power.  No need to call sympy.factorint() for that.



---

archive/issue_comments_006982.json:
```json
{
    "body": "That's what I do.\n\n```\nif n.is_power(): \n    from sympy import factorint \n    return [(Integer(p),e) for p,e in factorint(n).items()]\n```\n",
    "created_at": "2010-11-20T09:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6982",
    "user": "@a-andre"
}
```

That's what I do.

```
if n.is_power(): 
    from sympy import factorint 
    return [(Integer(p),e) for p,e in factorint(n).items()]
```




---

archive/issue_comments_006983.json:
```json
{
    "body": "That doesn't look good.  If `n` is a power, you should write `n` as `b^k` and then factor `b` and multiply all exponents by `k` instead of using the slower `sympy.factorint()`.",
    "created_at": "2010-11-20T10:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6983",
    "user": "@jdemeyer"
}
```

That doesn't look good.  If `n` is a power, you should write `n` as `b^k` and then factor `b` and multiply all exponents by `k` instead of using the slower `sympy.factorint()`.



---

archive/issue_comments_006984.json:
```json
{
    "body": "Replying to [comment:16 aapitzsch]:\n> Okay, I will move the code to a new module. How should it be called? Should it stay in `sage/rings`?\n\nYes, that'd be a fine place for it. \n\n> sympy.factorint becomes slow very fast but it can handle perfect powers better than other functions.\n\nThen -1 from moving away from Pari. We can check for perfect powers very quickly using gmp/mpir first. \n\n> quadratic sieve from flint is currently not installed, so I couldn't use it.\n\nWell, expect some followup patches then :). \n\n- Robert",
    "created_at": "2010-11-20T22:37:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6984",
    "user": "@robertwb"
}
```

Replying to [comment:16 aapitzsch]:
> Okay, I will move the code to a new module. How should it be called? Should it stay in `sage/rings`?

Yes, that'd be a fine place for it. 

> sympy.factorint becomes slow very fast but it can handle perfect powers better than other functions.

Then -1 from moving away from Pari. We can check for perfect powers very quickly using gmp/mpir first. 

> quadratic sieve from flint is currently not installed, so I couldn't use it.

Well, expect some followup patches then :). 

- Robert



---

archive/issue_comments_006985.json:
```json
{
    "body": "I moved the integer factorization code to factorint.pyx. The patch is attached to #5945 because adding *factor_using_flint* is a minor change than this one, so review should be easier.\n\nCurrently `arith.factor` links to `factorint.factor`. We can create a ticket to get rid of it after fixing #5945. But for now it would be to much I think.",
    "created_at": "2010-11-22T16:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6985",
    "user": "@a-andre"
}
```

I moved the integer factorization code to factorint.pyx. The patch is attached to #5945 because adding *factor_using_flint* is a minor change than this one, so review should be easier.

Currently `arith.factor` links to `factorint.factor`. We can create a ticket to get rid of it after fixing #5945. But for now it would be to much I think.



---

archive/issue_comments_006986.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-03T09:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6986",
    "user": "@a-andre"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_006987.json:
```json
{
    "body": "Attachment [trac_1145_cunningham_warning.patch](tarball://root/attachments/some-uuid/ticket1145/trac_1145_cunningham_warning.patch) by @a-andre created at 2010-12-07 15:56:41",
    "created_at": "2010-12-07T15:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6987",
    "user": "@a-andre"
}
```

Attachment [trac_1145_cunningham_warning.patch](tarball://root/attachments/some-uuid/ticket1145/trac_1145_cunningham_warning.patch) by @a-andre created at 2010-12-07 15:56:41



---

archive/issue_comments_006988.json:
```json
{
    "body": "I changed the things mentioned above.",
    "created_at": "2010-12-07T16:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6988",
    "user": "@a-andre"
}
```

I changed the things mentioned above.



---

archive/issue_comments_006989.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-12-07T16:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6989",
    "user": "@a-andre"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_006990.json:
```json
{
    "body": "if somebody wants to add GNFS to the list of algorithms available from Sage,\nCADO-NFS 1.0 was just released: http://cado-nfs.gforge.inria.fr/",
    "created_at": "2010-12-10T12:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6990",
    "user": "@zimmermann6"
}
```

if somebody wants to add GNFS to the list of algorithms available from Sage,
CADO-NFS 1.0 was just released: http://cado-nfs.gforge.inria.fr/



---

archive/issue_comments_006991.json:
```json
{
    "body": "Depends on #5310 and #5945\n\nApply trac_1145_integer_factorization.patch and trac_1145_cunningham_warning.patch",
    "created_at": "2010-12-17T22:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6991",
    "user": "@robertwb"
}
```

Depends on #5310 and #5945

Apply trac_1145_integer_factorization.patch and trac_1145_cunningham_warning.patch



---

archive/issue_comments_006992.json:
```json
{
    "body": "Attachment [trac_1145_integer_factorization.patch](tarball://root/attachments/some-uuid/ticket1145/trac_1145_integer_factorization.patch) by @zimmermann6 created at 2011-06-17 09:39:26\n\nYafu (http://sourceforge.net/projects/yafu/) might be an interesting software to include,\nalthough I have difficulties finding its license. It includes a multi-thread implementation\nof SIQS, which might be interesting in the 70-100 digit range.\n\nPaul Zimmermann",
    "created_at": "2011-06-17T09:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6992",
    "user": "@zimmermann6"
}
```

Attachment [trac_1145_integer_factorization.patch](tarball://root/attachments/some-uuid/ticket1145/trac_1145_integer_factorization.patch) by @zimmermann6 created at 2011-06-17 09:39:26

Yafu (http://sourceforge.net/projects/yafu/) might be an interesting software to include,
although I have difficulties finding its license. It includes a multi-thread implementation
of SIQS, which might be interesting in the 70-100 digit range.

Paul Zimmermann



---

archive/issue_comments_006993.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-01-05T10:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6993",
    "user": "@roed314"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_006994.json:
```json
{
    "body": "I know that it's waiting on #5310, but your patch is doubled: you exported to a file that already contained the patch.  Also, we should figure out how to merge these factoring improvements with those in #12125 and #12133; it shouldn't be too hard.\n\nA couple other comments: you should use the `perfect_power` method of Integers rather than writing your own base_exponent, and you should pass on the `use_pollard` parameter when you recurse.",
    "created_at": "2012-01-05T10:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6994",
    "user": "@roed314"
}
```

I know that it's waiting on #5310, but your patch is doubled: you exported to a file that already contained the patch.  Also, we should figure out how to merge these factoring improvements with those in #12125 and #12133; it shouldn't be too hard.

A couple other comments: you should use the `perfect_power` method of Integers rather than writing your own base_exponent, and you should pass on the `use_pollard` parameter when you recurse.



---

archive/issue_comments_006995.json:
```json
{
    "body": "See also #14970",
    "created_at": "2013-07-25T11:57:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1145",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1145#issuecomment-6995",
    "user": "@mstreng"
}
```

See also #14970

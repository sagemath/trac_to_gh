# Issue 8162: p-adic ring constructor documentation incorrect

archive/issues_008162.json:
```json
{
    "body": "Assignee: @roed314\n\nCC:  @roed314\n\nAccording to the documentation for Zq, the following code should construct the degree 3 unramified extension of the 5-adic integers, but fails.\n\n\n```\nsage: R = Zq([(5,3)], names=\"alpha\")\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/dmharvey/<ipython console> in <module>()\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/padics/factory.pyc in Zq(q, prec, type, modulus, names, print_mode, halt, ram_name, res_name, print_pos, print_sep, print_max_ram_terms, print_max_unram_terms, print_max_terse_terms, check)\n   1915     if check:\n   1916         if not isinstance(q, Integer):\n-> 1917             q = Integer(q)\n   1918         if not isinstance(prec, Integer):\n   1919             prec = Integer(prec)\n\n/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6820)()\n\nTypeError: unable to coerce <type 'list'> to an integer\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8162\n\n",
    "created_at": "2010-02-03T02:43:38Z",
    "labels": [
        "component: padics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.2",
    "title": "p-adic ring constructor documentation incorrect",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8162",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @roed314

CC:  @roed314

According to the documentation for Zq, the following code should construct the degree 3 unramified extension of the 5-adic integers, but fails.


```
sage: R = Zq([(5,3)], names="alpha")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/dmharvey/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/padics/factory.pyc in Zq(q, prec, type, modulus, names, print_mode, halt, ram_name, res_name, print_pos, print_sep, print_max_ram_terms, print_max_unram_terms, print_max_terse_terms, check)
   1915     if check:
   1916         if not isinstance(q, Integer):
-> 1917             q = Integer(q)
   1918         if not isinstance(prec, Integer):
   1919             prec = Integer(prec)

/usr/local/sage/local/lib/python2.6/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6820)()

TypeError: unable to coerce <type 'list'> to an integer
```



Issue created by migration from https://trac.sagemath.org/ticket/8162





---

archive/issue_comments_071673.json:
```json
{
    "body": "Attachment [8162.patch](tarball://root/attachments/some-uuid/ticket8162/8162.patch) by @roed314 created at 2011-11-09 03:42:58",
    "created_at": "2011-11-09T03:42:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71673",
    "user": "https://github.com/roed314"
}
```

Attachment [8162.patch](tarball://root/attachments/some-uuid/ticket8162/8162.patch) by @roed314 created at 2011-11-09 03:42:58



---

archive/issue_comments_071674.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-11-09T03:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71674",
    "user": "https://github.com/roed314"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071675.json:
```json
{
    "body": "Wouldn't it be better to have a pair as input, rather than a list whose only element is a pair?",
    "created_at": "2011-11-14T14:44:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71675",
    "user": "https://trac.sagemath.org/admin/accounts/users/johanbosman"
}
```

Wouldn't it be better to have a pair as input, rather than a list whose only element is a pair?



---

archive/issue_comments_071676.json:
```json
{
    "body": "The reason to use a list with a pair in it is so that the you can also pass in a factorization object.",
    "created_at": "2011-11-14T15:15:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71676",
    "user": "https://github.com/roed314"
}
```

The reason to use a list with a pair in it is so that the you can also pass in a factorization object.



---

archive/issue_comments_071677.json:
```json
{
    "body": "Ah, I see.  Yet, there is still a lot of room for improvement here.  The code doesn't check that the list has only 1 element.  And it would also be a lot better if it accepted a bare 2-tuple as well.",
    "created_at": "2011-11-30T21:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71677",
    "user": "https://trac.sagemath.org/admin/accounts/users/johanbosman"
}
```

Ah, I see.  Yet, there is still a lot of room for improvement here.  The code doesn't check that the list has only 1 element.  And it would also be a lot better if it accepted a bare 2-tuple as well.



---

archive/issue_comments_071678.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-11-30T21:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71678",
    "user": "https://trac.sagemath.org/admin/accounts/users/johanbosman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071679.json:
```json
{
    "body": "Attachment [8162.2.patch](tarball://root/attachments/some-uuid/ticket8162/8162.2.patch) by @roed314 created at 2011-12-12 15:28:05\n\nI changed the requirement that check=False.\n\nApply only 8162.patch.",
    "created_at": "2011-12-12T15:28:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71679",
    "user": "https://github.com/roed314"
}
```

Attachment [8162.2.patch](tarball://root/attachments/some-uuid/ticket8162/8162.2.patch) by @roed314 created at 2011-12-12 15:28:05

I changed the requirement that check=False.

Apply only 8162.patch.



---

archive/issue_comments_071680.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-12-12T15:28:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71680",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071681.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-12-19T00:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71681",
    "user": "https://github.com/saraedum"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071682.json:
```json
{
    "body": "I guess one should apply 8162.2.patch.\n\nEven though I read the comment above I don't understand under which circumstances one would get a list of the form [(p,n)]. If you factor some q you get a factorization object. If you select one of its coefficients you get a tuple. The only way I could think of is casting a factorization to a list but would this really be useful?\n\nI also find the use of 'check' confusing. One would expect 'check' to actually check whether q is a prime power (which probably the ExtensionFactory does, I haven't checked). Here it is also used to disable some of the input formats:\n\n\n```\nsage: k.<alpha> = Qq((2,1)) #works\nsage: k.<alpha> = Qq((2,1),check=False)\nTypeError: 'sage.rings.integer.Integer' object does not support indexing\n```\n\n\nSo, something that works with check does not work without check anymore.\n\nI can go ahead and fix these issues if you don't mind.",
    "created_at": "2011-12-19T00:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71682",
    "user": "https://github.com/saraedum"
}
```

I guess one should apply 8162.2.patch.

Even though I read the comment above I don't understand under which circumstances one would get a list of the form [(p,n)]. If you factor some q you get a factorization object. If you select one of its coefficients you get a tuple. The only way I could think of is casting a factorization to a list but would this really be useful?

I also find the use of 'check' confusing. One would expect 'check' to actually check whether q is a prime power (which probably the ExtensionFactory does, I haven't checked). Here it is also used to disable some of the input formats:


```
sage: k.<alpha> = Qq((2,1)) #works
sage: k.<alpha> = Qq((2,1),check=False)
TypeError: 'sage.rings.integer.Integer' object does not support indexing
```


So, something that works with check does not work without check anymore.

I can go ahead and fix these issues if you don't mind.



---

archive/issue_comments_071683.json:
```json
{
    "body": "Yeah, that was a typo: apply only 8162.2.patch.\n\nI can't think of a good reason to allow a list, but also no particular reason not to allow it, since lists are a common container for objects in Python.  :-)\n\nAs for the check parameter, my interpretation of check=False is that it only accepts input of a particular format in order to minimize the time spent in handling different input formats.  So I think it's completely reasonable for your example to fail when you don't pass in something of the form [(p, k)].\n\nSo I guess my conclusion is that I don't think the issues you're pointing out are problems.",
    "created_at": "2011-12-19T00:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71683",
    "user": "https://github.com/roed314"
}
```

Yeah, that was a typo: apply only 8162.2.patch.

I can't think of a good reason to allow a list, but also no particular reason not to allow it, since lists are a common container for objects in Python.  :-)

As for the check parameter, my interpretation of check=False is that it only accepts input of a particular format in order to minimize the time spent in handling different input formats.  So I think it's completely reasonable for your example to fail when you don't pass in something of the form [(p, k)].

So I guess my conclusion is that I don't think the issues you're pointing out are problems.



---

archive/issue_comments_071684.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd35\".",
    "created_at": "2011-12-21T15:24:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71684",
    "user": "https://github.com/saraedum"
}
```

Changing keywords from "" to "sd35".



---

archive/issue_comments_071685.json:
```json
{
    "body": "Any further thoughts?  I don't think we currently have agreement on what to do with this ticket, so I don't think \"needs work\" is the right classification.",
    "created_at": "2012-01-04T11:22:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71685",
    "user": "https://github.com/roed314"
}
```

Any further thoughts?  I don't think we currently have agreement on what to do with this ticket, so I don't think "needs work" is the right classification.



---

archive/issue_comments_071686.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2012-01-04T11:22:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71686",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_071687.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-03-03T00:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71687",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_071688.json:
```json
{
    "body": "Attachment [trac_8162.patch](tarball://root/attachments/some-uuid/ticket8162/trac_8162.patch) by @saraedum created at 2012-11-19 21:01:31\n\nReplying to [comment:7 roed]:\n> I can't think of a good reason to allow a list, but also no particular reason not to allow it, since lists are a common container for objects in Python.  :-)\nSure, this makes sense.\n\n> As for the check parameter, my interpretation of check=False is that it only accepts input of a particular format in order to minimize the time spent in handling different input formats.  So I think it's completely reasonable for your example to fail when you don't pass in something of the form [(p, k)].\nI mostly agree with you. I think that with `check=False` nothing should be done that could be expensive (things like checking whether a minimal polynomial is actually irreducible). However, I believe that `check` should not have an influence on the interface.\n\nI adapted your patch to only make the check trigger whether we check that `p` is actually a prime. All the other checks are just `isinstance` and `len` checks which come essentially for free.\n\nI looked at some timings and the two versions don't really seem to differ with `q=(p,k)` and `check=False`.\n\nWould this patch be acceptable for you?\n\n[I haven't run full doctests yet, so let me see if the patchbot at least likes it.]",
    "created_at": "2012-11-19T21:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71688",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_8162.patch](tarball://root/attachments/some-uuid/ticket8162/trac_8162.patch) by @saraedum created at 2012-11-19 21:01:31

Replying to [comment:7 roed]:
> I can't think of a good reason to allow a list, but also no particular reason not to allow it, since lists are a common container for objects in Python.  :-)
Sure, this makes sense.

> As for the check parameter, my interpretation of check=False is that it only accepts input of a particular format in order to minimize the time spent in handling different input formats.  So I think it's completely reasonable for your example to fail when you don't pass in something of the form [(p, k)].
I mostly agree with you. I think that with `check=False` nothing should be done that could be expensive (things like checking whether a minimal polynomial is actually irreducible). However, I believe that `check` should not have an influence on the interface.

I adapted your patch to only make the check trigger whether we check that `p` is actually a prime. All the other checks are just `isinstance` and `len` checks which come essentially for free.

I looked at some timings and the two versions don't really seem to differ with `q=(p,k)` and `check=False`.

Would this patch be acceptable for you?

[I haven't run full doctests yet, so let me see if the patchbot at least likes it.]



---

archive/issue_comments_071689.json:
```json
{
    "body": "Apply only trac_8162.patch",
    "created_at": "2012-11-19T21:02:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71689",
    "user": "https://github.com/saraedum"
}
```

Apply only trac_8162.patch



---

archive/issue_comments_071690.json:
```json
{
    "body": "The startup plugin says that the startup time might have increased. However, the functions this patch touches are not executed on startup, so this should only be noise.",
    "created_at": "2013-01-22T00:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71690",
    "user": "https://github.com/saraedum"
}
```

The startup plugin says that the startup time might have increased. However, the functions this patch touches are not executed on startup, so this should only be noise.



---

archive/issue_comments_071691.json:
```json
{
    "body": "Patch applies fine with 6.2.beta5. One doctest fail (an aged patchbot run was fine):\n\n```\nFile \"src/sage/rings/padics/factory.py\", line 1953, in sage.rings.padics.factory.?\nFailed example:\n    R = Zq([(5,3)], names=\"alpha\"); R\nExpected:\n    Unramified Extension of 5-adic Ring with capped absolute precision 20 in alpha defined by (1 + O(5^20))*x^3 + (3 + O(5^20))*x + (3 + O(5^20))\nGot:\n    Unramified Extension of 5-adic Ring with capped absolute precision 20 in alpha defined by (1 + O(5^20))*x^3 + (O(5^20))*x^2 + (3 + O(5^20))*x + (3 + O(5^20))\n```\n",
    "created_at": "2014-03-31T14:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71691",
    "user": "https://github.com/rwst"
}
```

Patch applies fine with 6.2.beta5. One doctest fail (an aged patchbot run was fine):

```
File "src/sage/rings/padics/factory.py", line 1953, in sage.rings.padics.factory.?
Failed example:
    R = Zq([(5,3)], names="alpha"); R
Expected:
    Unramified Extension of 5-adic Ring with capped absolute precision 20 in alpha defined by (1 + O(5^20))*x^3 + (3 + O(5^20))*x + (3 + O(5^20))
Got:
    Unramified Extension of 5-adic Ring with capped absolute precision 20 in alpha defined by (1 + O(5^20))*x^3 + (O(5^20))*x^2 + (3 + O(5^20))*x + (3 + O(5^20))
```




---

archive/issue_comments_071692.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-03-31T14:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71692",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071693.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-04-02T11:23:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71693",
    "user": "https://github.com/saraedum"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071694.json:
```json
{
    "body": "All tests pass now.\n----\nNew commits:",
    "created_at": "2014-04-02T14:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71694",
    "user": "https://github.com/rwst"
}
```

All tests pass now.
----
New commits:



---

archive/issue_comments_071695.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-04-02T14:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71695",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008366.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-04-04T18:52:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8162#event-8366"
}
```



---

archive/issue_comments_071696.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-04-04T18:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8162",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8162#issuecomment-71696",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed

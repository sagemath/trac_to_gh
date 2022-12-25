# Issue 8378: [trivial to fix] typo in documentation of crt

archive/issues_008378.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @JohnCremona @jasongrout\n\n\n```\nsage: crt(15,1,30,4)\n...\nValueError: arguments a and b must be coprime\n```\n\nHowever in the documentation of `crt` a, b are the residues,\nand the moduli are called m, n. Thus the message should be:\n\n```\nValueError: arguments m and n must be coprime\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8378\n\n",
    "created_at": "2010-02-26T10:14:22Z",
    "labels": [
        "component: basic arithmetic",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "[trivial to fix] typo in documentation of crt",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8378",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @aghitza

CC:  @JohnCremona @jasongrout


```
sage: crt(15,1,30,4)
...
ValueError: arguments a and b must be coprime
```

However in the documentation of `crt` a, b are the residues,
and the moduli are called m, n. Thus the message should be:

```
ValueError: arguments m and n must be coprime
```


Issue created by migration from https://trac.sagemath.org/ticket/8378





---

archive/issue_comments_074780.json:
```json
{
    "body": "Attachment [trac_8378.patch](tarball://root/attachments/some-uuid/ticket8378/trac_8378.patch) by @zimmermann6 created at 2010-04-23 10:31:47",
    "created_at": "2010-04-23T10:31:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8378#issuecomment-74780",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_8378.patch](tarball://root/attachments/some-uuid/ticket8378/trac_8378.patch) by @zimmermann6 created at 2010-04-23 10:31:47



---

archive/issue_comments_074781.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-23T10:31:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8378#issuecomment-74781",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074782.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-23T11:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8378#issuecomment-74782",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074783.json:
```json
{
    "body": "Of course this patch is fine (it applies OK to 4.4.alpha1).\n\nLooking at this function and its docstring, though, these thoughts occur to me:\n\n1. If the condition gcd(m,n) is required, it should be documented in the INPUT block (which is missing);  and there should be a test to show what happens when the condition fails.\n2. As we all know, there exists a solution iff gcd(m,n) divides a-b.  So why not generalise the function to allow for this case too?  It would only take a small change to the code, and of course the documentation would also need chenging.  (The solution is unique modulo lcm(m,n), not m*n, in general).\n\nI happen to have just been teaching this!\n\nPaul, if you fancy upgrading your patch, go ahead.  Or you could ask me to do it since I'm the one who has made difficulties!",
    "created_at": "2010-04-23T11:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8378#issuecomment-74783",
    "user": "https://github.com/JohnCremona"
}
```

Of course this patch is fine (it applies OK to 4.4.alpha1).

Looking at this function and its docstring, though, these thoughts occur to me:

1. If the condition gcd(m,n) is required, it should be documented in the INPUT block (which is missing);  and there should be a test to show what happens when the condition fails.
2. As we all know, there exists a solution iff gcd(m,n) divides a-b.  So why not generalise the function to allow for this case too?  It would only take a small change to the code, and of course the documentation would also need chenging.  (The solution is unique modulo lcm(m,n), not m*n, in general).

I happen to have just been teaching this!

Paul, if you fancy upgrading your patch, go ahead.  Or you could ask me to do it since I'm the one who has made difficulties!



---

archive/issue_comments_074784.json:
```json
{
    "body": "John,\n\n> Or you could ask me to do it since I'm the one who has made difficulties!\n\nplease go ahead! By the way, I noticed this while writing a textbook in french about Sage.\nThe textbook currently proposes a function `mycrt` which implements the general case:\n\n```\ndef mycrt(a,b,m,n):\n   g = gcd(m,n)\n   x0 = a % g                                                                   \n   y0 = b % g                                                                   \n   if x0 <> y0:\n      raise ValueError, \"no solution\"\n   return (x0 + g * crt((a-x0)//g,(b-x0)//g,m//g,n//g)) % (n*m//g)              \nsage: mycrt(15,1,30,4)\n45\nsage: mycrt(15,2,30,4)\nTraceback (most recent call last):\n...\nValueError: no solution\n```\n\nIf you implement the general case, I will need to revise the textbook, but this is not a\nproblem... I will be happy to review your patch, but maybe a separate ticket is needed,\notherwise we would both appear as author+reviewer, and I'm not sure the release manager\nwill be happy with that.",
    "created_at": "2010-04-23T11:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8378#issuecomment-74784",
    "user": "https://github.com/zimmermann6"
}
```

John,

> Or you could ask me to do it since I'm the one who has made difficulties!

please go ahead! By the way, I noticed this while writing a textbook in french about Sage.
The textbook currently proposes a function `mycrt` which implements the general case:

```
def mycrt(a,b,m,n):
   g = gcd(m,n)
   x0 = a % g                                                                   
   y0 = b % g                                                                   
   if x0 <> y0:
      raise ValueError, "no solution"
   return (x0 + g * crt((a-x0)//g,(b-x0)//g,m//g,n//g)) % (n*m//g)              
sage: mycrt(15,1,30,4)
45
sage: mycrt(15,2,30,4)
Traceback (most recent call last):
...
ValueError: no solution
```

If you implement the general case, I will need to revise the textbook, but this is not a
problem... I will be happy to review your patch, but maybe a separate ticket is needed,
otherwise we would both appear as author+reviewer, and I'm not sure the release manager
will be happy with that.



---

archive/issue_comments_074785.json:
```json
{
    "body": "Attachment [trac_8378-crt.patch](tarball://root/attachments/some-uuid/ticket8378/trac_8378-crt.patch) by @JohnCremona created at 2010-04-25 10:39:39\n\nreplaces previous;  applies to 4.4.rc0",
    "created_at": "2010-04-25T10:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8378#issuecomment-74785",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_8378-crt.patch](tarball://root/attachments/some-uuid/ticket8378/trac_8378-crt.patch) by @JohnCremona created at 2010-04-25 10:39:39

replaces previous;  applies to 4.4.rc0



---

archive/issue_comments_074786.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-25T10:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8378#issuecomment-74786",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074787.json:
```json
{
    "body": "My patch trac_8378-crt.patch replaces Paul's (though note that it still has Paul's user id in it).  It extends the crt function to handle non-coprime moduli sensibly, with additional doctests.\n\nThis also means that the typo in the error message which Paul's patch fixed has now changed even more, so that in effect the effect of original patch is obsolete.\n\nOne might now argue for a greater change in the title of the ticket, and  a change from the tag \"defect\" to \"enhancement\".  I am not bothered -- I hope Paul does not mind my having totally taking over this ticket!  We probably need an independent review anyway.",
    "created_at": "2010-04-25T10:45:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8378#issuecomment-74787",
    "user": "https://github.com/JohnCremona"
}
```

My patch trac_8378-crt.patch replaces Paul's (though note that it still has Paul's user id in it).  It extends the crt function to handle non-coprime moduli sensibly, with additional doctests.

This also means that the typo in the error message which Paul's patch fixed has now changed even more, so that in effect the effect of original patch is obsolete.

One might now argue for a greater change in the title of the ticket, and  a change from the tag "defect" to "enhancement".  I am not bothered -- I hope Paul does not mind my having totally taking over this ticket!  We probably need an independent review anyway.



---

archive/issue_comments_074788.json:
```json
{
    "body": "By the way, I notice that the way `crt([a1,a2,a3],[m1,m2,m3])` is not documented in\n`crt?`.",
    "created_at": "2010-04-27T12:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8378#issuecomment-74788",
    "user": "https://github.com/zimmermann6"
}
```

By the way, I notice that the way `crt([a1,a2,a3],[m1,m2,m3])` is not documented in
`crt?`.



---

archive/issue_comments_074789.json:
```json
{
    "body": "Attachment [trac_8378-reviewer.patch](tarball://root/attachments/some-uuid/ticket8378/trac_8378-reviewer.patch) by mvngu created at 2010-04-28 11:31:21",
    "created_at": "2010-04-28T11:31:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8378#issuecomment-74789",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8378-reviewer.patch](tarball://root/attachments/some-uuid/ticket8378/trac_8378-reviewer.patch) by mvngu created at 2010-04-28 11:31:21



---

archive/issue_comments_074790.json:
```json
{
    "body": "Reviewer patch has the following changes:\n\n* Explicitly mention the default values.\n* Properly typeset `lcm(m,n)`.\n* Clean up code following the conventions of [PEP 008](http://www.python.org/dev/peps/pep-0008/).\n* The improved documentation of `crt` says that this function also takes a list of residues and a list of moduli. Provide an example to demonstrate this usage.\n* Cross-reference the two functions `crt` and `CRT_list`.\n* The patch [trac_8378-crt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8378/trac_8378-crt.patch) results in two doctest failures in the English and French version of the Sage tutorial. Fix those doctest failures.\n\nIf the reviewer patch gets a positive review, then the whole ticket gets a positive review. I'm happy with [trac_8378-crt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8378/trac_8378-crt.patch). Any one but myself could review my reviewer patch.",
    "created_at": "2010-04-28T11:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8378#issuecomment-74790",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Reviewer patch has the following changes:

* Explicitly mention the default values.
* Properly typeset `lcm(m,n)`.
* Clean up code following the conventions of [PEP 008](http://www.python.org/dev/peps/pep-0008/).
* The improved documentation of `crt` says that this function also takes a list of residues and a list of moduli. Provide an example to demonstrate this usage.
* Cross-reference the two functions `crt` and `CRT_list`.
* The patch [trac_8378-crt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8378/trac_8378-crt.patch) results in two doctest failures in the English and French version of the Sage tutorial. Fix those doctest failures.

If the reviewer patch gets a positive review, then the whole ticket gets a positive review. I'm happy with [trac_8378-crt.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8378/trac_8378-crt.patch). Any one but myself could review my reviewer patch.



---

archive/issue_comments_074791.json:
```json
{
    "body": "Reviewer patch looks good;   testing now.  Thank a lot, Minh, for tidying upwhat I wrote (e.g. when I found that \\lcm was not defined I just did the lazy thing, while you did the proper thing!)",
    "created_at": "2010-04-28T11:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8378#issuecomment-74791",
    "user": "https://github.com/JohnCremona"
}
```

Reviewer patch looks good;   testing now.  Thank a lot, Minh, for tidying upwhat I wrote (e.g. when I found that \lcm was not defined I just did the lazy thing, while you did the proper thing!)



---

archive/issue_comments_074792.json:
```json
{
    "body": "Changing assignee from @aghitza to @JohnCremona.",
    "created_at": "2010-04-28T11:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8378#issuecomment-74792",
    "user": "https://github.com/JohnCremona"
}
```

Changing assignee from @aghitza to @JohnCremona.



---

archive/issue_comments_074793.json:
```json
{
    "body": "Tests pass, so I'm giving this (the review patch) a positive review, hence an overall positive review.",
    "created_at": "2010-04-28T11:53:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8378#issuecomment-74793",
    "user": "https://github.com/JohnCremona"
}
```

Tests pass, so I'm giving this (the review patch) a positive review, hence an overall positive review.



---

archive/issue_comments_074794.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-28T11:53:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8378#issuecomment-74794",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_020085.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-04-29T05:20:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8378",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8378#event-20085"
}
```



---

archive/issue_comments_074795.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T05:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8378",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8378#issuecomment-74795",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed

# Issue 6396: primes_of_degree_one is broken for relative extensions

archive/issues_006396.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @ncalexan\n\nThis is kind of irritating:\n\n```\nsage: N.<a,b> = NumberField([x^2 + 1, x^2 - 5])\nsage: N.primes_of_degree_one_list(10)\n[Fractional ideal (1),\n Fractional ideal (1),\n Fractional ideal (1),\n Fractional ideal (1),\n Fractional ideal (1),\n Fractional ideal (1),\n Fractional ideal (1),\n Fractional ideal (1),\n Fractional ideal (1),\n Fractional ideal (1)]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6396\n\n",
    "created_at": "2009-06-24T17:07:16Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "primes_of_degree_one is broken for relative extensions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6396",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @williamstein

CC:  @ncalexan

This is kind of irritating:

```
sage: N.<a,b> = NumberField([x^2 + 1, x^2 - 5])
sage: N.primes_of_degree_one_list(10)
[Fractional ideal (1),
 Fractional ideal (1),
 Fractional ideal (1),
 Fractional ideal (1),
 Fractional ideal (1),
 Fractional ideal (1),
 Fractional ideal (1),
 Fractional ideal (1),
 Fractional ideal (1),
 Fractional ideal (1)]
```

Issue created by migration from https://trac.sagemath.org/ticket/6396





---

archive/issue_comments_051287.json:
```json
{
    "body": "Here's a patch. Turns out that the bug was due to using the wrong generator. I've set it to use `absolute_generator` rather than `gen`, and patched absolute number fields so `absolute_generator` is an alias for `gen` in that case. The patch also ReSTifies small_primes_of_degree_one.py and adds it to the reference manual.\n\n(Nick, since he wrote the original code.)\n\nDavid",
    "created_at": "2009-06-24T18:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6396#issuecomment-51287",
    "user": "https://github.com/loefflerd"
}
```

Here's a patch. Turns out that the bug was due to using the wrong generator. I've set it to use `absolute_generator` rather than `gen`, and patched absolute number fields so `absolute_generator` is an alias for `gen` in that case. The patch also ReSTifies small_primes_of_degree_one.py and adds it to the reference manual.

(Nick, since he wrote the original code.)

David



---

archive/issue_comments_051288.json:
```json
{
    "body": "This looks good to me, and I am cautiously optimistic that the method will select the same generator on all architectures.  Apply.",
    "created_at": "2009-06-24T18:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6396#issuecomment-51288",
    "user": "https://github.com/ncalexan"
}
```

This looks good to me, and I am cautiously optimistic that the method will select the same generator on all architectures.  Apply.



---

archive/issue_events_015075.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2009-06-24T18:11:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6396",
    "milestone": "sage-4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6396#event-15075"
}
```



---

archive/issue_comments_051289.json:
```json
{
    "body": "Doctest failures when applied to 4.1.alpha1\n\n```\nsage -t -long devel/sage/sage/rings/number_field/small_primes_of_degree_one.py\n**********************************************************************\nFile \"/space/boothby/sage-4.1.alpha1/devel/sage-main/sage/rings/number_field/small_primes_of_degree_one.py\", line 204:\n    sage: N.primes_of_degree_one_list(10)\nExpected:\n    [Fractional ideal ((-1/2*b + 1/2)*a + 2),\n     Fractional ideal (-b*a + 1/2*b + 1/2),\n     Fractional ideal ((1/2*b + 3/2)*a - b),\n     Fractional ideal ((-1/2*b - 3/2)*a + b - 1),\n     Fractional ideal (-b*a - b + 1),\n     Fractional ideal (3*a + 1/2*b - 1/2),\n     Fractional ideal ((-3/2*b + 1/2)*a + 1/2*b - 1/2),\n     Fractional ideal ((-1/2*b - 5/2)*a - b + 1),\n     Fractional ideal (2*a - 3/2*b - 1/2),\n     Fractional ideal (3*a + 1/2*b + 5/2)]\nGot:\n    [Fractional ideal (2*a + 1/2*b - 1/2), Fractional ideal ((-1/2*b - 1/2)*a - b), Fractional ideal (b*a + 1/2*b + 3/2), Fractional ideal ((-1/2*b - 3/2)*a + b - 1), Fractional ideal ((-b + 1)*a + b), Fractional ideal (3*a + 1/2*b - 1/2), Fractional ideal ((1/2*b - 1/2)*a + 3/2*b - 1/2), Fractional ideal ((-1/2*b - 5/2)*a - b + 1), Fractional ideal (2*a - 3/2*b - 1/2), Fractional ideal (3*a + 1/2*b + 5/2)]\n**********************************************************************\n1 items had failures:\n   1 of   8 in __main__.example_5\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /space/boothby/sage-4.1.alpha1/tmp/.doctest_small_primes_of_degree_one.py\n         [3.2 s]\n```",
    "created_at": "2009-06-26T17:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6396#issuecomment-51289",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Doctest failures when applied to 4.1.alpha1

```
sage -t -long devel/sage/sage/rings/number_field/small_primes_of_degree_one.py
**********************************************************************
File "/space/boothby/sage-4.1.alpha1/devel/sage-main/sage/rings/number_field/small_primes_of_degree_one.py", line 204:
    sage: N.primes_of_degree_one_list(10)
Expected:
    [Fractional ideal ((-1/2*b + 1/2)*a + 2),
     Fractional ideal (-b*a + 1/2*b + 1/2),
     Fractional ideal ((1/2*b + 3/2)*a - b),
     Fractional ideal ((-1/2*b - 3/2)*a + b - 1),
     Fractional ideal (-b*a - b + 1),
     Fractional ideal (3*a + 1/2*b - 1/2),
     Fractional ideal ((-3/2*b + 1/2)*a + 1/2*b - 1/2),
     Fractional ideal ((-1/2*b - 5/2)*a - b + 1),
     Fractional ideal (2*a - 3/2*b - 1/2),
     Fractional ideal (3*a + 1/2*b + 5/2)]
Got:
    [Fractional ideal (2*a + 1/2*b - 1/2), Fractional ideal ((-1/2*b - 1/2)*a - b), Fractional ideal (b*a + 1/2*b + 3/2), Fractional ideal ((-1/2*b - 3/2)*a + b - 1), Fractional ideal ((-b + 1)*a + b), Fractional ideal (3*a + 1/2*b - 1/2), Fractional ideal ((1/2*b - 1/2)*a + 3/2*b - 1/2), Fractional ideal ((-1/2*b - 5/2)*a - b + 1), Fractional ideal (2*a - 3/2*b - 1/2), Fractional ideal (3*a + 1/2*b + 5/2)]
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file /space/boothby/sage-4.1.alpha1/tmp/.doctest_small_primes_of_degree_one.py
         [3.2 s]
```



---

archive/issue_comments_051290.json:
```json
{
    "body": "Aargh! Every damn thing we do with ideals seems to return different answers on different platforms -- I've never understood why this is and it's fantastically annoying. The ideals are the same ones, of course, but their string representations are different because Pari picks generators in a totally unpredictable way.\n\nI'll fix this when I get around to it (probably after SD16 is over)\n\nDavid",
    "created_at": "2009-06-26T17:42:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6396#issuecomment-51290",
    "user": "https://github.com/loefflerd"
}
```

Aargh! Every damn thing we do with ideals seems to return different answers on different platforms -- I've never understood why this is and it's fantastically annoying. The ideals are the same ones, of course, but their string representations are different because Pari picks generators in a totally unpredictable way.

I'll fix this when I get around to it (probably after SD16 is over)

David



---

archive/issue_comments_051291.json:
```json
{
    "body": "Attachment [trac_6396-deg1primes.patch](tarball://root/attachments/some-uuid/ticket6396/trac_6396-deg1primes.patch) by @loefflerd created at 2009-06-26 18:05:00",
    "created_at": "2009-06-26T18:05:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6396#issuecomment-51291",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_6396-deg1primes.patch](tarball://root/attachments/some-uuid/ticket6396/trac_6396-deg1primes.patch) by @loefflerd created at 2009-06-26 18:05:00



---

archive/issue_comments_051292.json:
```json
{
    "body": "Can you try this new patch and see if it works better for you? It works on my machine, but then so did the last one, and there is no sage.math binary of 4.0.2 available AFAIK.",
    "created_at": "2009-06-26T18:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6396#issuecomment-51292",
    "user": "https://github.com/loefflerd"
}
```

Can you try this new patch and see if it works better for you? It works on my machine, but then so did the last one, and there is no sage.math binary of 4.0.2 available AFAIK.



---

archive/issue_comments_051293.json:
```json
{
    "body": "BTW: having built myself a 4.1.alpha1 on sage.math overnight, I've checked that it passes doctests there too. Can I just reinstate the positive review now, or does it need to be re-reviewed?",
    "created_at": "2009-06-27T07:48:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6396#issuecomment-51293",
    "user": "https://github.com/loefflerd"
}
```

BTW: having built myself a 4.1.alpha1 on sage.math overnight, I've checked that it passes doctests there too. Can I just reinstate the positive review now, or does it need to be re-reviewed?



---

archive/issue_comments_051294.json:
```json
{
    "body": "Hello? I'm marking this as \"positive review\" so it comes to the attention of the release managers for 4.1.1, who can decide as they see fit what to do given the slightly ambiguous status. All that's needed is for someone to check that the doctests pass on both 64-bit and 32-bit.\n\n(I really would prefer it if this patch didn't hang around bitrotting forever -- this is necessary for a major project I'm working on, which seems to have exposed a remarkable number of bugs; see also #6457, #6458, #6462 and #6463.)",
    "created_at": "2009-07-14T16:43:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6396#issuecomment-51294",
    "user": "https://github.com/loefflerd"
}
```

Hello? I'm marking this as "positive review" so it comes to the attention of the release managers for 4.1.1, who can decide as they see fit what to do given the slightly ambiguous status. All that's needed is for someone to check that the doctests pass on both 64-bit and 32-bit.

(I really would prefer it if this patch didn't hang around bitrotting forever -- this is necessary for a major project I'm working on, which seems to have exposed a remarkable number of bugs; see also #6457, #6458, #6462 and #6463.)



---

archive/issue_comments_051295.json:
```json
{
    "body": "Attachment [trac_6396-reviewer.patch](tarball://root/attachments/some-uuid/ticket6396/trac_6396-reviewer.patch) by mvngu created at 2009-07-16 18:04:09\n\nreviewer patch; fix minor docstring formatting",
    "created_at": "2009-07-16T18:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6396#issuecomment-51295",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6396-reviewer.patch](tarball://root/attachments/some-uuid/ticket6396/trac_6396-reviewer.patch) by mvngu created at 2009-07-16 18:04:09

reviewer patch; fix minor docstring formatting



---

archive/issue_comments_051296.json:
```json
{
    "body": "The patch `trac_6396-reviewer.patch` makes some adjustment to the docstring introduced by `trac_6396-deg1primes.patch`, and fixes some typos therein. All tests passed on sage.math (a 64-bit machine) and on my 32-bit Debian Lenny machine. Just to let people know, both patches have been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(",
    "created_at": "2009-07-16T18:10:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6396#issuecomment-51296",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch `trac_6396-reviewer.patch` makes some adjustment to the docstring introduced by `trac_6396-deg1primes.patch`, and fixes some typos therein. All tests passed on sage.math (a 64-bit machine) and on my 32-bit Debian Lenny machine. Just to let people know, both patches have been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(



---

archive/issue_comments_051297.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-16T21:14:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6396#issuecomment-51297",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_015076.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-16T21:14:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6396",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6396#event-15076"
}
```



---

archive/issue_comments_051298.json:
```json
{
    "body": "See #6806 for a follow up to this ticket.",
    "created_at": "2009-08-22T20:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6396#issuecomment-51298",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See #6806 for a follow up to this ticket.

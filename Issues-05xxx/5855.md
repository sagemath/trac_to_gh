# Issue 5855: [with patch, with positive review] implement squarefree_divisors function

archive/issues_005855.json:
```json
{
    "body": "Assignee: somebody\n\ne.g.\n\n```\nsage: list(squarefree_divisors(12))\n[1, 2, 3, 6]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5855\n\n",
    "closed_at": "2009-04-30T05:51:51Z",
    "created_at": "2009-04-22T15:30:53Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "[with patch, with positive review] implement squarefree_divisors function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5855",
    "user": "https://github.com/rlmill"
}
```
Assignee: somebody

e.g.

```
sage: list(squarefree_divisors(12))
[1, 2, 3, 6]
```

Issue created by migration from https://trac.sagemath.org/ticket/5855





---

archive/issue_comments_046167.json:
```json
{
    "body": "Hmmm, is this supposed to work only for integers? If so, shouldn't it be a method on Integer? You might run into trouble if you apply it to an element of a ring of integers where there are more units than +1 and -1.",
    "created_at": "2009-04-25T01:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5855#issuecomment-46167",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Hmmm, is this supposed to work only for integers? If so, shouldn't it be a method on Integer? You might run into trouble if you apply it to an element of a ring of integers where there are more units than +1 and -1.



---

archive/issue_comments_046168.json:
```json
{
    "body": "Isn't there a lot of stuff in this file (arith.py) like that, though?  I'm not saying dmharvey is wrong, just that there is probably a lot of work to be done with figuring out where all these arithmetic functions go, since a lot of the ones here (e.g. is_prime_power) really are assuming we are working over the standard ring of integers, even though they are top-level in the rings directory.  So it would seem reasonable to add the functionality and then have someone make a new ticket asking for arith.py to be somehow refactored (yet still globally imported).",
    "created_at": "2009-04-26T02:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5855#issuecomment-46168",
    "user": "https://github.com/kcrisman"
}
```

Isn't there a lot of stuff in this file (arith.py) like that, though?  I'm not saying dmharvey is wrong, just that there is probably a lot of work to be done with figuring out where all these arithmetic functions go, since a lot of the ones here (e.g. is_prime_power) really are assuming we are working over the standard ring of integers, even though they are top-level in the rings directory.  So it would seem reasonable to add the functionality and then have someone make a new ticket asking for arith.py to be somehow refactored (yet still globally imported).



---

archive/issue_comments_046169.json:
```json
{
    "body": "Note that is_prime_power explicitly coerces its input to ZZ first, whereas squarefree_divisors doesn't.  \n\nAlso, just because some code wasn't written in a certain way in arith.py long ago, doesn't mean we should continue in that direction now.   You might as well argue that lots of code has no doctests, so \"it would seem reasonable to write lots more code with no doctests and then have someone make a new ticket to add doctests\".  It's the same argument you make above, but with \"doctests\" instead of \"making sense over more general rings\". \n\nRegarding the actual patch, David says \"Hmmm, is this supposed to work only for integers?\".  Note that the first sentence of the docstring says \"Iterator over the squarefree divisors of the integer N.\"\n\nThe only reasonable options seem to be:\n\n1. This should be a method of integers, or\n\n2. The input should be coerced to ZZ, or\n\n3. The function is modified so it works over more general rings, and it is stated in the docs that it is \"squarefree up to units\", and works for any ring where the prime_divisors function works.   Note that prime_divisors works for *any* ring where factor works. \n\n\nI like 3 the best.",
    "created_at": "2009-04-26T05:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5855#issuecomment-46169",
    "user": "https://github.com/williamstein"
}
```

Note that is_prime_power explicitly coerces its input to ZZ first, whereas squarefree_divisors doesn't.  

Also, just because some code wasn't written in a certain way in arith.py long ago, doesn't mean we should continue in that direction now.   You might as well argue that lots of code has no doctests, so "it would seem reasonable to write lots more code with no doctests and then have someone make a new ticket to add doctests".  It's the same argument you make above, but with "doctests" instead of "making sense over more general rings". 

Regarding the actual patch, David says "Hmmm, is this supposed to work only for integers?".  Note that the first sentence of the docstring says "Iterator over the squarefree divisors of the integer N."

The only reasonable options seem to be:

1. This should be a method of integers, or

2. The input should be coerced to ZZ, or

3. The function is modified so it works over more general rings, and it is stated in the docs that it is "squarefree up to units", and works for any ring where the prime_divisors function works.   Note that prime_divisors works for *any* ring where factor works. 


I like 3 the best.



---

archive/issue_comments_046170.json:
```json
{
    "body": "I agree, I prefer (3). Although I'm not sure I completely believe that `prime_divisors` really does the right thing over arbitrary rings, it also seems to have a bias regarding -1.\n\nI also don't like that the `divisors` function returns only positive divisors, but the proposed `squarefree_divisors` returns negative ones as well. I imagine the user would typically want only the positive ones, and they can easily add the negative ones if that's what they want.",
    "created_at": "2009-04-26T11:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5855#issuecomment-46170",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I agree, I prefer (3). Although I'm not sure I completely believe that `prime_divisors` really does the right thing over arbitrary rings, it also seems to have a bias regarding -1.

I also don't like that the `divisors` function returns only positive divisors, but the proposed `squarefree_divisors` returns negative ones as well. I imagine the user would typically want only the positive ones, and they can easily add the negative ones if that's what they want.



---

archive/issue_comments_046171.json:
```json
{
    "body": "Attachment [trac_5855-squarefree_divisors.patch](tarball://root/attachments/some-uuid/ticket5855/trac_5855-squarefree_divisors.patch) by @rlmill created at 2009-04-27 15:18:09",
    "created_at": "2009-04-27T15:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5855#issuecomment-46171",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_5855-squarefree_divisors.patch](tarball://root/attachments/some-uuid/ticket5855/trac_5855-squarefree_divisors.patch) by @rlmill created at 2009-04-27 15:18:09



---

archive/issue_comments_046172.json:
```json
{
    "body": "I'm a bit late to this discussion.  I see that the new funtcion applies, for example, tp ZZ[x], but gives the wrong results because factor() is wrong for that ring:\n\n```\nsage: R.<x> = ZZ[]\nsage: f = 30*x\nsage: f.factor()\n30 * x\n```\nwhich should return 2*3*5*x, if we mean the factors to be irreducibles in th parent ring.  Unless we make a deliberate design decision not to (since then factorization obviously becomes as hard as in ZZ).",
    "created_at": "2009-04-28T17:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5855#issuecomment-46172",
    "user": "https://github.com/JohnCremona"
}
```

I'm a bit late to this discussion.  I see that the new funtcion applies, for example, tp ZZ[x], but gives the wrong results because factor() is wrong for that ring:

```
sage: R.<x> = ZZ[]
sage: f = 30*x
sage: f.factor()
30 * x
```
which should return 2*3*5*x, if we mean the factors to be irreducibles in th parent ring.  Unless we make a deliberate design decision not to (since then factorization obviously becomes as hard as in ZZ).



---

archive/issue_comments_046173.json:
```json
{
    "body": "Thumbs up.\n\nJohn, I agree the results are wrong for ZZ[x], but that should be on a different ticket. (My 2c on that: I think the return value should be 2*3*5*x in your example, because algebraically that makes the most sense. The user should be aware that integer factorisation is hard, and they always have the option to remove the content manually if that suits their application.)",
    "created_at": "2009-04-28T19:03:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5855#issuecomment-46173",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Thumbs up.

John, I agree the results are wrong for ZZ[x], but that should be on a different ticket. (My 2c on that: I think the return value should be 2*3*5*x in your example, because algebraically that makes the most sense. The user should be aware that integer factorisation is hard, and they always have the option to remove the content manually if that suits their application.)



---

archive/issue_comments_046174.json:
```json
{
    "body": "OK for this patch.  FOr the wider issues, here's what I think we should do.  There are several divisor-related functions (including divisors(), square-free-divisors(), and some more) all of which are trivial get from a Factorization object such as is returned by factor() on a large variety of things (not just rings: think of ideal factorizations in number fields, for example).\n\nSo I think the Factorization class should implement all these.  By default they should ignore unit factors (if users know that there are finitely many users they can have a separate iterator over those and multiply).\n\nThen for the most general kind of ring where factorization makes sense (should be a UFD mathematicall) we put in a factor() function which is a placeholder (NotImplemented) together with a few one-line functions which return for example divisors() by just doing self.factor().divisors().  Then for any subsidiary classes which actuall implement factor(), these associated functions are automatically available.\n\nDoes any of that make sense?",
    "created_at": "2009-04-28T19:50:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5855#issuecomment-46174",
    "user": "https://github.com/JohnCremona"
}
```

OK for this patch.  FOr the wider issues, here's what I think we should do.  There are several divisor-related functions (including divisors(), square-free-divisors(), and some more) all of which are trivial get from a Factorization object such as is returned by factor() on a large variety of things (not just rings: think of ideal factorizations in number fields, for example).

So I think the Factorization class should implement all these.  By default they should ignore unit factors (if users know that there are finitely many users they can have a separate iterator over those and multiply).

Then for the most general kind of ring where factorization makes sense (should be a UFD mathematicall) we put in a factor() function which is a placeholder (NotImplemented) together with a few one-line functions which return for example divisors() by just doing self.factor().divisors().  Then for any subsidiary classes which actuall implement factor(), these associated functions are automatically available.

Does any of that make sense?



---

archive/issue_comments_046175.json:
```json
{
    "body": "See #5921 for improved handling of the content in integer poly factorization.  I may not have done the correct cythonic things.",
    "created_at": "2009-04-28T20:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5855#issuecomment-46175",
    "user": "https://github.com/JohnCremona"
}
```

See #5921 for improved handling of the content in integer poly factorization.  I may not have done the correct cythonic things.



---

archive/issue_events_013779.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-30T05:51:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5855",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5855#event-13779"
}
```



---

archive/issue_comments_046176.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T05:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5855#issuecomment-46176",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_046177.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T05:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5855",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5855#issuecomment-46177",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_013780.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-30T05:51:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5855",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5855#event-13780"
}
```

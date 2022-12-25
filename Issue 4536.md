# Issue 4536: Various number field order and ideal utilities

archive/issues_004536.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  m.t.aranes@warwick.ac.uk dl267@cam.ac.uk\n\nKeywords: number fields, orders, ideals\n\nAdditional methods for (fractional) ideals:\n\n1. Ideals cache their norms\n2. Integral ideals now have a residues() iterator\n3. numerator() and denominator() defined for fractional ideals\n4. is_coprime() defined for a fractional ideal & another (or a field element)\n5. euler_phi() defined for integral ideals\n\nAdditional method for orders:\n\n1. coordinates(x) for x in the field gives a vector of rationals expressing x as a linear combination of the order's Z-basis.\n    \n\nIssue created by migration from https://trac.sagemath.org/ticket/4536\n\n",
    "created_at": "2008-11-16T20:47:31Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "Various number field order and ideal utilities",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4536",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

CC:  m.t.aranes@warwick.ac.uk dl267@cam.ac.uk

Keywords: number fields, orders, ideals

Additional methods for (fractional) ideals:

1. Ideals cache their norms
2. Integral ideals now have a residues() iterator
3. numerator() and denominator() defined for fractional ideals
4. is_coprime() defined for a fractional ideal & another (or a field element)
5. euler_phi() defined for integral ideals

Additional method for orders:

1. coordinates(x) for x in the field gives a vector of rationals expressing x as a linear combination of the order's Z-basis.
    

Issue created by migration from https://trac.sagemath.org/ticket/4536





---

archive/issue_comments_033740.json:
```json
{
    "body": "Based on 3.2.rc1",
    "created_at": "2008-11-16T20:48:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4536#issuecomment-33740",
    "user": "https://github.com/JohnCremona"
}
```

Based on 3.2.rc1



---

archive/issue_comments_033741.json:
```json
{
    "body": "Attachment [trac-4536.patch](tarball://root/attachments/some-uuid/ticket4536/trac-4536.patch) by @mwhansen created at 2008-11-17 06:58:05\n\nHi John,\n\nJust one quick comment. Is there a reason you are manually doing the caching instead of using the cached_method decorator in sage/misc/cachefunc.py?  I think the result is a bit cleaner.\n\nAlso, you don't need to use backslashes to continue lines if it occurs with in parens or brackets because Python knows that they need to be closed.\n\n--Mike",
    "created_at": "2008-11-17T06:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4536#issuecomment-33741",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac-4536.patch](tarball://root/attachments/some-uuid/ticket4536/trac-4536.patch) by @mwhansen created at 2008-11-17 06:58:05

Hi John,

Just one quick comment. Is there a reason you are manually doing the caching instead of using the cached_method decorator in sage/misc/cachefunc.py?  I think the result is a bit cleaner.

Also, you don't need to use backslashes to continue lines if it occurs with in parens or brackets because Python knows that they need to be closed.

--Mike



---

archive/issue_comments_033742.json:
```json
{
    "body": "Replying to [comment:1 mhansen]:\n> Hi John,\n> \n> Just one quick comment. Is there a reason you are manually doing the caching instead of using the cached_method decorator in sage/misc/cachefunc.py?  I think the result is a bit cleaner.\n\nQuick answer: it never occurred to me to do it any other way!  But isn't it completely standard in Sage that when an object has a property (such as the norm for an ideal) then one computes it the first time and caches it so that further requests for the property used the cached value?  This is surely different from caching values of a function.\n\n> \n> Also, you don't need to use backslashes to continue lines if it occurs with in parens or brackets because Python knows that they need to be closed.\n\nOK -- I'll remember that for next time (and if I get to revising this patch I'll remove them).\n\nThanks\n\n> \n> --Mike",
    "created_at": "2008-11-17T09:43:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4536#issuecomment-33742",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:1 mhansen]:
> Hi John,
> 
> Just one quick comment. Is there a reason you are manually doing the caching instead of using the cached_method decorator in sage/misc/cachefunc.py?  I think the result is a bit cleaner.

Quick answer: it never occurred to me to do it any other way!  But isn't it completely standard in Sage that when an object has a property (such as the norm for an ideal) then one computes it the first time and caches it so that further requests for the property used the cached value?  This is surely different from caching values of a function.

> 
> Also, you don't need to use backslashes to continue lines if it occurs with in parens or brackets because Python knows that they need to be closed.

OK -- I'll remember that for next time (and if I get to revising this patch I'll remove them).

Thanks

> 
> --Mike



---

archive/issue_comments_033743.json:
```json
{
    "body": "Replying to [comment:2 cremona]:\n> Quick answer: it never occurred to me to do it any other way!  But isn't it completely standard in Sage that when an object has a property (such as the norm for an ideal) then one computes it the first time and caches it so that further requests for the property used the cached value?  This is surely different from caching values of a function.\n\nThe cached_method decorator is relatively new which is why it isn't in use throughout Sage.  For an example, see the groebner_basis method in sage/rings/polynomial/multi_polynomial_ideal.py\n\nThat's exactly what the cached_method decorator does except that it also handles the case where arguments are passed into the method.  The values are cached in a dictionary attribute on the object itself so it gets garbage collected correctly.  It also supports things such as clearing the cache, etc.",
    "created_at": "2008-11-17T11:08:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4536#issuecomment-33743",
    "user": "https://github.com/mwhansen"
}
```

Replying to [comment:2 cremona]:
> Quick answer: it never occurred to me to do it any other way!  But isn't it completely standard in Sage that when an object has a property (such as the norm for an ideal) then one computes it the first time and caches it so that further requests for the property used the cached value?  This is surely different from caching values of a function.

The cached_method decorator is relatively new which is why it isn't in use throughout Sage.  For an example, see the groebner_basis method in sage/rings/polynomial/multi_polynomial_ideal.py

That's exactly what the cached_method decorator does except that it also handles the case where arguments are passed into the method.  The values are cached in a dictionary attribute on the object itself so it gets garbage collected correctly.  It also supports things such as clearing the cache, etc.



---

archive/issue_comments_033744.json:
```json
{
    "body": "Replying to [comment:3 mhansen]:\n> Replying to [comment:2 cremona]:\n> > Quick answer: it never occurred to me to do it any other way!  But isn't it completely standard in Sage that when an object has a property (such as the norm for an ideal) then one computes it the first time and caches it so that further requests for the property used the cached value?  This is surely different from caching values of a function.\n> \n> The cached_method decorator is relatively new which is why it isn't in use throughout Sage.  For an example, see the groebner_basis method in sage/rings/polynomial/multi_polynomial_ideal.py\n> \n> That's exactly what the cached_method decorator does except that it also handles the case where arguments are passed into the method.  The values are cached in a dictionary attribute on the object itself so it gets garbage collected correctly.  It also supports things such as clearing the cache, etc.\n\nThat looks brilliant, and had completely passed me by.  I'll start using it right away!  It would also be a good idea to start to systematically use it all over (wouldn't it) -- then people would see it and use it themselves.",
    "created_at": "2008-11-17T12:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4536#issuecomment-33744",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:3 mhansen]:
> Replying to [comment:2 cremona]:
> > Quick answer: it never occurred to me to do it any other way!  But isn't it completely standard in Sage that when an object has a property (such as the norm for an ideal) then one computes it the first time and caches it so that further requests for the property used the cached value?  This is surely different from caching values of a function.
> 
> The cached_method decorator is relatively new which is why it isn't in use throughout Sage.  For an example, see the groebner_basis method in sage/rings/polynomial/multi_polynomial_ideal.py
> 
> That's exactly what the cached_method decorator does except that it also handles the case where arguments are passed into the method.  The values are cached in a dictionary attribute on the object itself so it gets garbage collected correctly.  It also supports things such as clearing the cache, etc.

That looks brilliant, and had completely passed me by.  I'll start using it right away!  It would also be a good idea to start to systematically use it all over (wouldn't it) -- then people would see it and use it themselves.



---

archive/issue_comments_033745.json:
```json
{
    "body": "Attachment [trac-4526-2.patch](tarball://root/attachments/some-uuid/ticket4536/trac-4526-2.patch) by @JohnCremona created at 2008-11-18 16:11:25\n\nThe second patch trac-4536-2.patch fixes a bug in the first implementation of residues(): I forgot to take the Smith Normal Form of the matrix.  The first of the two new doctests is an example which failed with the old version.",
    "created_at": "2008-11-18T16:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4536#issuecomment-33745",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac-4526-2.patch](tarball://root/attachments/some-uuid/ticket4536/trac-4526-2.patch) by @JohnCremona created at 2008-11-18 16:11:25

The second patch trac-4536-2.patch fixes a bug in the first implementation of residues(): I forgot to take the Smith Normal Form of the matrix.  The first of the two new doctests is an example which failed with the old version.



---

archive/issue_comments_033746.json:
```json
{
    "body": "Patches install and compile fine under 3.2, and all doctests in sage/rings/number_field pass.\n\nBut I'm not happy with the is_coprime() method for fractional ideals. I thought the outcome of the discussion on the sage-nt list was that coprime for fractional ideals means disjoint supports, but I got this:\n\n\n```\nsage: E.<a> = NumberField(x^5 + 7*x^4 + 18*x^2 + x - 3)\nsage: OE = E.ring_of_integers()\nsage: i,j,k = [u[0] for u in factor(3*OE)] # three distinct prime ideals of degrees 3,1,1\nsage: (i/j).is_coprime(j/k)\nTrue\nsage: (j/k).is_coprime(j/k)\nTrue\n```\n\n\nThe problem here is that the fractional ideal j/k has norm 1, and the code falsely assumes that if norm(i) and norm(j) are coprime, then i and j must be coprime. Thus the code will say that j/k is coprime to everything (including itself).",
    "created_at": "2008-11-25T06:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4536#issuecomment-33746",
    "user": "https://github.com/loefflerd"
}
```

Patches install and compile fine under 3.2, and all doctests in sage/rings/number_field pass.

But I'm not happy with the is_coprime() method for fractional ideals. I thought the outcome of the discussion on the sage-nt list was that coprime for fractional ideals means disjoint supports, but I got this:


```
sage: E.<a> = NumberField(x^5 + 7*x^4 + 18*x^2 + x - 3)
sage: OE = E.ring_of_integers()
sage: i,j,k = [u[0] for u in factor(3*OE)] # three distinct prime ideals of degrees 3,1,1
sage: (i/j).is_coprime(j/k)
True
sage: (j/k).is_coprime(j/k)
True
```


The problem here is that the fractional ideal j/k has norm 1, and the code falsely assumes that if norm(i) and norm(j) are coprime, then i and j must be coprime. Thus the code will say that j/k is coprime to everything (including itself).



---

archive/issue_comments_033747.json:
```json
{
    "body": "David, you are quite right.  We could just delete that coprimality of norms pre-test except when the ideals are integral.  I'll correct it and put up a new patch.\n\nThanks for spotting this mistake!",
    "created_at": "2008-11-25T09:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4536#issuecomment-33747",
    "user": "https://github.com/JohnCremona"
}
```

David, you are quite right.  We could just delete that coprimality of norms pre-test except when the ideals are integral.  I'll correct it and put up a new patch.

Thanks for spotting this mistake!



---

archive/issue_comments_033748.json:
```json
{
    "body": "Attachment [trac-4536-fix.patch](tarball://root/attachments/some-uuid/ticket4536/trac-4536-fix.patch) by @JohnCremona created at 2008-11-25 11:46:12",
    "created_at": "2008-11-25T11:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4536#issuecomment-33748",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac-4536-fix.patch](tarball://root/attachments/some-uuid/ticket4536/trac-4536-fix.patch) by @JohnCremona created at 2008-11-25 11:46:12



---

archive/issue_comments_033749.json:
```json
{
    "body": "The new patch trac-4536-fix.patch address the reviewer's just criticism, and adds a relevant doctest.",
    "created_at": "2008-11-25T11:47:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4536#issuecomment-33749",
    "user": "https://github.com/JohnCremona"
}
```

The new patch trac-4536-fix.patch address the reviewer's just criticism, and adds a relevant doctest.



---

archive/issue_comments_033750.json:
```json
{
    "body": "I've found no other problems, and the third patch certainly fixes the issue I reported, so I'll happily give this a positive review.",
    "created_at": "2008-11-26T08:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4536#issuecomment-33750",
    "user": "https://github.com/loefflerd"
}
```

I've found no other problems, and the third patch certainly fixes the issue I reported, so I'll happily give this a positive review.



---

archive/issue_comments_033751.json:
```json
{
    "body": "Merged all three patches in Sage 3.2.1.alpha1",
    "created_at": "2008-11-26T10:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4536#issuecomment-33751",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.2.1.alpha1



---

archive/issue_events_004782.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-26T10:30:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4536",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4536#event-4782"
}
```



---

archive/issue_comments_033752.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-26T10:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4536#issuecomment-33752",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

# Issue 4553: [with patch, with positive review] a few new methods for FiniteFieldElement

archive/issues_004553.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: finite field element\n\nThe attached patch adds a few methods for finite field elements.  It seems as though `.additive_order()` (and therefore `.order()`) was not implemented before (!), so I've implemented that.  I've also implemented pth powers and pth roots, where p is the characteristic of the field.\n\nThese are written pretty naively, so they may not be that fast. If anyone has suggestions for improvements, I'm happy to hear them (or to have you implement them).\n\nIssue created by migration from https://trac.sagemath.org/ticket/4553\n\n",
    "closed_at": "2008-11-25T13:41:46Z",
    "created_at": "2008-11-19T18:05:02Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "[with patch, with positive review] a few new methods for FiniteFieldElement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4553",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: somebody

Keywords: finite field element

The attached patch adds a few methods for finite field elements.  It seems as though `.additive_order()` (and therefore `.order()`) was not implemented before (!), so I've implemented that.  I've also implemented pth powers and pth roots, where p is the characteristic of the field.

These are written pretty naively, so they may not be that fast. If anyone has suggestions for improvements, I'm happy to hear them (or to have you implement them).

Issue created by migration from https://trac.sagemath.org/ticket/4553





---

archive/issue_comments_034061.json:
```json
{
    "body": "Attachment [finitefieldelement.patch](tarball://root/attachments/some-uuid/ticket4553/finitefieldelement.patch) by @jhpalmieri created at 2008-11-19 18:05:19",
    "created_at": "2008-11-19T18:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4553#issuecomment-34061",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [finitefieldelement.patch](tarball://root/attachments/some-uuid/ticket4553/finitefieldelement.patch) by @jhpalmieri created at 2008-11-19 18:05:19



---

archive/issue_events_010369.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2008-11-19T21:51:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4553",
    "milestone": "sage-3.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4553#event-10369"
}
```



---

archive/issue_comments_034062.json:
```json
{
    "body": "That's funny -- in 3.2 I get\n\n```\nsage: a = GF(13^5,'a').gen()\nsage: a.order()\n13\n```\nwhere the function order() is implemented just as in your patch.  But additive_order is not implemented.\n\nI definitely think that this functionality should go in.  But surely a.frobenius() should give `a^q` where q = a.parent().order() and not `a^p` where p = a.parent().characteristic()?  Secondly, you can use a.parent().degree(), there is no need to factor q to get the degree.\n\nLastly, I think it would be more efficient to compute (and cache) the matrix of frobenius as a linear map, viewing F_q as an F_p-vector space of dimension d where `q=p^d`.  I know an efficient way to do this (similar to tricks used in Berlekamp factorization).  Then taking q'th roots would be easy (invert the matrix).\n\nI'm not sure when I'll have time to try doing this!",
    "created_at": "2008-11-22T17:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4553#issuecomment-34062",
    "user": "https://github.com/JohnCremona"
}
```

That's funny -- in 3.2 I get

```
sage: a = GF(13^5,'a').gen()
sage: a.order()
13
```
where the function order() is implemented just as in your patch.  But additive_order is not implemented.

I definitely think that this functionality should go in.  But surely a.frobenius() should give `a^q` where q = a.parent().order() and not `a^p` where p = a.parent().characteristic()?  Secondly, you can use a.parent().degree(), there is no need to factor q to get the degree.

Lastly, I think it would be more efficient to compute (and cache) the matrix of frobenius as a linear map, viewing F_q as an F_p-vector space of dimension d where `q=p^d`.  I know an efficient way to do this (similar to tricks used in Berlekamp factorization).  Then taking q'th roots would be easy (invert the matrix).

I'm not sure when I'll have time to try doing this!



---

archive/issue_comments_034063.json:
```json
{
    "body": "Replying to [comment:2 cremona]:\n> That's funny -- in 3.2 I get\n\n{{{\nsage: a = GF(13^5,'a').gen()\nsage: a.order()\n13\n}}}\n> where the function order() is implemented just as in your patch.  But additive_order is not implemented.\n\n\nI'm not sure why I was thinking that order() wasn't implemented.  Anyway, in sage/structure/element.pyx, it says something like \"don't override order, override additive_order instead\" -- this is for instances of the class ModuleElement, from which FiniteFieldElement inherits.  So I'll produce a new patch that removes order() from finite_field_element.py and has  the definition of additive_order() in element.pyx.\n\n>  I definitely think that this functionality should go in.  But surely\n>  a.frobenius() should give `a^q` where q = a.parent().order() and not\n>  `a^p` where p = a.parent().characteristic()?  \n\n\nBut then the Frobenius map would always be the identity! Also, for what it's worth, both wikipedia and mathworld describe the Frobenius as being the `p`th power map, not the `p^k`th power map.\n\n>Secondly, you can use\n>  a.parent().degree(), there is no need to factor q to get the degree.\n\n\nGood point. I was looking for this sort of thing and hadn't found it. Thanks.\n\n>  Lastly, I think it would be more efficient to compute (and cache) the\n>  matrix of frobenius as a linear map, viewing F_q as an F_p-vector space of\n>  dimension d where `q=p^d`.  I know an efficient way to do this\n>  (similar to tricks used in Berlekamp factorization).  Then taking q'th\n>  roots would be easy (invert the matrix).\n\n>\n>  I'm not sure when I'll have time to try doing this!\n\n\nIs it worth accepting a patch without this efficiency change, and then adding this in later (as a separate ticket)?",
    "created_at": "2008-11-24T03:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4553#issuecomment-34063",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:2 cremona]:
> That's funny -- in 3.2 I get

{{{
sage: a = GF(13^5,'a').gen()
sage: a.order()
13
}}}
> where the function order() is implemented just as in your patch.  But additive_order is not implemented.


I'm not sure why I was thinking that order() wasn't implemented.  Anyway, in sage/structure/element.pyx, it says something like "don't override order, override additive_order instead" -- this is for instances of the class ModuleElement, from which FiniteFieldElement inherits.  So I'll produce a new patch that removes order() from finite_field_element.py and has  the definition of additive_order() in element.pyx.

>  I definitely think that this functionality should go in.  But surely
>  a.frobenius() should give `a^q` where q = a.parent().order() and not
>  `a^p` where p = a.parent().characteristic()?  


But then the Frobenius map would always be the identity! Also, for what it's worth, both wikipedia and mathworld describe the Frobenius as being the `p`th power map, not the `p^k`th power map.

>Secondly, you can use
>  a.parent().degree(), there is no need to factor q to get the degree.


Good point. I was looking for this sort of thing and hadn't found it. Thanks.

>  Lastly, I think it would be more efficient to compute (and cache) the
>  matrix of frobenius as a linear map, viewing F_q as an F_p-vector space of
>  dimension d where `q=p^d`.  I know an efficient way to do this
>  (similar to tricks used in Berlekamp factorization).  Then taking q'th
>  roots would be easy (invert the matrix).

>
>  I'm not sure when I'll have time to try doing this!


Is it worth accepting a patch without this efficiency change, and then adding this in later (as a separate ticket)?



---

archive/issue_comments_034064.json:
```json
{
    "body": "this replaces the other patch",
    "created_at": "2008-11-24T03:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4553#issuecomment-34064",
    "user": "https://github.com/jhpalmieri"
}
```

this replaces the other patch



---

archive/issue_comments_034065.json:
```json
{
    "body": "Attachment [finitefieldelement_new.patch](tarball://root/attachments/some-uuid/ticket4553/finitefieldelement_new.patch) by @JohnCremona created at 2008-11-24 08:58:04\n\nSorry about my silly comment about q'th power against p'th power, I was not thinking.\n\nThe linear algebra approach will have to wait until we have a common interface for all finite fields -- currently the functions available depend on q since they differ according to whether we use givaro or NTL or pari.  (e.g. an element a in GF(q) sometimes has a._coordinates() but not always.  So it's fine to go ahead with this one for now, perhaps with a note that a better implementation might be possible in future.\n\nI hope to review this properly, but Monday morning calls...",
    "created_at": "2008-11-24T08:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4553#issuecomment-34065",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [finitefieldelement_new.patch](tarball://root/attachments/some-uuid/ticket4553/finitefieldelement_new.patch) by @JohnCremona created at 2008-11-24 08:58:04

Sorry about my silly comment about q'th power against p'th power, I was not thinking.

The linear algebra approach will have to wait until we have a common interface for all finite fields -- currently the functions available depend on q since they differ according to whether we use givaro or NTL or pari.  (e.g. an element a in GF(q) sometimes has a._coordinates() but not always.  So it's fine to go ahead with this one for now, perhaps with a note that a better implementation might be possible in future.

I hope to review this properly, but Monday morning calls...



---

archive/issue_comments_034066.json:
```json
{
    "body": "The new patch looks good, applies cleanly to 3.2 and the doctests in both the changed files pass.\n\nAll tests in sage/structure and sage/rings pass.\n\nI say: go for it!",
    "created_at": "2008-11-25T12:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4553#issuecomment-34066",
    "user": "https://github.com/JohnCremona"
}
```

The new patch looks good, applies cleanly to 3.2 and the doctests in both the changed files pass.

All tests in sage/structure and sage/rings pass.

I say: go for it!



---

archive/issue_comments_034067.json:
```json
{
    "body": "Hmm, should we deprecate \"order\" in sage/rings/finite_field_element.py ?\n\nCheers,\n\nMichael",
    "created_at": "2008-11-25T13:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4553#issuecomment-34067",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmm, should we deprecate "order" in sage/rings/finite_field_element.py ?

Cheers,

Michael



---

archive/issue_comments_034068.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-25T13:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4553#issuecomment-34068",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034069.json:
```json
{
    "body": "Merged finitefieldelement_new.patch in Sage 3.2.1.alpha1",
    "created_at": "2008-11-25T13:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4553",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4553#issuecomment-34069",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged finitefieldelement_new.patch in Sage 3.2.1.alpha1



---

archive/issue_events_010370.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-25T13:41:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4553",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4553#event-10370"
}
```

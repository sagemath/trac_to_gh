# Issue 2220: irreducibility testing in relative extensions seems to be messed up

archive/issues_002220.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @ncalexan ccitro @orlitzky\n\nSee http://groups.google.com/group/sage-devel/browse_thread/thread/32fe12de12d5f6a5/c91753b5e65fe7b9#c91753b5e65fe7b9\n\n\n\n```\n> Is the following output for b.gens() correct?\n\n> sage: NumberField([x,x^2-3],'a')\n> Number Field in a0 with defining polynomial x over its base field\n> sage: b=NumberField([x,x^2-3],'a')\n> sage: b.gens()\n> (0, 0)\n\n> To contrast:\n\n> sage: c=NumberField([x^2-3, x^2-2],'a')\n> sage: c.gens()\n> (a0, a1)\n\n> Also, this blows up:\n\n> sage: c=NumberField([x^2-3, x],'a')\n\nThe problem here is that x is triggering a an error in the\nirreducibility test, which is a little bizarre since of course x is\nirreducible.\n\nSo the real issue is: why is x allowed to determine an absolute number\nfield (base Q) but not a relative one?  My guess is that this is a\nside-effect of the differing code being used to test irreducibility in\nthe two cases,\n\nPersonally, I think that trivial extensions should be allowed and\ntreated just as non-trivial ones.  I have recently had to define\nextensions of the ring ZZ, and find this awkward:\n\nsage: R=ZZ.extension(x^2+5,'a')\nsage: R.gens()\n[1, a]\nsage: S=ZZ.extension(x+5,'b')\nsage: S.gens()\n[1]\n\nIn the latter case I need S to remember the polynomial used to\ngeneraite it and would expect its gens() to include (in this case) -5.\n\nOn the same topic, R and S above have no defining_polynomial() method.\n I'll try to fix that if it looks easy. \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2220\n\n",
    "created_at": "2008-02-20T03:54:04Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.8",
    "title": "irreducibility testing in relative extensions seems to be messed up",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2220",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  @ncalexan ccitro @orlitzky

See http://groups.google.com/group/sage-devel/browse_thread/thread/32fe12de12d5f6a5/c91753b5e65fe7b9#c91753b5e65fe7b9



```
> Is the following output for b.gens() correct?

> sage: NumberField([x,x^2-3],'a')
> Number Field in a0 with defining polynomial x over its base field
> sage: b=NumberField([x,x^2-3],'a')
> sage: b.gens()
> (0, 0)

> To contrast:

> sage: c=NumberField([x^2-3, x^2-2],'a')
> sage: c.gens()
> (a0, a1)

> Also, this blows up:

> sage: c=NumberField([x^2-3, x],'a')

The problem here is that x is triggering a an error in the
irreducibility test, which is a little bizarre since of course x is
irreducible.

So the real issue is: why is x allowed to determine an absolute number
field (base Q) but not a relative one?  My guess is that this is a
side-effect of the differing code being used to test irreducibility in
the two cases,

Personally, I think that trivial extensions should be allowed and
treated just as non-trivial ones.  I have recently had to define
extensions of the ring ZZ, and find this awkward:

sage: R=ZZ.extension(x^2+5,'a')
sage: R.gens()
[1, a]
sage: S=ZZ.extension(x+5,'b')
sage: S.gens()
[1]

In the latter case I need S to remember the polynomial used to
generaite it and would expect its gens() to include (in this case) -5.

On the same topic, R and S above have no defining_polynomial() method.
 I'll try to fix that if it looks easy. 
```



Issue created by migration from https://trac.sagemath.org/ticket/2220





---

archive/issue_comments_014677.json:
```json
{
    "body": "As was pointed out (by was I think), the gens() for an extension of ZZ are ZZ-module generators, n in number for an extension of degree n.  For example:\n\n\n```\nsage: R.<a>=ZZ.extension(x^3-2)\nsage: R\nOrder in Number Field in a with defining polynomial x^3 - 2\nsage: R.gens()\n[1, a, a^2]\n```\n\n\nThis is quite clear in the docstring \"returns module generators of this order\" and so requires no action.\n\nFor examples such as this, I said that the following would be convenient to access more directly:\n\n```\nsage: R.fraction_field().gen()\na\nsage: R.fraction_field().defining_polynomial()\nx^3 - 2\n```\n\n\nHowever, objects of the type or R here <class 'sage.rings.number_field.order.AbsoluteOrder'>  might be created in more complicated ways so that they do not have one natural defining polynomial or (ring) generator.  In fact one immediately finds this:\n\n```\nsage: R.ring_generators()\n[a]\n```\n\nand the docstring for ring_generators() gives an example for which more than one generator is needed (remember that not every order is of the form Z[a] for some a), so it makes no sense at all, in general, to define methods gen() or ring_gen() or defining_polynomial() for general orders.\n\nAll this leaves from the original post is to work out why the specific polynomial x is not handled consistently.  The rest is perfect as it is.  Well done to the authors (was and robertb) for doing a good job, well documented!",
    "created_at": "2008-02-20T09:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2220#issuecomment-14677",
    "user": "https://github.com/JohnCremona"
}
```

As was pointed out (by was I think), the gens() for an extension of ZZ are ZZ-module generators, n in number for an extension of degree n.  For example:


```
sage: R.<a>=ZZ.extension(x^3-2)
sage: R
Order in Number Field in a with defining polynomial x^3 - 2
sage: R.gens()
[1, a, a^2]
```


This is quite clear in the docstring "returns module generators of this order" and so requires no action.

For examples such as this, I said that the following would be convenient to access more directly:

```
sage: R.fraction_field().gen()
a
sage: R.fraction_field().defining_polynomial()
x^3 - 2
```


However, objects of the type or R here <class 'sage.rings.number_field.order.AbsoluteOrder'>  might be created in more complicated ways so that they do not have one natural defining polynomial or (ring) generator.  In fact one immediately finds this:

```
sage: R.ring_generators()
[a]
```

and the docstring for ring_generators() gives an example for which more than one generator is needed (remember that not every order is of the form Z[a] for some a), so it makes no sense at all, in general, to define methods gen() or ring_gen() or defining_polynomial() for general orders.

All this leaves from the original post is to work out why the specific polynomial x is not handled consistently.  The rest is perfect as it is.  Well done to the authors (was and robertb) for doing a good job, well documented!



---

archive/issue_comments_014678.json:
```json
{
    "body": "Note that this part now works:\n\n\n```\nsage: c=NumberField([x^2-3, x],'a')\nsage: \nsage: c.gens()\n(a0, 0)\n```\n",
    "created_at": "2009-06-04T21:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2220#issuecomment-14678",
    "user": "https://github.com/mwhansen"
}
```

Note that this part now works:


```
sage: c=NumberField([x^2-3, x],'a')
sage: 
sage: c.gens()
(a0, 0)
```




---

archive/issue_comments_014679.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-20T19:57:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2220#issuecomment-14679",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_014680.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T19:57:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2220#issuecomment-14680",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_014681.json:
```json
{
    "body": "The other part works too now:\n\n\n```\nsage: b = NumberField([x, x^2 - 3], 'a')\nsage: b.gens()\n(0, a1)\n```\n",
    "created_at": "2011-03-01T12:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2220#issuecomment-14681",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

The other part works too now:


```
sage: b = NumberField([x, x^2 - 3], 'a')
sage: b.gens()
(0, a1)
```




---

archive/issue_comments_014682.json:
```json
{
    "body": "Attachment [sage-trac_2220.patch](tarball://root/attachments/some-uuid/ticket2220/sage-trac_2220.patch) by @orlitzky created at 2011-12-17 20:37:32\n\nAdd doctest for a trivial extension",
    "created_at": "2011-12-17T20:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2220#issuecomment-14682",
    "user": "https://github.com/orlitzky"
}
```

Attachment [sage-trac_2220.patch](tarball://root/attachments/some-uuid/ticket2220/sage-trac_2220.patch) by @orlitzky created at 2011-12-17 20:37:32

Add doctest for a trivial extension



---

archive/issue_comments_014683.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-12-17T20:38:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2220#issuecomment-14683",
    "user": "https://github.com/orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_014684.json:
```json
{
    "body": "I'm pretty sure this is fixed, so I've added a doctest.",
    "created_at": "2011-12-17T20:38:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2220#issuecomment-14684",
    "user": "https://github.com/orlitzky"
}
```

I'm pretty sure this is fixed, so I've added a doctest.



---

archive/issue_comments_014685.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-17T21:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2220#issuecomment-14685",
    "user": "https://trac.sagemath.org/admin/accounts/users/cpauderis"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_014686.json:
```json
{
    "body": "This appears to work exactly as advertised.  Positive review.",
    "created_at": "2011-12-17T21:27:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2220#issuecomment-14686",
    "user": "https://trac.sagemath.org/admin/accounts/users/cpauderis"
}
```

This appears to work exactly as advertised.  Positive review.



---

archive/issue_comments_014687.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-12-22T13:06:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2220",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2220#issuecomment-14687",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_005300.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-12-22T13:06:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2220",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2220#event-5300"
}
```

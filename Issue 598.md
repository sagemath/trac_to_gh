# Issue 598: implement substitute for monoids

archive/issues_000598.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nOn 9/5/07, Joel B. Mohler <joel@kiwistrawberry.us> wrote:\n\\> Yes, so I found FreeMonoid after sending my first e-mail and was testing it\n> out.  I think I may have found something that is not implemented:\n> \n> sage: a=FreeMonoid(1,'a').0\n> sage: a*a\n> a^2\n> sage: a.substitute(5)\n> a  # should be 5?\n> sage: a.substitute(a=5)\n> a  # should be 5?\n> \n> I would have expected those last two results to be 5 -- am I missing\n> something? \n\nThe whole \"substitute\" architecture was implemented in SAGE\nlong after monoids were implemented.  So you'll have to implement\nmonoid substitution. \n\n> I guess substituting isn't an entirely common operation for free\n> monoids, but it seems to be a sensibly defined operation.  Then again, maybe\n> not:\n> \n> sage: M.<x,y> = FreeMonoid(2)\n> sage: (x*y).substitute(x=1)\n> x*y  # I would think that this is 1*y\n> \n\n\n\n> I find that result unsatisfactory as well, but I sure don't have a good idea\n> about what ring (?) the result '1*y' would be a part of.\n\nJust do the arithmetic.    All monoids have a 1 by definition, so 1*y is just \"y\"\nin that monoid.\n\nWilliam\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/598\n\n",
    "created_at": "2007-09-06T00:56:30Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "implement substitute for monoids",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/598",
    "user": "was"
}
```
Assignee: somebody


```
On 9/5/07, Joel B. Mohler <joel@kiwistrawberry.us> wrote:
\> Yes, so I found FreeMonoid after sending my first e-mail and was testing it
> out.  I think I may have found something that is not implemented:
> 
> sage: a=FreeMonoid(1,'a').0
> sage: a*a
> a^2
> sage: a.substitute(5)
> a  # should be 5?
> sage: a.substitute(a=5)
> a  # should be 5?
> 
> I would have expected those last two results to be 5 -- am I missing
> something? 

The whole "substitute" architecture was implemented in SAGE
long after monoids were implemented.  So you'll have to implement
monoid substitution. 

> I guess substituting isn't an entirely common operation for free
> monoids, but it seems to be a sensibly defined operation.  Then again, maybe
> not:
> 
> sage: M.<x,y> = FreeMonoid(2)
> sage: (x*y).substitute(x=1)
> x*y  # I would think that this is 1*y
> 



> I find that result unsatisfactory as well, but I sure don't have a good idea
> about what ring (?) the result '1*y' would be a part of.

Just do the arithmetic.    All monoids have a 1 by definition, so 1*y is just "y"
in that monoid.

William
```


Issue created by migration from https://trac.sagemath.org/ticket/598





---

archive/issue_comments_003087.json:
```json
{
    "body": "Changing assignee from somebody to jbmohler.",
    "created_at": "2007-09-06T00:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/598#issuecomment-3087",
    "user": "was"
}
```

Changing assignee from somebody to jbmohler.



---

archive/issue_comments_003088.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-22T14:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/598#issuecomment-3088",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003089.json:
```json
{
    "body": "Changing assignee from jbmohler to mhansen.",
    "created_at": "2009-01-22T14:24:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/598#issuecomment-3089",
    "user": "mhansen"
}
```

Changing assignee from jbmohler to mhansen.



---

archive/issue_comments_003090.json:
```json
{
    "body": "Attachment [trac_598.patch](tarball://root/attachments/some-uuid/ticket598/trac_598.patch) by mhansen created at 2010-01-16 19:04:29",
    "created_at": "2010-01-16T19:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/598#issuecomment-3090",
    "user": "mhansen"
}
```

Attachment [trac_598.patch](tarball://root/attachments/some-uuid/ticket598/trac_598.patch) by mhansen created at 2010-01-16 19:04:29



---

archive/issue_comments_003091.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-16T19:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/598#issuecomment-3091",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_003092.json:
```json
{
    "body": "A positive review for me.\n\nNote: I did all doctests, and got exactly 22 Segfaults, as with vanilla 4.3.3 (see #7773).\nThus if a new failure occurred within one of those 22 doctests, I couldn't see it.",
    "created_at": "2010-03-14T12:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/598#issuecomment-3092",
    "user": "zimmerma"
}
```

A positive review for me.

Note: I did all doctests, and got exactly 22 Segfaults, as with vanilla 4.3.3 (see #7773).
Thus if a new failure occurred within one of those 22 doctests, I couldn't see it.



---

archive/issue_comments_003093.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-14T12:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/598#issuecomment-3093",
    "user": "zimmerma"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_003094.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T05:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/598#issuecomment-3094",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_003095.json:
```json
{
    "body": "Merged in 4.4.alpha0.",
    "created_at": "2010-04-15T05:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/598#issuecomment-3095",
    "user": "jhpalmieri"
}
```

Merged in 4.4.alpha0.

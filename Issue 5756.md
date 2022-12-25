# Issue 5756: improve coverage of rings/morphism.pyx

archive/issues_005756.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @robertwb\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5756\n\n",
    "created_at": "2009-04-11T17:24:57Z",
    "labels": [
        "component: doctest coverage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "improve coverage of rings/morphism.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5756",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

CC:  @robertwb



Issue created by migration from https://trac.sagemath.org/ticket/5756





---

archive/issue_comments_044904.json:
```json
{
    "body": "BUGS FOUND:\n\n1. bug in __cmp__\n\n```\n10:56 < wstein-5756> Wow, I was reading the __cmp__ for ring lifting maps.\n10:56 < wstein-5756> Check out this bug:\n10:56 < wstein-5756> Zmod(8).lift() == Zmod(10).lift()\n10:56 < wstein-5756> True\n10:56 < wstein-5756> Any two lifting maps are always equal.\n10:56 < wstein-5756> Ouch.\n```\n\n\n2. Another bug related to __cmp__:   #5758 (weird \"hello\")\n\n3. __nonzero__ is wrong for ring morphisms, since Sage does have the 0 ring where 0 == 1, so this code was wrong:\n\n```\n    def __nonzero__(self):\n        return True\n```\n\n\n4. Calling .lift() on a morphism returns None.  This is a bug that was caused by cythonizing morphism.pyx:\n\n```\nsage: R.<x,y> = QQ[]; R.hom([x,x]).lift() is None\nTrue\n```\n",
    "created_at": "2009-04-11T21:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5756#issuecomment-44904",
    "user": "https://github.com/williamstein"
}
```

BUGS FOUND:

1. bug in __cmp__

```
10:56 < wstein-5756> Wow, I was reading the __cmp__ for ring lifting maps.
10:56 < wstein-5756> Check out this bug:
10:56 < wstein-5756> Zmod(8).lift() == Zmod(10).lift()
10:56 < wstein-5756> True
10:56 < wstein-5756> Any two lifting maps are always equal.
10:56 < wstein-5756> Ouch.
```


2. Another bug related to __cmp__:   #5758 (weird "hello")

3. __nonzero__ is wrong for ring morphisms, since Sage does have the 0 ring where 0 == 1, so this code was wrong:

```
    def __nonzero__(self):
        return True
```


4. Calling .lift() on a morphism returns None.  This is a bug that was caused by cythonizing morphism.pyx:

```
sage: R.<x,y> = QQ[]; R.hom([x,x]).lift() is None
True
```




---

archive/issue_comments_044905.json:
```json
{
    "body": "BUGS FOUND:\n5. im_gens() returns a mutable list, which makes it trivial to *break* a morphism after it is created:\n\n```\nsage: R.<x,y> = QQ[]\nsage: f = R.hom([x,x+y])\nsage: f(x)\nx\nsage: f.im_gens()[0] = 5\nsage: f.im_gens()\n[5, x + y]\nsage: f(x)\n5\n```\n",
    "created_at": "2009-04-11T23:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5756#issuecomment-44905",
    "user": "https://github.com/williamstein"
}
```

BUGS FOUND:
5. im_gens() returns a mutable list, which makes it trivial to *break* a morphism after it is created:

```
sage: R.<x,y> = QQ[]
sage: f = R.hom([x,x+y])
sage: f(x)
x
sage: f.im_gens()[0] = 5
sage: f.im_gens()
[5, x + y]
sage: f(x)
5
```




---

archive/issue_comments_044906.json:
```json
{
    "body": "Attachment [trac_5756.patch](tarball://root/attachments/some-uuid/ticket5756/trac_5756.patch) by @williamstein created at 2009-04-11 23:29:09",
    "created_at": "2009-04-11T23:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5756#issuecomment-44906",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5756.patch](tarball://root/attachments/some-uuid/ticket5756/trac_5756.patch) by @williamstein created at 2009-04-11 23:29:09



---

archive/issue_comments_044907.json:
```json
{
    "body": "Starting to review this, which is in itself non-trivial!\n\nThere is some strange terminology here.  I'm not sure what a \"Set-theoretic ring endomorphism of Integer Ring\" is meant to be, let alone a \"set-theoretic ring\".  I think that what is meant is (in the first case) a map between rings which is not a ring homomorphism, such as a section of a surjective map.\n\nAlso the term \"lift\" is used for such a section, i.e. if f:R-->S is the surjective ring hom and h:S-->R is a section (so f(h(s))==s for all s in S) then the map h is being called a lift, where I would say that the element h(s) is a lift of s.  And \"cover\"?   Here R is being called a cover of S?\n\nI think it would be helpful if somewhere in this file this terminology is defined since not all of it is so standard...\n\nA more proper review will follow.",
    "created_at": "2009-04-12T11:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5756#issuecomment-44907",
    "user": "https://github.com/JohnCremona"
}
```

Starting to review this, which is in itself non-trivial!

There is some strange terminology here.  I'm not sure what a "Set-theoretic ring endomorphism of Integer Ring" is meant to be, let alone a "set-theoretic ring".  I think that what is meant is (in the first case) a map between rings which is not a ring homomorphism, such as a section of a surjective map.

Also the term "lift" is used for such a section, i.e. if f:R-->S is the surjective ring hom and h:S-->R is a section (so f(h(s))==s for all s in S) then the map h is being called a lift, where I would say that the element h(s) is a lift of s.  And "cover"?   Here R is being called a cover of S?

I think it would be helpful if somewhere in this file this terminology is defined since not all of it is so standard...

A more proper review will follow.



---

archive/issue_comments_044908.json:
```json
{
    "body": "Robert: In case you are reviewing this - all doctest in my rc3 merge tree with this patch applied pass.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T03:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5756#issuecomment-44908",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Robert: In case you are reviewing this - all doctest in my rc3 merge tree with this patch applied pass.

Cheers,

Michael



---

archive/issue_comments_044909.json:
```json
{
    "body": "I agree that the notation could be made more consistent, but this patch simply documents what is there (which is good) and fixes some bugs. \n\nOne thing I noticed, which is not just common to this patch, is that when we return a list that we don't want people to change (e.g. im_gens) we (hopefully) make a copy. This is why tuples were invited, shouldn't we just be using those instead?",
    "created_at": "2009-04-15T23:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5756#issuecomment-44909",
    "user": "https://github.com/robertwb"
}
```

I agree that the notation could be made more consistent, but this patch simply documents what is there (which is good) and fixes some bugs. 

One thing I noticed, which is not just common to this patch, is that when we return a list that we don't want people to change (e.g. im_gens) we (hopefully) make a copy. This is why tuples were invited, shouldn't we just be using those instead?



---

archive/issue_comments_044910.json:
```json
{
    "body": "Replying to [comment:6 robertwb]:\n> I agree that the notation could be made more consistent, but this patch simply documents what is there (which is good) and fixes some bugs. \n\nYeah, getting it in should be the main goal here and now.\n\n> One thing I noticed, which is not just common to this patch, is that when we return a list that we don't want people to change (e.g. im_gens) we (hopefully) make a copy. This is why tuples were invited, shouldn't we just be using those instead?\n\n**implemented* instead of **invited*' I assume? \n\nEither way, can you please open a followup ticket so that this doesn't get lost.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T02:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5756#issuecomment-44910",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:6 robertwb]:
> I agree that the notation could be made more consistent, but this patch simply documents what is there (which is good) and fixes some bugs. 

Yeah, getting it in should be the main goal here and now.

> One thing I noticed, which is not just common to this patch, is that when we return a list that we don't want people to change (e.g. im_gens) we (hopefully) make a copy. This is why tuples were invited, shouldn't we just be using those instead?

**implemented* instead of **invited*' I assume? 

Either way, can you please open a followup ticket so that this doesn't get lost.

Cheers,

Michael



---

archive/issue_events_006003.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-16T02:54:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5756",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5756#event-6003"
}
```



---

archive/issue_comments_044911.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T02:54:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5756#issuecomment-44911",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_044912.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-16T02:54:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5756#issuecomment-44912",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044913.json:
```json
{
    "body": "I meant invented...\n\nFollowup at #5802, perhaps there should be a followup to John Cremona's comments as well.",
    "created_at": "2009-04-16T07:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5756#issuecomment-44913",
    "user": "https://github.com/robertwb"
}
```

I meant invented...

Followup at #5802, perhaps there should be a followup to John Cremona's comments as well.

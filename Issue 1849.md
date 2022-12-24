# Issue 1849: bug in elementary_divisors for abelian groups

archive/issues_001849.json:
```json
{
    "body": "Assignee: joyner\n\n\n```\n\n\nOn Jan 19, 2008 8:00 AM, John Cremona <john.cremona@gmail.com> wrote:\n> \n> Either this is a bug or I have been teaching students the wrong thing for years:\n> \n> (in 2.9.3)\n> \n> sage: A=AbelianGroup([7,8])\n> \n> sage: A.invariants()\n>  [7,8]\n> \n> sage: A.elementary_divisors()\n>  [7,8]\n> \n> There are two sets of invariants for a finite abelian group.  The\n> \"elementary divisors\" should be a list of integers n_1,n_2,...,n_k\n> with each dividing the next such that A is the direct sum of cyclic\n> groups of order n_i.  In this case A is cyclic so the list should be\n> just [56].  The other set is a list of prime powers and in this case\n> is indeed [7,8] though we could argue about the ordering.\n> \n> Judging by the docstrings, the implemeter of these things in Sage does\n> not agree with me, since the code seems to assume that the\n> \"invariants\" are what I am calling the elem. divisors, and the elem.\n> divisors are the prime-power factors of the invariants, sorted.  In\n> which case the invariants is listed above are wrong!\n> \n> The Sage version of this is all explained in the documentation in file\n> sage/groups/abelian_gps/abelian_groups.py, attributed to David Joyner\n> .  Please will all the algebraists out there tell me whether tey agree\n> with me or him!  I'm not in a position to consult textbooks right now.\n>  The docs there refer to Henri Cohen's books so it is possible that\n> there is a French/English split here BUT in any case the group I\n> defined about is *cyclic* so one of the two outputs is wrong, even if\n> we disagree which one!\n\nThe problem is that when David Joyner implemented this, doing \n\nsage: A=AbelianGroup([7,8])\n\nwould immediately change the invariants to be the elementary divisors. \nI.e., it was *impossible* \nto make an abelian group with specified generator orders -- the would\nalso change to be elementary divisors.   This was so\nhugely painful to use that I fixed AbelianGroup so that one could create\na group with arbitrary generator orders.   Unfortunately, I evidently\ndidn't correctly update the elementary_divisors function.\n\nWilliam\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1849\n\n",
    "created_at": "2008-01-19T16:12:20Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "title": "bug in elementary_divisors for abelian groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1849",
    "user": "was"
}
```
Assignee: joyner


```


On Jan 19, 2008 8:00 AM, John Cremona <john.cremona@gmail.com> wrote:
> 
> Either this is a bug or I have been teaching students the wrong thing for years:
> 
> (in 2.9.3)
> 
> sage: A=AbelianGroup([7,8])
> 
> sage: A.invariants()
>  [7,8]
> 
> sage: A.elementary_divisors()
>  [7,8]
> 
> There are two sets of invariants for a finite abelian group.  The
> "elementary divisors" should be a list of integers n_1,n_2,...,n_k
> with each dividing the next such that A is the direct sum of cyclic
> groups of order n_i.  In this case A is cyclic so the list should be
> just [56].  The other set is a list of prime powers and in this case
> is indeed [7,8] though we could argue about the ordering.
> 
> Judging by the docstrings, the implemeter of these things in Sage does
> not agree with me, since the code seems to assume that the
> "invariants" are what I am calling the elem. divisors, and the elem.
> divisors are the prime-power factors of the invariants, sorted.  In
> which case the invariants is listed above are wrong!
> 
> The Sage version of this is all explained in the documentation in file
> sage/groups/abelian_gps/abelian_groups.py, attributed to David Joyner
> .  Please will all the algebraists out there tell me whether tey agree
> with me or him!  I'm not in a position to consult textbooks right now.
>  The docs there refer to Henri Cohen's books so it is possible that
> there is a French/English split here BUT in any case the group I
> defined about is *cyclic* so one of the two outputs is wrong, even if
> we disagree which one!

The problem is that when David Joyner implemented this, doing 

sage: A=AbelianGroup([7,8])

would immediately change the invariants to be the elementary divisors. 
I.e., it was *impossible* 
to make an abelian group with specified generator orders -- the would
also change to be elementary divisors.   This was so
hugely painful to use that I fixed AbelianGroup so that one could create
a group with arbitrary generator orders.   Unfortunately, I evidently
didn't correctly update the elementary_divisors function.

William
```


Issue created by migration from https://trac.sagemath.org/ticket/1849





---

archive/issue_comments_011696.json:
```json
{
    "body": "this is part 1 -- doctests outside abelian groups directory will be broken.",
    "created_at": "2008-01-28T06:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1849#issuecomment-11696",
    "user": "was"
}
```

this is part 1 -- doctests outside abelian groups directory will be broken.



---

archive/issue_comments_011697.json:
```json
{
    "body": "Attachment [trac-1849-abelian-group-rewrite-part1.patch](tarball://root/attachments/some-uuid/ticket1849/trac-1849-abelian-group-rewrite-part1.patch) by was created at 2008-02-01 23:59:41\n\nthis is part 2.  This is also not ready.",
    "created_at": "2008-02-01T23:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1849#issuecomment-11697",
    "user": "was"
}
```

Attachment [trac-1849-abelian-group-rewrite-part1.patch](tarball://root/attachments/some-uuid/ticket1849/trac-1849-abelian-group-rewrite-part1.patch) by was created at 2008-02-01 23:59:41

this is part 2.  This is also not ready.



---

archive/issue_comments_011698.json:
```json
{
    "body": "Attachment [abelian_groups_rewrite_part_2.patch](tarball://root/attachments/some-uuid/ticket1849/abelian_groups_rewrite_part_2.patch) by was created at 2008-02-06 23:02:06\n\nI just found this terrifying line in `abelian_group.py`:\n\n\n```\nHgensf = [x for x in Hgens if len(set(Ggens0).intersection(set(list(str(x)))))==0]\n```\n\n\nOUCH!   This will completely break if one makes, e.g., abelian groups with\ngenerators that have more than one letter.  For example, in current Sage\n\n```\nsage: G.<a,aa,aaa> = AbelianGroup(3,[5,0,0])\nsage: G.subgroup([a])\n\nMultiplicative Abelian Group isomorphic to C5, which is the subgroup of\nMultiplicative Abelian Group isomorphic to C5 x Z x Z\ngenerated by [a]\nsage: G.subgroup([aa])\n---------------------------------------------------------------------------\n<type 'exceptions.RuntimeError'>          Traceback (most recent call last)\n\n/Users/was/<ipython console> in <module>()\n\n/Users/was/sage2/local/lib/python2.5/site-packages/sage/groups/abelian_gps/abelian_group.py in subgroup(self, gensH, names)\n    701             if not(gensH[i] in G):\n    702                 raise TypeError, \"Subgroup generators must belong to the given group.\"\n--> 703         return AbelianGroup_subgroup(self, gensH, names)\n    704 \n    705     def __cmp__(self, right):\n\n/Users/was/sage2/local/lib/python2.5/site-packages/sage/groups/abelian_gps/abelian_group.py in __init__(self, ambient, gens, names)\n    927                gap.eval(cmd)\n    928         s2 = \"gensH:=%s\"%Hgensf #### remove from this the ones <--> 0 invar\n--> 929         gap.eval(s2)\n    930         s3 = 'H:=Subgroup(G,gensH)'\n    931         gap.eval(s3)\n\n/Users/was/sage2/local/lib/python2.5/site-packages/sage/interfaces/gap.py in eval(self, x, newlines, strip)\n    307         if len(x) == 0 or x[len(x) - 1] != ';':\n    308             x += ';'\n--> 309         s = Expect.eval(self, x)\n    310         if newlines:\n    311             return s\n\n/Users/was/sage2/local/lib/python2.5/site-packages/sage/interfaces/expect.py in eval(self, code, strip, **kwds)\n    705         try:\n    706             with gc_disabled():\n--> 707                 return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n    708         except KeyboardInterrupt:\n    709             # DO NOT CATCH KeyboardInterrupt, as it is being caught\n\n/Users/was/sage2/local/lib/python2.5/site-packages/sage/interfaces/gap.py in _eval_line(self, line, allow_use_file, wait_for_prompt)\n    508                         return ''\n    509                 else:\n--> 510                     raise RuntimeError, message\n    511 \n    512         except KeyboardInterrupt:\n\n<type 'exceptions.RuntimeError'>: Gap produced error output\nVariable: 'aa' must have a value\n\n\n   executing gensH:=[aa];\n```\n",
    "created_at": "2008-02-06T23:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1849#issuecomment-11698",
    "user": "was"
}
```

Attachment [abelian_groups_rewrite_part_2.patch](tarball://root/attachments/some-uuid/ticket1849/abelian_groups_rewrite_part_2.patch) by was created at 2008-02-06 23:02:06

I just found this terrifying line in `abelian_group.py`:


```
Hgensf = [x for x in Hgens if len(set(Ggens0).intersection(set(list(str(x)))))==0]
```


OUCH!   This will completely break if one makes, e.g., abelian groups with
generators that have more than one letter.  For example, in current Sage

```
sage: G.<a,aa,aaa> = AbelianGroup(3,[5,0,0])
sage: G.subgroup([a])

Multiplicative Abelian Group isomorphic to C5, which is the subgroup of
Multiplicative Abelian Group isomorphic to C5 x Z x Z
generated by [a]
sage: G.subgroup([aa])
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/sage2/local/lib/python2.5/site-packages/sage/groups/abelian_gps/abelian_group.py in subgroup(self, gensH, names)
    701             if not(gensH[i] in G):
    702                 raise TypeError, "Subgroup generators must belong to the given group."
--> 703         return AbelianGroup_subgroup(self, gensH, names)
    704 
    705     def __cmp__(self, right):

/Users/was/sage2/local/lib/python2.5/site-packages/sage/groups/abelian_gps/abelian_group.py in __init__(self, ambient, gens, names)
    927                gap.eval(cmd)
    928         s2 = "gensH:=%s"%Hgensf #### remove from this the ones <--> 0 invar
--> 929         gap.eval(s2)
    930         s3 = 'H:=Subgroup(G,gensH)'
    931         gap.eval(s3)

/Users/was/sage2/local/lib/python2.5/site-packages/sage/interfaces/gap.py in eval(self, x, newlines, strip)
    307         if len(x) == 0 or x[len(x) - 1] != ';':
    308             x += ';'
--> 309         s = Expect.eval(self, x)
    310         if newlines:
    311             return s

/Users/was/sage2/local/lib/python2.5/site-packages/sage/interfaces/expect.py in eval(self, code, strip, **kwds)
    705         try:
    706             with gc_disabled():
--> 707                 return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
    708         except KeyboardInterrupt:
    709             # DO NOT CATCH KeyboardInterrupt, as it is being caught

/Users/was/sage2/local/lib/python2.5/site-packages/sage/interfaces/gap.py in _eval_line(self, line, allow_use_file, wait_for_prompt)
    508                         return ''
    509                 else:
--> 510                     raise RuntimeError, message
    511 
    512         except KeyboardInterrupt:

<type 'exceptions.RuntimeError'>: Gap produced error output
Variable: 'aa' must have a value


   executing gensH:=[aa];
```




---

archive/issue_comments_011699.json:
```json
{
    "body": "#517 is in the same ball park.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-26T07:08:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1849#issuecomment-11699",
    "user": "mabshoff"
}
```

#517 is in the same ball park.

Cheers,

Michael



---

archive/issue_comments_011700.json:
```json
{
    "body": "See also #3127 and #2272.",
    "created_at": "2008-05-07T22:25:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1849#issuecomment-11700",
    "user": "was"
}
```

See also #3127 and #2272.



---

archive/issue_comments_011701.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_roed\".",
    "created_at": "2008-06-20T04:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1849#issuecomment-11701",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_roed".



---

archive/issue_comments_011702.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-29T13:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1849#issuecomment-11702",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_011703.json:
```json
{
    "body": "I propose that we resolve this as \"fixed\" now #6449 has gone in.",
    "created_at": "2010-07-29T13:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1849#issuecomment-11703",
    "user": "davidloeffler"
}
```

I propose that we resolve this as "fixed" now #6449 has gone in.



---

archive/issue_comments_011704.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-12T10:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1849#issuecomment-11704",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_011705.json:
```json
{
    "body": "I'm deducing that you agree with my proposal to close this, so I'm setting it to \"positive review\". Release manager: please close as duplicate.",
    "created_at": "2010-10-12T10:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1849#issuecomment-11705",
    "user": "davidloeffler"
}
```

I'm deducing that you agree with my proposal to close this, so I'm setting it to "positive review". Release manager: please close as duplicate.



---

archive/issue_comments_011706.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-10-17T04:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1849#issuecomment-11706",
    "user": "mpatel"
}
```

Resolution: duplicate

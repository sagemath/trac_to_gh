# Issue 6072: Boundary space for GammaH fails to identify vanishing classes

archive/issues_006072.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @craigcitro\n\nIf G is a congruence subgroup (not containing -1), then cusps of G can \"magically\" vanish in the space of odd weight boundary symbols when the weight is odd.\n\nReading the explanation in boundary.py, I think that the explanation there just boils down to that this happens if and only if the cusp is irregular (in the sense that the generator of its stabiliser looks like [-1, h ; 0, -1]). But for the group `GammaH(8, [3])` there are 4 cusps of which 2 are irregular, namely 1/2 and 1/4 -- but the boundary space doesn't realise this. It's possible that I've misunderstood the definitions, but I'm pretty sure that the boundary space is supposed to be dual to the space of Eisenstein series, and that certainly has dimension 2 here.\n\nThis is certainly of no great significance at the moment since we don't really have much functionality working for GammaH spaces anyway, but it's still not ideal that the functionality we do have implemented is giving wrong answers.\n\nCraig: I'm ccing you here as I got the impression you wrote most of the GammaH stuff -- do you have any idea what's going on here?\n\nIssue created by migration from https://trac.sagemath.org/ticket/6072\n\n",
    "created_at": "2009-05-18T17:52:59Z",
    "labels": [
        "component: modular forms",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.3",
    "title": "Boundary space for GammaH fails to identify vanishing classes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6072",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @craigcitro

CC:  @craigcitro

If G is a congruence subgroup (not containing -1), then cusps of G can "magically" vanish in the space of odd weight boundary symbols when the weight is odd.

Reading the explanation in boundary.py, I think that the explanation there just boils down to that this happens if and only if the cusp is irregular (in the sense that the generator of its stabiliser looks like [-1, h ; 0, -1]). But for the group `GammaH(8, [3])` there are 4 cusps of which 2 are irregular, namely 1/2 and 1/4 -- but the boundary space doesn't realise this. It's possible that I've misunderstood the definitions, but I'm pretty sure that the boundary space is supposed to be dual to the space of Eisenstein series, and that certainly has dimension 2 here.

This is certainly of no great significance at the moment since we don't really have much functionality working for GammaH spaces anyway, but it's still not ideal that the functionality we do have implemented is giving wrong answers.

Craig: I'm ccing you here as I got the impression you wrote most of the GammaH stuff -- do you have any idea what's going on here?

Issue created by migration from https://trac.sagemath.org/ticket/6072





---

archive/issue_comments_048246.json:
```json
{
    "body": "Hi David,\n\nYep, I'm definitely responsible for this code. There **is** a bug here -- in the case that the sign is 0, and the weight is odd, there are definitely relations I didn't use to determine if a cusp that gets coerced in is 0. (Note that the relation still gets picked up if you're computing with sign equal to 1 or -1.) Luckily, though, the code that's used to compute modular symbols spaces is `_coerce_in_manin_symbol` -- so it wasn't really affecting the resulting modular symbols spaces that were computed. (I had checked the dimensions of these spaces were correct via the dimension formulas, so I would have been a little surprised if they were wrong.)\n\nI think the attached patch should fix this -- let me know if you don't trust it, or if you think it needs more documentation/doctests.",
    "created_at": "2009-05-19T08:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6072#issuecomment-48246",
    "user": "https://github.com/craigcitro"
}
```

Hi David,

Yep, I'm definitely responsible for this code. There **is** a bug here -- in the case that the sign is 0, and the weight is odd, there are definitely relations I didn't use to determine if a cusp that gets coerced in is 0. (Note that the relation still gets picked up if you're computing with sign equal to 1 or -1.) Luckily, though, the code that's used to compute modular symbols spaces is `_coerce_in_manin_symbol` -- so it wasn't really affecting the resulting modular symbols spaces that were computed. (I had checked the dimensions of these spaces were correct via the dimension formulas, so I would have been a little surprised if they were wrong.)

I think the attached patch should fix this -- let me know if you don't trust it, or if you think it needs more documentation/doctests.



---

archive/issue_comments_048247.json:
```json
{
    "body": "Attachment [trac-6072.patch](tarball://root/attachments/some-uuid/ticket6072/trac-6072.patch) by @loefflerd created at 2009-05-25 12:56:59\n\nSorry it's taken me so long to get around to reviewing this, but it still doesn't seem to quite fix the problem:\n\n```\nsage: G = GammaH(4, [])\nsage: B3 = G.modular_symbols(weight=3).boundary_space()\nsage: [B3(x) for x in G.cusps()]\n[[0], 0, [Infinity]]\nsage: B3.rank()\n3\n```\n\nI think the problem is that the check to see whether or not the new cusp class vanishes gets done *after* the cusp is added to `B3._known_cusps`, and the rank method just checks the length of known_cusps. The same happens if instead of explicitly coercing all the cusps of G into B3, you do `B3 = G.modular_symbols(weight=3).boundary_map().codomain()` to get a fully-initialised version.\n\nAnother silly minor quibble: if -1 is in G, then the boundary space should clearly be zero in all odd weights, but this doesn't seem to happen: \n\n```\nsage: G = GammaH(10, [9])\nsage: B3 = G.modular_symbols(weight=3).boundary_space()\nsage: B3(Cusp(1))\nsage: [B3(x) for x in G.cusps()]\n[[1], 0, [1/4], 0, [1/3], 0, [1/2], 0]\n```\n\nFinally, here's another (possibly completely unrelated) bug:\n\n```\nsage: G = GammaH(8, [5])\nsage: G.modular_symbols(weight=3).boundary_map() \n---------------------------------------------------------------------------                 \nAssertionError                            Traceback (most recent call last)                 \n\n/home/david/.sage/temp/groke/13903/_home_david__sage_init_sage_0.py in <module>()\n\n/home/david/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.pyc in boundary_map(self)                                                                     \n   1251             # compute boundary map                                                  \n   1252             B = self.boundary_space()                                               \n-> 1253             I = [B(b) for b in self.basis()]                                        \n   1254             W = matrix_space.MatrixSpace(self.base_ring(), len(I), B.rank(), sparse=True)                                                                                       \n   1255                                                                                     \n\n/home/david/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.pyc in __call__(self, x)                                                                     \n    583             if len(S) == 0:                                                         \n    584                 return self(0)                                                      \n--> 585             return sum([c*self._coerce_in_manin_symbol(v) for c, v in S])           \n    586                                                                                     \n    587         elif is_FreeModuleElement(x):\n\n/home/david/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.pyc in _coerce_in_manin_symbol(self, x)\n    532         \"\"\"\n    533         i = x.i\n--> 534         alpha, beta = x.endpoints(self.level())\n    535         if self.weight() == 2:\n    536             return self(alpha) - self(beta)\n\n/home/david/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/manin_symbols.pyc in endpoints(self, N)\n   1758             if N < 1:\n   1759                 raise ArithmeticError, \"N must be positive\"\n-> 1760         a,b,c,d = self.lift_to_sl2z()\n   1761         return cusps.Cusp(b,d), cusps.Cusp(a,c)\n   1762\n\n/home/david/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/manin_symbols.pyc in lift_to_sl2z(self, N)\n   1735         d += N*m\n   1736         g, z1, z2 = arith.XGCD(c,d)\n-> 1737         assert g==1\n   1738         return [z2, -z1, c, d]\n   1739\n\nAssertionError:\n```\n\n(This may well be nothing to do with any of this, I just happened to spot it while testing your patch, so feel free to ignore it if it's not relevant).",
    "created_at": "2009-05-25T12:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6072#issuecomment-48247",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac-6072.patch](tarball://root/attachments/some-uuid/ticket6072/trac-6072.patch) by @loefflerd created at 2009-05-25 12:56:59

Sorry it's taken me so long to get around to reviewing this, but it still doesn't seem to quite fix the problem:

```
sage: G = GammaH(4, [])
sage: B3 = G.modular_symbols(weight=3).boundary_space()
sage: [B3(x) for x in G.cusps()]
[[0], 0, [Infinity]]
sage: B3.rank()
3
```

I think the problem is that the check to see whether or not the new cusp class vanishes gets done *after* the cusp is added to `B3._known_cusps`, and the rank method just checks the length of known_cusps. The same happens if instead of explicitly coercing all the cusps of G into B3, you do `B3 = G.modular_symbols(weight=3).boundary_map().codomain()` to get a fully-initialised version.

Another silly minor quibble: if -1 is in G, then the boundary space should clearly be zero in all odd weights, but this doesn't seem to happen: 

```
sage: G = GammaH(10, [9])
sage: B3 = G.modular_symbols(weight=3).boundary_space()
sage: B3(Cusp(1))
sage: [B3(x) for x in G.cusps()]
[[1], 0, [1/4], 0, [1/3], 0, [1/2], 0]
```

Finally, here's another (possibly completely unrelated) bug:

```
sage: G = GammaH(8, [5])
sage: G.modular_symbols(weight=3).boundary_map() 
---------------------------------------------------------------------------                 
AssertionError                            Traceback (most recent call last)                 

/home/david/.sage/temp/groke/13903/_home_david__sage_init_sage_0.py in <module>()

/home/david/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.pyc in boundary_map(self)                                                                     
   1251             # compute boundary map                                                  
   1252             B = self.boundary_space()                                               
-> 1253             I = [B(b) for b in self.basis()]                                        
   1254             W = matrix_space.MatrixSpace(self.base_ring(), len(I), B.rank(), sparse=True)                                                                                       
   1255                                                                                     

/home/david/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.pyc in __call__(self, x)                                                                     
    583             if len(S) == 0:                                                         
    584                 return self(0)                                                      
--> 585             return sum([c*self._coerce_in_manin_symbol(v) for c, v in S])           
    586                                                                                     
    587         elif is_FreeModuleElement(x):

/home/david/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/boundary.pyc in _coerce_in_manin_symbol(self, x)
    532         """
    533         i = x.i
--> 534         alpha, beta = x.endpoints(self.level())
    535         if self.weight() == 2:
    536             return self(alpha) - self(beta)

/home/david/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/manin_symbols.pyc in endpoints(self, N)
   1758             if N < 1:
   1759                 raise ArithmeticError, "N must be positive"
-> 1760         a,b,c,d = self.lift_to_sl2z()
   1761         return cusps.Cusp(b,d), cusps.Cusp(a,c)
   1762

/home/david/sage-4.0.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/manin_symbols.pyc in lift_to_sl2z(self, N)
   1735         d += N*m
   1736         g, z1, z2 = arith.XGCD(c,d)
-> 1737         assert g==1
   1738         return [z2, -z1, c, d]
   1739

AssertionError:
```

(This may well be nothing to do with any of this, I just happened to spot it while testing your patch, so feel free to ignore it if it's not relevant).



---

archive/issue_events_014250.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6072#event-14250"
}
```



---

archive/issue_events_014251.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6072#event-14251"
}
```



---

archive/issue_events_014252.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6072#event-14252"
}
```



---

archive/issue_comments_048248.json:
```json
{
    "body": "Here is a git branch\n\n---\nNew commits:",
    "created_at": "2014-03-21T21:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6072#issuecomment-48248",
    "user": "https://github.com/fchapoton"
}
```

Here is a git branch

---
New commits:



---

archive/issue_events_014253.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6072#event-14253"
}
```



---

archive/issue_events_014254.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6072#event-14254"
}
```



---

archive/issue_events_014255.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6072#event-14255"
}
```



---

archive/issue_events_014256.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6072#event-14256"
}
```



---

archive/issue_comments_048249.json:
```json
{
    "body": "why does this needs work ?",
    "created_at": "2017-04-17T09:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6072#issuecomment-48249",
    "user": "https://github.com/fchapoton"
}
```

why does this needs work ?



---

archive/issue_events_014257.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2017-04-17T09:18:35Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6072#event-14257"
}
```



---

archive/issue_events_014258.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2017-04-17T09:18:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "milestone": "sage-8.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6072#event-14258"
}
```



---

archive/issue_comments_048250.json:
```json
{
    "body": "> why does this needs work ?\n\n\nBecause nobody worked on it? \n\nMy comment (from 8 years ago!) clearly points out a corner case of the bug which is not fixed by Craig Citro's patch; nobody has done anything since, except convert the existing partial fix into a Git branch; ergo, it is \"needs work\".",
    "created_at": "2017-04-19T08:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6072#issuecomment-48250",
    "user": "https://github.com/loefflerd"
}
```

> why does this needs work ?


Because nobody worked on it? 

My comment (from 8 years ago!) clearly points out a corner case of the bug which is not fixed by Craig Citro's patch; nobody has done anything since, except convert the existing partial fix into a Git branch; ergo, it is "needs work".



---

archive/issue_comments_048251.json:
```json
{
    "body": "I revisited this, after 8 years delay, because this ticket, #7837 and #25268 are sufficiently closely related that it made sense to do them all at once. \n\nThe old code was sometimes failing to determine correctly which cusps are irregular; we now have a method ` is_regular_cusp ` of arithmetic groups that does exactly this (reliably), so I just stripped out the buggy code here and replaced it with calls to that other implementation. I also tweaked the way boundary symbols are represented, avoiding the redundant 0 entries in their coordinate vectors when the relations force a cusp to vanish; this solves the problems noticed here and at #7837 about ` rank()` giving misleading answers.\n\n---\nNew commits:",
    "created_at": "2018-05-12T21:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6072#issuecomment-48251",
    "user": "https://github.com/loefflerd"
}
```

I revisited this, after 8 years delay, because this ticket, #7837 and #25268 are sufficiently closely related that it made sense to do them all at once. 

The old code was sometimes failing to determine correctly which cusps are irregular; we now have a method ` is_regular_cusp ` of arithmetic groups that does exactly this (reliably), so I just stripped out the buggy code here and replaced it with calls to that other implementation. I also tweaked the way boundary symbols are represented, avoiding the redundant 0 entries in their coordinate vectors when the relations force a cusp to vanish; this solves the problems noticed here and at #7837 about ` rank()` giving misleading answers.

---
New commits:



---

archive/issue_comments_048252.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2018-05-12T21:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6072#issuecomment-48252",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_048253.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-05-13T12:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6072#issuecomment-48253",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_048254.json:
```json
{
    "body": "ok, let it be",
    "created_at": "2018-05-13T12:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6072#issuecomment-48254",
    "user": "https://github.com/fchapoton"
}
```

ok, let it be



---

archive/issue_events_014259.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2018-05-13T12:11:18Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "milestone": "sage-8.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6072#event-14259"
}
```



---

archive/issue_events_014260.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2018-05-13T12:11:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "milestone": "sage-8.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6072#event-14260"
}
```



---

archive/issue_comments_048255.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2018-05-15T22:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6072#issuecomment-48255",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_014261.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2018-05-15T22:34:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6072",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6072#event-14261"
}
```

# Issue 7191: is_primitive() for a Dirichlet character doesn't work when base ring is CC

archive/issues_007191.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @categorie\n\nSee the following example:\n\n\n```\nsage: G = DirichletGroup(500, base_ring=CC)\nsage: G[0].is_primitive()\nFalse\nsage: G[1].is_primitive()\n---------------------------------------------------------------------------\nKeyError                                  Traceback (most recent call last)\n\n/home/bober/.sage/temp/bober/24617/_home_bober__sage_init_sage_0.py in <module>()\n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)\n    240             return cache[key]\n    241         else:\n--> 242             cache[key] = self.f(self._instance, *args, **kwds)\n    243             return cache[key]\n    244 \n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in is_primitive(self)\n   1161             True\n   1162         \"\"\"\n-> 1163         return (self.conductor() == self.modulus())\n   1164 \n   1165     @cached_method\n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)\n    240             return cache[key]\n    241         else:\n--> 242             cache[key] = self.f(self._instance, *args, **kwds)\n    243             return cache[key]\n    244 \n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in conductor(self)\n    624         F = arith.factor(self.modulus())\n    625         if len(F) > 1:\n--> 626             return misc.mul([d.conductor() for d in self.decomposition()])\n    627         p = F[0][0]\n    628         # When p is odd, and x =/= 1, the conductor is the smallest p**r such that\n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)\n    240             return cache[key]\n    241         else:\n--> 242             cache[key] = self.f(self._instance, *args, **kwds)\n    243             return cache[key]\n    244 \n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in conductor(self)\n    620             20\n    621         \"\"\"\n--> 622         if self.modulus() == 1 or self.is_trivial():\n    623             return 1\n    624         F = arith.factor(self.modulus())\n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)\n    240             return cache[key]\n    241         else:\n--> 242             cache[key] = self.f(self._instance, *args, **kwds)\n    243             return cache[key]\n    244 \n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in is_trivial(self)\n   1177             True\n   1178         \"\"\"\n-> 1179         return (self.element() == 0)\n   1180 \n   1181     def kernel(self):\n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in element(self)\n   1531             M    = P._module\n   1532             dlog = P._zeta_dlog\n-> 1533             v = M([dlog[x] for x in self.values_on_gens()])\n   1534             self.__element = v\n   1535             return v\n\nKeyError: -1.00000000000000 - 2.63677968348475e-16*I\nsage: G[3].is_primitive()\n---------------------------------------------------------------------------\nKeyError                                  Traceback (most recent call last)\n\n/home/bober/.sage/temp/bober/24617/_home_bober__sage_init_sage_0.py in <module>()\n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)\n    240             return cache[key]\n    241         else:\n--> 242             cache[key] = self.f(self._instance, *args, **kwds)\n    243             return cache[key]\n    244 \n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in is_primitive(self)\n   1161             True\n   1162         \"\"\"\n-> 1163         return (self.conductor() == self.modulus())\n   1164 \n   1165     @cached_method\n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)\n    240             return cache[key]\n    241         else:\n--> 242             cache[key] = self.f(self._instance, *args, **kwds)\n    243             return cache[key]\n    244 \n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in conductor(self)\n    624         F = arith.factor(self.modulus())\n    625         if len(F) > 1:\n--> 626             return misc.mul([d.conductor() for d in self.decomposition()])\n    627         p = F[0][0]\n    628         # When p is odd, and x =/= 1, the conductor is the smallest p**r such that\n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)\n    240             return cache[key]\n    241         else:\n--> 242             cache[key] = self.f(self._instance, *args, **kwds)\n    243             return cache[key]\n    244 \n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in conductor(self)\n    620             20\n    621         \"\"\"\n--> 622         if self.modulus() == 1 or self.is_trivial():\n    623             return 1\n    624         F = arith.factor(self.modulus())\n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)\n    240             return cache[key]\n    241         else:\n--> 242             cache[key] = self.f(self._instance, *args, **kwds)\n    243             return cache[key]\n    244 \n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in is_trivial(self)\n   1177             True\n   1178         \"\"\"\n-> 1179         return (self.element() == 0)\n   1180 \n   1181     def kernel(self):\n\n/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in element(self)\n   1531             M    = P._module\n   1532             dlog = P._zeta_dlog\n-> 1533             v = M([dlog[x] for x in self.values_on_gens()])\n   1534             self.__element = v\n   1535             return v\n\nKeyError: -1.00000000000000 - 2.63677968348475e-16*I\nsage:\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7191\n\n",
    "created_at": "2009-10-12T02:58:56Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.3",
    "title": "is_primitive() for a Dirichlet character doesn't work when base ring is CC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7191",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```
Assignee: @williamstein

CC:  @categorie

See the following example:


```
sage: G = DirichletGroup(500, base_ring=CC)
sage: G[0].is_primitive()
False
sage: G[1].is_primitive()
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)

/home/bober/.sage/temp/bober/24617/_home_bober__sage_init_sage_0.py in <module>()

/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)
    240             return cache[key]
    241         else:
--> 242             cache[key] = self.f(self._instance, *args, **kwds)
    243             return cache[key]
    244 

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in is_primitive(self)
   1161             True
   1162         """
-> 1163         return (self.conductor() == self.modulus())
   1164 
   1165     @cached_method

/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)
    240             return cache[key]
    241         else:
--> 242             cache[key] = self.f(self._instance, *args, **kwds)
    243             return cache[key]
    244 

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in conductor(self)
    624         F = arith.factor(self.modulus())
    625         if len(F) > 1:
--> 626             return misc.mul([d.conductor() for d in self.decomposition()])
    627         p = F[0][0]
    628         # When p is odd, and x =/= 1, the conductor is the smallest p**r such that

/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)
    240             return cache[key]
    241         else:
--> 242             cache[key] = self.f(self._instance, *args, **kwds)
    243             return cache[key]
    244 

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in conductor(self)
    620             20
    621         """
--> 622         if self.modulus() == 1 or self.is_trivial():
    623             return 1
    624         F = arith.factor(self.modulus())

/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)
    240             return cache[key]
    241         else:
--> 242             cache[key] = self.f(self._instance, *args, **kwds)
    243             return cache[key]
    244 

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in is_trivial(self)
   1177             True
   1178         """
-> 1179         return (self.element() == 0)
   1180 
   1181     def kernel(self):

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in element(self)
   1531             M    = P._module
   1532             dlog = P._zeta_dlog
-> 1533             v = M([dlog[x] for x in self.values_on_gens()])
   1534             self.__element = v
   1535             return v

KeyError: -1.00000000000000 - 2.63677968348475e-16*I
sage: G[3].is_primitive()
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)

/home/bober/.sage/temp/bober/24617/_home_bober__sage_init_sage_0.py in <module>()

/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)
    240             return cache[key]
    241         else:
--> 242             cache[key] = self.f(self._instance, *args, **kwds)
    243             return cache[key]
    244 

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in is_primitive(self)
   1161             True
   1162         """
-> 1163         return (self.conductor() == self.modulus())
   1164 
   1165     @cached_method

/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)
    240             return cache[key]
    241         else:
--> 242             cache[key] = self.f(self._instance, *args, **kwds)
    243             return cache[key]
    244 

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in conductor(self)
    624         F = arith.factor(self.modulus())
    625         if len(F) > 1:
--> 626             return misc.mul([d.conductor() for d in self.decomposition()])
    627         p = F[0][0]
    628         # When p is odd, and x =/= 1, the conductor is the smallest p**r such that

/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)
    240             return cache[key]
    241         else:
--> 242             cache[key] = self.f(self._instance, *args, **kwds)
    243             return cache[key]
    244 

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in conductor(self)
    620             20
    621         """
--> 622         if self.modulus() == 1 or self.is_trivial():
    623             return 1
    624         F = arith.factor(self.modulus())

/home/bober/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.pyc in __call__(self, *args, **kwds)
    240             return cache[key]
    241         else:
--> 242             cache[key] = self.f(self._instance, *args, **kwds)
    243             return cache[key]
    244 

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in is_trivial(self)
   1177             True
   1178         """
-> 1179         return (self.element() == 0)
   1180 
   1181     def kernel(self):

/home/bober/sage/local/lib/python2.6/site-packages/sage/modular/dirichlet.pyc in element(self)
   1531             M    = P._module
   1532             dlog = P._zeta_dlog
-> 1533             v = M([dlog[x] for x in self.values_on_gens()])
   1534             self.__element = v
   1535             return v

KeyError: -1.00000000000000 - 2.63677968348475e-16*I
sage:
```


Issue created by migration from https://trac.sagemath.org/ticket/7191





---

archive/issue_comments_059451.json:
```json
{
    "body": "The attached patch may fix the issues. (But perhaps some issues remain.)\n\nThe main solution is to fix things so that the discrete log table is not used when the base ring is a complex field. (It really isn't needed since the nth root of unity that is chosen will always be e(1/n).)\n\nThere are also some small fixes to deal with the gauss sum, and to deal with is_even and is_odd. In the latter case, we again have the problem that we can't test chi(-1) == -1, for example, since things are approximate.\n\nThere might be some more issues to fix to make things work well, but all doctests pass for me, so the patch at least doesn't break anything.",
    "created_at": "2011-04-02T01:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59451",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

The attached patch may fix the issues. (But perhaps some issues remain.)

The main solution is to fix things so that the discrete log table is not used when the base ring is a complex field. (It really isn't needed since the nth root of unity that is chosen will always be e(1/n).)

There are also some small fixes to deal with the gauss sum, and to deal with is_even and is_odd. In the latter case, we again have the problem that we can't test chi(-1) == -1, for example, since things are approximate.

There might be some more issues to fix to make things work well, but all doctests pass for me, so the patch at least doesn't break anything.



---

archive/issue_comments_059452.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-04-02T01:27:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59452",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059453.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-05T16:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59453",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059454.json:
```json
{
    "body": "It looks to me as you attached the printout of an \"ls\" rather than the ticket in this directory.",
    "created_at": "2011-04-05T16:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59454",
    "user": "https://github.com/categorie"
}
```

It looks to me as you attached the printout of an "ls" rather than the ticket in this directory.



---

archive/issue_comments_059455.json:
```json
{
    "body": "Replying to [comment:4 wuthrich]:\n> It looks to me as you attached the printout of an \"ls\" rather than the ticket in this directory.\n\nOops. Fixed now. \n\n(Curiously, my bash history contains the lines:\n\nhg export 15468\nls\nls > trac7191.patch\n)",
    "created_at": "2011-04-05T18:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59455",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

Replying to [comment:4 wuthrich]:
> It looks to me as you attached the printout of an "ls" rather than the ticket in this directory.

Oops. Fixed now. 

(Curiously, my bash history contains the lines:

hg export 15468
ls
ls > trac7191.patch
)



---

archive/issue_comments_059456.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-05T18:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59456",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059457.json:
```json
{
    "body": "I just discovered a spot where rishi's lcalc wrapper uses\n\n` if chi(-1) == 1 `\n\nto check whether chi is even. This causes problems. (It should use chi.is_even().) Since this problem may well occur elsewhere, I'm going to change this back to \"needs work\" for now.",
    "created_at": "2011-04-08T19:06:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59457",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

I just discovered a spot where rishi's lcalc wrapper uses

` if chi(-1) == 1 `

to check whether chi is even. This causes problems. (It should use chi.is_even().) Since this problem may well occur elsewhere, I'm going to change this back to "needs work" for now.



---

archive/issue_comments_059458.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-08T19:06:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59458",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059459.json:
```json
{
    "body": "Changing assignee from @williamstein to bober.",
    "created_at": "2011-04-08T19:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59459",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

Changing assignee from @williamstein to bober.



---

archive/issue_comments_059460.json:
```json
{
    "body": "Attachment [trac7191.patch](tarball://root/attachments/some-uuid/ticket7191/trac7191.patch) by bober created at 2011-09-02 10:42:55",
    "created_at": "2011-09-02T10:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59460",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

Attachment [trac7191.patch](tarball://root/attachments/some-uuid/ticket7191/trac7191.patch) by bober created at 2011-09-02 10:42:55



---

archive/issue_comments_059461.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-09-02T10:44:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59461",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059462.json:
```json
{
    "body": "I changed the patch now to include the one-line fix to the lcalc wrapper. I think it is probably not a waste of time for someone to review this now.",
    "created_at": "2011-09-02T10:44:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59462",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```

I changed the patch now to include the one-line fix to the lcalc wrapper. I think it is probably not a waste of time for someone to review this now.



---

archive/issue_comments_059463.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-11-14T18:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59463",
    "user": "https://trac.sagemath.org/admin/accounts/users/johanbosman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059464.json:
```json
{
    "body": "The NotImplementedError message should also be adjusted in the gauss_sum() function as you did in gauss_sum_numerical().\n\n```\nsage: G = DirichletGroup(500, base_ring=RR)\nsage: G[1].gauss_sum()\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n...\nNotImplementedError: Gauss sums only currently implemented when the base ring is a cyclotomic field or QQ.\n```\n\n\nIn the function is_odd:\n\n```\n       if rings.is_ComplexField(self.base_ring()):\n            return abs(self(-1) - self.base_ring()(-1)) < 1.0/self.parent().zeta_order()\n```\n\nI do not understand why the rather mysterious expression 1.0/self.parent().zeta_order() is used.  I'd say that the difference is either 0 or 2, so if it's less than 1 in absolute value, this should already be sufficient to test numerically that it is 0.  Similarly for is_even().\n\nAnd now that I've put you back to work anyway, let's remove the C-style brackets in the if-statement in line 1616. ;).\n\n```\n            if(rings.is_ComplexField(C)):\n```\n",
    "created_at": "2011-11-14T18:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59464",
    "user": "https://trac.sagemath.org/admin/accounts/users/johanbosman"
}
```

The NotImplementedError message should also be adjusted in the gauss_sum() function as you did in gauss_sum_numerical().

```
sage: G = DirichletGroup(500, base_ring=RR)
sage: G[1].gauss_sum()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
...
NotImplementedError: Gauss sums only currently implemented when the base ring is a cyclotomic field or QQ.
```


In the function is_odd:

```
       if rings.is_ComplexField(self.base_ring()):
            return abs(self(-1) - self.base_ring()(-1)) < 1.0/self.parent().zeta_order()
```

I do not understand why the rather mysterious expression 1.0/self.parent().zeta_order() is used.  I'd say that the difference is either 0 or 2, so if it's less than 1 in absolute value, this should already be sufficient to test numerically that it is 0.  Similarly for is_even().

And now that I've put you back to work anyway, let's remove the C-style brackets in the if-statement in line 1616. ;).

```
            if(rings.is_ComplexField(C)):
```




---

archive/issue_comments_059465.json:
```json
{
    "body": "Attachment [trac_7191_v2.patch](tarball://root/attachments/some-uuid/ticket7191/trac_7191_v2.patch) by @fchapoton created at 2013-10-19 20:50:21",
    "created_at": "2013-10-19T20:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59465",
    "user": "https://github.com/fchapoton"
}
```

Attachment [trac_7191_v2.patch](tarball://root/attachments/some-uuid/ticket7191/trac_7191_v2.patch) by @fchapoton created at 2013-10-19 20:50:21



---

archive/issue_comments_059466.json:
```json
{
    "body": "Here is a new version with minor changes.\n\napply trac_7191_v2.patch",
    "created_at": "2013-10-19T20:51:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59466",
    "user": "https://github.com/fchapoton"
}
```

Here is a new version with minor changes.

apply trac_7191_v2.patch



---

archive/issue_comments_059467.json:
```json
{
    "body": "Here is a git branch\n----\nNew commits:",
    "created_at": "2014-01-07T19:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59467",
    "user": "https://github.com/fchapoton"
}
```

Here is a git branch
----
New commits:



---

archive/issue_comments_059468.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-04-24T08:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59468",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059469.json:
```json
{
    "body": "There was a merge conflict with the current development branch.  I also fixed a doctest and made the changes suggested by Johan in comment:9.  If you agree with these, it is a positive review from me.",
    "created_at": "2014-04-24T14:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59469",
    "user": "https://github.com/pjbruin"
}
```

There was a merge conflict with the current development branch.  I also fixed a doctest and made the changes suggested by Johan in comment:9.  If you agree with these, it is a positive review from me.



---

archive/issue_comments_059470.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-27T14:39:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59470",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_059471.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-05-27T14:39:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59471",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059472.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-05-29T18:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7191#issuecomment-59472",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_007410.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-05-29T18:54:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7191",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7191#event-7410"
}
```

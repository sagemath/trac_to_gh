# Issue 2704: bug in lcm(a,b) for a,b polynomials in QQ[] if a is constant

archive/issues_002704.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: lcm, polynomial, singular\n\nIn `QQ[]`, `lcm(X,1)` works fine but not `lcm(1,X)`:\n\n\n```\nsage: R.<X>=QQ[]\nsage: a=R(1)\nsage: b=X\nsage: lcm(b,a)\nX\nsage: lcm(a,b)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/jec/sage-2.11.alpha1/devel/sage-generic/sage/rings/<ipython console> in <module>()\n\n/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/rings/arith.py in lcm(a, b, integer)\n   1096     if not isinstance(a, RingElement):\n   1097         a = integer_ring.ZZ(a)\n-> 1098     return a.lcm(b)\n   1099\n   1100 LCM = lcm\n\n/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in lcm(self, singular, have_ring)\n    284         return _singular_init_func(self, singular, have_ring, force)\n    285     def lcm(self, singular=singular_default, have_ring=False):\n--> 286         return lcm_func(self, singular, have_ring)\n    287     def resultant(self, other, variable=None):\n    288         return resultant_func(self, other, variable)\n\n/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in lcm_func(self, right, have_ring)\n    385         (a^2 + a)*x^6*y + (a^3 + a - 1)*x^4*y + (-a)*x^4\n    386     \"\"\"\n--> 387     lcm = self._singular_(have_ring=have_ring).lcm(right._singular_(have_ring=have_ring))\n    388     return lcm.sage_poly(self.parent())\n    389\n\n/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, *args)\n    970\n    971     def __call__(self, *args):\n--> 972         return self._obj.parent().function_call(self._name, [self._obj] + list(args))\n    973\n    974     def help(self):\n\n/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/expect.py in function_call(self, function, args)\n    899             if not isinstance(args[i], ExpectElement):\n    900                 args[i] = self.new(args[i])\n--> 901         return self.new(\"%s(%s)\"%(function, \",\".join([s.name() for s in args])))\n    902\n    903     def call(self, function_name, *args):\n\n/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/expect.py in new(self, code)\n    801\n    802     def new(self, code):\n--> 803         return self(code)\n    804\n    805     ###################################################################\n\n/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/singular.py in __call__(self, x, type)\n    496             x = str(x)[1:-1]\n    497\n--> 498         return SingularElement(self, type, x, False)\n    499\n    500\n\n/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/singular.py in __init__(self, parent, type, value, is_name)\n    817             except (RuntimeError, TypeError, KeyboardInterrupt), x:\n    818                 self._session_number = -1\n--> 819                 raise TypeError, x\n    820         else:\n    821             self._name = value\n\n<type 'exceptions.TypeError'>: Singular error:\n   ? // ** list element must be an integer\n   ? error occurred in poly.lib::lcm line 721: ` ERROR(\"// ** list element must be an integer\");`\n   ? leaving poly.lib::lcm\n   skipping text from `;` error at token `)`\n```\n\n\nIt works fine in ZZ[] so I guess it's a problem with the singular interface.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2704\n\n",
    "created_at": "2008-03-28T18:22:46Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "bug in lcm(a,b) for a,b polynomials in QQ[] if a is constant",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2704",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

Keywords: lcm, polynomial, singular

In `QQ[]`, `lcm(X,1)` works fine but not `lcm(1,X)`:


```
sage: R.<X>=QQ[]
sage: a=R(1)
sage: b=X
sage: lcm(b,a)
X
sage: lcm(a,b)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/jec/sage-2.11.alpha1/devel/sage-generic/sage/rings/<ipython console> in <module>()

/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/rings/arith.py in lcm(a, b, integer)
   1096     if not isinstance(a, RingElement):
   1097         a = integer_ring.ZZ(a)
-> 1098     return a.lcm(b)
   1099
   1100 LCM = lcm

/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in lcm(self, singular, have_ring)
    284         return _singular_init_func(self, singular, have_ring, force)
    285     def lcm(self, singular=singular_default, have_ring=False):
--> 286         return lcm_func(self, singular, have_ring)
    287     def resultant(self, other, variable=None):
    288         return resultant_func(self, other, variable)

/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_singular_interface.py in lcm_func(self, right, have_ring)
    385         (a^2 + a)*x^6*y + (a^3 + a - 1)*x^4*y + (-a)*x^4
    386     """
--> 387     lcm = self._singular_(have_ring=have_ring).lcm(right._singular_(have_ring=have_ring))
    388     return lcm.sage_poly(self.parent())
    389

/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, *args)
    970
    971     def __call__(self, *args):
--> 972         return self._obj.parent().function_call(self._name, [self._obj] + list(args))
    973
    974     def help(self):

/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/expect.py in function_call(self, function, args)
    899             if not isinstance(args[i], ExpectElement):
    900                 args[i] = self.new(args[i])
--> 901         return self.new("%s(%s)"%(function, ",".join([s.name() for s in args])))
    902
    903     def call(self, function_name, *args):

/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/expect.py in new(self, code)
    801
    802     def new(self, code):
--> 803         return self(code)
    804
    805     ###################################################################

/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/singular.py in __call__(self, x, type)
    496             x = str(x)[1:-1]
    497
--> 498         return SingularElement(self, type, x, False)
    499
    500

/home/jec/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/singular.py in __init__(self, parent, type, value, is_name)
    817             except (RuntimeError, TypeError, KeyboardInterrupt), x:
    818                 self._session_number = -1
--> 819                 raise TypeError, x
    820         else:
    821             self._name = value

<type 'exceptions.TypeError'>: Singular error:
   ? // ** list element must be an integer
   ? error occurred in poly.lib::lcm line 721: ` ERROR("// ** list element must be an integer");`
   ? leaving poly.lib::lcm
   skipping text from `;` error at token `)`
```


It works fine in ZZ[] so I guess it's a problem with the singular interface.


Issue created by migration from https://trac.sagemath.org/ticket/2704





---

archive/issue_comments_018609.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2008-04-15T04:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2704#issuecomment-18609",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_comments_018610.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2008-04-15T04:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2704#issuecomment-18610",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to critical.



---

archive/issue_comments_018611.json:
```json
{
    "body": "Changing component from interfaces to commutative algebra.",
    "created_at": "2008-04-15T04:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2704#issuecomment-18611",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from interfaces to commutative algebra.



---

archive/issue_comments_018612.json:
```json
{
    "body": "Martin,\n\nthis sounds like something that is in your domain. Can you check it out?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-15T04:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2704#issuecomment-18612",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Martin,

this sounds like something that is in your domain. Can you check it out?

Cheers,

Michael



---

archive/issue_comments_018613.json:
```json
{
    "body": "Attachment [trac_2704_poly_lcm.patch](tarball://root/attachments/some-uuid/ticket2704/trac_2704_poly_lcm.patch) by @malb created at 2008-04-15 09:02:58",
    "created_at": "2008-04-15T09:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2704#issuecomment-18613",
    "user": "https://github.com/malb"
}
```

Attachment [trac_2704_poly_lcm.patch](tarball://root/attachments/some-uuid/ticket2704/trac_2704_poly_lcm.patch) by @malb created at 2008-04-15 09:02:58



---

archive/issue_comments_018614.json:
```json
{
    "body": "patch attached.",
    "created_at": "2008-04-15T09:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2704#issuecomment-18614",
    "user": "https://github.com/malb"
}
```

patch attached.



---

archive/issue_comments_018615.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-15T09:15:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2704#issuecomment-18615",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_018616.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-15T09:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2704#issuecomment-18616",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha5



---

archive/issue_comments_018617.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-15T09:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2704#issuecomment-18617",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

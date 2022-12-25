# Issue 9054: create a class for basic function_field arithmetic for Sage

archive/issues_009054.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @burcin khwilson @koffie @mstreng @novoselt @pjbruin minz @saraedum\n\nOne of the first things we learned at Sage Days 21: Function Fields, is that it is not even possible to really define or even do arithmetic in function fields *at all* in Sage!  It's amazing that this most basic arithmetic still isn't supported, but it isn't (maybe it used to be via generic machinery, but got broken...?).  The point of this ticket is to create classes for standard function field structures, along with support for arithmetic.   This should be organized in a way similar to number fields. \n\nFor this code, the main point is to establish an API that works solidly.  It will be insanely slow.  A subsequent patch will make things fast. \n\nSee also: #9069, #9051, #9094, #9095.\n\nNote that the dependancy on #9138 is only because of a really minor change in the doctests. This ticket already has a positive review so I suspect this will get merged first. If that ticket eventually gets rejected it will be trivial to rebase the patch withouth that ticket.\n\nApply [attachment:9054_function_fields.patch] to the Sage library.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9054\n\n",
    "closed_at": "2012-02-02T12:52:09Z",
    "created_at": "2010-05-26T11:21:12Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "create a class for basic function_field arithmetic for Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9054",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @burcin khwilson @koffie @mstreng @novoselt @pjbruin minz @saraedum

One of the first things we learned at Sage Days 21: Function Fields, is that it is not even possible to really define or even do arithmetic in function fields *at all* in Sage!  It's amazing that this most basic arithmetic still isn't supported, but it isn't (maybe it used to be via generic machinery, but got broken...?).  The point of this ticket is to create classes for standard function field structures, along with support for arithmetic.   This should be organized in a way similar to number fields. 

For this code, the main point is to establish an API that works solidly.  It will be insanely slow.  A subsequent patch will make things fast. 

See also: #9069, #9051, #9094, #9095.

Note that the dependancy on #9138 is only because of a really minor change in the doctests. This ticket already has a positive review so I suspect this will get merged first. If that ticket eventually gets rejected it will be trivial to rebase the patch withouth that ticket.

Apply [attachment:9054_function_fields.patch] to the Sage library.

Issue created by migration from https://trac.sagemath.org/ticket/9054





---

archive/issue_comments_083717.json:
```json
{
    "body": "Attachment [trac_9054-part1.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part1.patch) by @burcin created at 2010-05-26 22:22:52",
    "created_at": "2010-05-26T22:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83717",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_9054-part1.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part1.patch) by @burcin created at 2010-05-26 22:22:52



---

archive/issue_comments_083718.json:
```json
{
    "body": "Attachment [trac_9054-part2.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part2.patch) by @williamstein created at 2010-05-27 01:27:22",
    "created_at": "2010-05-27T01:27:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83718",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9054-part2.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part2.patch) by @williamstein created at 2010-05-27 01:27:22



---

archive/issue_comments_083719.json:
```json
{
    "body": "Attachment [trac_9054-part3.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part3.patch) by @williamstein created at 2010-05-27 03:01:01",
    "created_at": "2010-05-27T03:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83719",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9054-part3.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part3.patch) by @williamstein created at 2010-05-27 03:01:01



---

archive/issue_comments_083720.json:
```json
{
    "body": "There seems to be an issue with returning the base ring of a RationalFunctionField. Neither base() nor base_ring() return the correct ring:\n\n\n```\nsage: K.<t> = FunctionField(QQ); K\nRational function field in t over Rational Field\nsage: R1 = K.base(); R1\nRational function field in t over Rational Field\nsage: R2 = K.base_ring(); R2\nRational function field in t over Rational Field\nsage: R3.<s> = QQ[]; K3 = Frac(R3); K3\nFraction Field of Univariate Polynomial Ring in s over Rational Field\nsage: R3\nUnivariate Polynomial Ring in s over Rational Field\nsage: K3.base() == R3\nTrue\n```",
    "created_at": "2010-05-27T05:38:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83720",
    "user": "https://trac.sagemath.org/admin/accounts/users/salmanhb"
}
```

There seems to be an issue with returning the base ring of a RationalFunctionField. Neither base() nor base_ring() return the correct ring:


```
sage: K.<t> = FunctionField(QQ); K
Rational function field in t over Rational Field
sage: R1 = K.base(); R1
Rational function field in t over Rational Field
sage: R2 = K.base_ring(); R2
Rational function field in t over Rational Field
sage: R3.<s> = QQ[]; K3 = Frac(R3); K3
Fraction Field of Univariate Polynomial Ring in s over Rational Field
sage: R3
Univariate Polynomial Ring in s over Rational Field
sage: K3.base() == R3
True
```



---

archive/issue_comments_083721.json:
```json
{
    "body": "Attachment [trac_9054-part5.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part5.patch) by @robertwb created at 2010-05-27 10:10:47",
    "created_at": "2010-05-27T10:10:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83721",
    "user": "https://github.com/robertwb"
}
```

Attachment [trac_9054-part5.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part5.patch) by @robertwb created at 2010-05-27 10:10:47



---

archive/issue_comments_083722.json:
```json
{
    "body": "Looks like you forgot to add the file `function_field_order`, so I wasn't able to doctest on top of your latest patch (let alone debug it). See also #9051 for added speed in the positive characteristic case.",
    "created_at": "2010-05-27T10:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83722",
    "user": "https://github.com/robertwb"
}
```

Looks like you forgot to add the file `function_field_order`, so I wasn't able to doctest on top of your latest patch (let alone debug it). See also #9051 for added speed in the positive characteristic case.



---

archive/issue_comments_083723.json:
```json
{
    "body": "Attachment [trac_9054-part7.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part7.patch) by @williamstein created at 2010-05-27 22:53:04\n\npolynomial factorization!",
    "created_at": "2010-05-27T22:53:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83723",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9054-part7.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part7.patch) by @williamstein created at 2010-05-27 22:53:04

polynomial factorization!



---

archive/issue_comments_083724.json:
```json
{
    "body": "FunctionField constructor clips names\n\n```\nsage: F = FunctionField(GF(7), 'bit')\nsage: F.gen()\nb\n```",
    "created_at": "2010-05-28T01:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83724",
    "user": "https://github.com/jbalakrishnan"
}
```

FunctionField constructor clips names

```
sage: F = FunctionField(GF(7), 'bit')
sage: F.gen()
b
```



---

archive/issue_comments_083725.json:
```json
{
    "body": "ideals and orders!",
    "created_at": "2010-05-28T06:29:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83725",
    "user": "https://github.com/williamstein"
}
```

ideals and orders!



---

archive/issue_comments_083726.json:
```json
{
    "body": "Attachment [trac_9054-part8.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part8.patch) by @williamstein created at 2010-05-28 08:22:52\n\ninverses of fractional ideals",
    "created_at": "2010-05-28T08:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83726",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9054-part8.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part8.patch) by @williamstein created at 2010-05-28 08:22:52

inverses of fractional ideals



---

archive/issue_comments_083727.json:
```json
{
    "body": "Attachment [trac_9054-part9.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part9.patch) by @williamstein created at 2010-05-28 10:54:25\n\nReplying to [comment:2 salmanhb]:\n> There seems to be an issue with returning the base ring of a RationalFunctionField. Neither base() nor base_ring() return the correct ring:\n> \n> \n> \n> ```\n> sage: K.<t> = FunctionField(QQ); K\n> Rational function field in t over Rational Field\n> sage: R1 = K.base(); R1\n> Rational function field in t over Rational Field\n> sage: R2 = K.base_ring(); R2\n> Rational function field in t over Rational Field\n> sage: R3.<s> = QQ[]; K3 = Frac(R3); K3\n> Fraction Field of Univariate Polynomial Ring in s over Rational Field\n> sage: R3\n> Univariate Polynomial Ring in s over Rational Field\n> sage: K3.base() == R3\n> True\n> ```\n\n\nThe above is correct.  To get what you want, use the constant_field() method. \n\n```\nsage: K.<t> = FunctionField(QQ);\nsage: K.constant_field()\nRational Field\n```",
    "created_at": "2010-05-28T10:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83727",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9054-part9.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part9.patch) by @williamstein created at 2010-05-28 10:54:25

Replying to [comment:2 salmanhb]:
> There seems to be an issue with returning the base ring of a RationalFunctionField. Neither base() nor base_ring() return the correct ring:
> 
> 
> 
> ```
> sage: K.<t> = FunctionField(QQ); K
> Rational function field in t over Rational Field
> sage: R1 = K.base(); R1
> Rational function field in t over Rational Field
> sage: R2 = K.base_ring(); R2
> Rational function field in t over Rational Field
> sage: R3.<s> = QQ[]; K3 = Frac(R3); K3
> Fraction Field of Univariate Polynomial Ring in s over Rational Field
> sage: R3
> Univariate Polynomial Ring in s over Rational Field
> sage: K3.base() == R3
> True
> ```


The above is correct.  To get what you want, use the constant_field() method. 

```
sage: K.<t> = FunctionField(QQ);
sage: K.constant_field()
Rational Field
```



---

archive/issue_comments_083728.json:
```json
{
    "body": "morphisms of function fields",
    "created_at": "2010-05-28T10:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83728",
    "user": "https://github.com/williamstein"
}
```

morphisms of function fields



---

archive/issue_comments_083729.json:
```json
{
    "body": "Attachment [trac_9054-part10.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part10.patch) by @williamstein created at 2010-05-29 03:13:02",
    "created_at": "2010-05-29T03:13:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83729",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9054-part10.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part10.patch) by @williamstein created at 2010-05-29 03:13:02



---

archive/issue_comments_083730.json:
```json
{
    "body": "Attachment [trac_9054-part12.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part12.patch) by @robertwb created at 2010-05-30 09:54:48\n\nVarious methods needed for #9095 (doctesets depend on #9094)",
    "created_at": "2010-05-30T09:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83730",
    "user": "https://github.com/robertwb"
}
```

Attachment [trac_9054-part12.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part12.patch) by @robertwb created at 2010-05-30 09:54:48

Various methods needed for #9095 (doctesets depend on #9094)



---

archive/issue_comments_083731.json:
```json
{
    "body": "Should be some automatic way to do the following:\n\n```\nK.<T> = FunctionField(GF(17))\nP = T-5\nf = P^5\nR = K._ring\nR(f.element()).valuation(R(p.element()))\n```",
    "created_at": "2010-06-04T22:17:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83731",
    "user": "https://trac.sagemath.org/admin/accounts/users/khwilson"
}
```

Should be some automatic way to do the following:

```
K.<T> = FunctionField(GF(17))
P = T-5
f = P^5
R = K._ring
R(f.element()).valuation(R(p.element()))
```



---

archive/issue_comments_083732.json:
```json
{
    "body": "Attachment [trac_9054-part1-12.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part1-12.patch) by @williamstein created at 2010-07-06 09:25:32\n\nflattened patch that incorporates all of patches 1-12 above into a single patch.",
    "created_at": "2010-07-06T09:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83732",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9054-part1-12.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-part1-12.patch) by @williamstein created at 2010-07-06 09:25:32

flattened patch that incorporates all of patches 1-12 above into a single patch.



---

archive/issue_comments_083733.json:
```json
{
    "body": "Here is a link to the result of doctesting sage-4.4.4 + patches 1-12:\n\n   http://sage.math.washington.edu/home/wstein/patches/9054-part1-12.doctest.txt\n\nThe failed tests:\n\n```\nThe following tests failed:\n\n        sage -t  devel/sage-main/sage/matrix/matrix2.pyx # 1 doctests failed\n        sage -t  devel/sage-main/sage/plot/matrix_plot.py # 0 doctests failed\n        sage -t  devel/sage-main/sage/modular/abvar/morphism.py # 1 doctests failed\n        sage -t  devel/sage-main/sage/modular/abvar/finite_subgroup.py # 1 doctests failed\n        sage -t  devel/sage-main/sage/tests/startup.py # 1 doctests failed\n        sage -t  devel/sage-main/sage/modular/modform/hecke_operator_on_qexp.py # 1 doctests failed\n        sage -t  devel/sage-main/sage/categories/function_fields.py # 5 doctests failed\n        sage -t  devel/sage-main/sage/rings/function_field/function_field_element.pyx # 14 doctests failed\n```",
    "created_at": "2010-07-06T09:37:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83733",
    "user": "https://github.com/williamstein"
}
```

Here is a link to the result of doctesting sage-4.4.4 + patches 1-12:

   http://sage.math.washington.edu/home/wstein/patches/9054-part1-12.doctest.txt

The failed tests:

```
The following tests failed:

        sage -t  devel/sage-main/sage/matrix/matrix2.pyx # 1 doctests failed
        sage -t  devel/sage-main/sage/plot/matrix_plot.py # 0 doctests failed
        sage -t  devel/sage-main/sage/modular/abvar/morphism.py # 1 doctests failed
        sage -t  devel/sage-main/sage/modular/abvar/finite_subgroup.py # 1 doctests failed
        sage -t  devel/sage-main/sage/tests/startup.py # 1 doctests failed
        sage -t  devel/sage-main/sage/modular/modform/hecke_operator_on_qexp.py # 1 doctests failed
        sage -t  devel/sage-main/sage/categories/function_fields.py # 5 doctests failed
        sage -t  devel/sage-main/sage/rings/function_field/function_field_element.pyx # 14 doctests failed
```



---

archive/issue_comments_083734.json:
```json
{
    "body": "Changing assignee from @aghitza to @williamstein.",
    "created_at": "2010-07-06T09:37:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83734",
    "user": "https://github.com/williamstein"
}
```

Changing assignee from @aghitza to @williamstein.



---

archive/issue_comments_083735.json:
```json
{
    "body": "NOTE: #9094 implements sqrt for polynomials, which is relevant to trac_9054-doctest.patch",
    "created_at": "2010-07-07T13:01:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83735",
    "user": "https://github.com/williamstein"
}
```

NOTE: #9094 implements sqrt for polynomials, which is relevant to trac_9054-doctest.patch



---

archive/issue_comments_083736.json:
```json
{
    "body": "I guess the doctest patch isn't really usefull addition to sage (although making it was a usefull learning experience for Peter Bruin and me since it was our first patch). The patch fixes some bugs which are also fixed in other patches in trac. Some are indeed fixed by #9094 (although i think this can be done faster and more elegant) and another one related calculating the valuation in fraction fields is fixed by 9051-FpT_4.patch in #9051.\n\nSince I'm quite new to developing and using trac and hg etc. I would like to know what is the best thing to do now. And especially how to deal with the relating patches wich also contain fixes for stuff happening here.",
    "created_at": "2010-07-07T21:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83736",
    "user": "https://github.com/koffie"
}
```

I guess the doctest patch isn't really usefull addition to sage (although making it was a usefull learning experience for Peter Bruin and me since it was our first patch). The patch fixes some bugs which are also fixed in other patches in trac. Some are indeed fixed by #9094 (although i think this can be done faster and more elegant) and another one related calculating the valuation in fraction fields is fixed by 9051-FpT_4.patch in #9051.

Since I'm quite new to developing and using trac and hg etc. I would like to know what is the best thing to do now. And especially how to deal with the relating patches wich also contain fixes for stuff happening here.



---

archive/issue_comments_083737.json:
```json
{
    "body": "Added an attachment that fixes all but three doctest failures. The remaining failures are:\n\n```\n\nsage -t \u00a0\"devel/sage-mderickx/sage/modular/abvar/morphism.py\" # 1 failure\n\nsage -t \u00a0\"devel/sage-mderickx/sage/modular/abvar/finite_subgroup.py\" # 1 failure\n\nsage -t \u00a0\"devel/sage-main/sage/modular/modform/hecke_operator_on_qexp.py\" # 1 failure\n\n}}}They are all related since their error messages all end in:`\u00a0\u00a0 \u00a0 \u00a0File \"/Applications/sage/local/lib/python/site-packages/sage/modules/free_module.py\", line 4700, in _echelonized_basis\u00a0\u00a0 \u00a0 \u00a0 \u00a0d = self._denominator(basis)\u00a0\u00a0 \u00a0 \u00a0File \"/Applications/sage/local/lib/python/site-packages/sage/modules/free_module.py\", line 4810, in _denominator\u00a0\u00a0 \u00a0 \u00a0 \u00a0d = d.lcm(x.denominator())\u00a0\u00a0 \u00a0!AttributeError: 'int' object has no attribute 'lcm'`It would be nice if someone who has a better understanding of sage to fix this final bug, since then we would have no doctests failing anymore for this patch.",
    "created_at": "2010-07-17T11:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83737",
    "user": "https://github.com/koffie"
}
```

Added an attachment that fixes all but three doctest failures. The remaining failures are:

```

sage -t  "devel/sage-mderickx/sage/modular/abvar/morphism.py" # 1 failure

sage -t  "devel/sage-mderickx/sage/modular/abvar/finite_subgroup.py" # 1 failure

sage -t  "devel/sage-main/sage/modular/modform/hecke_operator_on_qexp.py" # 1 failure

}}}They are all related since their error messages all end in:`      File "/Applications/sage/local/lib/python/site-packages/sage/modules/free_module.py", line 4700, in _echelonized_basis        d = self._denominator(basis)      File "/Applications/sage/local/lib/python/site-packages/sage/modules/free_module.py", line 4810, in _denominator        d = d.lcm(x.denominator())    !AttributeError: 'int' object has no attribute 'lcm'`It would be nice if someone who has a better understanding of sage to fix this final bug, since then we would have no doctests failing anymore for this patch.



---

archive/issue_comments_083738.json:
```json
{
    "body": "Oeps, wrong fromatting. Now a bit more readable:\n\n```\nsage -t  \"devel/sage-mderickx/sage/modular/abvar/morphism.py\" # 1 failure\n\nsage -t  \"devel/sage-mderickx/sage/modular/abvar/finite_subgroup.py\" # 1 failure\n\nsage -t  \"devel/sage-main/sage/modular/modform/hecke_operator_on_qexp.py\" # 1 failure\n\n```\n\nThey are all related since their error messages all end in:\n\n```\n\n      File \"/Applications/sage/local/lib/python/site-packages/sage/modules/free_module.py\", line 4700, in _echelonized_basis\n        d = self._denominator(basis)\n      File \"/Applications/sage/local/lib/python/site-packages/sage/modules/free_module.py\", line 4810, in _denominator\n        d = d.lcm(x.denominator())\n    AttributeError: 'int' object has no attribute 'lcm'\n```",
    "created_at": "2010-07-17T11:05:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83738",
    "user": "https://github.com/koffie"
}
```

Oeps, wrong fromatting. Now a bit more readable:

```
sage -t  "devel/sage-mderickx/sage/modular/abvar/morphism.py" # 1 failure

sage -t  "devel/sage-mderickx/sage/modular/abvar/finite_subgroup.py" # 1 failure

sage -t  "devel/sage-main/sage/modular/modform/hecke_operator_on_qexp.py" # 1 failure

```

They are all related since their error messages all end in:

```

      File "/Applications/sage/local/lib/python/site-packages/sage/modules/free_module.py", line 4700, in _echelonized_basis
        d = self._denominator(basis)
      File "/Applications/sage/local/lib/python/site-packages/sage/modules/free_module.py", line 4810, in _denominator
        d = d.lcm(x.denominator())
    AttributeError: 'int' object has no attribute 'lcm'
```



---

archive/issue_comments_083739.json:
```json
{
    "body": "Has there been any work on this since sage days > 23? Even if the work is only partially finnished it would be good to know to avoid double work.",
    "created_at": "2010-07-30T18:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83739",
    "user": "https://github.com/koffie"
}
```

Has there been any work on this since sage days > 23? Even if the work is only partially finnished it would be good to know to avoid double work.



---

archive/issue_comments_083740.json:
```json
{
    "body": "Attachment [trac_9054-doctest.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-doctest.patch) by @koffie created at 2010-07-31 16:08:17\n\nAplies to sage 4.4.4 after 1-12 patch and it also needs the #9054 patch trac_9094-sqrt-mderickx.patch",
    "created_at": "2010-07-31T16:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83740",
    "user": "https://github.com/koffie"
}
```

Attachment [trac_9054-doctest.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-doctest.patch) by @koffie created at 2010-07-31 16:08:17

Aplies to sage 4.4.4 after 1-12 patch and it also needs the #9054 patch trac_9094-sqrt-mderickx.patch



---

archive/issue_comments_083741.json:
```json
{
    "body": "Replying to [comment:20 mderickx]:\n> Has there been any work on this since sage days > 23? Even if the work is only partially \n> finished it would be good to know to avoid double work.\n\n\nThere has been no further work.   When I do work further on this, I will post a patch.  I always post patches of everything I do as I go, as soon as I'm done with a session of work.",
    "created_at": "2010-08-25T05:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83741",
    "user": "https://github.com/williamstein"
}
```

Replying to [comment:20 mderickx]:
> Has there been any work on this since sage days > 23? Even if the work is only partially 
> finished it would be good to know to avoid double work.


There has been no further work.   When I do work further on this, I will post a patch.  I always post patches of everything I do as I go, as soon as I'm done with a session of work.



---

archive/issue_comments_083742.json:
```json
{
    "body": "I am moving this entirely out of Sage and into the psage library.   See\n\n   http://code.google.com/p/purplesage/issues/detail?id=3",
    "created_at": "2010-10-26T15:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83742",
    "user": "https://github.com/williamstein"
}
```

I am moving this entirely out of Sage and into the psage library.   See

   http://code.google.com/p/purplesage/issues/detail?id=3



---

archive/issue_events_022178.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-10-26T22:47:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9054#event-22178"
}
```



---

archive/issue_comments_083743.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-10-26T22:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83743",
    "user": "https://github.com/williamstein"
}
```

Resolution: wontfix



---

archive/issue_comments_083744.json:
```json
{
    "body": "I'm closing this since I'm no longer interested in getting it included in the main sage distribution.  It is now in psage as mentioned above.",
    "created_at": "2010-10-26T22:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83744",
    "user": "https://github.com/williamstein"
}
```

I'm closing this since I'm no longer interested in getting it included in the main sage distribution.  It is now in psage as mentioned above.



---

archive/issue_events_022179.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-10-27T08:20:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9054#event-22179"
}
```



---

archive/issue_comments_083745.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-10-27T16:05:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83745",
    "user": "https://github.com/robertwb"
}
```

Changing status from closed to new.



---

archive/issue_events_022180.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2010-10-27T16:05:50Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9054#event-22180"
}
```



---

archive/issue_comments_083746.json:
```json
{
    "body": "I think eventually this should be in the main sage distribution, even if no one's actively working on it right now.",
    "created_at": "2010-10-27T16:05:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83746",
    "user": "https://github.com/robertwb"
}
```

I think eventually this should be in the main sage distribution, even if no one's actively working on it right now.



---

archive/issue_comments_083747.json:
```json
{
    "body": "Resolution changed from wontfix to ",
    "created_at": "2010-10-27T16:05:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83747",
    "user": "https://github.com/robertwb"
}
```

Resolution changed from wontfix to 



---

archive/issue_events_022181.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2010-10-27T16:05:50Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9054#event-22181"
}
```



---

archive/issue_events_022182.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2010-10-27T16:05:50Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9054#event-22182"
}
```



---

archive/issue_comments_083748.json:
```json
{
    "body": "There should be no doctest failures left. Comments, remarks, and reviews are welcome. :)\n\nApply trac_9054-all-parts.patch\n\nDepends on #9094, #11034",
    "created_at": "2011-03-31T15:14:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83748",
    "user": "https://trac.sagemath.org/admin/accounts/users/minz"
}
```

There should be no doctest failures left. Comments, remarks, and reviews are welcome. :)

Apply trac_9054-all-parts.patch

Depends on #9094, #11034



---

archive/issue_comments_083749.json:
```json
{
    "body": "The doctests of `function_field.py` contain the following lines:\n\n```\nsage: R.<x> = FunctionField(QQ); S.<y> = R[]\nsage: R2.<t> = FunctionField(QQ); S2.<w> = R2[]\nsage: L2.<w> = R.extension((4*w)^2 - (t+1)^3 - 1)\n```\nI think it is confusing that it does not make a difference whether you write R.extension or R2.extension in this example. I'm new to sage so maybe I'm misunderstanding something here.",
    "created_at": "2011-06-08T19:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83749",
    "user": "https://github.com/saraedum"
}
```

The doctests of `function_field.py` contain the following lines:

```
sage: R.<x> = FunctionField(QQ); S.<y> = R[]
sage: R2.<t> = FunctionField(QQ); S2.<w> = R2[]
sage: L2.<w> = R.extension((4*w)^2 - (t+1)^3 - 1)
```
I think it is confusing that it does not make a difference whether you write R.extension or R2.extension in this example. I'm new to sage so maybe I'm misunderstanding something here.



---

archive/issue_comments_083750.json:
```json
{
    "body": "Attachment [trac_9054_polynomial_base_field.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_polynomial_base_field.patch) by @saraedum created at 2011-06-08 19:56:44\n\npolynomial used for a field extension must be defined over the base field",
    "created_at": "2011-06-08T19:56:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83750",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_polynomial_base_field.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_polynomial_base_field.patch) by @saraedum created at 2011-06-08 19:56:44

polynomial used for a field extension must be defined over the base field



---

archive/issue_comments_083751.json:
```json
{
    "body": "There are some problems with the zero of a function field:\n\n```\nsage: K.<x> = FunctionField(QQ); R.<y> = K[]; L.<y> = K.extension(y^2+x);\nsage: coerce(L,L.polynomial())==0\nFalse\nsage: y/0\n0\n```",
    "created_at": "2011-06-28T17:22:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83751",
    "user": "https://github.com/saraedum"
}
```

There are some problems with the zero of a function field:

```
sage: K.<x> = FunctionField(QQ); R.<y> = K[]; L.<y> = K.extension(y^2+x);
sage: coerce(L,L.polynomial())==0
False
sage: y/0
0
```



---

archive/issue_comments_083752.json:
```json
{
    "body": "fixes the problems regarding zero.",
    "created_at": "2011-06-28T17:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83752",
    "user": "https://github.com/saraedum"
}
```

fixes the problems regarding zero.



---

archive/issue_comments_083753.json:
```json
{
    "body": "Attachment [trac_9054_zero.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_zero.patch) by @saraedum created at 2011-07-22 16:26:22\n\nEntering the following at the sage prompt produces a `TypeError: Unable to coerce -u^2 (...) to Rational`.\n\n```\nK.<x> = FunctionField(QQ); R.<y> = K[]\nL.<y> = K.extension(y^2 - x)\nM.<u> = FunctionField(QQ); R.<v> = M[]\nN.<v> = M.extension(v-u^2)\nL.hom([u,v])\n```\nThis is due to the fact that `hom()` determines the codomain by looking only at the first element of `[u,v]`.",
    "created_at": "2011-07-22T16:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83753",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_zero.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_zero.patch) by @saraedum created at 2011-07-22 16:26:22

Entering the following at the sage prompt produces a `TypeError: Unable to coerce -u^2 (...) to Rational`.

```
K.<x> = FunctionField(QQ); R.<y> = K[]
L.<y> = K.extension(y^2 - x)
M.<u> = FunctionField(QQ); R.<v> = M[]
N.<v> = M.extension(v-u^2)
L.hom([u,v])
```
This is due to the fact that `hom()` determines the codomain by looking only at the first element of `[u,v]`.



---

archive/issue_comments_083754.json:
```json
{
    "body": "Attachment [trac_9054_codomain.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_codomain.patch) by @saraedum created at 2011-07-22 16:27:07\n\nset the correct codomain for function fields",
    "created_at": "2011-07-22T16:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83754",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_codomain.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_codomain.patch) by @saraedum created at 2011-07-22 16:27:07

set the correct codomain for function fields



---

archive/issue_comments_083755.json:
```json
{
    "body": "Attachment [trac_9054_doctest-2.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_doctest-2.patch) by @saraedum created at 2011-07-22 16:49:18\n\nfixes hash doctests for 32bit and a random doctest",
    "created_at": "2011-07-22T16:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83755",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_doctest-2.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_doctest-2.patch) by @saraedum created at 2011-07-22 16:49:18

fixes hash doctests for 32bit and a random doctest



---

archive/issue_comments_083756.json:
```json
{
    "body": "Is there a reason why a FunctionFieldMorphism is a Map and not a RingHomomorphism?",
    "created_at": "2011-07-22T17:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83756",
    "user": "https://github.com/saraedum"
}
```

Is there a reason why a FunctionFieldMorphism is a Map and not a RingHomomorphism?



---

archive/issue_comments_083757.json:
```json
{
    "body": "Attachment [trac_9054_function_fields_sd32.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_function_fields_sd32.patch) by @saraedum created at 2011-08-25 05:04:33\n\nMinimal support for functions field. Does not include all of the above patches.",
    "created_at": "2011-08-25T05:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83757",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_function_fields_sd32.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_function_fields_sd32.patch) by @saraedum created at 2011-08-25 05:04:33

Minimal support for functions field. Does not include all of the above patches.



---

archive/issue_comments_083758.json:
```json
{
    "body": "I'm now busy with very troughly checking the entire patch wich at least with some changed free module stuff passes all doctests. There will be a big doctest patch comming up which includes tests I've thought up to also test some more none trivial examples.\n\nThere is are at least two big issues which I run in to today. They all occured in the same terminal session.\n\n```\nsage: K.<x> = FunctionField(QQ)\nsage: R.<y> = K[]\nsage: L.<w> = K.extension(y^5 - (x^3 + 2*x*y + 1/x));\nsage: w.is_integral()\nFalse\nsage: L.order(w)  #should raise a value error since orders can only be generated by integral elements\nOrder in Function field in w defined by y^5 - 2*x*y + (-x^4 - 1)/x\nsage: L.order(w).gens()\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/Users/maarten/Downloads/sage-4.7.2.alpha2/devel/sage-main/<ipython console> in <module>()\n\n/Users/maarten/Downloads/sage-4.7.2.alpha2/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens.gens (sage/structure/parent_gens.c:2741)()\n\n/Users/maarten/Downloads/sage-4.7.2.alpha2/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens.ngens (sage/structure/parent_gens.c:2548)()\n\n/Users/maarten/Downloads/sage-4.7.2.alpha2/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.check_old_coerce (sage/structure/parent_gens.c:1228)()\n\nRuntimeError: Order in Function field in w defined by y^5 - 2*x*y + (-x^4 - 1)/x still using old coercion framework\n```",
    "created_at": "2011-08-26T22:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83758",
    "user": "https://github.com/koffie"
}
```

I'm now busy with very troughly checking the entire patch wich at least with some changed free module stuff passes all doctests. There will be a big doctest patch comming up which includes tests I've thought up to also test some more none trivial examples.

There is are at least two big issues which I run in to today. They all occured in the same terminal session.

```
sage: K.<x> = FunctionField(QQ)
sage: R.<y> = K[]
sage: L.<w> = K.extension(y^5 - (x^3 + 2*x*y + 1/x));
sage: w.is_integral()
False
sage: L.order(w)  #should raise a value error since orders can only be generated by integral elements
Order in Function field in w defined by y^5 - 2*x*y + (-x^4 - 1)/x
sage: L.order(w).gens()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/Users/maarten/Downloads/sage-4.7.2.alpha2/devel/sage-main/<ipython console> in <module>()

/Users/maarten/Downloads/sage-4.7.2.alpha2/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens.gens (sage/structure/parent_gens.c:2741)()

/Users/maarten/Downloads/sage-4.7.2.alpha2/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens.ngens (sage/structure/parent_gens.c:2548)()

/Users/maarten/Downloads/sage-4.7.2.alpha2/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.check_old_coerce (sage/structure/parent_gens.c:1228)()

RuntimeError: Order in Function field in w defined by y^5 - 2*x*y + (-x^4 - 1)/x still using old coercion framework
```



---

archive/issue_comments_083759.json:
```json
{
    "body": "the review patch is not entirely ready, but julian wanted to have a look so I uploaded it",
    "created_at": "2011-08-28T06:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83759",
    "user": "https://github.com/koffie"
}
```

the review patch is not entirely ready, but julian wanted to have a look so I uploaded it



---

archive/issue_comments_083760.json:
```json
{
    "body": "At [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c62fa3dae0a2ca82), Maarten mentioned that pickling does not seem to work for the code posted here, which seems to be due to some attributes typically involved in coercion.\n\nLooking at [attachment:trac_9054-all-parts.patch], I see that the base class for function fields is derived from `sage.rings.ring.Field`, but `Field.__init__` is not called.\n\nThe rings in vanilla Sage do not pay enough attention to coercion and categories. #9944 and (in particular) #9138 aim at improving the situation. In particular, with #9138 it should now possible to avoid any direct call to `ParentWithGens.__init__`; calling `Field.__init__` should just work (tm). Can you try?",
    "created_at": "2011-08-28T06:58:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83760",
    "user": "https://github.com/simon-king-jena"
}
```

At [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c62fa3dae0a2ca82), Maarten mentioned that pickling does not seem to work for the code posted here, which seems to be due to some attributes typically involved in coercion.

Looking at [attachment:trac_9054-all-parts.patch], I see that the base class for function fields is derived from `sage.rings.ring.Field`, but `Field.__init__` is not called.

The rings in vanilla Sage do not pay enough attention to coercion and categories. #9944 and (in particular) #9138 aim at improving the situation. In particular, with #9138 it should now possible to avoid any direct call to `ParentWithGens.__init__`; calling `Field.__init__` should just work (tm). Can you try?



---

archive/issue_comments_083761.json:
```json
{
    "body": "PS: After [attachment:trac_9054-all-parts.patch] was created, several other patches were posted. Can you please clearly state (in the ticket description and, for the patchbot, also in a comment) which patches are supposed to be applied? It is difficult to work on the pickling problem (or reviewing) if it is not clear what code exactly we are talking about.",
    "created_at": "2011-08-28T07:03:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83761",
    "user": "https://github.com/simon-king-jena"
}
```

PS: After [attachment:trac_9054-all-parts.patch] was created, several other patches were posted. Can you please clearly state (in the ticket description and, for the patchbot, also in a comment) which patches are supposed to be applied? It is difficult to work on the pickling problem (or reviewing) if it is not clear what code exactly we are talking about.



---

archive/issue_comments_083762.json:
```json
{
    "body": "Here are some comments on [attachment:trac_9054-all-parts.patch]:\n\n* Please remove the `__contains__` method from the category `FunctionFields`. Containment in categories should rely on the default implementation, unless there is a compelling reason to do otherwise.\n\n Even worse, your containment test is ultimately based on testing class inheritance (namely in the function `is_FunctionField`). That totally undermines the category framework. It must be possible for an object to be a function field even without inheriting from `sage.rings.function_field.function_field.FunctionField`.\n\n The default implementation of `F in FunctionFields()` relies on the category of F: The containment test returns True if and only if `F.category()` is a sub-category of `FunctionFields()`. That should be much better, from a mathematical point of view, than testing class inheritance!\n\n* You should add a test of the form `TestSuite(F).run()`, where F is a function field. The test suite is formed by some generic tests defined in the category framework and includes many sanity tests (such as pickling for the field and its elements, associativity, commtativity, ...). If you can think of specific tests for function fields, then you should add methods named `_test_...` as parent or element methods of `sage.categories.function_fields.FunctionFields`. Such methods will be automatically called when running `TestSuite(F).run()`.\n\n* You should also add a test of the form `loads(dumps(F)) is F`, in order to test uniqueness of parent structures; if I recall correctly, the test suite from the category would only test `loads(dumps(F))==F`.\n\n* It should not be needed to have a function `is_FunctionField` (that just tests class inheritance) - `F in FunctionFields()` is a better test, IMHO. If you do want to preserve `is_FunctionField` then please do not simply put it in the global name space. At least, it should be deprecated, similar to `is_Ring` being deprecated. There is a function decorator to do so.\n\n* In the doc test for the `_element_constructor_` method, you explicitly call the method. I think it should better be an indirect test (after all, the documentation is supposed to show how the user is supposed to work with stuff). Hence, not `L._element_constructor_(L.polynomial_ring().gen())` but `L(L.polynomial_ring().gen())   #indirect doctest`.\n\n* I already mentioned, since `FunctionField` is derived from `sage.rings.ring.Field`, that `Field.__init__(...)` should be called. It could be that this only works when #9138 is used. Just calling `ParentWithGens.__init__` may be insufficient.\n\n* There are several methods, such as polynomial_ring or vector_space, that use a hand-made cache. Please use the `@`cached_method decorator instead! That has several reasons. \n  1. It is more easy. You don't need to manually update attributes.\n  2. With #11115, the `@`cached_method decorator is rewritten in Cython and provides a faster cache than anything you could possibly create with Python.\n\n* Is there a reason why you have a method `base_field` that simply returns the function field itself? From the behaviour of the  `base_ring` method of polynomial rings, I would rather expect that `FunctionField(QQ,['t']).base_field()` returns the rational field.",
    "created_at": "2011-08-28T08:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83762",
    "user": "https://github.com/simon-king-jena"
}
```

Here are some comments on [attachment:trac_9054-all-parts.patch]:

* Please remove the `__contains__` method from the category `FunctionFields`. Containment in categories should rely on the default implementation, unless there is a compelling reason to do otherwise.

 Even worse, your containment test is ultimately based on testing class inheritance (namely in the function `is_FunctionField`). That totally undermines the category framework. It must be possible for an object to be a function field even without inheriting from `sage.rings.function_field.function_field.FunctionField`.

 The default implementation of `F in FunctionFields()` relies on the category of F: The containment test returns True if and only if `F.category()` is a sub-category of `FunctionFields()`. That should be much better, from a mathematical point of view, than testing class inheritance!

* You should add a test of the form `TestSuite(F).run()`, where F is a function field. The test suite is formed by some generic tests defined in the category framework and includes many sanity tests (such as pickling for the field and its elements, associativity, commtativity, ...). If you can think of specific tests for function fields, then you should add methods named `_test_...` as parent or element methods of `sage.categories.function_fields.FunctionFields`. Such methods will be automatically called when running `TestSuite(F).run()`.

* You should also add a test of the form `loads(dumps(F)) is F`, in order to test uniqueness of parent structures; if I recall correctly, the test suite from the category would only test `loads(dumps(F))==F`.

* It should not be needed to have a function `is_FunctionField` (that just tests class inheritance) - `F in FunctionFields()` is a better test, IMHO. If you do want to preserve `is_FunctionField` then please do not simply put it in the global name space. At least, it should be deprecated, similar to `is_Ring` being deprecated. There is a function decorator to do so.

* In the doc test for the `_element_constructor_` method, you explicitly call the method. I think it should better be an indirect test (after all, the documentation is supposed to show how the user is supposed to work with stuff). Hence, not `L._element_constructor_(L.polynomial_ring().gen())` but `L(L.polynomial_ring().gen())   #indirect doctest`.

* I already mentioned, since `FunctionField` is derived from `sage.rings.ring.Field`, that `Field.__init__(...)` should be called. It could be that this only works when #9138 is used. Just calling `ParentWithGens.__init__` may be insufficient.

* There are several methods, such as polynomial_ring or vector_space, that use a hand-made cache. Please use the `@`cached_method decorator instead! That has several reasons. 
  1. It is more easy. You don't need to manually update attributes.
  2. With #11115, the `@`cached_method decorator is rewritten in Cython and provides a faster cache than anything you could possibly create with Python.

* Is there a reason why you have a method `base_field` that simply returns the function field itself? From the behaviour of the  `base_ring` method of polynomial rings, I would rather expect that `FunctionField(QQ,['t']).base_field()` returns the rational field.



---

archive/issue_comments_083763.json:
```json
{
    "body": "Replying to [comment:37 SimonKing]:\n> \n> * I already mentioned, \n\n\n... namely on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c62fa3dae0a2ca82),\n\n> that `Field.__init__(...)` should be called. It could be that this only works when #9138 is used. Just calling `ParentWithGens.__init__` may be insufficient.",
    "created_at": "2011-08-28T16:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83763",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:37 SimonKing]:
> 
> * I already mentioned, 


... namely on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c62fa3dae0a2ca82),

> that `Field.__init__(...)` should be called. It could be that this only works when #9138 is used. Just calling `ParentWithGens.__init__` may be insufficient.



---

archive/issue_comments_083764.json:
```json
{
    "body": "Replying to [comment:37 SimonKing]:\n> Here are some comments on [attachment:trac_9054-all-parts.patch]:\n> \n> * Please remove the `__contains__` method from the category `FunctionFields`. Containment in categories should rely on the default implementation, unless there is a compelling reason to do otherwise.\n> \n>  Even worse, your containment test is ultimately based on testing class inheritance (namely in the function `is_FunctionField`). That totally undermines the category framework. It must be possible for an object to be a function field even without inheriting from `sage.rings.function_field.function_field.FunctionField`.\n> \n>  The default implementation of `F in FunctionFields()` relies on the category of F: The containment test returns True if and only if `F.category()` is a sub-category of `FunctionFields()`. That should be much better, from a mathematical point of view, than testing class inheritance!\n> \n\n\nTechnically this is true.   But this category framework instead of inheritance -- really two very different approaches to design -- leads directly to slow code in some cases in practice, which is *really* annoying, IMHO.   For example, see #11657, where one of the root causes of slowness was code in is_Ring that was added to support this category approach, and which slowed everything down.   Fortunately for me I have psage where I can write streamlined code without having to be weighed down, and for generic Sage working well and being extensible is more important, so of course I agree with you in this case.  \n\n>  * You should add a test of the form `TestSuite(F).run()`, where F is a function field. The test suite is formed by some generic tests defined in the category framework and includes many sanity tests (such as pickling for the field and its elements, associativity, commtativity, ...). If you can think of specific tests for function fields, then you should add methods named `_test_...` as parent or element methods of `sage.categories.function_fields.FunctionFields`. Such methods will be automatically called when running `TestSuite(F).run()`.\n \n> \n>  * You should also add a test of the form `loads(dumps(F)) is F`, in order to test uniqueness of parent structures; if I recall correctly, the test suite from the category would only test `loads(dumps(F))==F`.\n \n> \n\nThis is also testing that pickling works at all.  This code is used by the pickle jar to create pickles for testing later. \n\n>  * It should not be needed to have a function `is_FunctionField` (that just tests class inheritance) - `F in FunctionFields()` is a better test, IMHO. If you do want to preserve `is_FunctionField` then please do not simply put it in the global name space. At least, it should be deprecated, similar to `is_Ring` being deprecated. There is a function decorator to do so.\n \n> \n\nis_Ring is only deprecated when used from the top level (i.e., the Sage prompt).   However, there is still a is_Ring function, which can be used in library code, and is not deprecated for this purpose.   And the is_Ring function does test for category stuff. \n\n>  * In the doc test for the `_element_constructor_` method, you explicitly call the method. I think i\n \nt should better be an indirect test (after all, the documentation is supposed to show how the user is supposed to work with stuff). Hence, not `L._element_constructor_(L.polynomial_ring().gen())` but `L(L.polynomial_ring().gen())   #indirect doctest`.\n> \n\n\nI disagree.   I view \"#indirect test\" for situations where you can't think of a clean way of directly calling the function.  If there is such a way, use it!  That way, at least you know for sure it is really being tested.  Suggesting to get rid of that makes no sense to me.  What if `L(L.polynomial_ring().gen())` doesn't call `_element_constructor_` at all?   Also, one can also just have two tests -- one that is indirect and one that isn't.\n\n>  * I already mentioned, since `FunctionField` is derived from `sage.rings.ring.Field`, that `Field.__init__(...)` should be called. It could be that this only works when #9138 is used. Just calling `ParentWithGens.__init__` may be insufficient.\n \n> \n>  * There are several methods, such as polynomial_ring or vector_space, that use a hand-made cache. Please use the `@`cached_method decorator instead! That has several reasons. \n>    1. It is more easy. You don't need to manually update attributes.\n>    2. With #11115, the `@`cached_method decorator is rewritten in Cython and provides a faster cache than anything you could possibly create with Python.\n\n\n+1.  Note that when the very first version of the function field code was written (by me) `@`cached_method was disturbingly slow.  I really, really appreciate the fast Cython rewrite. \n\n>  * Is there a reason why you have a method `base_field` that simply returns the function field itself? From the behaviour of the  `base_ring` method of polynomial rings, I would rather expect that `FunctionField(QQ,['t']).base_field()` returns the rational field.\n \n> \n\nNo.  The base field of a function field is a rational function field in 1 variable.  The base field of that rational function field is then a field such as QQ.   Most function fields aren't rational, e.g., they are finite extensions K/QQ(t), or even relative extensions L/K.  In the first case, the base field is QQ(t) and in the second it is K.  \nIf Simon was confused by this, it should be documented better.   \n\n\n\n>",
    "created_at": "2011-08-28T16:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83764",
    "user": "https://github.com/williamstein"
}
```

Replying to [comment:37 SimonKing]:
> Here are some comments on [attachment:trac_9054-all-parts.patch]:
> 
> * Please remove the `__contains__` method from the category `FunctionFields`. Containment in categories should rely on the default implementation, unless there is a compelling reason to do otherwise.
> 
>  Even worse, your containment test is ultimately based on testing class inheritance (namely in the function `is_FunctionField`). That totally undermines the category framework. It must be possible for an object to be a function field even without inheriting from `sage.rings.function_field.function_field.FunctionField`.
> 
>  The default implementation of `F in FunctionFields()` relies on the category of F: The containment test returns True if and only if `F.category()` is a sub-category of `FunctionFields()`. That should be much better, from a mathematical point of view, than testing class inheritance!
> 


Technically this is true.   But this category framework instead of inheritance -- really two very different approaches to design -- leads directly to slow code in some cases in practice, which is *really* annoying, IMHO.   For example, see #11657, where one of the root causes of slowness was code in is_Ring that was added to support this category approach, and which slowed everything down.   Fortunately for me I have psage where I can write streamlined code without having to be weighed down, and for generic Sage working well and being extensible is more important, so of course I agree with you in this case.  

>  * You should add a test of the form `TestSuite(F).run()`, where F is a function field. The test suite is formed by some generic tests defined in the category framework and includes many sanity tests (such as pickling for the field and its elements, associativity, commtativity, ...). If you can think of specific tests for function fields, then you should add methods named `_test_...` as parent or element methods of `sage.categories.function_fields.FunctionFields`. Such methods will be automatically called when running `TestSuite(F).run()`.
 
> 
>  * You should also add a test of the form `loads(dumps(F)) is F`, in order to test uniqueness of parent structures; if I recall correctly, the test suite from the category would only test `loads(dumps(F))==F`.
 
> 

This is also testing that pickling works at all.  This code is used by the pickle jar to create pickles for testing later. 

>  * It should not be needed to have a function `is_FunctionField` (that just tests class inheritance) - `F in FunctionFields()` is a better test, IMHO. If you do want to preserve `is_FunctionField` then please do not simply put it in the global name space. At least, it should be deprecated, similar to `is_Ring` being deprecated. There is a function decorator to do so.
 
> 

is_Ring is only deprecated when used from the top level (i.e., the Sage prompt).   However, there is still a is_Ring function, which can be used in library code, and is not deprecated for this purpose.   And the is_Ring function does test for category stuff. 

>  * In the doc test for the `_element_constructor_` method, you explicitly call the method. I think i
 
t should better be an indirect test (after all, the documentation is supposed to show how the user is supposed to work with stuff). Hence, not `L._element_constructor_(L.polynomial_ring().gen())` but `L(L.polynomial_ring().gen())   #indirect doctest`.
> 


I disagree.   I view "#indirect test" for situations where you can't think of a clean way of directly calling the function.  If there is such a way, use it!  That way, at least you know for sure it is really being tested.  Suggesting to get rid of that makes no sense to me.  What if `L(L.polynomial_ring().gen())` doesn't call `_element_constructor_` at all?   Also, one can also just have two tests -- one that is indirect and one that isn't.

>  * I already mentioned, since `FunctionField` is derived from `sage.rings.ring.Field`, that `Field.__init__(...)` should be called. It could be that this only works when #9138 is used. Just calling `ParentWithGens.__init__` may be insufficient.
 
> 
>  * There are several methods, such as polynomial_ring or vector_space, that use a hand-made cache. Please use the `@`cached_method decorator instead! That has several reasons. 
>    1. It is more easy. You don't need to manually update attributes.
>    2. With #11115, the `@`cached_method decorator is rewritten in Cython and provides a faster cache than anything you could possibly create with Python.


+1.  Note that when the very first version of the function field code was written (by me) `@`cached_method was disturbingly slow.  I really, really appreciate the fast Cython rewrite. 

>  * Is there a reason why you have a method `base_field` that simply returns the function field itself? From the behaviour of the  `base_ring` method of polynomial rings, I would rather expect that `FunctionField(QQ,['t']).base_field()` returns the rational field.
 
> 

No.  The base field of a function field is a rational function field in 1 variable.  The base field of that rational function field is then a field such as QQ.   Most function fields aren't rational, e.g., they are finite extensions K/QQ(t), or even relative extensions L/K.  In the first case, the base field is QQ(t) and in the second it is K.  
If Simon was confused by this, it should be documented better.   



>



---

archive/issue_comments_083765.json:
```json
{
    "body": "Replying to [comment:39 was]:\n> Replying to [comment:37 SimonKing]:\n> > Here are some comments on [attachment:trac_9054-all-parts.patch]:\n> > \n> > * Please remove the `__contains__` method from the category `FunctionFields`. Containment in categories should rely on the default implementation, unless there is a compelling reason to do otherwise.\n\n> ...\n> \n> Technically this is true.   But this category framework instead of inheritance -- really two very different approaches to design -- leads directly to slow code in some cases in practice, which is *really* annoying, IMHO. \n\n\nA while ago, I had worked on a ticket #10667 about category containment. One purpose was to get a speedup. The trick was (again) to use Cython. For some reason, the work on that ticket has stalled. Perhaps it would be worth while to resume it.\n\nGenerally, I think it is better to improve the category framework, rather than to work around it.\n\n>  For example, see #11657, where one of the root causes of slowness was code in is_Ring that was added to support this category approach, and which slowed everything down.\n\n\nThen why is the existing `is_Ring` not rewritten along the lines of what you do in #11657?\n\n> is_Ring is only deprecated when used from the top level (i.e., the Sage prompt).\n\n\nYes, this is what I meant. I did not mean \"deprecated\" in the sense of \"will soon be removed\", but in the sense of \"please don't try this at home\".\n\n>  And the is_Ring function does test for category stuff. \n\n\nActually I have not been aware that category stuff is tested in `is_Ring`. I was thinking about various other `is_...` methods that really do nothing more than isinstance.\n \n> >  * Is there a reason why you have a method `base_field` that simply returns the function field itself? From the behaviour of the  `base_ring` method of polynomial rings, I would rather expect that `FunctionField(QQ,['t']).base_field()` returns the rational field.\n \n> > \n> \n> No.  The base field of a function field is a rational function field in 1 variable. \n\n\nOuch, so I was mistaken.\n\n> The base field of that rational function field is then a field such as QQ.   Most function fields aren't rational, e.g., they are finite extensions K/QQ(t), or even relative extensions L/K.  In the first case, the base field is QQ(t) and in the second it is K.  \n> If Simon was confused by this, it should be documented better.   \n\n\nNot needed. What I stated was based on reading the patch \"diagonally\". I only noticed one of the two base_field methods.",
    "created_at": "2011-08-28T17:42:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83765",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:39 was]:
> Replying to [comment:37 SimonKing]:
> > Here are some comments on [attachment:trac_9054-all-parts.patch]:
> > 
> > * Please remove the `__contains__` method from the category `FunctionFields`. Containment in categories should rely on the default implementation, unless there is a compelling reason to do otherwise.

> ...
> 
> Technically this is true.   But this category framework instead of inheritance -- really two very different approaches to design -- leads directly to slow code in some cases in practice, which is *really* annoying, IMHO. 


A while ago, I had worked on a ticket #10667 about category containment. One purpose was to get a speedup. The trick was (again) to use Cython. For some reason, the work on that ticket has stalled. Perhaps it would be worth while to resume it.

Generally, I think it is better to improve the category framework, rather than to work around it.

>  For example, see #11657, where one of the root causes of slowness was code in is_Ring that was added to support this category approach, and which slowed everything down.


Then why is the existing `is_Ring` not rewritten along the lines of what you do in #11657?

> is_Ring is only deprecated when used from the top level (i.e., the Sage prompt).


Yes, this is what I meant. I did not mean "deprecated" in the sense of "will soon be removed", but in the sense of "please don't try this at home".

>  And the is_Ring function does test for category stuff. 


Actually I have not been aware that category stuff is tested in `is_Ring`. I was thinking about various other `is_...` methods that really do nothing more than isinstance.
 
> >  * Is there a reason why you have a method `base_field` that simply returns the function field itself? From the behaviour of the  `base_ring` method of polynomial rings, I would rather expect that `FunctionField(QQ,['t']).base_field()` returns the rational field.
 
> > 
> 
> No.  The base field of a function field is a rational function field in 1 variable. 


Ouch, so I was mistaken.

> The base field of that rational function field is then a field such as QQ.   Most function fields aren't rational, e.g., they are finite extensions K/QQ(t), or even relative extensions L/K.  In the first case, the base field is QQ(t) and in the second it is K.  
> If Simon was confused by this, it should be documented better.   


Not needed. What I stated was based on reading the patch "diagonally". I only noticed one of the two base_field methods.



---

archive/issue_comments_083766.json:
```json
{
    "body": "Replying to [comment:40 SimonKing]:\n> A while ago, I had worked on a ticket #10667 about category containment. One purpose was to get a speedup. The trick was (again) to use Cython. For some reason, the work on that ticket has stalled. Perhaps it would be worth while to resume it.\n> \n\n\n+1\n\n> Generally, I think it is better to improve the category framework, rather than to work around it.\n> \n> >  For example, see #11657, where one of the root causes of slowness was code in is_Ring that was added to support this category approach, and which slowed everything down.\n\n> \n> Then why is the existing `is_Ring` not rewritten along the lines of what you do in #11657?\n\n\nWhat I did there slows down `is_Ring` testing if the object in question does not derive from Ring. \n\n> > is_Ring is only deprecated when used from the top level (i.e., the Sage prompt).\n\n> \n> Yes, this is what I meant. I did not mean \"deprecated\" in the sense of \"will soon be removed\", but in the sense of \"please don't try this at home\".\n> \n\n\nIf you are developing on the Sage library, I think it is OK to use. \n\n> >  And the is_Ring function does test for category stuff. \n\n> \n> Actually I have not been aware that category stuff is tested in `is_Ring`. I was thinking about various other `is_...` methods that really do nothing more than isinstance.\n>  \n\n\nYes, take a look at the code.  I too was surprised by this!\n\n -- William",
    "created_at": "2011-08-28T17:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83766",
    "user": "https://github.com/williamstein"
}
```

Replying to [comment:40 SimonKing]:
> A while ago, I had worked on a ticket #10667 about category containment. One purpose was to get a speedup. The trick was (again) to use Cython. For some reason, the work on that ticket has stalled. Perhaps it would be worth while to resume it.
> 


+1

> Generally, I think it is better to improve the category framework, rather than to work around it.
> 
> >  For example, see #11657, where one of the root causes of slowness was code in is_Ring that was added to support this category approach, and which slowed everything down.

> 
> Then why is the existing `is_Ring` not rewritten along the lines of what you do in #11657?


What I did there slows down `is_Ring` testing if the object in question does not derive from Ring. 

> > is_Ring is only deprecated when used from the top level (i.e., the Sage prompt).

> 
> Yes, this is what I meant. I did not mean "deprecated" in the sense of "will soon be removed", but in the sense of "please don't try this at home".
> 


If you are developing on the Sage library, I think it is OK to use. 

> >  And the is_Ring function does test for category stuff. 

> 
> Actually I have not been aware that category stuff is tested in `is_Ring`. I was thinking about various other `is_...` methods that really do nothing more than isinstance.
>  


Yes, take a look at the code.  I too was surprised by this!

 -- William



---

archive/issue_comments_083767.json:
```json
{
    "body": "I changed the description so that it's clear which code to look at. I will read the rest of all the remarks when I'm back from lunch.",
    "created_at": "2011-08-28T19:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83767",
    "user": "https://github.com/koffie"
}
```

I changed the description so that it's clear which code to look at. I will read the rest of all the remarks when I'm back from lunch.



---

archive/issue_comments_083768.json:
```json
{
    "body": "Dear Simon,\n\nThanks for the help and suggestions. But sadly it did not help (altough I find #9138 a very cool ticket it's good to make a lot of rings finally more consistent with the current model of doing things with the category framework).\n\nAfter some fiddeling around I managed to reduce the error to something in FunctionFieldElement_rational initialization code (hence probably not something with the categorie an coercion framework).\n\n```\nsage: K = QQ['x'].fraction_field(); x = K.gen(0)\nsage: sage.rings.function_field.function_field_element.FunctionFieldElement_rational(K, x)\nx\nsage: l=sage.rings.function_field.function_field_element.FunctionFieldElement_rational(K, x)\nsage: dumps(l)\nPicklingError                             Traceback (most recent call last)\n...\nPicklingError: Can't pickle <type 'dictproxy'>: attribute lookup __builtin__.dictproxy failed\nsage: l.__getstate__()\n(Fraction Field of Univariate Polynomial Ring in x over Rational Field, <dictproxy object at 0x10ddf9948>)\n```",
    "created_at": "2011-08-29T02:44:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83768",
    "user": "https://github.com/koffie"
}
```

Dear Simon,

Thanks for the help and suggestions. But sadly it did not help (altough I find #9138 a very cool ticket it's good to make a lot of rings finally more consistent with the current model of doing things with the category framework).

After some fiddeling around I managed to reduce the error to something in FunctionFieldElement_rational initialization code (hence probably not something with the categorie an coercion framework).

```
sage: K = QQ['x'].fraction_field(); x = K.gen(0)
sage: sage.rings.function_field.function_field_element.FunctionFieldElement_rational(K, x)
x
sage: l=sage.rings.function_field.function_field_element.FunctionFieldElement_rational(K, x)
sage: dumps(l)
PicklingError                             Traceback (most recent call last)
...
PicklingError: Can't pickle <type 'dictproxy'>: attribute lookup __builtin__.dictproxy failed
sage: l.__getstate__()
(Fraction Field of Univariate Polynomial Ring in x over Rational Field, <dictproxy object at 0x10ddf9948>)
```



---

archive/issue_comments_083769.json:
```json
{
    "body": "It took me a while to find out how to solve the problems with pickling but I finally managed to do so. It was because of cython objects not being pickleable automatically so you have to write your own pickling methods. A more experienced programmer might have found this out way faster then me, but I had a lot of trouble (basically spent this entire afternoon reading about how pickling protocol works so I could fix it. I will now look into the issues you described and get a definite patch up.",
    "created_at": "2011-08-29T06:51:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83769",
    "user": "https://github.com/koffie"
}
```

It took me a while to find out how to solve the problems with pickling but I finally managed to do so. It was because of cython objects not being pickleable automatically so you have to write your own pickling methods. A more experienced programmer might have found this out way faster then me, but I had a lot of trouble (basically spent this entire afternoon reading about how pickling protocol works so I could fix it. I will now look into the issues you described and get a definite patch up.



---

archive/issue_comments_083770.json:
```json
{
    "body": "Just for your information: I resumed work on #10667. \n\nTesting whether QQ is a ring works faster with the methods from #11115 and #10667 than with using the current `is_Ring`:\n\n```\nsage: C = CommutativeRings().objects()\nsage: QQ in C\nTrue\nsage: %timeit QQ in C\n625 loops, best of 3: 3.88 \u00b5s per loop\n```\nversus\n\n```\nsage: from sage.rings.ring import is_Ring\nsage: %timeit is_Ring(QQ)\n625 loops, best of 3: 5.06 \u00b5s per loop\n```\n\nOf course, just testing the class is a lot faster:\n\n```\nsage: from sage.rings.ring import Ring\nsage: %timeit isinstance(QQ,Ring)\n625 loops, best of 3: 666 ns per loop\n```",
    "created_at": "2011-08-29T09:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83770",
    "user": "https://github.com/simon-king-jena"
}
```

Just for your information: I resumed work on #10667. 

Testing whether QQ is a ring works faster with the methods from #11115 and #10667 than with using the current `is_Ring`:

```
sage: C = CommutativeRings().objects()
sage: QQ in C
True
sage: %timeit QQ in C
625 loops, best of 3: 3.88 µs per loop
```
versus

```
sage: from sage.rings.ring import is_Ring
sage: %timeit is_Ring(QQ)
625 loops, best of 3: 5.06 µs per loop
```

Of course, just testing the class is a lot faster:

```
sage: from sage.rings.ring import Ring
sage: %timeit isinstance(QQ,Ring)
625 loops, best of 3: 666 ns per loop
```



---

archive/issue_comments_083771.json:
```json
{
    "body": "I really think that `is_Ring` should be *globally* improved. For example, it already helps to define\n\n```\ndef is_Ring(x):\n    \"\"\"\n    Return True if x is a ring.\n\n    EXAMPLES::\n\n        sage: from sage.rings.ring import is_Ring\n        sage: is_Ring(ZZ)\n        True\n    \"\"\"\n    if isinstance(x, Ring):\n        return True\n    from sage.categories.rings import Rings\n    return x in Rings()\n```\nhence, only do the import when needed.\n\nThe timings become\n\n```\nsage: from sage.rings.ring import is_Ring\nsage: P.<x,y,z> = QQ[]\nsage: is_Ring(P)\nTrue\nsage: %timeit is_Ring(P)\n625 loops, best of 3: 243 ns per loop\nsage: MS = MatrixSpace(QQ,2)\nsage: is_Ring(MS)\nTrue\nsage: %timeit is_Ring(MS)\n625 loops, best of 3: 21.5 \u00b5s per loop\n```\nversus\n\n```\nsage: from sage.rings.ring import is_Ring\nsage: sage: P.<x,y,z> = QQ[]\nsage: is_Ring(P)\nTrue\nsage: %timeit is_Ring(P)\n625 loops, best of 3: 4.93 \u00b5s per loop\nsage: MS = MatrixSpace(QQ,2)\nsage: sage: is_Ring(MS)\nTrue\nsage: %timeit is_Ring(MS)\n625 loops, best of 3: 26.4 \u00b5s per loop\n```\n\nBut I think I'll move it to #10667.",
    "created_at": "2011-08-29T11:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83771",
    "user": "https://github.com/simon-king-jena"
}
```

I really think that `is_Ring` should be *globally* improved. For example, it already helps to define

```
def is_Ring(x):
    """
    Return True if x is a ring.

    EXAMPLES::

        sage: from sage.rings.ring import is_Ring
        sage: is_Ring(ZZ)
        True
    """
    if isinstance(x, Ring):
        return True
    from sage.categories.rings import Rings
    return x in Rings()
```
hence, only do the import when needed.

The timings become

```
sage: from sage.rings.ring import is_Ring
sage: P.<x,y,z> = QQ[]
sage: is_Ring(P)
True
sage: %timeit is_Ring(P)
625 loops, best of 3: 243 ns per loop
sage: MS = MatrixSpace(QQ,2)
sage: is_Ring(MS)
True
sage: %timeit is_Ring(MS)
625 loops, best of 3: 21.5 µs per loop
```
versus

```
sage: from sage.rings.ring import is_Ring
sage: sage: P.<x,y,z> = QQ[]
sage: is_Ring(P)
True
sage: %timeit is_Ring(P)
625 loops, best of 3: 4.93 µs per loop
sage: MS = MatrixSpace(QQ,2)
sage: sage: is_Ring(MS)
True
sage: %timeit is_Ring(MS)
625 loops, best of 3: 26.4 µs per loop
```

But I think I'll move it to #10667.



---

archive/issue_comments_083772.json:
```json
{
    "body": "Time for a little advertisement: I obtain a much improved performance with #10667 (introducing the class of objects and morphisms of a category, written in Cython). Perhaps it is useful for you?\n\n**__Testing commutative rings__**\n\nThe function `is_CommutativeRing` does nothing but testing the class. But it is a Python function. Let us compare its speed with the speed of a Cython container, testing category containment.\n\n`is_CommutativeRing`:\n\n```\nsage: from sage.rings.commutative_ring import is_CommutativeRing\nsage: is_CommutativeRing??\n...\nSource:\ndef is_CommutativeRing(R):\n    return isinstance(R, CommutativeRing)\nsage: is_CommutativeRing(QQ)\nTrue\nsage: s = SymmetricGroup(4)\nsage: is_CommutativeRing(s)\nFalse\nsage: %timeit is_CommutativeRing(QQ)\n625 loops, best of 3: 1.09 \u00b5s per loop\nsage: %timeit is_CommutativeRing(s)\n625 loops, best of 3: 3.51 \u00b5s per loop\n```\n\nCython container:\n\n```\nsage: O = CommutativeRings().objects()\nsage: QQ in O\nTrue\nsage: s in O\nFalse\nsage: %timeit QQ in O\n625 loops, best of 3: 1.5 \u00b5s per loop\nsage: %timeit s in O\n625 loops, best of 3: 1.46 \u00b5s per loop\n```\nHence, when applied to a symmetric group, the container performs a category containment test (with negative result, of course) that is *faster* than a Python class check!\n\n**__Testing rings__**\n\nAs you have observed, the current `is_Ring` function is suboptimal. I rewrote it in #10667.\n\nWithout #10667 (but with #11115 for a fast cache):\n\n```\nsage: from sage.rings.ring import is_Ring\nsage: MS = MatrixSpace(QQ,2)\nsage: %timeit is_Ring(QQ)\n625 loops, best of 3: 5.1 \u00b5s per loop\nsage: is_Ring(MS)\nTrue\nsage: %timeit is_Ring(MS)\n625 loops, best of 3: 17.3 \u00b5s per loop\nsage: C = Rings()\nsage: %timeit QQ in C\n625 loops, best of 3: 4.18 \u00b5s per loop\nsage: %timeit MS in C\n625 loops, best of 3: 4.31 \u00b5s per loop\n```\nWith #10667 in addition:\n\n```\nsage: from sage.rings.ring import is_Ring\nsage: MS = MatrixSpace(QQ,2)\nsage: %timeit is_Ring(QQ)\n625 loops, best of 3: 259 ns per loop\nsage: %timeit is_Ring(MS)\n625 loops, best of 3: 17.5 \u00b5s per loop\nsage: C = Rings().objects()\nsage: %timeit QQ in C\n625 loops, best of 3: 1.49 \u00b5s per loop\nsage: %timeit MS in C\n625 loops, best of 3: 1.57 \u00b5s per loop\n```",
    "created_at": "2011-08-30T10:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83772",
    "user": "https://github.com/simon-king-jena"
}
```

Time for a little advertisement: I obtain a much improved performance with #10667 (introducing the class of objects and morphisms of a category, written in Cython). Perhaps it is useful for you?

**__Testing commutative rings__**

The function `is_CommutativeRing` does nothing but testing the class. But it is a Python function. Let us compare its speed with the speed of a Cython container, testing category containment.

`is_CommutativeRing`:

```
sage: from sage.rings.commutative_ring import is_CommutativeRing
sage: is_CommutativeRing??
...
Source:
def is_CommutativeRing(R):
    return isinstance(R, CommutativeRing)
sage: is_CommutativeRing(QQ)
True
sage: s = SymmetricGroup(4)
sage: is_CommutativeRing(s)
False
sage: %timeit is_CommutativeRing(QQ)
625 loops, best of 3: 1.09 µs per loop
sage: %timeit is_CommutativeRing(s)
625 loops, best of 3: 3.51 µs per loop
```

Cython container:

```
sage: O = CommutativeRings().objects()
sage: QQ in O
True
sage: s in O
False
sage: %timeit QQ in O
625 loops, best of 3: 1.5 µs per loop
sage: %timeit s in O
625 loops, best of 3: 1.46 µs per loop
```
Hence, when applied to a symmetric group, the container performs a category containment test (with negative result, of course) that is *faster* than a Python class check!

**__Testing rings__**

As you have observed, the current `is_Ring` function is suboptimal. I rewrote it in #10667.

Without #10667 (but with #11115 for a fast cache):

```
sage: from sage.rings.ring import is_Ring
sage: MS = MatrixSpace(QQ,2)
sage: %timeit is_Ring(QQ)
625 loops, best of 3: 5.1 µs per loop
sage: is_Ring(MS)
True
sage: %timeit is_Ring(MS)
625 loops, best of 3: 17.3 µs per loop
sage: C = Rings()
sage: %timeit QQ in C
625 loops, best of 3: 4.18 µs per loop
sage: %timeit MS in C
625 loops, best of 3: 4.31 µs per loop
```
With #10667 in addition:

```
sage: from sage.rings.ring import is_Ring
sage: MS = MatrixSpace(QQ,2)
sage: %timeit is_Ring(QQ)
625 loops, best of 3: 259 ns per loop
sage: %timeit is_Ring(MS)
625 loops, best of 3: 17.5 µs per loop
sage: C = Rings().objects()
sage: %timeit QQ in C
625 loops, best of 3: 1.49 µs per loop
sage: %timeit MS in C
625 loops, best of 3: 1.57 µs per loop
```



---

archive/issue_comments_083773.json:
```json
{
    "body": "Ok I'm done with my reviewing of the original work. I guess a review patch of 39.8 KB deserves a review of its own :P",
    "created_at": "2011-09-01T00:59:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83773",
    "user": "https://github.com/koffie"
}
```

Ok I'm done with my reviewing of the original work. I guess a review patch of 39.8 KB deserves a review of its own :P



---

archive/issue_comments_083774.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-09-01T00:59:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83774",
    "user": "https://github.com/koffie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083775.json:
```json
{
    "body": "Note that this patch needs the patch at http://trac.sagemath.org/sage_trac/ticket/11751 to work, but altough the patch at that ticket makes all the doctest for function fields pass, it makes a lot of other doctests fail :(",
    "created_at": "2011-09-01T02:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83775",
    "user": "https://github.com/koffie"
}
```

Note that this patch needs the patch at http://trac.sagemath.org/sage_trac/ticket/11751 to work, but altough the patch at that ticket makes all the doctest for function fields pass, it makes a lot of other doctests fail :(



---

archive/issue_comments_083776.json:
```json
{
    "body": "Ok #11751 is ready for review and the code here passes all tests (at least I tested it on sage 4.7.2.alpha2 ) after you apply the tickets at 11751. So this one can finally get merged as soon as it has positive review.",
    "created_at": "2011-09-10T21:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83776",
    "user": "https://github.com/koffie"
}
```

Ok #11751 is ready for review and the code here passes all tests (at least I tested it on sage 4.7.2.alpha2 ) after you apply the tickets at 11751. So this one can finally get merged as soon as it has positive review.



---

archive/issue_comments_083777.json:
```json
{
    "body": "Attachment [trac_9054-review.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-review.patch) by @koffie created at 2011-09-11 09:19:14",
    "created_at": "2011-09-11T09:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83777",
    "user": "https://github.com/koffie"
}
```

Attachment [trac_9054-review.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-review.patch) by @koffie created at 2011-09-11 09:19:14



---

archive/issue_comments_083778.json:
```json
{
    "body": "Attachment [trac_9054_undo_unittest.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_undo_unittest.patch) by @saraedum created at 2011-09-14 15:47:13\n\nrevert changes to misc.unittest introduced by the review patch",
    "created_at": "2011-09-14T15:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83778",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_undo_unittest.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_undo_unittest.patch) by @saraedum created at 2011-09-14 15:47:13

revert changes to misc.unittest introduced by the review patch



---

archive/issue_comments_083779.json:
```json
{
    "body": "Attachment [trac_9054-invert_ideal.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-invert_ideal.patch) by @saraedum created at 2011-09-15 00:54:34\n\nuse category in is_FunctionField()",
    "created_at": "2011-09-15T00:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83779",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054-invert_ideal.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-invert_ideal.patch) by @saraedum created at 2011-09-15 00:54:34

use category in is_FunctionField()



---

archive/issue_comments_083780.json:
```json
{
    "body": "Attachment [trac_9054_cached_method.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_cached_method.patch) by @saraedum created at 2011-09-15 01:04:28\n\nreplace manual caching with cached_method",
    "created_at": "2011-09-15T01:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83780",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_cached_method.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_cached_method.patch) by @saraedum created at 2011-09-15 01:04:28

replace manual caching with cached_method



---

archive/issue_comments_083781.json:
```json
{
    "body": "Attachment [trac_9054_maximal_order_member_check.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_maximal_order_member_check.patch) by @saraedum created at 2011-09-15 01:11:43\n\n_element_constructor_ checks that element is in maximal order",
    "created_at": "2011-09-15T01:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83781",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_maximal_order_member_check.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_maximal_order_member_check.patch) by @saraedum created at 2011-09-15 01:11:43

_element_constructor_ checks that element is in maximal order



---

archive/issue_comments_083782.json:
```json
{
    "body": "added missing calls to superclass constructors",
    "created_at": "2011-09-15T01:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83782",
    "user": "https://github.com/saraedum"
}
```

added missing calls to superclass constructors



---

archive/issue_comments_083783.json:
```json
{
    "body": "Attachment [trac_9054_UniqueFactory.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_UniqueFactory.patch) by @saraedum created at 2011-09-15 01:17:44\n\nuse UniqueFactory instead of cached_method in constructors",
    "created_at": "2011-09-15T01:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83783",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_UniqueFactory.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_UniqueFactory.patch) by @saraedum created at 2011-09-15 01:17:44

use UniqueFactory instead of cached_method in constructors



---

archive/issue_comments_083784.json:
```json
{
    "body": "refactored maps class hieararchy",
    "created_at": "2011-09-15T01:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83784",
    "user": "https://github.com/saraedum"
}
```

refactored maps class hieararchy



---

archive/issue_comments_083785.json:
```json
{
    "body": "Attachment [trac_9054_doctests-3.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_doctests-3.patch) by @saraedum created at 2011-09-15 02:04:50\n\nextended and unified doctests",
    "created_at": "2011-09-15T02:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83785",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_doctests-3.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_doctests-3.patch) by @saraedum created at 2011-09-15 02:04:50

extended and unified doctests



---

archive/issue_comments_083786.json:
```json
{
    "body": "cleanup code and imports",
    "created_at": "2011-09-15T02:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83786",
    "user": "https://github.com/saraedum"
}
```

cleanup code and imports



---

archive/issue_comments_083787.json:
```json
{
    "body": "Attachment [trac_9054_cleanup.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_cleanup.patch) by @saraedum created at 2011-09-15 02:12:19\n\nadded authors and copyright headers",
    "created_at": "2011-09-15T02:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83787",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_cleanup.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_cleanup.patch) by @saraedum created at 2011-09-15 02:12:19

added authors and copyright headers



---

archive/issue_events_022183.json:
```json
{
    "actor": "https://github.com/saraedum",
    "created_at": "2011-09-15T02:18:19Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9054#event-22183"
}
```



---

archive/issue_events_022184.json:
```json
{
    "actor": "https://github.com/saraedum",
    "created_at": "2011-09-15T02:18:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "milestone": "sage-4.7.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9054#event-22184"
}
```



---

archive/issue_comments_083788.json:
```json
{
    "body": "Attachment [trac_9054_authors.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_authors.patch) by @saraedum created at 2011-09-15 02:18:19",
    "created_at": "2011-09-15T02:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83788",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_authors.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_authors.patch) by @saraedum created at 2011-09-15 02:18:19



---

archive/issue_comments_083789.json:
```json
{
    "body": "Apply trac_9054-all-parts.patch, trac_9054_polynomial_base_field.patch, trac_9054_zero.patch, trac_9054_codomain.patch, trac_9054_doctest-2.patch, trac_9054-review.patch, trac_9054_undo_unittest.patch, trac_9054-invert_ideal.patch, trac_9054_isFunctionField.patch, trac_9054_UniqueFactory.patch, trac_9054_cached_method.patch, trac_9054_maximal_order_member_check.patch, trac_9054_call_super_constructors.patch, trac_9054_maps_refactor.patch, trac_9054_doctests-3.patch, trac_9054_cleanup.patch, trac_9054_authors.patch",
    "created_at": "2011-09-15T02:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83789",
    "user": "https://github.com/saraedum"
}
```

Apply trac_9054-all-parts.patch, trac_9054_polynomial_base_field.patch, trac_9054_zero.patch, trac_9054_codomain.patch, trac_9054_doctest-2.patch, trac_9054-review.patch, trac_9054_undo_unittest.patch, trac_9054-invert_ideal.patch, trac_9054_isFunctionField.patch, trac_9054_UniqueFactory.patch, trac_9054_cached_method.patch, trac_9054_maximal_order_member_check.patch, trac_9054_call_super_constructors.patch, trac_9054_maps_refactor.patch, trac_9054_doctests-3.patch, trac_9054_cleanup.patch, trac_9054_authors.patch



---

archive/issue_comments_083790.json:
```json
{
    "body": "(Apparently the patchbot expects these \"Apply\" instructions in a comment and not in the ticket description)\n\nA more detailed description of the patches since `trac_9054-invert_ideal.patch`:\n \n* `trac_9054_isFunctionField.patch` hopefully does what Simon King proposed for `is_FunctionField`\n* `trac_9054_UniqueFactory.patch` replaces the ``@`cached_method` in `constructor.py` with UniqueFactories -- apparently that class is meant for that purpose\n* `trac_9054_cached_method.patch` replaces all manual caching with ``@`cached_method` methods\n* `trac_9054_maximal_order_member_check.patch` fixes a todo about checking that members  passed to an `_element_constructor` are actually in the order\n* `trac_9054_call_super_constructors.patch` is the one I'm not sure about. At two places the super classes were not properly called -- was that by intention? I hope this fixes it.\n* `trac_9054_maps_refactor.patch` slightly changes the base classes of function field morphisms\n* `trac_9054_doctests-3.patch` essentially unifies the naming of variables in the doctests, so function fields are now called K and L, variables x, y, z. Also I added an entry to `/doc/en/reference/index.rst`, is that correct?\n* `trac_9054_cleanup.patch` reorganizes some imports and removes empty lines\n* `trac_9054_authors.patch` adds authors and copyrights to the files. I followed [http://www.sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files](http://www.sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files), hopefully I got it right?\n\nI also reviewed Maarten's changes and they looked good except for the very few things I patched here. Maarten could you review my patches? It looks like a lot of work, but it should be fairly trivial to review.",
    "created_at": "2011-09-15T02:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83790",
    "user": "https://github.com/saraedum"
}
```

(Apparently the patchbot expects these "Apply" instructions in a comment and not in the ticket description)

A more detailed description of the patches since `trac_9054-invert_ideal.patch`:
 
* `trac_9054_isFunctionField.patch` hopefully does what Simon King proposed for `is_FunctionField`
* `trac_9054_UniqueFactory.patch` replaces the ``@`cached_method` in `constructor.py` with UniqueFactories -- apparently that class is meant for that purpose
* `trac_9054_cached_method.patch` replaces all manual caching with ``@`cached_method` methods
* `trac_9054_maximal_order_member_check.patch` fixes a todo about checking that members  passed to an `_element_constructor` are actually in the order
* `trac_9054_call_super_constructors.patch` is the one I'm not sure about. At two places the super classes were not properly called -- was that by intention? I hope this fixes it.
* `trac_9054_maps_refactor.patch` slightly changes the base classes of function field morphisms
* `trac_9054_doctests-3.patch` essentially unifies the naming of variables in the doctests, so function fields are now called K and L, variables x, y, z. Also I added an entry to `/doc/en/reference/index.rst`, is that correct?
* `trac_9054_cleanup.patch` reorganizes some imports and removes empty lines
* `trac_9054_authors.patch` adds authors and copyrights to the files. I followed [http://www.sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files](http://www.sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files), hopefully I got it right?

I also reviewed Maarten's changes and they looked good except for the very few things I patched here. Maarten could you review my patches? It looks like a lot of work, but it should be fairly trivial to review.



---

archive/issue_comments_083791.json:
```json
{
    "body": "Attachment [trac_9054_is_function_field.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_is_function_field.patch) by @saraedum created at 2011-09-19 14:02:42\n\nidentical to trac_9054_isFunctionField.patch but the patch bot does not like upper case in patch files",
    "created_at": "2011-09-19T14:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83791",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_is_function_field.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_is_function_field.patch) by @saraedum created at 2011-09-19 14:02:42

identical to trac_9054_isFunctionField.patch but the patch bot does not like upper case in patch files



---

archive/issue_comments_083792.json:
```json
{
    "body": "Attachment [trac_9054_unique_factory.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_unique_factory.patch) by @saraedum created at 2011-09-19 14:04:11\n\nidentical to trac_9054_UniqueFactory.patch (patchbot does not like uppercase)",
    "created_at": "2011-09-19T14:04:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83792",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_unique_factory.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_unique_factory.patch) by @saraedum created at 2011-09-19 14:04:11

identical to trac_9054_UniqueFactory.patch (patchbot does not like uppercase)



---

archive/issue_comments_083793.json:
```json
{
    "body": "Apply trac_9054-all-parts.patch, trac_9054_polynomial_base_field.patch, trac_9054_zero.patch, trac_9054_codomain.patch, trac_9054_doctest-2.patch, trac_9054-review.patch, trac_9054_undo_unittest.patch, trac_9054-invert_ideal.patch, trac_9054_is_function_field.patch, trac_9054_unique_factory.patch, trac_9054_cached_method.patch, trac_9054_maximal_order_member_check.patch, trac_9054_call_super_constructors.patch, trac_9054_maps_refactor.patch, trac_9054_doctests-3.patch, trac_9054_cleanup.patch, trac_9054_authors.patch",
    "created_at": "2011-09-19T14:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83793",
    "user": "https://github.com/saraedum"
}
```

Apply trac_9054-all-parts.patch, trac_9054_polynomial_base_field.patch, trac_9054_zero.patch, trac_9054_codomain.patch, trac_9054_doctest-2.patch, trac_9054-review.patch, trac_9054_undo_unittest.patch, trac_9054-invert_ideal.patch, trac_9054_is_function_field.patch, trac_9054_unique_factory.patch, trac_9054_cached_method.patch, trac_9054_maximal_order_member_check.patch, trac_9054_call_super_constructors.patch, trac_9054_maps_refactor.patch, trac_9054_doctests-3.patch, trac_9054_cleanup.patch, trac_9054_authors.patch



---

archive/issue_comments_083794.json:
```json
{
    "body": "fixes in the reference manual",
    "created_at": "2011-09-19T15:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83794",
    "user": "https://github.com/saraedum"
}
```

fixes in the reference manual



---

archive/issue_comments_083795.json:
```json
{
    "body": "Attachment [trac_9054_reference.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_reference.patch) by @saraedum created at 2011-09-19 15:29:53",
    "created_at": "2011-09-19T15:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83795",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_reference.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_reference.patch) by @saraedum created at 2011-09-19 15:29:53



---

archive/issue_comments_083796.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-09-20T09:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83796",
    "user": "https://github.com/saraedum"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083797.json:
```json
{
    "body": "[attachment:trac_9054_cleanup.patch] introduced a problem with cyclic imports \u00ad\u2014 I'm working on it.",
    "created_at": "2011-09-20T09:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83797",
    "user": "https://github.com/saraedum"
}
```

[attachment:trac_9054_cleanup.patch] introduced a problem with cyclic imports ­— I'm working on it.



---

archive/issue_comments_083798.json:
```json
{
    "body": "fixes an import problem in factor()",
    "created_at": "2011-09-20T12:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83798",
    "user": "https://github.com/saraedum"
}
```

fixes an import problem in factor()



---

archive/issue_comments_083799.json:
```json
{
    "body": "Attachment [trac_9054_factor.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_factor.patch) by @saraedum created at 2011-09-20 12:32:07\n\nIt turned out not to be a cyclic import problem but just the wrong module that was imported. I'm waiting for the doctests to set this back to needs_review.",
    "created_at": "2011-09-20T12:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83799",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_factor.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_factor.patch) by @saraedum created at 2011-09-20 12:32:07

It turned out not to be a cyclic import problem but just the wrong module that was imported. I'm waiting for the doctests to set this back to needs_review.



---

archive/issue_comments_083800.json:
```json
{
    "body": "orders have no category set",
    "created_at": "2011-09-20T13:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83800",
    "user": "https://github.com/saraedum"
}
```

orders have no category set



---

archive/issue_comments_083801.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-09-20T13:48:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83801",
    "user": "https://github.com/saraedum"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083802.json:
```json
{
    "body": "Attachment [trac_9054_order_category.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_order_category.patch) by @saraedum created at 2011-09-20 13:48:04",
    "created_at": "2011-09-20T13:48:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83802",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_order_category.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_order_category.patch) by @saraedum created at 2011-09-20 13:48:04



---

archive/issue_comments_083803.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-11-05T18:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83803",
    "user": "https://github.com/koffie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083804.json:
```json
{
    "body": "On sage.math using the just released sage-4.7.2 with the following 21! patches applied\n\n```\nmderickx@sage:/scratch/mderickx/sage/devel/sage$ hg qser | nl\n     1\t9138_flat.patch\n     2\ttrac_9054-all-parts.patch\n     3\ttrac_9054_polynomial_base_field.patch\n     4\ttrac_9054_zero.patch\n     5\ttrac_9054_codomain.patch\n     6\ttrac_9054_doctest-2.patch\n     7\ttrac_9054-review.patch\n     8\ttrac_9054_undo_unittest.patch\n     9\ttrac_9054-invert_ideal.patch\n    10\ttrac_9054_is_function_field.patch\n    11\ttrac_9054_unique_factory.patch\n    12\ttrac_9054_cached_method.patch\n    13\ttrac_9054_maximal_order_member_check.patch\n    14\ttrac_9054_call_super_constructors.patch\n    15\ttrac_9054_maps_refactor.patch\n    16\ttrac_9054_doctests-3.patch\n    17\ttrac_9054_cleanup.patch\n    18\ttrac_9054_authors.patch\n    19\ttrac_9054_reference.patch\n    20\ttrac_9054_factor.patch\n    21\ttrac_9054_order_category.patch\n```\n\nI get \n\n```\n\nThe following tests failed:\n\n\tsage -t --long devel/sage-main/sage/rings/function_field/maps.py # 1 doctests failed\n\tsage -t --long devel/sage-main/sage/rings/function_field/function_field.py # 7 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 1102.4 seconds\n```",
    "created_at": "2011-11-05T18:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83804",
    "user": "https://github.com/koffie"
}
```

On sage.math using the just released sage-4.7.2 with the following 21! patches applied

```
mderickx@sage:/scratch/mderickx/sage/devel/sage$ hg qser | nl
     1	9138_flat.patch
     2	trac_9054-all-parts.patch
     3	trac_9054_polynomial_base_field.patch
     4	trac_9054_zero.patch
     5	trac_9054_codomain.patch
     6	trac_9054_doctest-2.patch
     7	trac_9054-review.patch
     8	trac_9054_undo_unittest.patch
     9	trac_9054-invert_ideal.patch
    10	trac_9054_is_function_field.patch
    11	trac_9054_unique_factory.patch
    12	trac_9054_cached_method.patch
    13	trac_9054_maximal_order_member_check.patch
    14	trac_9054_call_super_constructors.patch
    15	trac_9054_maps_refactor.patch
    16	trac_9054_doctests-3.patch
    17	trac_9054_cleanup.patch
    18	trac_9054_authors.patch
    19	trac_9054_reference.patch
    20	trac_9054_factor.patch
    21	trac_9054_order_category.patch
```

I get 

```

The following tests failed:

	sage -t --long devel/sage-main/sage/rings/function_field/maps.py # 1 doctests failed
	sage -t --long devel/sage-main/sage/rings/function_field/function_field.py # 7 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1102.4 seconds
```



---

archive/issue_comments_083805.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-11-05T18:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83805",
    "user": "https://github.com/koffie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083806.json:
```json
{
    "body": "Sorry false alarm. I didn't have all patches applied!",
    "created_at": "2011-11-05T18:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83806",
    "user": "https://github.com/koffie"
}
```

Sorry false alarm. I didn't have all patches applied!



---

archive/issue_comments_083807.json:
```json
{
    "body": "All patches till review.patch combined",
    "created_at": "2011-11-07T13:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83807",
    "user": "https://github.com/koffie"
}
```

All patches till review.patch combined



---

archive/issue_comments_083808.json:
```json
{
    "body": "Attachment [trac_9054-all-parts.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-all-parts.patch) by @koffie created at 2011-11-07 13:37:13\n\nAll julians patches after review.patch combined",
    "created_at": "2011-11-07T13:37:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83808",
    "user": "https://github.com/koffie"
}
```

Attachment [trac_9054-all-parts.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-all-parts.patch) by @koffie created at 2011-11-07 13:37:13

All julians patches after review.patch combined



---

archive/issue_comments_083809.json:
```json
{
    "body": "Attachment [trac_9054-review2.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-review2.patch) by @koffie created at 2011-11-07 13:37:58\n\nFixes last minor errors introduced by julians patches",
    "created_at": "2011-11-07T13:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83809",
    "user": "https://github.com/koffie"
}
```

Attachment [trac_9054-review2.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-review2.patch) by @koffie created at 2011-11-07 13:37:58

Fixes last minor errors introduced by julians patches



---

archive/issue_comments_083810.json:
```json
{
    "body": "It turned out that also when applying all julians patches to sage 4.7.2 with #9138 we get some errors. I fixed this in my minor review2.patch. I also combined some patches so that it becomes easier for someone else to do something with this ticket (i.e. doesnt have to download 20 patches). I'm now reading trough [attachment:trac_9054-julian-combined.patch] if it does logical things.",
    "created_at": "2011-11-07T13:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83810",
    "user": "https://github.com/koffie"
}
```

It turned out that also when applying all julians patches to sage 4.7.2 with #9138 we get some errors. I fixed this in my minor review2.patch. I also combined some patches so that it becomes easier for someone else to do something with this ticket (i.e. doesnt have to download 20 patches). I'm now reading trough [attachment:trac_9054-julian-combined.patch] if it does logical things.



---

archive/issue_comments_083811.json:
```json
{
    "body": "Just a note on #9138: It had already been merged, but was unmerged because of an unacceptable regression in elliptic curve computations. But at #11900, I was able to avoid the regression and even turn it into a speed-up, in some cases. #11900 needs review, and then I guess #9138 would be merged again.",
    "created_at": "2011-11-07T14:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83811",
    "user": "https://github.com/simon-king-jena"
}
```

Just a note on #9138: It had already been merged, but was unmerged because of an unacceptable regression in elliptic curve computations. But at #11900, I was able to avoid the regression and even turn it into a speed-up, in some cases. #11900 needs review, and then I guess #9138 would be merged again.



---

archive/issue_comments_083812.json:
```json
{
    "body": "Ok these are the results from reading trough you patches:\n\nWhy did you make some_elements in function_field.py return only one element? This number should be at least two (and preferable even at least 3) since else a lot of tests in TestSuite(F).run() will be meaningless with just one element because one element is always equal to itself for example!\n\nIf you make vector_space a cached method then why don't you change\n\n```\nself._vector_space = (V, from_V, to_V) \nreturn self._vector_space \n```\nto\n\n```\nreturn (V, from_V, to_V) \n```\nThis code is in two places.\n\nIn function_field_order.py there is a typo in the sentence \"the function field in which this iss an order.\"\n\nWhy did you remove:\n\n```\nif is_Ideal(gens): \n    gens = gens.gens() \n```\nin function_field_order.py. I suspect the code was there to make the (not doctested) use case of:\n\n```\nsage: K.<x> = FunctionField(QQ) \nsage: O=K.maximal_order()\nsage: I=O.ideal(x)\nsage: O.ideal(I)\n```\nsince you should be able to make an ideal with input an ideal.\n\nFor the rest your combination patch looks very nice. Also good that you made the documentation quality so much higher. If you either answer the above questions with the right arguments or if you change them back it seems that we can finally have function fields in sage!",
    "created_at": "2011-11-07T15:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83812",
    "user": "https://github.com/koffie"
}
```

Ok these are the results from reading trough you patches:

Why did you make some_elements in function_field.py return only one element? This number should be at least two (and preferable even at least 3) since else a lot of tests in TestSuite(F).run() will be meaningless with just one element because one element is always equal to itself for example!

If you make vector_space a cached method then why don't you change

```
self._vector_space = (V, from_V, to_V) 
return self._vector_space 
```
to

```
return (V, from_V, to_V) 
```
This code is in two places.

In function_field_order.py there is a typo in the sentence "the function field in which this iss an order."

Why did you remove:

```
if is_Ideal(gens): 
    gens = gens.gens() 
```
in function_field_order.py. I suspect the code was there to make the (not doctested) use case of:

```
sage: K.<x> = FunctionField(QQ) 
sage: O=K.maximal_order()
sage: I=O.ideal(x)
sage: O.ideal(I)
```
since you should be able to make an ideal with input an ideal.

For the rest your combination patch looks very nice. Also good that you made the documentation quality so much higher. If you either answer the above questions with the right arguments or if you change them back it seems that we can finally have function fields in sage!



---

archive/issue_comments_083813.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-11-07T15:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83813",
    "user": "https://github.com/koffie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083814.json:
```json
{
    "body": "Replying to [comment:67 mderickx]:\n> Why did you make some_elements in function_field.py return only one element? This number should be at least two (and preferable even at least 3) since else a lot of tests in TestSuite(F).run() will be meaningless with just one element because one element is always equal to itself for example!\n\n\nI think I had seen that somewhere else only one element was returned and copied that. (at that time I didn't know what some_elements() was good for)\nI'll fix that.\n\n> If you make vector_space a cached method then why don't you change\n> \n> ```\n> self._vector_space = (V, from_V, to_V) \n> return self._vector_space \n> ```\n> to\n> \n> ```\n> return (V, from_V, to_V) \n> ```\n> This code is in two places.\n\nThat's true. Must have missed that.\n\n> In function_field_order.py there is a typo in the sentence \"the function field in which this iss an order.\"\n\nWill be fixed in the next patch.\n\n> Why did you remove:\n> \n> ```\n> if is_Ideal(gens): \n>     gens = gens.gens() \n> ```\n> in function_field_order.py. I suspect the code was there to make the (not doctested) use case of:\n> \n> ```\n> sage: K.<x> = FunctionField(QQ) \n> sage: O=K.maximal_order()\n> sage: I=O.ideal(x)\n> sage: O.ideal(I)\n> ```\n> since you should be able to make an ideal with input an ideal.\n\nGood question. It's part of a doctest patch so I guess it just got in by accident.\n\n> For the rest your combination patch looks very nice. Also good that you made the documentation quality so much higher. If you either answer the above questions with the right arguments or if you change them back it seems that we can finally have function fields in sage!\nOk. I'll prepare a patch to fix these issues. Thanks you took the time and had a look at these patches. :)",
    "created_at": "2011-11-07T16:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83814",
    "user": "https://github.com/saraedum"
}
```

Replying to [comment:67 mderickx]:
> Why did you make some_elements in function_field.py return only one element? This number should be at least two (and preferable even at least 3) since else a lot of tests in TestSuite(F).run() will be meaningless with just one element because one element is always equal to itself for example!


I think I had seen that somewhere else only one element was returned and copied that. (at that time I didn't know what some_elements() was good for)
I'll fix that.

> If you make vector_space a cached method then why don't you change
> 
> ```
> self._vector_space = (V, from_V, to_V) 
> return self._vector_space 
> ```
> to
> 
> ```
> return (V, from_V, to_V) 
> ```
> This code is in two places.

That's true. Must have missed that.

> In function_field_order.py there is a typo in the sentence "the function field in which this iss an order."

Will be fixed in the next patch.

> Why did you remove:
> 
> ```
> if is_Ideal(gens): 
>     gens = gens.gens() 
> ```
> in function_field_order.py. I suspect the code was there to make the (not doctested) use case of:
> 
> ```
> sage: K.<x> = FunctionField(QQ) 
> sage: O=K.maximal_order()
> sage: I=O.ideal(x)
> sage: O.ideal(I)
> ```
> since you should be able to make an ideal with input an ideal.

Good question. It's part of a doctest patch so I guess it just got in by accident.

> For the rest your combination patch looks very nice. Also good that you made the documentation quality so much higher. If you either answer the above questions with the right arguments or if you change them back it seems that we can finally have function fields in sage!
Ok. I'll prepare a patch to fix these issues. Thanks you took the time and had a look at these patches. :)



---

archive/issue_comments_083815.json:
```json
{
    "body": "patches to mderickx's review comments",
    "created_at": "2011-11-07T19:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83815",
    "user": "https://github.com/saraedum"
}
```

patches to mderickx's review comments



---

archive/issue_comments_083816.json:
```json
{
    "body": "Attachment [trac_9054_review_fixup.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_review_fixup.patch) by @saraedum created at 2011-11-07 20:07:51\n\nApply trac_9054-all-parts.patch, trac_9054-julian-combined.patch, trac_9054-review2.patch, trac_9054_review_fixup.patch.\n\nMaarten, I'm not so sure about the is_Ideal() check anymore. Is it really expected behavior that ideal(I) creates the ideal generated by the generators of I \u2014 no matter where the ideal I lives? If you feel like that should happen, then add these two lines again and set the ticket to positive review. Or don't add them if you feel that people should be more explicit by actually calling ideal(I.gens()).",
    "created_at": "2011-11-07T20:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83816",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_review_fixup.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_review_fixup.patch) by @saraedum created at 2011-11-07 20:07:51

Apply trac_9054-all-parts.patch, trac_9054-julian-combined.patch, trac_9054-review2.patch, trac_9054_review_fixup.patch.

Maarten, I'm not so sure about the is_Ideal() check anymore. Is it really expected behavior that ideal(I) creates the ideal generated by the generators of I — no matter where the ideal I lives? If you feel like that should happen, then add these two lines again and set the ticket to positive review. Or don't add them if you feel that people should be more explicit by actually calling ideal(I.gens()).



---

archive/issue_comments_083817.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-11-07T20:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83817",
    "user": "https://github.com/saraedum"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083818.json:
```json
{
    "body": "I will add it just to be consistent with numberfields.\n\n```\nsage: K.<a> = QQ.extension(x^2-2)\nsage: I = K.ideal(3)\nsage: L.<b> = K.extension(x^2-3)\nsage: L.ideal(I)\nFractional ideal (3)\nsage: L.ideal(p).factor()\n(Fractional ideal (b))^2\n```\n\nNote that it also mathematically makes sense in the most general setting since the ideal created this way is the ideal extension corresponding to the coersion map from I.ring() to self.",
    "created_at": "2011-11-07T23:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83818",
    "user": "https://github.com/koffie"
}
```

I will add it just to be consistent with numberfields.

```
sage: K.<a> = QQ.extension(x^2-2)
sage: I = K.ideal(3)
sage: L.<b> = K.extension(x^2-3)
sage: L.ideal(I)
Fractional ideal (3)
sage: L.ideal(p).factor()
(Fractional ideal (b))^2
```

Note that it also mathematically makes sense in the most general setting since the ideal created this way is the ideal extension corresponding to the coersion map from I.ring() to self.



---

archive/issue_comments_083819.json:
```json
{
    "body": "Attachment [trac_9054-can_this_really_be_the_last.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-can_this_really_be_the_last.patch) by @koffie created at 2011-11-08 00:31:52",
    "created_at": "2011-11-08T00:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83819",
    "user": "https://github.com/koffie"
}
```

Attachment [trac_9054-can_this_really_be_the_last.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-can_this_really_be_the_last.patch) by @koffie created at 2011-11-08 00:31:52



---

archive/issue_comments_083820.json:
```json
{
    "body": "If you can just check my last patch then it can have positive review.",
    "created_at": "2011-11-08T00:34:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83820",
    "user": "https://github.com/koffie"
}
```

If you can just check my last patch then it can have positive review.



---

archive/issue_comments_083821.json:
```json
{
    "body": "```\nsage: K.<x> = FunctionField(QQ)\nsage: R.<y> = K[]\nsage: L.<y> = K.extension(y^3-x)\nsage: loads(dumps(L))\nAttributeError: (\"'module' object has no attribute 'FunctionField_polymod'\", <built-in function lookup_global>, ('FunctionField_polymod',))\n```\n\nThis was also checked by `sage: TestSuite(L).run() #long time` in function_field.py.\n\nThe latest patch fixes this problem.\n\nMaarten, if you agree with this latest patch you can set it to positive review.",
    "created_at": "2011-11-08T16:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83821",
    "user": "https://github.com/saraedum"
}
```

```
sage: K.<x> = FunctionField(QQ)
sage: R.<y> = K[]
sage: L.<y> = K.extension(y^3-x)
sage: loads(dumps(L))
AttributeError: ("'module' object has no attribute 'FunctionField_polymod'", <built-in function lookup_global>, ('FunctionField_polymod',))
```

This was also checked by `sage: TestSuite(L).run() #long time` in function_field.py.

The latest patch fixes this problem.

Maarten, if you agree with this latest patch you can set it to positive review.



---

archive/issue_comments_083822.json:
```json
{
    "body": "I guess my last ticket name was a bit to hopefull. I just forgot to do add a --long after sage -tp 20 once and immediately a bug slips trough. I'm now testing everything with your last patch.",
    "created_at": "2011-11-08T17:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83822",
    "user": "https://github.com/koffie"
}
```

I guess my last ticket name was a bit to hopefull. I just forgot to do add a --long after sage -tp 20 once and immediately a bug slips trough. I'm now testing everything with your last patch.



---

archive/issue_comments_083823.json:
```json
{
    "body": "One more question. Shouldn't the line\n\nFunctionField = FunctionFieldFactory(\"FunctionField\")\n\nalso be changed in a way similar in you last patch. I mean the two things should work in the same way right?",
    "created_at": "2011-11-08T20:14:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83823",
    "user": "https://github.com/koffie"
}
```

One more question. Shouldn't the line

FunctionField = FunctionFieldFactory("FunctionField")

also be changed in a way similar in you last patch. I mean the two things should work in the same way right?



---

archive/issue_comments_083824.json:
```json
{
    "body": "We could change it but it is not necessary. `FunctionField` is exported to sage.all so the pickling infrastructure can find the name there. `FunctionField_polymod`, however, can not be found in sage.all, that's why there is the fully qualified name.",
    "created_at": "2011-11-09T12:46:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83824",
    "user": "https://github.com/saraedum"
}
```

We could change it but it is not necessary. `FunctionField` is exported to sage.all so the pickling infrastructure can find the name there. `FunctionField_polymod`, however, can not be found in sage.all, that's why there is the fully qualified name.



---

archive/issue_comments_083825.json:
```json
{
    "body": "Attachment [trac_9054_pickling.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_pickling.patch) by @koffie created at 2011-11-11 12:19:55\n\nfix pickling of FunctionField_polymod",
    "created_at": "2011-11-11T12:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83825",
    "user": "https://github.com/koffie"
}
```

Attachment [trac_9054_pickling.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_pickling.patch) by @koffie created at 2011-11-11 12:19:55

fix pickling of FunctionField_polymod



---

archive/issue_comments_083826.json:
```json
{
    "body": "I'd like to have the consistency so I changed you last patch. If your ok with it this ticket can finally have a positive review.",
    "created_at": "2011-11-11T12:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83826",
    "user": "https://github.com/koffie"
}
```

I'd like to have the consistency so I changed you last patch. If your ok with it this ticket can finally have a positive review.



---

archive/issue_comments_083827.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-11-11T15:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83827",
    "user": "https://github.com/saraedum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022185.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-11-11T22:23:00Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "milestone": "sage-4.7.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9054#event-22185"
}
```



---

archive/issue_events_022186.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-11-11T22:23:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "milestone": "sage-pending",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9054#event-22186"
}
```



---

archive/issue_comments_083828.json:
```json
{
    "body": "The commit messages of the patches could be cleaned up:\n1. [attachment:trac_9054-julian-combined.patch]: the commit message *starts* with `* * *` instead of something useful.\n2. [attachment:trac_9054-review.patch] has no proper commit message.  This improper commit message is also in [attachment:trac_9054-all-parts.patch], which should be fixed.\n3. [attachment:trac_9054-all-parts.patch] \"`contains parts 1-12, marteen's additions and final doctest fixes`\" makes no sense if you don't know this ticket, the message should makes sense on its own.  The word \"function field\" does not even appear in the message of this patch!",
    "created_at": "2011-11-15T11:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83828",
    "user": "https://github.com/jdemeyer"
}
```

The commit messages of the patches could be cleaned up:
1. [attachment:trac_9054-julian-combined.patch]: the commit message *starts* with `* * *` instead of something useful.
2. [attachment:trac_9054-review.patch] has no proper commit message.  This improper commit message is also in [attachment:trac_9054-all-parts.patch], which should be fixed.
3. [attachment:trac_9054-all-parts.patch] "`contains parts 1-12, marteen's additions and final doctest fixes`" makes no sense if you don't know this ticket, the message should makes sense on its own.  The word "function field" does not even appear in the message of this patch!



---

archive/issue_comments_083829.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-11-15T11:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83829",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_083830.json:
```json
{
    "body": "I'm replacing the commit messages now. I don't have privileges to replace attachements so I have to upload a new set of patches instead.",
    "created_at": "2011-11-15T13:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83830",
    "user": "https://github.com/saraedum"
}
```

I'm replacing the commit messages now. I don't have privileges to replace attachements so I have to upload a new set of patches instead.



---

archive/issue_comments_083831.json:
```json
{
    "body": "provide basic function field arithmetic (combined patch by various authors)",
    "created_at": "2011-11-15T13:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83831",
    "user": "https://github.com/saraedum"
}
```

provide basic function field arithmetic (combined patch by various authors)



---

archive/issue_comments_083832.json:
```json
{
    "body": "Attachment [trac_9054-julian-combined.2.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-julian-combined.2.patch) by @saraedum created at 2011-11-15 13:37:50\n\ncleanup function field code and documentation",
    "created_at": "2011-11-15T13:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83832",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054-julian-combined.2.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-julian-combined.2.patch) by @saraedum created at 2011-11-15 13:37:50

cleanup function field code and documentation



---

archive/issue_comments_083833.json:
```json
{
    "body": "Attachment [trac_9054-review2.2.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-review2.2.patch) by @saraedum created at 2011-11-15 13:38:18\n\nfix doctests for function fields",
    "created_at": "2011-11-15T13:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83833",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054-review2.2.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-review2.2.patch) by @saraedum created at 2011-11-15 13:38:18

fix doctests for function fields



---

archive/issue_comments_083834.json:
```json
{
    "body": "Attachment [trac_9054_review_fixup.2.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_review_fixup.2.patch) by @saraedum created at 2011-11-15 13:38:47\n\nfixes for function fields related to the review comments by mderickx",
    "created_at": "2011-11-15T13:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83834",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_review_fixup.2.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_review_fixup.2.patch) by @saraedum created at 2011-11-15 13:38:47

fixes for function fields related to the review comments by mderickx



---

archive/issue_comments_083835.json:
```json
{
    "body": "Attachment [trac_9054-can_this_really_be_the_last.2.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-can_this_really_be_the_last.2.patch) by @saraedum created at 2011-11-15 13:39:14\n\nlast fixes for function fields",
    "created_at": "2011-11-15T13:39:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83835",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054-can_this_really_be_the_last.2.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054-can_this_really_be_the_last.2.patch) by @saraedum created at 2011-11-15 13:39:14

last fixes for function fields



---

archive/issue_comments_083836.json:
```json
{
    "body": "fix pickling for extensions of function fields",
    "created_at": "2011-11-15T13:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83836",
    "user": "https://github.com/saraedum"
}
```

fix pickling for extensions of function fields



---

archive/issue_comments_083837.json:
```json
{
    "body": "Attachment [trac_9054_pickling.2.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_pickling.2.patch) by @saraedum created at 2011-11-15 13:42:17\n\nApply trac_9054-all-parts.2.patch, trac_9054-julian-combined.2.patch, trac_9054-review2.2.patch, trac_9054_review_fixup.2.patch, trac_9054-can_this_really_be_the_last.2.patch, trac_9054_pickling.2.patch",
    "created_at": "2011-11-15T13:42:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83837",
    "user": "https://github.com/saraedum"
}
```

Attachment [trac_9054_pickling.2.patch](tarball://root/attachments/some-uuid/ticket9054/trac_9054_pickling.2.patch) by @saraedum created at 2011-11-15 13:42:17

Apply trac_9054-all-parts.2.patch, trac_9054-julian-combined.2.patch, trac_9054-review2.2.patch, trac_9054_review_fixup.2.patch, trac_9054-can_this_really_be_the_last.2.patch, trac_9054_pickling.2.patch



---

archive/issue_comments_083838.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-11-15T13:42:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83838",
    "user": "https://github.com/saraedum"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_events_022187.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-12-09T23:57:29Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "milestone": "sage-pending",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9054#event-22187"
}
```



---

archive/issue_events_022188.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-12-09T23:57:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9054#event-22188"
}
```



---

archive/issue_comments_083839.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-01-22T21:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83839",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_083840.json:
```json
{
    "body": "Patches [attachment:trac_9054-all-parts.2.patch] and [attachment:trac_9054-review2.2.patch] apply with fuzz 2 against sage-5.0.beta1.  Please rebase such that they apply cleanly.",
    "created_at": "2012-01-22T21:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83840",
    "user": "https://github.com/jdemeyer"
}
```

Patches [attachment:trac_9054-all-parts.2.patch] and [attachment:trac_9054-review2.2.patch] apply with fuzz 2 against sage-5.0.beta1.  Please rebase such that they apply cleanly.



---

archive/issue_comments_083841.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-01-30T10:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83841",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_083842.json:
```json
{
    "body": "Thanks for rebasing, I added it to my todo list, but didn't get to it yet.",
    "created_at": "2012-01-30T12:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83842",
    "user": "https://github.com/koffie"
}
```

Thanks for rebasing, I added it to my todo list, but didn't get to it yet.



---

archive/issue_comments_083843.json:
```json
{
    "body": "Attachment [9054_function_fields.patch](tarball://root/attachments/some-uuid/ticket9054/9054_function_fields.patch) by @jdemeyer created at 2012-01-31 09:08:07",
    "created_at": "2012-01-31T09:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83843",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [9054_function_fields.patch](tarball://root/attachments/some-uuid/ticket9054/9054_function_fields.patch) by @jdemeyer created at 2012-01-31 09:08:07



---

archive/issue_comments_083844.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-02-02T12:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9054#issuecomment-83844",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_022189.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-02-02T12:52:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9054",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9054#event-22189"
}
```

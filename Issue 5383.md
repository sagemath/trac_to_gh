# Issue 5383: isinstance(PrincipalIdealDomain) should be replaced with a method .is_principal_ideal_domain()

archive/issues_005383.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: principal ideal domain span free module isinstance\n\nThis is the cause of things like:\n\n\n```\nsage: R.<x, y> = QQ[]\nsage: M = R^2\nsage: span(R, vector([1, 0]))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/ncalexan/.sage/temp/dhcp_v009_038.mobile.uci.edu/301/_Users_ncalexan_Documents_School_rumely_polynomial_ring_as_module2_sage_142.py in <module>()\n\n/Users/ncalexan/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in span(gens, base_ring, check, already_echelonized)\n    408 \n    409     if not isinstance(R, principal_ideal_domain.PrincipalIdealDomain):\n--> 410         raise TypeError, \"The base_ring (= %s) must be a principal ideal domain.\"%R\n    411     if len(gens) == 0:\n    412         return FreeModule(R, 0)\n\nTypeError: The base_ring (= Multivariate Polynomial Ring in x, y over Rational Field) must be a principal ideal domain.\n```\n\n\nSurprisingly few places where this bites us:\n\n\n```\nsage: search_src('PrincipalIdealDomain')\nmodules/free_module.py:        elif isinstance(base_ring, principal_ideal_domain.PrincipalIdealDomain):\nmodules/free_module.py:    if not isinstance(R, principal_ideal_domain.PrincipalIdealDomain):\nmodules/free_module.py:        if not isinstance(base_ring, principal_ideal_domain.PrincipalIdealDomain):\nmodules/free_quadratic_module.py:    elif isinstance(base_ring, principal_ideal_domain.PrincipalIdealDomain):\nrings/all.py:from principal_ideal_domain import PrincipalIdealDomain, is_PrincipalIdealDomain\nrings/all.py:from principal_ideal_domain_element import PrincipalIdealDomainElement, is_PrincipalIdealDomainElement\nrings/ideal.py:    if isinstance(R, sage.rings.principal_ideal_domain.PrincipalIdealDomain):\n<snip>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5383\n\n",
    "created_at": "2009-02-26T04:41:00Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.2",
    "title": "isinstance(PrincipalIdealDomain) should be replaced with a method .is_principal_ideal_domain()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5383",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

Keywords: principal ideal domain span free module isinstance

This is the cause of things like:


```
sage: R.<x, y> = QQ[]
sage: M = R^2
sage: span(R, vector([1, 0]))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/ncalexan/.sage/temp/dhcp_v009_038.mobile.uci.edu/301/_Users_ncalexan_Documents_School_rumely_polynomial_ring_as_module2_sage_142.py in <module>()

/Users/ncalexan/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in span(gens, base_ring, check, already_echelonized)
    408 
    409     if not isinstance(R, principal_ideal_domain.PrincipalIdealDomain):
--> 410         raise TypeError, "The base_ring (= %s) must be a principal ideal domain."%R
    411     if len(gens) == 0:
    412         return FreeModule(R, 0)

TypeError: The base_ring (= Multivariate Polynomial Ring in x, y over Rational Field) must be a principal ideal domain.
```


Surprisingly few places where this bites us:


```
sage: search_src('PrincipalIdealDomain')
modules/free_module.py:        elif isinstance(base_ring, principal_ideal_domain.PrincipalIdealDomain):
modules/free_module.py:    if not isinstance(R, principal_ideal_domain.PrincipalIdealDomain):
modules/free_module.py:        if not isinstance(base_ring, principal_ideal_domain.PrincipalIdealDomain):
modules/free_quadratic_module.py:    elif isinstance(base_ring, principal_ideal_domain.PrincipalIdealDomain):
rings/all.py:from principal_ideal_domain import PrincipalIdealDomain, is_PrincipalIdealDomain
rings/all.py:from principal_ideal_domain_element import PrincipalIdealDomainElement, is_PrincipalIdealDomainElement
rings/ideal.py:    if isinstance(R, sage.rings.principal_ideal_domain.PrincipalIdealDomain):
<snip>
```


Issue created by migration from https://trac.sagemath.org/ticket/5383





---

archive/issue_comments_041375.json:
```json
{
    "body": "I realize now, of course, that QQ['x', 'y'] is not a PID... but I still think our type dependent implementation is not good :)",
    "created_at": "2009-02-26T17:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5383#issuecomment-41375",
    "user": "https://github.com/ncalexan"
}
```

I realize now, of course, that QQ['x', 'y'] is not a PID... but I still think our type dependent implementation is not good :)



---

archive/issue_comments_041376.json:
```json
{
    "body": "Better luck in 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5383#issuecomment-41376",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Better luck in 3.4.1.

Cheers,

Michael



---

archive/issue_comments_041377.json:
```json
{
    "body": "This should do it.",
    "created_at": "2013-07-23T14:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5383#issuecomment-41377",
    "user": "https://github.com/mwhansen"
}
```

This should do it.



---

archive/issue_comments_041378.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-07-23T14:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5383#issuecomment-41378",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_041379.json:
```json
{
    "body": "Attachment [trac_5383.patch](tarball://root/attachments/some-uuid/ticket5383/trac_5383.patch) by @mwhansen created at 2013-07-23 15:30:09",
    "created_at": "2013-07-23T15:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5383#issuecomment-41379",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5383.patch](tarball://root/attachments/some-uuid/ticket5383/trac_5383.patch) by @mwhansen created at 2013-07-23 15:30:09



---

archive/issue_comments_041380.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-18T07:32:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5383#issuecomment-41380",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_041381.json:
```json
{
    "body": "Easy ticket.\n----\nNew commits:",
    "created_at": "2014-02-18T07:32:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5383#issuecomment-41381",
    "user": "https://github.com/rwst"
}
```

Easy ticket.
----
New commits:



---

archive/issue_comments_041382.json:
```json
{
    "body": "Changing status from positive_review to needs_review.",
    "created_at": "2014-02-20T17:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5383#issuecomment-41382",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Changing status from positive_review to needs_review.



---

archive/issue_comments_041383.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:",
    "created_at": "2014-02-20T17:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5383#issuecomment-41383",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:



---

archive/issue_comments_041384.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-20T17:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5383#issuecomment-41384",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_041385.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-02-23T07:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5383#issuecomment-41385",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed

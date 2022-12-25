# Issue 1127: modularSymbol complement fails for E=128a

archive/issues_001127.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robertwb\n\nThe following code raises the following exception:\n\n```\nsage: E=EllipticCurve(\"128a\")\nsage: ME=E.modular_symbol_space()\nsage: ME.complement()\n---------------------------------------------------------------------------\n<type 'exceptions.RuntimeError'>          Traceback (most recent call last)\n\n/net/mathserv/1/home/syazdani/research/programs/<ipython console> in <module>()\n\n/home/syazdani/sage/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py in complement(self, bound)\n    200         else:\n    201             # failed\n--> 202             raise RuntimeError, \"Computation of complementary space failed (cut down to rank %s, but should have cut down to rank %s).\"%(V.rank(), self.rank())\n    203\n    204\n\n<type 'exceptions.RuntimeError'>: Computation of complementary space failed (cut down to rank 18, but should have cut down to rank 1).\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1127\n\n",
    "created_at": "2007-11-07T20:35:42Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "modularSymbol complement fails for E=128a",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1127",
    "user": "https://github.com/syazdani77"
}
```
Assignee: @williamstein

CC:  @robertwb

The following code raises the following exception:

```
sage: E=EllipticCurve("128a")
sage: ME=E.modular_symbol_space()
sage: ME.complement()
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/net/mathserv/1/home/syazdani/research/programs/<ipython console> in <module>()

/home/syazdani/sage/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py in complement(self, bound)
    200         else:
    201             # failed
--> 202             raise RuntimeError, "Computation of complementary space failed (cut down to rank %s, but should have cut down to rank %s)."%(V.rank(), self.rank())
    203
    204

<type 'exceptions.RuntimeError'>: Computation of complementary space failed (cut down to rank 18, but should have cut down to rank 1).
```

Issue created by migration from https://trac.sagemath.org/ticket/1127





---

archive/issue_events_003010.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-07T22:35:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1127",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1127#event-3010"
}
```



---

archive/issue_events_003011.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-18T09:11:26Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1127",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1127#event-3011"
}
```



---

archive/issue_events_003012.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-18T09:11:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1127",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1127#event-3012"
}
```



---

archive/issue_comments_006787.json:
```json
{
    "body": "This remains unfixed in Sage 2.9.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-18T09:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1127#issuecomment-6787",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This remains unfixed in Sage 2.9.

Cheers,

Michael



---

archive/issue_comments_006788.json:
```json
{
    "body": "And it is still open in Sage 2.10.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-20T02:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1127#issuecomment-6788",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

And it is still open in Sage 2.10.

Cheers,

Michael



---

archive/issue_comments_006789.json:
```json
{
    "body": "And it is still broken in Sage 3.0.3. This looks like a job for Craig Citro :)\n\nCheers,\n\nMichael",
    "created_at": "2008-06-26T06:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1127#issuecomment-6789",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

And it is still broken in Sage 3.0.3. This looks like a job for Craig Citro :)

Cheers,

Michael



---

archive/issue_comments_006790.json:
```json
{
    "body": "Changing assignee from @williamstein to @craigcitro.",
    "created_at": "2008-06-26T06:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1127#issuecomment-6790",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to @craigcitro.



---

archive/issue_comments_006791.json:
```json
{
    "body": "Could #2535 be related?\n\nCheers,\n\nMichael",
    "created_at": "2008-11-02T16:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1127#issuecomment-6791",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Could #2535 be related?

Cheers,

Michael



---

archive/issue_comments_006792.json:
```json
{
    "body": "For the record, there are other failures for conductors 144, 192, 225.  These are the only conductors smaller than 250 that fail.\n\nThe patch implements a naive fix.",
    "created_at": "2009-01-22T23:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1127#issuecomment-6792",
    "user": "https://github.com/aghitza"
}
```

For the record, there are other failures for conductors 144, 192, 225.  These are the only conductors smaller than 250 that fail.

The patch implements a naive fix.



---

archive/issue_comments_006793.json:
```json
{
    "body": "I'd review this, but I helped write it. :)",
    "created_at": "2009-01-22T23:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1127#issuecomment-6793",
    "user": "https://github.com/craigcitro"
}
```

I'd review this, but I helped write it. :)



---

archive/issue_comments_006794.json:
```json
{
    "body": "I'm still getting \n\n```\nsage: E = EllipticCurve(\"128a\") \nsage: E.congruence_number()\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 2618, in congruence_number\n    self.__congruence_number = W.congruence_number(V)\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py\", line 938, in congruence_number\n    W = other.q_expansion_module(prec, ZZ)\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py\", line 770, in q_expansion_module\n    return self._q_expansion_module_integral(prec)\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py\", line 910, in _q_expansion_module_integral\n    V = self.q_expansion_module(prec, QQ)\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py\", line 772, in q_expansion_module\n    return self._q_expansion_module_rational(prec)\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py\", line 861, in _q_expansion_module_rational\n    return self._q_expansion_module(prec)\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py\", line 820, in _q_expansion_module\n    return A.span([f.padded_list(prec) for f in self.q_expansion_basis(prec, algorithm)])\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py\", line 602, in q_expansion_basis\n    return Sequence(self._q_expansion_basis_hecke_dual(prec), cr=True)\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py\", line 1073, in _q_expansion_basis_hecke_dual\n    v = [self.dual_hecke_matrix(n).column(i) for n in range(1,prec)]\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/hecke/module.py\", line 797, in dual_hecke_matrix\n    T = self._compute_dual_hecke_matrix(n)\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py\", line 110, in _compute_dual_hecke_matrix\n    return A.restrict(self.dual_free_module(), check=check)\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py\", line 320, in dual_free_module\n    \"(cut down to rank %s, but should have cut down to rank %s).\"%(V.rank(), self.rank())\nRuntimeError: Computation of embedded dual vector space failed (cut down to rank 9, but should have cut down to rank 8).\n```",
    "created_at": "2009-01-23T22:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1127#issuecomment-6794",
    "user": "https://github.com/robertwb"
}
```

I'm still getting 

```
sage: E = EllipticCurve("128a") 
sage: E.congruence_number()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 2618, in congruence_number
    self.__congruence_number = W.congruence_number(V)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 938, in congruence_number
    W = other.q_expansion_module(prec, ZZ)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 770, in q_expansion_module
    return self._q_expansion_module_integral(prec)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 910, in _q_expansion_module_integral
    V = self.q_expansion_module(prec, QQ)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 772, in q_expansion_module
    return self._q_expansion_module_rational(prec)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 861, in _q_expansion_module_rational
    return self._q_expansion_module(prec)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 820, in _q_expansion_module
    return A.span([f.padded_list(prec) for f in self.q_expansion_basis(prec, algorithm)])
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 602, in q_expansion_basis
    return Sequence(self._q_expansion_basis_hecke_dual(prec), cr=True)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 1073, in _q_expansion_basis_hecke_dual
    v = [self.dual_hecke_matrix(n).column(i) for n in range(1,prec)]
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/hecke/module.py", line 797, in dual_hecke_matrix
    T = self._compute_dual_hecke_matrix(n)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py", line 110, in _compute_dual_hecke_matrix
    return A.restrict(self.dual_free_module(), check=check)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py", line 320, in dual_free_module
    "(cut down to rank %s, but should have cut down to rank %s)."%(V.rank(), self.rank())
RuntimeError: Computation of embedded dual vector space failed (cut down to rank 9, but should have cut down to rank 8).
```



---

archive/issue_comments_006795.json:
```json
{
    "body": "This is a separate issue, see #5080. The patch fixes the issue that was raised.",
    "created_at": "2009-01-24T00:31:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1127#issuecomment-6795",
    "user": "https://github.com/robertwb"
}
```

This is a separate issue, see #5080. The patch fixes the issue that was raised.



---

archive/issue_comments_006796.json:
```json
{
    "body": "Attachment [trac_1127.patch](tarball://root/attachments/some-uuid/ticket1127/trac_1127.patch) by mabshoff created at 2009-01-24 19:30:30\n\nMerged in Sage 3.3.alpha2\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T19:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1127#issuecomment-6796",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_1127.patch](tarball://root/attachments/some-uuid/ticket1127/trac_1127.patch) by mabshoff created at 2009-01-24 19:30:30

Merged in Sage 3.3.alpha2

Cheers,

Michael



---

archive/issue_events_003013.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T19:30:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1127",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1127#event-3013"
}
```



---

archive/issue_comments_006797.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T19:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1127#issuecomment-6797",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003014.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T19:30:30Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1127",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1127#event-3014"
}
```



---

archive/issue_events_003015.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T19:30:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1127",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1127#event-3015"
}
```

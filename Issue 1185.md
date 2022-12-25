# Issue 1185: Coercion trouble

archive/issues_001185.json:
```json
{
    "body": "Assignee: @williamstein\n\nI run into some coercion trouble when I reduce a fourier coefficient\nof a cusp form modulo a prime ideal.\n\nAny idea how I can avoid this?\n\n\n```\nsage: M = ModularSymbols(77, 2)\n\nsage: s = M.cuspidal_subspace().new_subspace()\n\nsage: N = s.decomposition()\n\nsage: f = N[3].q_eigenform()\n\nsage: R = f.base_ring()\n\nsage: K = R.number_field()\n\nsage: O = K.ring_of_integers()\n\nsage: I = O.ideal(7)\n\nsage: F = O.residue_field(I)\n\nsage: F(f[2])\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call\nlast)\n\n/home/burhanud/tau_nov14_07/<ipython console> in <module>()\n\n/home/burhanud/tau_nov14_07/residue_field.pyx in\nsage.rings.residue_field.ResidueFiniteField_givaro.__call__()\n\n/home/burhanud/tau_nov14_07/finite_field_givaro.pyx in\nsage.rings.finite_field_givaro.FiniteField_givaro.__call__()\n\n<type 'exceptions.TypeError'>: unable to coerce\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1185\n\n",
    "created_at": "2007-11-16T10:39:30Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "Coercion trouble",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1185",
    "user": "https://trac.sagemath.org/admin/accounts/users/ifti"
}
```
Assignee: @williamstein

I run into some coercion trouble when I reduce a fourier coefficient
of a cusp form modulo a prime ideal.

Any idea how I can avoid this?


```
sage: M = ModularSymbols(77, 2)

sage: s = M.cuspidal_subspace().new_subspace()

sage: N = s.decomposition()

sage: f = N[3].q_eigenform()

sage: R = f.base_ring()

sage: K = R.number_field()

sage: O = K.ring_of_integers()

sage: I = O.ideal(7)

sage: F = O.residue_field(I)

sage: F(f[2])
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call
last)

/home/burhanud/tau_nov14_07/<ipython console> in <module>()

/home/burhanud/tau_nov14_07/residue_field.pyx in
sage.rings.residue_field.ResidueFiniteField_givaro.__call__()

/home/burhanud/tau_nov14_07/finite_field_givaro.pyx in
sage.rings.finite_field_givaro.FiniteField_givaro.__call__()

<type 'exceptions.TypeError'>: unable to coerce
```


Issue created by migration from https://trac.sagemath.org/ticket/1185





---

archive/issue_comments_007293.json:
```json
{
    "body": "This was an email posted to the sage-devel mailing list on 11/05/07. Consult thread for the discussion.",
    "created_at": "2007-11-16T10:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1185#issuecomment-7293",
    "user": "https://trac.sagemath.org/admin/accounts/users/ifti"
}
```

This was an email posted to the sage-devel mailing list on 11/05/07. Consult thread for the discussion.



---

archive/issue_comments_007294.json:
```json
{
    "body": "David Roe filed another ticket on that, so please also look at #1183.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-16T11:13:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1185#issuecomment-7294",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

David Roe filed another ticket on that, so please also look at #1183.

Cheers,

Michael



---

archive/issue_comments_007295.json:
```json
{
    "body": "The correct way is this, which works with #1183 applied.\n\n```\nsage: M = ModularSymbols(77, 2)\nsage: s = M.cuspidal_subspace().new_subspace()\nsage: N = s.decomposition()\nsage: f = N[3].q_eigenform()\nsage: R = f.base_ring()\nsage: K = R.number_field()\nsage: O = K.ring_of_integers()\nsage: I = O.ideal(7)\nsage: F = O.residue_field(I)\nsage: F(f[2].lift())\nalphabar\n```\n",
    "created_at": "2007-12-15T10:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1185#issuecomment-7295",
    "user": "https://github.com/williamstein"
}
```

The correct way is this, which works with #1183 applied.

```
sage: M = ModularSymbols(77, 2)
sage: s = M.cuspidal_subspace().new_subspace()
sage: N = s.decomposition()
sage: f = N[3].q_eigenform()
sage: R = f.base_ring()
sage: K = R.number_field()
sage: O = K.ring_of_integers()
sage: I = O.ideal(7)
sage: F = O.residue_field(I)
sage: F(f[2].lift())
alphabar
```




---

archive/issue_comments_007296.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T13:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1185#issuecomment-7296",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007297.json:
```json
{
    "body": "resolved due to patch set from #1183",
    "created_at": "2007-12-15T13:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1185",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1185#issuecomment-7297",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

resolved due to patch set from #1183

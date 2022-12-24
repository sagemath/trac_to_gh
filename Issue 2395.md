# Issue 2395: [with patch, needs review] New features for number fields (gap interface, matrix groups)

archive/issues_002395.json:
```json
{
    "body": "Assignee: @simon-king-jena\n\nCC:  @wdjoyner\n\nKeywords: number field, gap interface, matrix group\n\nThis ticket replaces #2348 and #2367. The attached patch provides several new features related with number fields.\n\n---------\n\nFirstly, the patch fixes a bug of the gap interface for number fields and their elements. The _gap_init_ method of number fields is now based on gap inline functions (thanks to Nathan Dunfield for that hint!):\n\n```\nsage: F=CyclotomicField(8)\nsage: gap(QQ).name()\n'$sage1'\nsage: F._gap_init_()\n'CallFuncList(function() local x,E; x:=Indeterminate($sage1,\"x\"); E:=AlgebraicExtension($sage1,x^4 + 1,\"zeta8\"); return E; end,[])'\nsage: gap(F)\n<algebraic extension over the Rationals of degree 4>\n```\n\nNote that the variable `$sage1` represents gap(QQ) -- QQ is the base ring of F.\n\nI also learned from Nathan Dunfield that gap(F) is cached. Hence, if p is an element of F then p._gap_init_() may refer to gap(F).name(), which is `$sage2`:\n\n```\nsage: p=3*F.gen()^3-F.gen()^2+F.gen()+1\nsage: p._gap_init_()\n'3*GeneratorsOfField($sage2)[1]^3 - GeneratorsOfField($sage2)[1]^2 + GeneratorsOfField($sage2)[1] + 1'\nsage: gap(p)\n(1+zeta8-1*zeta8^2+3*zeta8^3)\n```\n\nNote that the generator of gap(F) got the same name `'zeta8'` as the generator of F.\n\nAnother extension was needed in the _gap_init_ method of matrices. The problem is that `[[elem1,elem2],[elem3,elem4]]` is in general not a matrix; it has to be multiplied with One(field):\n\n```\nsage: z=F.gen()\nsage: a=z+1/z\nsage: b=z^2\nsage: MS=MatrixSpace(F,2,2)\nsage: g1=MS([[1/a,1/a],[1/a,-1/a]])\nsage: g2=MS([[1,0],[0,b]])\nsage: g3=MS([[b,0],[0,1]])\nsage: g1._gap_init_()\n'[[-1/2*GeneratorsOfField($sage2)[1]^3 + 1/2*GeneratorsOfField($sage2)[1],-1/2*GeneratorsOfField($sage2)[1]^3 + 1/2*GeneratorsOfField($sage2)[1]],[-1/2*GeneratorsOfField($sage2)[1]^3 + 1/2*GeneratorsOfField($sage2)[1],1/2*GeneratorsOfField($sage2)[1]^3 - 1/2*GeneratorsOfField($sage2)[1]]]*One($sage2)'\n\nsage: gap(g1)\n[ [ (1/2*zeta8-1/2*zeta8^3), (1/2*zeta8-1/2*zeta8^3) ],\n  [ (1/2*zeta8-1/2*zeta8^3), (-1/2*zeta8+1/2*zeta8^3) ] ]\nsage: gap(g1).IsMatrix()\ntrue\n\nsage: gap('[[GeneratorsOfField($sage2)[1],1],[1,GeneratorsOfField($sage2)[1]]]').IsMatrix()\nfalse\n```\n\n\nNow, one can compute with the gap matrices:\n\n```\nsage: (gap(g1)*gap(g2))^12\n[ [ !-1, !0 ], [ !0, !-1 ] ]\nsage: (g1*g2)^12\n[-1  0]\n[ 0 -1]\n```\n\nNote that `!-1` means that the integer -1 is interpreted as element of a different field, namely of gap(F).\n\n--------\n\nSecondly, the patch extends the method invariant_generators of MatrixGroup to the case of matrix groups over number fields. Fixing the gap interface for number fields suffices for defining matrix groups over number fields; but extending the method invariant_generators requires more effort. Now, the following computation works:\n\n```\nsage: G=MatrixGroup([g1,g2,g3])\nsage: G.order()\n192\nsage: G.invariant_generators()\n[x1^8 + 14*x1^4*x2^4 + x2^8,\n x1^24 + 10626/1025*x1^20*x2^4 + 735471/1025*x1^16*x2^8 + 2704156/1025*x1^12*x2^12 + 735471/1025*x1^8*x2^16 + 10626/1025*x1^4*x2^20 + x2^24]\n```\n\n\n---------------\n\nThe various _gap_init_ methods (in matrix1.pyx, number_field_element.pyx, number_field.py, matrix_group.py and matrix_group_element.py) got doctests. Also, i added more doc tests to invariant_generators, based on examples of David Joyner.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2395\n\n",
    "created_at": "2008-03-05T10:28:19Z",
    "labels": [
        "group theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch, needs review] New features for number fields (gap interface, matrix groups)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2395",
    "user": "@simon-king-jena"
}
```
Assignee: @simon-king-jena

CC:  @wdjoyner

Keywords: number field, gap interface, matrix group

This ticket replaces #2348 and #2367. The attached patch provides several new features related with number fields.

---------

Firstly, the patch fixes a bug of the gap interface for number fields and their elements. The _gap_init_ method of number fields is now based on gap inline functions (thanks to Nathan Dunfield for that hint!):

```
sage: F=CyclotomicField(8)
sage: gap(QQ).name()
'$sage1'
sage: F._gap_init_()
'CallFuncList(function() local x,E; x:=Indeterminate($sage1,"x"); E:=AlgebraicExtension($sage1,x^4 + 1,"zeta8"); return E; end,[])'
sage: gap(F)
<algebraic extension over the Rationals of degree 4>
```

Note that the variable `$sage1` represents gap(QQ) -- QQ is the base ring of F.

I also learned from Nathan Dunfield that gap(F) is cached. Hence, if p is an element of F then p._gap_init_() may refer to gap(F).name(), which is `$sage2`:

```
sage: p=3*F.gen()^3-F.gen()^2+F.gen()+1
sage: p._gap_init_()
'3*GeneratorsOfField($sage2)[1]^3 - GeneratorsOfField($sage2)[1]^2 + GeneratorsOfField($sage2)[1] + 1'
sage: gap(p)
(1+zeta8-1*zeta8^2+3*zeta8^3)
```

Note that the generator of gap(F) got the same name `'zeta8'` as the generator of F.

Another extension was needed in the _gap_init_ method of matrices. The problem is that `[[elem1,elem2],[elem3,elem4]]` is in general not a matrix; it has to be multiplied with One(field):

```
sage: z=F.gen()
sage: a=z+1/z
sage: b=z^2
sage: MS=MatrixSpace(F,2,2)
sage: g1=MS([[1/a,1/a],[1/a,-1/a]])
sage: g2=MS([[1,0],[0,b]])
sage: g3=MS([[b,0],[0,1]])
sage: g1._gap_init_()
'[[-1/2*GeneratorsOfField($sage2)[1]^3 + 1/2*GeneratorsOfField($sage2)[1],-1/2*GeneratorsOfField($sage2)[1]^3 + 1/2*GeneratorsOfField($sage2)[1]],[-1/2*GeneratorsOfField($sage2)[1]^3 + 1/2*GeneratorsOfField($sage2)[1],1/2*GeneratorsOfField($sage2)[1]^3 - 1/2*GeneratorsOfField($sage2)[1]]]*One($sage2)'

sage: gap(g1)
[ [ (1/2*zeta8-1/2*zeta8^3), (1/2*zeta8-1/2*zeta8^3) ],
  [ (1/2*zeta8-1/2*zeta8^3), (-1/2*zeta8+1/2*zeta8^3) ] ]
sage: gap(g1).IsMatrix()
true

sage: gap('[[GeneratorsOfField($sage2)[1],1],[1,GeneratorsOfField($sage2)[1]]]').IsMatrix()
false
```


Now, one can compute with the gap matrices:

```
sage: (gap(g1)*gap(g2))^12
[ [ !-1, !0 ], [ !0, !-1 ] ]
sage: (g1*g2)^12
[-1  0]
[ 0 -1]
```

Note that `!-1` means that the integer -1 is interpreted as element of a different field, namely of gap(F).

--------

Secondly, the patch extends the method invariant_generators of MatrixGroup to the case of matrix groups over number fields. Fixing the gap interface for number fields suffices for defining matrix groups over number fields; but extending the method invariant_generators requires more effort. Now, the following computation works:

```
sage: G=MatrixGroup([g1,g2,g3])
sage: G.order()
192
sage: G.invariant_generators()
[x1^8 + 14*x1^4*x2^4 + x2^8,
 x1^24 + 10626/1025*x1^20*x2^4 + 735471/1025*x1^16*x2^8 + 2704156/1025*x1^12*x2^12 + 735471/1025*x1^8*x2^16 + 10626/1025*x1^4*x2^20 + x2^24]
```


---------------

The various _gap_init_ methods (in matrix1.pyx, number_field_element.pyx, number_field.py, matrix_group.py and matrix_group_element.py) got doctests. Also, i added more doc tests to invariant_generators, based on examples of David Joyner.



Issue created by migration from https://trac.sagemath.org/ticket/2395





---

archive/issue_comments_016157.json:
```json
{
    "body": "Patch provides extension of the gap interface and of matrix groups to the case of number fields. Should apply to sage-2.10.3.rc1",
    "created_at": "2008-03-05T10:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2395#issuecomment-16157",
    "user": "@simon-king-jena"
}
```

Patch provides extension of the gap interface and of matrix groups to the case of number fields. Should apply to sage-2.10.3.rc1



---

archive/issue_comments_016158.json:
```json
{
    "body": "Attachment [about_numberfields.patch](tarball://root/attachments/some-uuid/ticket2395/about_numberfields.patch) by @mwhansen created at 2008-03-05 13:36:20\n\nApplies and passes tests for me.",
    "created_at": "2008-03-05T13:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2395#issuecomment-16158",
    "user": "@mwhansen"
}
```

Attachment [about_numberfields.patch](tarball://root/attachments/some-uuid/ticket2395/about_numberfields.patch) by @mwhansen created at 2008-03-05 13:36:20

Applies and passes tests for me.



---

archive/issue_comments_016159.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc2",
    "created_at": "2008-03-05T14:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2395#issuecomment-16159",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc2



---

archive/issue_comments_016160.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-05T14:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2395#issuecomment-16160",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016161.json:
```json
{
    "body": "This looks good too. Applies cleanly against 2.10.3.rc1. Passes sage -testall, except for the ones that fail without any patches (rings/polynomial/groebner_fan.py, plot/plot.py).",
    "created_at": "2008-03-05T14:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2395#issuecomment-16161",
    "user": "@wdjoyner"
}
```

This looks good too. Applies cleanly against 2.10.3.rc1. Passes sage -testall, except for the ones that fail without any patches (rings/polynomial/groebner_fan.py, plot/plot.py).

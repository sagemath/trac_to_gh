# Issue 4388: elliptic curves: basis_matrix command totally broken

archive/issues_004388.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: EllipticCurve('11a').period_lattice().basis_matrix()\nTraceback (most recent call last):\n...\nTypeError: Unable to coerce 0.634604652139777 + 1.45881661693850*I (<type 'sage.rings.complex_number.ComplexNumber'>) to Rational\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4388\n\n",
    "created_at": "2008-10-30T05:15:58Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "elliptic curves: basis_matrix command totally broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4388",
    "user": "was"
}
```
Assignee: was


```
sage: EllipticCurve('11a').period_lattice().basis_matrix()
Traceback (most recent call last):
...
TypeError: Unable to coerce 0.634604652139777 + 1.45881661693850*I (<type 'sage.rings.complex_number.ComplexNumber'>) to Rational
```


Issue created by migration from https://trac.sagemath.org/ticket/4388





---

archive/issue_comments_032298.json:
```json
{
    "body": "Comment:  I noticed this when I reworked the whole of period_lattice.py recently.  But the function basis_matrix only exists because  PeriodLattice_ell derives from  PeriodLattice and hence from FreeModule_generic_pid.  But I don't think it makes a lot of sense to ask for a basis matrix in a case like this, when the thing is a Z-module but it does not sit in an ambient Q-vector space.\n\nIf people agree, we should at least add the function but have it raise a sensible error.",
    "created_at": "2008-10-30T17:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4388#issuecomment-32298",
    "user": "cremona"
}
```

Comment:  I noticed this when I reworked the whole of period_lattice.py recently.  But the function basis_matrix only exists because  PeriodLattice_ell derives from  PeriodLattice and hence from FreeModule_generic_pid.  But I don't think it makes a lot of sense to ask for a basis matrix in a case like this, when the thing is a Z-module but it does not sit in an ambient Q-vector space.

If people agree, we should at least add the function but have it raise a sensible error.



---

archive/issue_comments_032299.json:
```json
{
    "body": "But I really wanted basis_matrix(), since I wanted to compute the determinant of the basis matrix in order to find the volume of the period lattice. \n\nThere is no volume method.  That would also be nice.   \n\nI think at least mathematically the idea of \"basis matrix\" makes sense, and I was happy it was there (except that it is broken).",
    "created_at": "2008-10-30T18:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4388#issuecomment-32299",
    "user": "was"
}
```

But I really wanted basis_matrix(), since I wanted to compute the determinant of the basis matrix in order to find the volume of the period lattice. 

There is no volume method.  That would also be nice.   

I think at least mathematically the idea of "basis matrix" makes sense, and I was happy it was there (except that it is broken).



---

archive/issue_comments_032300.json:
```json
{
    "body": "Replying to [comment:2 was]:\n> But I really wanted basis_matrix(), since I wanted to compute the determinant of the basis matrix in order to find the volume of the period lattice. \n> \n> There is no volume method.  That would also be nice.   \n\nIt _is_ there:  complex_area()  (not my choice of name)!\n\n> \n> I think at least mathematically the idea of \"basis matrix\" makes sense, and I was happy it was there (except that it is broken).\n\nYou'll have to explain it to me.  Do you want the 2x2 matrix of reals consisting of the real and imaginary parts of the period basis?  That would be easy to add, like this:\n\n\n```\nsage: E = EllipticCurve('389a1')\nsage: L = E.period_lattice()\nsage: M = Matrix([[CC(w).real(), CC(w).imag()] for w in L.basis()]); M\n\n[ 2.49021256085505 0.000000000000000]\n[0.000000000000000  1.97173770155165]\nsage: M.det()\n4.91004599111539\nsage: L.complex_area()\n4.91004599111539\n```\n\n\n\nand\n\n\n```\nsage: E = EllipticCurve('11a1')\nsage: L = E.period_lattice()\nsage: M = Matrix([[CC(w).real(), CC(w).imag()] for w in L.basis()]); M\n\n[ 1.26920930427955 0.000000000000000]\n[0.634604652139777  1.45881661693850]\nsage: M.det()\n1.85154362345596\nsage: L.complex_area()\n1.85154362345596\n```\n",
    "created_at": "2008-10-30T18:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4388#issuecomment-32300",
    "user": "cremona"
}
```

Replying to [comment:2 was]:
> But I really wanted basis_matrix(), since I wanted to compute the determinant of the basis matrix in order to find the volume of the period lattice. 
> 
> There is no volume method.  That would also be nice.   

It _is_ there:  complex_area()  (not my choice of name)!

> 
> I think at least mathematically the idea of "basis matrix" makes sense, and I was happy it was there (except that it is broken).

You'll have to explain it to me.  Do you want the 2x2 matrix of reals consisting of the real and imaginary parts of the period basis?  That would be easy to add, like this:


```
sage: E = EllipticCurve('389a1')
sage: L = E.period_lattice()
sage: M = Matrix([[CC(w).real(), CC(w).imag()] for w in L.basis()]); M

[ 2.49021256085505 0.000000000000000]
[0.000000000000000  1.97173770155165]
sage: M.det()
4.91004599111539
sage: L.complex_area()
4.91004599111539
```



and


```
sage: E = EllipticCurve('11a1')
sage: L = E.period_lattice()
sage: M = Matrix([[CC(w).real(), CC(w).imag()] for w in L.basis()]); M

[ 1.26920930427955 0.000000000000000]
[0.634604652139777  1.45881661693850]
sage: M.det()
1.85154362345596
sage: L.complex_area()
1.85154362345596
```




---

archive/issue_comments_032301.json:
```json
{
    "body": "Attachment [sage-trac4388.patch](tarball://root/attachments/some-uuid/ticket4388/sage-trac4388.patch) by cremona created at 2008-10-30 18:46:03",
    "created_at": "2008-10-30T18:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4388#issuecomment-32301",
    "user": "cremona"
}
```

Attachment [sage-trac4388.patch](tarball://root/attachments/some-uuid/ticket4388/sage-trac4388.patch) by cremona created at 2008-10-30 18:46:03



---

archive/issue_comments_032302.json:
```json
{
    "body": "Patch sage-trac4388.patch attached (based on 3.2.alpha1).",
    "created_at": "2008-10-30T18:46:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4388#issuecomment-32302",
    "user": "cremona"
}
```

Patch sage-trac4388.patch attached (based on 3.2.alpha1).



---

archive/issue_comments_032303.json:
```json
{
    "body": "Looks good to me. I agree with was's statement that the concept of a basis matrix makes sense here, and that basis_matrix() should return this rather than an error; patch applies fine in 3.2.alpha1; and all doctests in sage/schemes/elliptic_curves pass.",
    "created_at": "2008-11-03T15:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4388#issuecomment-32303",
    "user": "davidloeffler"
}
```

Looks good to me. I agree with was's statement that the concept of a basis matrix makes sense here, and that basis_matrix() should return this rather than an error; patch applies fine in 3.2.alpha1; and all doctests in sage/schemes/elliptic_curves pass.



---

archive/issue_comments_032304.json:
```json
{
    "body": "Merged in Sage 3.2.alpha3",
    "created_at": "2008-11-04T14:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4388#issuecomment-32304",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha3



---

archive/issue_comments_032305.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-04T14:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4388",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4388#issuecomment-32305",
    "user": "mabshoff"
}
```

Resolution: fixed

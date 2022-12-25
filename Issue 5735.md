# Issue 5735: delete extended rationals and integers completely

archive/issues_005735.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nFrom David Roe:\n> And yes, I originally wrote Extended Integers and Extended Rationals when I\n> was writing lazy p-adics.  Since lazy p-adics aren't currently in good\n> enough shape to be turned on, I don't think any part of the sage library\n> uses Extended Integers or Extended Rationals.  Upon further reflection, I'm\n> not sure I even need them for lazy p-adics.  I don't know if it's a good\n> idea to just get rid of extended integers and rationals or not.\n```\n\n\n\n+1 to getting rid of them both.   Nobody knows what they are really, and they aren't needed, and they are probably partly broken given the bad coverage (at least of integer).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5735\n\n",
    "created_at": "2009-04-10T17:08:07Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "delete extended rationals and integers completely",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5735",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody


```
From David Roe:
> And yes, I originally wrote Extended Integers and Extended Rationals when I
> was writing lazy p-adics.  Since lazy p-adics aren't currently in good
> enough shape to be turned on, I don't think any part of the sage library
> uses Extended Integers or Extended Rationals.  Upon further reflection, I'm
> not sure I even need them for lazy p-adics.  I don't know if it's a good
> idea to just get rid of extended integers and rationals or not.
```



+1 to getting rid of them both.   Nobody knows what they are really, and they aren't needed, and they are probably partly broken given the bad coverage (at least of integer).


Issue created by migration from https://trac.sagemath.org/ticket/5735





---

archive/issue_comments_044726.json:
```json
{
    "body": "#2515 should be closed when this is done.",
    "created_at": "2009-04-10T17:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5735#issuecomment-44726",
    "user": "https://github.com/burcin"
}
```

#2515 should be closed when this is done.



---

archive/issue_comments_044727.json:
```json
{
    "body": "\n```\nRobert-Bradshaws-Laptop:~/sage/current/devel/sage-docday robert$ grep -r \"extended_integer_ring\" sage | grep -v \"rings/extended_\"\nsage/rings/all.py:from extended_integer_ring import ExtendedIntegerRing\nRobert-Bradshaws-Laptop:~/sage/current/devel/sage-docday robert$ grep -r \"extended_rational_field\" sage | grep -v \"rings/extended_\" \nsage/rings/all.py:from extended_rational_field import ExtendedRationalField\nsage/rings/padics/valuation.py:import sage.rings.extended_rational_field\nsage/rings/padics/valuation.py:QQe = sage.rings.extended_rational_field.ExtendedRationalField\nRobert-Bradshaws-Laptop:~/sage/current/devel/sage-docday robert$ grep -r \"ExtendedRationalField\" sage | grep -v \"rings/extended_\"sage/rings/all.py:from extended_rational_field import ExtendedRationalField\nsage/rings/padics/valuation.py:QQe = sage.rings.extended_rational_field.ExtendedRationalField\nsage/rings/rational_field.py:        sage: E = ExtendedRationalField\n```\n",
    "created_at": "2009-04-12T00:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5735#issuecomment-44727",
    "user": "https://github.com/robertwb"
}
```


```
Robert-Bradshaws-Laptop:~/sage/current/devel/sage-docday robert$ grep -r "extended_integer_ring" sage | grep -v "rings/extended_"
sage/rings/all.py:from extended_integer_ring import ExtendedIntegerRing
Robert-Bradshaws-Laptop:~/sage/current/devel/sage-docday robert$ grep -r "extended_rational_field" sage | grep -v "rings/extended_" 
sage/rings/all.py:from extended_rational_field import ExtendedRationalField
sage/rings/padics/valuation.py:import sage.rings.extended_rational_field
sage/rings/padics/valuation.py:QQe = sage.rings.extended_rational_field.ExtendedRationalField
Robert-Bradshaws-Laptop:~/sage/current/devel/sage-docday robert$ grep -r "ExtendedRationalField" sage | grep -v "rings/extended_"sage/rings/all.py:from extended_rational_field import ExtendedRationalField
sage/rings/padics/valuation.py:QQe = sage.rings.extended_rational_field.ExtendedRationalField
sage/rings/rational_field.py:        sage: E = ExtendedRationalField
```




---

archive/issue_comments_044728.json:
```json
{
    "body": "Attachment [5735-remove-extended-QQ-ZZ.patch](tarball://root/attachments/some-uuid/ticket5735/5735-remove-extended-QQ-ZZ.patch) by @robertwb created at 2009-04-12 00:33:21\n\nI've removed these files, it only required two minor changes outside of this removal (padic valuation and a coercion test). All doctests in piadics pass.",
    "created_at": "2009-04-12T00:33:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5735#issuecomment-44728",
    "user": "https://github.com/robertwb"
}
```

Attachment [5735-remove-extended-QQ-ZZ.patch](tarball://root/attachments/some-uuid/ticket5735/5735-remove-extended-QQ-ZZ.patch) by @robertwb created at 2009-04-12 00:33:21

I've removed these files, it only required two minor changes outside of this removal (padic valuation and a coercion test). All doctests in piadics pass.



---

archive/issue_comments_044729.json:
```json
{
    "body": "Hmm, this patch fails to apply:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-3.4.1.rc3/devel/sage$ hg import 5735-remove-extended-QQ-ZZ.patch \napplying 5735-remove-extended-QQ-ZZ.patch\npatching file sage/rings/extended_rational_field.py\nHunk #1 FAILED at 0\n1 out of 1 hunks FAILED -- saving rejects to file sage/rings/extended_rational_field.py.rej\nabort: patch failed to apply\n```\n\nIt should be trivial to fix since this hunk just deletes extended_rational_field.py.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-12T20:23:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5735#issuecomment-44729",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmm, this patch fails to apply:

```
mabshoff@sage:/scratch/mabshoff/sage-3.4.1.rc3/devel/sage$ hg import 5735-remove-extended-QQ-ZZ.patch 
applying 5735-remove-extended-QQ-ZZ.patch
patching file sage/rings/extended_rational_field.py
Hunk #1 FAILED at 0
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/extended_rational_field.py.rej
abort: patch failed to apply
```

It should be trivial to fix since this hunk just deletes extended_rational_field.py.

Cheers,

Michael



---

archive/issue_comments_044730.json:
```json
{
    "body": "Attachment [trac_5735-remove-extended-QQ-ZZ.patch](tarball://root/attachments/some-uuid/ticket5735/trac_5735-remove-extended-QQ-ZZ.patch) by mabshoff created at 2009-04-12 20:39:23",
    "created_at": "2009-04-12T20:39:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5735#issuecomment-44730",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5735-remove-extended-QQ-ZZ.patch](tarball://root/attachments/some-uuid/ticket5735/trac_5735-remove-extended-QQ-ZZ.patch) by mabshoff created at 2009-04-12 20:39:23



---

archive/issue_comments_044731.json:
```json
{
    "body": "trac_5735-remove-extended-QQ-ZZ.patch is the rebased patch which was needed since John Cremona added some code to ExtendedRationalField. Since that file was completely deleted the rebase was trivial :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-12T20:40:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5735#issuecomment-44731",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

trac_5735-remove-extended-QQ-ZZ.patch is the rebased patch which was needed since John Cremona added some code to ExtendedRationalField. Since that file was completely deleted the rebase was trivial :)

Cheers,

Michael



---

archive/issue_comments_044732.json:
```json
{
    "body": "Merged trac_5735-remove-extended-QQ-ZZ.patch in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-12T20:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5735#issuecomment-44732",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_5735-remove-extended-QQ-ZZ.patch in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_044733.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-12T20:41:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5735#issuecomment-44733",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044734.json:
```json
{
    "body": "Mhh, a complete rebuild of the Sage library exposes this issue:\n\n```\nsage -t  \"devel/sage/sage/structure/sage_object.pyx\"        \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/sage/structure/sage_object.pyx\", line 715:\n    sage: sage.structure.sage_object.unpickle_all(std)\nExpected:\n    doctest:...: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.\n    Successfully unpickled 487 objects.\n    Failed to unpickle 0 objects.\nGot:\n    ** failed:  _class__sage_rings_extended_rational_field_ExtendedRationalField_class__.sobj\n    ** failed:  _class__sage_rings_extended_rational_field_Q_to_ExtendedQ__.sobj\n    ** failed:  _class__sage_rings_extended_rational_field_RationalMinusInfinity__.sobj\n    ** failed:  _class__sage_rings_extended_rational_field_RationalPlusInfinity__.sobj\n    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.\n    Failed:\n    _class__sage_rings_extended_rational_field_ExtendedRationalField_class__.sobj\n    _class__sage_rings_extended_rational_field_Q_to_ExtendedQ__.sobj\n    _class__sage_rings_extended_rational_field_RationalMinusInfinity__.sobj\n    _class__sage_rings_extended_rational_field_RationalPlusInfinity__.sobj\n    Successfully unpickled 483 objects.\n    Failed to unpickle 4 objects.\n**********************************************************************\n```\n\nRemoving those four files from the pickle jar fixes the issue.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T07:59:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5735#issuecomment-44734",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mhh, a complete rebuild of the Sage library exposes this issue:

```
sage -t  "devel/sage/sage/structure/sage_object.pyx"        
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc3/devel/sage/sage/structure/sage_object.pyx", line 715:
    sage: sage.structure.sage_object.unpickle_all(std)
Expected:
    doctest:...: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    Successfully unpickled 487 objects.
    Failed to unpickle 0 objects.
Got:
    ** failed:  _class__sage_rings_extended_rational_field_ExtendedRationalField_class__.sobj
    ** failed:  _class__sage_rings_extended_rational_field_Q_to_ExtendedQ__.sobj
    ** failed:  _class__sage_rings_extended_rational_field_RationalMinusInfinity__.sobj
    ** failed:  _class__sage_rings_extended_rational_field_RationalPlusInfinity__.sobj
    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    Failed:
    _class__sage_rings_extended_rational_field_ExtendedRationalField_class__.sobj
    _class__sage_rings_extended_rational_field_Q_to_ExtendedQ__.sobj
    _class__sage_rings_extended_rational_field_RationalMinusInfinity__.sobj
    _class__sage_rings_extended_rational_field_RationalPlusInfinity__.sobj
    Successfully unpickled 483 objects.
    Failed to unpickle 4 objects.
**********************************************************************
```

Removing those four files from the pickle jar fixes the issue.

Cheers,

Michael



---

archive/issue_comments_044735.json:
```json
{
    "body": "Attachment [trac_5735-pickle-number-fix.patch](tarball://root/attachments/some-uuid/ticket5735/trac_5735-pickle-number-fix.patch) by mabshoff created at 2009-04-13 08:14:05",
    "created_at": "2009-04-13T08:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5735#issuecomment-44735",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5735-pickle-number-fix.patch](tarball://root/attachments/some-uuid/ticket5735/trac_5735-pickle-number-fix.patch) by mabshoff created at 2009-04-13 08:14:05



---

archive/issue_comments_044736.json:
```json
{
    "body": "For the record: I merged  trac_5735-remove-extended-QQ-ZZ.patch and trac_5735-pickle-number-fix.patch and also checked in the changes to pickle_jar.tar.bz2 in data/extcode/pickle_jar/\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T08:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5735",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5735#issuecomment-44736",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the record: I merged  trac_5735-remove-extended-QQ-ZZ.patch and trac_5735-pickle-number-fix.patch and also checked in the changes to pickle_jar.tar.bz2 in data/extcode/pickle_jar/

Cheers,

Michael

# Issue 5735: delete extended rationals and integers completely

Issue created by migration from https://trac.sagemath.org/ticket/5735

Original creator: was

Original creation time: 2009-04-10 17:08:07

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



---

Comment by burcin created at 2009-04-10 17:34:58

#2515 should be closed when this is done.


---

Comment by robertwb created at 2009-04-12 00:20:41


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

Attachment

I've removed these files, it only required two minor changes outside of this removal (padic valuation and a coercion test). All doctests in piadics pass.


---

Comment by mabshoff created at 2009-04-12 20:23:44

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

Attachment


---

Comment by mabshoff created at 2009-04-12 20:40:52

trac_5735-remove-extended-QQ-ZZ.patch is the rebased patch which was needed since John Cremona added some code to ExtendedRationalField. Since that file was completely deleted the rebase was trivial :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-12 20:41:16

Merged trac_5735-remove-extended-QQ-ZZ.patch in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-12 20:41:16

Resolution: fixed


---

Comment by mabshoff created at 2009-04-13 07:59:44

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

Attachment


---

Comment by mabshoff created at 2009-04-13 08:15:02

For the record: I merged  trac_5735-remove-extended-QQ-ZZ.patch and trac_5735-pickle-number-fix.patch and also checked in the changes to pickle_jar.tar.bz2 in data/extcode/pickle_jar/

Cheers,

Michael

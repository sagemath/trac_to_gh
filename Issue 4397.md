# Issue 4397: Sage 3.1.4: optional doctest failure in sage/rings/number_field/number_field.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-10-30 17:03:16

Assignee: was


```
sage -t -long -optional devel/sage/sage/rings/number_field/number_field.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha1/tmp/number_field.py", line 2446:
    sage: NumberField(x^2+2, 'a').galois_group(pari_group=False)  # optional database_gap package
Expected:
    Galois group Transitive group number 1 of degree 2 of the Number Field in a with defining polynomial x^2 + 2
Got:
    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap packa
ge. Please install it.
    Galois group Transitive group number 1 of degree 2 of the Number Field in a with defining polynomial x^2 + 2
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha1/tmp/number_field.py", line 2448:
    sage: NumberField(x^3-2, 'a').galois_group(pari_group=False)  # optional database_gap package
Expected:
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 - 2
Got:
    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap packa
ge. Please install it.
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 - 2
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha1/tmp/number_field.py", line 2452:
    sage: NumberField(x^3 + 2*x + 1, 'a').galois_group(pari_group=False)
Expected:
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
Got:
    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap packa
ge. Please install it.
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha1/tmp/number_field.py", line 2454:
    sage: NumberField(x^3 + 2*x + 1, 'a').galois_group(algorithm='magma')   # optional -- requires magma
Expected:
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
Got:
    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap packa
ge. Please install it.
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1

**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha1/tmp/number_field.py", line 3395:
    sage: L               # optional
Expected:
    Number Field with defining polynomial t^2 + 1 over the Rational Field
Got:
    Number Field with defining polynomial $.1^2 + 1 over the Rational Field
**********************************************************************
```

This last Magma issue very much looks like the same problem as #4394.

Cheers,

Michael


---

Comment by was created at 2008-10-30 20:57:18

Everything works fine after the fixes for #4393, #4394, #4395 are applied and the database_gap package is installed.  All but the last error listed above is fixed by installing the database_gap package. 

I can't replicate the last error you get above, even without #4393-4395 installed.

I set the heading to "with patch; needs review", though there is no patch.


---

Comment by was created at 2008-10-30 20:57:54


```
teragon:number_field wstein$ sage -i database_gap-4.4.10
...
teragon:number_field wstein$ sage -t --optional --long number_field.py 
sage -t --optional --long devel/sage-bugday/sage/rings/number_field/number_field.py
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.

	 [26.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 26.2 seconds
teragon:number_field wstein$ 
```



---

Comment by mabshoff created at 2008-10-30 23:59:31

Resolution: invalid


---

Comment by mabshoff created at 2008-10-30 23:59:31

I think the solution here are the two extcode patches that were missing from #2171. With those two patches applied and the database_gap.spkg installed I get

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.3.final$ ./sage -t -long -optional devel/sage/sage/rings/number_field/number_field.py
sage -t -long -optional devel/sage/sage/rings/number_field/number_field.py
  ***   Warning: large Minkowski bound: certification will be VERY long.
  ***   Warning: large Minkowski bound: certification will be VERY long.

	 [45.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 45.4 seconds
```

Hence: Invalid, sorry for the noise.

Cheers,

Michael

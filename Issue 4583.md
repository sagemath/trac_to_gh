# Issue 4583: implement "sage -t --only-optional"

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-11-22 20:25:48

Assignee: mabshoff

I am going to implement exactly one thing for this ticket:

I will add an option

```
   sage -t --only-optional=comma,separated,list,of,tags file1.py dir ...
```


This would run every doctest block where at least one line in the block contains 

```
# optional - set of tags that must be subset of those above
```


The complete block would run, but with any # optional's that don't have tags a subset of the input to sage -t removed. 

Also, there is one special case:

```
sage -t only-optional
```

with no tages.  In this case, every doctest block that contains any # optional's is run.  All others are skipped. 

This design is joint work with Michael Abshoff.


---

Attachment

apply to the local/bin/ scripts repo.


---

Attachment

this rolls out using # optional - foo for most of the magma, macaulay2 and mathematica doctests.  It changes a *LOT* of files.  Note -- the optional doctests for those components may not pass (e.g., the magma ones won't), because it is already known that many optional doctests have bitrotted.  Fixing this is the subject of another ticket.  Note, in a few cases I increased doctest coverage, since I saw functions with no doctests at all.


---

Attachment


---

Attachment

this finishes the only_optional no args case


---

Comment by mabshoff created at 2008-11-23 02:55:52

With the first two Sage repo patches applied I am seeing two issues #4590 and

```
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/number_field/number_field.py", line 2453:
    sage: NumberField(x^3 + 2*x + 1, 'a').galois_group(pari_group=False)
Expected:
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
Got:
    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1

**********************************************************************
```


Cheers,

Michael


---

Attachment

sage-4583-part3.patch fixes the above issue with sage/rings/number_field/number_field.py I mentioned above.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-23 03:46:33

I really like this patch :)

So far everything I tried works well. The patch seems to expose some small issues like the ones below:

```
age -t -only-optional=magma devel/sage/sage/rings/number_field/number_field.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/number_field/number_field.py", line 2452:
    sage: x = polygen(QQ)
Expected:
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
Got nothing
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/number_field/number_field.py", line 2455:
    sage: NumberField(x^3 + 2*x + 1, 'a').galois_group(algorithm='magma')   # optional - magma
Expected:
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
Got:
    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
**********************************************************************
```

I.e. the last test should depend on Magma and database_gap. But all these little bugs can be addressed via follow up patches, so I am giving this patch a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-23 04:19:57

Resolution: fixed


---

Comment by mabshoff created at 2008-11-23 04:19:57

Merged all five patches in Sage 3.2.1.alpha0

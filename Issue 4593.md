# Issue 4593: do not uncinditionally use M2 for Gbasis computations over ZZ if it is installed

Issue created by migration from https://trac.sagemath.org/ticket/4593

Original creator: mabshoff

Original creation time: 2008-11-23 04:59:19

Assignee: malb

This is a left over from #4589: The doctest below from sage/rings/polynomial/multi_polynomial_ideal.py changes depending on whether M2 is installed or not since the GBasis computation uses the optional M2 if it is installed. But the interface should offer an option what code is used since results should not vary depending on optional spkg

```
@@ -164,7 +166,7 @@

         sage: I.change_ring(P.change_ring( IntegerModRing(2*7) )).groebner_basis()
         verbose 0 (...: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to very slow toy implementation.
-        [x + y + z, y^2 + y + 8, y*z + y + 2, 2*y + 6, z^2 + 3, 2*z + 10]
+        [x + y + z^3 + z^2 + 11, y^2 + y + 5*z^3 + 2*z^2 + 3*z + 10, y*z + y + 9*z^3 + 5*z^2 + 9*z + 11, 2*y + 2*z^3 + 4*z^2 + 4*z + 8, z^2 + 3, 2*z + 10]

     Modulo any other prime the Groebner basis is trivial so there are
     no other solutions. For example:
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-12-01 06:25:29

I have also made the other doctest "optional - m2" since I have been seeing the following failure:

```
File "/Users/mabshoff/sage-3.2.1.alpha2/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py", line 145:
    sage: I.groebner_basis()
Expected:
    verbose 0 ... Warning: falling back to very slow toy implementation.
    [x + y + z, y^2 + y + 23234, y*z + y + 26532, 2*y + 158864, z^2 + 17223, 2*z + 41856, 164878]
Got:
    verbose 0 (1792: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to very slow toy implementation.
    [x + y + 3*z + 206734, y^2 + y + 2*z + 65090, y*z + y + 26532, 2*y + 158864, z^2 + 2*z + 223957, 2*z + 206734, 164878]
```

This is on varro, i.e. the MacOSX 10.4 box on SkyNet.

Cheers,

Michael


---

Comment by was created at 2008-12-23 20:05:11

Changing priority from critical to blocker.


---

Comment by was created at 2008-12-23 20:34:33

For the record, thinking about this, it does seem stupid to not just use M2 when it is available, just because we can't proper doctest this.    A natural way to fix this would be to make the output random, get rid of the verbose warning altogether, and include an extra example that is marked

```
   # optional -- macaulay2
```


I think *all* warnings about "using slow toy implementations" for any algorithm in sage should use some sort of unified framework, which is different (but related to) the verbose flag.  E.g., each slow function would at the start call a function defined in misc:

```
   slow("Groebner over ZZ -- install M2 to speed this up")
```

This would print a warning iff a certain flag is set, which would be off by default.

It would be good to add calls like that everywhere e.g., in the base classes for matrices and other places where we have "slow generic code".  Then when people run code, they can set the flag and see a list of messages indicating exactly what they need to do to eliminate generic code from that a given code path, which would tip them off about how to speed up their code. 

Obviously, this has to be done carefully.  E.g., it would be bad to put slow(...) in the matrix __getitem__ method, since that would slow the __getitem__ method itself down. 


 -- William


---

Comment by mabshoff created at 2008-12-23 20:42:55

I am pretty sure that the generic framework for slow generic code should be its own ticket, but I really do like the idea.

Moving to 3.2.3, too :)

Cheers,

Michael


---

Comment by was created at 2008-12-24 01:58:35

> I am pretty sure that the generic framework for slow generic code should be its own 
> ticket, but I really do like the idea.

I strongly agree that it should be another ticket.


---

Comment by mabshoff created at 2008-12-26 17:31:54

For the record: The two failures listed above already are optional, so I asked Jaap who has been seeing those failure to open another ticket in case they are still around.

Since we will not be fixing the fundamental problem here in 3.2.2 I am reassigning this to 3.4.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-26 17:44:44

The ticket to make another test optional for now until this is resolved is #4882

Cheers,

Michael


---

Comment by malb created at 2009-01-23 07:40:16

disables default M2 if avaiable


---

Attachment


---

Comment by mabshoff created at 2009-02-03 17:52:13

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-03 17:53:44

Resolution: fixed


---

Comment by mabshoff created at 2009-02-03 17:53:44

Merged in Sage 3.3.alpha5.

Cheers,

Michael

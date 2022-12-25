# Issue 4593: do not uncinditionally use M2 for Gbasis computations over ZZ if it is installed

archive/issues_004593.json:
```json
{
    "body": "Assignee: @malb\n\nThis is a left over from #4589: The doctest below from sage/rings/polynomial/multi_polynomial_ideal.py changes depending on whether M2 is installed or not since the GBasis computation uses the optional M2 if it is installed. But the interface should offer an option what code is used since results should not vary depending on optional spkg\n\n```\n@@ -164,7 +166,7 @@\n\n         sage: I.change_ring(P.change_ring( IntegerModRing(2*7) )).groebner_basis()\n         verbose 0 (...: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to very slow toy implementation.\n-        [x + y + z, y^2 + y + 8, y*z + y + 2, 2*y + 6, z^2 + 3, 2*z + 10]\n+        [x + y + z^3 + z^2 + 11, y^2 + y + 5*z^3 + 2*z^2 + 3*z + 10, y*z + y + 9*z^3 + 5*z^2 + 9*z + 11, 2*y + 2*z^3 + 4*z^2 + 4*z + 8, z^2 + 3, 2*z + 10]\n\n     Modulo any other prime the Groebner basis is trivial so there are\n     no other solutions. For example:\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4593\n\n",
    "created_at": "2008-11-23T04:59:19Z",
    "labels": [
        "component: commutative algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "do not uncinditionally use M2 for Gbasis computations over ZZ if it is installed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4593",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @malb

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

Issue created by migration from https://trac.sagemath.org/ticket/4593





---

archive/issue_comments_034378.json:
```json
{
    "body": "I have also made the other doctest \"optional - m2\" since I have been seeing the following failure:\n\n```\nFile \"/Users/mabshoff/sage-3.2.1.alpha2/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\", line 145:\n    sage: I.groebner_basis()\nExpected:\n    verbose 0 ... Warning: falling back to very slow toy implementation.\n    [x + y + z, y^2 + y + 23234, y*z + y + 26532, 2*y + 158864, z^2 + 17223, 2*z + 41856, 164878]\nGot:\n    verbose 0 (1792: multi_polynomial_ideal.py, groebner_basis) Warning: falling back to very slow toy implementation.\n    [x + y + 3*z + 206734, y^2 + y + 2*z + 65090, y*z + y + 26532, 2*y + 158864, z^2 + 2*z + 223957, 2*z + 206734, 164878]\n```\n\nThis is on varro, i.e. the MacOSX 10.4 box on SkyNet.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-01T06:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4593#issuecomment-34378",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

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

archive/issue_comments_034379.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2008-12-23T20:05:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4593#issuecomment-34379",
    "user": "https://github.com/williamstein"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_034380.json:
```json
{
    "body": "For the record, thinking about this, it does seem stupid to not just use M2 when it is available, just because we can't proper doctest this.    A natural way to fix this would be to make the output random, get rid of the verbose warning altogether, and include an extra example that is marked\n\n```\n   # optional -- macaulay2\n```\n\n\nI think *all* warnings about \"using slow toy implementations\" for any algorithm in sage should use some sort of unified framework, which is different (but related to) the verbose flag.  E.g., each slow function would at the start call a function defined in misc:\n\n```\n   slow(\"Groebner over ZZ -- install M2 to speed this up\")\n```\n\nThis would print a warning iff a certain flag is set, which would be off by default.\n\nIt would be good to add calls like that everywhere e.g., in the base classes for matrices and other places where we have \"slow generic code\".  Then when people run code, they can set the flag and see a list of messages indicating exactly what they need to do to eliminate generic code from that a given code path, which would tip them off about how to speed up their code. \n\nObviously, this has to be done carefully.  E.g., it would be bad to put slow(...) in the matrix __getitem__ method, since that would slow the __getitem__ method itself down. \n\n\n -- William",
    "created_at": "2008-12-23T20:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4593#issuecomment-34380",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_034381.json:
```json
{
    "body": "I am pretty sure that the generic framework for slow generic code should be its own ticket, but I really do like the idea.\n\nMoving to 3.2.3, too :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-23T20:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4593#issuecomment-34381",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am pretty sure that the generic framework for slow generic code should be its own ticket, but I really do like the idea.

Moving to 3.2.3, too :)

Cheers,

Michael



---

archive/issue_comments_034382.json:
```json
{
    "body": "> I am pretty sure that the generic framework for slow generic code should be its own \n> ticket, but I really do like the idea.\n\nI strongly agree that it should be another ticket.",
    "created_at": "2008-12-24T01:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4593#issuecomment-34382",
    "user": "https://github.com/williamstein"
}
```

> I am pretty sure that the generic framework for slow generic code should be its own 
> ticket, but I really do like the idea.

I strongly agree that it should be another ticket.



---

archive/issue_comments_034383.json:
```json
{
    "body": "For the record: The two failures listed above already are optional, so I asked Jaap who has been seeing those failure to open another ticket in case they are still around.\n\nSince we will not be fixing the fundamental problem here in 3.2.2 I am reassigning this to 3.4.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-26T17:31:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4593#issuecomment-34383",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the record: The two failures listed above already are optional, so I asked Jaap who has been seeing those failure to open another ticket in case they are still around.

Since we will not be fixing the fundamental problem here in 3.2.2 I am reassigning this to 3.4.

Cheers,

Michael



---

archive/issue_comments_034384.json:
```json
{
    "body": "The ticket to make another test optional for now until this is resolved is #4882\n\nCheers,\n\nMichael",
    "created_at": "2008-12-26T17:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4593#issuecomment-34384",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The ticket to make another test optional for now until this is resolved is #4882

Cheers,

Michael



---

archive/issue_comments_034385.json:
```json
{
    "body": "disables default M2 if avaiable",
    "created_at": "2009-01-23T07:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4593#issuecomment-34385",
    "user": "https://github.com/malb"
}
```

disables default M2 if avaiable



---

archive/issue_comments_034386.json:
```json
{
    "body": "Attachment [m2.patch](tarball://root/attachments/some-uuid/ticket4593/m2.patch) by @malb created at 2009-01-23 07:40:42",
    "created_at": "2009-01-23T07:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4593#issuecomment-34386",
    "user": "https://github.com/malb"
}
```

Attachment [m2.patch](tarball://root/attachments/some-uuid/ticket4593/m2.patch) by @malb created at 2009-01-23 07:40:42



---

archive/issue_comments_034387.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T17:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4593#issuecomment-34387",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_events_004842.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-03T17:53:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4593",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4593#event-4842"
}
```



---

archive/issue_comments_034388.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-03T17:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4593#issuecomment-34388",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034389.json:
```json
{
    "body": "Merged in Sage 3.3.alpha5.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T17:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4593",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4593#issuecomment-34389",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha5.

Cheers,

Michael

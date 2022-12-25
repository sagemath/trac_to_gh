# Issue 6993: [with package, needs review] update pynac to 0.1.9

archive/issues_006993.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @williamstein @mwhansen @ncalexan\n\nNew pynac package available at:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.9.spkg\n\nChanges to pynac can also be viewed by going here:\n\nhttp://pynac.sagemath.org/hg/rev/beb49aa3cebf\n\nand clicking the link for \"children\" to see the other patches.\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6993\n\n",
    "created_at": "2009-09-22T19:18:06Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with package, needs review] update pynac to 0.1.9",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6993",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

CC:  @williamstein @mwhansen @ncalexan

New pynac package available at:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.9.spkg

Changes to pynac can also be viewed by going here:

http://pynac.sagemath.org/hg/rev/beb49aa3cebf

and clicking the link for "children" to see the other patches.





Issue created by migration from https://trac.sagemath.org/ticket/6993





---

archive/issue_comments_057730.json:
```json
{
    "body": "Attachment [trac_6993-revert_evalf.patch](tarball://root/attachments/some-uuid/ticket6993/trac_6993-revert_evalf.patch) by @burcin created at 2009-09-22 19:26:03\n\nThis package includes corresponding changes for the tickets:\n\n* #6948 powers of exp are over simplified\n* #6902 log(x) is typeset as \\ln x\n* #6851 hashes for derivatives of symbolic functions still collide\n* #6524 Ratio of two symbolic expressions involving derivative does not simplify\n* #6992 rename lngamma to log gamma\n\nThe patch attached to this ticket is just an enhancement. It is the first step to cleaning up the interface for symbolic functions. Pynac now evaluates symbolic functions on non-exact input again. This eliminates the need for a separate `__call__` method in `sage.symbolic.function.PrimitiveFunction`.",
    "created_at": "2009-09-22T19:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6993#issuecomment-57730",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6993-revert_evalf.patch](tarball://root/attachments/some-uuid/ticket6993/trac_6993-revert_evalf.patch) by @burcin created at 2009-09-22 19:26:03

This package includes corresponding changes for the tickets:

* #6948 powers of exp are over simplified
* #6902 log(x) is typeset as \ln x
* #6851 hashes for derivatives of symbolic functions still collide
* #6524 Ratio of two symbolic expressions involving derivative does not simplify
* #6992 rename lngamma to log gamma

The patch attached to this ticket is just an enhancement. It is the first step to cleaning up the interface for symbolic functions. Pynac now evaluates symbolic functions on non-exact input again. This eliminates the need for a separate `__call__` method in `sage.symbolic.function.PrimitiveFunction`.



---

archive/issue_comments_057731.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-22T19:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6993#issuecomment-57731",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_057732.json:
```json
{
    "body": "There are a lot of other doctest failures caused by this package than the ones fixed above.  It is possible that some are spurious because I missed something in the tickets listed above, but I will post them here for now.\n Ones not covered elsewhere I describe.\n\tsage -t  \"devel/sage/sage/calculus/calculus.py\"\n\tsage -t  \"devel/sage/sage/calculus/desolvers.py\"\n\tsage -t  \"devel/sage/sage/calculus/functional.py\"\n\tsage -t  \"devel/sage/sage/calculus/functions.py\"\n\tsage -t  \"devel/sage/sage/functions/log.py\"\n\tsage -t  \"devel/sage/sage/calculus/tests.py\"\nAll of these are just order switches and should be trivial to fix.\n\n\tsage -t  \"devel/sage/sage/calculus/wester.py\"\n\n```\n    sage: print RealField(150)(a)\nExpected:\n    2.6253741264076874399999999999925007259719820e17\nGot:\n    2.6253741264076874399999999999925007259719819e17\n*********************************************************************\t\n    sage: taylor(log(x)^a*exp(-b*x), x, 1, 3)\nExpected:\n    -1/48*(x - 1)^3*((6*b + 5)*(x - 1)^a*a^2 + (x - 1)^a*a^3 + 8*(x - 1)^a*b^3 + 2*(6*b^2 + 5*b + 3)*(x - 1)^a*a)*e^(-b) + 1/24*(x - 1)^2*((12*b + 5)*(x - 1)^a*a + 3*(x - 1)^a*a^2 + 12*(x - 1)^a*b^2)*e^(-b) - 1/2*(x - 1)*((x - 1)^a*a + 2*(x - 1)^a*b)*e^(-b) + (x - 1)^a*e^(-b)\nGot:\n    -1/48*(x - 1)^3*((6*b + 5)*(x - 1)^a*a^2 + (x - 1)^a*a^3 + 8*(x - 1)^a*b^3 + 2*(6*b^2 + 5*b + 3)*(x - 1)^a*a)/e^b + 1/24*(x - 1)^2*((12*b + 5)*(x - 1)^a*a + 3*(x - 1)^a*a^2 + 12*(x - 1)^a*b^2)/e^b - 1/2*(x - 1)*((x - 1)^a*a + 2*(x - 1)^a*b)/e^b + (x - 1)^a/e^b\n*********************************************************************\n```\n\n\tsage -t  \"devel/sage/sage/symbolic/expression.pyx\"\n\tsage -t  \"devel/sage/sage/symbolic/expression_conversions.py\"\nBoth of these have a problem with QQbar(e^(pi*I/3)).  This is definitely an algebraic number, so hopefully it's covered elsewhere.  Specifically,\n\n```\nges/sage/symbolic/expression_conversions.pyc in composition(self, ex, operator)\n    729             if rat_arg == 0:\n    730                 # here we will either try and simplify, or return\n--> 731                 raise ValueError, \"Unable to represent as an algebraic number.\"\n    732             real = operand.real()\n    733             if real:\n\nValueError: Unable to represent as an algebraic number.\n```\n\n\tsage -t  \"devel/sage/sage/symbolic/relation.py\"\nThis is:\n\n```\n   sage: eq._maxima_init_()\nExpected:\n    '(x)^(3/5) >= ((%pi)^(2))+(exp(0+%i*1))'\nGot:\n    '(x)^(3/5) >= ((%pi)^(2))+((exp(1))^(0+%i*1))'\n******\n   sage: solve(f==0,x)\nExpected:\n    [x == (-a)^(1/5)*e^(2/5*I*pi), x == (-a)^(1/5)*e^(4/5*I*pi), x == (-a)^(1/5)*e^(-4/5*I*pi), x == (-a)^(1/5)*e^(-2/5*I*pi), x == (-a)^(1/5)]\nGot:\n    [x == e^(2/5*I*pi)*(-a)^(1/5), x == e^(4/5*I*pi)*(-a)^(1/5), x == e^(-4/5*I*pi)*(-a)^(1/5), x == e^(-2/5*I*pi)*(-a)^(1/5), x == (-a)^(1/5)]\n**********************************************************************\n```\n",
    "created_at": "2009-09-23T02:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6993#issuecomment-57732",
    "user": "https://github.com/kcrisman"
}
```

There are a lot of other doctest failures caused by this package than the ones fixed above.  It is possible that some are spurious because I missed something in the tickets listed above, but I will post them here for now.
 Ones not covered elsewhere I describe.
	sage -t  "devel/sage/sage/calculus/calculus.py"
	sage -t  "devel/sage/sage/calculus/desolvers.py"
	sage -t  "devel/sage/sage/calculus/functional.py"
	sage -t  "devel/sage/sage/calculus/functions.py"
	sage -t  "devel/sage/sage/functions/log.py"
	sage -t  "devel/sage/sage/calculus/tests.py"
All of these are just order switches and should be trivial to fix.

	sage -t  "devel/sage/sage/calculus/wester.py"

```
    sage: print RealField(150)(a)
Expected:
    2.6253741264076874399999999999925007259719820e17
Got:
    2.6253741264076874399999999999925007259719819e17
*********************************************************************	
    sage: taylor(log(x)^a*exp(-b*x), x, 1, 3)
Expected:
    -1/48*(x - 1)^3*((6*b + 5)*(x - 1)^a*a^2 + (x - 1)^a*a^3 + 8*(x - 1)^a*b^3 + 2*(6*b^2 + 5*b + 3)*(x - 1)^a*a)*e^(-b) + 1/24*(x - 1)^2*((12*b + 5)*(x - 1)^a*a + 3*(x - 1)^a*a^2 + 12*(x - 1)^a*b^2)*e^(-b) - 1/2*(x - 1)*((x - 1)^a*a + 2*(x - 1)^a*b)*e^(-b) + (x - 1)^a*e^(-b)
Got:
    -1/48*(x - 1)^3*((6*b + 5)*(x - 1)^a*a^2 + (x - 1)^a*a^3 + 8*(x - 1)^a*b^3 + 2*(6*b^2 + 5*b + 3)*(x - 1)^a*a)/e^b + 1/24*(x - 1)^2*((12*b + 5)*(x - 1)^a*a + 3*(x - 1)^a*a^2 + 12*(x - 1)^a*b^2)/e^b - 1/2*(x - 1)*((x - 1)^a*a + 2*(x - 1)^a*b)/e^b + (x - 1)^a/e^b
*********************************************************************
```

	sage -t  "devel/sage/sage/symbolic/expression.pyx"
	sage -t  "devel/sage/sage/symbolic/expression_conversions.py"
Both of these have a problem with QQbar(e^(pi*I/3)).  This is definitely an algebraic number, so hopefully it's covered elsewhere.  Specifically,

```
ges/sage/symbolic/expression_conversions.pyc in composition(self, ex, operator)
    729             if rat_arg == 0:
    730                 # here we will either try and simplify, or return
--> 731                 raise ValueError, "Unable to represent as an algebraic number."
    732             real = operand.real()
    733             if real:

ValueError: Unable to represent as an algebraic number.
```

	sage -t  "devel/sage/sage/symbolic/relation.py"
This is:

```
   sage: eq._maxima_init_()
Expected:
    '(x)^(3/5) >= ((%pi)^(2))+(exp(0+%i*1))'
Got:
    '(x)^(3/5) >= ((%pi)^(2))+((exp(1))^(0+%i*1))'
******
   sage: solve(f==0,x)
Expected:
    [x == (-a)^(1/5)*e^(2/5*I*pi), x == (-a)^(1/5)*e^(4/5*I*pi), x == (-a)^(1/5)*e^(-4/5*I*pi), x == (-a)^(1/5)*e^(-2/5*I*pi), x == (-a)^(1/5)]
Got:
    [x == e^(2/5*I*pi)*(-a)^(1/5), x == e^(4/5*I*pi)*(-a)^(1/5), x == e^(-4/5*I*pi)*(-a)^(1/5), x == e^(-2/5*I*pi)*(-a)^(1/5), x == (-a)^(1/5)]
**********************************************************************
```




---

archive/issue_comments_057733.json:
```json
{
    "body": "I think you should have been more explicit about how to test this - it wasn't clear that all the patches were necessary to avoid doctest issues.  I checked and I think they must all have been related to powers of exp.\n\nAnyway, relevant tests pass, the \"children\" were easy to follow, so the only thing (possibly) hindering positive review is the parenthesis issue in #6948.",
    "created_at": "2009-09-23T20:58:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6993#issuecomment-57733",
    "user": "https://github.com/kcrisman"
}
```

I think you should have been more explicit about how to test this - it wasn't clear that all the patches were necessary to avoid doctest issues.  I checked and I think they must all have been related to powers of exp.

Anyway, relevant tests pass, the "children" were easy to follow, so the only thing (possibly) hindering positive review is the parenthesis issue in #6948.



---

archive/issue_comments_057734.json:
```json
{
    "body": "New package here: \n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.9.p0.spkg\n\nIncludes printing fixes for #6948.",
    "created_at": "2009-09-24T06:35:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6993#issuecomment-57734",
    "user": "https://github.com/burcin"
}
```

New package here: 

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.9.p0.spkg

Includes printing fixes for #6948.



---

archive/issue_comments_057735.json:
```json
{
    "body": "Positive review!  Great.  My only complaint is that Pynac is not on the Sage revision control system, so it's both difficult to look at (hence, thanks for the link to the changesets) and difficult to fix symbolic issues in Sage that really \"should\" live in Pynac.\n\nTo release manager: apply .p0 package first, then the tickets listed above in reverse numerical order, with #6948 ticket applying first the regular patch, then the print patch.  I think that should be the correct order, and should lead to no new doctest failures.  (In actual fact, I think that only the patch on this ticket needs to be applied before the others, but that's the order that worked for me.)",
    "created_at": "2009-09-24T13:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6993#issuecomment-57735",
    "user": "https://github.com/kcrisman"
}
```

Positive review!  Great.  My only complaint is that Pynac is not on the Sage revision control system, so it's both difficult to look at (hence, thanks for the link to the changesets) and difficult to fix symbolic issues in Sage that really "should" live in Pynac.

To release manager: apply .p0 package first, then the tickets listed above in reverse numerical order, with #6948 ticket applying first the regular patch, then the print patch.  I think that should be the correct order, and should lead to no new doctest failures.  (In actual fact, I think that only the patch on this ticket needs to be applied before the others, but that's the order that worked for me.)



---

archive/issue_events_007217.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-09-25T22:43:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6993",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6993#event-7217"
}
```



---

archive/issue_comments_057736.json:
```json
{
    "body": "Merged `pynac-0.1.9.p0.spkg` in the standard packages repository. Merged `trac_6993-revert_evalf.patch` in the Sage library.",
    "created_at": "2009-09-25T22:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6993#issuecomment-57736",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged `pynac-0.1.9.p0.spkg` in the standard packages repository. Merged `trac_6993-revert_evalf.patch` in the Sage library.



---

archive/issue_comments_057737.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-25T22:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6993#issuecomment-57737",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057738.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6993#issuecomment-57738",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.

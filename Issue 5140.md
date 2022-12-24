# Issue 5140: is_irreducible() reports units as irreducible

archive/issues_005140.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: is_irreducible\n\n# Description of the bug\nThe following happens with\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n```\n\n| SAGE Version 3.1.2, Release Date: 2008-09-19                       |\n| Type notebook() for the GUI, and license() for information.        |\n**The function is_irreducible returns True on units:**\n\n```\nsage: R.<x>=PolynomialRing( IntegerModRing(13),'x')\nsage: (x^2-2).is_irreducible()\nTrue\nsage: (x^2).is_irreducible()\nFalse\nsage: R(1).is_irreducible()\nTrue\n```\n\nThe last line should say False or raise an exception as R(0).is_irreducible() does. Because irreducibility of B requires B to be not zero and not a unit. \n\n# Use case where this bug occured to me\n\nIf I want to loop over polynomials in R and count irreducible ones, I need a loop like this:\n\n```\nfor p in R.polynomials(max_degree=3):\n     if not p.is_zero() and not p.is_unit() and p.is_irreducible():\n         # count p\n```\n\nIt is easy to forget the check if p is a unit. Then the count would be wrong. \n\n# Bug-Fix\nThe bug is in the implementation:\n\n```\ne=R(1)\ne.is_irreducible??\n```\n\nshows as code after the docstring: \n\n```\nif self.is_zero():\n            raise ValueError, \"self must be nonzero\"\nif self.degree() == 0:\n            return True\n```\n\n\n**I propose to insert a check**\n\n```\nif self.is_unit():\n            raise ValueError, \"self must not be a unit\"\n```\n\nbetween the above ifs. I created a file via commit and  bundle with this modification. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5140\n\n",
    "created_at": "2009-01-30T21:15:34Z",
    "labels": [
        "algebra",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "is_irreducible() reports units as irreducible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5140",
    "user": "lars.fischer"
}
```
Assignee: tbd

Keywords: is_irreducible

# Description of the bug
The following happens with

```
----------------------------------------------------------------------
----------------------------------------------------------------------
```

| SAGE Version 3.1.2, Release Date: 2008-09-19                       |
| Type notebook() for the GUI, and license() for information.        |
**The function is_irreducible returns True on units:**

```
sage: R.<x>=PolynomialRing( IntegerModRing(13),'x')
sage: (x^2-2).is_irreducible()
True
sage: (x^2).is_irreducible()
False
sage: R(1).is_irreducible()
True
```

The last line should say False or raise an exception as R(0).is_irreducible() does. Because irreducibility of B requires B to be not zero and not a unit. 

# Use case where this bug occured to me

If I want to loop over polynomials in R and count irreducible ones, I need a loop like this:

```
for p in R.polynomials(max_degree=3):
     if not p.is_zero() and not p.is_unit() and p.is_irreducible():
         # count p
```

It is easy to forget the check if p is a unit. Then the count would be wrong. 

# Bug-Fix
The bug is in the implementation:

```
e=R(1)
e.is_irreducible??
```

shows as code after the docstring: 

```
if self.is_zero():
            raise ValueError, "self must be nonzero"
if self.degree() == 0:
            return True
```


**I propose to insert a check**

```
if self.is_unit():
            raise ValueError, "self must not be a unit"
```

between the above ifs. I created a file via commit and  bundle with this modification. 


Issue created by migration from https://trac.sagemath.org/ticket/5140





---

archive/issue_comments_039302.json:
```json
{
    "body": "Attachment [irred_bug_fix.bundle.hg](tarball://root/attachments/some-uuid/ticket5140/irred_bug_fix.bundle.hg) by lars.fischer created at 2009-01-30 21:16:31\n\nThe mentioned modification.",
    "created_at": "2009-01-30T21:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5140#issuecomment-39302",
    "user": "lars.fischer"
}
```

Attachment [irred_bug_fix.bundle.hg](tarball://root/attachments/some-uuid/ticket5140/irred_bug_fix.bundle.hg) by lars.fischer created at 2009-01-30 21:16:31

The mentioned modification.



---

archive/issue_comments_039303.json:
```json
{
    "body": "Lars,\n\nI am not so sure what you attached, but it does bot look like the change you describe. Please extract the commit for the fix and attach it as patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-30T22:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5140#issuecomment-39303",
    "user": "mabshoff"
}
```

Lars,

I am not so sure what you attached, but it does bot look like the change you describe. Please extract the commit for the fix and attach it as patch.

Cheers,

Michael



---

archive/issue_comments_039304.json:
```json
{
    "body": "Attachment [irred_bug_fix.export.patch](tarball://root/attachments/some-uuid/ticket5140/irred_bug_fix.export.patch) by lars.fischer created at 2009-01-31 13:11:13\n\nThe same patch via hg_sage.export().",
    "created_at": "2009-01-31T13:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5140#issuecomment-39304",
    "user": "lars.fischer"
}
```

Attachment [irred_bug_fix.export.patch](tarball://root/attachments/some-uuid/ticket5140/irred_bug_fix.export.patch) by lars.fischer created at 2009-01-31 13:11:13

The same patch via hg_sage.export().



---

archive/issue_comments_039305.json:
```json
{
    "body": "Hello Michael,\n\nI exported the modification and attached the file as irred_bug_fix.export.patch. \nSorry for the inconvenience.\n\nWith best regards,\nLars",
    "created_at": "2009-01-31T13:14:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5140#issuecomment-39305",
    "user": "lars.fischer"
}
```

Hello Michael,

I exported the modification and attached the file as irred_bug_fix.export.patch. 
Sorry for the inconvenience.

With best regards,
Lars



---

archive/issue_comments_039306.json:
```json
{
    "body": "Review:  I agree entirely that units need to be handled properly here, but I do not think that this patch solves the issue.  \n\nFirstly, I don't think that raising an error is necessary or helpful, and would prefer to return False for units.\n\nSecondly, you have left in the code which (now for non-units) returns True for degree 0 polynomials.  But that is wrong for polynomials over rings which are not fields such as ZZ[x], where 6 has degree 0, is not a unit but is not irreducible.  Instead, for degree 0 polynomials (which have already been handled by the is_unit() test) one should test irreducibility in the base ring.\n\nExample:\n\n```\nsage: R.<x>=ZZ[]\nsage: R(6).is_irreducible()\nTrue\n```\n\nis wrong, and it would be nice if the patch handled this also.\n\nLastly: Lars, when you make a patch to correct some incorrect behaviour in Sage you should add a doctest to the function which shows that the problem has been solved.",
    "created_at": "2009-02-01T15:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5140#issuecomment-39306",
    "user": "cremona"
}
```

Review:  I agree entirely that units need to be handled properly here, but I do not think that this patch solves the issue.  

Firstly, I don't think that raising an error is necessary or helpful, and would prefer to return False for units.

Secondly, you have left in the code which (now for non-units) returns True for degree 0 polynomials.  But that is wrong for polynomials over rings which are not fields such as ZZ[x], where 6 has degree 0, is not a unit but is not irreducible.  Instead, for degree 0 polynomials (which have already been handled by the is_unit() test) one should test irreducibility in the base ring.

Example:

```
sage: R.<x>=ZZ[]
sage: R(6).is_irreducible()
True
```

is wrong, and it would be nice if the patch handled this also.

Lastly: Lars, when you make a patch to correct some incorrect behaviour in Sage you should add a doctest to the function which shows that the problem has been solved.



---

archive/issue_comments_039307.json:
```json
{
    "body": "Changing priority from trivial to minor.",
    "created_at": "2009-02-01T15:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5140#issuecomment-39307",
    "user": "cremona"
}
```

Changing priority from trivial to minor.



---

archive/issue_comments_039308.json:
```json
{
    "body": "Attachment [trac_5140.patch](tarball://root/attachments/some-uuid/ticket5140/trac_5140.patch) by cremona created at 2009-02-01 16:12:58\n\nReplaces earlier patches; based on 3.3.alpha3",
    "created_at": "2009-02-01T16:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5140#issuecomment-39308",
    "user": "cremona"
}
```

Attachment [trac_5140.patch](tarball://root/attachments/some-uuid/ticket5140/trac_5140.patch) by cremona created at 2009-02-01 16:12:58

Replaces earlier patches; based on 3.3.alpha3



---

archive/issue_comments_039309.json:
```json
{
    "body": "Attachment [trac_5140_rebase.patch](tarball://root/attachments/some-uuid/ticket5140/trac_5140_rebase.patch) by cremona created at 2009-03-18 17:33:39\n\nReplaces all previous; based on 3.4",
    "created_at": "2009-03-18T17:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5140#issuecomment-39309",
    "user": "cremona"
}
```

Attachment [trac_5140_rebase.patch](tarball://root/attachments/some-uuid/ticket5140/trac_5140_rebase.patch) by cremona created at 2009-03-18 17:33:39

Replaces all previous; based on 3.4



---

archive/issue_comments_039310.json:
```json
{
    "body": "I have rebased this on 3.4.  Testing revealed a problem: Now that 1 is no longer reported as an irreducible element of ZZ[x] (as it used to be, amazingly), the quotient of ZZ[x] by the ideal (1) is not tagged as an integral domain, and then a doctest which tested the is_finite() function on that quotient failed since is_finite was always NotImplemented for general rings.\n\nTo solve this I implemented an is_zero() function for completely general rings (it just tests is the one_element() equals the zero_element(), and some small functions on general rings can now be decided if the ring is zero -- such as is_finite().\n\nI tested everything in sage/rings.",
    "created_at": "2009-03-18T17:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5140#issuecomment-39310",
    "user": "cremona"
}
```

I have rebased this on 3.4.  Testing revealed a problem: Now that 1 is no longer reported as an irreducible element of ZZ[x] (as it used to be, amazingly), the quotient of ZZ[x] by the ideal (1) is not tagged as an integral domain, and then a doctest which tested the is_finite() function on that quotient failed since is_finite was always NotImplemented for general rings.

To solve this I implemented an is_zero() function for completely general rings (it just tests is the one_element() equals the zero_element(), and some small functions on general rings can now be decided if the ring is zero -- such as is_finite().

I tested everything in sage/rings.



---

archive/issue_comments_039311.json:
```json
{
    "body": "Since John posted an updated patch I am marking this as \"needs review\". From the history it seems that there are some unresolved issues, so feel free to change it to \"needs work\".\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T06:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5140#issuecomment-39311",
    "user": "mabshoff"
}
```

Since John posted an updated patch I am marking this as "needs review". From the history it seems that there are some unresolved issues, so feel free to change it to "needs work".

Cheers,

Michael



---

archive/issue_comments_039312.json:
```json
{
    "body": "I just checked that my patch trac_5140_rebase.patch still applies fine to 3.4.rc0, and tests still pass.  That patch dealt with all the issues which I came up against when testing, so as far as I am concerned it is ready to go, but I agree that an independent reviewer is needed since I touched quite a few other things.  Anyone familiar with basic ring stuff could do it!",
    "created_at": "2009-04-06T10:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5140#issuecomment-39312",
    "user": "cremona"
}
```

I just checked that my patch trac_5140_rebase.patch still applies fine to 3.4.rc0, and tests still pass.  That patch dealt with all the issues which I came up against when testing, so as far as I am concerned it is ready to go, but I agree that an independent reviewer is needed since I touched quite a few other things.  Anyone familiar with basic ring stuff could do it!



---

archive/issue_comments_039313.json:
```json
{
    "body": "Replying to [comment:7 AlexGhitza]:  Thanks, Alex!",
    "created_at": "2009-04-09T08:45:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5140#issuecomment-39313",
    "user": "cremona"
}
```

Replying to [comment:7 AlexGhitza]:  Thanks, Alex!



---

archive/issue_comments_039314.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-09T09:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5140#issuecomment-39314",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039315.json:
```json
{
    "body": "Merged trac_5140_rebase.patch in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T09:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5140",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5140#issuecomment-39315",
    "user": "mabshoff"
}
```

Merged trac_5140_rebase.patch in Sage 3.4.1.rc2.

Cheers,

Michael

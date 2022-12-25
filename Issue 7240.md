# Issue 7240: factorization of Cunningham numbers - applications

archive/issues_007240.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jpflori @rwst\n\nFollowing #7239, use the factorization of Cunningham numbers to speed up polynomial primitivity testing and other finite field stuff (for small characteristic).\n\nIssue created by migration from https://trac.sagemath.org/ticket/7240\n\n",
    "created_at": "2009-10-18T10:35:29Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-pending",
    "title": "factorization of Cunningham numbers - applications",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7240",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```
Assignee: tbd

CC:  jpflori @rwst

Following #7239, use the factorization of Cunningham numbers to speed up polynomial primitivity testing and other finite field stuff (for small characteristic).

Issue created by migration from https://trac.sagemath.org/ticket/7240





---

archive/issue_comments_059962.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-26T21:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59962",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059963.json:
```json
{
    "body": "The patch applies fine to 4.3.rc0 after installing the optional spkg at #7239 and the patch there, and tests pass.  Good doctests included.\n\nBUT in both places where _cunningham_prime_factors() is called, a run-time error will be raised if the optional database is not installed.  If the database is really going to be optional then these calls must be wrapped with try/except, otherwise people who have not installed the optional package will find lots of their code fails.\n\nHence: needs work.",
    "created_at": "2009-12-18T17:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59963",
    "user": "https://github.com/JohnCremona"
}
```

The patch applies fine to 4.3.rc0 after installing the optional spkg at #7239 and the patch there, and tests pass.  Good doctests included.

BUT in both places where _cunningham_prime_factors() is called, a run-time error will be raised if the optional database is not installed.  If the database is really going to be optional then these calls must be wrapped with try/except, otherwise people who have not installed the optional package will find lots of their code fails.

Hence: needs work.



---

archive/issue_comments_059964.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-18T17:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59964",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059965.json:
```json
{
    "body": "In fact if the patch from #7239 is applied, but the database not installed, `_factor_cunningham` will just be the usual factor, with the first time it's called a warning (not an error) saying:\n\n\"You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``\"\n\nMoreover this warning will only be seen if the characteristic is `p \\in {2,3,5,7,11}` and `p^k > 2^100`. I thought it was nice to tell the user that there exists an optional package useful for them, but I can remove it if necessary.",
    "created_at": "2009-12-18T18:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59965",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

In fact if the patch from #7239 is applied, but the database not installed, `_factor_cunningham` will just be the usual factor, with the first time it's called a warning (not an error) saying:

"You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``"

Moreover this warning will only be seen if the characteristic is `p \in {2,3,5,7,11}` and `p^k > 2^100`. I thought it was nice to tell the user that there exists an optional package useful for them, but I can remove it if necessary.



---

archive/issue_comments_059966.json:
```json
{
    "body": "OK, that is more reasonable.   But why don't we (you!) put a case to sage-devel for including this spkg as standard?  It's only another 492837 bytes, and the cremona database is 78M.",
    "created_at": "2009-12-18T20:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59966",
    "user": "https://github.com/JohnCremona"
}
```

OK, that is more reasonable.   But why don't we (you!) put a case to sage-devel for including this spkg as standard?  It's only another 492837 bytes, and the cremona database is 78M.



---

archive/issue_comments_059967.json:
```json
{
    "body": "This ticket is marked as \"needs work\", but what should be done exactly?",
    "created_at": "2010-01-20T14:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59967",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

This ticket is marked as "needs work", but what should be done exactly?



---

archive/issue_comments_059968.json:
```json
{
    "body": "I set it to \"needs work\" but then agreed that it was good (but did not change the label).  On the other hand, there has been discussion on sage-devel in favour of including this as standard anyway.   \n\nSo I suggest that we give this a positive review.  This will take two steps....",
    "created_at": "2010-01-20T15:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59968",
    "user": "https://github.com/JohnCremona"
}
```

I set it to "needs work" but then agreed that it was good (but did not change the label).  On the other hand, there has been discussion on sage-devel in favour of including this as standard anyway.   

So I suggest that we give this a positive review.  This will take two steps....



---

archive/issue_comments_059969.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T15:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59969",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059970.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T15:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59970",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059971.json:
```json
{
    "body": "After applying the attachment [trac7240_Cunningham_factorization_application.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7240/trac7240_Cunningham_factorization_application.patch), I got the following doctest failures on Sage 4.3.1. In all of these cases, I didn't install the optional Cunningham spkg at #7239\n\n```\n[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/rings/finite_field_ntl_gf2e.pyx\nsage -t -long \"devel/sage-main/sage/rings/finite_field_ntl_gf2e.pyx\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/rings/finite_field_ntl_gf2e.pyx\", line 1349:\n    sage: b._gap_init_()\nExpected:\n    'Z(65536)^1'\nGot:\n    doctest:21: UserWarning: You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``\n    'Z(65536)^1'\n\n[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/rings/finite_field_element.py\nsage -t -long \"devel/sage-main/sage/rings/finite_field_element.py\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/rings/finite_field_element.py\", line 375:\n    sage: a.multiplicative_order()\nExpected:\n    124\nGot:\n    doctest:21: UserWarning: You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``\n    124\n\n[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/rings/finite_field_ext_pari.py\nsage -t -long \"devel/sage-main/sage/rings/finite_field_ext_pari.py\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/rings/finite_field_ext_pari.py\", line 103:\n    sage: z.multiplicative_order()\nExpected:\n    15\nGot:\n    doctest:21: UserWarning: You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``\n    15\n\n[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/rings/polynomial/polynomial_element.pyx\nsage -t -long \"devel/sage-main/sage/rings/polynomial/polynomial_element.pyx\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx\", line 2860:\n    sage: f.is_irreducible(), f.is_primitive()\nExpected:\n    (True, False)\nGot:\n    doctest:21: UserWarning: You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``\n    (True, False)\n\n[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/groups/generic.py\nsage -t -long \"devel/sage-main/sage/groups/generic.py\"      \n**********************************************************************\nFile \"/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/groups/generic.py\", line 774:\n    sage: discrete_log(u,g)\nExpected:\n    123456789\nGot:\n    doctest:21: UserWarning: You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``\n    123456789\n```\n",
    "created_at": "2010-01-22T17:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59971",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

After applying the attachment [trac7240_Cunningham_factorization_application.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7240/trac7240_Cunningham_factorization_application.patch), I got the following doctest failures on Sage 4.3.1. In all of these cases, I didn't install the optional Cunningham spkg at #7239

```
[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/rings/finite_field_ntl_gf2e.pyx
sage -t -long "devel/sage-main/sage/rings/finite_field_ntl_gf2e.pyx"
**********************************************************************
File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/rings/finite_field_ntl_gf2e.pyx", line 1349:
    sage: b._gap_init_()
Expected:
    'Z(65536)^1'
Got:
    doctest:21: UserWarning: You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``
    'Z(65536)^1'

[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/rings/finite_field_element.py
sage -t -long "devel/sage-main/sage/rings/finite_field_element.py"
**********************************************************************
File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/rings/finite_field_element.py", line 375:
    sage: a.multiplicative_order()
Expected:
    124
Got:
    doctest:21: UserWarning: You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``
    124

[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/rings/finite_field_ext_pari.py
sage -t -long "devel/sage-main/sage/rings/finite_field_ext_pari.py"
**********************************************************************
File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/rings/finite_field_ext_pari.py", line 103:
    sage: z.multiplicative_order()
Expected:
    15
Got:
    doctest:21: UserWarning: You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``
    15

[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/rings/polynomial/polynomial_element.pyx
sage -t -long "devel/sage-main/sage/rings/polynomial/polynomial_element.pyx"
**********************************************************************
File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/rings/polynomial/polynomial_element.pyx", line 2860:
    sage: f.is_irreducible(), f.is_primitive()
Expected:
    (True, False)
Got:
    doctest:21: UserWarning: You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``
    (True, False)

[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/groups/generic.py
sage -t -long "devel/sage-main/sage/groups/generic.py"      
**********************************************************************
File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/groups/generic.py", line 774:
    sage: discrete_log(u,g)
Expected:
    123456789
Got:
    doctest:21: UserWarning: You might consider installing the optional package for factoring Cunningham numbers with the following command: ``sage -i cunningham_tables-1.0``
    123456789
```




---

archive/issue_comments_059972.json:
```json
{
    "body": "I think my positive review was dependent on the vote we had (yes we did!) to include the spkg as standard rather then optional -- it is very small and requires no building.  The spkg is attached to (sorry, linked to) the ticket #7239.  I'm sure I assumed that when that ticket was closed, the right thing would happen to its spkg!",
    "created_at": "2010-01-22T17:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59972",
    "user": "https://github.com/JohnCremona"
}
```

I think my positive review was dependent on the vote we had (yes we did!) to include the spkg as standard rather then optional -- it is very small and requires no building.  The spkg is attached to (sorry, linked to) the ticket #7239.  I'm sure I assumed that when that ticket was closed, the right thing would happen to its spkg!



---

archive/issue_comments_059973.json:
```json
{
    "body": "Replying to [comment:11 cremona]:\n> I think my positive review was dependent on the vote we had (yes we did!) to include the spkg as standard rather then optional\n\nThank you for the clarification, John. The merging of this ticket can wait until:\n\n1. the (currently optional) Cunningham package becomes a standard spkg; or\n2. there is some code to test whether that spkg is installed.",
    "created_at": "2010-01-22T18:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59973",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:11 cremona]:
> I think my positive review was dependent on the vote we had (yes we did!) to include the spkg as standard rather then optional

Thank you for the clarification, John. The merging of this ticket can wait until:

1. the (currently optional) Cunningham package becomes a standard spkg; or
2. there is some code to test whether that spkg is installed.



---

archive/issue_comments_059974.json:
```json
{
    "body": "Attachment [trac7240_make_standard.patch](tarball://root/attachments/some-uuid/ticket7240/trac7240_make_standard.patch) by ylchapuy created at 2010-01-25 09:55:22",
    "created_at": "2010-01-25T09:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59974",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac7240_make_standard.patch](tarball://root/attachments/some-uuid/ticket7240/trac7240_make_standard.patch) by ylchapuy created at 2010-01-25 09:55:22



---

archive/issue_comments_059975.json:
```json
{
    "body": "This is of course all my fault. I stated that the warning wouldn't appear for numbers of less than 100 bits, but it was not the case. I updated the patch, switching two lines and it should be fine now. At least for me the above failures disappear.\n\nThe second patch I added is what should be done if the package become standard (and yes we had a vote, what's the next step?). It replaces my warning/advertisment with an error.\n\nYann",
    "created_at": "2010-01-25T09:59:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59975",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

This is of course all my fault. I stated that the warning wouldn't appear for numbers of less than 100 bits, but it was not the case. I updated the patch, switching two lines and it should be fine now. At least for me the above failures disappear.

The second patch I added is what should be done if the package become standard (and yes we had a vote, what's the next step?). It replaces my warning/advertisment with an error.

Yann



---

archive/issue_comments_059976.json:
```json
{
    "body": "Dear everyone,\n\nI would like to add a few comments here.  If I understand things correctly, the Cunningham database in SAGE is now just a list of numbers without structure, right?\n\nI have written myself a PARI/GP-2.4 script which\n\n1) tries to determine which b<sup>n</sup>-1 numbers have a non-trivial gcd with a given number.  The algorithm is essentially p-1 factorisation, but with several well-chosen bases instead of one (random) base.\n\n2) uses that information to do Aurifeuillian factorisation and a more clever table lookup.\n\nStep 1) can be skipped if we know exactly that we want to factor 10^555-1 for example.\n\nI could probably manage to port this to some SAGE functions in Python.  Once this has been done, I would like to add a lot more factors to more numbers of the form b^n-1 to the database (larger b and n).",
    "created_at": "2010-02-11T15:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59976",
    "user": "https://github.com/jdemeyer"
}
```

Dear everyone,

I would like to add a few comments here.  If I understand things correctly, the Cunningham database in SAGE is now just a list of numbers without structure, right?

I have written myself a PARI/GP-2.4 script which

1) tries to determine which b<sup>n</sup>-1 numbers have a non-trivial gcd with a given number.  The algorithm is essentially p-1 factorisation, but with several well-chosen bases instead of one (random) base.

2) uses that information to do Aurifeuillian factorisation and a more clever table lookup.

Step 1) can be skipped if we know exactly that we want to factor 10^555-1 for example.

I could probably manage to port this to some SAGE functions in Python.  Once this has been done, I would like to add a lot more factors to more numbers of the form b^n-1 to the database (larger b and n).



---

archive/issue_comments_059977.json:
```json
{
    "body": "Replying to [comment:14 jdemeyer]:\n> Dear everyone,\n> \n> I would like to add a few comments here.  If I understand things correctly, the Cunningham database in SAGE is now just a list of numbers without structure, right?\n\nYes right, this was just a quick and dirty solution to my problems.\n\n> I have written myself a PARI/GP-2.4 script (snip)\n> I could probably manage to port this to some SAGE functions in Python. (snip)\n\nThis would be great if you port your work to SAGE. My first thought was to include your script but currently SAGE is still shipping pari 2.3.3.\n\nYann",
    "created_at": "2010-02-11T17:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59977",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Replying to [comment:14 jdemeyer]:
> Dear everyone,
> 
> I would like to add a few comments here.  If I understand things correctly, the Cunningham database in SAGE is now just a list of numbers without structure, right?

Yes right, this was just a quick and dirty solution to my problems.

> I have written myself a PARI/GP-2.4 script (snip)
> I could probably manage to port this to some SAGE functions in Python. (snip)

This would be great if you port your work to SAGE. My first thought was to include your script but currently SAGE is still shipping pari 2.3.3.

Yann



---

archive/issue_comments_059978.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-29T05:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59978",
    "user": "https://github.com/williamstein"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_059979.json:
```json
{
    "body": "rebased on sage 4.4",
    "created_at": "2010-04-29T14:51:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59979",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

rebased on sage 4.4



---

archive/issue_comments_059980.json:
```json
{
    "body": "Attachment [trac7240_Cunningham_factorization_application.patch](tarball://root/attachments/some-uuid/ticket7240/trac7240_Cunningham_factorization_application.patch) by ylchapuy created at 2010-04-29 22:03:15\n\nI think it's ok for review now.",
    "created_at": "2010-04-29T22:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59980",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac7240_Cunningham_factorization_application.patch](tarball://root/attachments/some-uuid/ticket7240/trac7240_Cunningham_factorization_application.patch) by ylchapuy created at 2010-04-29 22:03:15

I think it's ok for review now.



---

archive/issue_comments_059981.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-29T22:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59981",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059982.json:
```json
{
    "body": "(again...) and it should be ok without the spkg.",
    "created_at": "2010-04-29T22:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59982",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

(again...) and it should be ok without the spkg.



---

archive/issue_comments_059983.json:
```json
{
    "body": "Changing component from algebra to factorization.",
    "created_at": "2010-07-08T14:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59983",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from algebra to factorization.



---

archive/issue_comments_059984.json:
```json
{
    "body": "I plan to work on this and improve it a lot.  In particular, the database of Cunningham factors should not be just a list, it should know of which numbers the factors are factors of (i.e. factor p divides Phi_a(b))",
    "created_at": "2010-07-08T14:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59984",
    "user": "https://github.com/jdemeyer"
}
```

I plan to work on this and improve it a lot.  In particular, the database of Cunningham factors should not be just a list, it should know of which numbers the factors are factors of (i.e. factor p divides Phi_a(b))



---

archive/issue_comments_059985.json:
```json
{
    "body": "This is one of the tickets which the Sage nagbot regularly nags me about.  But anyone seeing Jeroen's last comment will wait rather than review it.  I suggest that *either* this patch gets reviewed as is, and Jeroen's improvements go on another ticket, *or* the \"needs review\" tag is changed to \"needs work\".",
    "created_at": "2010-08-22T13:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59985",
    "user": "https://github.com/JohnCremona"
}
```

This is one of the tickets which the Sage nagbot regularly nags me about.  But anyone seeing Jeroen's last comment will wait rather than review it.  I suggest that *either* this patch gets reviewed as is, and Jeroen's improvements go on another ticket, *or* the "needs review" tag is changed to "needs work".



---

archive/issue_comments_059986.json:
```json
{
    "body": "It's still in my TODO list.",
    "created_at": "2010-08-22T13:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59986",
    "user": "https://github.com/jdemeyer"
}
```

It's still in my TODO list.



---

archive/issue_comments_059987.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-22T13:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59987",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059988.json:
```json
{
    "body": "As encouragement for working on this ticket, I'm using `_factor_cunningham` in #7931.  Now that #8334 has a positive review, #7931 is ready to review, but it's getting doctest failures because of the warning generated by _factor_cunningham.",
    "created_at": "2010-09-24T17:53:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59988",
    "user": "https://github.com/roed314"
}
```

As encouragement for working on this ticket, I'm using `_factor_cunningham` in #7931.  Now that #8334 has a positive review, #7931 is ready to review, but it's getting doctest failures because of the warning generated by _factor_cunningham.



---

archive/issue_comments_059989.json:
```json
{
    "body": "Any progress on this ticket?  I'd like to use it in #8335.",
    "created_at": "2011-06-21T11:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59989",
    "user": "https://github.com/roed314"
}
```

Any progress on this ticket?  I'd like to use it in #8335.



---

archive/issue_comments_059990.json:
```json
{
    "body": "This patch accompanies a new spkg: [http://sage.math.washington.edu/home/roed/cunningham_tables-2.0.spkg](http://sage.math.washington.edu/home/roed/cunningham_tables-2.0.spkg).\n\nApply 7240.patch only.",
    "created_at": "2011-12-05T10:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59990",
    "user": "https://github.com/roed314"
}
```

This patch accompanies a new spkg: [http://sage.math.washington.edu/home/roed/cunningham_tables-2.0.spkg](http://sage.math.washington.edu/home/roed/cunningham_tables-2.0.spkg).

Apply 7240.patch only.



---

archive/issue_comments_059991.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-12-05T10:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59991",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059992.json:
```json
{
    "body": "Also, this patch assumes that the Cunningham tables spkg has been made standard.  I'll e-mail sage-devel about that soon.",
    "created_at": "2011-12-05T10:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59992",
    "user": "https://github.com/roed314"
}
```

Also, this patch assumes that the Cunningham tables spkg has been made standard.  I'll e-mail sage-devel about that soon.



---

archive/issue_comments_059993.json:
```json
{
    "body": "Changing assignee from tbd to @roed314.",
    "created_at": "2011-12-05T11:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59993",
    "user": "https://github.com/roed314"
}
```

Changing assignee from tbd to @roed314.



---

archive/issue_comments_059994.json:
```json
{
    "body": "There's a new version of the spkg at: [Cunningham_Tables-2.1](http://sage.math.washington.edu/home/roed/cunningham_tables-2.1.spkg).  This new version will only work after applying #12133.",
    "created_at": "2012-01-04T10:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59994",
    "user": "https://github.com/roed314"
}
```

There's a new version of the spkg at: [Cunningham_Tables-2.1](http://sage.math.washington.edu/home/roed/cunningham_tables-2.1.spkg).  This new version will only work after applying #12133.



---

archive/issue_comments_059995.json:
```json
{
    "body": "please make sure that both sobj's use python ints (and longs) and not sage integers. Also remove the trailing whitespace in\n\n* docstring for FiniteField.factored_order\n* docstring for Polynomial.is_primitive\n* docstring for CunninghamDatabase\n* \"x is not a list\" line in cunningham_database.py\n\nFinally, it would be great if you would make your error's python 3 compatible, since we should probably start thinking forward to the day we make that transition.",
    "created_at": "2012-03-18T18:29:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59995",
    "user": "https://github.com/ohanar"
}
```

please make sure that both sobj's use python ints (and longs) and not sage integers. Also remove the trailing whitespace in

* docstring for FiniteField.factored_order
* docstring for Polynomial.is_primitive
* docstring for CunninghamDatabase
* "x is not a list" line in cunningham_database.py

Finally, it would be great if you would make your error's python 3 compatible, since we should probably start thinking forward to the day we make that transition.



---

archive/issue_comments_059996.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-03-18T18:29:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59996",
    "user": "https://github.com/ohanar"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059997.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-03-02T01:11:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59997",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059998.json:
```json
{
    "body": "I've addressed Andrew's comments, and added a new version of the SPKG at http://sage.math.washington.edu/home/roed/cunningham_tables-2.2.spkg",
    "created_at": "2013-03-02T01:11:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59998",
    "user": "https://github.com/roed314"
}
```

I've addressed Andrew's comments, and added a new version of the SPKG at http://sage.math.washington.edu/home/roed/cunningham_tables-2.2.spkg



---

archive/issue_comments_059999.json:
```json
{
    "body": "Attachment [7240.patch](tarball://root/attachments/some-uuid/ticket7240/7240.patch) by @jdemeyer created at 2013-08-13 15:35:53",
    "created_at": "2013-08-13T15:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-59999",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [7240.patch](tarball://root/attachments/some-uuid/ticket7240/7240.patch) by @jdemeyer created at 2013-08-13 15:35:53



---

archive/issue_comments_060000.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-02-13T10:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-60000",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060001.json:
```json
{
    "body": "Your file `7240.patch` tries to upgrade the `cunningham_table` package to 2.2 which isn't what is advertised with this ticket. Please don't do this, it makes difficult things even more so.\n\nI suppose then that the patch to be reviewed would be the one by `@`ylchapuy named ` trac7240_Cunningham_factorization_application.patch\u200b`. Even with the `-l` option it fails to apply with Sage-6.0.",
    "created_at": "2014-02-13T10:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-60001",
    "user": "https://github.com/rwst"
}
```

Your file `7240.patch` tries to upgrade the `cunningham_table` package to 2.2 which isn't what is advertised with this ticket. Please don't do this, it makes difficult things even more so.

I suppose then that the patch to be reviewed would be the one by `@`ylchapuy named ` trac7240_Cunningham_factorization_application.patch​`. Even with the `-l` option it fails to apply with Sage-6.0.



---

archive/issue_comments_060002.json:
```json
{
    "body": "From the sage developer's guide:\n\nIf a function requires an optional package, that function should fail gracefully\u2014**perhaps using a try-except block\u2014when the optional package is not available**, and should give a hint about how to install it. ...",
    "created_at": "2014-02-13T10:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-60002",
    "user": "https://github.com/rwst"
}
```

From the sage developer's guide:

If a function requires an optional package, that function should fail gracefully—**perhaps using a try-except block—when the optional package is not available**, and should give a hint about how to install it. ...



---

archive/issue_comments_060003.json:
```json
{
    "body": "Changing assignee from @roed314 to @rwst.",
    "created_at": "2014-02-13T10:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-60003",
    "user": "https://github.com/rwst"
}
```

Changing assignee from @roed314 to @rwst.



---

archive/issue_comments_060004.json:
```json
{
    "body": "Replying to [comment:11 cremona]:\n> I think my positive review was dependent on the vote we had (yes we did!) to include the spkg as standard rather then optional -- it is very small and requires no building.  The spkg is attached to (sorry, linked to) the ticket #7239.  I'm sure I assumed that when that ticket was closed, the right thing would happen to its spkg!\n>  \nIt was voted that the new cunningham package would become standard.",
    "created_at": "2014-02-13T13:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-60004",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Replying to [comment:11 cremona]:
> I think my positive review was dependent on the vote we had (yes we did!) to include the spkg as standard rather then optional -- it is very small and requires no building.  The spkg is attached to (sorry, linked to) the ticket #7239.  I'm sure I assumed that when that ticket was closed, the right thing would happen to its spkg!
>  
It was voted that the new cunningham package would become standard.



---

archive/issue_comments_060005.json:
```json
{
    "body": "(And note that the data provided should surely be updated.)",
    "created_at": "2014-02-13T13:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-60005",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

(And note that the data provided should surely be updated.)



---

archive/issue_comments_060006.json:
```json
{
    "body": "Replying to [comment:43 jpflori]:\n> (And note that the data provided should surely be updated.)\n\nBut don't use $SAGE_DATA anymore, use $SAGE_SHARE or $SAGE_ROOT/share, see #15814",
    "created_at": "2014-02-14T08:48:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-60006",
    "user": "https://github.com/rwst"
}
```

Replying to [comment:43 jpflori]:
> (And note that the data provided should surely be updated.)

But don't use $SAGE_DATA anymore, use $SAGE_SHARE or $SAGE_ROOT/share, see #15814



---

archive/issue_comments_060007.json:
```json
{
    "body": "Separated from the SPKG install (#15813) and rebased on 6.2.base2.\n----\nNew commits:",
    "created_at": "2014-02-20T14:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-60007",
    "user": "https://github.com/rwst"
}
```

Separated from the SPKG install (#15813) and rebased on 6.2.base2.
----
New commits:



---

archive/issue_comments_060008.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-02-20T14:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-60008",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060009.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-04-04T14:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-60009",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060010.json:
```json
{
    "body": "patchbot reports failures in `rings/` and `groups/`: among others `ImportError: cannot import name CunninghamDatabase`. Of course the patchbot will test without the package being installed, so it made sense what I wrote in comment:39 about failing gracefully...",
    "created_at": "2014-04-04T14:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-60010",
    "user": "https://github.com/rwst"
}
```

patchbot reports failures in `rings/` and `groups/`: among others `ImportError: cannot import name CunninghamDatabase`. Of course the patchbot will test without the package being installed, so it made sense what I wrote in comment:39 about failing gracefully...



---

archive/issue_comments_060011.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-04-04T16:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-60011",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060012.json:
```json
{
    "body": "Rebase on 6.2.beta6. Fix failing doctests.\n----\nNew commits:",
    "created_at": "2014-04-04T16:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-60012",
    "user": "https://github.com/rwst"
}
```

Rebase on 6.2.beta6. Fix failing doctests.
----
New commits:



---

archive/issue_comments_060013.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-05-07T13:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7240#issuecomment-60013",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_review to needs_work.

# Issue 7886: [with patch, needs work] Implement conjugacy classes

archive/issues_007886.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  @wdjoyner @jdemeyer jlopez\n\nGAP has several functions concerning conjugacy classes of groups. It would be nice to have a way to access such functions from Sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7886\n\n",
    "created_at": "2010-01-09T21:49:27Z",
    "labels": [
        "component: group theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.8",
    "title": "[with patch, needs work] Implement conjugacy classes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7886",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```
Assignee: joyner

CC:  @wdjoyner @jdemeyer jlopez

GAP has several functions concerning conjugacy classes of groups. It would be nice to have a way to access such functions from Sage.

Issue created by migration from https://trac.sagemath.org/ticket/7886





---

archive/issue_comments_068417.json:
```json
{
    "body": "Implementation of a python class for conjugacy classes, wrapping some GAP functions and some native python methods.",
    "created_at": "2010-01-09T21:50:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68417",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Implementation of a python class for conjugacy classes, wrapping some GAP functions and some native python methods.



---

archive/issue_comments_068418.json:
```json
{
    "body": "Attachment [trac_7886_conjugacy_classes.patch](tarball://root/attachments/some-uuid/ticket7886/trac_7886_conjugacy_classes.patch) by jlopez created at 2011-12-06 18:01:03\n\nConjugacy classes code",
    "created_at": "2011-12-06T18:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68418",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Attachment [trac_7886_conjugacy_classes.patch](tarball://root/attachments/some-uuid/ticket7886/trac_7886_conjugacy_classes.patch) by jlopez created at 2011-12-06 18:01:03

Conjugacy classes code



---

archive/issue_comments_068419.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-12-06T18:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68419",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068420.json:
```json
{
    "body": "Patch submitted. All tests pass on my machine (OX-X 10.6.8) with the exception of the ConjugacyClass Testsuite, which fails testing equality. I have no idea how the testsuite works, so could use some help here.",
    "created_at": "2011-12-06T18:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68420",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Patch submitted. All tests pass on my machine (OX-X 10.6.8) with the exception of the ConjugacyClass Testsuite, which fails testing equality. I have no idea how the testsuite works, so could use some help here.



---

archive/issue_comments_068421.json:
```json
{
    "body": "For the patchbot:\n\nApply trac_7886_conjugacy_classes.patch",
    "created_at": "2011-12-06T18:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68421",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

For the patchbot:

Apply trac_7886_conjugacy_classes.patch



---

archive/issue_comments_068422.json:
```json
{
    "body": "Oops! Forgot to add the new module to the patch, here it is!",
    "created_at": "2011-12-06T18:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68422",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Oops! Forgot to add the new module to the patch, here it is!



---

archive/issue_comments_068423.json:
```json
{
    "body": "Apply trac_7886_conjugacy_classes_module.patch, trac_7886_conjugacy_classes.patch",
    "created_at": "2011-12-06T18:56:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68423",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Apply trac_7886_conjugacy_classes_module.patch, trac_7886_conjugacy_classes.patch



---

archive/issue_comments_068424.json:
```json
{
    "body": "conjugacy_classes.py module with passing Testsuite",
    "created_at": "2011-12-07T16:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68424",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

conjugacy_classes.py module with passing Testsuite



---

archive/issue_comments_068425.json:
```json
{
    "body": "Attachment [trac_7886_conjugacy_classes_module.patch](tarball://root/attachments/some-uuid/ticket7886/trac_7886_conjugacy_classes_module.patch) by jlopez created at 2011-12-07 16:46:30\n\nUpdated the conjugacy_classes.py module with the fixed _cmp_ method so that the testsuite passes. All test pass on my machine, so ready for review.",
    "created_at": "2011-12-07T16:46:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68425",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Attachment [trac_7886_conjugacy_classes_module.patch](tarball://root/attachments/some-uuid/ticket7886/trac_7886_conjugacy_classes_module.patch) by jlopez created at 2011-12-07 16:46:30

Updated the conjugacy_classes.py module with the fixed _cmp_ method so that the testsuite passes. All test pass on my machine, so ready for review.



---

archive/issue_comments_068426.json:
```json
{
    "body": "The code looks fine to me. I tested it on a 10.6.8 mac under sage-4.8.a3 and on a Ubuntu 10.04 (Lucid Lynx) machine under sage-4.8.a1.\n\nThere was a discussion of cached methods in sage-devel, but I'm not sure how that relates to this ticket, so I'm giving this a positive review. Maybe changes, if any, from that thread can go in a separate ticket.",
    "created_at": "2011-12-09T14:37:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68426",
    "user": "https://github.com/wdjoyner"
}
```

The code looks fine to me. I tested it on a 10.6.8 mac under sage-4.8.a3 and on a Ubuntu 10.04 (Lucid Lynx) machine under sage-4.8.a1.

There was a discussion of cached methods in sage-devel, but I'm not sure how that relates to this ticket, so I'm giving this a positive review. Maybe changes, if any, from that thread can go in a separate ticket.



---

archive/issue_comments_068427.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-09T14:37:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68427",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068428.json:
```json
{
    "body": "In the file `sage/groups/perm_gps/permgroup.py`, you use Unicode but the encoding has not been declared to be utf-8.\n\nSee [http://www.python.org/dev/peps/pep-0263/](http://www.python.org/dev/peps/pep-0263/)",
    "created_at": "2011-12-11T10:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68428",
    "user": "https://github.com/jdemeyer"
}
```

In the file `sage/groups/perm_gps/permgroup.py`, you use Unicode but the encoding has not been declared to be utf-8.

See [http://www.python.org/dev/peps/pep-0263/](http://www.python.org/dev/peps/pep-0263/)



---

archive/issue_comments_068429.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-12-11T10:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68429",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_068430.json:
```json
{
    "body": "Fixed encoding and improvement of naive set method.",
    "created_at": "2011-12-12T11:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68430",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Fixed encoding and improvement of naive set method.



---

archive/issue_comments_068431.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-12-12T11:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68431",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068432.json:
```json
{
    "body": "Attachment [trac_7886_conjugacy_classes_encoding_fix.patch](tarball://root/attachments/some-uuid/ticket7886/trac_7886_conjugacy_classes_encoding_fix.patch) by jlopez created at 2011-12-12 11:51:23\n\nSorry, I thought we were using utf-8 by default. Fixed the encoding in permgroup.py and conjugacy_classes.py\nAlso implemented a more efficient fallback method using TransitiveIdeal.\nNeeds review.",
    "created_at": "2011-12-12T11:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68432",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Attachment [trac_7886_conjugacy_classes_encoding_fix.patch](tarball://root/attachments/some-uuid/ticket7886/trac_7886_conjugacy_classes_encoding_fix.patch) by jlopez created at 2011-12-12 11:51:23

Sorry, I thought we were using utf-8 by default. Fixed the encoding in permgroup.py and conjugacy_classes.py
Also implemented a more efficient fallback method using TransitiveIdeal.
Needs review.



---

archive/issue_comments_068433.json:
```json
{
    "body": "For the patchbot:\nApply trac_7886_conjugacy_classes_module.patch, trac_7886_conjugacy_classes.patch, trac_7886_conjugacy_classes_encoding_fix.patch",
    "created_at": "2011-12-12T12:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68433",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

For the patchbot:
Apply trac_7886_conjugacy_classes_module.patch, trac_7886_conjugacy_classes.patch, trac_7886_conjugacy_classes_encoding_fix.patch



---

archive/issue_comments_068434.json:
```json
{
    "body": "Just a little bump. Jeroen, can you please check that the UTF encoding is working properly now? David Joyner already reviewed the math-related part of the ticket.",
    "created_at": "2012-02-08T09:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68434",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Just a little bump. Jeroen, can you please check that the UTF encoding is working properly now? David Joyner already reviewed the math-related part of the ticket.



---

archive/issue_comments_068435.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-01-03T20:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68435",
    "user": "https://github.com/tkluck"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068436.json:
```json
{
    "body": "This has been lingering on trac for a while; thought I could review it. I tried to apply these patches to 5.5 in the given order.\n\nThe second one gives\n\n```\napplying http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7886/trac_7886_conjugacy_classes.patch\npatching file sage/groups/perm_gps/permgroup.py\nHunk #1 succeeded at 95 with fuzz 2 (offset 3 lines).\nHunk #2 FAILED at 132\n1 out of 3 hunks FAILED -- saving rejects to file sage/groups/perm_gps/permgroup.py.rej\nabort: patch failed to apply\n```\n\n\nIs it possible to rebase them? I'll set this ticket to 'needs work' in the mean time.",
    "created_at": "2013-01-03T20:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68436",
    "user": "https://github.com/tkluck"
}
```

This has been lingering on trac for a while; thought I could review it. I tried to apply these patches to 5.5 in the given order.

The second one gives

```
applying http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7886/trac_7886_conjugacy_classes.patch
patching file sage/groups/perm_gps/permgroup.py
Hunk #1 succeeded at 95 with fuzz 2 (offset 3 lines).
Hunk #2 FAILED at 132
1 out of 3 hunks FAILED -- saving rejects to file sage/groups/perm_gps/permgroup.py.rej
abort: patch failed to apply
```


Is it possible to rebase them? I'll set this ticket to 'needs work' in the mean time.



---

archive/issue_comments_068437.json:
```json
{
    "body": "I will give it a go during the weekend. Thanks for volunteering for reviewing!",
    "created_at": "2013-01-31T19:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68437",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

I will give it a go during the weekend. Thanks for volunteering for reviewing!



---

archive/issue_comments_068438.json:
```json
{
    "body": "Tests pass on my Mac Os X 10.6.8, ready for review. Apply the combined patch only.",
    "created_at": "2013-02-04T19:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68438",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Tests pass on my Mac Os X 10.6.8, ready for review. Apply the combined patch only.



---

archive/issue_comments_068439.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-02-04T19:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68439",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068440.json:
```json
{
    "body": "patchbot: apply trac_7886_conjugacy_classes_combined.patch",
    "created_at": "2013-02-04T19:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68440",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

patchbot: apply trac_7886_conjugacy_classes_combined.patch



---

archive/issue_comments_068441.json:
```json
{
    "body": "Hey,\n\nThank you for working on this. However there are multiple docstring issues you will need to address. More specifically, you will need to change (for example)\n\n```\nEXAMPLES:\n    sage: H = MatrixGroup([matrix(GF(5),2,[1,2, -1, 1]), matrix(GF(5),2, [1,1, 0,1])])\n    sage: h = H(matrix(GF(5),2,[1,2, -1, 1]))\n    sage: H.conjugacy_class(h)\n    ...\n\n#####\n\nTODO:\n    - Implement a non-naive fallback method for computing all the elements of\n    the conjugacy class when the group is not defined in GAP, as the one in\n    Butler's paper.\n    - Define a sage method for gap matrices so that groups of matrices can\n    use the quicker GAP algorithm rather than the naive one.\n\nEXAMPLES::\n\n- Conjugacy classes for groups of permutations \n\n    sage: G = SymmetricGroup(4) \n    ...\n```\n\nto\n\n```\nEXAMPLES::\n\n    sage: H = MatrixGroup([matrix(GF(5),2,[1,2, -1, 1]), matrix(GF(5),2, [1,1, 0,1])])\n    sage: h = H(matrix(GF(5),2,[1,2, -1, 1]))\n    sage: H.conjugacy_class(h)\n    ...\n\n####\n\n\n.. TODO::\n\n    - Implement a non-naive fallback method for computing all the elements of\n      the conjugacy class when the group is not defined in GAP, as the one in\n      Butler's paper.\n    - Define a sage method for gap matrices so that groups of matrices can\n      use the quicker GAP algorithm rather than the naive one.\n\nEXAMPLES:\n\nConjugacy classes for groups of permutations::\n\n    sage: G = SymmetricGroup(4) \n    ...\n```\n\notherwise the formatting will be incorrect (the convention is not to use bullet points for different examples). For a full description, see [the conventions page](http://www.sagemath.org/doc/developer/conventions.html:).\n\nAlso you will need to cleanup the patch's header message.\n\nThanks,\n\nTravis",
    "created_at": "2013-02-19T20:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68441",
    "user": "https://github.com/tscrim"
}
```

Hey,

Thank you for working on this. However there are multiple docstring issues you will need to address. More specifically, you will need to change (for example)

```
EXAMPLES:
    sage: H = MatrixGroup([matrix(GF(5),2,[1,2, -1, 1]), matrix(GF(5),2, [1,1, 0,1])])
    sage: h = H(matrix(GF(5),2,[1,2, -1, 1]))
    sage: H.conjugacy_class(h)
    ...

#####

TODO:
    - Implement a non-naive fallback method for computing all the elements of
    the conjugacy class when the group is not defined in GAP, as the one in
    Butler's paper.
    - Define a sage method for gap matrices so that groups of matrices can
    use the quicker GAP algorithm rather than the naive one.

EXAMPLES::

- Conjugacy classes for groups of permutations 

    sage: G = SymmetricGroup(4) 
    ...
```

to

```
EXAMPLES::

    sage: H = MatrixGroup([matrix(GF(5),2,[1,2, -1, 1]), matrix(GF(5),2, [1,1, 0,1])])
    sage: h = H(matrix(GF(5),2,[1,2, -1, 1]))
    sage: H.conjugacy_class(h)
    ...

####


.. TODO::

    - Implement a non-naive fallback method for computing all the elements of
      the conjugacy class when the group is not defined in GAP, as the one in
      Butler's paper.
    - Define a sage method for gap matrices so that groups of matrices can
      use the quicker GAP algorithm rather than the naive one.

EXAMPLES:

Conjugacy classes for groups of permutations::

    sage: G = SymmetricGroup(4) 
    ...
```

otherwise the formatting will be incorrect (the convention is not to use bullet points for different examples). For a full description, see [the conventions page](http://www.sagemath.org/doc/developer/conventions.html:).

Also you will need to cleanup the patch's header message.

Thanks,

Travis



---

archive/issue_comments_068442.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-02-20T16:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68442",
    "user": "https://github.com/KPanComputes"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068443.json:
```json
{
    "body": "This patch needs to address referee's comments. I am changing this to `needs_work` in the meanwhile.",
    "created_at": "2013-02-20T16:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68443",
    "user": "https://github.com/KPanComputes"
}
```

This patch needs to address referee's comments. I am changing this to `needs_work` in the meanwhile.



---

archive/issue_comments_068444.json:
```json
{
    "body": "Thanks for looking at my patch! I have a complicated work situation during the week, but will fix the docstring style and rebase again over sage 5.7 on Friday or Saturday.\n\nNot sure what you mean about the patch header message. Do you mean the Spanish characters in my name? That is automatically added by my hg configuration, but it seems that trac does not support UTF-8; I added the appropriate encoding to the python files, but don't know how to do it for the patch (and don't feel inclined to change my name either). If it is about the cruft that came from patch folding, I will take care of that as well.\n\nCheers,\nJ",
    "created_at": "2013-02-20T21:59:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68444",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Thanks for looking at my patch! I have a complicated work situation during the week, but will fix the docstring style and rebase again over sage 5.7 on Friday or Saturday.

Not sure what you mean about the patch header message. Do you mean the Spanish characters in my name? That is automatically added by my hg configuration, but it seems that trac does not support UTF-8; I added the appropriate encoding to the python files, but don't know how to do it for the patch (and don't feel inclined to change my name either). If it is about the cruft that came from patch folding, I will take care of that as well.

Cheers,
J



---

archive/issue_comments_068445.json:
```json
{
    "body": "Hey Javier,\n\nReplying to [comment:20 jlopez]:\n> Thanks for looking at my patch! I have a complicated work situation during the week, but will fix the docstring style and rebase again over sage 5.7 on Friday or Saturday.\n\nThank you! There's not a huge rush, just ping back when it's done and I'll give it a look-over.\n\n> Not sure what you mean about the patch header message. Do you mean the Spanish characters in my name? That is automatically added by my hg configuration, but it seems that trac does not support UTF-8; I added the appropriate encoding to the python files, but don't know how to do it for the patch (and don't feel inclined to change my name either). If it is about the cruft that came from patch folding, I will take care of that as well.\n\nIf you look at the beginning of the patch, you have the following:\n\n```\n# HG changeset patch\n# User Javier L\u00c3\u00b3pez Pe\u00c3\u00b1a <vengoroso@gmail.com>\n# Date 1360004753 0\n# Node ID 2782ba59f14a8dafdb44e05a67972e5a9d4db0cf\n# Parent  fa8decac55338225dc33568ad600c261fc777b4c\n* * *\nTrac 7886: Conjugacy classes\n* * *\nTrac 7886: Created module for conjugacy classes of finite groups.\nAdded wrappers for GAP functions and naive fallback method.\n* * *\nTrac 7886: Conjugacy classes\n```\n\nIn particular, the line right after the `# Parent ...` should be a one line summary of the patch with the ticket number (such as `Trac 7886: Conjugacy classes` which is probably what you originally had). This can get mangled when folding patches. You can change this by doing a `qrefresh -e`. I don't think the encoding for your name in the header is important.\n\nGracias por tu trabajo,\n\nTravis",
    "created_at": "2013-02-21T15:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68445",
    "user": "https://github.com/tscrim"
}
```

Hey Javier,

Replying to [comment:20 jlopez]:
> Thanks for looking at my patch! I have a complicated work situation during the week, but will fix the docstring style and rebase again over sage 5.7 on Friday or Saturday.

Thank you! There's not a huge rush, just ping back when it's done and I'll give it a look-over.

> Not sure what you mean about the patch header message. Do you mean the Spanish characters in my name? That is automatically added by my hg configuration, but it seems that trac does not support UTF-8; I added the appropriate encoding to the python files, but don't know how to do it for the patch (and don't feel inclined to change my name either). If it is about the cruft that came from patch folding, I will take care of that as well.

If you look at the beginning of the patch, you have the following:

```
# HG changeset patch
# User Javier LÃ³pez PeÃ±a <vengoroso@gmail.com>
# Date 1360004753 0
# Node ID 2782ba59f14a8dafdb44e05a67972e5a9d4db0cf
# Parent  fa8decac55338225dc33568ad600c261fc777b4c
* * *
Trac 7886: Conjugacy classes
* * *
Trac 7886: Created module for conjugacy classes of finite groups.
Added wrappers for GAP functions and naive fallback method.
* * *
Trac 7886: Conjugacy classes
```

In particular, the line right after the `# Parent ...` should be a one line summary of the patch with the ticket number (such as `Trac 7886: Conjugacy classes` which is probably what you originally had). This can get mangled when folding patches. You can change this by doing a `qrefresh -e`. I don't think the encoding for your name in the header is important.

Gracias por tu trabajo,

Travis



---

archive/issue_comments_068446.json:
```json
{
    "body": "I think I fixed all the docstring formatting. Also removed some trailing whitespaces and rebased over sage 5.7. Needs review.\n\nPatchbot apply trac_7886_conjugacy_classes_combined.patch",
    "created_at": "2013-02-22T14:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68446",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

I think I fixed all the docstring formatting. Also removed some trailing whitespaces and rebased over sage 5.7. Needs review.

Patchbot apply trac_7886_conjugacy_classes_combined.patch



---

archive/issue_comments_068447.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-02-22T14:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68447",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068448.json:
```json
{
    "body": "Hey Javier,\n\nThere are still many misformatted docstrings (did you forget to refresh the patch?) and the examples are still itemized. Also remove the `* * *` from the header. In case you are unaware, you can run `sage -docbuild reference html` (or reference/groups and/or reference/categories with #6495) to view the documentation.\n\nThanks,\n\nTravis",
    "created_at": "2013-02-22T14:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68448",
    "user": "https://github.com/tscrim"
}
```

Hey Javier,

There are still many misformatted docstrings (did you forget to refresh the patch?) and the examples are still itemized. Also remove the `* * *` from the header. In case you are unaware, you can run `sage -docbuild reference html` (or reference/groups and/or reference/categories with #6495) to view the documentation.

Thanks,

Travis



---

archive/issue_comments_068449.json:
```json
{
    "body": "Hi Travis,\n\nrefreshed, fixed the itemized examples. My docbuild refuses to work due to the presence of UTF8 characters in the docstring:\n\n```\n    reading sources... [ 75%] sage/groups/perm_gps/permgroup                        \n    Sphinx error:\n    'ascii' codec can't decode byte 0xc3 in position 3438: ordinal not in range(128)\n```\n\n\nIs there any way to tell sphinx to use the utf8 codec instead? I already included the \n\n```\n# coding = utf-8\n```\n\nin the python file, but the docbuild seems to ignore that.",
    "created_at": "2013-02-22T15:28:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68449",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Hi Travis,

refreshed, fixed the itemized examples. My docbuild refuses to work due to the presence of UTF8 characters in the docstring:

```
    reading sources... [ 75%] sage/groups/perm_gps/permgroup                        
    Sphinx error:
    'ascii' codec can't decode byte 0xc3 in position 3438: ordinal not in range(128)
```


Is there any way to tell sphinx to use the utf8 codec instead? I already included the 

```
# coding = utf-8
```

in the python file, but the docbuild seems to ignore that.



---

archive/issue_comments_068450.json:
```json
{
    "body": "Docstring and whitespaces fixes, rebased for sage 5.7. Apply this patch only.",
    "created_at": "2013-02-22T16:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68450",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Docstring and whitespaces fixes, rebased for sage 5.7. Apply this patch only.



---

archive/issue_comments_068451.json:
```json
{
    "body": "Attachment [trac_7886_conjugacy_classes_combined.patch](tarball://root/attachments/some-uuid/ticket7886/trac_7886_conjugacy_classes_combined.patch) by @tscrim created at 2013-02-22 17:19:01",
    "created_at": "2013-02-22T17:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68451",
    "user": "https://github.com/tscrim"
}
```

Attachment [trac_7886_conjugacy_classes_combined.patch](tarball://root/attachments/some-uuid/ticket7886/trac_7886_conjugacy_classes_combined.patch) by @tscrim created at 2013-02-22 17:19:01



---

archive/issue_comments_068452.json:
```json
{
    "body": "Attachment [trac_7886-conjugacy_classes-review-ts.patch](tarball://root/attachments/some-uuid/ticket7886/trac_7886-conjugacy_classes-review-ts.patch) by @tscrim created at 2013-02-22 17:24:46\n\nHey Javier,\n\nI've attaching a review patch which fixes up the remaining documentation and adds the files to the docbuild (I had to do some extra tweaks in the `categories/finite_groups.py` since it wasn't in the docbuild prior to this patch). If everything works and looks good to you, you go ahead and set this to positive review.\n\nThanks,\n\nTravis\n\nFor patchbot:\n\nApply: trac_7886_conjugacy_classes_combined.patch, trac_7886-conjugacy_classes-review-ts.patch",
    "created_at": "2013-02-22T17:24:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68452",
    "user": "https://github.com/tscrim"
}
```

Attachment [trac_7886-conjugacy_classes-review-ts.patch](tarball://root/attachments/some-uuid/ticket7886/trac_7886-conjugacy_classes-review-ts.patch) by @tscrim created at 2013-02-22 17:24:46

Hey Javier,

I've attaching a review patch which fixes up the remaining documentation and adds the files to the docbuild (I had to do some extra tweaks in the `categories/finite_groups.py` since it wasn't in the docbuild prior to this patch). If everything works and looks good to you, you go ahead and set this to positive review.

Thanks,

Travis

For patchbot:

Apply: trac_7886_conjugacy_classes_combined.patch, trac_7886-conjugacy_classes-review-ts.patch



---

archive/issue_comments_068453.json:
```json
{
    "body": "Hi Travis,\n\nyour reviewer patch fails to apply for me:\n\n\n```\napplying trac_7886-conjugacy_classes-review-ts.patch\nunable to find 'doc/en/reference/categories/index.rst' for patching\n1 out of 1 hunks FAILED -- saving rejects to file doc/en/reference/categories/index.rst.rej\nunable to find 'doc/en/reference/groups/index.rst' for patching\n1 out of 1 hunks FAILED -- saving rejects to file doc/en/reference/groups/index.rst.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_7886-conjugacy_classes-review-ts.patch\n```\n\n\nAre we working over the same version of sage (I'm on 5.7), or did you apply any previous patches that changed documentation files?",
    "created_at": "2013-02-23T12:26:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68453",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Hi Travis,

your reviewer patch fails to apply for me:


```
applying trac_7886-conjugacy_classes-review-ts.patch
unable to find 'doc/en/reference/categories/index.rst' for patching
1 out of 1 hunks FAILED -- saving rejects to file doc/en/reference/categories/index.rst.rej
unable to find 'doc/en/reference/groups/index.rst' for patching
1 out of 1 hunks FAILED -- saving rejects to file doc/en/reference/groups/index.rst.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_7886-conjugacy_classes-review-ts.patch
```


Are we working over the same version of sage (I'm on 5.7), or did you apply any previous patches that changed documentation files?



---

archive/issue_comments_068454.json:
```json
{
    "body": "Hey Javier,\n\nActually I have #6495 applied, it might be because of that. I've added it as a dependency. Try applying the patches with #6495.\n\nThanks,\n\nTravis",
    "created_at": "2013-02-23T13:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68454",
    "user": "https://github.com/tscrim"
}
```

Hey Javier,

Actually I have #6495 applied, it might be because of that. I've added it as a dependency. Try applying the patches with #6495.

Thanks,

Travis



---

archive/issue_comments_068455.json:
```json
{
    "body": "Alright. WIth #6495 applied the reviewer patch applies and docs build properly. Tests pass, so I think this is good to go.\nThanks for your help with the reviewing and the docstring formatting!",
    "created_at": "2013-02-23T18:02:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68455",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Alright. WIth #6495 applied the reviewer patch applies and docs build properly. Tests pass, so I think this is good to go.
Thanks for your help with the reviewing and the docstring formatting!



---

archive/issue_comments_068456.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-23T18:02:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68456",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068457.json:
```json
{
    "body": "Patchbot seems confused about what needs to be applied, so here it goes again:\n\nApply trac_7886_conjugacy_classes_combined.patch trac_7886-conjugacy_classes-review-ts.patch",
    "created_at": "2013-02-23T18:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68457",
    "user": "https://trac.sagemath.org/admin/accounts/users/jlopez"
}
```

Patchbot seems confused about what needs to be applied, so here it goes again:

Apply trac_7886_conjugacy_classes_combined.patch trac_7886-conjugacy_classes-review-ts.patch



---

archive/issue_events_008101.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-02-28T10:32:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7886#event-8101"
}
```



---

archive/issue_comments_068458.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-02-28T10:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68458",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_068459.json:
```json
{
    "body": "You shouldn't return lists from `@`cached_method functions. If somebody mutates the output list then future calls return the wrong result! Always return tuples instead of lists unless you want the output to be mutable.\n\nAlso, `ConjugacyClass` is a parent without elements; Use `SageObject` as base for classes that do not use the parent/element pattern.",
    "created_at": "2013-02-28T20:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7886#issuecomment-68459",
    "user": "https://github.com/vbraun"
}
```

You shouldn't return lists from `@`cached_method functions. If somebody mutates the output list then future calls return the wrong result! Always return tuples instead of lists unless you want the output to be mutable.

Also, `ConjugacyClass` is a parent without elements; Use `SageObject` as base for classes that do not use the parent/element pattern.

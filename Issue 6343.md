# Issue 6343: Adds SageObject.check() generic testing framework

archive/issues_006343.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat cwitty @roed314 @saliola mvngu\n\nThis patch adds a .check() method in SageObject which runs systematic checks on the object. Here is a typical call:\n\n     sage: ZZ.check(verbose = True)\n     running test_an_element ... done\n     running test_element_pickling ... done\n     running test_not_implemented_methods ... done\n     running test_pickling ... done\n\nIn practice, o.check() runs all the methods named test_* of the object o.\n\nThe test_* methods are typically implemented by abstract super classes and in particular via categories, in order to enforce standard behavior and API (test_pickling, test_an_element), or provide mathematical sanity checks (test_associativity).\n\nFor consistent error reporting, the test_* methods in turn must use the gadget sage.misc.instance_tester.InstanceTester to actually run the tests.\n\nThis patch is a prerequisite for #5891 (category framework), which uses it intensively. Some examples in the patch illustrate this, and are therefore temporarily disabled.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6343\n\n",
    "created_at": "2009-06-16T22:21:54Z",
    "labels": [
        "doctest coverage",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Adds SageObject.check() generic testing framework",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6343",
    "user": "@nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat cwitty @roed314 @saliola mvngu

This patch adds a .check() method in SageObject which runs systematic checks on the object. Here is a typical call:

     sage: ZZ.check(verbose = True)
     running test_an_element ... done
     running test_element_pickling ... done
     running test_not_implemented_methods ... done
     running test_pickling ... done

In practice, o.check() runs all the methods named test_* of the object o.

The test_* methods are typically implemented by abstract super classes and in particular via categories, in order to enforce standard behavior and API (test_pickling, test_an_element), or provide mathematical sanity checks (test_associativity).

For consistent error reporting, the test_* methods in turn must use the gadget sage.misc.instance_tester.InstanceTester to actually run the tests.

This patch is a prerequisite for #5891 (category framework), which uses it intensively. Some examples in the patch illustrate this, and are therefore temporarily disabled.

Issue created by migration from https://trac.sagemath.org/ticket/6343





---

archive/issue_comments_050685.json:
```json
{
    "body": "Change the name from obj.check() to obj._check().  It is not reasonable that if one does obj.<tab> on *any* Sage object, one sees check.  \n\nWilliam",
    "created_at": "2009-06-18T14:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50685",
    "user": "@williamstein"
}
```

Change the name from obj.check() to obj._check().  It is not reasonable that if one does obj.<tab> on *any* Sage object, one sees check.  

William



---

archive/issue_comments_050686.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-18T16:12:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50686",
    "user": "@nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_050687.json:
```json
{
    "body": "Change the name from obj.check() to obj._check(). It is not reasonable that if one does obj.<tab> on *any* Sage object, one sees check.",
    "created_at": "2009-06-20T14:41:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50687",
    "user": "@williamstein"
}
```

Change the name from obj.check() to obj._check(). It is not reasonable that if one does obj.<tab> on *any* Sage object, one sees check.



---

archive/issue_comments_050688.json:
```json
{
    "body": "Changing keywords from \"\" to \"testunit\".",
    "created_at": "2009-06-26T08:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50688",
    "user": "@nthiery"
}
```

Changing keywords from "" to "testunit".



---

archive/issue_comments_050689.json:
```json
{
    "body": "Patch reworked, after the discussion on sage-devel.\n\nNote: After peeking again into the testunit framework, I finally went for TestSuite(object).run() which\nis most consistent with it, while being meaningful.\n\nThe otherwise discussed functionality TestSuite(object).associativity() will be implemented in a later patch\n(if deemed useful in the meantime).",
    "created_at": "2009-06-26T08:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50689",
    "user": "@nthiery"
}
```

Patch reworked, after the discussion on sage-devel.

Note: After peeking again into the testunit framework, I finally went for TestSuite(object).run() which
is most consistent with it, while being meaningful.

The otherwise discussed functionality TestSuite(object).associativity() will be implemented in a later patch
(if deemed useful in the meantime).



---

archive/issue_comments_050690.json:
```json
{
    "body": "I like the new design and class/function names.",
    "created_at": "2009-07-08T14:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50690",
    "user": "@williamstein"
}
```

I like the new design and class/function names.



---

archive/issue_comments_050691.json:
```json
{
    "body": "Attachment [trac_6343-sage_object-test-nt.patch](tarball://root/attachments/some-uuid/ticket6343/trac_6343-sage_object-test-nt.patch) by @nthiery created at 2009-07-10 22:27:48\n\nOops, the doctests were broken (I had forgotten to rename stuff in there)",
    "created_at": "2009-07-10T22:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50691",
    "user": "@nthiery"
}
```

Attachment [trac_6343-sage_object-test-nt.patch](tarball://root/attachments/some-uuid/ticket6343/trac_6343-sage_object-test-nt.patch) by @nthiery created at 2009-07-10 22:27:48

Oops, the doctests were broken (I had forgotten to rename stuff in there)



---

archive/issue_comments_050692.json:
```json
{
    "body": "Looks good to me.  We just have to make sure to re-enable the missing tests when the category stuff is added.",
    "created_at": "2009-07-16T21:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50692",
    "user": "@mwhansen"
}
```

Looks good to me.  We just have to make sure to re-enable the missing tests when the category stuff is added.



---

archive/issue_comments_050693.json:
```json
{
    "body": "Thanks for the review!\nI just fixed my name to please my grand father :-)",
    "created_at": "2009-07-16T21:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50693",
    "user": "@nthiery"
}
```

Thanks for the review!
I just fixed my name to please my grand father :-)



---

archive/issue_comments_050694.json:
```json
{
    "body": "No worries.  I really should just add key tomy keyboard layout :-)",
    "created_at": "2009-07-16T21:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50694",
    "user": "@mwhansen"
}
```

No worries.  I really should just add key tomy keyboard layout :-)



---

archive/issue_comments_050695.json:
```json
{
    "body": "reviewer patch; fixes typos and docstring formatting",
    "created_at": "2009-07-16T23:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50695",
    "user": "mvngu"
}
```

reviewer patch; fixes typos and docstring formatting



---

archive/issue_comments_050696.json:
```json
{
    "body": "Attachment [trac_6343-reviewer.patch](tarball://root/attachments/some-uuid/ticket6343/trac_6343-reviewer.patch) by mvngu created at 2009-07-16 23:59:47\n\nThe patch `trac_6343-reviewer.patch` fixes some typos and copy the docstring for `__init__()` in the class `InstanceTester` to the class itself. This is necessary as docstring in methods whose names begin with an underscore (i.e. `_`) would not show up in the reference manual.\n\n\n\nApart from that, here's a small issue. Can you provide examples and/or tests for the function `_test_pickling()` in `sage/structure/sage_object.pyx`? The doctest coverage for `sage/structure/sage_object.pyx` is very short of 50% and we don't want to make it more difficult to reach 100% coverage.",
    "created_at": "2009-07-16T23:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50696",
    "user": "mvngu"
}
```

Attachment [trac_6343-reviewer.patch](tarball://root/attachments/some-uuid/ticket6343/trac_6343-reviewer.patch) by mvngu created at 2009-07-16 23:59:47

The patch `trac_6343-reviewer.patch` fixes some typos and copy the docstring for `__init__()` in the class `InstanceTester` to the class itself. This is necessary as docstring in methods whose names begin with an underscore (i.e. `_`) would not show up in the reference manual.



Apart from that, here's a small issue. Can you provide examples and/or tests for the function `_test_pickling()` in `sage/structure/sage_object.pyx`? The doctest coverage for `sage/structure/sage_object.pyx` is very short of 50% and we don't want to make it more difficult to reach 100% coverage.



---

archive/issue_comments_050697.json:
```json
{
    "body": "Attachment [trac_6343-reviewer-nt.patch](tarball://root/attachments/some-uuid/ticket6343/trac_6343-reviewer-nt.patch) by @nthiery created at 2009-07-20 23:23:40\n\nReplying to [comment:13 mvngu]:\n> The patch `trac_6343-reviewer.patch` fixes some typos and copy the docstring for `__init__()` in the class `InstanceTester` to the class itself. This is necessary as docstring in methods whose names begin with an underscore (i.e. `_`) would not show up in the reference manual.\n\nAgreed, that's better (but not for that argument: my opinion is that _* methods, or at least _*_ and __*__ methods should show up in the manual; but that's another discussion).\n\nThanks for your doc fixes! I double checked them.\n\n> Apart from that, here's a small issue. Can you provide examples and/or tests for the function `_test_pickling()` in `sage/structure/sage_object.pyx`? The doctest coverage for `sage/structure/sage_object.pyx` is very short of 50% and we don't want to make it more difficult to reach 100% coverage.\n\nThanks also for spotting the missing doctest. The attached patch fixes this.",
    "created_at": "2009-07-20T23:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50697",
    "user": "@nthiery"
}
```

Attachment [trac_6343-reviewer-nt.patch](tarball://root/attachments/some-uuid/ticket6343/trac_6343-reviewer-nt.patch) by @nthiery created at 2009-07-20 23:23:40

Replying to [comment:13 mvngu]:
> The patch `trac_6343-reviewer.patch` fixes some typos and copy the docstring for `__init__()` in the class `InstanceTester` to the class itself. This is necessary as docstring in methods whose names begin with an underscore (i.e. `_`) would not show up in the reference manual.

Agreed, that's better (but not for that argument: my opinion is that _* methods, or at least _*_ and __*__ methods should show up in the manual; but that's another discussion).

Thanks for your doc fixes! I double checked them.

> Apart from that, here's a small issue. Can you provide examples and/or tests for the function `_test_pickling()` in `sage/structure/sage_object.pyx`? The doctest coverage for `sage/structure/sage_object.pyx` is very short of 50% and we don't want to make it more difficult to reach 100% coverage.

Thanks also for spotting the missing doctest. The attached patch fixes this.



---

archive/issue_comments_050698.json:
```json
{
    "body": "Everything looks good to me now.  Apply all patches.",
    "created_at": "2009-09-08T07:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50698",
    "user": "@mwhansen"
}
```

Everything looks good to me now.  Apply all patches.



---

archive/issue_comments_050699.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `trac_6343-sage_object-test-nt.patch`\n2. `trac_6343-reviewer.patch`\n3. `trac_6343-reviewer-nt.patch`",
    "created_at": "2009-09-08T11:09:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50699",
    "user": "mvngu"
}
```

Merged patches in this order:

1. `trac_6343-sage_object-test-nt.patch`
2. `trac_6343-reviewer.patch`
3. `trac_6343-reviewer-nt.patch`



---

archive/issue_comments_050700.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-08T11:09:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50700",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_050701.json:
```json
{
    "body": "Thanks Mike, thanks Minh!",
    "created_at": "2009-09-08T11:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50701",
    "user": "@nthiery"
}
```

Thanks Mike, thanks Minh!

# Issue 6343: [with patch, positive review] Adds TestSuite(object).run() generic testing framework

archive/issues_006343.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat cwitty @roed314 @saliola mvngu\n\nKeywords: testunit\n\nThis patch implements TestSuite(object).run()  which runs\nsystematic checks on the object. Here is a typical call:\n\n```\n     sage: TestSuite(ZZ).run(verbose = True)\n     running ._test_an_element() ... done\n     running ._test_element_pickling() ... done\n     running ._test_not_implemented_methods() ... done\n     running ._test_pickling() ... done\n```\nIn practice, TestSuite(o).run() runs all the methods named _test_* of the object o.\nThe _test_* methods are typically implemented by abstract super classes\nand in particular via categories, in order to enforce standard\nbehavior and API (_test_pickling, _test_an_element), or provide\nmathematical sanity checks (_test_associativity).\n\nFor consistent error reporting, the _test_* methods in turn must use\nthe new gadget sage.misc.sage_unittest.InstanceTester to actually\nrun the tests.\n\nThis is used by the category patches #5891 and followers\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6343\n\n",
    "closed_at": "2009-09-08T11:09:27Z",
    "created_at": "2009-06-16T22:21:54Z",
    "labels": [
        "component: doctest coverage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, positive review] Adds TestSuite(object).run() generic testing framework",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6343",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat cwitty @roed314 @saliola mvngu

Keywords: testunit

This patch implements TestSuite(object).run()  which runs
systematic checks on the object. Here is a typical call:

```
     sage: TestSuite(ZZ).run(verbose = True)
     running ._test_an_element() ... done
     running ._test_element_pickling() ... done
     running ._test_not_implemented_methods() ... done
     running ._test_pickling() ... done
```
In practice, TestSuite(o).run() runs all the methods named _test_* of the object o.
The _test_* methods are typically implemented by abstract super classes
and in particular via categories, in order to enforce standard
behavior and API (_test_pickling, _test_an_element), or provide
mathematical sanity checks (_test_associativity).

For consistent error reporting, the _test_* methods in turn must use
the new gadget sage.misc.sage_unittest.InstanceTester to actually
run the tests.

This is used by the category patches #5891 and followers


Issue created by migration from https://trac.sagemath.org/ticket/6343





---

archive/issue_comments_050588.json:
```json
{
    "body": "Change the name from obj.check() to obj._check().  It is not reasonable that if one does obj.<tab> on *any* Sage object, one sees check.  \n\nWilliam",
    "created_at": "2009-06-18T14:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50588",
    "user": "https://github.com/williamstein"
}
```

Change the name from obj.check() to obj._check().  It is not reasonable that if one does obj.<tab> on *any* Sage object, one sees check.  

William



---

archive/issue_comments_050589.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-18T16:12:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50589",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_050590.json:
```json
{
    "body": "Change the name from obj.check() to obj._check(). It is not reasonable that if one does obj.<tab> on *any* Sage object, one sees check.",
    "created_at": "2009-06-20T14:41:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50590",
    "user": "https://github.com/williamstein"
}
```

Change the name from obj.check() to obj._check(). It is not reasonable that if one does obj.<tab> on *any* Sage object, one sees check.



---

archive/issue_comments_050591.json:
```json
{
    "body": "Changing keywords from \"\" to \"testunit\".",
    "created_at": "2009-06-26T08:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50591",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "" to "testunit".



---

archive/issue_comments_050592.json:
```json
{
    "body": "Patch reworked, after the discussion on sage-devel.\n\nNote: After peeking again into the testunit framework, I finally went for TestSuite(object).run() which\nis most consistent with it, while being meaningful.\n\nThe otherwise discussed functionality TestSuite(object).associativity() will be implemented in a later patch\n(if deemed useful in the meantime).",
    "created_at": "2009-06-26T08:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50592",
    "user": "https://github.com/nthiery"
}
```

Patch reworked, after the discussion on sage-devel.

Note: After peeking again into the testunit framework, I finally went for TestSuite(object).run() which
is most consistent with it, while being meaningful.

The otherwise discussed functionality TestSuite(object).associativity() will be implemented in a later patch
(if deemed useful in the meantime).



---

archive/issue_comments_050593.json:
```json
{
    "body": "I like the new design and class/function names.",
    "created_at": "2009-07-08T14:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50593",
    "user": "https://github.com/williamstein"
}
```

I like the new design and class/function names.



---

archive/issue_comments_050594.json:
```json
{
    "body": "Attachment [trac_6343-sage_object-test-nt.patch](tarball://root/attachments/some-uuid/ticket6343/trac_6343-sage_object-test-nt.patch) by @nthiery created at 2009-07-10 22:27:48\n\nOops, the doctests were broken (I had forgotten to rename stuff in there)",
    "created_at": "2009-07-10T22:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50594",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_6343-sage_object-test-nt.patch](tarball://root/attachments/some-uuid/ticket6343/trac_6343-sage_object-test-nt.patch) by @nthiery created at 2009-07-10 22:27:48

Oops, the doctests were broken (I had forgotten to rename stuff in there)



---

archive/issue_comments_050595.json:
```json
{
    "body": "Looks good to me.  We just have to make sure to re-enable the missing tests when the category stuff is added.",
    "created_at": "2009-07-16T21:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50595",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  We just have to make sure to re-enable the missing tests when the category stuff is added.



---

archive/issue_comments_050596.json:
```json
{
    "body": "Thanks for the review!\nI just fixed my name to please my grand father :-)",
    "created_at": "2009-07-16T21:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50596",
    "user": "https://github.com/nthiery"
}
```

Thanks for the review!
I just fixed my name to please my grand father :-)



---

archive/issue_comments_050597.json:
```json
{
    "body": "No worries.  I really should just add key tomy keyboard layout :-)",
    "created_at": "2009-07-16T21:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50597",
    "user": "https://github.com/mwhansen"
}
```

No worries.  I really should just add key tomy keyboard layout :-)



---

archive/issue_comments_050598.json:
```json
{
    "body": "reviewer patch; fixes typos and docstring formatting",
    "created_at": "2009-07-16T23:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50598",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

reviewer patch; fixes typos and docstring formatting



---

archive/issue_comments_050599.json:
```json
{
    "body": "Attachment [trac_6343-reviewer.patch](tarball://root/attachments/some-uuid/ticket6343/trac_6343-reviewer.patch) by mvngu created at 2009-07-16 23:59:47\n\nThe patch `trac_6343-reviewer.patch` fixes some typos and copy the docstring for `__init__()` in the class `InstanceTester` to the class itself. This is necessary as docstring in methods whose names begin with an underscore (i.e. `_`) would not show up in the reference manual.\n\n\n\nApart from that, here's a small issue. Can you provide examples and/or tests for the function `_test_pickling()` in `sage/structure/sage_object.pyx`? The doctest coverage for `sage/structure/sage_object.pyx` is very short of 50% and we don't want to make it more difficult to reach 100% coverage.",
    "created_at": "2009-07-16T23:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50599",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6343-reviewer.patch](tarball://root/attachments/some-uuid/ticket6343/trac_6343-reviewer.patch) by mvngu created at 2009-07-16 23:59:47

The patch `trac_6343-reviewer.patch` fixes some typos and copy the docstring for `__init__()` in the class `InstanceTester` to the class itself. This is necessary as docstring in methods whose names begin with an underscore (i.e. `_`) would not show up in the reference manual.



Apart from that, here's a small issue. Can you provide examples and/or tests for the function `_test_pickling()` in `sage/structure/sage_object.pyx`? The doctest coverage for `sage/structure/sage_object.pyx` is very short of 50% and we don't want to make it more difficult to reach 100% coverage.



---

archive/issue_comments_050600.json:
```json
{
    "body": "Attachment [trac_6343-reviewer-nt.patch](tarball://root/attachments/some-uuid/ticket6343/trac_6343-reviewer-nt.patch) by @nthiery created at 2009-07-20 23:23:40\n\nReplying to [comment:13 mvngu]:\n> The patch `trac_6343-reviewer.patch` fixes some typos and copy the docstring for `__init__()` in the class `InstanceTester` to the class itself. This is necessary as docstring in methods whose names begin with an underscore (i.e. `_`) would not show up in the reference manual.\n\n\nAgreed, that's better (but not for that argument: my opinion is that _* methods, or at least _*_ and __*__ methods should show up in the manual; but that's another discussion).\n\nThanks for your doc fixes! I double checked them.\n\n> Apart from that, here's a small issue. Can you provide examples and/or tests for the function `_test_pickling()` in `sage/structure/sage_object.pyx`? The doctest coverage for `sage/structure/sage_object.pyx` is very short of 50% and we don't want to make it more difficult to reach 100% coverage.\n\n\nThanks also for spotting the missing doctest. The attached patch fixes this.",
    "created_at": "2009-07-20T23:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50600",
    "user": "https://github.com/nthiery"
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

archive/issue_comments_050601.json:
```json
{
    "body": "Everything looks good to me now.  Apply all patches.",
    "created_at": "2009-09-08T07:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50601",
    "user": "https://github.com/mwhansen"
}
```

Everything looks good to me now.  Apply all patches.



---

archive/issue_comments_050602.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `trac_6343-sage_object-test-nt.patch`\n2. `trac_6343-reviewer.patch`\n3. `trac_6343-reviewer-nt.patch`",
    "created_at": "2009-09-08T11:09:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50602",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged patches in this order:

1. `trac_6343-sage_object-test-nt.patch`
2. `trac_6343-reviewer.patch`
3. `trac_6343-reviewer-nt.patch`



---

archive/issue_comments_050603.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-08T11:09:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50603",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_014920.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-08T11:09:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6343#event-14920"
}
```



---

archive/issue_comments_050604.json:
```json
{
    "body": "Thanks Mike, thanks Minh!",
    "created_at": "2009-09-08T11:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6343#issuecomment-50604",
    "user": "https://github.com/nthiery"
}
```

Thanks Mike, thanks Minh!

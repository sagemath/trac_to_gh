# Issue 8208: Click "No" actually publishes a worksheet in SageNB 0.7.4

archive/issues_008208.json:
```json
{
    "body": "Assignee: was\n\nCC:  timdumol acleone was\n\nFollow-up to #7786.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8208\n\n",
    "created_at": "2010-02-07T16:20:18Z",
    "labels": [
        "notebook",
        "critical",
        "bug"
    ],
    "title": "Click \"No\" actually publishes a worksheet in SageNB 0.7.4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8208",
    "user": "mpatel"
}
```
Assignee: was

CC:  timdumol acleone was

Follow-up to #7786.

Issue created by migration from https://trac.sagemath.org/ticket/8208





---

archive/issue_comments_072383.json:
```json
{
    "body": "Revert to pre-#7786 buttons.  sagenb repo.",
    "created_at": "2010-02-07T16:22:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8208#issuecomment-72383",
    "user": "mpatel"
}
```

Revert to pre-#7786 buttons.  sagenb repo.



---

archive/issue_comments_072384.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-07T16:22:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8208#issuecomment-72384",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072385.json:
```json
{
    "body": "Attachment [trac_8208-publish_buttons.patch](tarball://root/attachments/some-uuid/ticket8208/trac_8208-publish_buttons.patch) by mpatel created at 2010-02-07 16:22:37",
    "created_at": "2010-02-07T16:22:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8208#issuecomment-72385",
    "user": "mpatel"
}
```

Attachment [trac_8208-publish_buttons.patch](tarball://root/attachments/some-uuid/ticket8208/trac_8208-publish_buttons.patch) by mpatel created at 2010-02-07 16:22:37



---

archive/issue_comments_072386.json:
```json
{
    "body": "We need to fix the Selenium tests, too.",
    "created_at": "2010-02-07T16:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8208#issuecomment-72386",
    "user": "mpatel"
}
```

We need to fix the Selenium tests, too.



---

archive/issue_comments_072387.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-07T16:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8208#issuecomment-72387",
    "user": "mpatel"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072388.json:
```json
{
    "body": "ERROR: test_3960 (sagenb.testing.tests.test_accounts.TestAccounts)\nERROR: test_7433 (sagenb.testing.tests.test_worksheet.TestWorksheet)\nERROR: test_7428 (sagenb.testing.tests.test_worksheet_list.TestWorksheetList)\nERROR: test_7444 (sagenb.testing.tests.test_worksheet_list.TestWorksheetList)\n\nException: ERROR: Element //button[text()='Yes'] not found\n\nOr maybe we can fix the buttons in another way.",
    "created_at": "2010-02-07T16:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8208#issuecomment-72388",
    "user": "mpatel"
}
```

ERROR: test_3960 (sagenb.testing.tests.test_accounts.TestAccounts)
ERROR: test_7433 (sagenb.testing.tests.test_worksheet.TestWorksheet)
ERROR: test_7428 (sagenb.testing.tests.test_worksheet_list.TestWorksheetList)
ERROR: test_7444 (sagenb.testing.tests.test_worksheet_list.TestWorksheetList)

Exception: ERROR: Element //button[text()='Yes'] not found

Or maybe we can fix the buttons in another way.



---

archive/issue_comments_072389.json:
```json
{
    "body": "We should also check that all of the publish buttons work in WebKit browsers.",
    "created_at": "2010-02-07T16:42:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8208#issuecomment-72389",
    "user": "mpatel"
}
```

We should also check that all of the publish buttons work in WebKit browsers.



---

archive/issue_comments_072390.json:
```json
{
    "body": "I did test this patch, and it definitely *works* irregardless of the test issue.  I'll likely apply this to sagenb.org.  I was going to give it a positive review, but obviously the selenium test failure is an issue.",
    "created_at": "2010-02-07T17:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8208#issuecomment-72390",
    "user": "was"
}
```

I did test this patch, and it definitely *works* irregardless of the test issue.  I'll likely apply this to sagenb.org.  I was going to give it a positive review, but obviously the selenium test failure is an issue.



---

archive/issue_comments_072391.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-07T23:08:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8208#issuecomment-72391",
    "user": "acleone"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072392.json:
```json
{
    "body": "I added a selenium test (test_8208).  Here's the output without the fix\n\n```\ntest_3960 (tests.test_accounts.TestAccounts) ... ok\ntest_4050 (tests.test_accounts.TestAccounts) ... ok\ntest_4088 (tests.test_accounts.TestAccounts) ... ok\ntest_3711 (tests.test_worksheet.TestWorksheet) ... ok\ntest_3957 (tests.test_worksheet.TestWorksheet) ... ok\ntest_7341 (tests.test_worksheet.TestWorksheet) ... ok\ntest_7433 (tests.test_worksheet.TestWorksheet) ... ok\ntest_7434 (tests.test_worksheet.TestWorksheet) ... ok\ntest_8208 (tests.test_worksheet.TestWorksheet) ... FAIL\ntest_edit (tests.test_worksheet.TestWorksheet) ... ok\ntest_operations1 (tests.test_worksheet.TestWorksheet) ... ok\ntest_simple_evaluation (tests.test_worksheet.TestWorksheet) ... ok\ntest_7428 (tests.test_worksheet_list.TestWorksheetList) ... ok\ntest_7444 (tests.test_worksheet_list.TestWorksheetList) ... ok\ntest_creating_worksheet (tests.test_worksheet_list.TestWorksheetList) ... ok\ntest_opening_worksheet (tests.test_worksheet_list.TestWorksheetList) ... ok\ntest_searching_for_worksheets (tests.test_worksheet_list.TestWorksheetList) ... ok\n\n======================================================================\nFAIL: test_8208 (tests.test_worksheet.TestWorksheet)\n----------------------------------------------------------------------\nTraceback (most recent call last):\n  File \"/home/alex/sage-dev/sagenb-0.7.4/src/sagenb/sagenb/testing/tests/test_worksheet.py\", line 231, in test_8208\n    self.assertFalse(self.is_worksheet_published('not_p_ws'))\nAssertionError\n\n----------------------------------------------------------------------\nRan 17 tests in 384.271s\n\nFAILED (failures=1)\n```\n\n\nAfter the fix:\n\n```\ntest_3960 (tests.test_accounts.TestAccounts) ... ok\ntest_4050 (tests.test_accounts.TestAccounts) ... ok\ntest_4088 (tests.test_accounts.TestAccounts) ... ok\ntest_3711 (tests.test_worksheet.TestWorksheet) ... ok\ntest_3957 (tests.test_worksheet.TestWorksheet) ... ok\ntest_7341 (tests.test_worksheet.TestWorksheet) ... ok\ntest_7433 (tests.test_worksheet.TestWorksheet) ... ok\ntest_7434 (tests.test_worksheet.TestWorksheet) ... ok\ntest_8208 (tests.test_worksheet.TestWorksheet) ... ok\ntest_edit (tests.test_worksheet.TestWorksheet) ... ok\ntest_operations1 (tests.test_worksheet.TestWorksheet) ... ok\ntest_simple_evaluation (tests.test_worksheet.TestWorksheet) ... ok\ntest_7428 (tests.test_worksheet_list.TestWorksheetList) ... ok\ntest_7444 (tests.test_worksheet_list.TestWorksheetList) ... ok\ntest_creating_worksheet (tests.test_worksheet_list.TestWorksheetList) ... ok\ntest_opening_worksheet (tests.test_worksheet_list.TestWorksheetList) ... ok\ntest_searching_for_worksheets (tests.test_worksheet_list.TestWorksheetList) ... ok\n\n----------------------------------------------------------------------\nRan 17 tests in 381.556s\n\nOK\n```\n",
    "created_at": "2010-02-07T23:08:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8208#issuecomment-72392",
    "user": "acleone"
}
```

I added a selenium test (test_8208).  Here's the output without the fix

```
test_3960 (tests.test_accounts.TestAccounts) ... ok
test_4050 (tests.test_accounts.TestAccounts) ... ok
test_4088 (tests.test_accounts.TestAccounts) ... ok
test_3711 (tests.test_worksheet.TestWorksheet) ... ok
test_3957 (tests.test_worksheet.TestWorksheet) ... ok
test_7341 (tests.test_worksheet.TestWorksheet) ... ok
test_7433 (tests.test_worksheet.TestWorksheet) ... ok
test_7434 (tests.test_worksheet.TestWorksheet) ... ok
test_8208 (tests.test_worksheet.TestWorksheet) ... FAIL
test_edit (tests.test_worksheet.TestWorksheet) ... ok
test_operations1 (tests.test_worksheet.TestWorksheet) ... ok
test_simple_evaluation (tests.test_worksheet.TestWorksheet) ... ok
test_7428 (tests.test_worksheet_list.TestWorksheetList) ... ok
test_7444 (tests.test_worksheet_list.TestWorksheetList) ... ok
test_creating_worksheet (tests.test_worksheet_list.TestWorksheetList) ... ok
test_opening_worksheet (tests.test_worksheet_list.TestWorksheetList) ... ok
test_searching_for_worksheets (tests.test_worksheet_list.TestWorksheetList) ... ok

======================================================================
FAIL: test_8208 (tests.test_worksheet.TestWorksheet)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/alex/sage-dev/sagenb-0.7.4/src/sagenb/sagenb/testing/tests/test_worksheet.py", line 231, in test_8208
    self.assertFalse(self.is_worksheet_published('not_p_ws'))
AssertionError

----------------------------------------------------------------------
Ran 17 tests in 384.271s

FAILED (failures=1)
```


After the fix:

```
test_3960 (tests.test_accounts.TestAccounts) ... ok
test_4050 (tests.test_accounts.TestAccounts) ... ok
test_4088 (tests.test_accounts.TestAccounts) ... ok
test_3711 (tests.test_worksheet.TestWorksheet) ... ok
test_3957 (tests.test_worksheet.TestWorksheet) ... ok
test_7341 (tests.test_worksheet.TestWorksheet) ... ok
test_7433 (tests.test_worksheet.TestWorksheet) ... ok
test_7434 (tests.test_worksheet.TestWorksheet) ... ok
test_8208 (tests.test_worksheet.TestWorksheet) ... ok
test_edit (tests.test_worksheet.TestWorksheet) ... ok
test_operations1 (tests.test_worksheet.TestWorksheet) ... ok
test_simple_evaluation (tests.test_worksheet.TestWorksheet) ... ok
test_7428 (tests.test_worksheet_list.TestWorksheetList) ... ok
test_7444 (tests.test_worksheet_list.TestWorksheetList) ... ok
test_creating_worksheet (tests.test_worksheet_list.TestWorksheetList) ... ok
test_opening_worksheet (tests.test_worksheet_list.TestWorksheetList) ... ok
test_searching_for_worksheets (tests.test_worksheet_list.TestWorksheetList) ... ok

----------------------------------------------------------------------
Ran 17 tests in 381.556s

OK
```




---

archive/issue_comments_072393.json:
```json
{
    "body": "Attachment [trac_8208-no-publish.patch](tarball://root/attachments/some-uuid/ticket8208/trac_8208-no-publish.patch) by acleone created at 2010-02-07 23:14:46\n\nChanges buttons to inputs and adds a Selenium test",
    "created_at": "2010-02-07T23:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8208#issuecomment-72393",
    "user": "acleone"
}
```

Attachment [trac_8208-no-publish.patch](tarball://root/attachments/some-uuid/ticket8208/trac_8208-no-publish.patch) by acleone created at 2010-02-07 23:14:46

Changes buttons to inputs and adds a Selenium test



---

archive/issue_comments_072394.json:
```json
{
    "body": "The patch looks good.  Thanks for adding the test!",
    "created_at": "2010-02-09T03:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8208#issuecomment-72394",
    "user": "mpatel"
}
```

The patch looks good.  Thanks for adding the test!



---

archive/issue_comments_072395.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-09T03:11:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8208#issuecomment-72395",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072396.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-10T18:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8208",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8208#issuecomment-72396",
    "user": "mpatel"
}
```

Resolution: fixed

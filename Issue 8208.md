# Issue 8208: Click "No" actually publishes a worksheet in SageNB 0.7.4

Issue created by migration from https://trac.sagemath.org/ticket/8208

Original creator: mpatel

Original creation time: 2010-02-07 16:20:18

Assignee: was

CC:  timdumol acleone was

Follow-up to #7786.


---

Comment by mpatel created at 2010-02-07 16:22:06

Revert to pre-#7786 buttons.  sagenb repo.


---

Comment by mpatel created at 2010-02-07 16:22:37

Changing status from new to needs_review.


---

Attachment


---

Comment by mpatel created at 2010-02-07 16:28:39

We need to fix the Selenium tests, too.


---

Comment by mpatel created at 2010-02-07 16:28:39

Changing status from needs_review to needs_work.


---

Comment by mpatel created at 2010-02-07 16:31:02

ERROR: test_3960 (sagenb.testing.tests.test_accounts.TestAccounts)
ERROR: test_7433 (sagenb.testing.tests.test_worksheet.TestWorksheet)
ERROR: test_7428 (sagenb.testing.tests.test_worksheet_list.TestWorksheetList)
ERROR: test_7444 (sagenb.testing.tests.test_worksheet_list.TestWorksheetList)

Exception: ERROR: Element //button[text()='Yes'] not found

Or maybe we can fix the buttons in another way.


---

Comment by mpatel created at 2010-02-07 16:42:02

We should also check that all of the publish buttons work in WebKit browsers.


---

Comment by was created at 2010-02-07 17:42:08

I did test this patch, and it definitely *works* irregardless of the test issue.  I'll likely apply this to sagenb.org.  I was going to give it a positive review, but obviously the selenium test failure is an issue.


---

Comment by acleone created at 2010-02-07 23:08:59

Changing status from needs_work to needs_review.


---

Comment by acleone created at 2010-02-07 23:08:59

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

Attachment

Changes buttons to inputs and adds a Selenium test


---

Comment by mpatel created at 2010-02-09 03:11:23

The patch looks good.  Thanks for adding the test!


---

Comment by mpatel created at 2010-02-09 03:11:23

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-10 18:31:12

Resolution: fixed

# Issue 7343: SageNB -- Add a Selenium test suite.

archive/issues_007343.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein @qed777\n\nInclusion of a test suite will prevent regressions, and make development *much* easier.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7343\n\n",
    "created_at": "2009-10-29T04:05:54Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "SageNB -- Add a Selenium test suite.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7343",
    "user": "https://github.com/TimDumol"
}
```
Assignee: boothby

CC:  @williamstein @qed777

Inclusion of a test suite will prevent regressions, and make development *much* easier.

Issue created by migration from https://trac.sagemath.org/ticket/7343





---

archive/issue_comments_061333.json:
```json
{
    "body": "New Selenium test suite.",
    "created_at": "2009-10-29T04:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61333",
    "user": "https://github.com/TimDumol"
}
```

New Selenium test suite.



---

archive/issue_comments_061334.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-29T04:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61334",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061335.json:
```json
{
    "body": "Attachment [trac_7343-selenium-tests.patch](tarball://root/attachments/some-uuid/ticket7343/trac_7343-selenium-tests.patch) by @TimDumol created at 2009-10-29 04:08:58\n\nDepends on #7309, #7310 and #7332. This is an initial version of the test suite. Many of these test cases were adapted and mildly modified from Mike Hansen's original Selenium test code.\n\nMore test cases to come, but I feel that having a test suite included asap is essential.",
    "created_at": "2009-10-29T04:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61335",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7343-selenium-tests.patch](tarball://root/attachments/some-uuid/ticket7343/trac_7343-selenium-tests.patch) by @TimDumol created at 2009-10-29 04:08:58

Depends on #7309, #7310 and #7332. This is an initial version of the test suite. Many of these test cases were adapted and mildly modified from Mike Hansen's original Selenium test code.

More test cases to come, but I feel that having a test suite included asap is essential.



---

archive/issue_comments_061336.json:
```json
{
    "body": "Running the test suite:\n\n```\nsage: from sagenb.testing.run_tests import run_tests; run_tests()\n```\n\n\nNote that this requires an instance of the Selenium server running on port 4444. The Selenium server can be downloaded from http://seleniumhq.org/download/ as part of the Selenium RC package and can be run with `java -jar selenium-server.jar`. This could not be included in the patch due to possible conflicts with the system binaries and libraries (Firefox, etc.).",
    "created_at": "2009-10-29T04:12:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61336",
    "user": "https://github.com/TimDumol"
}
```

Running the test suite:

```
sage: from sagenb.testing.run_tests import run_tests; run_tests()
```


Note that this requires an instance of the Selenium server running on port 4444. The Selenium server can be downloaded from http://seleniumhq.org/download/ as part of the Selenium RC package and can be run with `java -jar selenium-server.jar`. This could not be included in the patch due to possible conflicts with the system binaries and libraries (Firefox, etc.).



---

archive/issue_comments_061337.json:
```json
{
    "body": "A note: There is a failure in `test_searching_worksheets`. It is an actual bug -- the requisite javascript libraries are not loaded.",
    "created_at": "2009-10-29T04:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61337",
    "user": "https://github.com/TimDumol"
}
```

A note: There is a failure in `test_searching_worksheets`. It is an actual bug -- the requisite javascript libraries are not loaded.



---

archive/issue_comments_061338.json:
```json
{
    "body": "The previous patch had some errors (*~ files, missing file).",
    "created_at": "2009-10-29T05:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61338",
    "user": "https://github.com/TimDumol"
}
```

The previous patch had some errors (*~ files, missing file).



---

archive/issue_comments_061339.json:
```json
{
    "body": "Attachment [trac_7343-selenium-tests.3.patch](tarball://root/attachments/some-uuid/ticket7343/trac_7343-selenium-tests.3.patch) by @TimDumol created at 2009-10-29 12:06:04\n\nAdded a test to confirm that #7341 works.",
    "created_at": "2009-10-29T12:06:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61339",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7343-selenium-tests.3.patch](tarball://root/attachments/some-uuid/ticket7343/trac_7343-selenium-tests.3.patch) by @TimDumol created at 2009-10-29 12:06:04

Added a test to confirm that #7341 works.



---

archive/issue_comments_061340.json:
```json
{
    "body": "Added \"Edit worksheet\" test. Made sure that no orphan processes are left behind by failed tests.",
    "created_at": "2009-10-30T13:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61340",
    "user": "https://github.com/TimDumol"
}
```

Added "Edit worksheet" test. Made sure that no orphan processes are left behind by failed tests.



---

archive/issue_comments_061341.json:
```json
{
    "body": "Attachment [trac_7343-selenium-tests.4.patch](tarball://root/attachments/some-uuid/ticket7343/trac_7343-selenium-tests.4.patch) by @qed777 created at 2009-10-31 15:10:51\n\nSo far, this looks great!  I'm still reading through the [Selenium-RC documentation](http://seleniumhq.org/docs/05_selenium_rc.html), but I think I can review this ticket formally tomorrow.  At the risk of asking too soon: Can we specify the particular browser to test in `run_tests()`?  Another potentially useful option, at least for Firefox: Use, e.g., `firefox -P selenium-test -remote \"openURL($*, new-tab)\"`, to open multiple tabs instead of windows.  I'll investigate.\n\nAside: It's nice that both [Selenium](http://seleniumhq.org/) and [FunkLoad](http://funkload.nuxeo.org/) are build on Python's [unittest framework](http://docs.python.org/library/unittest.html).  Of course, FunkLoad only simulates a browser, but I think we can attain approximate parity between the notebook's functional (i.e., with Selenium) and load (i.e., with FunkLoad) tests.  Selenium's advantage is that it tests real-world browsers, but even with [Selenium-Grid](http://selenium-grid.seleniumhq.org/), we'd have difficulty (I think) simulating thousands of simultaneous notebook users.",
    "created_at": "2009-10-31T15:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61341",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7343-selenium-tests.4.patch](tarball://root/attachments/some-uuid/ticket7343/trac_7343-selenium-tests.4.patch) by @qed777 created at 2009-10-31 15:10:51

So far, this looks great!  I'm still reading through the [Selenium-RC documentation](http://seleniumhq.org/docs/05_selenium_rc.html), but I think I can review this ticket formally tomorrow.  At the risk of asking too soon: Can we specify the particular browser to test in `run_tests()`?  Another potentially useful option, at least for Firefox: Use, e.g., `firefox -P selenium-test -remote "openURL($*, new-tab)"`, to open multiple tabs instead of windows.  I'll investigate.

Aside: It's nice that both [Selenium](http://seleniumhq.org/) and [FunkLoad](http://funkload.nuxeo.org/) are build on Python's [unittest framework](http://docs.python.org/library/unittest.html).  Of course, FunkLoad only simulates a browser, but I think we can attain approximate parity between the notebook's functional (i.e., with Selenium) and load (i.e., with FunkLoad) tests.  Selenium's advantage is that it tests real-world browsers, but even with [Selenium-Grid](http://selenium-grid.seleniumhq.org/), we'd have difficulty (I think) simulating thousands of simultaneous notebook users.



---

archive/issue_comments_061342.json:
```json
{
    "body": "Possibly useful: [HTMLTestRunner.py](http://tungwaiyip.info/software/HTMLTestRunner.html)?",
    "created_at": "2009-10-31T16:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61342",
    "user": "https://github.com/qed777"
}
```

Possibly useful: [HTMLTestRunner.py](http://tungwaiyip.info/software/HTMLTestRunner.html)?



---

archive/issue_comments_061343.json:
```json
{
    "body": "Tweaked a few tests.  See the comment.  Apply only this patch.",
    "created_at": "2009-11-01T10:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61343",
    "user": "https://github.com/qed777"
}
```

Tweaked a few tests.  See the comment.  Apply only this patch.



---

archive/issue_comments_061344.json:
```json
{
    "body": "Attachment [trac_7343-selenium-tests.5.patch](tarball://root/attachments/some-uuid/ticket7343/trac_7343-selenium-tests.5.patch) by @qed777 created at 2009-11-01 10:45:58\n\nVersion 5:\n\n* Fixes `TestWorksheet.test_edit`.\n\n* Changes `TestWorksheet.test_7341`, for now, to use\n\n```python\nsel.get_eval('window.evaluate_cell_introspection(1, null, null);')\n```\n\n   instead of\n\n```python\nself.tab('cell_input_1')\n```\n\n   For some reason, `self.selenium.key_press_native(9)` doesn't consistently send a TAB character in Firefox 3.5.3, at least for me.  I think the problem is Selenium's.\n\n* Simplifies `TestWorksheetsList.test_searching_for_worksheets`.  Is searching published worksheets broken in sagenb's tip?  I see, e.g.,\n\n```\n        exceptions.IOError: [Errno 2] No such file or directory: '/home/.sage/sage_notebook.sagenb/home/pub/12/worksheet.html\n```\n\n   if I publish a worksheet, visit \"Published,\" and try a search.  Restarting the server fixes the problem.\n\nAnyway, this is great work!  To the extent it counts, my review is positive.",
    "created_at": "2009-11-01T10:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61344",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7343-selenium-tests.5.patch](tarball://root/attachments/some-uuid/ticket7343/trac_7343-selenium-tests.5.patch) by @qed777 created at 2009-11-01 10:45:58

Version 5:

* Fixes `TestWorksheet.test_edit`.

* Changes `TestWorksheet.test_7341`, for now, to use

```python
sel.get_eval('window.evaluate_cell_introspection(1, null, null);')
```

   instead of

```python
self.tab('cell_input_1')
```

   For some reason, `self.selenium.key_press_native(9)` doesn't consistently send a TAB character in Firefox 3.5.3, at least for me.  I think the problem is Selenium's.

* Simplifies `TestWorksheetsList.test_searching_for_worksheets`.  Is searching published worksheets broken in sagenb's tip?  I see, e.g.,

```
        exceptions.IOError: [Errno 2] No such file or directory: '/home/.sage/sage_notebook.sagenb/home/pub/12/worksheet.html
```

   if I publish a worksheet, visit "Published," and try a search.  Restarting the server fixes the problem.

Anyway, this is great work!  To the extent it counts, my review is positive.



---

archive/issue_comments_061345.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-01T10:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61345",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061346.json:
```json
{
    "body": "A sample Selenium-RC startup script:\n\n```sh\n#!/bin/bash\nJAVA=\"/usr/java/latest/bin/java\"\nSEL_DIR=\"/home/apps/selenium/selenium-remote-control-1.0.1/selenium-serve\nr-1.0.1\"\n\nFF_BROW=\"*firefox3\"\nFF_EXEC=\"/usr/lib64/firefox-3.5.3/firefox\"\nFF_PROF=\"/home/sage/selenium/firefox/selenium1\"\nOP_BROW=\"*opera\"\nOP_EXEC=\"/usr/lib/opera/opera\"\nCR_BROW=\"*chrome\"\nCR_EXEC=\"/usr/lib64/chromium-browser/chromium-browser\"\n\nBROW=\"$FF_BROW\"\nBROW_EXEC=\"$FF_EXEC\"\n\nOPTS=\"\"\n#OPTS=\"$OPTS -firefoxProfileTemplate $FF_PROF\"\nOPTS=\"$OPTS -singleWindow\"\n#OPTS=\"$OPTS -browserSessionReuse\"\n#OPTS=\"$OPTS -ensureCleanSession\"\n#OPTS=\"$OPTS -debug\"\n#OPTS=\"$OPTS -browserSideLog\"\n#OPTS=\"$OPTS -log test.log\"\n#OPTS=\"$OPTS -trustAllSSLCertificates\"\n#OPTS=\"$OPTS -forcedBrowserMode $BROW\"\nOPTS=\"$OPTS -forcedBrowserModeRestOfLine $BROW $BROW_EXEC\"\n\n$JAVA -jar \"$SEL_DIR/selenium-server.jar\" $* $OPTS \n```\n\n\nNote: Opera 10 and Chromium are not supported.",
    "created_at": "2009-11-04T16:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61346",
    "user": "https://github.com/qed777"
}
```

A sample Selenium-RC startup script:

```sh
#!/bin/bash
JAVA="/usr/java/latest/bin/java"
SEL_DIR="/home/apps/selenium/selenium-remote-control-1.0.1/selenium-serve
r-1.0.1"

FF_BROW="*firefox3"
FF_EXEC="/usr/lib64/firefox-3.5.3/firefox"
FF_PROF="/home/sage/selenium/firefox/selenium1"
OP_BROW="*opera"
OP_EXEC="/usr/lib/opera/opera"
CR_BROW="*chrome"
CR_EXEC="/usr/lib64/chromium-browser/chromium-browser"

BROW="$FF_BROW"
BROW_EXEC="$FF_EXEC"

OPTS=""
#OPTS="$OPTS -firefoxProfileTemplate $FF_PROF"
OPTS="$OPTS -singleWindow"
#OPTS="$OPTS -browserSessionReuse"
#OPTS="$OPTS -ensureCleanSession"
#OPTS="$OPTS -debug"
#OPTS="$OPTS -browserSideLog"
#OPTS="$OPTS -log test.log"
#OPTS="$OPTS -trustAllSSLCertificates"
#OPTS="$OPTS -forcedBrowserMode $BROW"
OPTS="$OPTS -forcedBrowserModeRestOfLine $BROW $BROW_EXEC"

$JAVA -jar "$SEL_DIR/selenium-server.jar" $* $OPTS 
```


Note: Opera 10 and Chromium are not supported.



---

archive/issue_comments_061347.json:
```json
{
    "body": "Replying to [comment:5 mpatel]:\n> Possibly useful: [HTMLTestRunner.py](http://tungwaiyip.info/software/HTMLTestRunner.html)?\n\nSee #7390.",
    "created_at": "2009-11-04T20:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61347",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:5 mpatel]:
> Possibly useful: [HTMLTestRunner.py](http://tungwaiyip.info/software/HTMLTestRunner.html)?

See #7390.



---

archive/issue_comments_061348.json:
```json
{
    "body": "Unfortunately, I can't use any of this under OS X, because the sqlite libraries included in OS X and Firefox are incompatible: \n\n* http://jira.openqa.org/browse/SRC-743\n\n* https://bugzilla.mozilla.org/show_bug.cgi?id=513747\n\n\nAfter nearly two hours of trying to get this to work, I'm giving up for now.  I guess Selenium is just broken on OS X for now.   Hopefully the Firefox and/or Selenium devs will fix this asap.    In the meantime, this is a vote from me to check out FunkLoad: \"Of course, FunkLoad only simulates a browser, but I think we can attain approximate parity between the notebook's functional (i.e., with Selenium) and load (i.e., with FunkLoad) tests.\"   If nothing else, it would be really good to have a test suite that we can include and that anybody can trivially use with no confusing (or in my case, impossible) setup and configuration issues.",
    "created_at": "2009-11-09T03:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61348",
    "user": "https://github.com/williamstein"
}
```

Unfortunately, I can't use any of this under OS X, because the sqlite libraries included in OS X and Firefox are incompatible: 

* http://jira.openqa.org/browse/SRC-743

* https://bugzilla.mozilla.org/show_bug.cgi?id=513747


After nearly two hours of trying to get this to work, I'm giving up for now.  I guess Selenium is just broken on OS X for now.   Hopefully the Firefox and/or Selenium devs will fix this asap.    In the meantime, this is a vote from me to check out FunkLoad: "Of course, FunkLoad only simulates a browser, but I think we can attain approximate parity between the notebook's functional (i.e., with Selenium) and load (i.e., with FunkLoad) tests."   If nothing else, it would be really good to have a test suite that we can include and that anybody can trivially use with no confusing (or in my case, impossible) setup and configuration issues.



---

archive/issue_comments_061349.json:
```json
{
    "body": "Further comments about this:\n\n  (1) I tried to use FunkLoad to test Sage (again in OS X) for a while, and got nowhere.  It seems to be a mess and not very polished.   Evidently it exists because some company wrote it and thought it might be useful to the community, so they released it.    I'm dubious about FunkLoad. \n \n  (2) No matter what, I think we need functional testing of the sage notebook that works on our build farms.  There's no way Selenium can do that.    I think we need something else to complement Selenium, possibly just something straightforward written in python using urllib, urllib2, etc.",
    "created_at": "2009-11-09T18:48:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61349",
    "user": "https://github.com/williamstein"
}
```

Further comments about this:

  (1) I tried to use FunkLoad to test Sage (again in OS X) for a while, and got nowhere.  It seems to be a mess and not very polished.   Evidently it exists because some company wrote it and thought it might be useful to the community, so they released it.    I'm dubious about FunkLoad. 
 
  (2) No matter what, I think we need functional testing of the sage notebook that works on our build farms.  There's no way Selenium can do that.    I think we need something else to complement Selenium, possibly just something straightforward written in python using urllib, urllib2, etc.



---

archive/issue_comments_061350.json:
```json
{
    "body": "Some browser drivers and/or simulators:\n\n* [FunkLoad](http://funkload.nuxeo.org/) simulates.\n* [Pylot](http://www.pylot.org/) simulates.\n* [Sahi](http://sahi.co.in/w/) drives.\n* [Selenium RC](http://seleniumhq.org/) drives but see WebDriver below.  [Selenium Grid](http://selenium-grid.seleniumhq.org/) drives Selenium RC.\n* [Watir](http://watir.com/) drives, but [Celerity](http://celerity.rubyforge.org/) simulates.\n* [WebDriver](http://code.google.com/p/webdriver/) is merging with [Selenium](http://code.google.com/p/selenium/).  See [this blog post](http://google-opensource.blogspot.com/2009/05/introducing-webdriver.html) and [the FAQ](http://code.google.com/p/selenium/wiki/FrequentlyAskedQuestions).  It drives and simulates.  Already?\n* [Windmill](http://www.getwindmill.com/) drives.\n* [zope.testbrowser](http://pypi.python.org/pypi/zope.testbrowser) simulates.\n\nI apologize for any misclassifications.  Some of the simulators can simulate JS, to a degree.  I *think* these are all based on [HtmlUnit](http://htmlunit.sourceforge.net/).\n\nIt would be great if we could write tests in just one actively developed and supported framework/API but be able to run both truly functional and simulated tests.  Selenium/WebDriver *may* be(come) that framework.",
    "created_at": "2009-11-10T02:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61350",
    "user": "https://github.com/qed777"
}
```

Some browser drivers and/or simulators:

* [FunkLoad](http://funkload.nuxeo.org/) simulates.
* [Pylot](http://www.pylot.org/) simulates.
* [Sahi](http://sahi.co.in/w/) drives.
* [Selenium RC](http://seleniumhq.org/) drives but see WebDriver below.  [Selenium Grid](http://selenium-grid.seleniumhq.org/) drives Selenium RC.
* [Watir](http://watir.com/) drives, but [Celerity](http://celerity.rubyforge.org/) simulates.
* [WebDriver](http://code.google.com/p/webdriver/) is merging with [Selenium](http://code.google.com/p/selenium/).  See [this blog post](http://google-opensource.blogspot.com/2009/05/introducing-webdriver.html) and [the FAQ](http://code.google.com/p/selenium/wiki/FrequentlyAskedQuestions).  It drives and simulates.  Already?
* [Windmill](http://www.getwindmill.com/) drives.
* [zope.testbrowser](http://pypi.python.org/pypi/zope.testbrowser) simulates.

I apologize for any misclassifications.  Some of the simulators can simulate JS, to a degree.  I *think* these are all based on [HtmlUnit](http://htmlunit.sourceforge.net/).

It would be great if we could write tests in just one actively developed and supported framework/API but be able to run both truly functional and simulated tests.  Selenium/WebDriver *may* be(come) that framework.



---

archive/issue_comments_061351.json:
```json
{
    "body": "By the way, this ticket depends on #7309, #7310, and #7332.",
    "created_at": "2009-11-10T03:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61351",
    "user": "https://github.com/qed777"
}
```

By the way, this ticket depends on #7309, #7310, and #7332.



---

archive/issue_comments_061352.json:
```json
{
    "body": "[The Grinder](http://grinder.sourceforge.net/), a Java load testing framework, has Jython bindings.  It might be worth a closer look.",
    "created_at": "2009-11-10T13:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61352",
    "user": "https://github.com/qed777"
}
```

[The Grinder](http://grinder.sourceforge.net/), a Java load testing framework, has Jython bindings.  It might be worth a closer look.



---

archive/issue_comments_061353.json:
```json
{
    "body": "Notes:\n\n*  I tried testing WebDriver's Python bindings to no avail.  It may be best to wait for a post-merger release of Selenium.\n\n* Pylot test cases must be written in XML, which is not as expressive as Python.\n\n* Can we use Selenium Grid with a Linux virtual machine to work around the OS X problem, for now?\n\n* zope.testbrowser seems promising for light-weight functional testing.\n\n* For load tests, I think The Grinder and (yes) FunkLoad are worth a closer look.  To get some data, I'll try to extend the simple FL test I ran recently to more complicated scenarios.  The Grinder may well be a better choice, although it's written in Java, since it seems to be mature, well-documented, and actively developed.  Moreover, we can write tests in Python, [more or less](http://grinder.sourceforge.net/g3/tutorial-perks.html).",
    "created_at": "2009-11-11T08:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61353",
    "user": "https://github.com/qed777"
}
```

Notes:

*  I tried testing WebDriver's Python bindings to no avail.  It may be best to wait for a post-merger release of Selenium.

* Pylot test cases must be written in XML, which is not as expressive as Python.

* Can we use Selenium Grid with a Linux virtual machine to work around the OS X problem, for now?

* zope.testbrowser seems promising for light-weight functional testing.

* For load tests, I think The Grinder and (yes) FunkLoad are worth a closer look.  To get some data, I'll try to extend the simple FL test I ran recently to more complicated scenarios.  The Grinder may well be a better choice, although it's written in Java, since it seems to be mature, well-documented, and actively developed.  Moreover, we can write tests in Python, [more or less](http://grinder.sourceforge.net/g3/tutorial-perks.html).



---

archive/issue_comments_061354.json:
```json
{
    "body": "Good news, I think:  We can use FunkLoad to create a new worksheet, enter/evaluate a cell, and check for updates every 0.25 seconds.  We just need to send a [conditional] sequence of HTTP GET and POST requests.  Unless there are objections, I'll try to carry this further, along the lines of the Selenium test suite.   To the extent that FL is pure Python, its \"functional\" and load tests should run on multiple platforms.\n\nNote: I did need to make one change to FL's redirect handling code: \n\n```diff\n--- trunk/src/funkload/FunkLoadTestCase.py      2009-11-11 02:31:27.000000000 -0800\n+++ funkload/src/funkload/FunkLoadTestCase.py   2009-10-14 14:51:19.000000000 -0700\n@@ -277,6 +277,9 @@ class FunkLoadTestCase(unittest.TestCase\n             thread_sleep()              # give a chance to other threads\n             while response.code in (301, 302, 303, 307) and max_redirect_count:\n                 # Figure the location - which may be relative\n+                cookie = response.headers.get('Set-Cookie')\n+                if cookie:\n+                    self.setHeader('cookie', cookie)\n                 newurl = response.headers['Location']\n                 url = urljoin(url_in, newurl)\n                 # save the current url as the base for future redirects\n```\n",
    "created_at": "2009-11-11T11:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61354",
    "user": "https://github.com/qed777"
}
```

Good news, I think:  We can use FunkLoad to create a new worksheet, enter/evaluate a cell, and check for updates every 0.25 seconds.  We just need to send a [conditional] sequence of HTTP GET and POST requests.  Unless there are objections, I'll try to carry this further, along the lines of the Selenium test suite.   To the extent that FL is pure Python, its "functional" and load tests should run on multiple platforms.

Note: I did need to make one change to FL's redirect handling code: 

```diff
--- trunk/src/funkload/FunkLoadTestCase.py      2009-11-11 02:31:27.000000000 -0800
+++ funkload/src/funkload/FunkLoadTestCase.py   2009-10-14 14:51:19.000000000 -0700
@@ -277,6 +277,9 @@ class FunkLoadTestCase(unittest.TestCase
             thread_sleep()              # give a chance to other threads
             while response.code in (301, 302, 303, 307) and max_redirect_count:
                 # Figure the location - which may be relative
+                cookie = response.headers.get('Set-Cookie')
+                if cookie:
+                    self.setHeader('cookie', cookie)
                 newurl = response.headers['Location']
                 url = urljoin(url_in, newurl)
                 # save the current url as the base for future redirects
```




---

archive/issue_comments_061355.json:
```json
{
    "body": "By the way FL, uses [gnuplot](http://www.gnuplot.info/) to make graphs for bench reports.  I suppose we could use [matplotlib](http://matplotlib.sourceforge.net/) or Sage, instead, but I haven't examined the plotting code.",
    "created_at": "2009-11-11T11:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61355",
    "user": "https://github.com/qed777"
}
```

By the way FL, uses [gnuplot](http://www.gnuplot.info/) to make graphs for bench reports.  I suppose we could use [matplotlib](http://matplotlib.sourceforge.net/) or Sage, instead, but I haven't examined the plotting code.



---

archive/issue_comments_061356.json:
```json
{
    "body": "Replying to [comment:15 mpatel]:\n> Good news, I think:  We can use FunkLoad to create a new worksheet, enter/evaluate a cell, and check for updates every 0.25 seconds.  We just need to send a [conditional] sequence of HTTP GET and POST requests.  Unless there are objections, I'll try to carry this further, along the lines of the Selenium test suite.   To the extent that FL is pure Python, its \"functional\" and load tests should run on multiple platforms.\n> [snip]\n\nNoting that FunkLoad apparently requires patching before it is fully usable, what are the disadvantages to using `zope.testbrowser`, which seems to be better maintained and planned? I haven't tried it personally yet though, so I my impression may be wrong.",
    "created_at": "2009-11-11T11:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61356",
    "user": "https://github.com/TimDumol"
}
```

Replying to [comment:15 mpatel]:
> Good news, I think:  We can use FunkLoad to create a new worksheet, enter/evaluate a cell, and check for updates every 0.25 seconds.  We just need to send a [conditional] sequence of HTTP GET and POST requests.  Unless there are objections, I'll try to carry this further, along the lines of the Selenium test suite.   To the extent that FL is pure Python, its "functional" and load tests should run on multiple platforms.
> [snip]

Noting that FunkLoad apparently requires patching before it is fully usable, what are the disadvantages to using `zope.testbrowser`, which seems to be better maintained and planned? I haven't tried it personally yet though, so I my impression may be wrong.



---

archive/issue_comments_061357.json:
```json
{
    "body": "I also haven't used zope.testbrowser, but after reading through its documentation, I think it's better for \"functional\" testing than for load testing.  In particular, it [very likely] has better cookie and form-handling capabilities than FL (actually, [webunit](http://mechanicalcat.net/tech/webunit/)).  On the other hand, FL already has an infrastructure for concurrent testing and it can load/cache CSS/images/etc.\n\nOf course, neither is a replacement for Selenium's truly functional tests.  For \"functional\" tests alone, z.t may be a good choice.  For load tests, FL seems to be a good Pythonic choice that can also go \"functional.\"  However, if we don't mind using other languages, Watir/Celerity or The Grinder may be better.  How important are the load tests?  Perhaps we can build a load test framework on z.t?",
    "created_at": "2009-11-11T13:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61357",
    "user": "https://github.com/qed777"
}
```

I also haven't used zope.testbrowser, but after reading through its documentation, I think it's better for "functional" testing than for load testing.  In particular, it [very likely] has better cookie and form-handling capabilities than FL (actually, [webunit](http://mechanicalcat.net/tech/webunit/)).  On the other hand, FL already has an infrastructure for concurrent testing and it can load/cache CSS/images/etc.

Of course, neither is a replacement for Selenium's truly functional tests.  For "functional" tests alone, z.t may be a good choice.  For load tests, FL seems to be a good Pythonic choice that can also go "functional."  However, if we don't mind using other languages, Watir/Celerity or The Grinder may be better.  How important are the load tests?  Perhaps we can build a load test framework on z.t?



---

archive/issue_comments_061358.json:
```json
{
    "body": "I would think that load tests are quite important, since http://sagenb.org serves in excess of 10k users. I personally don't mind using other languages.",
    "created_at": "2009-11-11T16:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61358",
    "user": "https://github.com/TimDumol"
}
```

I would think that load tests are quite important, since http://sagenb.org serves in excess of 10k users. I personally don't mind using other languages.



---

archive/issue_comments_061359.json:
```json
{
    "body": "> By the way, this ticket depends on #7309, #7310, and #7332. \n\nThanks for pointing this out.  The sagenb-0.4.1 release I made that was going to to go into sage-4.2.1 contains #7343 but not #7309, #7310, and #7332.  I'll merge those.",
    "created_at": "2009-11-11T16:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61359",
    "user": "https://github.com/williamstein"
}
```

> By the way, this ticket depends on #7309, #7310, and #7332. 

Thanks for pointing this out.  The sagenb-0.4.1 release I made that was going to to go into sage-4.2.1 contains #7343 but not #7309, #7310, and #7332.  I'll merge those.



---

archive/issue_comments_061360.json:
```json
{
    "body": "\"If nothing else, it would be really good to have a test suite that we can include and that anybody can trivially use with no confusing (or in my case, impossible) setup and configuration issues.\"\n\nTo achieve this --- moreover, a fast, self-contained suite --- Python is a logical choice.  But setup/config may be significantly simpler with simulated browsers.  I suppose we need to cover three areas with up to three frameworks:\n\na. In-browser - Se, Wa.\nb. Sim-browser - FL, Se 2.0, Wa, Zt.\nc. Load - FL, Gr.",
    "created_at": "2009-11-11T17:15:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61360",
    "user": "https://github.com/qed777"
}
```

"If nothing else, it would be really good to have a test suite that we can include and that anybody can trivially use with no confusing (or in my case, impossible) setup and configuration issues."

To achieve this --- moreover, a fast, self-contained suite --- Python is a logical choice.  But setup/config may be significantly simpler with simulated browsers.  I suppose we need to cover three areas with up to three frameworks:

a. In-browser - Se, Wa.
b. Sim-browser - FL, Se 2.0, Wa, Zt.
c. Load - FL, Gr.



---

archive/issue_comments_061361.json:
```json
{
    "body": "Replying to [comment:20 was]:\n> > By the way, this ticket depends on #7309, #7310, and #7332. \n> \n> Thanks for pointing this out.  The sagenb-0.4.1 release I made that was going to to go into sage-4.2.1 contains #7343 but not #7309, #7310, and #7332.  I'll merge those.\n\nFor 4.2.1, it may also be worthwhile to include one or more of these bug fixes: #7316, #7318, #7339, #7354, #7385.",
    "created_at": "2009-11-11T17:21:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61361",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:20 was]:
> > By the way, this ticket depends on #7309, #7310, and #7332. 
> 
> Thanks for pointing this out.  The sagenb-0.4.1 release I made that was going to to go into sage-4.2.1 contains #7343 but not #7309, #7310, and #7332.  I'll merge those.

For 4.2.1, it may also be worthwhile to include one or more of these bug fixes: #7316, #7318, #7339, #7354, #7385.



---

archive/issue_events_017382.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-11-11T19:50:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "milestone": "sage-4.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7343#event-17382"
}
```



---

archive/issue_comments_061362.json:
```json
{
    "body": "I've merged this into sagenb-0.4.2 (sage-4.2.1)",
    "created_at": "2009-11-11T19:50:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61362",
    "user": "https://github.com/williamstein"
}
```

I've merged this into sagenb-0.4.2 (sage-4.2.1)



---

archive/issue_events_017383.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-11-11T19:50:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7343#event-17383"
}
```



---

archive/issue_comments_061363.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-11T19:50:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61363",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_061364.json:
```json
{
    "body": "A passing thought: We could reuse some functions in a \"functional\" Python test suite for a Sage Remote Access API (see, e.g., [Google Documents List Data API](http://code.google.com/apis/documents/overview.html)).  This would permit authenticated, programmatic access for manipulating worksheets.  This may be an independent reason to use Zt.",
    "created_at": "2009-11-12T22:50:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61364",
    "user": "https://github.com/qed777"
}
```

A passing thought: We could reuse some functions in a "functional" Python test suite for a Sage Remote Access API (see, e.g., [Google Documents List Data API](http://code.google.com/apis/documents/overview.html)).  This would permit authenticated, programmatic access for manipulating worksheets.  This may be an independent reason to use Zt.



---

archive/issue_comments_061365.json:
```json
{
    "body": "On organizing tests:\n\nSuppose we put all framework-dependent code (or as much as possible) in `sagenb.testing.notebook_test_case`, where we define `NotebookTestCaseSelenium`, `NotebookTestCaseZopeTestbrowser`, etc., as subclasses of `NotebookTestCaseAbstract`.  Then, we can write tests under `sagenb.testing.tests` with a [largely] framework-independent, higher-level API.  We can select a framework with which to run the tests in `sagenb.testing.run_tests`.\n\nOf course, we can add specialized methods for particular frameworks.  Moreover, over time, we can add or remove framework classes without discarding too many tests.\n\nThoughts?",
    "created_at": "2009-11-15T08:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7343",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7343#issuecomment-61365",
    "user": "https://github.com/qed777"
}
```

On organizing tests:

Suppose we put all framework-dependent code (or as much as possible) in `sagenb.testing.notebook_test_case`, where we define `NotebookTestCaseSelenium`, `NotebookTestCaseZopeTestbrowser`, etc., as subclasses of `NotebookTestCaseAbstract`.  Then, we can write tests under `sagenb.testing.tests` with a [largely] framework-independent, higher-level API.  We can select a framework with which to run the tests in `sagenb.testing.run_tests`.

Of course, we can add specialized methods for particular frameworks.  Moreover, over time, we can add or remove framework classes without discarding too many tests.

Thoughts?

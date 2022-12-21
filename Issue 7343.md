# Issue 7343: SageNB -- Add a Selenium test suite.

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-10-29 04:05:54

Assignee: boothby

CC:  was mpatel

Inclusion of a test suite will prevent regressions, and make development *much* easier.


---

Comment by timdumol created at 2009-10-29 04:06:39

New Selenium test suite.


---

Comment by timdumol created at 2009-10-29 04:08:58

Changing status from new to needs_review.


---

Attachment

Depends on #7309, #7310 and #7332. This is an initial version of the test suite. Many of these test cases were adapted and mildly modified from Mike Hansen's original Selenium test code.

More test cases to come, but I feel that having a test suite included asap is essential.


---

Comment by timdumol created at 2009-10-29 04:12:01

Running the test suite:

```
sage: from sagenb.testing.run_tests import run_tests; run_tests()
```


Note that this requires an instance of the Selenium server running on port 4444. The Selenium server can be downloaded from http://seleniumhq.org/download/ as part of the Selenium RC package and can be run with `java -jar selenium-server.jar`. This could not be included in the patch due to possible conflicts with the system binaries and libraries (Firefox, etc.).


---

Comment by timdumol created at 2009-10-29 04:18:54

A note: There is a failure in `test_searching_worksheets`. It is an actual bug -- the requisite javascript libraries are not loaded.


---

Comment by timdumol created at 2009-10-29 05:06:39

The previous patch had some errors (*~ files, missing file).


---

Attachment

Added a test to confirm that #7341 works.


---

Comment by timdumol created at 2009-10-30 13:39:39

Added "Edit worksheet" test. Made sure that no orphan processes are left behind by failed tests.


---

Attachment

So far, this looks great!  I'm still reading through the [Selenium-RC documentation](http://seleniumhq.org/docs/05_selenium_rc.html), but I think I can review this ticket formally tomorrow.  At the risk of asking too soon: Can we specify the particular browser to test in `run_tests()`?  Another potentially useful option, at least for Firefox: Use, e.g., `firefox -P selenium-test -remote "openURL($*, new-tab)"`, to open multiple tabs instead of windows.  I'll investigate.

Aside: It's nice that both [Selenium](http://seleniumhq.org/) and [FunkLoad](http://funkload.nuxeo.org/) are build on Python's [unittest framework](http://docs.python.org/library/unittest.html).  Of course, FunkLoad only simulates a browser, but I think we can attain approximate parity between the notebook's functional (i.e., with Selenium) and load (i.e., with FunkLoad) tests.  Selenium's advantage is that it tests real-world browsers, but even with [Selenium-Grid](http://selenium-grid.seleniumhq.org/), we'd have difficulty (I think) simulating thousands of simultaneous notebook users.


---

Comment by mpatel created at 2009-10-31 16:07:18

Possibly useful: [HTMLTestRunner.py](http://tungwaiyip.info/software/HTMLTestRunner.html)?


---

Comment by mpatel created at 2009-11-01 10:19:45

Tweaked a few tests.  See the comment.  Apply only this patch.


---

Attachment

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

Comment by mpatel created at 2009-11-01 10:45:58

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2009-11-04 16:30:05

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

Comment by mpatel created at 2009-11-04 20:59:56

Replying to [comment:5 mpatel]:
> Possibly useful: [HTMLTestRunner.py](http://tungwaiyip.info/software/HTMLTestRunner.html)?

See #7390.


---

Comment by was created at 2009-11-09 03:21:27

Unfortunately, I can't use any of this under OS X, because the sqlite libraries included in OS X and Firefox are incompatible: 

  * http://jira.openqa.org/browse/SRC-743

  * https://bugzilla.mozilla.org/show_bug.cgi?id=513747


After nearly two hours of trying to get this to work, I'm giving up for now.  I guess Selenium is just broken on OS X for now.   Hopefully the Firefox and/or Selenium devs will fix this asap.    In the meantime, this is a vote from me to check out FunkLoad: "Of course, FunkLoad only simulates a browser, but I think we can attain approximate parity between the notebook's functional (i.e., with Selenium) and load (i.e., with FunkLoad) tests."   If nothing else, it would be really good to have a test suite that we can include and that anybody can trivially use with no confusing (or in my case, impossible) setup and configuration issues.


---

Comment by was created at 2009-11-09 18:48:30

Further comments about this:

  (1) I tried to use FunkLoad to test Sage (again in OS X) for a while, and got nowhere.  It seems to be a mess and not very polished.   Evidently it exists because some company wrote it and thought it might be useful to the community, so they released it.    I'm dubious about FunkLoad. 
 
  (2) No matter what, I think we need functional testing of the sage notebook that works on our build farms.  There's no way Selenium can do that.    I think we need something else to complement Selenium, possibly just something straightforward written in python using urllib, urllib2, etc.


---

Comment by mpatel created at 2009-11-10 02:56:11

Some browser drivers and/or simulators:

 * [FunkLoad](http://funkload.nuxeo.org/) simulates.
 * [Pylot](http://www.pylot.org/) simulates.
 * [Sahi](http://sahi.co.in/w/) drives.
 * [Selenium RC](http://seleniumhq.org/) drives but see WebDriver below.  [Selenium Grid](http://selenium-grid.seleniumhq.org/) drives Selenium RC.
 * [Watir](http://watir.com/) drives, but [Celerity](http://celerity.rubyforge.org/) simulates.
 * [WebDriver](http://code.google.com/p/webdriver/) is merging with [Selenium](http://code.google.com/p/selenium/).  See [this blog post](http://google-opensource.blogspot.com/2009/05/introducing-webdriver.html) and [the FAQ](http://code.google.com/p/selenium/wiki/FrequentlyAskedQuestions).  It drives and simulates.  Already?
 * [Windmill](http://www.getwindmill.com/) drives.
 * [zope.testbrowser](http://pypi.python.org/pypi/zope.testbrowser) simulates.

I apologize for any misclassifications.  Some of the simulators can simulate JS, to a degree.  I _think_ these are all based on [HtmlUnit](http://htmlunit.sourceforge.net/).

It would be great if we could write tests in just one actively developed and supported framework/API but be able to run both truly functional and simulated tests.  Selenium/WebDriver _may_ be(come) that framework.


---

Comment by mpatel created at 2009-11-10 03:19:36

By the way, this ticket depends on #7309, #7310, and #7332.


---

Comment by mpatel created at 2009-11-10 13:43:01

[The Grinder](http://grinder.sourceforge.net/), a Java load testing framework, has Jython bindings.  It might be worth a closer look.


---

Comment by mpatel created at 2009-11-11 08:08:04

Notes:

 *  I tried testing WebDriver's Python bindings to no avail.  It may be best to wait for a post-merger release of Selenium.

 * Pylot test cases must be written in XML, which is not as expressive as Python.

 * Can we use Selenium Grid with a Linux virtual machine to work around the OS X problem, for now?

 * zope.testbrowser seems promising for light-weight functional testing.

 * For load tests, I think The Grinder and (yes) FunkLoad are worth a closer look.  To get some data, I'll try to extend the simple FL test I ran recently to more complicated scenarios.  The Grinder may well be a better choice, although it's written in Java, since it seems to be mature, well-documented, and actively developed.  Moreover, we can write tests in Python, [more or less](http://grinder.sourceforge.net/g3/tutorial-perks.html).


---

Comment by mpatel created at 2009-11-11 11:07:37

Good news, I think:  We can use FunkLoad to create a new worksheet, enter/evaluate a cell, and check for updates every 0.25 seconds.  We just need to send a [conditional] sequence of HTTP GET and POST requests.  Unless there are objections, I'll try to carry this further, along the lines of the Selenium test suite.   To the extent that FL is pure Python, its "functional" and load tests should run on multiple platforms.

Note: I did need to make one change to FL's redirect handling code: 

```diff
--- trunk/src/funkload/FunkLoadTestCase.py      2009-11-11 02:31:27.000000000 -0800
+++ funkload/src/funkload/FunkLoadTestCase.py   2009-10-14 14:51:19.000000000 -0700
`@``@` -277,6 +277,9 `@``@` class FunkLoadTestCase(unittest.TestCase
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

Comment by mpatel created at 2009-11-11 11:15:18

By the way FL, uses [gnuplot](http://www.gnuplot.info/) to make graphs for bench reports.  I suppose we could use [matplotlib](http://matplotlib.sourceforge.net/) or Sage, instead, but I haven't examined the plotting code.


---

Comment by timdumol created at 2009-11-11 11:18:40

Replying to [comment:15 mpatel]:
> Good news, I think:  We can use FunkLoad to create a new worksheet, enter/evaluate a cell, and check for updates every 0.25 seconds.  We just need to send a [conditional] sequence of HTTP GET and POST requests.  Unless there are objections, I'll try to carry this further, along the lines of the Selenium test suite.   To the extent that FL is pure Python, its "functional" and load tests should run on multiple platforms.
> [snip]

Noting that FunkLoad apparently requires patching before it is fully usable, what are the disadvantages to using `zope.testbrowser`, which seems to be better maintained and planned? I haven't tried it personally yet though, so I my impression may be wrong.


---

Comment by mpatel created at 2009-11-11 13:29:08

I also haven't used zope.testbrowser, but after reading through its documentation, I think it's better for "functional" testing than for load testing.  In particular, it [very likely] has better cookie and form-handling capabilities than FL (actually, [webunit](http://mechanicalcat.net/tech/webunit/)).  On the other hand, FL already has an infrastructure for concurrent testing and it can load/cache CSS/images/etc.

Of course, neither is a replacement for Selenium's truly functional tests.  For "functional" tests alone, z.t may be a good choice.  For load tests, FL seems to be a good Pythonic choice that can also go "functional."  However, if we don't mind using other languages, Watir/Celerity or The Grinder may be better.  How important are the load tests?  Perhaps we can build a load test framework on z.t?


---

Comment by timdumol created at 2009-11-11 16:17:07

I would think that load tests are quite important, since http://sagenb.org serves in excess of 10k users. I personally don't mind using other languages.


---

Comment by was created at 2009-11-11 16:59:10

> By the way, this ticket depends on #7309, #7310, and #7332. 

Thanks for pointing this out.  The sagenb-0.4.1 release I made that was going to to go into sage-4.2.1 contains #7343 but not #7309, #7310, and #7332.  I'll merge those.


---

Comment by mpatel created at 2009-11-11 17:15:28

"If nothing else, it would be really good to have a test suite that we can include and that anybody can trivially use with no confusing (or in my case, impossible) setup and configuration issues."

To achieve this --- moreover, a fast, self-contained suite --- Python is a logical choice.  But setup/config may be significantly simpler with simulated browsers.  I suppose we need to cover three areas with up to three frameworks:

  a. In-browser - Se, Wa.
  b. Sim-browser - FL, Se 2.0, Wa, Zt.
  c. Load - FL, Gr.


---

Comment by mpatel created at 2009-11-11 17:21:46

Replying to [comment:20 was]:
> > By the way, this ticket depends on #7309, #7310, and #7332. 
> 
> Thanks for pointing this out.  The sagenb-0.4.1 release I made that was going to to go into sage-4.2.1 contains #7343 but not #7309, #7310, and #7332.  I'll merge those.

For 4.2.1, it may also be worthwhile to include one or more of these bug fixes: #7316, #7318, #7339, #7354, #7385.


---

Comment by was created at 2009-11-11 19:50:24

I've merged this into sagenb-0.4.2 (sage-4.2.1)


---

Comment by was created at 2009-11-11 19:50:24

Resolution: fixed


---

Comment by mpatel created at 2009-11-12 22:50:55

A passing thought: We could reuse some functions in a "functional" Python test suite for a Sage Remote Access API (see, e.g., [Google Documents List Data API](http://code.google.com/apis/documents/overview.html)).  This would permit authenticated, programmatic access for manipulating worksheets.  This may be an independent reason to use Zt.


---

Comment by mpatel created at 2009-11-15 08:42:49

On organizing tests:

Suppose we put all framework-dependent code (or as much as possible) in `sagenb.testing.notebook_test_case`, where we define `NotebookTestCaseSelenium`, `NotebookTestCaseZopeTestbrowser`, etc., as subclasses of `NotebookTestCaseAbstract`.  Then, we can write tests under `sagenb.testing.tests` with a [largely] framework-independent, higher-level API.  We can select a framework with which to run the tests in `sagenb.testing.run_tests`.

Of course, we can add specialized methods for particular frameworks.  Moreover, over time, we can add or remove framework classes without discarding too many tests.

Thoughts?

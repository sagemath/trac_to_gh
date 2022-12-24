# Issue 7786: Restructure templates to idiomatic Jinja

archive/issues_007786.json:
```json
{
    "body": "Assignee: was\n\nCC:  mpatel was\n\nBy idiomatic Jinja, I mean\n\n* Inheritance instead of inclusion\n\n* Arguments required are only the needed models to produce the required view [1]\n\nThis will make editing the templates easier, and will allow for a more consistent interface (by specifying base templates for each section).\n\n[1] [Model-View-Controller](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)\n\nIssue created by migration from https://trac.sagemath.org/ticket/7786\n\n",
    "created_at": "2009-12-29T09:19:36Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Restructure templates to idiomatic Jinja",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7786",
    "user": "timdumol"
}
```
Assignee: was

CC:  mpatel was

By idiomatic Jinja, I mean

* Inheritance instead of inclusion

* Arguments required are only the needed models to produce the required view [1]

This will make editing the templates easier, and will allow for a more consistent interface (by specifying base templates for each section).

[1] [Model-View-Controller](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)

Issue created by migration from https://trac.sagemath.org/ticket/7786





---

archive/issue_comments_067146.json:
```json
{
    "body": "Attachment [trac_7783-sage-scripts.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7783-sage-scripts.patch) by timdumol created at 2009-12-29 09:21:01\n\nPreliminary work. Worksheet pages not yet done.",
    "created_at": "2009-12-29T09:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67146",
    "user": "timdumol"
}
```

Attachment [trac_7783-sage-scripts.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7783-sage-scripts.patch) by timdumol created at 2009-12-29 09:21:01

Preliminary work. Worksheet pages not yet done.



---

archive/issue_comments_067147.json:
```json
{
    "body": "Attachment [trac_7786-template-jinja-idiomatic.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.patch) by timdumol created at 2010-01-02 06:50:07\n\nConverts template structure to an inheritance based tree. Apply this patch alone to sagenb repo.",
    "created_at": "2010-01-02T06:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67147",
    "user": "timdumol"
}
```

Attachment [trac_7786-template-jinja-idiomatic.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.patch) by timdumol created at 2010-01-02 06:50:07

Converts template structure to an inheritance based tree. Apply this patch alone to sagenb repo.



---

archive/issue_comments_067148.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-02T07:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67148",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067149.json:
```json
{
    "body": "This is a big patch that makes the template structure more consistent by using inheritance. It also removes a lot of non-semantic markup (<br />, <hr />, etc.). Please note that there are some visual changes (font stack, bar below banner at login.html, headers instead of bold tags at login.html, etc.). I hope they're not too major. Kindly note any changes that are too big and may require consultation at the mailing list.",
    "created_at": "2010-01-02T07:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67149",
    "user": "timdumol"
}
```

This is a big patch that makes the template structure more consistent by using inheritance. It also removes a lot of non-semantic markup (<br />, <hr />, etc.). Please note that there are some visual changes (font stack, bar below banner at login.html, headers instead of bold tags at login.html, etc.). I hope they're not too major. Kindly note any changes that are too big and may require consultation at the mailing list.



---

archive/issue_comments_067150.json:
```json
{
    "body": "Note: Depends on #7269, #7650, and dependencies.",
    "created_at": "2010-01-02T08:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67150",
    "user": "timdumol"
}
```

Note: Depends on #7269, #7650, and dependencies.



---

archive/issue_comments_067151.json:
```json
{
    "body": "I can only look at the patch right now, but I think these are much-needed and appreciated changes to SageNB.  I think we should make merging this ticket (plus its dependencies) a priority.  I'll try to start reviewing the patch soon.\n\nAs the merge nears, I'll rebase #7666 and its descendants, as necessary.",
    "created_at": "2010-01-02T09:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67151",
    "user": "mpatel"
}
```

I can only look at the patch right now, but I think these are much-needed and appreciated changes to SageNB.  I think we should make merging this ticket (plus its dependencies) a priority.  I'll try to start reviewing the patch soon.

As the merge nears, I'll rebase #7666 and its descendants, as necessary.



---

archive/issue_comments_067152.json:
```json
{
    "body": "Attachment [trac_7786-template-jinja-idiomatic.2.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.2.patch) by timdumol created at 2010-01-02 17:20:16\n\nRebased on #7650 and its dependencies. Apply this patch alone to sagenb repo.",
    "created_at": "2010-01-02T17:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67152",
    "user": "timdumol"
}
```

Attachment [trac_7786-template-jinja-idiomatic.2.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.2.patch) by timdumol created at 2010-01-02 17:20:16

Rebased on #7650 and its dependencies. Apply this patch alone to sagenb repo.



---

archive/issue_comments_067153.json:
```json
{
    "body": "Rebased on #7650 and its dependencies. Apply this patch alone to sagenb repo.",
    "created_at": "2010-01-02T19:08:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67153",
    "user": "timdumol"
}
```

Rebased on #7650 and its dependencies. Apply this patch alone to sagenb repo.



---

archive/issue_comments_067154.json:
```json
{
    "body": "Attachment [trac_7786-template-jinja-idiomatic.3.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.3.patch) by timdumol created at 2010-01-03 17:20:50\n\nUpdates `source_code.html` and adds styling for it. Also adds a warning to the .css files.",
    "created_at": "2010-01-03T17:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67154",
    "user": "timdumol"
}
```

Attachment [trac_7786-template-jinja-idiomatic.3.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.3.patch) by timdumol created at 2010-01-03 17:20:50

Updates `source_code.html` and adds styling for it. Also adds a warning to the .css files.



---

archive/issue_comments_067155.json:
```json
{
    "body": "Attachment [trac_7786-template-jinja-idiomatic.4.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.4.patch) by timdumol created at 2010-01-03 17:31:39\n\nAdds missing div_wrap argument to template call at `Cell.html()`",
    "created_at": "2010-01-03T17:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67155",
    "user": "timdumol"
}
```

Attachment [trac_7786-template-jinja-idiomatic.4.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.4.patch) by timdumol created at 2010-01-03 17:31:39

Adds missing div_wrap argument to template call at `Cell.html()`



---

archive/issue_comments_067156.json:
```json
{
    "body": "V4 applies cleanly to 4.3.1.alpha0 + #7650's latest.  With this configuration, I see\n\n* Se test errors:\n  * 4050: `Exception: Timed out after 30000ms`\n  * 7433: `Exception: ERROR: Element link=Sign out not found`\n  * 3960, 7433, 7428, 7444, searching_for_worksheets: `Exception: ERROR: Element link=Worksheet not found`\n\n* Doctests:\n  * Failures: `challenge.py`, `template.py`, `worksheet.py`.\n  * Memory-leak(?): `cell.py`.",
    "created_at": "2010-01-05T01:36:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67156",
    "user": "mpatel"
}
```

V4 applies cleanly to 4.3.1.alpha0 + #7650's latest.  With this configuration, I see

* Se test errors:
  * 4050: `Exception: Timed out after 30000ms`
  * 7433: `Exception: ERROR: Element link=Sign out not found`
  * 3960, 7433, 7428, 7444, searching_for_worksheets: `Exception: ERROR: Element link=Worksheet not found`

* Doctests:
  * Failures: `challenge.py`, `template.py`, `worksheet.py`.
  * Memory-leak(?): `cell.py`.



---

archive/issue_comments_067157.json:
```json
{
    "body": "* \"Home\" page contains \"Toggle\" link.\n  * Printed/published worksheets: Click bar is visible (on hover).  Clicking adds a cell, which appears to be editable.\n  * Upon opening a worksheet: all existing input cells appear to have the same size.\n  * Docbrowser worksheets:\n   * Extra clickbar at top.\n   * Shift-click is not disabled.",
    "created_at": "2010-01-05T03:33:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67157",
    "user": "mpatel"
}
```

* "Home" page contains "Toggle" link.
  * Printed/published worksheets: Click bar is visible (on hover).  Clicking adds a cell, which appears to be editable.
  * Upon opening a worksheet: all existing input cells appear to have the same size.
  * Docbrowser worksheets:
   * Extra clickbar at top.
   * Shift-click is not disabled.



---

archive/issue_comments_067158.json:
```json
{
    "body": "* Minor: Message at top of `main.sass` should also refer to the `readme.txt` (cf. `test_report.sass`.\n  * Just Se test 4050 fails with\n\n```\ntrac_7843-cell_listdir.patch\ntrac_7844-notebook_address.patch\ntrac_7847-empty_trash_ie_ff.patch\ntrac_7846-no_CODE_PY_symlinks.patch\ntrac_7650-sagenb_doctesting_v3.patch\ntrac_7786-template-jinja-idiomatic.4.patch\n```\n\n\n  !",
    "created_at": "2010-01-05T09:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67158",
    "user": "mpatel"
}
```

* Minor: Message at top of `main.sass` should also refer to the `readme.txt` (cf. `test_report.sass`.
  * Just Se test 4050 fails with

```
trac_7843-cell_listdir.patch
trac_7844-notebook_address.patch
trac_7847-empty_trash_ie_ff.patch
trac_7846-no_CODE_PY_symlinks.patch
trac_7650-sagenb_doctesting_v3.patch
trac_7786-template-jinja-idiomatic.4.patch
```


  !



---

archive/issue_comments_067159.json:
```json
{
    "body": "* Actually, 4050 gives the same *error* (i.e., not a failure) as above.\n  * `js.py` does not compress `main.js`.\n  * `'Error:'` --> `'Error: '` on the Sign in page.\n  * Ratings:\n   * Unrated worksheets are rated -1.0, it seems.\n   * A worksheet's ratings page shows \"rating[0]\" under User and \"rating[1]\" under \"Rating.\"\n   * Out of curiosity: Is there a maximum comment length?",
    "created_at": "2010-01-05T10:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67159",
    "user": "mpatel"
}
```

* Actually, 4050 gives the same *error* (i.e., not a failure) as above.
  * `js.py` does not compress `main.js`.
  * `'Error:'` --> `'Error: '` on the Sign in page.
  * Ratings:
   * Unrated worksheets are rated -1.0, it seems.
   * A worksheet's ratings page shows "rating[0]" under User and "rating[1]" under "Rating."
   * Out of curiosity: Is there a maximum comment length?



---

archive/issue_comments_067160.json:
```json
{
    "body": "Simple Jinja template dependency graph worksheet.  Not a patch.",
    "created_at": "2010-01-05T12:38:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67160",
    "user": "mpatel"
}
```

Simple Jinja template dependency graph worksheet.  Not a patch.



---

archive/issue_comments_067161.json:
```json
{
    "body": "Attachment [jinja_template_deps.html](tarball://root/attachments/some-uuid/ticket7786/jinja_template_deps.html) by mpatel created at 2010-01-05 12:47:16\n\nThe [attachment:jinja_template_deps.html attached worksheet] (just paste it into an \"Edit\" window) generates a template dependency graph in Sage.  I'm sure there are many improvements to make, but I hope it's a useful start.  By the way, the last non-empty cell requires [Graphviz's](http://www.graphviz.org/) `dot`.",
    "created_at": "2010-01-05T12:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67161",
    "user": "mpatel"
}
```

Attachment [jinja_template_deps.html](tarball://root/attachments/some-uuid/ticket7786/jinja_template_deps.html) by mpatel created at 2010-01-05 12:47:16

The [attachment:jinja_template_deps.html attached worksheet] (just paste it into an "Edit" window) generates a template dependency graph in Sage.  I'm sure there are many improvements to make, but I hope it's a useful start.  By the way, the last non-empty cell requires [Graphviz's](http://www.graphviz.org/) `dot`.



---

archive/issue_comments_067162.json:
```json
{
    "body": "* It seems there are two `account_recovery.html` pages.",
    "created_at": "2010-01-05T12:51:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67162",
    "user": "mpatel"
}
```

* It seems there are two `account_recovery.html` pages.



---

archive/issue_comments_067163.json:
```json
{
    "body": "Actually, [Graph.plot's](http://www.sagemath.org/doc/reference/sage/graphs/graph.html#sage.graphs.graph.GenericGraph.plot) `partition` option may be a better choice for coloring vertices.  Anyway, have fun!",
    "created_at": "2010-01-05T13:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67163",
    "user": "mpatel"
}
```

Actually, [Graph.plot's](http://www.sagemath.org/doc/reference/sage/graphs/graph.html#sage.graphs.graph.GenericGraph.plot) `partition` option may be a better choice for coloring vertices.  Anyway, have fun!



---

archive/issue_comments_067164.json:
```json
{
    "body": "Hi Tim -- Do you mind if I make a separate, commuting patch here of just changes under `sagenb/testing`?  If it's OK, I'd like to incorporate some changes I made at #7666, including running a test(s) by name (e.g., `rt.run_any(['4088', 'test_3711'], verbosity=1)`) and making it easier to test other browsers (e.g., first steps toward enabling Selenium Grid).  Actually getting the tests to pass in the other browsers --- I found this very tedious / time-consuming --- we can leave for another ticket.",
    "created_at": "2010-01-05T17:03:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67164",
    "user": "mpatel"
}
```

Hi Tim -- Do you mind if I make a separate, commuting patch here of just changes under `sagenb/testing`?  If it's OK, I'd like to incorporate some changes I made at #7666, including running a test(s) by name (e.g., `rt.run_any(['4088', 'test_3711'], verbosity=1)`) and making it easier to test other browsers (e.g., first steps toward enabling Selenium Grid).  Actually getting the tests to pass in the other browsers --- I found this very tedious / time-consuming --- we can leave for another ticket.



---

archive/issue_comments_067165.json:
```json
{
    "body": "Sure, no problem.",
    "created_at": "2010-01-05T18:04:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67165",
    "user": "timdumol"
}
```

Sure, no problem.



---

archive/issue_comments_067166.json:
```json
{
    "body": "By the way, the dependency graph is *awesome*. You may want to put it in the wiki somewhere, for Sage Notebook development tools.",
    "created_at": "2010-01-05T19:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67166",
    "user": "timdumol"
}
```

By the way, the dependency graph is *awesome*. You may want to put it in the wiki somewhere, for Sage Notebook development tools.



---

archive/issue_comments_067167.json:
```json
{
    "body": "Attachment [trac_7786-template-jinja-idiomatic.5.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.5.patch) by timdumol created at 2010-01-05 20:28:40\n\nFixes the issues pointed out (Se failures, etc.)",
    "created_at": "2010-01-05T20:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67167",
    "user": "timdumol"
}
```

Attachment [trac_7786-template-jinja-idiomatic.5.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.5.patch) by timdumol created at 2010-01-05 20:28:40

Fixes the issues pointed out (Se failures, etc.)



---

archive/issue_comments_067168.json:
```json
{
    "body": "The doctest failures are not yet fixed. I am having trouble with the Se tests: after a recent kernel upgrade, it seems that `shutil.rmdir()` fails silently, and `os.path.exists` reports the directory as gone, but is actually still there. I can only think of a kludgy fix of sleeping a while and looping until it can be deleted. Any ideas?",
    "created_at": "2010-01-05T20:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67168",
    "user": "timdumol"
}
```

The doctest failures are not yet fixed. I am having trouble with the Se tests: after a recent kernel upgrade, it seems that `shutil.rmdir()` fails silently, and `os.path.exists` reports the directory as gone, but is actually still there. I can only think of a kludgy fix of sleeping a while and looping until it can be deleted. Any ideas?



---

archive/issue_comments_067169.json:
```json
{
    "body": "Attachment [trac_7786-template-jinja-idiomatic.6.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.6.patch) by mpatel created at 2010-01-06 15:20:33\n\nNew test options.  Should fix Se + doc tests.  Replaces previous.",
    "created_at": "2010-01-06T15:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67169",
    "user": "mpatel"
}
```

Attachment [trac_7786-template-jinja-idiomatic.6.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.6.patch) by mpatel created at 2010-01-06 15:20:33

New test options.  Should fix Se + doc tests.  Replaces previous.



---

archive/issue_comments_067170.json:
```json
{
    "body": "V6 *might* help.  I've tested just FF 3.5.6 on Linux, so far.  Examples:\n\n```python\nimport sagenb.testing.run_tests as rt\n\n# Selenium.\nrt.setup_tests(environment='*firefox3 /usr/lib64/firefox-3.5.6/firefox')\nrt.run_any()\n\n# Selenium Grid.\nenvs = [\n    '*firefox',\n#    '*googlechrome',\n    '*iexplore',\n    '*opera',\n#    '*safari'\n    ]\n\nfor e in envs:\n    rt.setup_tests('192.168.50.99', False, e)\n    name = 'report_' + e.split()[0][1:] + '.html'\n    rt.run_any(make_report=True, report_filename=name)\n```\n\nFor other tickets:\n\n* Parallel testing.\n* Abstract away all `self.selenium` calls from `sagenb/tests/*`, i.e., put them all in a `notebook_test_case.SeleniumTestCase`.  Then we may be able to reuse `test_*` for pure `zope.testbrowser` tests --- \"just\" write a corresponding `notebook_test_case.ZTTestCase`.",
    "created_at": "2010-01-06T15:38:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67170",
    "user": "mpatel"
}
```

V6 *might* help.  I've tested just FF 3.5.6 on Linux, so far.  Examples:

```python
import sagenb.testing.run_tests as rt

# Selenium.
rt.setup_tests(environment='*firefox3 /usr/lib64/firefox-3.5.6/firefox')
rt.run_any()

# Selenium Grid.
envs = [
    '*firefox',
#    '*googlechrome',
    '*iexplore',
    '*opera',
#    '*safari'
    ]

for e in envs:
    rt.setup_tests('192.168.50.99', False, e)
    name = 'report_' + e.split()[0][1:] + '.html'
    rt.run_any(make_report=True, report_filename=name)
```

For other tickets:

* Parallel testing.
* Abstract away all `self.selenium` calls from `sagenb/tests/*`, i.e., put them all in a `notebook_test_case.SeleniumTestCase`.  Then we may be able to reuse `test_*` for pure `zope.testbrowser` tests --- "just" write a corresponding `notebook_test_case.ZTTestCase`.



---

archive/issue_comments_067171.json:
```json
{
    "body": "Of course, please feel free to make changes!\n\nOn the dependency graph:  Thanks!  Maybe we should include parts of the code (wrapped in a `try-except` block) in `template.py`?",
    "created_at": "2010-01-06T15:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67171",
    "user": "mpatel"
}
```

Of course, please feel free to make changes!

On the dependency graph:  Thanks!  Maybe we should include parts of the code (wrapped in a `try-except` block) in `template.py`?



---

archive/issue_comments_067172.json:
```json
{
    "body": "Attachment [trac_7786-template-jinja-idiomatic.7.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.7.patch) by mpatel created at 2010-01-06 15:59:40\n\nConditional `main.js` compression.  See `js.py`.  Replaces previous.",
    "created_at": "2010-01-06T15:59:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67172",
    "user": "mpatel"
}
```

Attachment [trac_7786-template-jinja-idiomatic.7.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.7.patch) by mpatel created at 2010-01-06 15:59:40

Conditional `main.js` compression.  See `js.py`.  Replaces previous.



---

archive/issue_comments_067173.json:
```json
{
    "body": "* It's not possible to delete compute cells from docbrowser worksheets, it seems.",
    "created_at": "2010-01-06T16:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67173",
    "user": "mpatel"
}
```

* It's not possible to delete compute cells from docbrowser worksheets, it seems.



---

archive/issue_comments_067174.json:
```json
{
    "body": "Reminder: Use self-closing `<input />` tags in HTML files.  WebKit browsers will complain about extra `</input>`s.",
    "created_at": "2010-01-06T16:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67174",
    "user": "mpatel"
}
```

Reminder: Use self-closing `<input />` tags in HTML files.  WebKit browsers will complain about extra `</input>`s.



---

archive/issue_comments_067175.json:
```json
{
    "body": "Can we delete `twist.Reset_css`?",
    "created_at": "2010-01-06T19:05:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67175",
    "user": "mpatel"
}
```

Can we delete `twist.Reset_css`?



---

archive/issue_comments_067176.json:
```json
{
    "body": "Replying to [comment:16 mpatel]:\n> Of course, please feel free to make changes!\n> \n> On the dependency graph:  Thanks!  Maybe we should include parts of the code (wrapped in a `try-except` block) in `template.py`?\n\nIt doesn't sound like it can be used by a non-developer, so I don't think it's worth including into the package. That's just my opinion though.",
    "created_at": "2010-01-06T19:15:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67176",
    "user": "timdumol"
}
```

Replying to [comment:16 mpatel]:
> Of course, please feel free to make changes!
> 
> On the dependency graph:  Thanks!  Maybe we should include parts of the code (wrapped in a `try-except` block) in `template.py`?

It doesn't sound like it can be used by a non-developer, so I don't think it's worth including into the package. That's just my opinion though.



---

archive/issue_comments_067177.json:
```json
{
    "body": "Should `NotebookSettingsPage.render` return a `HTMLResponse`, instead of a `Response`?",
    "created_at": "2010-01-06T19:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67177",
    "user": "mpatel"
}
```

Should `NotebookSettingsPage.render` return a `HTMLResponse`, instead of a `Response`?



---

archive/issue_comments_067178.json:
```json
{
    "body": "Replying to [comment:19 mpatel]:\n> Can we delete `twist.Reset_css`?\n\nYes, we can.\n\n> Should NotebookSettingsPage.render return a HTMLResponse, instead of a Response? \n\nYes.\n\nBut I think this patch has way too many changes in it as is. The clean up on `twist.py` should probably be spun off to another ticket.",
    "created_at": "2010-01-06T19:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67178",
    "user": "timdumol"
}
```

Replying to [comment:19 mpatel]:
> Can we delete `twist.Reset_css`?

Yes, we can.

> Should NotebookSettingsPage.render return a HTMLResponse, instead of a Response? 

Yes.

But I think this patch has way too many changes in it as is. The clean up on `twist.py` should probably be spun off to another ticket.



---

archive/issue_comments_067179.json:
```json
{
    "body": "Replying to [comment:22 timdumol]:\n> But I think this patch has way too many changes in it as is. The clean up on `twist.py` should probably be spun off to another ticket.\n\nSounds good.  I need to do this anyway for public / remote interacts.",
    "created_at": "2010-01-06T19:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67179",
    "user": "mpatel"
}
```

Replying to [comment:22 timdumol]:
> But I think this patch has way too many changes in it as is. The clean up on `twist.py` should probably be spun off to another ticket.

Sounds good.  I need to do this anyway for public / remote interacts.



---

archive/issue_comments_067180.json:
```json
{
    "body": "Attachment [trac_7786-template-jinja-idiomatic.8.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.8.patch) by mpatel created at 2010-01-07 01:08:26\n\nFurther small fixes.  Replaces previous.",
    "created_at": "2010-01-07T01:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67180",
    "user": "mpatel"
}
```

Attachment [trac_7786-template-jinja-idiomatic.8.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.8.patch) by mpatel created at 2010-01-07 01:08:26

Further small fixes.  Replaces previous.



---

archive/issue_comments_067181.json:
```json
{
    "body": "V8 should cover the problems above, except for deleting docbrowser cells, which is a known \"problem\" --- we don't save changes to these worksheets.  Anyway, to the extent it counts, my review is positive, except:\n\n* Is `_topbar.sass` missing?  When compiling, I see\n\n```\nSass::SyntaxError on line 29 of /.../sass/src/main.sass: File to import not found or unreadable: topbar.sass.\n```\n\n   If I comment out the ``@`import`, the generated `main.css` seems to be missing topbar directives.\n\nBy the way, I removed `template_error.html` and `base_popup.html`, since they don't appear to be used.  I also put `set div_wrap = true` in `cell.html` (when printing).  I apologize for going too far, in case I have.",
    "created_at": "2010-01-07T01:16:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67181",
    "user": "mpatel"
}
```

V8 should cover the problems above, except for deleting docbrowser cells, which is a known "problem" --- we don't save changes to these worksheets.  Anyway, to the extent it counts, my review is positive, except:

* Is `_topbar.sass` missing?  When compiling, I see

```
Sass::SyntaxError on line 29 of /.../sass/src/main.sass: File to import not found or unreadable: topbar.sass.
```

   If I comment out the ``@`import`, the generated `main.css` seems to be missing topbar directives.

By the way, I removed `template_error.html` and `base_popup.html`, since they don't appear to be used.  I also put `set div_wrap = true` in `cell.html` (when printing).  I apologize for going too far, in case I have.



---

archive/issue_comments_067182.json:
```json
{
    "body": "Adds missing file `_topbar.sass`",
    "created_at": "2010-01-07T17:30:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67182",
    "user": "timdumol"
}
```

Adds missing file `_topbar.sass`



---

archive/issue_comments_067183.json:
```json
{
    "body": "Attachment [trac_7786-template-jinja-idiomatic.9.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.9.patch) by timdumol created at 2010-01-07 17:30:43\n\nYes, it was missing. This patch fixes that problem.",
    "created_at": "2010-01-07T17:30:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67183",
    "user": "timdumol"
}
```

Attachment [trac_7786-template-jinja-idiomatic.9.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.9.patch) by timdumol created at 2010-01-07 17:30:43

Yes, it was missing. This patch fixes that problem.



---

archive/issue_comments_067184.json:
```json
{
    "body": "Positive review from me.  If you agree, please update the status.",
    "created_at": "2010-01-08T09:19:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67184",
    "user": "mpatel"
}
```

Positive review from me.  If you agree, please update the status.



---

archive/issue_comments_067185.json:
```json
{
    "body": "Actually, I just noticed some problems with `$(document).ready()`.  I'm working on V10.",
    "created_at": "2010-01-08T15:06:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67185",
    "user": "mpatel"
}
```

Actually, I just noticed some problems with `$(document).ready()`.  I'm working on V10.



---

archive/issue_comments_067186.json:
```json
{
    "body": "Attachment [trac_7786-template-jinja-idiomatic.10.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.10.patch) by mpatel created at 2010-01-08 16:32:28\n\nDOM ready / load event timing fixes.  Replaces previous.",
    "created_at": "2010-01-08T16:32:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67186",
    "user": "mpatel"
}
```

Attachment [trac_7786-template-jinja-idiomatic.10.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.10.patch) by mpatel created at 2010-01-08 16:32:28

DOM ready / load event timing fixes.  Replaces previous.



---

archive/issue_comments_067187.json:
```json
{
    "body": "In V10, I replaced `$(document).ready()` in a few places with either synchronous evaluation or `$(window).load()` (in particular, `$(document).load()` does not always work).  The main reason is timing --- the \"DOM ready\" event can fire too early for certain notebook initializations.  For example, evaluate\n\n```\nimport time\ntime.sleep(20)\nprint 'foo'\n```\n\nand reload the worksheet.  Published interacts are another, forthcoming example...\n\nI noticed that `Worksheet.html_cell_list` in V9\n\n* Referred to a non-existent template `published_worksheet.html`.\n* Is really no longer used.  The lone remaining call, in `twist.py` sends refreshed HTML that `notebook_lib.js` ignores.\n\nI've replaced the call with an empty string.  *However,* the main problem is that HTML for published worksheets is now no longer cached by the server.  Or am I mistaken?\n\nI'll try to fix this in V11...",
    "created_at": "2010-01-08T16:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67187",
    "user": "mpatel"
}
```

In V10, I replaced `$(document).ready()` in a few places with either synchronous evaluation or `$(window).load()` (in particular, `$(document).load()` does not always work).  The main reason is timing --- the "DOM ready" event can fire too early for certain notebook initializations.  For example, evaluate

```
import time
time.sleep(20)
print 'foo'
```

and reload the worksheet.  Published interacts are another, forthcoming example...

I noticed that `Worksheet.html_cell_list` in V9

* Referred to a non-existent template `published_worksheet.html`.
* Is really no longer used.  The lone remaining call, in `twist.py` sends refreshed HTML that `notebook_lib.js` ignores.

I've replaced the call with an empty string.  *However,* the main problem is that HTML for published worksheets is now no longer cached by the server.  Or am I mistaken?

I'll try to fix this in V11...



---

archive/issue_comments_067188.json:
```json
{
    "body": "Attachment [trac_7786-template-jinja-idiomatic.11.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.11.patch) by mpatel created at 2010-01-08 17:07:41\n\nCache HTML for published worksheets.  Replaces previous.",
    "created_at": "2010-01-08T17:07:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67188",
    "user": "mpatel"
}
```

Attachment [trac_7786-template-jinja-idiomatic.11.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.11.patch) by mpatel created at 2010-01-08 17:07:41

Cache HTML for published worksheets.  Replaces previous.



---

archive/issue_comments_067189.json:
```json
{
    "body": "V11 is attached.",
    "created_at": "2010-01-08T17:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67189",
    "user": "mpatel"
}
```

V11 is attached.



---

archive/issue_comments_067190.json:
```json
{
    "body": "If I save `$\\alpha$` in a text cell, then edit the cell again, I see `\u00cb` in the editor.  Moreover, the HTML source now contains `<span>` tags, etc.",
    "created_at": "2010-01-08T20:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67190",
    "user": "mpatel"
}
```

If I save `$\alpha$` in a text cell, then edit the cell again, I see `Ë` in the editor.  Moreover, the HTML source now contains `<span>` tags, etc.



---

archive/issue_comments_067191.json:
```json
{
    "body": "Fix text cell typesetting.  Replaces previous.",
    "created_at": "2010-01-08T22:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67191",
    "user": "mpatel"
}
```

Fix text cell typesetting.  Replaces previous.



---

archive/issue_comments_067192.json:
```json
{
    "body": "Attachment [trac_7786-template-jinja-idiomatic.12.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.12.patch) by mpatel created at 2010-01-08 22:11:45\n\nReplying to [comment:31 mpatel]:\n> If I save `$\\alpha$` in a text cell, then edit the cell again, I see `\u00cb` in the editor.  Moreover, the HTML source now contains `<span>` tags, etc.\nV12 should fix this.",
    "created_at": "2010-01-08T22:11:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67192",
    "user": "mpatel"
}
```

Attachment [trac_7786-template-jinja-idiomatic.12.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.12.patch) by mpatel created at 2010-01-08 22:11:45

Replying to [comment:31 mpatel]:
> If I save `$\alpha$` in a text cell, then edit the cell again, I see `Ë` in the editor.  Moreover, the HTML source now contains `<span>` tags, etc.
V12 should fix this.



---

archive/issue_comments_067193.json:
```json
{
    "body": "I just noticed that Sphinx fails to build the reference manual.  The \"problem\" may be in `template.py`:\n\n```\nSphinx error:\n'utf8' codec can't decode bytes in position 746-749: invalid data\n```\n",
    "created_at": "2010-01-09T00:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67193",
    "user": "mpatel"
}
```

I just noticed that Sphinx fails to build the reference manual.  The "problem" may be in `template.py`:

```
Sphinx error:
'utf8' codec can't decode bytes in position 746-749: invalid data
```




---

archive/issue_comments_067194.json:
```json
{
    "body": "Fix HTML reference manual build.  Replaces previous.",
    "created_at": "2010-01-09T02:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67194",
    "user": "mpatel"
}
```

Fix HTML reference manual build.  Replaces previous.



---

archive/issue_comments_067195.json:
```json
{
    "body": "Attachment [trac_7786-template-jinja-idiomatic.13.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.13.patch) by mpatel created at 2010-01-09 02:55:25\n\nReplying to [comment:33 mpatel]:\n> I just noticed that Sphinx fails to build the reference manual.  The \"problem\" may be in `template.py`:\nV13 should fix this.",
    "created_at": "2010-01-09T02:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67195",
    "user": "mpatel"
}
```

Attachment [trac_7786-template-jinja-idiomatic.13.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.13.patch) by mpatel created at 2010-01-09 02:55:25

Replying to [comment:33 mpatel]:
> I just noticed that Sphinx fails to build the reference manual.  The "problem" may be in `template.py`:
V13 should fix this.



---

archive/issue_comments_067196.json:
```json
{
    "body": "It seems the worksheet/cell layout is less compact than before.  It's probably easier to fix this at #7666.",
    "created_at": "2010-01-09T14:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67196",
    "user": "mpatel"
}
```

It seems the worksheet/cell layout is less compact than before.  It's probably easier to fix this at #7666.



---

archive/issue_comments_067197.json:
```json
{
    "body": "Replying to [comment:35 mpatel]:\n> It seems the worksheet/cell layout is less compact than before.  It's probably easier to fix this at #7666.\nOr the same?  Anyway, possibilities for a completely different ticket:\n\n* Remove `&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;` from `td.cell_number` for cells with no output.\n* Put the green \"cell is running\" bar adjacent to the red \"cell is not evaluated\" line.  The latter is actually a border, but we could insert a fixed-width `div` element here.  We could make this a status-area for the whole cell (input + output), add a right-click menu (e.g., for select / insert / move / delete operations, etc.), an on-hover toolbar, etc.",
    "created_at": "2010-01-09T23:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67197",
    "user": "mpatel"
}
```

Replying to [comment:35 mpatel]:
> It seems the worksheet/cell layout is less compact than before.  It's probably easier to fix this at #7666.
Or the same?  Anyway, possibilities for a completely different ticket:

* Remove `&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;` from `td.cell_number` for cells with no output.
* Put the green "cell is running" bar adjacent to the red "cell is not evaluated" line.  The latter is actually a border, but we could insert a fixed-width `div` element here.  We could make this a status-area for the whole cell (input + output), add a right-click menu (e.g., for select / insert / move / delete operations, etc.), an on-hover toolbar, etc.



---

archive/issue_comments_067198.json:
```json
{
    "body": "Attachment [trac_7786-template-jinja-idiomatic.14.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.14.patch) by timdumol created at 2010-01-17 19:27:26\n\nRebased on #7650 reviewer patch.",
    "created_at": "2010-01-17T19:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67198",
    "user": "timdumol"
}
```

Attachment [trac_7786-template-jinja-idiomatic.14.patch](tarball://root/attachments/some-uuid/ticket7786/trac_7786-template-jinja-idiomatic.14.patch) by timdumol created at 2010-01-17 19:27:26

Rebased on #7650 reviewer patch.



---

archive/issue_comments_067199.json:
```json
{
    "body": "My patch series before up to this patch:\n\n\n```\ntrac_7650-sagenb_doctesting_v6.patch\ntrac_7650-reviewer.patch\ntrac_7648-missing_indent.patch\ntrac_7663-rstrip_prompt.patch\ntrac_7847-empty-trash-no-referer.patch\ntrac_7786-template-jinja-idiomatic.patch\n```\n",
    "created_at": "2010-01-17T19:28:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67199",
    "user": "timdumol"
}
```

My patch series before up to this patch:


```
trac_7650-sagenb_doctesting_v6.patch
trac_7650-reviewer.patch
trac_7648-missing_indent.patch
trac_7663-rstrip_prompt.patch
trac_7847-empty-trash-no-referer.patch
trac_7786-template-jinja-idiomatic.patch
```




---

archive/issue_comments_067200.json:
```json
{
    "body": "Tim -- Can you confirm the review (unless you want to get a third opinion)?  At this stage, I suggest we create new tickets to fix problems (if any) discovered later.",
    "created_at": "2010-01-18T05:10:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67200",
    "user": "mpatel"
}
```

Tim -- Can you confirm the review (unless you want to get a third opinion)?  At this stage, I suggest we create new tickets to fix problems (if any) discovered later.



---

archive/issue_comments_067201.json:
```json
{
    "body": "Alright, signing this off.",
    "created_at": "2010-01-18T06:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67201",
    "user": "timdumol"
}
```

Alright, signing this off.



---

archive/issue_comments_067202.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T06:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67202",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067203.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7786#issuecomment-67203",
    "user": "timdumol"
}
```

Resolution: fixed

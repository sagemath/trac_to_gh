# Issue 9015: typing `?` on the command line brings up IPython help

archive/issues_009015.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  vbraun\n\nI was looking over the shoulder of a new user as he started Sage for the first time and typed `?` on the command line. This shows the IPython help text which doesn't mention Sage at all.\n\nWe should change this to show the text displayed with `help()`.\n\nPrinting some more information when someone types `help` without the parenthesis would also be nice.\n\n\n```\nsage: help\n<function help at 0x1d6fc80>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9015\n\n",
    "created_at": "2010-05-22T11:39:16Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "typing `?` on the command line brings up IPython help",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9015",
    "user": "burcin"
}
```
Assignee: mvngu

CC:  vbraun

I was looking over the shoulder of a new user as he started Sage for the first time and typed `?` on the command line. This shows the IPython help text which doesn't mention Sage at all.

We should change this to show the text displayed with `help()`.

Printing some more information when someone types `help` without the parenthesis would also be nice.


```
sage: help
<function help at 0x1d6fc80>
```


Issue created by migration from https://trac.sagemath.org/ticket/9015





---

archive/issue_comments_083383.json:
```json
{
    "body": "This is still the case, though now\n\n```\nsage: help\n<function sage.misc.sagedoc.help>\n```\n\n\nVolker, you are currently the Ipython-in-Sage guru - is there an easy way to fix this?",
    "created_at": "2014-11-24T17:48:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9015#issuecomment-83383",
    "user": "kcrisman"
}
```

This is still the case, though now

```
sage: help
<function sage.misc.sagedoc.help>
```


Volker, you are currently the Ipython-in-Sage guru - is there an easy way to fix this?



---

archive/issue_comments_083384.json:
```json
{
    "body": "I was hoping that you could add `usage = 'Useful message here'` somewhere in `DEFAULT_SAGE_CONFIG` in sage/repl/interpreter.py`, but that doesn't seem to have any effect. I also tried\n\n```diff\ndiff --git a/src/sage/repl/interpreter.py b/src/sage/repl/interpreter.py\nindex dbbd683..e748b9e 100644\n--- a/src/sage/repl/interpreter.py\n+++ b/src/sage/repl/interpreter.py\n@@ -502,6 +502,7 @@ class SageCrashHandler(IPAppCrashHandler):\n \n class SageTerminalApp(TerminalIPythonApp):\n     name = u'Sage'\n+    usage='Useful message here'\n     crash_handler_class = SageCrashHandler\n     test_shell = False\n \n```\n\nI don't know what else to try right now.",
    "created_at": "2014-11-25T00:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9015#issuecomment-83384",
    "user": "jhpalmieri"
}
```

I was hoping that you could add `usage = 'Useful message here'` somewhere in `DEFAULT_SAGE_CONFIG` in sage/repl/interpreter.py`, but that doesn't seem to have any effect. I also tried

```diff
diff --git a/src/sage/repl/interpreter.py b/src/sage/repl/interpreter.py
index dbbd683..e748b9e 100644
--- a/src/sage/repl/interpreter.py
+++ b/src/sage/repl/interpreter.py
@@ -502,6 +502,7 @@ class SageCrashHandler(IPAppCrashHandler):
 
 class SageTerminalApp(TerminalIPythonApp):
     name = u'Sage'
+    usage='Useful message here'
     crash_handler_class = SageCrashHandler
     test_shell = False
 
```

I don't know what else to try right now.



---

archive/issue_comments_083385.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-11-25T12:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9015#issuecomment-83385",
    "user": "vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083386.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-11-25T12:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9015#issuecomment-83386",
    "user": "vbraun"
}
```

New commits:



---

archive/issue_comments_083387.json:
```json
{
    "body": "If you want to figure out what happens you can always run in under the debugger:\n\n```\nsage: ip = get_ipython()\nsage: %debug ip.run_cell('?')\n```\n",
    "created_at": "2014-11-25T12:11:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9015#issuecomment-83387",
    "user": "vbraun"
}
```

If you want to figure out what happens you can always run in under the debugger:

```
sage: ip = get_ipython()
sage: %debug ip.run_cell('?')
```




---

archive/issue_comments_083388.json:
```json
{
    "body": "I have two comments. First, I think we should document this way of debugging. I now see that `get_ipython()` is documented near the top of `interpreter.py`, which is great. Maybe add a line or two about debugging right there.\n\nSecond, do we want to have an easy way of accessing the IPython help? Maybe that information could just be added to the end of the current help string. \n\nI'll see if I can come up with something over the next few days.",
    "created_at": "2014-11-26T21:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9015#issuecomment-83388",
    "user": "jhpalmieri"
}
```

I have two comments. First, I think we should document this way of debugging. I now see that `get_ipython()` is documented near the top of `interpreter.py`, which is great. Maybe add a line or two about debugging right there.

Second, do we want to have an easy way of accessing the IPython help? Maybe that information could just be added to the end of the current help string. 

I'll see if I can come up with something over the next few days.



---

archive/issue_comments_083389.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-11-28T12:22:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9015#issuecomment-83389",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_083390.json:
```json
{
    "body": "IMHO it is confusing to have the IPython help crop up. If there is anything that is necessary to use Sage in there then we should add it to our docs.",
    "created_at": "2014-11-28T12:32:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9015#issuecomment-83390",
    "user": "vbraun"
}
```

IMHO it is confusing to have the IPython help crop up. If there is anything that is necessary to use Sage in there then we should add it to our docs.



---

archive/issue_comments_083391.json:
```json
{
    "body": "I think this is good. Regarding the comment in the ticket description,\n> Printing some more information when someone types help without the parenthesis would also be nice.\nI guess there are ways to do this (see http://stackoverflow.com/questions/10875442/possible-to-change-a-functions-repr-in-python), but I don't know if they're worth it. The banner when you start Sage already says\n\n```\nType \"help()\" for help.\n```\n\n\nPositive review from me. Karl-Dieter?",
    "created_at": "2014-12-01T20:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9015#issuecomment-83391",
    "user": "jhpalmieri"
}
```

I think this is good. Regarding the comment in the ticket description,
> Printing some more information when someone types help without the parenthesis would also be nice.
I guess there are ways to do this (see http://stackoverflow.com/questions/10875442/possible-to-change-a-functions-repr-in-python), but I don't know if they're worth it. The banner when you start Sage already says

```
Type "help()" for help.
```


Positive review from me. Karl-Dieter?



---

archive/issue_comments_083392.json:
```json
{
    "body": "I won't have time to look at this, the reason I got involved was just checking whether the ticket was still valid.  I'm sure you did due diligence :)",
    "created_at": "2014-12-02T13:44:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9015#issuecomment-83392",
    "user": "kcrisman"
}
```

I won't have time to look at this, the reason I got involved was just checking whether the ticket was still valid.  I'm sure you did due diligence :)



---

archive/issue_comments_083393.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-02T15:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9015#issuecomment-83393",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083394.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-12-03T21:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9015",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9015#issuecomment-83394",
    "user": "vbraun"
}
```

Resolution: fixed

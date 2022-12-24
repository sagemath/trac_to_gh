# Issue 7657: notebook -- traceback involving "_before_preparse" in sagenb.org log

archive/issues_007657.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @williamstein boothby @kcrisman @jhpalmieri\n\nThe sagenb.org log has this error in it a bunch:\n\n```\n2009-12-10 13:58:06-0800 [HTTPChannel,203984,127.0.0.1] Exception rendering:2009-12-10 13:58:06-0800 [HTTPChannel,203984,127.0.0.1] Unhandled Error\n        Traceback (most recent call last):\n          File \"/usr/local/sage/local/lib/python2.6/site-packages/Twisted-8.2.0-py2.6-linux-x86_64.egg/twisted/internet/defer.py\", line 630, in gotResult\n            _deferGenerator(g, deferred)\n          File \"/usr/local/sage/local/lib/python2.6/site-packages/Twisted-8.2.0-py2.6-linux-x86_64.egg/twisted/internet/defer.py\", line 607, in _deferGenerator\n            deferred.callback(result)\n          File \"/usr/local/sage/local/lib/python2.6/site-packages/Twisted-8.2.0-py2.6-linux-x86_64.egg/twisted/internet/defer.py\", line 243, in callback\n            self._startRunCallbacks(result)\n          File \"/usr/local/sage/local/lib/python2.6/site-packages/Twisted-8.2.0-py2.6-linux-x86_64.egg/twisted/internet/defer.py\", line 312, in _startRunCallbacks\n            self._runCallbacks()\n        --- <exception caught here> ---\n          File \"/usr/local/sage/local/lib/python2.6/site-packages/Twisted-8.2.0-py2.6-linux-x86_64.eg\ng/twisted/internet/defer.py\", line 328, in _runCallbacks\n            self.result = callback(self.result, *args, **kw)\n          File \"/usr/local/sage/local/lib/python2.6/site-packages/Twisted-8.2.0-py2.6-linux-x86_64.eg\ng/twisted/web2/resource.py\", line 230, in <lambda>            ).addCallback(lambda res: self.render(request))\n          File \"/usr/local/sage/local/lib/python2.6/site-packages/sagenb/notebook/twist.py\", line 113\n1, in render            worksheet.check_comp()\n          File \"/usr/local/sage/local/lib/python2.6/site-packages/sagenb/notebook/worksheet.py\", line\n 3133, in check_comp            out = self.postprocess_output(output_status.output, C)\n          File \"/usr/local/sage/local/lib/python2.6/site-packages/sagenb/notebook/worksheet.py\", line\n 3619, in postprocess_output            I = C._before_preparse.split('\\n')\n        exceptions.AttributeError: Cell instance has no attribute '_before_preparse'\n```\n\n\nFix this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7657\n\n",
    "created_at": "2009-12-11T05:04:23Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook -- traceback involving \"_before_preparse\" in sagenb.org log",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7657",
    "user": "@williamstein"
}
```
Assignee: @williamstein

CC:  @williamstein boothby @kcrisman @jhpalmieri

The sagenb.org log has this error in it a bunch:

```
2009-12-10 13:58:06-0800 [HTTPChannel,203984,127.0.0.1] Exception rendering:2009-12-10 13:58:06-0800 [HTTPChannel,203984,127.0.0.1] Unhandled Error
        Traceback (most recent call last):
          File "/usr/local/sage/local/lib/python2.6/site-packages/Twisted-8.2.0-py2.6-linux-x86_64.egg/twisted/internet/defer.py", line 630, in gotResult
            _deferGenerator(g, deferred)
          File "/usr/local/sage/local/lib/python2.6/site-packages/Twisted-8.2.0-py2.6-linux-x86_64.egg/twisted/internet/defer.py", line 607, in _deferGenerator
            deferred.callback(result)
          File "/usr/local/sage/local/lib/python2.6/site-packages/Twisted-8.2.0-py2.6-linux-x86_64.egg/twisted/internet/defer.py", line 243, in callback
            self._startRunCallbacks(result)
          File "/usr/local/sage/local/lib/python2.6/site-packages/Twisted-8.2.0-py2.6-linux-x86_64.egg/twisted/internet/defer.py", line 312, in _startRunCallbacks
            self._runCallbacks()
        --- <exception caught here> ---
          File "/usr/local/sage/local/lib/python2.6/site-packages/Twisted-8.2.0-py2.6-linux-x86_64.eg
g/twisted/internet/defer.py", line 328, in _runCallbacks
            self.result = callback(self.result, *args, **kw)
          File "/usr/local/sage/local/lib/python2.6/site-packages/Twisted-8.2.0-py2.6-linux-x86_64.eg
g/twisted/web2/resource.py", line 230, in <lambda>            ).addCallback(lambda res: self.render(request))
          File "/usr/local/sage/local/lib/python2.6/site-packages/sagenb/notebook/twist.py", line 113
1, in render            worksheet.check_comp()
          File "/usr/local/sage/local/lib/python2.6/site-packages/sagenb/notebook/worksheet.py", line
 3133, in check_comp            out = self.postprocess_output(output_status.output, C)
          File "/usr/local/sage/local/lib/python2.6/site-packages/sagenb/notebook/worksheet.py", line
 3619, in postprocess_output            I = C._before_preparse.split('\n')
        exceptions.AttributeError: Cell instance has no attribute '_before_preparse'
```


Fix this.

Issue created by migration from https://trac.sagemath.org/ticket/7657





---

archive/issue_comments_065500.json:
```json
{
    "body": "Has this happened recently? Othrewise this can be closed.",
    "created_at": "2010-01-19T09:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7657#issuecomment-65500",
    "user": "@TimDumol"
}
```

Has this happened recently? Othrewise this can be closed.



---

archive/issue_comments_065501.json:
```json
{
    "body": "The problem is that in `check_comp` we have\n\n```\nC = self.__queue[0]\n<a few things>\ntry:\n    output_status = S.output_status()\nexcept RuntimeError, msg:\n    verbose(\"Computation was interrupted or failed. Restarting.\\n%s\" % msg) \n    self.__comp_is_running = False\n    self.start_next_comp()\n    return 'w', C\nout = self.postprocess_output(output_status.output, C)\n```\n\nwhich is where the exception is raised, but this `_before_preparse` is only defined in `start_next_comp`, which *also* does\n\n```\nC = self.__queue[0]\n<a lot of stuff getting the input>\nself.sage().execute(input, os.path.abspath(self.data_directory()))\n```\n\nSo if a worksheet cell is updated in `sagenb/flask_version/worksheet.py` and \n\n```\n@worksheet_command('cell_update')\ndef worksheet_cell_update(worksheet):\n    <stuff>\n    worksheet.check_comp()\n    <lots more>\n     # Compute 'em, if we got 'em.\n    worksheet.start_next_comp()\n```\n\nor if somehow in the code above the computation is interrupted but the same cell is enqueued, this kind of race condition could occur.  I'd recommend either enqueuing a lot of cells at once, or interrupting and restarting a lot of cells, to replicate this - which could be hard.",
    "created_at": "2014-12-10T20:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7657#issuecomment-65501",
    "user": "@kcrisman"
}
```

The problem is that in `check_comp` we have

```
C = self.__queue[0]
<a few things>
try:
    output_status = S.output_status()
except RuntimeError, msg:
    verbose("Computation was interrupted or failed. Restarting.\n%s" % msg) 
    self.__comp_is_running = False
    self.start_next_comp()
    return 'w', C
out = self.postprocess_output(output_status.output, C)
```

which is where the exception is raised, but this `_before_preparse` is only defined in `start_next_comp`, which *also* does

```
C = self.__queue[0]
<a lot of stuff getting the input>
self.sage().execute(input, os.path.abspath(self.data_directory()))
```

So if a worksheet cell is updated in `sagenb/flask_version/worksheet.py` and 

```
@worksheet_command('cell_update')
def worksheet_cell_update(worksheet):
    <stuff>
    worksheet.check_comp()
    <lots more>
     # Compute 'em, if we got 'em.
    worksheet.start_next_comp()
```

or if somehow in the code above the computation is interrupted but the same cell is enqueued, this kind of race condition could occur.  I'd recommend either enqueuing a lot of cells at once, or interrupting and restarting a lot of cells, to replicate this - which could be hard.



---

archive/issue_comments_065502.json:
```json
{
    "body": "ancient ticket about deprecated sagenb, can we close ?\n\nThere are still many such tickets, seen by clicking on the \"notebook\" component link.",
    "created_at": "2020-03-29T08:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7657#issuecomment-65502",
    "user": "@fchapoton"
}
```

ancient ticket about deprecated sagenb, can we close ?

There are still many such tickets, seen by clicking on the "notebook" component link.



---

archive/issue_comments_065503.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-03-29T08:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7657#issuecomment-65503",
    "user": "@fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065504.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-03-29T15:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7657#issuecomment-65504",
    "user": "@videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065505.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2020-03-29T15:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7657#issuecomment-65505",
    "user": "@videlec"
}
```

Resolution: wontfix

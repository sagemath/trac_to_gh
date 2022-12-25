# Issue 6575: notebook bug in do_sage_extension_preparsing

archive/issues_006575.json:
```json
{
    "body": "Assignee: boothby\n\nI got this traceback with sage-4.1:\n\n```\n2009-07-20 15:22:18-0700 [HTTPChannel,3400,127.0.0.1] Unhandled Error\n\tTraceback (most recent call last):\n\t  File \"/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 630, in gotResult\n\t    _deferGenerator(g, deferred)\n\t  File \"/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 607, in _deferGenerator\n\t    deferred.callback(result)\n\t  File \"/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 243, in callback\n\t    self._startRunCallbacks(result)\n\t  File \"/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 312, in _startRunCallbacks\n\t    self._runCallbacks()\n\t--- <exception caught here> ---\n\t  File \"/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n\t    self.result = callback(self.result, *args, **kw)\n\t  File \"/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 230, in <lambda>\n\t    ).addCallback(lambda res: self.render(request))\n\t  File \"/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/sage/server/notebook/twist.py\", line 1152, in render\n\t    worksheet.start_next_comp()\n\t  File \"/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py\", line 2922, in start_next_comp\n\t    input += self.preparse_input(I, C)\n\t  File \"/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py\", line 3406, in preparse_input\n\t    input = self.preparse_nonswitched_input(input)\n\t  File \"/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py\", line 3440, in preparse_nonswitched_input\n\t    input = self.do_sage_extensions_preparsing(input)\n\t  File \"/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py\", line 3693, in do_sage_extensions_preparsing\n\t    filename = self.hunt_file(filename)\n\texceptions.UnboundLocalError: local variable 'filename' referenced before assignment\n\t\n```\n\n\nInspection of the relevant source code should make this trivial to fix.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6575\n\n",
    "created_at": "2009-07-21T00:47:07Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook bug in do_sage_extension_preparsing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6575",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

I got this traceback with sage-4.1:

```
2009-07-20 15:22:18-0700 [HTTPChannel,3400,127.0.0.1] Unhandled Error
	Traceback (most recent call last):
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 630, in gotResult
	    _deferGenerator(g, deferred)
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 607, in _deferGenerator
	    deferred.callback(result)
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 243, in callback
	    self._startRunCallbacks(result)
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 312, in _startRunCallbacks
	    self._runCallbacks()
	--- <exception caught here> ---
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
	    self.result = callback(self.result, *args, **kw)
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 230, in <lambda>
	    ).addCallback(lambda res: self.render(request))
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/sage/server/notebook/twist.py", line 1152, in render
	    worksheet.start_next_comp()
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py", line 2922, in start_next_comp
	    input += self.preparse_input(I, C)
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py", line 3406, in preparse_input
	    input = self.preparse_nonswitched_input(input)
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py", line 3440, in preparse_nonswitched_input
	    input = self.do_sage_extensions_preparsing(input)
	  File "/Users/wstein/build/64bit/sage-4.1/local/lib/python2.6/site-packages/sage/server/notebook/worksheet.py", line 3693, in do_sage_extensions_preparsing
	    filename = self.hunt_file(filename)
	exceptions.UnboundLocalError: local variable 'filename' referenced before assignment
	
```


Inspection of the relevant source code should make this trivial to fix.

Issue created by migration from https://trac.sagemath.org/ticket/6575





---

archive/issue_events_006812.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-01-25T15:48:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6575",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6575#event-6812"
}
```



---

archive/issue_comments_053585.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-01-25T15:48:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6575#issuecomment-53585",
    "user": "https://github.com/qed777"
}
```

Resolution: invalid



---

archive/issue_comments_053586.json:
```json
{
    "body": "I'm closing this, since we've removed `Worksheet.do_sage_extensions_preparsing` and no longer use `Worksheet.hunt_file` (cf. #7483).  We can open a separate ticket to trim obsolete code from `worksheet.py`.",
    "created_at": "2010-01-25T15:48:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6575#issuecomment-53586",
    "user": "https://github.com/qed777"
}
```

I'm closing this, since we've removed `Worksheet.do_sage_extensions_preparsing` and no longer use `Worksheet.hunt_file` (cf. #7483).  We can open a separate ticket to trim obsolete code from `worksheet.py`.

# Issue 236: attaching spyx files from the notebook doesn't work

archive/issues_000236.json:
```json
{
    "body": "Assignee: was\n\nattaching a spyx file from the notebook doesn't work and throws an exception:\n\n```\nException happened during processing of request from ('127.0.0.1', 47956)\nTraceback (most recent call last):\n  File \"SAGE/local/lib/python/SocketServer.py\", line 222, in handle_request\n    self.process_request(request, client_address)\n  File \"SAGE/local/lib/python/SocketServer.py\", line 241, in process_request\n    self.finish_request(request, client_address)\n  File \"SAGE/local/lib/python/SocketServer.py\", line 254, in finish_request\n    self.RequestHandlerClass(request, client_address, self)\n  File \"SAGE/local/lib/python/SocketServer.py\", line 521, in __init__\n    self.handle()\n  File \"SAGE/local/lib/python/BaseHTTPServer.py\", line 316, in handle\n    self.handle_one_request()\n  File \"SAGE/local/lib/python/BaseHTTPServer.py\", line 310, in handle_one_request\n    method()\n  File \"SAGE/local/lib/python2.5/site-packages/sage/server/notebook/server.py\", line 928, in do_POST\n    eval(\"self.%s()\"%method)\n  File \"<string>\", line 1, in <module>\n  File \"SAGE/local/lib/python2.5/site-packages/sage/server/notebook/server.py\", line 346, in cell_update\n    worksheet.check_comp()\n  File \"SAGE/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py\", line 614, in check_comp\n    self.start_next_comp()\n  File \"SAGE/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py\", line 530, in start_next_comp\n    input += self.preparse_input(I, C)\n  File \"SAGE/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py\", line 1115, in preparse_input\n    input = self.do_sage_extensions_preparsing(input)\n  File \"SAGE/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py\", line 983, in do_sage_extensions_preparsing\n    z += self._load_file(filename, files_seen_so_far, this_file) + '\\n'\n  File \"SAGE/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py\", line 957, in _load_file\n    t = self.do_sage_extensions_preparsing(t,\nUnboundLocalError: local variable 't' referenced before assignment\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/236\n\n",
    "created_at": "2007-01-31T05:31:04Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "attaching spyx files from the notebook doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/236",
    "user": "malb"
}
```
Assignee: was

attaching a spyx file from the notebook doesn't work and throws an exception:

```
Exception happened during processing of request from ('127.0.0.1', 47956)
Traceback (most recent call last):
  File "SAGE/local/lib/python/SocketServer.py", line 222, in handle_request
    self.process_request(request, client_address)
  File "SAGE/local/lib/python/SocketServer.py", line 241, in process_request
    self.finish_request(request, client_address)
  File "SAGE/local/lib/python/SocketServer.py", line 254, in finish_request
    self.RequestHandlerClass(request, client_address, self)
  File "SAGE/local/lib/python/SocketServer.py", line 521, in __init__
    self.handle()
  File "SAGE/local/lib/python/BaseHTTPServer.py", line 316, in handle
    self.handle_one_request()
  File "SAGE/local/lib/python/BaseHTTPServer.py", line 310, in handle_one_request
    method()
  File "SAGE/local/lib/python2.5/site-packages/sage/server/notebook/server.py", line 928, in do_POST
    eval("self.%s()"%method)
  File "<string>", line 1, in <module>
  File "SAGE/local/lib/python2.5/site-packages/sage/server/notebook/server.py", line 346, in cell_update
    worksheet.check_comp()
  File "SAGE/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 614, in check_comp
    self.start_next_comp()
  File "SAGE/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 530, in start_next_comp
    input += self.preparse_input(I, C)
  File "SAGE/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 1115, in preparse_input
    input = self.do_sage_extensions_preparsing(input)
  File "SAGE/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 983, in do_sage_extensions_preparsing
    z += self._load_file(filename, files_seen_so_far, this_file) + '\n'
  File "SAGE/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 957, in _load_file
    t = self.do_sage_extensions_preparsing(t,
UnboundLocalError: local variable 't' referenced before assignment
```


Issue created by migration from https://trac.sagemath.org/ticket/236





---

archive/issue_comments_001040.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-08-18T09:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/236#issuecomment-1040",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_001041.json:
```json
{
    "body": "Changing component from algebraic geometry to notebook.",
    "created_at": "2007-08-18T09:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/236#issuecomment-1041",
    "user": "was"
}
```

Changing component from algebraic geometry to notebook.



---

archive/issue_comments_001042.json:
```json
{
    "body": "Changing assignee from was to boothby.",
    "created_at": "2007-08-18T09:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/236#issuecomment-1042",
    "user": "was"
}
```

Changing assignee from was to boothby.



---

archive/issue_comments_001043.json:
```json
{
    "body": "Since it's no longer an exception it's now a feature request.",
    "created_at": "2007-08-18T09:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/236#issuecomment-1043",
    "user": "was"
}
```

Since it's no longer an exception it's now a feature request.



---

archive/issue_comments_001044.json:
```json
{
    "body": "I can reproduce the problem, but the error message has changed:\n\n```\nload \"hello.spyx\"\nError loading /tmp/Work2/sage-2.8.1/sage-2.8.1/hello.spyx -- file not\nfound\n```\n\n\nThe spyx file can actually be found in $SAGE_ROOT/data/extcode/sage/hello.spyx\n\nThis bug also seems to be duplicate of #230.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-21T12:04:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/236#issuecomment-1044",
    "user": "mabshoff"
}
```

I can reproduce the problem, but the error message has changed:

```
load "hello.spyx"
Error loading /tmp/Work2/sage-2.8.1/sage-2.8.1/hello.spyx -- file not
found
```


The spyx file can actually be found in $SAGE_ROOT/data/extcode/sage/hello.spyx

This bug also seems to be duplicate of #230.

Cheers,

Michael



---

archive/issue_comments_001045.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2007-09-07T00:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/236#issuecomment-1045",
    "user": "was"
}
```

Resolution: invalid

# Issue 236: attaching spyx files from the notebook doesn't work

Issue created by migration from https://trac.sagemath.org/ticket/236

Original creator: malb

Original creation time: 2007-01-31 05:31:04

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



---

Comment by was created at 2007-08-18 09:50:01

Changing type from defect to enhancement.


---

Comment by was created at 2007-08-18 09:50:01

Changing component from algebraic geometry to notebook.


---

Comment by was created at 2007-08-18 09:50:01

Changing assignee from was to boothby.


---

Comment by was created at 2007-08-18 09:50:01

Since it's no longer an exception it's now a feature request.


---

Comment by mabshoff created at 2007-08-21 12:04:57

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

Comment by was created at 2007-09-07 00:22:47

Resolution: invalid

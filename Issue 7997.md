# Issue 7997: Use ast to replace display hook hack

Issue created by migration from https://trac.sagemath.org/ticket/7997

Original creator: acleone

Original creation time: 2010-01-19 15:09:00

Assignee: was

CC:  timdumol acleone mpatel was boothby jason chapoton

See http://docs.python.org/library/ast.html#ast.NodeTransformer

Replace any Expr node in the ast tree with a function call to

```
def __print_if_not_none(expr):
    if expr is not None:
        print expr
```

An Expr node is anything like

```
123
do_foo()
for i in range(10):
    i
```

Which will be replaced by

```
__print_if_not_none(123)
__print_if_not_none(do_foo())
for i in range(10):
    __print_if_not_none(i)
```

Which will output

```
123
0
1
...
9
```



---

Comment by timdumol created at 2010-01-19 16:08:03

Incomplete implementation


---

Attachment

Hey, are you working on the pexpect stuff yet? If not, I'll start work on it as soon as you reply.


---

Comment by acleone created at 2010-01-21 02:28:22

Ok, you should probably work on this.  I think this patch should just change the way `%sage`/`%python` is executed:
 1. Preparse to valid python
 1. Save to a file.
   * Not base64 encoded, etc, just straight the straight unicode text after Preparsing
   * (So the file matches the cell exactly except for preparsing)
 1. Parse the source into an ast
   * syntax errors are caught here
 1. Unless `%no_print_exprs` or something, add in `print_if_not_none` calls with the `ast.NodeTransformer` for any `Expr` nodes that aren't in function def's.
 1. exec the ast tree, with globals set to a dictionary built from all previously evaluated cells and sage globals


---

Comment by timdumol created at 2010-02-01 10:06:48

Hey, I think I'm gonna be pretty busy till I graduate this March, so if anyone wants to work on this patch, I'm posting an updated incomplete patch now. The new interface based on multiprocessing seems to work quite well, with a 300ms speed boost (really makes things seem lightning fast on local calculation of cheap stuff), but I haven't quite found out exactly how to get file saving to work properly. It would be great if anyone could do so.

Please note that this patch does not work well with the pexpect implementation (changing location of preparsing, etc. means that it probably won't work at all), and so even after fixing the pipes implementation, either the remote pexpect implementation should be fixed, or a new remote implementation should be made (I'm thinking a quick Twisted [or even `asyncore`] server/client should do the job, with a similar interface as the pipes interface between server & client).


---

Comment by timdumol created at 2010-02-01 10:06:48

Changing status from new to needs_work.


---

Comment by timdumol created at 2010-02-01 10:07:21

Incomplete implementation. See comments for elaboration.


---

Attachment

I'd like to work on this patch.  At this point we're doing a lot more than just replacing the display hook hack - what should the scope of this patch be?

(Tom, correct me if I'm wrong) The patch currently:
 1. Replaces the display hook hack with a much more robust implementation using python's [ast library](http://docs.python.org/library/ast.html).
 2. Adds a new process implementation that passes a data object across
    * The old implementation passed a string to get exec-ed.  The string was "write this base64 encoded string to a file and exec it".
    * The new implementation gets the data object, writes the preparsed string to a file (just so exec will have line numbers), and exec's the string.  This is faster because it's only one exec.


---

Comment by timdumol created at 2010-02-06 11:22:58

Actually I'm assuming it's faster due to the reduced I/O (less files) and post-processing (filtering things out with pexpect).

I'd say the scope should be getting a working local and remote WorksheetProcess implementation, changing the interface as judged as needed. The resulting implementation should have functionality that is at least equivalent, if not a superset of, the local and remote pexpect interfaces. There should be no noticeable change in output for clients, except for speed differences. Notably, the traceback output should remain properly.

By the way, it's Tim.


---

Comment by timdumol created at 2010-03-09 15:48:21

Hi, has there been any progress on this? I'd love to assist/continue any work done here.


---

Comment by acleone created at 2010-03-09 16:40:05

Unfortunately not - I overestimated the amount of time I had.


---

Attachment

Completely working (hopefully) implementation of a local WorksheetProcess. Need to implement a remote version too, before this patch is ready.


---

Comment by timdumol created at 2010-04-02 12:04:13

Hi,

I have managed to finish the local implementation of WorksheetProcess_PipesImplementation (WPPI), and I have found it to be roughly 251.3 ms faster than WorksheetProcess_ExpectImplementation (WPEI). The patch, however, makes WPEI and its remote equivalent useless, due to an API change on the WorksheetProcess interface. This means that to finish this patch, a remote implementation must be made, and that both be *very* thoroughly tested.

Here are the benchmark results, if anyone's interested:


```
sage: from sagenb.interfaces.pipes_interface import WorksheetProcess_PipesImpl as WPPI
sage: wp = WPPI()

# This is without the print_expressions, which is not equivalent to what WPEI does. Mean: 251.53 µs
sage: timeit("""wp.execute('print 1', preparse=False, print_expressions=False)\nwhile wp.is_computing(): pass""")
625 loops, best of 3: 488 µs per loop
sage: timeit("""wp.execute('print 1', preparse=False, print_expressions=False)\nwhile wp.is_computing(): pass""")
625 loops, best of 3: 451 µs per loop
sage: timeit("""wp.execute('print 1', preparse=False, print_expressions=False)\nwhile wp.is_computing(): pass""")
625 loops, best of 3: 424 µs per loop
sage: timeit("""wp.execute('print 1', preparse=False, print_expressions=False)\nwhile wp.is_computing(): pass""")
625 loops, best of 3: 481 µs per loop
sage: timeit("""wp.execute('print 1', preparse=False, print_expressions=False)\nwhile wp.is_computing(): pass""")
625 loops, best of 3: 479 µs per loop

sage: wp.execute('from sage.all_notebook import *; import sagenb', preparse=False, print_expressions=False)

# This, on the other hand, is. Mean: 680 µs
sage: timeit("""wp.execute('1', preparse=False)\nwhile wp.is_computing(): pass""")
625 loops, best of 3: 664 µs per loop
sage: timeit("""wp.execute('1', preparse=False)\nwhile wp.is_computing(): pass""")
625 loops, best of 3: 734 µs per loop
sage: timeit("""wp.execute('1', preparse=False)\nwhile wp.is_computing(): pass""")
5 loops, best of 3: 601 µs per loop
sage: timeit("""wp.execute('1', preparse=False)\nwhile wp.is_computing(): pass""")
625 loops, best of 3: 739 µs per loop
sage: timeit("""wp.execute('1', preparse=False)\nwhile wp.is_computing(): pass""")
625 loops, best of 3: 664 µs per loop

# Note, this has preparsing. This checks to see if the speedup scales. It does not.
sage: timeit("""wp.execute('[x for x in primes(1e4)]')\nwhile wp.is_computing(): pass""")
5 loops, best of 3: 21.5 ms per loop
sage: timeit("""wp.execute('[x for x in primes(1e4)]')\nwhile wp.is_computing(): pass""")
25 loops, best of 3: 19.6 ms per loop
sage: timeit("""wp.execute('[x for x in primes(1e4)]')\nwhile wp.is_computing(): pass""")
25 loops, best of 3: 19.5 ms per loop
sage: timeit("""wp.execute('[x for x in primes(1e4)]')\nwhile wp.is_computing(): pass""")
25 loops, best of 3: 17.7 ms per loop
sage: timeit("""wp.execute('[x for x in primes(1e4)]')\nwhile wp.is_computing(): pass""")
25 loops, best of 3: 19.7 ms per loop
```


By contrast, here is the benchmark for WPEI:


```
sage: from sagenb.interfaces.expect import WorksheetProcess_ExpectImplementation as WPEI
sage: wp = WPEI()

sage: timeit("""wp.execute('1')\nwhile wp.is_computing():\n    wp.output_status()""")
5 loops, best of 3: 252 ms per loop
sage: timeit("""wp.execute('1')\nwhile wp.is_computing():\n    wp.output_status()""")
5 loops, best of 3: 252 ms per loop
sage: timeit("""wp.execute('1')\nwhile wp.is_computing():\n    wp.output_status()""")
5 loops, best of 3: 252 ms per loop
sage: timeit("""wp.execute('1')\nwhile wp.is_computing():\n    wp.output_status()""")
5 loops, best of 3: 252 ms per loop
sage: timeit("""wp.execute('1')\nwhile wp.is_computing():\n    wp.output_status()""")
5 loops, best of 3: 252 ms per loop

# Transmission lag is much slower than computation time, which accounts for the lack of difference, I think.
sage: sage: timeit("""wp.execute('[x for x in primes(1e4)]')\nwhile wp.is_computing(): wp.output_status()""")
5 loops, best of 3: 252 ms per loop
sage: sage: timeit("""wp.execute('[x for x in primes(1e4)]')\nwhile wp.is_computing(): wp.output_status()""")
5 loops, best of 3: 252 ms per loop
sage: sage: timeit("""wp.execute('[x for x in primes(1e4)]')\nwhile wp.is_computing(): wp.output_status()""")
5 loops, best of 3: 252 ms per loop
sage: sage: timeit("""wp.execute('[x for x in primes(1e4)]')\nwhile wp.is_computing(): wp.output_status()""")
5 loops, best of 3: 252 ms per loop
sage: sage: timeit("""wp.execute('[x for x in primes(1e4)]')\nwhile wp.is_computing(): wp.output_status()""")
5 loops, best of 3: 252 ms per loop
```



---

Comment by acleone created at 2010-04-02 17:40:32

Wow - that's awesome - great work Tim!  I definitely need to read up on the `multiprocessing` module.  Using `multiprocessing.Pipe()` and `multiprocessing.Connection()` is definitely the way to go.  Also it should be fairly easy to create a remote implementation with `multiprocessing.connection.Client()`.

Just a note for others on how this works: The worker process that executes the code has a `multiprocessing.Connection()` back to the manager process.  That connection can `send(obj)` and `recv() -> obj`, where `obj` is a picklable object, in this case:
  * Manager to Worker: `ExecutionData(preparse, print_expressions, string, tempdir, temp_file.name, transaction_number)` objects
  * Worker to Manager: either `(transaction_number, data)` where `data` is a string from `sys.stdout` or `sys.stderr`, or `(transaction_number, 0)` where the `0` means that the computation is finished.


---

Comment by timdumol created at 2010-04-03 15:22:17

Completely working implementation of a remote WorksheetProcess. Deprecates pexepct-based WP's. See comments for more.


---

Attachment

Tom Boothby, I'm adding you to the CC since this also fixes the problem with the tracebacks you mentioned to me last January.

This version of the patch is hopefully the final version of the patch. It does the following:

* Uses ast to replace the displayhook_hack in `sagenb.misc.format`, this was achieved through the efforts of me and Alex Leone (thank you!).

 * The new version, now named `parse_display_expr`, can now print either the last expression, as before:


```
1
2
3
----
3
```


  or all root level expressions:


```
1
2
for x in range(3):
    x
3
-----
1
2
3
```


  or all expressions:


```
1
2
for x in range(2):
    x
3
-----
1
2
0
1
3
```


     This new functionality is customizable via the Notebook Settings page.

* Adds new WorksheetProcess implementations based on `multiprocessing`, and deprecates the pexpect based ones, since this also changes the WorksheetProcess API. The blocking reference implementation has been updated to the new API.

 * The local implementation (`WorksheetProcess_PipesImpl`) is on average 251.3 ms faster than the pexpect based one.

 * The remote implementation ('WorksheetProcess_RemoteSSHPipesImpl`) is on average 212 ms faster than the remote pexpect based one. For now, it has the same vulnerabilities as the old one, with one additional: the connection between the main server and the computing server is unencrypted, and thus may be snooped on. It is trivial to fix this, however I am not sure whether the speed (and extra computing load) tradeoffs are worth it.

* It now formats tracebacks as:


```
Traceback (most recent call last):
  Line 7, in <module>
    bar()
  Line 5, in bar
    foo()
  Line 2, in foo
    raise Exception("Hello")
Exception: Hello
```


instead of:


```
Traceback (most recent call last):    def baz():
  File "", line 1, in <module>
    
  File "/tmp/tmpfzcGzr/___code___.py", line 13, in <module>
    baz()
  File "", line 1, in <module>
    
  File "/tmp/tmpfzcGzr/___code___.py", line 10, in baz
    bar()
  File "/tmp/tmpfzcGzr/___code___.py", line 7, in bar
    foo()
  File "/tmp/tmpfzcGzr/___code___.py", line 4, in foo
    raise Exception("Hello")
Exception: Hello
```


which have their line numbers offset by +2, also.


---

Comment by timdumol created at 2010-04-03 15:44:17

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2010-04-09 12:22:25

Fixed bug with empty input to parse_display_expr.


---

Attachment


---

Attachment

Fixes a doctest.


---

Comment by timdumol created at 2010-04-18 07:42:58

Fixes a doctest.


---

Attachment

This patch fixes a doctest. Please ignore attachment:trac_7908-pub_interact_c11-rebase.patch.


---

Comment by timdumol created at 2010-04-21 20:31:17

Fixes a bug with %time.


---

Attachment

How's the refactoring going?


---

Comment by acleone created at 2010-05-20 08:26:12

Tim: Can you split this into 2 patches:
  1. The AST stuff and API changes.
  2. Adding the multiprocessing interface.

William mentioned that we should keep the pexpect interface working.


---

Attachment

Makes the pexpect implementation conform to the new API, and adds backend configuration.


---

Comment by timdumol created at 2010-05-23 13:08:20

This new patch lets the pexpect interface work again, and allows one to configure the backend to pexpect, pipes or reference (defaulting to pipes). Is this enough, or shall I split it?


---

Comment by jason created at 2010-09-28 21:07:12

ping about reviewing.  If the two of you wrote this together, what do you want from a third reviewer?  I don't have time to read and understand it all right now.  But I can install and test it.

I had a student complain the other day that Sage only did one thing at a time, so this patch would be appreciated!


---

Comment by jason created at 2010-09-28 21:49:07

I have a setup where I have apache forward port 80 to port 8000, and Sage runs the notebook on port 8000.  I also use the server_pool option.  I applied this patch to a slightly modified 4.5.2.  I logged in.  When I tried to open a new worksheet, I got the following error in the log (and I got an error page in the browser):


```
2010-09-28 16:42:52-0500 [HTTPChannel,0,127.0.0.1] User 'jason.grout' logged in.
2010-09-28 16:42:58-0500 [HTTPChannel,1,127.0.0.1] ERROR initializing compute process:
2010-09-28 16:42:58-0500 [HTTPChannel,1,127.0.0.1] 
2010-09-28 16:42:58-0500 [HTTPChannel,1,127.0.0.1] find_next_available_port() takes at least 2 arguments (1 given)
2010-09-28 16:42:58-0500 [HTTPChannel,1,127.0.0.1] Exception rendering:
2010-09-28 16:42:58-0500 [HTTPChannel,1,127.0.0.1] Unhandled Error
	Traceback (most recent call last):
	  File "/home/sageserver/sage/local/lib/python2.6/site-packages/Twisted-9.0.0-py2.6-linux-x86_64.egg/twisted/internet/defer.py", line 181, in addCallbacks
	    self._runCallbacks()
	  File "/home/sageserver/sage/local/lib/python2.6/site-packages/Twisted-9.0.0-py2.6-linux-x86_64.egg/twisted/internet/defer.py", line 323, in _runCallbacks
	    self.result = callback(self.result, *args, **kw)
	  File "/home/sageserver/sage/local/lib/python2.6/site-packages/Twisted-9.0.0-py2.6-linux-x86_64.egg/twisted/internet/defer.py", line 284, in _continue
	    self.unpause()
	  File "/home/sageserver/sage/local/lib/python2.6/site-packages/Twisted-9.0.0-py2.6-linux-x86_64.egg/twisted/internet/defer.py", line 280, in unpause
	    self._runCallbacks()
	--- <exception caught here> ---
	  File "/home/sageserver/sage/local/lib/python2.6/site-packages/Twisted-9.0.0-py2.6-linux-x86_64.egg/twisted/internet/defer.py", line 323, in _runCallbacks
	    self.result = callback(self.result, *args, **kw)
	  File "/home/sageserver/sage/local/lib/python2.6/site-packages/Twisted-9.0.0-py2.6-linux-x86_64.egg/twisted/web2/server.py", line 296, in <lambda>
	    d.addCallback(lambda res, req: res.renderHTTP(req), self)
	  File "/home/sageserver/sage/local/lib/python2.6/site-packages/Twisted-9.0.0-py2.6-linux-x86_64.egg/twisted/web2/resource.py", line 85, in renderHTTP
	    return method(request)
	  File "/home/sageserver/sage/local/lib/python2.6/site-packages/Twisted-9.0.0-py2.6-linux-x86_64.egg/twisted/web2/resource.py", line 202, in http_GET
	    return super(Resource, self).http_GET(request)
	  File "/home/sageserver/sage/local/lib/python2.6/site-packages/Twisted-9.0.0-py2.6-linux-x86_64.egg/twisted/web2/resource.py", line 128, in http_GET
	    return self.render(request)
	  File "/home/sageserver/sage-4.5.2-test/devel/sagenb-main/sagenb/notebook/twist.py", line 1534, in render
	    self.worksheet.sage()
	  File "/home/sageserver/sage-4.5.2-test/devel/sagenb-main/sagenb/notebook/worksheet.py", line 2836, in sage
	    self.initialize_sage()
	  File "/home/sageserver/sage-4.5.2-test/devel/sagenb-main/sagenb/notebook/worksheet.py", line 2806, in initialize_sage
	    raise RuntimeError(msg)
	exceptions.RuntimeError: find_next_available_port() takes at least 2 arguments (1 given)
```



---

Comment by jason created at 2010-09-28 21:49:07

Changing status from needs_review to needs_work.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2020-08-25 09:35:31

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-08-29 15:27:48

Resolution: invalid

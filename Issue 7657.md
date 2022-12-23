# Issue 7657: notebook -- traceback involving "_before_preparse" in sagenb.org log

Issue created by migration from https://trac.sagemath.org/ticket/7657

Original creator: was

Original creation time: 2009-12-11 05:04:23

Assignee: was

CC:  was boothby kcrisman jhpalmieri

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


---

Comment by timdumol created at 2010-01-19 09:06:08

Has this happened recently? Othrewise this can be closed.


---

Comment by kcrisman created at 2014-12-10 20:19:24

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

which is where the exception is raised, but this `_before_preparse` is only defined in `start_next_comp`, which _also_ does

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

Comment by chapoton created at 2020-03-29 08:15:52

ancient ticket about deprecated sagenb, can we close ?

There are still many such tickets, seen by clicking on the "notebook" component link.


---

Comment by chapoton created at 2020-03-29 08:15:52

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2020-03-29 15:52:41

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2020-03-29 15:52:51

Resolution: wontfix

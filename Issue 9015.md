# Issue 9015: typing `?` on the command line brings up IPython help

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-05-22 11:39:16

Assignee: mvngu

CC:  vbraun

I was looking over the shoulder of a new user as he started Sage for the first time and typed `?` on the command line. This shows the IPython help text which doesn't mention Sage at all.

We should change this to show the text displayed with `help()`.

Printing some more information when someone types `help` without the parenthesis would also be nice.


```
sage: help
<function help at 0x1d6fc80>
```



---

Comment by kcrisman created at 2014-11-24 17:48:59

This is still the case, though now

```
sage: help
<function sage.misc.sagedoc.help>
```


Volker, you are currently the Ipython-in-Sage guru - is there an easy way to fix this?


---

Comment by jhpalmieri created at 2014-11-25 00:24:36

I was hoping that you could add `usage = 'Useful message here'` somewhere in `DEFAULT_SAGE_CONFIG` in sage/repl/interpreter.py`, but that doesn't seem to have any effect. I also tried

```diff
diff --git a/src/sage/repl/interpreter.py b/src/sage/repl/interpreter.py
index dbbd683..e748b9e 100644
--- a/src/sage/repl/interpreter.py
+++ b/src/sage/repl/interpreter.py
`@``@` -502,6 +502,7 `@``@` class SageCrashHandler(IPAppCrashHandler):
 
 class SageTerminalApp(TerminalIPythonApp):
     name = u'Sage'
+    usage='Useful message here'
     crash_handler_class = SageCrashHandler
     test_shell = False
 
```

I don't know what else to try right now.


---

Comment by vbraun created at 2014-11-25 12:10:00

Changing status from new to needs_review.


---

Comment by vbraun created at 2014-11-25 12:10:00

New commits:


---

Comment by vbraun created at 2014-11-25 12:11:47

If you want to figure out what happens you can always run in under the debugger:

```
sage: ip = get_ipython()
sage: %debug ip.run_cell('?')
```



---

Comment by jhpalmieri created at 2014-11-26 21:51:21

I have two comments. First, I think we should document this way of debugging. I now see that `get_ipython()` is documented near the top of `interpreter.py`, which is great. Maybe add a line or two about debugging right there.

Second, do we want to have an easy way of accessing the IPython help? Maybe that information could just be added to the end of the current help string. 

I'll see if I can come up with something over the next few days.


---

Comment by git created at 2014-11-28 12:22:14

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vbraun created at 2014-11-28 12:32:52

IMHO it is confusing to have the IPython help crop up. If there is anything that is necessary to use Sage in there then we should add it to our docs.


---

Comment by jhpalmieri created at 2014-12-01 20:52:38

I think this is good. Regarding the comment in the ticket description,
> Printing some more information when someone types help without the parenthesis would also be nice.
I guess there are ways to do this (see http://stackoverflow.com/questions/10875442/possible-to-change-a-functions-repr-in-python), but I don't know if they're worth it. The banner when you start Sage already says

```
Type "help()" for help.
```


Positive review from me. Karl-Dieter?


---

Comment by kcrisman created at 2014-12-02 13:44:23

I won't have time to look at this, the reason I got involved was just checking whether the ticket was still valid.  I'm sure you did due diligence :)


---

Comment by jhpalmieri created at 2014-12-02 15:31:00

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-12-03 21:56:20

Resolution: fixed

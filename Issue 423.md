# Issue 423: command line help() --> modules fails for *some* people

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-08-10 20:55:49

Assignee: was

David Harvey says

```

I can confirm this:


sage: help()

Welcome to Python 2.5!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://www.python.org/doc/tut/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help> modules

Please wait a moment while I gather a list of all available modules...

---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)

/Users/wdj/sagefiles/sage-2.7/<ipython console> in <module>()

...

++++++++++++++++++++++++++++++++++++++++++
```


For other people (e.g., me) there's no problem.  Hmm. 


---

Comment by was created at 2007-08-18 23:54:25

fixed by patching python itself (for sage-2.8.2)


---

Comment by was created at 2007-08-18 23:54:25

Resolution: fixed

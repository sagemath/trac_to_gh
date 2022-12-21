# Issue 9170: cygwin: get_memory_usage isn't implemented, e.g., because there's no top

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-07 04:34:30

Assignee: tbd

CC:  jpflori


```

sage -t  "devel/sage/sage/misc/getusage.py"                 
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/misc/getusage.py", line 30:
    sage: print "ignore this";  top()              # random output
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[2]>", line 1, in <module>
        print "ignore this";  top()              # random output###line 30:
    sage: print "ignore this";  top()              # random output
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/misc/getusage.py", line 57, in top
        raise NotImplementedError("top not implemented on platform %s" % U)
    NotImplementedError: top not implemented on platform cygwin_nt-5.1
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/misc/getusage.py", line 92:
    sage: t = get_memory_usage()
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[2]>", line 1, in <module>
        t = get_memory_usage()###line 92:
    sage: t = get_memory_usage()
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/misc/getusage.py", line 128, in get_memory_usage
        raise NotImplementedError("memory usage not implemented on platform %s" % U)
    NotImplementedError: memory usage not implemented on platform cygwin_nt-5.1
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/misc/getusage.py", line 93:
    sage: get_memory_usage(t)          # amount of memory more than when we defined t.
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 1, in <module>
        get_memory_usage(t)          # amount of memory more than when we defined t.###line 93:
    sage: get_memory_usage(t)          # amount of memory more than when we defined t.
    NameError: name 't' is not defined
**********************************************************************
```



---

Comment by was created at 2010-06-07 04:54:33

Another test failure caused by this:

```

sage -t  "devel/sage/sage/rings/tests.py"                   
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/rings/tests.py", line 229:
    sage: sage.rings.tests.test_random_elements(trials=2, seed=0)
Expected:
```



---

Comment by drkirkby created at 2010-08-02 04:20:12

I assume this means that 


```
sage: top()
```


will not work either. I know on Solaris, I called `prstat` rather than `top` as that is a standard part of Solaris, and `top` is not. But I thought on Linux there were some sysem calls in Sage for computing memory usage on Linux. Could it be as simple as changing


```
if [ "x$UNAME" = xLinux ] ; then 
   // Use Linux code
elif [ "x$UNAME" = xSunOS ] ; then 
  // call prstat
```


to 


```
if [ "x$UNAME" = xLinux ] || [ "x$UNAME" = xCYGWIN ] ; then 
   // Use Linux code
elif [ "x$UNAME" = xSunOS ] ; then 
  // call prstat
```


Dave


---

Comment by gbe created at 2010-10-27 18:12:42

Changing status from new to needs_work.


---

Comment by gbe created at 2010-10-27 18:12:42

Replying to [comment:2 drkirkby]:
> I assume this means that 
> 
> {{{
> sage: top()
> }}}
> 
> will not work either.

I'm not at home so I can't test on my machine, but 


```
File "/home/wstein/sage-4.4.3/devel/sage/sage/misc/getusage.py", line 30:
    sage: print "ignore this";  top()              # random output
```


looks like the line that's causing the first error to be throwing. The offending line(s) should be


```
    if U == 'linux':
        cmd = 'top -b -n 1 -p %s' % pid
    elif U == 'darwin':
        cmd = 'top -l 1 |grep "^ *%s "' % pid
    elif U == 'sunos':
        cmd = '/usr/bin/prstat -n 100000 1 1  | grep "^ *%s "' % pid
    else:
        raise NotImplementedError("top not implemented on platform %s" % U)
```


I've double checked, and cygwin _does_ ship with a top, so I suspect all that needs to be done is add a few instances along the line of "or U == 'cygwin'" and these issue would be resolved.

I'll try to test this over the weekend and have a patch prepared.


---

Comment by drkirkby created at 2010-10-27 18:43:22

Irrespective of whether Cygwin comes with top or not, using it can't be the best way to get memory usage. top is not used on Linux exept as a last resort. There are system calls to get the memory usage, which is the most sensible way to do this. If those system calls work on Cygwin, then it would be

 * More accurate
 * Faster
 * Not require 'top' to be installed. 

`top` is not a standard Unix command. It's not defined by POSIX and will not be installed by default on Cygwin. It's better to avoid calling `top` if at all possible. 

Dave


---

Comment by gbe created at 2010-10-28 00:58:30

Very true. I should have thought about what the code was doing, not just how to fix the breakage. As for top not being POSIX, I wasn't aware of that. I had always assumed it was. Since it's not POSIX it seems fine to let top() calls fail on Windows if top() is not installed, leaving an appropriately worded explanation.

The only time top is called on linux is via a top() call. To get the memory usage under linux, the /proc/<pid>/status is inspected. While they don't seem to document how complete it is, cygwin does populate a /proc directory. I'll poke around to see if the cygwin /proc system has what is needed. As far as I can see this the closest Python has to a memory usage call without using external libraries.

Geoff


---

Comment by drkirkby created at 2011-03-07 09:26:16

Replying to [comment:5 gbe]:
> Very true. I should have thought about what the code was doing, not just how to fix the breakage. As for top not being POSIX, I wasn't aware of that. I had always assumed it was. Since it's not POSIX it seems fine to let top() calls fail on Windows if top() is not installed, leaving an appropriately worded explanation.
> 
> The only time top is called on linux is via a top() call. To get the memory usage under linux, the /proc/<pid>/status is inspected. While they don't seem to document how complete it is, cygwin does populate a /proc directory. I'll poke around to see if the cygwin /proc system has what is needed. As far as I can see this the closest Python has to a memory usage call without using external libraries.
> 
> Geoff

I don't know, but I thought the plan was to make an installer for Cygwin which installed the perquisites, which would include top. So it should not really fail. 

As much as I don't like the idea of using 'top', I think in the short term it is a OK. There are more significant issues causing problems on Cygwin. I would have thought this one of the lower priority ones, but that's just my opinion. 

Dave


---

Comment by kcrisman created at 2013-01-15 15:38:44

Unsurprisingly, this still doesn't work, though most stuff now does/can on Cygwin.


---

Comment by jpflori created at 2013-01-15 18:11:47

I guess we could prereq for the Cygwin procps package but is this really necessary?


---

Comment by kcrisman created at 2013-01-15 18:13:57

Well, `get_memory_usage` is pretty useful.  Otherwise the real question would be how to change these doctests so they pass on Cygwin, which isn't clear to me.


---

Comment by jpflori created at 2013-01-15 22:10:20

After fighting with Cygwin to get enough memory to run heegner.py test (did not manage yet... not sure that I changed anything but I can allocate 500000000 bytes, but not 512000000), I'm not really convinced that get_memory_usage is that useful on Cygwin as you won't really be able to allocate as much memory as you want (without fighting with Cygwin...).


---

Comment by jpflori created at 2013-01-15 22:13:25

Whatsoever, with Cygwin procps package which provides top, the doctests do not pass.
And this is expected as the top function implemented in getusage.py explicitely raises an Error on not explicitely listed systems, which include Cygwin.


---

Comment by jpflori created at 2013-01-15 22:19:00

So I still think the best solution is not to test this on Cygwin or to expect a different result...

Or if you insist we add procps as a prereq and modify the Sage's top function implem.

Alternatively, we could modify Sage's top so that it raises an Error iff the system top is not available.
Then only the top implementation would vary, depending on the availability of top, not the doctest which would expect random output on Cygwin (0.0 if top is installed, Error otherwise).
But we would still need to deal with doctests producing different output depending on the system (let's say mark it as random Cygwin so that it will (hackingly) deal with both situation (whether procps is installed or not), rather than making it depend on the fact that it is installed which looks impossible; and expect 0.0 on other systems).


---

Comment by kcrisman created at 2013-01-16 01:18:47

Given that #12828 just uses completely different commands (i.e., `ps`) to get this information, which should presumably be available (?) on Cygwin, can we just do that?  Note that we also do this on Solaris.  I.e. we just add another case, perhaps on top (no pun intended) of #12828.


---

Comment by jpflori created at 2013-01-16 10:50:43

Yes ps is included in the "cygwin" package itself so always available.


---

Comment by jpflori created at 2013-01-16 11:01:06

But that won't help, I guess we are stuck with top.


---

Comment by jpflori created at 2013-01-16 11:03:45

Or we could just directly look into /proc/meminfo, not sure why we don't do that on Linuces.


---

Comment by jpflori created at 2013-01-16 11:04:49

Or rather things in /proc/$PID/


---

Comment by jpflori created at 2013-01-16 11:05:30

Surely that is not portable across a large range of Linuces.


---

Comment by dimpase created at 2013-01-27 08:43:13

I do have top on my Cygwin install and its output is very much Linux-like. So I propose just to hack `misc/getusage.py` to let it work on cygwin, too.


---

Attachment

enabling it on Cygwin


---

Comment by dimpase created at 2013-01-27 09:12:34

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2013-01-27 09:18:07

please test the patch (on Cygwin you might need to install `top`). The patch works on my Cygwin install just fine.


---

Comment by jpflori created at 2013-02-08 12:43:15

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-02-09 12:13:09

Resolution: fixed

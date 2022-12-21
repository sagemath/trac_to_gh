# Issue 9631: Remerge #9501 after resolving NFS and/or doctest problems with @fork

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-07-29 05:12:06

Assignee: jason

CC:  leif jhpalmieri kcrisman malb mvngu simonking was

We merged #9501 in Sage 4.5.2.alpha1 but backed it out entirely in 4.5.2.rc0 (cf. #9616), because a Network File System (NFS) problem on the Sage cluster gives frequent doctest failures.

Please see #9501 and #9616 for discussion.


---

Comment by mpatel created at 2010-10-05 05:38:02

After the recent changes on the Sage cluster, I still see failures on sage.math with 4.6.alpha2 + #9501's v2 patch:

```python
sage-4.6.a2$ env DOT_SAGE="$HOME/.sage" ./sage -t -long devel/sage/sage/parallel/decorate.py
sage -t -long "devel/sage/sage/parallel/decorate.py"        


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------

**********************************************************************
File "/mnt/usb1/scratch/mpatel/apps/sage-4.6.a2/devel/sage/sage/parallel/decorate.py", line 300:
    sage: g()
Expected:
    '10'
Got:
    [Errno 16] Device or resource busy: '/home/mpatel/.sage/temp/sage.math.washington.edu/7514/dir_0/.nfs00000000015a0bad0006c177'
    '10'
**********************************************************************
File "/mnt/usb1/scratch/mpatel/apps/sage-4.6.a2/devel/sage/sage/parallel/decorate.py", line 311:
    sage: g()
Expected:
    'a'
Got:
    [Errno 16] Device or resource busy: '/home/mpatel/.sage/temp/sage.math.washington.edu/7514/dir_1/.nfs00000000015a0bad0006c178'
    'a'
**********************************************************************
File "/mnt/usb1/scratch/mpatel/apps/sage-4.6.a2/devel/sage/sage/parallel/decorate.py", line 300:
    sage: g()
Expected:
    '10'
Got:
    [Errno 16] Device or resource busy: '/home/mpatel/.sage/temp/sage.math.washington.edu/7514/dir_0/.nfs00000000015a0bad0006c177'
    '10'
**********************************************************************
File "/mnt/usb1/scratch/mpatel/apps/sage-4.6.a2/devel/sage/sage/parallel/decorate.py", line 311:
    sage: g()
Expected:
    'a'
Got:
    [Errno 16] Device or resource busy: '/home/mpatel/.sage/temp/sage.math.washington.edu/7514/dir_1/.nfs00000000015a0bad0006c178'
    'a'
```

I believe the `Unhandled SIGSEGV` is expected.


---

Comment by mpatel created at 2010-10-10 09:33:50

Ticket #10098 is about a similar `[Errno 16] Device or resource busy` error.


---

Comment by mpatel created at 2010-10-10 09:42:26

Replying to [comment:2 mpatel]:
> Ticket #10098 is about a similar `[Errno 16] Device or resource busy` error.

See #10098's [comment:ticket:10098:9 comment 9ff] for a proposed possible solution.


---

Attachment

Version of #9501's v2, rebased for 4.6.rc0.


---

Comment by mpatel created at 2010-10-22 08:04:08

I've attached a tweaked version of William's patch v2 from #9501.


---

Comment by mpatel created at 2010-10-22 08:04:08

Changing status from new to needs_review.


---

Attachment

Rediffed for sage-4.7.1.rc1


---

Comment by vbraun created at 2011-08-03 10:49:51

One more docfix


---

Comment by vbraun created at 2011-08-03 10:53:24

Changing status from needs_review to positive_review.


---

Attachment

I've updated the patch for Sage-4.7.1, there were some rejects due to changed docstrings. I didn't touch any actual functionality. 

The actual workings of the fork decorator look good. Positive review.


---

Comment by leif created at 2011-08-14 16:05:26

There are still a few typos in the docstrings.

Related (but _should<sup>TM</sup>_ apply independently, haven't tested this yet): #11658


---

Attachment

polished docstrings fixing some typos.


---

Comment by was created at 2011-08-15 02:50:56

Hi Leif,  I just attached trac_9631-fork_decorator.4.patch which polished the docstrings fixing some typos.  If there are any remaining typos, please point them out explicitly.


---

Comment by leif created at 2011-08-15 04:27:22

Replying to [comment:8 was]:
> Hi Leif,  I just attached trac_9631-fork_decorator.4.patch which polished the docstrings fixing some typos.  If there are any remaining typos, please point them out explicitly.


```diff
--- trac_9631-fork_decorator.4.patch.orig	2011-08-15 05:19:25.000000000 +0200
+++ trac_9631-fork_decorator.4.patch	2011-08-15 06:10:11.000000000 +0200
`@``@` -17,7 +17,7 `@``@`
 +++ b/sage/parallel/decorate.py
 `@``@` -15,19 +15,17 `@``@`
      r"""
-     Convert a to a pair (args, kwds) using some rules:
+     Convert ``a`` to a pair ``(args, kwds)`` using some rules:
  
 -        * if already of that form, leave that way.
 -        * if a is a tuple make (a,{})
`@``@` -44,7 +44,7 `@``@`
 `@``@` -53,9 +51,14 `@``@`
  class Parallel:
      r"""
-     Create parallel decorated function.
+     Create ``parallel``-decorated function.
 -
      """
      def __init__(self, p_iter = 'fork', ncpus=None, **kwds):
`@``@` -56,7 +56,7 `@``@`
 +        """
          # The default p_iter is currently the reference implementation.
          # This may change.
-         self.p_iter = None
+         self.p_iter = None # ??? = p_iter, which defaults to 'fork', not the sequ. ref. impl.
 `@``@` -81,19 +84,16 `@``@`
  
      def __call__(self, f):
`@``@` -67,8 +67,8 `@``@`
 -        in possibly random order. Here x is replaced by its
 +        Create a function that wraps ``f`` and that when called with a
 +        list of inputs returns an iterator over pairs ``(x, f(x))`` in
-+        possibly random order. Here ``x`` is replaced by its
-         normalized form (args, kwds) using normalize_inputs.
++        possibly random order.  Here ``x`` is replaced by its
+         normalized form ``(args, kwds)`` using ``normalize_inputs()``.
  
          INPUT:
 -
`@``@` -102,7 +102,7 `@``@`
 +         The parallel subprocesses will not have access to data
 +         created in pexpect interfaces.  This behavior with respect to
 +         pexpect interfaces is very important to keep in mind when
-+         setting up certain computations. It's the one big limitation
++         setting up certain computations.  It's the one big limitation
 +         of this decorator.
 +
      INPUT:
`@``@` -114,24 +114,24 `@``@`
 +            - ``fork``            -- (default) use a new forked process for each input
 +            - ``multiprocessing`` -- use multiprocessing library
 +            - ``reference``       -- use a fake serial reference implementation
-      - ``ncpus`` -- integer, number of cpus
-      - ``timeout`` -- number of seconds until task is killed (only supported by 'fork')
+      - ``ncpus`` -- integer, maximal number of subprocesses to use at the same time
+      - ``timeout`` -- number of seconds until a subprocess is killed (only supported by ``fork``; zero means not at all)
  
 +    .. warning::
 +
-+         If you use anything but 'fork' above, then a whole new
++         If you use anything but ``fork`` above, then a whole new
 +         subprocess is spawned, so none of your local state (variables,
 +         certain functions, etc.) is available.
 +
      EXAMPLES:
  
-     We create a simple decoration for a simple function. The number
+     We create a simple decoration for a simple function.  The number
 `@``@` -148,7 +166,6 `@``@`
          sage: `@`parallel(2)
          ... def f(n): return n*n
  
 -
-     We create a decorator that uses 3 processes, and times out
+     We create a decorator that uses three subprocesses, and times out
      individual processes after 10 seconds::
  
 `@``@` -174,3 +191,152 `@``@`
`@``@` -144,7 +144,7 `@``@`
 +
 +###################################################################
 +# The `@`fork decorator -- evaluate a function with no side effects
-+# in memory, so the only side effects are on disk.
++# in memory, so the only side effects (if any) are on disk.
 +#
 +# We have both a function and a class below, so that the decorator
 +# can be used with or without options:
`@``@` -158,13 +158,13 `@``@`
 +
 +class Fork:
 +    """
-+    A fork decorator class. 
++    A ``fork`` decorator class.
 +    """
 +    def __init__(self, timeout=0, verbose=False):
 +        """
 +        INPUT:
-+         - ``timeout`` -- (default: 0) kills subrocess after this many
-+           seconds, or if timeout=0, do not kill the subprocess.
++         - ``timeout`` -- (default: 0) kill each subprocess after it has run this many
++           seconds (wall time), or if ``timeout`` is zero, do not kill any subprocesses.
 +         - ``verbose`` -- (default: ``False``) whether to print
 +           anything about what the decorator does (e.g., killing
 +           subprocesses)
`@``@` -182,9 +182,11 `@``@`
 +    def __call__(self, f):
 +        """
 +        INPUT:
+
 +         - ``f`` -- a function
 +
 +        OUTPUT:
+
 +         - A decorated function.
 +
 +        EXAMPLES::
`@``@` -206,30 +208,30 `@``@`
 +    """
 +    Decorate a function so that when called it runs in a forked
 +    subprocess.  This means that it won't have any in-memory
-+    side-effects on the parent Sage process.  The pexpect interfaces
++    side effects on the parent Sage process.  The pexpect interfaces
 +    are all reset. 
 +    
 +    INPUT:
 +      - ``f`` -- a function
-+      - ``timeout`` -- (default: 0) if positive, kills subrocess after
-+        this many seconds
++      - ``timeout`` -- (default: 0) if positive, kill subprocess after
++        this many seconds (wall time)
 +      - ``verbose`` -- (default: ``False``) whether to print anything
-+        about what the decorator does (e.g., killing subprocesses)
++        about what the decorator does (e.g., killing the subprocess)
 +
 +    .. warning::
 +
-+        The forked subprocesses will not have access to data created
++        The forked subprocess will not have access to data created
 +        in pexpect interfaces.  This behavior with respect to pexpect
 +        interfaces is very important to keep in mind when setting up
-+        certain computations. It's the one big limitation of this
++        certain computations.  It's the one big limitation of this
 +        decorator.
 +
 +    EXAMPLES:
 +
-+    We create a function and run it with the fork decorator.  Note
++    We create a function and run it with the ``fork`` decorator.  Note
 +    that it does not have a side effect.  Despite trying to change
-+    the global variable "a" below in g, the variable a does not get
-+    changed.::
++    the global variable ``a`` below in ``g``, the variable ``a`` does not get
++    changed::
 +    
 +        sage: a = 5
 +        sage: `@`fork
`@``@` -242,7 +244,7 `@``@`
 +        sage: a
 +        5
 +
-+    We use fork to make sure that the function terminates after 1
++    We use ``fork`` to make sure that the function terminates after one
 +    second, no matter what::
 +    
 +        sage: `@`fork(timeout=1, verbose=True)
`@``@` -253,7 +255,7 `@``@`
 +        Killing subprocess ... with input ((10000000,), {'m': 5}) which took too long
 +        'NO DATA (timed out)'
 +
-+    We illustrate that pexpect interface state is not affected by
++    We illustrate that the state of the pexpect interface is not altered by
 +    forked functions (they get their own new pexpect interfaces!)::
 +    
 +        sage: gp.eval('a = 5')
`@``@` -305,14 +307,14 `@``@`
 -            - ``timeout`` -- (float) time in seconds until a subprocess is automatically killed
 -            - ``verbose`` -- whether to print anything about what the iterator does (e.g., killing subprocesses)
 +            - ``ncpus`` -- the maximal number of simultaneous
-+              processes to spawn
-+            - ``timeout`` -- (float, default: 0) time in seconds until
++              subprocesses to spawn
++            - ``timeout`` -- (float, default: 0) wall time in seconds until
 +              a subprocess is automatically killed
 +            - ``verbose`` -- (default: False) whether to print
 +              anything about what the iterator does (e.g., killing
 +              subprocesses)
 +            - ``reset_interfaces`` -- (default: True) whether to reset
-+              all expect interfaces
++              all pexpect interfaces
  
          EXAMPLES::
  
`@``@` -326,7 +328,7 `@``@`
          """
 `@``@` -206,7 +213,8 `@``@`
  
-             # The expect interfaces (and objects defined in them) are
+             # The pexpect interfaces (and objects defined in them) are
              # not valid.
 -            sage.interfaces.quit.invalidate_all()
 +            if self.reset_interfaces:
```


Explicit, but perhaps a bit inconvenient. Didn't apply it, only looked at the patch.


---

Comment by leif created at 2011-08-15 04:33:31

P.S.: The wording w.r.t. `ncpus` and `timeout` could be unified.


---

Comment by was created at 2011-08-15 04:52:08

Since you changed the code, you should post a patch, since it seems silly for me to just manually copy your changes in...


---

Comment by was created at 2011-08-15 04:53:42

I see -- you literally patched the patch?   I don't know how to get your patch of the patch off of trac.  I can view it, but can't download it...?


---

Comment by leif created at 2011-08-15 06:42:39

Replying to [comment:12 was]:
> I see -- you literally patched the patch?   I don't know how to get your patch of the patch off of trac.  I can view it, but can't download it...?

Yep, sorry. (I actually _edited_ your patch and then made a diff just for displaying.)

In principle one can extract inline patches from mail notifications (or "reply" to the comment just to copy parts), but since I also changed context lines, the patched patch wouldn't apply anyway.

I was just going to upload a v5 (no code changes btw., just in comments), but somehow managed to totally mess up the patch (and apparently also the files themselves) such that I now have two mixed versions with _both_ having some of your and some of my changes... 8/

Trying to fix this, then I'll upload a "real" v5 patch; I made more changes than in the comment above.


---

Comment by leif created at 2011-08-15 08:21:10

Diff between v4 (William's) and v5 (Leif's) patch. For reference / review only.


---

Attachment

Some more docstring fixes.


---

Attachment

Ok, attached a v5 patch, and a diff between William's v4 and my version.

Take a look at it, haven't updated the description yet.

Hope I didn't miss something, as I had to redo almost all from scratch, because some very weird things must have happened. Not only did the editor confuse files, presumably due to renaming and symbolic links, but also my first committed and exported version completely vanished from the Mercurial repository, which must be some weird bug related to cloning  and rebuilding a branch.


---

Comment by vbraun created at 2011-08-15 13:43:54

Looks good. If you can add a description then we'll be good to go.


---

Comment by vbraun created at 2011-08-15 13:43:54

Changing status from positive_review to needs_work.


---

Comment by leif created at 2011-08-15 16:02:07

Replying to [comment:15 vbraun]:
> Looks good. If you can add a description then we'll be good to go.

? I just meant I haven't updated _the ticket's_ description to refer to the new v5 patch.


---

Comment by leif created at 2011-08-15 16:02:33

Changing status from needs_work to needs_info.


---

Comment by vbraun created at 2011-08-15 16:15:35

Changing status from needs_info to needs_review.


---

Comment by vbraun created at 2011-08-15 16:15:35

Sorry, I didn't notice that the patch does already include some description; since it starts with a hash-mark its somewhat indistinguishable from the automatic mercurial comments. But should be good enough.


---

Comment by vbraun created at 2011-08-15 16:15:54

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-08-18 22:01:53

Resolution: fixed

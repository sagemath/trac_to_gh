# Issue 9224: Unify sage-test and sage-ptest

Issue created by migration from https://trac.sagemath.org/ticket/9224

Original creator: mpatel

Original creation time: 2010-06-12 09:55:23

Assignee: mvngu

CC:  cwitty ddrake drkirkby jhpalmieri leif wjp

We currently have separate single and multi-threaded Sage doctest scripts.  In particular, `sage -t ...` invokes `SAGE_ROOT/local/bin/sage-test` and `sage -tp ...` invokes `sage-ptest`.  These files share many lines of almost functionally identical identical code.  Unifying these scripts should make it easier to maintain and extend the Sage doctest system.

Related: #2379, #7993, #7995, #8641.


---

Comment by mpatel created at 2010-06-12 10:01:43

It seems the merger is overdue, although I doubt I can work on it in the immediate future, e.g., before #8641 closes.

What if we start with mapping `sage -t ...` to `sage -tp 1 ...`?


---

Comment by ddrake created at 2010-06-15 04:23:13

Replying to [comment:1 mpatel]:
> What if we start with mapping `sage -t ...` to `sage -tp 1 ...`?

This sounds great to me. It immediately removes the code duplication and is very easy to implement. Perhaps it's worth asking on sage-devel about this, in case anyone knows of a substantive difference between "-t" and "-tp 1", but I think this is a good idea.


---

Comment by ddrake created at 2010-06-15 08:23:14

I'm looking at this, and it might be a bit trickier than I thought. Doing "sage -tp 1 ..." tests to see if Sage starts, which we don't want. That's easy to fix, though. What might be harder is that sage-ptest has some awful code in it. The test_file function, according to comments, is supposed to return a 4-tuple, but sometimes it returns a 3-tuple (line 122); there's a bare "except", which is probably not a good idea; the function that processes the tuples just mentioned does this:

```
  F = result[0]
  ret = result[1]
  finished_time = result[2]
  ol = result[3]
```

The "result" usually is a 4-tuple: (filename, return_code, time, some_string). But sometimes it returns a 3-tuple: (-5, 0, some_string). So the code above sometimes gets a filename for F, and sometimes gets the integer -5. Then there's this:

```
  if ol!="" and (not ol.isspace()):
        if (ol[len(ol)-1]=="\n"):
            ol=ol[0:len(ol)-1]
        print ol
```

Why is that not

```
  if ol and not ol.isspace():
    print ol.rstrip()
```

? There is some strange stuff in sage-ptest.


---

Comment by ddrake created at 2010-06-15 09:35:39

See #9243 for a related ticket -- it feels weird to be or'ing return codes together when the basic return codes are not powers of 2.


---

Comment by mpatel created at 2010-07-07 03:36:56

I've opened #9225 for possible new [optional] doctesting features.  Feel free to make suggestions.


---

Attachment

`Doctester` class pseudo-interface.  Not a patch.


---

Comment by mpatel created at 2010-07-15 01:57:45

I've attached a first take on an interface for a Sage `Doctester` class.  Please see [comment:ticket:9225:4 this comment] at #9225 for possible uses.  I'm not sure whether to put this in the Sage library (under `misc/`) or in `SAGE_LOCAL/bin`.  But I think we'll need to add `sage-doctest` to the unification efforts.

Thoughts?


---

Comment by mpatel created at 2010-07-15 07:32:32

If the interface above (or a variation) is reasonable, we could populate `doctest.py` with most of the non-parsing-related, non-redundant parts of `sage-doctest` and `sage-(p)test`.  To ensure that we test `doctest.py` regularly, I suggest we put it in the sage repository, under `misc/`.  Then we'd put just the command-line parsing code in a `sage-test` in the scripts repository.  This script would `import sage.misc.doctest` and instantiate/call a `Doctester` object to run the tests.

More keyword arguments for `Doctester`'s constructor: `timeout`, `timeout_long`, `testdir`, and various Valgrind settings.


---

Comment by mpatel created at 2010-07-16 21:43:24

Just requesting feedback on re-{design,writ,refactor}-ing the doctesting system --- but only when it's convenient, as I can't work on this immediately.


---

Comment by cwitty created at 2010-07-20 20:59:49

I do like the idea of merging sage-test and sage-ptest.

Your Doctester API seems reasonable at first glance; there might have to be minor changes when it's actually implemented, but it's surely basically sound.  (I mean that it has to be possible to split sage-(p)test into pieces, one of which implements your Doctester API, and one which calls it.)

Merging sage-doctest into the same code seems trickier, especially if you mean it to also run in the same process.

I'm afraid I'm not giving very good feedback... "sounds like a good idea, but it might be hard" :)  The problem is that at the moment I don't understand sage-test, sage-ptest, and sage-doctest well enough to give more detailed comments.


---

Comment by mhansen created at 2010-08-07 06:18:39

Quite awhile ago, I had some success with using nose ( http://code.google.com/p/python-nose/ ) to test Sage.  I'm not sure if I still have that code.  It might be something to look into since a number of projects use it for testing.


---

Comment by drkirkby created at 2010-08-07 06:45:06

Replying to [comment:12 mhansen]:
> Quite awhile ago, I had some success with using nose ( http://code.google.com/p/python-nose/ ) to test Sage.  I'm not sure if I still have that code.  It might be something to look into since a number of projects use it for testing.

Sqlalchemy (a standard package in Sage) has a set of self-tests which rely on 'nose'. I did ask on sage-devel a few weeks back if that should be included in Sage, but what response I did get was negative. 

I'm keen we have more testing of the individual components of Sage. At the minute, few have spkg-check files, and as I say, at least sqlalchemy will not work without nose. 

#9281 has a list of all the standard packages and whether they have an spkg-check file. The number is depressing small - about 20% of them. 

Dave


---

Comment by leif created at 2010-12-16 02:31:07

I have some more comments (here just on `sage-ptest`) I'll post inline also here:


```diff
diff --git a/sage-ptest b/sage-ptest
--- a/sage-ptest
+++ b/sage-ptest
@@ -81,12 +81,18 @@
     Returns true if the file should not be tested
     """
     if not os.path.exists(F):
+        # XXX IMHO this should never happen; in case it does, it's certainly
+        #     an error to be reported (either filesystem, or bad name specified
+        #     on the command line). -leif
         return True
     G = abspath(F)
     i = G.rfind(os.path.sep)
+    # XXX The following should IMHO be performed in populatefilelist():
+    #     (Currently, populatefilelist() only looks for "__nodoctest__".)
     if os.path.exists(os.path.join(G[:i], 'nodoctest.py')):
         printmutex.acquire()
         print "%s (skipping) -- nodoctest.py file in directory"%abs(F)
+        sys.stdout.flush()
         printmutex.release()
         return True
     filenm = os.path.split(F)[1]
@@ -95,6 +101,7 @@
         return True
     if G.find(os.path.join('doc', 'output')) != -1:
         return True
+    # XXX The following is (also/already) handled in populatefilelist():
     if not (os.path.splitext(F)[1] in ['.py', '.pyx', '.tex', '.pxi', '.sage', '.rst']):
         return True
     return False
@@ -115,6 +122,7 @@
     for i in range(0,numiteration):
         os.chdir(os.path.dirname(F))
         command = os.path.join(SAGE_ROOT, 'local', 'bin', 'sage-%s' % cmd)
+        # FIXME: Why call bash here? (Also, we use 'shell=True' below anyway.)
         s = 'bash -c "%s %s > %s" ' % (command, filestr, outfile.name)
         try:
             t = time.time()
@@ -161,10 +169,12 @@
         print sage_test_cmd(F[len(CUR)+1:])
     else:
         print abs(F)
+    sys.stdout.flush()
     if ol!="" and (not ol.isspace()):
         if (ol[len(ol)-1]=="\n"):
             ol=ol[0:len(ol)-1]
         print ol
+        sys.stdout.flush()
     time_dict[abs_sage_path(F)] = finished_time
     if XML_RESULTS:
         t = finished_time
@@ -192,6 +202,7 @@
         """.strip() % locals())
         f.close()
     print "\t [%.1f s]"%(finished_time)
+    sys.stdout.flush()
 
 def infiles_cmp(a,b):
     """
@@ -231,7 +242,14 @@
                 base, ext = os.path.splitext(F)
                 if not (ext in ['.sage', '.py', '.pyx', '.tex', '.pxi', '.rst']):
                     continue
-                elif '__nodoctest__' in files:
+                elif '__nodoctest__' in files: # XXX Shouldn't this be 'lfiles'?
+                    # Also, this test should IMHO be in the outer loop (1 level).
+                    # Furthermore, the current practice is to put "nodoctest.py"
+                    # files in the directories that should be skipped, not
+                    # "__nodoctest__". (I haven't found a single instance of the
+                    # latter in Sage 4.6.1.alpha3.)
+                    # "nodoctest.py" is handled in skip() (!), to also be fixed.
+                    # -leif
                     continue
                 appendstr = os.path.join(root,F)
                 if skip(appendstr):
@@ -252,6 +270,9 @@
     argv = [X for X in argv if X[0] != '-']
 
     try: 
+        # FIXME: Nice, but <NUMTHREADS> should immediately follow '-tp' etc.,
+        #        i.e., be the next argument. We might have file or directory
+        #        names that properly convert to an int...
         numthreads = int(argv[1])
         infiles = argv[2:]
     except ValueError: # can't convert first arg to an integer: arg was probably omitted
```

(This is against Sage 4.6.1.alpha3.)

The comments all refer to inconsistencies; the only actual change is flushing the output since it currently comes in bursts, which is IMHO odd for watching it. I don't think this measurably slows down doctesting...


---

Comment by jhpalmieri created at 2011-09-11 17:32:23

Some random comments:

 1. If we keep `SAGE_TESTDIR` as a subdirectory of `DOT_SAGE`, we should call it `DOT_SAGE/testing/` instead of `DOT_SAGE/tmp/`.  This describes the directory better, and the directory can contain timing files, for example, which are intended to persist, not be temporary.

 2. Note that the script `sage-test` creates `SAGE_TESTDIR` as `DOT_SAGE/tmp`, and then creates a further subdirectory `tmp` of this.  I don't think there is any reason for this subdirectory to exist.

 3. Note also `sage-maketest` which writes files to `SAGE_TESTDIR`.  (It also has a different default setting for this variable.)  This script may not require any modification, but it's another one to keep an eye on.


---

Comment by leif created at 2011-09-11 18:40:16

Changing keywords from "" to "testlong maketest parallel race condition unique doctest directories".


---

Comment by leif created at 2011-09-11 18:40:16

Replying to [comment:16 jhpalmieri]:
>  1. If we keep `SAGE_TESTDIR` as a subdirectory of `DOT_SAGE`, we should call it `DOT_SAGE/testing/` instead of `DOT_SAGE/tmp/`.  This describes the directory better, and the directory can contain timing files, for example, which are intended to persist, not be temporary.

At least for the _temporary_ files, I think the name of the subdirectory should also contain the hostname and the PID of the parent process (just like `sage-ptest` now manages this, cf. #9739), to support e.g. running `make testlong` simultaneously from different machines sharing the same filesystem, i.e., sharing the `DOT_SAGE` directory or whatever `SAGE_TESTDIR` might be, and also running different instances of e.g. `make testlong` or `sage -t ...` _on the same machine_ at the same time.

(At least Dave requested this feature, cf. [comment:ticket:9739:19 his comment here] and [comment:ticket:9739:21 here], and [comment:ticket:9739:83 my suggestion].)

Timings should perhaps have their own, persistent directory. Either we accept the possibility of race conditions there, or we should add e.g. the hostname and the time (the former reasonable anyway), eventually also the PID, to the filenames.




>  2. Note that the script `sage-test` creates `SAGE_TESTDIR` as `DOT_SAGE/tmp`, and then creates a further subdirectory `tmp` of this.  I don't think there is any reason for this subdirectory to exist.

Yep, that's odd. We have a whole bunch of `tmp` / `temp` subdirectories all around.


---

Comment by jhpalmieri created at 2011-09-11 19:30:50

Replying to [comment:17 leif]:
> Replying to [comment:16 jhpalmieri]:
> >  1. If we keep `SAGE_TESTDIR` as a subdirectory of `DOT_SAGE`, we should call it `DOT_SAGE/testing/` instead of `DOT_SAGE/tmp/`.  This describes the directory better, and the directory can contain timing files, for example, which are intended to persist, not be temporary.
> 
> At least for the _temporary_ files, I think the name of the subdirectory should also contain the hostname and the PID of the parent process.

Right, my intention was, by default anyway, to create such a temporary directory inside SAGE_TESTDIR.  Or we can have separate environment variables for the (parent of the) testing directory and the directory containing timing files, etc.


---

Comment by roed created at 2012-02-06 04:46:47

Note that Robert Bradshaw has a bunch of code that I'm working on incorporating into Sage that redoes the doctesting framework (and adds various nice features).  See #12415.


---

Comment by jdemeyer created at 2013-02-22 21:34:00

Resolution: duplicate


---

Comment by jdemeyer created at 2013-02-22 21:34:00

Superseded by #12415.

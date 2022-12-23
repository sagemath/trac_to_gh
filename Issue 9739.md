# Issue 9739: Handle duplicate file basenames when testing multiple files in parallel

Issue created by migration from https://trac.sagemath.org/ticket/9739

Original creator: mpatel

Original creation time: 2010-08-13 01:27:24

Assignee: mvngu

CC:  drkirkby jhpalmieri leif robertwb jdemeyer

When we test

`/path/to/foo.py`

`sage-doctest` writes

`SAGE_TESTDIR/.doctest_foo.py`

runs the new file through `python`, and deletes it.  This can cause
collisions when we test in parallel multiple files with the same
basename, e.g., `__init__`, `all`, `misc`, `conf`, `constructor`, `morphism`, `index`, `tests`, `homset`, `element`, `twist`, `tutorial`, `sagetex`, `crystals`, `cartesian_product`, `template`, `ring`, etc.

There's a similar problem with testing non-library files, which `sage-doctest` first effectively copies to `SAGE_TESTDIR`.

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/0239f712a39fce4a/367bfc0d83c0e9b8#367bfc0d83c0e9b8) for background.


---

Comment by mpatel created at 2010-08-13 01:30:39

William Stein [suggests](http://groups.google.com/group/sage-devel/browse_thread/thread/0239f712a39fce4a/488672084383d442#488672084383d442):

```
Could we use the tempfile module instead of using SAGE_TESTDIR.  The
tempfile module makes files and directories by default that are unique
and are *designed* to live on a fast filesystem, which gets cleaned
regularly.

sage: import tempfile 
```



---

Attachment

Frequency-sorted list of doctest file basenames (includes .py, .pyx, .pxi, .rst, .tex files).  Not a patch.


---

Comment by mpatel created at 2010-08-13 01:49:29

I've attached a list of ~1500 unique basenames for the ~2500 files we doctest (give or take a handful).


---

Comment by mpatel created at 2010-09-04 06:52:17

Doctest with unique temporary files.  Apply to scripts repo.


---

Attachment

I've attached a patch.  I haven't modified `sage-test`, since we're likely to phase it out at #9224.


---

Comment by mpatel created at 2010-09-04 07:01:05

Changing status from new to needs_review.


---

Comment by leif created at 2010-09-04 07:39:55

Hmmm, I'm not sure if people will like substituting the filename with the whole test command everywhere. (I have a wide screen, but...)

Can we please stop creating "hidden" doctest files? To me that doesn't make sense at all; especially but not limited to files in `~/.sage/*/`.

Does the _"For whitespace errors, see ..."_ still work (i.e., print the correct filename)?

The notion of _"absolute filenames relative to ..."_ is a bit weird... (But thanks for renaming `abs()`. :) )

The rest seems ok; I've yet only looked at the patch though.


---

Comment by leif created at 2010-09-04 08:10:22

While printing the number of global and file iterations even if both are 1 isn't that useful, I'd like to see the current / appropriate timeout setting[s] printed in `sage-ptest` (i.e. `SAGE_TIMEOUT` for normal tests, and _only_ `SAGE_TIMEOUT_LONG` when `-long` was given).

(In principle, files containing no examples marked `# long time` should IMHO _not_ be tested with `SAGE_TIMEOUT_LONG`, but the normal timeout. In that case we should print both timeout settings, and perhaps also indicate with which a file is being tested.)


---

Comment by leif created at 2010-09-04 08:16:30

Replying to [comment:5 leif]:
> Hmmm, I'm not sure if people will like substituting the filename with the whole test command everywhere. (I have a wide screen, but...)

Ok, sorry, hard to read. The behavoir seems to be the same as before...


---

Comment by drkirkby created at 2010-09-04 09:25:44

How should I best apply this:


```
drkirkby@hawk:~/2/sage-4.5.3.alpha2$ cd local/bin
drkirkby@hawk:~/2/sage-4.5.3.alpha2/local/bin$ hg qimport  http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9739/trac_9739-unique_doctest_names.patch
adding trac_9739-unique_doctest_names.patch to series file
drkirkby@hawk:~/2/sage-4.5.3.alpha2/local/bin$ hg push
abort: repository /space/rlm/sage-4.1.rc1/local/bin not found!
```


Something, somewhere seems to be looking for some directory of what I assume is Robert Millers. 

Dave


---

Comment by mpatel created at 2010-09-04 09:30:58

Replying to [comment:8 drkirkby]:
> Something, somewhere seems to be looking for some directory of what I assume is Robert Millers. 

What happens if you (re)move `SAGE_LOCAL/bin/.hg/hgrc`?  The problem might be that when you're in `SAGE_LOCAL/bin`, you're invoking `./hg`, instead of `/usr/local/bin/hg`.


---

Comment by robertwb created at 2010-09-16 00:58:58

Note that you don't want to create a race condition with two tests
trying to create the same directory at the same time. Perhaps mangling
"/" -> "." would be sufficient.


---

Comment by mpatel created at 2010-10-02 21:58:14

Replying to [comment:11 robertwb]:
> Note that you don't want to create a race condition with two tests
> trying to create the same directory at the same time. Perhaps mangling
> "/" -> "." would be sufficient.

Thanks, Robert.  How about adding the process ID, too, or instead?  I'd also like to reduce the chance of races when we run multiple `sage -t(p)` commands simultaneously with the same `DOT_SAGE`.  Or are there other potential races under this directory, e.g., in `DOT_SAGE/gap`?


---

Comment by mpatel created at 2010-10-02 21:58:20

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-10-23 17:07:04

Has there been any more thoughts on this? 

I had a doctest failure today on my OpenSolaris machine _hawk_, which is almost certainly a result of this bug. This is using sage-4.6.rc0.


```
The following tests failed:

	sage -t  -long local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/notebook/misc.py # 0 doctests failed
	sage -t  -long devel/sage/sage/plot/plot.py # 5 doctests failed
```


The likely reason for the first of these failures can be seen if we look further up the log. 


```
sage -t  -long local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/misc/misc.py
         [2.9 s]
sage -t  -long local/lib/python2.6/site-packages/sagenb-0.8.2-py2.6.egg/sagenb/notebook/misc.py
python: can't open file '/export/home/drkirkby/.sage//tmp/misc.py': [Errno 2] No such file or directory

         [0.2 s]
```


The log clearly shows a file `misc.py` being tested, followed by a second test with a different file also called `misc.py`. That file is then not found. It seems almost inevitable one test deleted the file needed by another test as they were both called `misc.py` and both tested around the same time. 

Note this is the same machine on which the buildbot passed all doctests. 

http://build.sagemath.org/sage/builders/hawk%20full/builds/8/steps/shell_6/logs/stdio

so it seems to be an intermittent problem. (I've also had all tests pass on this). 

These doctests issues are really annoying, as one never knows if its a real Sage bug, or a doctest bug. 

Dave


---

Comment by mpatel created at 2010-10-23 21:42:54

I'm planning to return to this soon, probably after 4.6 is out.


---

Comment by jdemeyer created at 2010-10-24 08:26:40

Replying to [comment:16 mpatel]:
> I'm planning to return to this soon, probably after 4.6 is out.
That would be great, because I have also hit this error quite a few times.


---

Comment by jdemeyer created at 2010-10-25 08:00:02

Changing priority from critical to blocker.


---

Comment by jdemeyer created at 2010-10-25 08:00:02

Changing keywords from "" to "doctest scripts".


---

Comment by drkirkby created at 2010-10-31 13:01:11

There is another problem, which could exist even if every file had a different name. 

If one tests multiple instances of Sage serially, then since they both write to $HOME/.sage, failures can occur even if the file names of the doctests are unique to any one copy of Sage. They need to be unique for any number of instances of Sage. I think testing under $HOME/.sage is a bit silly myself - it would be better to test under the directory where Sage is installed. 

I found that testing `devel/sage/sage/libs/fplll/fplll.pyx` (see #10195), would generate problems when I was testing two copies of Sage at the same time (slightly different versions). I don't know if this patch can handle that situation, but it would be good if it could. 

Dave


---

Comment by leif created at 2010-10-31 13:31:37

Replying to [comment:19 drkirkby]:
> There is another problem, which could exist even if every file had a different name. 
> 
> If one tests multiple instances of Sage serially, then since they both write to $HOME/.sage, failures can occur even if the file names of the doctests are unique to any one copy of Sage.

Well this would definitely be a *user error*. You can always set `DOT_SAGE` or `SAGE_TESTDIR` (or whatever it is called) if you want to run multiple tests simultaneously in different shells, even in / with the _same_ Sage installation.

> They need to be unique for any number of instances of Sage. I think testing under $HOME/.sage is a bit silly myself - it would be better to test under the directory where Sage is installed.

Definitely not, since this wouldn't work for site installations, where users usually have no write permissions under `SAGE_ROOT`.


> I don't know if this patch can handle that situation, but it would be good if it could.

One could use Sage's PID, user and machine parameters etc. to try to create unique directories, or generally create "random" directories with `mktemp (1)` or `mkdtemp()`, but I think this would be an overkill, since the user can itself do such by setting one of the above variables.


---

Comment by drkirkby created at 2010-10-31 19:34:28

Replying to [comment:20 leif]:
> Replying to [comment:19 drkirkby]:
> > There is another problem, which could exist even if every file had a different name. 
> > 
> > If one tests multiple instances of Sage serially, then since they both write to $HOME/.sage, failures can occur even if the file names of the doctests are unique to any one copy of Sage.
> 
> Well this would definitely be a *user error*. You can always set `DOT_SAGE` or `SAGE_TESTDIR` (or whatever it is called) if you want to run multiple tests simultaneously in different shells, even in / with the _same_ Sage installation.
> 
> > They need to be unique for any number of instances of Sage. I think testing under $HOME/.sage is a bit silly myself - it would be better to test under the directory where Sage is installed.
> 
> Definitely not, since this wouldn't work for site installations, where users usually have no write permissions under `SAGE_ROOT`.
> 
> 
> > I don't know if this patch can handle that situation, but it would be good if it could.
> 
> One could use Sage's PID, user and machine parameters etc. to try to create unique directories, or generally create "random" directories with `mktemp (1)` or `mkdtemp()`, but I think this would be an overkill, since the user can itself do such by setting one of the above variables.

I disagree. I don't think creating unique temporary files is overkill. It would be far less error prone. With a test you want to run many times, having a dozen copies of Sage around for test purposes is quite a sensible thing to do with multi-core machines. Havving to set DOT_SAGE for each is annoying, when a unique temporary file could be made. 

Dave


---

Comment by leif created at 2010-10-31 20:01:45

Replying to [comment:21 drkirkby]:
> I disagree. I don't think creating unique temporary files is overkill. 

I didn't say that, but it IMHO suffices to have unique names in the namespace of a ptest run.


> It would be far less error prone. With a test you want to run many times, having a dozen copies of Sage around for test purposes is quite a sensible thing to do with multi-core machines. Havving to set DOT_SAGE for each is annoying, when a unique temporary file could be made.

As I said, you can automatically set up unique test directories by setting one of the above variables e.g. based on the "login" shell's PID, one per terminal / shell.

If multiple machines share the same filesystem, simply add e.g. the hostname, too.


---

Comment by robertwb created at 2010-11-02 02:06:30

+1 to temp (per instance) directories. They would get cleaned up properly, and /tmp is almost always fast and local which is another plus. 

(Really, we shouldn't have to be writing these files out at all...)


---

Comment by drkirkby created at 2010-11-02 08:16:51

Replying to [comment:23 robertwb]:
> +1 to temp (per instance) directories. They would get cleaned up properly, and /tmp is almost always fast and local which is another plus. 
> 
> (Really, we shouldn't have to be writing these files out at all...)

I'm not sure if you are agreeing with me or Leif there Robert - perhaps you can clarify. 

I was going to suggest that we should be using /tmp, but I did not since I can see a disadvantage of it. NFS file systems have caused problems with doc tests failing, especially if they are mis-configured. As such, it would be better if a user tested Sage on the file system where it will be used. By using /tmp they might get a false sense of security. That said, using /tmp for temporary files has been the norm for years. 

I personally think where reasonably practical, we should stop multiple instances of running Sage tests interfering with each other. Although Leif considers this a user error, it is one that a user might easily make. 

But if it possible to avoid creating temporary files, then that should be done. But I would imagine that requires more changes than just adding a pid or hostname. 

Dave


---

Comment by leif created at 2010-11-03 02:38:54

OT: My `make ptestlong` of Sage 4.6 on Ubuntu 9.04 x86 somehow went into an infinite loop...

This never happened before (in dozens of builds), any idea?

(I started the complete build with `make ptestlong`, build succeeded and building the documentation went normal, but now I'm meanwhile at the tenth doctest run! Checked this with `grep Doctesting ptestlong.log`.)


---

Comment by robertwb created at 2010-11-03 08:07:14

Replying to [comment:24 drkirkby]:
> Replying to [comment:23 robertwb]:
> > +1 to temp (per instance) directories. They would get cleaned up properly, and /tmp is almost always fast and local which is another plus. 
> > 
> > (Really, we shouldn't have to be writing these files out at all...)
> 
> I'm not sure if you are agreeing with me or Leif there Robert - perhaps you can clarify. 

Agreeing with drkirkby, we should use temp directories. 

> I was going to suggest that we should be using /tmp, but I did not since I can see a disadvantage of it. NFS file systems have caused problems with doc tests failing, especially if they are mis-configured. As such, it would be better if a user tested Sage on the file system where it will be used. By using /tmp they might get a false sense of security. That said, using /tmp for temporary files has been the norm for years. 

Don't know if mktemp is POSIX, but it's widely available. Of course from Python you always have http://docs.python.org/library/tempfile.html Both are much better than manually specifying /tmp. 

> I personally think where reasonably practical, we should stop multiple instances of running Sage tests interfering with each other. Although Leif considers this a user error, it is one that a user might easily make. 

I don't consider it a user error, and I also don't like filling .sage with lots of junk. 

> But if it possible to avoid creating temporary files, then that should be done. But I would imagine that requires more changes than just adding a pid or hostname. 

True, and this ticket has been opened for far too long. 

- Robert


---

Comment by leif created at 2010-11-03 18:02:52

Replying to [comment:25 leif]:
> OT: My `make ptestlong` of Sage 4.6 on Ubuntu 9.04 x86 somehow went into an infinite loop...
> 
> This never happened before (in dozens of builds), any idea?
> 
> (I started the complete build with `make ptestlong`, build succeeded and building the documentation went normal, but now I'm meanwhile at the tenth doctest run! Checked this with `grep Doctesting ptestlong.log`.)
> 

Ouch. I just noticed I had set `SAGE_TEST_GLOBAL_ITER=1000` earlier in that shell...

(But all tests passed; I then aborted it during the 14th run.)


---

Comment by jdemeyer created at 2010-11-07 10:48:18

What is the current status of this patch, do you consider it ready for review?  If not, I'm willing to join in and help where needed.


---

Comment by mpatel created at 2010-11-07 23:37:46

Replying to [comment:28 jdemeyer]:
> What is the current status of this patch, do you consider it ready for review?  If not, I'm willing to join in and help where needed.

It's not ready for review.  I don't think I have the time to work on this in the next several days, so if you'd like to help, please do!

I think we can make a temporary directory for each run in `sage-(p)test` and pass it to `sage-doctest`, which should ensure the temporary files under the directory are unique.  The existing doesn't quite yet do the latter, but it should be easy to modify it so it does (e.g., with full paths and/or pids, etc.).


---

Comment by drkirkby created at 2010-11-08 00:08:11

Using both a hostname and a PID should mean the filename is practically unique if people test on more than one computer using a shared drive. I don't think 'mktemp' will be unique on NFS shared drives, though the probability of a collision would then be very small indeed. But adding a hostname would reduce it even further. 

But we need to be careful if using mktemp. Whilst many systems have it, the implementation is not the same on every system. I know Solaris works a bit different to Linux or OS X (I forget which). I know using something on Solaris with mktemp which would not work with Linux or OS X. (I forget which OS it was though). It seems HP-UX and Solaris differ too. 

I would be very keen to use something that will work on AIX. There is a chance of IBM donating a quad core 4.5 GHz machine to the Sage project with AIX on it. 

Anyway, whatever solution is used, I think it will be 1000x better than the current solution, but personally I'd like to see something that's unique to a machine and portable. 

Dave


---

Comment by jdemeyer created at 2010-12-02 15:05:22

I'm still interested in working on this patch, but I don't expect it to be ready on time for 4.6.1.


---

Comment by leif created at 2010-12-16 02:45:27

While we are at it, I have some more comments on `sage-ptest` I'll also post here with an inline patch:


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

Comment by leif created at 2010-12-16 03:11:41

Just for the record:

#10458 also patches `sage-ptest` to support IPython/Sage-style line continuations in doctests ("`....: `" rather than only "`...`").


---

Comment by leif created at 2010-12-16 03:15:16

Replying to [comment:33 leif]:
> Just for the record:
> 
> #10458 also patches `sage-ptest` to support IPython/Sage-style line continuations in doctests ("`....: `" rather than only "`...`").

Ooops, sorry, #10458 patches `sage-doctest`, *not* `sage-ptest`.


---

Comment by forextrading11 created at 2011-01-27 21:11:15

Changing type from defect to task.


---

Comment by forextrading11 created at 2011-01-27 21:11:15

Replying to [ticket:9739 mpatel]:
> When we test
> 
> `/path/to/foo.py`
> 
> `sage-doctest` writes
> 
> `SAGE_TESTDIR/.doctest_foo.py`
> 
> runs the new file through `python`, and deletes it.  This can cause
> collisions when we test in parallel multiple files with the same
> basename, e.g., `__init__`, `all`, `misc`, `conf`, `constructor`, `morphism`, `index`, `tests`, `homset`, `element`, `twist`, `tutorial`, `sagetex`, `crystals`, `cartesian_product`, `template`, `ring`, etc.
> 
> There's a similar problem with testing non-library files, which `sage-doctest` first effectively copies to `SAGE_TESTDIR`.
> 
> See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/0239f712a39fce4a/367bfc0d83c0e9b8#367bfc0d83c0e9b8) for background.
> 
> This ticket may help with some of the doctesting problems discussed on the Sage mailing lists.  Related tickets: #9224, #9225, #9449.


---

Comment by forextrading11 created at 2011-01-27 21:11:15

Changing keywords from "doctest scripts" to "currency trading, forex analysis, forex trading, online forex trading".


---

Comment by forextrading11 created at 2011-01-27 21:11:15

Changing priority from blocker to trivial.


---

Comment by forextrading11 created at 2011-01-27 21:11:15

Changing component from doctest to build.


---

Comment by jason created at 2011-01-28 06:49:43

Changing type from task to defect.


---

Comment by jason created at 2011-01-28 06:49:43

Changing keywords from "currency trading, forex analysis, forex trading, online forex trading" to "doctest scripts".


---

Comment by jason created at 2011-01-28 06:49:43

Changing priority from trivial to blocker.


---

Comment by jason created at 2011-01-28 06:49:43

Changing component from build to doctest.


---

Comment by jason created at 2011-01-28 06:50:24

Please ban forextrading11 for spam.


---

Comment by mvngu created at 2011-01-28 07:06:59

Replying to [comment:37 jason]:
> Please ban forextrading11 for spam.

Done.


---

Comment by drkirkby created at 2011-04-07 21:25:20

Replying to [comment:39 jdemeyer]:

This is marked as a blocker for 4.7. but there's been no work on it for 8 weeks. 

Dave


---

Comment by jdemeyer created at 2011-04-18 08:32:55

Changing priority from blocker to critical.


---

Comment by leif created at 2011-07-27 12:39:45

To me it would -- at least for the moment, or this ticket -- be totally sufficient to have unique filenames by mangling the relative path into the temporary filename.

If someone wants to test multiple Sage installations at the same time, he can simply set `SAGE_TESTDIR` to different locations in each shell.

Doctesting in (or below) `$DOT_SAGE` (which is usually `$HOME/.sage/`) is IMHO a bad idea anyway, not only because `/tmp/` is much more likely to be [on] a local filesystem than `/home/`. (It is usually also faster and auto-cleaned.) Creating a unique temporary directory there shouldn't be a problem.

For the sake of _"For whitespace errors see ..."_, failing files could still be copied elsewhere (to a perhaps more persistent location) at the end of the doctest process.


---

Comment by leif created at 2011-07-27 13:00:45

I've restored the original description the spammer deleted.


---

Comment by leif created at 2011-07-27 14:07:47

For the record, we already have the following in `sage/misc/misc.py`:


```python
...
HOSTNAME = socket.gethostname().replace('-','_').replace('/','_').replace('\\','_')

LOCAL_IDENTIFIER = '%s.%s'%(HOSTNAME , os.getpid())
...
try:
    DOT_SAGE = os.environ['DOT_SAGE']
except KeyError:
    try:
        DOT_SAGE = '%s/.sage/'%os.environ['HOME']
    except KeyError:
        DOT_SAGE = '%s/.sage/'%SAGE_ROOT
...
if not os.path.exists(DOT_SAGE):
    os.makedirs(DOT_SAGE)

_mode = os.stat(DOT_SAGE)[stat.ST_MODE]
_desired_mode = 040700     # drwx------
if _mode != _desired_mode:
    print "Setting permissions of DOT_SAGE directory so only you can read and write it."
    # Change mode of DOT_SAGE.
    os.chmod(DOT_SAGE, _desired_mode)
...
SAGE_TMP='%s/temp/%s/%s/'%(DOT_SAGE, HOSTNAME, os.getpid())
if not os.path.exists(SAGE_TMP):
    try:
        os.makedirs(SAGE_TMP)
    except OSError, msg:
        print msg
        raise OSError, " ** Error trying to create the Sage tmp directory..."
...
```



---

Comment by leif created at 2011-07-27 14:28:56

... so we could do almost the same for / below `SAGE_TESTDIR`, perhaps creating a single directory name from `HOSTNAME` and the PID (avoiding further race conditions, provided `$SAGE_TESTDIR` already exists), putting all temporary files (names mangled as proposed, unique to each _test instance_) into that, i.e.

`${SAGE_TESTDIR}/${hostname}-${pid}/doctest-relative__path__to__foo__foo.py`

for a file `./relative/path/to/foo/foo.py`.


---

Comment by jhpalmieri created at 2011-07-27 14:58:03

Can we just use Python's tempfile module, for example [mkstemp](http://docs.python.org/library/tempfile.html#tempfile.mkstemp)?  This should produce a temporary file safely, avoiding race conditions.  We can have the name end with the file being tested, including its path.

(I think we should do the same thing for `SAGE_TMP` in `misc.py`, but that's for another ticket.)


---

Comment by leif created at 2011-07-27 15:08:57

Replying to [comment:47 jhpalmieri]:
> Can we just use Python's tempfile module, for example [mkstemp](http://docs.python.org/library/tempfile.html#tempfile.mkstemp)?  This should produce a temporary file safely, avoiding race conditions.  We can have the name end with the file being tested, including its path.

I see no reason for doing so. We don't need even more cryptic filenames, and I don't think it will work across NFS filesystems.

The only "race condition" that can occur in what I suggested above is in the creation of `SAGE_TESTDIR` itself (if it doesn't already exist), and that can easily be catched.

> (I think we should do the same thing for `SAGE_TMP` in `misc.py`, but that's for another ticket.)

I wouldn't do that either. If we create temporary files from shell scripts, we can use the same mechanism.


---

Comment by leif created at 2011-07-27 15:19:23

Furthermore:

 _"The file descriptor is not inherited by child processes."_

 _"There is thus no guarantee that the generated filename will have any nice properties, such as not requiring quoting when passed to external commands via `os.popen()`."_


---

Comment by jhpalmieri created at 2011-07-27 15:38:33

> I see no reason for doing so.

There are several reasons for doing so: one is to not reinvent the wheel, and anything we come up with is likely to be less robust than what's built into Python.  Also, if we want to doctest outside of `$HOME/.sage`, is `/tmp` always the best place?  The mkstemp function doesn't always create files there, so I'm not convinced we should.

By the way, using the PID in the directory name means creating many directories: as far as I can tell, running `sage -t DIR` uses a different process for each file in DIR.  Perhaps the PID should be in the mangled filename instead of part of a new directory.


---

Comment by leif created at 2011-07-27 15:44:46

Still, the best thing is to not create temporary files at all.

(And only dump what would have been written in case of doctest errors, once at the end, with the "same problems", though identical filenames would there be even more unlikely, and could easily be numbered.)

But that's probably for another ticket; we should IMHO here only _quickly_ fix the most prominent errors, namely identical filenames within the _same_ `ptest`[`long`] instance. If we also allow simultaneous testing of the same or different Sage installations, that's ok, but a pretty minor issue, because -- in contrast to the former -- you can trivially avoid race conditions between such concurrent `ptest` runs. (And a normal user wouldn't do the latter either.)


---

Comment by leif created at 2011-07-27 16:06:19

Replying to [comment:50 jhpalmieri]:
> > I see no reason for doing so.
> 
> There are several reasons for doing so: one is to not reinvent the wheel, and anything we come up with is likely to be less robust than what's built into Python.

Amen? Also, unless it uses a local filesystem, I don't think it will work with NFS.

>  Also, if we want to doctest outside of `$HOME/.sage`, is `/tmp` always the best place?  The mkstemp function doesn't always create files there, so I'm not convinced we should.

It simply (in contrast to Sage) respects the commonly used `TMP` (`TEMP` on M$ Windows) and `TMPDIR` environment variables.

Btw, on typical machines `/tmp` does not even really exist on a drive, it's just in memory (and if that's exhausted, swap space will be used transparently). If it is a real partition on a drive, you either use an SSD or at least use that area of a conventional hard drive that is fastest (same for swap).

> By the way, using the PID in the directory name means creating many directories: as far as I can tell, running `sage -t DIR` uses a different process for each file in DIR.  Perhaps the PID should be in the mangled filename instead of part of a new directory.

At least at the moment, we're dealing with `ptest*` only here, so that's another matter (if you want to run multiple `testlong`s for example using the same temporary directory). So `sage -t ...` wouldn't create any directories at all.


---

Comment by jhpalmieri created at 2011-07-27 16:42:48

Replying to [comment:52 leif]:

> > By the way, using the PID in the directory name means creating many directories: as far as I can tell, running `sage -t DIR` uses a different process for each file in DIR.  Perhaps the PID should be in the mangled filename instead of part of a new directory.
> 
> At least at the moment, we're dealing with `ptest*` only here, so that's another matter (if you want to run multiple `testlong`s for example using the same temporary directory). So `sage -t ...` wouldn't create any directories at all.

I was envisioning patching sage-doctest, since that's what copies the file being tested to SAGE_TESTDIR (and later deletes it), and it gets run by "sage -t ...", "sage -tp ...", etc.   Running "sage -tp DIR" also uses a different PID for each execution of sage-doctest.


---

Comment by leif created at 2011-07-27 17:26:05

Replying to [comment:53 jhpalmieri]:
> I was envisioning patching sage-doctest, since that's what copies the file being tested to SAGE_TESTDIR (and later deletes it), and it gets run by "sage -t ...", "sage -tp ...", etc.   Running "sage -tp DIR" also uses a different PID for each execution of sage-doctest.

I would simply pass `sage-doctest` the already created directory (either as a parameter, or simply in the environment variable which it already uses anyway).

Creating the directory inside `sage-doctest` doesn't make any sense, since *all* instances would attempt to create it. (You can or could use `os.getppid()` though.)


The whole collection of doctest scripts needs an overhaul (or redesign) in the long run...

P.S.: We can use `tempfile.gettempdir()` in case `SAGE_TESTDIR` isn't set if that makes you happy.


---

Comment by jhpalmieri created at 2011-07-27 18:41:12

Right now, if there are doctest failures or if doctesting is interrupted, the temporary files remain in SAGE_TEMPDIR.  If we create a new directory each time, then these directories will remain (we should certainly check if they're empty and then delete them, but if they're not empty, we should not automatically delete them, I think).  Is it any better or worse to have a bunch of directories in SAGE_TEMPDIR, as opposed to a bunch of files?

Meanwhile, here's an attempt at a patch.


---

Comment by jhpalmieri created at 2011-07-27 18:41:12

Changing status from needs_work to needs_review.


---

Comment by leif created at 2011-07-28 14:24:55

At this point just a comment on the naming / mangling:

 * To me, it doesn't make any sense to create "hidden" files, so I would omit the leading period.
 * We should perhaps apply some character substitutions to `socket.gethostname()` as well, like `sage.misc.misc` does (see quote above).
 * Thinking more about it, I would replace slashs (`os.path.sep`) by periods (and not double-underscores or, as currently, dashs), since that way the temporary filenames resemble (at least partially) fully qualified Python module names.

(As discussed, I'd also change the _default_ for `SAGE_TESTDIR`, e.g. to `tempfile.gettempdir()`.)

We could make sure once that the temporary directory (`${SAGE_TESTDIR}/${hostname}-${pid}/`) is writable by the user. I think we should also clean it up in case it already exists, as anything left there is potentially very old and unrelated to the current test run. We _might_ also adjust the permissions of the directory.


Looking only at your (John's) patch, is `temp_py_file` defined anywhere? (I only see it gets added to `tmpfiles`.)


P.S.: Why not base the patch on Mitesh's? (Which AFAIR only needed two changes.)


---

Comment by jhpalmieri created at 2011-07-28 16:26:33

Replying to [comment:56 leif]:
> At this point just a comment on the naming / mangling:
> 
>  * To me, it doesn't make any sense to create "hidden" files, so I would omit the leading period.

Okay, not a high priority and outside the scope of this ticket, but harmless enough.  Done.  (We could do the same thing with the files recording timing data, but that's for another ticket.)

>  * We should perhaps apply some character substitutions to `socket.gethostname()` as well, like `sage.misc.misc` does (see quote above).

Done.

>  * Thinking more about it, I would replace slashs (`os.path.sep`) by periods (and not double-underscores or, as currently, dashs), since that way the temporary filenames resemble (at least partially) fully qualified Python module names.

Done.

> 
> (As discussed, I'd also change the _default_ for `SAGE_TESTDIR`, e.g. to `tempfile.gettempdir()`.)

I know that I was suggesting this earlier, but on further reflection, we shouldn't do this here: for example, there may be users who expect the doctesting files to be in `.sage/tmp/`, and changing this may therefore make people unhappy.  I think it's a good idea, but it should be on another ticket. (I'm agreeing with Dave's point that we should try to fix just the bug here, and then we can work on other improvement separately.)

> We could make sure once that the temporary directory (`${SAGE_TESTDIR}/${hostname}-${pid}/`) is writable by the user. I think we should also clean it up in case it already exists, as anything left there is potentially very old and unrelated to the current test run. We _might_ also adjust the permissions of the directory.

Done.

> Looking only at your (John's) patch, is `temp_py_file` defined anywhere? (I only see it gets added to `tmpfiles`.)

That was a mistake, which I think I've fixed.
 
> P.S.: Why not base the patch on Mitesh's? (Which AFAIR only needed two changes.)

No good reason.


---

Comment by jhpalmieri created at 2011-07-28 17:40:47

Oops, just found a mistake.  In non-Sage library code, when doctesting "file0.py", we write a line

```
from file0 import *
```

With the name mangling, this doesn't work anymore: the periods confuse things, and so would hyphens, commas, and other symbols not allowed in python module names.  We can either just revert the part of the code involving non-Sage library code, or we can try to fix the mangled names.  Right now I'm doing the first of these, since the first priority should be to fix things for doctesting the Sage library.


---

Comment by leif created at 2011-07-28 17:42:17

Replying to [comment:57 jhpalmieri]:
> Replying to [comment:56 leif]:
> > (As discussed, I'd also change the _default_ for `SAGE_TESTDIR`, e.g. to `tempfile.gettempdir()`.)
> 
> I know that I was suggesting this earlier, but on further reflection, we shouldn't do this here: for example, there may be users who expect the doctesting files to be in `.sage/tmp/`, and changing this may therefore make people unhappy.  I think it's a good idea, but it should be on another ticket. (I'm agreeing with Dave's point that we should try to fix just the bug here, and then we can work on other improvement separately.)

That was my opinion; Dave earlier requested extensions to allow _simultaneous_ testing (including `make test`[`long`] etc.) of _multiple_ (possibly the same) Sage installations in the "same" directory (`SAGE_TESTDIR`), i.e. without having to manually set `SAGE_TESTDIR` in different shells.

As further enhancements, we should perhaps print the location at the beginning, and also at the end if any doctest errors occurred. (I'm right now not sure if `GLOBAL_ITER` etc. get printed, I only recall we should also print *either* `SAGE_TIMEOUT` *or* `SAGE_TIMEOUT_LONG`, whichever is appropriate, as many people seem to misunderstand the meaning and perhaps also don't know the defaults, which are btw. _wall_ time and not CPU time -- perhaps subject to change later as well... :) .)

(A few `print` statements wouldn't complicate the patch _here_ though. And if we print `SAGE_TESTDIR` anyway, we could at the same time change its default to a sensible value as well.)




> > P.S.: Why not base the patch on Mitesh's? (Which AFAIR only needed two changes.)
> 
> No good reason.

Hmmm. Mitesh fixed some other things as well, so we should somehow make sure the changes don't get lost once this ticket is merged / closed. (I remember having reviewed them last year, before he updated the patch again though IIRC. I think Robert was also ok with his changes, except for the creation of directories / the temporary files' names and locations.)

Unfortunately, there are meanwhile _many_ "concurrent" tickets dealing with the doctest scripts.

I'd of course also like to see my comments from the [comment:32 inline patch to `sage-ptest` above] in it... ;-) (Just the comments, which are FIXMEs / TODOs, not [necessarily] the `flush()`s.)




I'll apply and take a look at your second patch later.


---

Comment by leif created at 2011-07-28 18:40:15

Replying to [comment:58 jhpalmieri]:
> Oops, just found a mistake.  In non-Sage library code, when doctesting "file0.py", we write a line

```
from file0 import *
```

> With the name mangling, this doesn't work anymore: the periods confuse things, and so would hyphens, commas, and other symbols not allowed in python module names.

Hence underscores, which I originally thought of?

It doesn't make sense to copy [only] each single non-library file to doctest to the temporary directory anyway, as it might import other files located in the original directory.

We could either just `cd` to the original directory, or -- IMHO much better -- add the original directory to `PYTHONPATH` or `sys.path`, both methods solving the mangling issue in `from ... import *`, as well as saving useless copying. (We of course still have to create temporary preparsed files in `SAGE_TESTDIR/.../` for `.sage` and `.spyx` files though.)


---

Comment by jhpalmieri created at 2011-07-28 21:18:12

Replying to [comment:60 leif]:
> Replying to [comment:58 jhpalmieri]:
> > Oops, just found a mistake.  In non-Sage library code, when doctesting "file0.py", we write a line
> {{{
> from file0 import *
> }}}
> > With the name mangling, this doesn't work anymore: the periods confuse things, and so would hyphens, commas, and other symbols not allowed in python module names.
> 
> Hence underscores, which I originally thought of?

Well, the host name could contain all sorts of characters in it, couldn't it?  Same for the directories in the path to the file, especially since we're talking about files not in the Sage library.  Doing some sort of regexp search and replace is a lot of work for perhaps minimal gain.  It certainly doesn't have to do with the issue on this ticket.

> It doesn't make sense to copy [only] each single non-library file to doctest to the temporary directory anyway, as it might import other files located in the original directory.

Outside the scope of this ticket.  If we leave that part alone, we're not creating a new bug, just leaving a less-than-perfect implementation in place.

Meanwhile, if you want to add in some print statements, comments, some of the relevant parts of Mitesh's patch, or anything else, go ahead.  I have to work on some other things for at least a few days.


---

Comment by leif created at 2011-07-29 01:34:21

Replying to [comment:61 jhpalmieri]:
> Replying to [comment:60 leif]:
> > Replying to [comment:58 jhpalmieri]:
> > > Oops, just found a mistake.  In non-Sage library code, when doctesting "file0.py", we write a line

```
from file0 import *
```

> > > With the name mangling, this doesn't work anymore: the periods confuse things, and so would hyphens, commas, and other symbols not allowed in python module names.
> > Hence underscores, which I originally thought of?
> 
> Well, the host name could contain all sorts of characters in it, couldn't it?  Same for the directories in the path to the file, especially since we're talking about files not in the Sage library.
> Doing some sort of regexp search and replace is a lot of work for perhaps minimal gain.

Well, you don't have to mangle the name in the `import` statement at all (and the hostname is part of the _directory_ name, not a filename, anyway).

> It certainly doesn't have to do with the issue on this ticket.

Of course it does. You tried to also mangle the `import` name to avoid name clashs, but that's simply not necessary. Just prepend the original (source) directory of the file to test to `PYTHONPATH`, and keep the [base]name of the file in `from ... import *` unmodified (and of course without a path). 

For files of the Sage library, we strip that path (at least Mitesh did), since all necessary (root) directories are already in `PYTHONPATH`.

The only "problem" are files that have to be preparsed (`*.sage`), at least if we don't want to create the intermediate, preparsed `.py` files at the original location, preferably just once.

For these files, we simply can do almost what Mitesh did, namely create a temporary file with an "arbitrary" (Python module name-conforming) but unique basename and the extension `.py` in `SAGE_TESTDIR` (from the perspective of `sage-doctest`, i.e. already containing the hostname and the pid of the parent process), using either `tempfile.mkstemp()` [which is safe here] or preferably just `sage-doctest`'s PID, import _that_ in the `doctest_*` file, and also append it to `tmpfiles`:

```python
    # We are in "sage-doctest",
    # SAGE_TESTDIR is already ".../${hostname}-${ppid}/"
    ...
    if not library_code: 

        if ext in ['.pyx','.spyx']: 
            s += "cython(open('%s').read())\n\n" % file_name

        elif ext in ['.py', '.sage']: 

            source = file_name # full name with path
            target_name = "%s_%d" % (name, os.getpid()) # like 'name', but unique
            target_base = os.path.join(SAGE_TESTDIR, target_name) # like 'base', also unique

            if ext == '.sage':
                # Unfortunately, "sage -preparse <file>.sage" doesn't have any
                # output options and always creates <file>.py in the same
                # directory, so we first copy the *source* into SAGE_TESTDIR:
                os.system("cp '%s' %s.sage" % (source, target_base))
                # Now create SAGE_TESTDIR/<target_name>.py:
                os.system("sage -preparse %s.sage" % target_base)
                # Remove the copy of the original (.sage):
                # (We could also just add it to 'tmpfiles'.)
                os.system("rm -f %s.sage" % target_base)

            else:
                # Plain Python file (".py"), just copy it:
                # (If we added source's directory to PYTHONPATH,
                # we wouldn't have to copy the file, but then also
                # would have to import from 'name' instead of 'target_name'.)
                os.system("cp '%s' %s.py" % (source, target_base))

            s += "from %s import *\n\n" % target_name

            tmpfiles.append(target_base + ".py") # preparsed or copied original
            tmpfiles.append(target_base + ".pyc") # compiled version of it

    ...
```





A better solution, as Mitesh noted in the `TODO` comment, is to preparse the file into a string, and directly write that string into the `doctest_*` file where we currently have the `from ... import *`.

_That enhancement_ is most probably a thing to do on a follow-up ticket, but not supporting (i.e. avoiding name clashes for) non-library files would be a regression w.r.t. Mitesh's patch.




> > It doesn't make sense to copy [only] each single non-library file to doctest to the temporary directory anyway, as it might import other files located in the original directory.
> 
> Outside the scope of this ticket.  If we leave that part alone, we're not creating a new bug, just leaving a less-than-perfect implementation in place.

See above. I there just copy the "main" file, which we still can change later.




> Meanwhile, if you want to add in some print statements, comments, some of the relevant parts of Mitesh's patch, or anything else, go ahead.  I have to work on some other things for at least a few days.

As I said, I would have preferred having your patch based on Mitesh's, since there are a couple of changes that could have been kept, just changing the "mangling".

I can add a reviewer patch for _my comments_ (and perhaps a few `print` statements) later; rebasing Mitesh's would be a lot of work and so I don't know if I'll do that.


---

Comment by jhpalmieri created at 2011-08-13 01:07:04

Here is a patch based on Mitesh's; the "delta" patch shows the changes; these changes include your in-line patch.  This does not change SAGE_TESTDIR to `tempfile.gettempdir()`: we store timing information in this directory, so it should not be temporary.  It might be a good idea to change `TMP` (as used in `sage-ptest`) to a temporary directory, but I didn't make this change either, just added a comnent about it.

The changes: 
 - the filename mangling uses the full path of the file rather than `tempfile.mkstemp`; this should be good enough, especially since we work in a directory with name determined by the pid and the hostname.
 - there was one situation in which the temporary files stored in `tmpfiles` needed to be deleted but weren't; this was the case before any of the patches.
 - there are now messages printed about the doctesting directory, and then deleting it at the end.


---

Comment by jhpalmieri created at 2011-08-13 01:28:35

Oh, I forgot: I tested this with some non-library code, and it mostly worked.  I say "mostly" because when I set `SAGE_CHECK=yes` and installed the package at #9894, a bunch of files produced errors.  I got the following odd behavior:

 - before applying the patch, after spkg-check ran, it said that maybe a dozen files gave errors, but only 4 of them remained in `SAGE_TESTDIR` (4 of them, plus their `.pyc` files, plus their `.doctest...` files).

 - after applying the patch: for the dozen files which gave errors, all of them remained in `SAGE_TESTDIR`, plus their `.pyc` files, plus only 4 of the `doctest...` files — the ones corresponding to the same 4 files as in the first case.

I don't know what's going on here.  The spkg-check script is not a completely straightforward program; it doesn't just run "sage -tp" on some directory.  So that may cause some of the issues.  Anyway, there are better results after applying the patch than before, but it's still not perfect.

For all of my other tests with non-library code, it worked just the way it should.


---

Comment by leif created at 2011-08-13 04:26:24

_Sorry, atm too tired to look at the whole, only a few remarks before I again forget them..._

Replying to [comment:63 jhpalmieri]:
> Here is a patch based on Mitesh's; the "delta" patch shows the changes; these changes include your in-line patch.

Nice, thanks. Even flushing the output.




> This does not change SAGE_TESTDIR to `tempfile.gettempdir()`: we store timing information in this directory, so it should not be temporary.

Who cares? ;-)

The odd thing with that is that we then again produce potential race conditions for the timing files. I think we'd have to use locking then (which can also cause headaches), perhaps on a follow-up.

IMHO these files also shouldn't be "hidden", and could live in or below `DOT_SAGE` (if we have to use locking anyway). Moreover, they perhaps shouldn't get lost if one "manually" sets `SAGE_TESTDIR` to e.g. `/tmp`, which seems reasonable at least as long as we don't automatically use some presumably fast filesystem for the really temporary files. 




> It might be a good idea to change `TMP` (as used in `sage-ptest`) to a temporary directory, but I didn't make this change either, just added a comnent about it.

Ok, see above; at least documented.




> The changes: 

>  - the filename mangling uses the full path of the file rather than `tempfile.mkstemp`; this should be good enough, especially since we work in a directory with name determined by the pid and the hostname.

This doesn't help when simultaneously testing the same file from one `sage-ptest` instance (`SAGE_TEST_ITER`, `SAGE_TEST_GLOBAL_ITER`) if I'm not wrong; we could mangle *`sage-doctest`'s* PID into the _filename_, too, as I suggested above.




>  - there are now messages printed about the doctesting directory, and then deleting it at the end.

For readability, I'd move the `print` statements (_"Removing the directory ..."_, which hopefully don't raise exceptions) out of the `try` block.

Also, `sage-ptest` should know whether tests failed (or doctesting was interrupted), in which case we don't have to issue a warning since keeping the failed doctest files is intentional (and the left files should have been mentioned in previous messages).

So I wouldn't try to remove the directory if any doctests failed, unless they were [all] interrupted by Ctrl-C (in which case `sage-doctest` should immediately remove all temporary files belonging to the aborted doctest, which it currently doesn't).

----

Btw., unrelated to _this_ ticket: `sage-doctest` shouldn't sleep for 0.1 seconds (and not continually poll the state of the child process) if the timeout is in seconds anyway; instead, it should use `signal.alarm()` and `wait()`.


---

Comment by jhpalmieri created at 2011-08-13 17:01:36

Replying to [comment:65 leif]:

> > This does not change SAGE_TESTDIR to `tempfile.gettempdir()`: we store timing information in this directory, so it should not be temporary.
> 
> Who cares? ;-)

Well, someone might...
 
> The odd thing with that is that we then again produce potential race conditions for the timing files. I think we'd have to use locking then (which can also cause headaches), perhaps on a follow-up.

True, theoretically, but I've never heard of this coming up.  I don't think these files are open for very long, so race conditions should be very rare.  I agree it should be dealt with on a follow-up, if at all.  (Instead of locking, we could perhaps use a "try ... except" block, since if two processes are trying to write to the same timing file, it's not a disaster if we just completely discard one of those.)

> IMHO these files also shouldn't be "hidden", and could live in or below `DOT_SAGE`

I thought about this when working on the most recent patch, but it was too much work for too little gain to make it backwards compatible (if `.ptest_timing...` exists, then read it, otherwise, look for `ptest_timing...`, etc.).  It could be done on another ticket.

>  (if we have to use locking anyway). Moreover, they perhaps shouldn't get lost if one "manually" sets `SAGE_TESTDIR` to e.g. `/tmp`, which seems reasonable at least as long as we don't automatically use some presumably fast filesystem for the really temporary files. 

That's a good point.

> > The changes: 

> >  - the filename mangling uses the full path of the file rather than `tempfile.mkstemp`; this should be good enough, especially since we work in a directory with name determined by the pid and the hostname.
> 
> This doesn't help when simultaneously testing the same file from one `sage-ptest` instance (`SAGE_TEST_ITER`, `SAGE_TEST_GLOBAL_ITER`) if I'm not wrong; we could mangle *`sage-doctest`'s* PID into the _filename_, too, as I suggested above.

I can do that, or we can use `mkstemp` instead of or in addition to the path.  Opinions either way?

> >  - there are now messages printed about the doctesting directory, and then deleting it at the end.
> 
> For readability, I'd move the `print` statements (_"Removing the directory ..."_, which hopefully don't raise exceptions) out of the `try` block.

Okay.

> Also, `sage-ptest` should know whether tests failed (or doctesting was interrupted), in which case we don't have to issue a warning since keeping the failed doctest files is intentional (and the left files should have been mentioned in previous messages).
> 
> So I wouldn't try to remove the directory if any doctests failed, unless they were [all] interrupted by Ctrl-C (in which case `sage-doctest` should immediately remove all temporary files belonging to the aborted doctest, which it currently doesn't).

Perhaps it should, but that should be on another ticket.  As Dave said earlier, "a sub-optimal solution is a better temporary measure than a complete industrial strength bullet-proof solution".  I don't want to have to deal with the inner workings of doctesting here any more than is necessary, and I don't think this particular issue is necessary to deal with for this ticket.  I can add a comment to the code about this.


---

Comment by leif created at 2011-08-13 18:50:31

Replying to [comment:66 jhpalmieri]:
> True, theoretically, but I've never heard of this coming up.  I don't think these files are open for very long, so race conditions should be very rare.  I agree it should be dealt with on a follow-up, if at all.  (Instead of locking, we could perhaps use a "try ... except" block, since if two processes are trying to write to the same timing file, it's not a disaster if we just completely discard one of those.)

Ok, I thought timings were accumulated; never looked at this.

> I thought about this when working on the most recent patch, but it was too much work for too little gain to make it backwards compatible (if `.ptest_timing...` exists, then read it, otherwise, look for `ptest_timing...`, etc.).  It could be done on another ticket.

I wouldn't care much about backward compatibility in this case.




> > >  - the filename mangling uses the full path of the file rather than `tempfile.mkstemp`; this should be good enough, especially since we work in a directory with name determined by the pid and the hostname.
> > 
> > This doesn't help when simultaneously testing the same file from one `sage-ptest` instance (`SAGE_TEST_ITER`, `SAGE_TEST_GLOBAL_ITER`) if I'm not wrong; we could mangle *`sage-doctest`'s* PID into the _filename_, too, as I suggested above.
> 
> I can do that, or we can use `mkstemp` instead of or in addition to the path.  Opinions either way?

I'd prefer `sage-doctest`'s PID, appended (separated by an underscore) as [comment:62 above].




> > Also, `sage-ptest` should know whether tests failed (or doctesting was interrupted), in which case we don't have to issue a warning since keeping the failed doctest files is intentional (and the left files should have been mentioned in previous messages).
> > 

> > So I wouldn't try to remove the directory if any doctests failed, unless they were [all] interrupted by Ctrl-C (in which case `sage-doctest` should immediately remove all temporary files belonging to the aborted doctest, which it currently doesn't).
> 
> Perhaps it should, but that should be on another ticket.

The deletion upon Ctrl-C in `sage-doctest`; I just wouldn't try to remove the directory in `sage-ptest` if any error occurred (along with a perhaps confusing warning message).

> "complete industrial strength bullet-proof solution"

I don't think we'll ever reach this, also because the addition of new features will never stop. So Sage's version number won't converge.

> I can add a comment to the code about this.

I'd appreciate that, such that others can catch up. IMHO too much things end up in ticket comments hardly anybody will see or read later.


---

Comment by jhpalmieri created at 2011-08-13 20:53:03

Replying to [comment:67 leif]:
> I'd prefer `sage-doctest`'s PID, appended (separated by an underscore) as [comment:62 above].

Do we also need to add this PID to the output from `filename_mangler`, in case someone is doctesting the same file in the Sage library several times simultaneously?

Regarding the timing files: I'm not touching that code, although I've added some comments.

Regarding deleting files on interruption: it's not clear how to easily determine whether there was an error before the interruption — do you need to use `post_process`? — so I'm just adding some comments and not touching the code.


---

Attachment

scripts repo


---

Comment by leif created at 2011-08-14 01:25:15

Replying to [comment:68 jhpalmieri]:
> Replying to [comment:67 leif]:
> > I'd prefer `sage-doctest`'s PID, appended (separated by an underscore) as [comment:62 above].
> 
> Do we also need to add this PID to the output from `filename_mangler`, in case someone is doctesting the same file in the Sage library several times simultaneously?

Yes; you apparently already did so in the new patch.

But we actually don't have to mangle any path into the filename if we do that, since every file is tested by its own `sage-doctest` instance, in a directory unique to the host and the `sage-ptest` instance. [We'd have to do the same for `sage-test`, i.e., also create a unique directory there, perhaps on a follow-up, to also support simultaneous _sequential_ testing on _different_ hosts which share the same `$SAGE_TESTDIR` (from the perspective of `sage-[p]test`).]




> Regarding the timing files: I'm not touching that code, although I've added some comments.

Ok.




> Regarding deleting files on interruption: it's not clear how to easily determine whether there was an error before the interruption — do you need to use `post_process`? — so I'm just adding some comments and not touching the code.

Ok. I actually didn't think about doctest errors _in the same file_ that may have occurred prior to interruption; it would IMHO be ok to just "discard" them, but we can decide on that on the corresponding follow-up.


---

Comment by leif created at 2011-08-14 01:39:29

P.S.: For future changes, could we do some versioning with the patch(es)?

I meanwhile have a handful of tabs with different versions of the attached one and different deltas, losing track... ;-)


---

Comment by jhpalmieri created at 2011-08-15 16:20:14

What still needs to be done here?

Replying to [comment:70 leif]:
> Replying to [comment:68 jhpalmieri]:
> > Replying to [comment:67 leif]:
> > > I'd prefer `sage-doctest`'s PID, appended (separated by an underscore) as [comment:62 above].
> > 
> > Do we also need to add this PID to the output from `filename_mangler`, in case someone is doctesting the same file in the Sage library several times simultaneously?
> 
> Yes; you apparently already did so in the new patch.
> 
> But we actually don't have to mangle any path into the filename if we do that, since every file is tested by its own `sage-doctest` instance, in a directory unique to the host and the `sage-ptest` instance.

I can remove the pathname from the mangling. If we're just adding the pid, I may discard the function `filename_mangler` and deal with it like this:

```diff
-        f = os.path.splitext(filename_mangler(file))[0] + '.py'
+        f = os.path.join(SAGE_TESTDIR, "doctest_%s_%s.py" % (os.getpid(), name))
```

`filename_mangler` only gets used in this one place anyway.

> > Regarding deleting files on interruption: it's not clear how to easily determine whether there was an error before the interruption — do you need to use `post_process`? — so I'm just adding some comments and not touching the code.
> 
> Ok. I actually didn't think about doctest errors _in the same file_ that may have occurred prior to interruption; it would IMHO be ok to just "discard" them, but we can decide on that on the corresponding follow-up.

Well, some library files can take a long time to doctest, so I can imagine someone doctesting a file, seeing that it fails and then interrupting it, but wanting to keep the temporary file for some reason.  (As I said, I'm not planning on modifying this code anyway.)


---

Comment by leif created at 2011-09-10 18:28:14

Because, as mentioned, it currently can happen that doctests for a file `.../bar/foo` are reported to have passed successfully though actually `.../baz/foo` was tested.

Afterwards rerunning (just) the tests for `.../baz/foo` (which in contrast were reported to have failed) won't show any errors, hiding possible doctest errors in `.../bar/foo`.


---

Comment by leif created at 2011-09-10 18:28:14

Changing priority from critical to blocker.


---

Comment by leif created at 2011-09-10 18:52:57

Replying to [comment:72 jhpalmieri]:
> What still needs to be done here? 

> 

> Replying to [comment:70 leif]:
> > Replying to [comment:68 jhpalmieri]:
> > > Replying to [comment:67 leif]:
> > > > I'd prefer `sage-doctest`'s PID, appended (separated by an underscore) as [comment:62 above].
> I can remove the pathname from the mangling. If we're just adding the pid, I may discard the function `filename_mangler` and deal with it like this:

```diff
-        f = os.path.splitext(filename_mangler(file))[0] + '.py'
+        f = os.path.join(SAGE_TESTDIR, "doctest_%s_%s.py" % (os.getpid(), name))
```


I'd prefer having the name first, then the PID; then we can also drop the `doctest_` prefix (because e.g. `1_module` is not a valid Python module name).

I think this way it's easier to locate a file (with `ls` or some file manager), since the files will be in alphabetical order, sorted by their original name (as opposed to some random PIDs).


---

Comment by jhpalmieri created at 2011-09-10 20:59:38

Here are some new patches.  First, [attachment:trac_9739.v2.patch] and a "delta" patch [attachment:trac_9739-delta1to2.patch]: the differences from the previous version are

 - It changes how filenames are mangled: it uses "NAME_PID.py" instead of "doctest_PID_NAME.py" or whatever what there before.

 - I've decided that I agree with you: we shouldn't print the messages about removing the doctesting directory every time.  I've changed it so it only prints them if "-verbose" is one of the command-line options.  (This is overusing the "-verbose" option, I suppose, so we could instead could completely disable printing just by setting the variable "verbose" in sage-ptest to be False always.)  If the directory is not deleted at the end, then a message is printed regardless of verbosity settings.

Along these lines, we have [attachment:trac_9739-graphviz.patch], a patch for the main Sage library, which writes a temporary file to SAGE_TMP rather than to SAGE_TESTDIR, so that the doctesting directory is indeed empty after doctesting the Sage library.


---

Attachment

for review only


---

Comment by jhpalmieri created at 2011-09-10 21:00:20

main Sage library repo


---

Attachment

Replying to [comment:75 jhpalmieri]:
> Along these lines, we have [attachment:trac_9739-graphviz.patch], a patch for the main Sage library, which writes a temporary file to SAGE_TMP rather than to SAGE_TESTDIR, so that the doctesting directory is indeed empty after doctesting the Sage library.

Shouldn't doctests delete the files they create afterwards anyway?


---

Comment by leif created at 2011-09-10 23:14:16

Some minor things:

 * `"%s" % os.getpid()` works, but in principle it should use `"%d"`.
 * I think we should also (already) support the proper long option format, `--verbose`, there.
 * I would omit the "_Warning:_" in case (we know that) doctest errors occurred, since it is the desired behaviour to keep at least the failing files in that case. 

   We _could_ also list the contents of the directory there ("_The following files have been kept [because of doctest errors]: ..._"). (In principle we also would have to relate them back to their original files, to remove the ambiguity this ticket is all about.)


---

Comment by jhpalmieri created at 2011-09-10 23:31:11

> Shouldn't doctests delete the files they create afterwards anyway?

Examples in Sage code can create files anywhere in the filesystem, but they _should_ only create temporary files or delete files after they're finished with them.  The directory SAGE_TMP gets cleaned up automatically, so it's a good choice, as opposed to SAGE_TESTDIR.

Replying to [comment:77 leif]:
> Some minor things:
> 
>  * `"%s" % os.getpid()` works, but in principle it should use `"%d"`.

Okay. We seem to have used "%d" elsewhere in the file, not sure why I didn't this time.

>  * I think we should also (already) support the proper long option format, `--verbose`, there.

Oh, right, I misunderstood `opts`: I thought it was just the string of options instead of a list.

>  * I would omit the "_Warning:_" in case (we know that) doctest errors occurred, since it is the desired behaviour to keep at least the failing files in that case. 


Okay.

>    We _could_ also list the contents of the directory there ("_The following files have been kept [because of doctest errors]: ..._"). (In principle we also would have to relate them back to their original files, to remove the ambiguity this ticket is all about.)

Looks like an enhancement for another ticket.

I don't think it's worth making a "v3" patch out of this.  Here's the difference between the previous v2 patch and this one:

```diff
diff --git a/sage-doctest b/sage-doctest
--- a/sage-doctest
+++ b/sage-doctest
@@ -644,7 +644,7 @@ def test_file(file, library_code):
 
         name = os.path.basename(file)
         name = name[:name.find(".")]
-        f = os.path.join(SAGE_TESTDIR, "%s_%s.py" % (name, os.getpid()))
+        f = os.path.join(SAGE_TESTDIR, "%s_%d.py" % (name, os.getpid()))
 
         open(f,"w").write(s)
         tmpfiles.append(f)
diff --git a/sage-ptest b/sage-ptest
--- a/sage-ptest
+++ b/sage-ptest
@@ -295,7 +295,7 @@ for gr in range(0,numglobaliteration):
 
         infiles.append(os.path.join(sagenb_loc, 'sagenb'))
 
-    verbose = '-verbose' in opts
+    verbose = ('-verbose' in opts or '--verbose' in opts)
 
     if numthreads == 0:
         # Set numthreads to be the number of processors, with a default
@@ -430,7 +430,7 @@ for gr in range(0,numglobaliteration):
         # TODO (probably in sage-doctest): if tests were interrupted
         # but there were no failures in the interrupted files, delete
         # the temporary files, so that this directory is empty.
-        print "Warning: the temporary doctesting directory"
+        print "The temporary doctesting directory"
         print "   %s" % TMP
         print "was not removed: it is not empty, probably because doctesting"
         print "failed or was interrupted."
```



---

Attachment

scripts repo


---

Comment by leif created at 2011-09-10 23:43:59

Replying to [comment:78 jhpalmieri]:
> >    We _could_ also list the contents of the directory there ("_The following files have been kept [because of doctest errors]: ..._"). (In principle we also would have to relate them back to their original files, to remove the ambiguity this ticket is all about.)
> 
> Looks like an enhancement for another ticket.

Ok. Just in case you were bored... Btw, it wouldn't be bad to put the full path of the original file into a comment of the generated doctest file either.

> I don't think it's worth making a "v3" patch out of this.  Here's the difference between the previous v2 patch and this one ...

Ok.


---

Comment by leif created at 2011-09-10 23:49:27

... although I'd say
  _"... *presumably* because doctest*s* failed or *doctesting* was interrupted"_.


---

Comment by jhpalmieri created at 2011-09-11 01:14:26

Okay, here is a v3 patch with cumulative changes from the original v2 patch in the corresponding delta patch; thus you can get from the original patch to the v3 patch by applying the two delta patches.

I added the path of the original file to the doctest file, but did nothing about listing files in the directory.  (It should be clear from other messages what the files are -- they should correspond to doctest failures -- and people can also just `ls` the directory.  The current message is there just to alert people to the fact that their `.sage` directory (by default) is possibly being polluted with some things which could be cleaned up if desired, so just printing the directory name is good enough.)


---

Attachment

for review only


---

Comment by jhpalmieri created at 2011-09-11 01:15:26

scripts repo


---

Attachment


---

Comment by leif created at 2011-09-11 01:25:39

I think we should create the same temporary directory (`$SAGE_TESTDIR/$hostname-$pid`) in `sage-test` as well (on this ticket), and export this in `SAGE_TESTDIR` for `sage-doctest`.

Also wouldn't be bad to put such common code into a separate module, before we "unify" (or unite) `sage-test` and `sage-ptest`.


---

Comment by leif created at 2011-09-11 01:51:50

Sorry, missed your updates. Now I can't provide a reviewer patch... :)

Wonderful:

```
/tmp/leif/home/.sage/tmp/redhawk-16925:
total 300
-rw-r--r-- 1 leif leif  2398 2011-09-10 18:45 algebra_18699.py
-rw-r--r-- 1 leif leif  2422 2011-09-10 18:45 algebras_18570.py
-rw-r--r-- 1 leif leif  2441 2011-09-10 18:45 arithgroup_18497.py
-rw-r--r-- 1 leif leif 14054 2011-09-10 18:45 branching_rules_17653.py
-rw-r--r-- 1 leif leif  2052 2011-09-10 18:45 cmd_18353.py
-rw-r--r-- 1 leif leif 14762 2011-09-10 18:45 coercion_18657.py
-rw-r--r-- 1 leif leif  2454 2011-09-10 18:45 crystals_18792.py
-rw-r--r-- 1 leif leif  2231 2011-09-10 18:45 databases_18494.py
-rw-r--r-- 1 leif leif  2200 2011-09-10 18:45 designs_18697.py
-rw-r--r-- 1 leif leif  2352 2011-09-10 18:45 developer_18793.py
-rw-r--r-- 1 leif leif  2301 2011-09-10 18:45 functions_18457.py
-rw-r--r-- 1 leif leif 25616 2011-09-10 18:45 group_theory_17619.py
-rw-r--r-- 1 leif leif  2320 2011-09-10 18:45 hecke_18619.py
-rw-r--r-- 1 leif leif  2422 2011-09-10 18:45 homology_18513.py
-rw-r--r-- 1 leif leif  2252 2011-09-10 18:45 iet_18686.py

-rw-r--r-- 1 leif leif  6279 2011-09-10 18:45 index_17344.py
-rw-r--r-- 1 leif leif  3478 2011-09-10 18:45 index_18779.py

-rw-r--r-- 1 leif leif  3556 2011-09-10 18:45 kazhdan_lusztig_polynomials_17696.py
-rw-r--r-- 1 leif leif  2425 2011-09-10 18:45 modabvar_18649.py
-rw-r--r-- 1 leif leif  2498 2011-09-10 18:45 modsym_18633.py
-rw-r--r-- 1 leif leif  2075 2011-09-10 18:45 networking_18398.py
-rw-r--r-- 1 leif leif  2130 2011-09-10 18:45 numerical_18660.py
-rw-r--r-- 1 leif leif  3142 2011-09-10 18:45 padics_18685.py
-rw-r--r-- 1 leif leif  2182 2011-09-10 18:45 parallel_18621.py
-rw-r--r-- 1 leif leif  2444 2011-09-10 18:45 plot3d_18453.py
-rw-r--r-- 1 leif leif  2391 2011-09-10 18:45 polynomial_rings_18651.py
-rw-r--r-- 1 leif leif  2301 2011-09-10 18:45 polynomial_rings_infinite_18371.py
-rw-r--r-- 1 leif leif  2784 2011-09-10 18:45 polynomial_rings_univar_18551.py
-rw-r--r-- 1 leif leif  2259 2011-09-10 18:45 posets_18828.py
-rw-r--r-- 1 leif leif  2324 2011-09-10 18:45 power_series_18638.py
-rw-r--r-- 1 leif leif  2127 2011-09-10 18:45 probability_18369.py
-rw-r--r-- 1 leif leif  2303 2011-09-10 18:45 quadratic_forms_18675.py
-rw-r--r-- 1 leif leif  2159 2011-09-10 18:45 quat_algebras_18571.py
-rw-r--r-- 1 leif leif  2413 2011-09-10 18:45 root_systems_18706.py
-rw-r--r-- 1 leif leif  2100 2011-09-10 18:45 semirings_18493.py
-rw-r--r-- 1 leif leif  2146 2011-09-10 18:45 species_18786.py
-rw-r--r-- 1 leif leif  2179 2011-09-10 18:45 stats_18647.py
-rw-r--r-- 1 leif leif  2668 2011-09-10 18:45 symmetric_functions_18691.py
-rw-r--r-- 1 leif leif  2201 2011-09-10 18:45 tableaux_18773.py
-rw-r--r-- 1 leif leif  2025 2011-09-10 18:45 todolist_18572.py
-rw-r--r-- 1 leif leif 20114 2011-09-10 18:45 tour_advanced_17551.py
-rw-r--r-- 1 leif leif  6039 2011-09-10 18:45 tour_groups_17418.py

-rw-r--r-- 1 leif leif 11469 2011-09-10 18:44 tour_plotting_17181.py
-rw-r--r-- 1 leif leif 11468 2011-09-10 18:45 tour_plotting_17372.py

-rw-r--r-- 1 leif leif 17816 2011-09-10 18:45 weyl_character_ring_17672.py
-rw-r--r-- 1 leif leif 10807 2011-09-10 18:45 weyl_groups_17663.py
-rw-r--r-- 1 leif leif  2522 2011-09-10 18:45 words_18739.py
```

(Blank lines inserted.)


---

Comment by jhpalmieri created at 2011-09-11 17:34:00

Replying to [comment:83 leif]:
> I think we should create the same temporary directory (`$SAGE_TESTDIR/$hostname-$pid`) in `sage-test` as well (on this ticket), and export this in `SAGE_TESTDIR` for `sage-doctest`.
> 
> Also wouldn't be bad to put such common code into a separate module, before we "unify" (or unite) `sage-test` and `sage-ptest`.

These both sound like issues for #9224, not here.  I really don't want to add any more to this ticket unless there is an extremely good reason to do so.


---

Comment by leif created at 2011-09-11 19:27:01

Sorry for the delay.

I started testing the v2 yesterday, also with `make testlong`, which took ages, the latter unfortunately right before you made the v3, and later made a mistake when wanting to test v3, retesting v2 again... 8/

I've now also tested v3, with both sequential doctests (since we've modified `sage-doctest`, but not yet `sage-test`, except for a comment), and parallel tests with up to 128 threads.

I've reviewed the code already, so I can -- hopefully finally -- give this a *positive review*. (At least until something unexpected happens; I must admit I haven't tested the latest versions with non-library code yet.)

Thanks for spending so much time on this.




Replying to [comment:85 jhpalmieri]:
> Replying to [comment:83 leif]:
> > I think we should create the same temporary directory (`$SAGE_TESTDIR/$hostname-$pid`) in `sage-test` as well (on this ticket), and export this in `SAGE_TESTDIR` for `sage-doctest`.
> > 
> > Also wouldn't be bad to put such common code into a separate module, before we "unify" (or unite) `sage-test` and `sage-ptest`.
> 
> These both sound like issues for #9224, not here.

Well, Dave wanted this (the former), at least when we started here last year... ;-)

I've added a comment there w.r.t. also using unique directories when testing sequentially, since there might be multiple instances running at the same time.




> I really don't want to add any more to this ticket unless there is an extremely good reason to do so.

Ok, agreed. This ticket has really been dragging enough.




By the way, you were right; `opts` is a _string_ (of the concatenated options) there, as opposed to a list of strings, so `"-verbose" in opts` would have been enough. But it works this way, too, and is IMHO nothing worth fixing again _here_.

Also, or on the other hand, I don't think anybody will ever use `--verbose` when doctesting in parallel, since the output would be totally messed up, unless one uses `sage -tp 1 ...` (or `make NUM_THREADS=1 ...`, which is also useful in some cases.


---

Comment by leif created at 2011-09-11 19:27:01

Changing keywords from "doctest scripts" to "doctest scripts race condition unique filenames ptestlong -tp".


---

Comment by leif created at 2011-09-11 19:27:01

Changing status from needs_review to positive_review.


---

Comment by leif created at 2011-09-12 18:00:27

Resolution: fixed


---

Comment by jhpalmieri created at 2011-09-28 00:34:00

Here's an add-on patch to fix the issues mentioned at #8708: testing non-library .py files is broken in two ways.


---

Comment by leif created at 2011-09-28 00:55:51

Could you reupload it with a matching commit message? ;-)


---

Comment by jhpalmieri created at 2011-09-28 01:23:50

I knew we weren't really done with this ticket...


---

Comment by leif created at 2011-09-28 01:29:05

I've attached your patch with a corrected commit message 6 seconds before you did. :D

Deleting it again; thanks.




I thought we were done, but it will break again as soon as others start to mess with how files are preparsed or their names...


---

Comment by jhpalmieri created at 2011-10-03 19:44:26

Should the extra patch be put on a new ticket to make sure it gets reviewed and/or merged in the next alpha?  I'm a little concerned that it will get lost since it was attached to an already closed-and-merged ticket.


---

Comment by jdemeyer created at 2011-10-03 19:49:10

Replying to [comment:93 jhpalmieri]:
> Should the extra patch be put on a new ticket
Absolutely, see #11893.  I deleted the patch here to remove confusion.


---

Comment by jdemeyer created at 2011-10-03 19:50:39

Can somebody please review John's patch at #11893?


---

Comment by leif created at 2011-10-03 20:16:43

Replying to [comment:94 jdemeyer]:
> Replying to [comment:93 jhpalmieri]:
> > Should the extra patch be put on a new ticket
> Absolutely, see #11893.  I deleted the patch here to remove confusion.

Please reattach it; it is already merged!


---

Comment by leif created at 2011-10-03 20:27:44

Replying to [comment:97 leif]:
> Replying to [comment:94 jdemeyer]:
> > Replying to [comment:93 jhpalmieri]:
> > > Should the extra patch be put on a new ticket
> > Absolutely, see #11893.  I deleted the patch here to remove confusion.
> 
> Please reattach it; it is already merged!

See http://trac.sagemath.org/sage_trac/ticket/8708#comment:14 ff. for part of the discussion.


---

Comment by jhpalmieri created at 2011-10-03 20:30:07

It wasn't clear from this ticket that the patch had been merged: it was marked as merged and closed before the patch was attached, and I didn't check the actual log to see if it had been merged.  Sorry.


---

Comment by jhpalmieri created at 2011-10-03 20:31:17

scripts repo; apply on top of other patch


---

Attachment

Replying to [comment:99 jhpalmieri]:
> It wasn't clear from this ticket that the patch had been merged: it was marked as merged and closed before the patch was attached, and I didn't check the actual log to see if it had been merged.  Sorry.

Well, I could have added a clarifying comment, although I thought it was clear from the context that it is indeed merged; otherwise I would have reopened the ticket or moved the patch to another one.


---

Comment by jdemeyer created at 2011-10-04 07:02:45

Sorry for the mess here, I jumped too quickly.  Unfortunately, my attempt to avoid confusion only created confusion.

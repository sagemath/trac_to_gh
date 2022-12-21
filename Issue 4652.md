# Issue 4652: [with code, needs testing] make distutils compile Cython extensions in parallel

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-11-29 11:37:40

Assignee: craigcitro

Currently, we've got excellent code to run Cython in parallel as part of the Sage build process. However, once we ask distutils to begin compiling that code, everything is done in serial, because distutils works solely in serial. 

## The Code

The attached file changes that. This (somewhat brutally) hacks distutils to dispatch the calls to build C/C++ extensions in parallel, using pyprocessing. (I totally jacked William's code from #3765 for this.) Here's how to put this code in place:

  * download the attached file (`build_ext.py`)
  * replace `$SAGE_ROOT/local/lib/python2.5/distutils/command/build_ext.py` with the new version.
  
Now, if you want to test the new code, do the following:

  * set the environment variable `SAGE_PARALLEL_DIST` to something. (The code just checks to see if the variable is defined at all.)
  * set the environment variable `MAKE` to `MAKE -j2`, where `2` is replaced by the number of simultaneous build processes you want. 
  * build.

## Notes

If you want to test this, don't go around touching the `.pyx` files in the Sage library, since Cython is much slower than `gcc`. Instead, simply go around touching the `.c` and `.cpp` files in `$SAGE_ROOT/devel/sage/sage`. One of the cool features we added with the new build system is that these files get recompiled when they change.

There is now a line that prints as part of the build process that looks like:

```
Total time spent compiling C/C++ extensions:  5.2876701355 seconds.
```

So try touching a bunch of files in the Sage library, and seeing what kind of speedups you get.

There are two caveats I want to offer with this code: 

 * Michael points out that numpy does a lot with distutils. I could very well have broken their use of distutils.
 * I don't do anything involving dependency tracking between extensions. In particular, if there are extensions that have to be built in a certain order, this code could break it. (This code still compiles all source files *within* an extension in the usual way.) Neither Michael nor I could think of a situation where this would break anything in Sage, but who knows ...

## The Plan

So while this code is cool, and will definitely save a ton of CPU time on `sage.math` (*cough* mabshoff *cough*), the plan is *not* to maintain it as a part of the Sage Python spkg indefinitely. Instead, if it seems to work well, then we should try to clean this code up a bit more and upstream it, since pyprocessing is standard in Python 2.6.


---

Attachment

Just out of curiosity, did you try to get this to work without modifying build_ext.py at all, but by simply changing stuff in that module at runtime, like I illustrate in #3765?

Here's the diff of what you did:

```
--- build_ext.py.orig	2008-11-29 10:32:57.000000000 -0800
+++ build_ext.py	2008-11-29 03:38:35.000000000 -0800
`@``@` -409,13 +409,57 `@``@`
     # get_outputs ()
 
     def build_extensions(self):
+
         # First, sanity-check the 'extensions' list
         self.check_extensions_list(self.extensions)
 
-        for ext in self.extensions:
-            self.build_extension(ext)
+        if not os.environ.has_key('MAKE'):
+            ncpus = 1
+        else:
+            MAKE = os.environ['MAKE']
+            z = [w[2:] for w in MAKE.split() if w.startswith('-j')]
+            if len(z) == 0:  # no command line option
+                ncpus = 1
+            else:
+                # Determine number of cpus from command line argument.
+                # Also, use the OS to cap the number of cpus, in case
+                # user annoyingly makes a typo and asks to use 10000
+                # cpus at once.
+                try:
+                    ncpus = int(z[0])
+                    n = 2*number_of_cpus()
+                    if n:  # prevent dumb typos.
+                        ncpus = min(ncpus, n)
+                except ValueError:
+                    ncpus = 1
+
+        import time
+        t = time.time()
+        
+        # See if we're trying out the experimental parallel build
+        # code.
+        if ncpus > 1 and os.environ.has_key('SAGE_PARALLEL_DIST'):
+            extensions_to_compile = []
+            for ext in self.extensions:
+                need_to_compile, p = self.prepare_extension(ext)
+                if need_to_compile:
+                    extensions_to_compile.append(p)
+
+            if extensions_to_compile:
+               from processing import Pool
+               p = Pool(min(ncpus, len(extensions_to_compile)))
+               for r in p.imap(self.build_extension, extensions_to_compile):
+                   pass
+            
+        else:
+            for ext in self.extensions:
+                need_to_compile, p = self.prepare_extension(ext)
+                if need_to_compile:
+                    self.build_extension(p)
+
+        print "Total time spent compiling C/C++ extensions: ", time.time() - t, "seconds."
 
-    def build_extension(self, ext):
+    def prepare_extension(self, ext):
         sources = ext.sources
         if sources is None or type(sources) not in (ListType, TupleType):
             raise DistutilsSetupError, \
`@``@` -443,9 +487,16 `@``@`
         depends = sources + ext.depends
         if not (self.force or newer_group(depends, ext_filename, 'newer')):
             log.debug("skipping '%s' extension (up-to-date)", ext.name)
-            return
+            need_to_compile = False
         else:
             log.info("building '%s' extension", ext.name)
+            need_to_compile = True
+
+        return need_to_compile, (sources, ext, ext_filename)
+
+    def build_extension(self, p):
+
+        sources, ext, ext_filename = p
 
         # First, scan the sources for SWIG definition files (.i), run
         # SWIG on 'em to create .c files, and modify the sources list
`@``@` -715,3 +766,23 `@``@`
                 return ext.libraries
 
 # class build_ext
+
+
+
+def number_of_cpus():
+    """
+    Try to determine the number of cpu's on this system.
+    If successful return that number.  Otherwise return 0
+    to indicate failure.
+
+    OUTPUT:
+        int
+    """
+    if hasattr(os, "sysconf") and os.sysconf_names.has_key("SC_NPROCESSORS_ONLN"): # Linux and Unix
+        n = os.sysconf("SC_NPROCESSORS_ONLN")
+        if isinstance(n, int) and n > 0:
+            return n
+    try:
+        return int(os.popen2("sysctl -n hw.ncpu")[1].read().strip())
+    except:
+        return 0
```



---

Comment by was created at 2008-11-30 08:05:28

POSITIVE TESTING: I just want to comment that I used this a *lot* all day today on both OS X and Linux, and didn't have a single problem.  I like it!


---

Comment by ncalexan created at 2008-12-09 19:05:24

This has been in my tree for more than a week on a Mac OS X 10.5 machine.  I have been doing some fairly heavy development, although most has not been in Cython.  No problems to report; I say merge.


```
sage: version()
'Sage Version 3.2.1.alpha2, Release Date: 2008-11-26'
```



---

Comment by mabshoff created at 2008-12-11 10:26:03

There is a slight chicken and egg problem here since we build pyprocessing after python, so if someone sets the wrong environment variable the build of Python itself will blow up.

To fix this:

 * make sure to unset SAGE_PARALLEL_DIST for the python.spkg as well as the pyprocessing.spkg
 * make all the other python based spkgs depend on pyprocessing, so it is immediately build after Python

Then this should work out of the box, even though we should still test this with a couple rounds of builds of Sage with a high parallel level to make sure we do not hit any race conditions.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-13 10:54:03

After some chit chat with Craig we agreed that this should go into the enf of the pyprocessing spkg-install. That way everything is in place even for a fresh build.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-13 11:50:45

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.2/alpha2/pyprocessing-0.52.p0.spkg

contains the fix. I tested it in various configs and it works for me :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-13 11:50:45

Resolution: fixed


---

Comment by mabshoff created at 2008-12-13 18:01:41

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-12-13 18:01:41

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-12-13 18:01:41

This breaks at least the numpy and scipy build, so I am reverting for now.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-13 18:11:12

Some more info: even unsetting SAGE_PARALLEL_DIST does not fix the problem, bot numpy and scipy fail in different work. So while this is useful when merging patches it breaks too easily on -upgrade or a build from scratch.

Cheers,

Michael


---

Attachment


---

Comment by craigcitro created at 2009-06-05 08:08:39

Ok, new version of the code is up. This is done differently than last time; rather than patch our python, I'm simply inserting the code in our `setup.py`, and calling distutils with the new code *only* from Sage. 

So, to test this, do the following:

 * download and apply trac-4652-testing.patch
 * set the env variable `SAGE_PARALLEL_DIST` to anything
 * set the env variable `MAKE` to something like `make -j168` (where 168 is the number of simultaneous threads you want)
 * `sage -br` or `sage -ba`

If this seems to work for people, then we can try building Sage from scratch with it. (I'm going to try setting my machine to do that overnight with `4.0.1.rc2`, I think.) If it works fine, I just want to add a little bit of documentation and then I'm happy to have this merged. If it works for a release or so, I'll start working on getting *something* like this upstream. (I have no idea how uphill that battle will be.)


---

Comment by craigcitro created at 2009-06-05 16:23:35

Okay, I ran a build from scratch with this in place, and it worked fine. In particular, it doesn't cause scipy or numpy to fail at building, which was the goal.

So I'm curious what other people say -- if everyone spoke up real fast, should we try to push this into 4.0.1? (I know several developers have been clamoring for it.)


---

Comment by ncalexan created at 2009-06-05 16:29:01

I have certainly been clamoring but I'd really like to see this go through an alpha revision and get tested on multiple platforms before we ship it.  Thanks for doing this, Craig!


---

Comment by mhansen created at 2009-06-06 00:10:28

I've merged trac-4652-testing.patch in 4.0.1.rc3.


---

Comment by craigcitro created at 2009-06-12 07:02:16

Resolution: fixed

# Issue 4652: [with code, needs testing] make distutils compile Cython extensions in parallel

archive/issues_004652.json:
```json
{
    "body": "Assignee: craigcitro\n\nCurrently, we've got excellent code to run Cython in parallel as part of the Sage build process. However, once we ask distutils to begin compiling that code, everything is done in serial, because distutils works solely in serial. \n\n## The Code\n\nThe attached file changes that. This (somewhat brutally) hacks distutils to dispatch the calls to build C/C++ extensions in parallel, using pyprocessing. (I totally jacked William's code from #3765 for this.) Here's how to put this code in place:\n\n* download the attached file (`build_ext.py`)\n* replace `$SAGE_ROOT/local/lib/python2.5/distutils/command/build_ext.py` with the new version.\n  \nNow, if you want to test the new code, do the following:\n\n* set the environment variable `SAGE_PARALLEL_DIST` to something. (The code just checks to see if the variable is defined at all.)\n* set the environment variable `MAKE` to `MAKE -j2`, where `2` is replaced by the number of simultaneous build processes you want. \n* build.\n\n## Notes\n\nIf you want to test this, don't go around touching the `.pyx` files in the Sage library, since Cython is much slower than `gcc`. Instead, simply go around touching the `.c` and `.cpp` files in `$SAGE_ROOT/devel/sage/sage`. One of the cool features we added with the new build system is that these files get recompiled when they change.\n\nThere is now a line that prints as part of the build process that looks like:\n\n```\nTotal time spent compiling C/C++ extensions:  5.2876701355 seconds.\n```\n\nSo try touching a bunch of files in the Sage library, and seeing what kind of speedups you get.\n\nThere are two caveats I want to offer with this code: \n\n* Michael points out that numpy does a lot with distutils. I could very well have broken their use of distutils.\n* I don't do anything involving dependency tracking between extensions. In particular, if there are extensions that have to be built in a certain order, this code could break it. (This code still compiles all source files **within** an extension in the usual way.) Neither Michael nor I could think of a situation where this would break anything in Sage, but who knows ...\n\n## The Plan\n\nSo while this code is cool, and will definitely save a ton of CPU time on `sage.math` (**cough** mabshoff **cough**), the plan is **not** to maintain it as a part of the Sage Python spkg indefinitely. Instead, if it seems to work well, then we should try to clean this code up a bit more and upstream it, since pyprocessing is standard in Python 2.6.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4652\n\n",
    "created_at": "2008-11-29T11:37:40Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with code, needs testing] make distutils compile Cython extensions in parallel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4652",
    "user": "craigcitro"
}
```
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
* I don't do anything involving dependency tracking between extensions. In particular, if there are extensions that have to be built in a certain order, this code could break it. (This code still compiles all source files **within** an extension in the usual way.) Neither Michael nor I could think of a situation where this would break anything in Sage, but who knows ...

## The Plan

So while this code is cool, and will definitely save a ton of CPU time on `sage.math` (**cough** mabshoff **cough**), the plan is **not** to maintain it as a part of the Sage Python spkg indefinitely. Instead, if it seems to work well, then we should try to clean this code up a bit more and upstream it, since pyprocessing is standard in Python 2.6.

Issue created by migration from https://trac.sagemath.org/ticket/4652





---

archive/issue_comments_035008.json:
```json
{
    "body": "Attachment [build_ext.py](tarball://root/attachments/some-uuid/ticket4652/build_ext.py) by was created at 2008-11-29 18:37:59\n\nJust out of curiosity, did you try to get this to work without modifying build_ext.py at all, but by simply changing stuff in that module at runtime, like I illustrate in #3765?\n\nHere's the diff of what you did:\n\n```\n--- build_ext.py.orig\t2008-11-29 10:32:57.000000000 -0800\n+++ build_ext.py\t2008-11-29 03:38:35.000000000 -0800\n@@ -409,13 +409,57 @@\n     # get_outputs ()\n \n     def build_extensions(self):\n+\n         # First, sanity-check the 'extensions' list\n         self.check_extensions_list(self.extensions)\n \n-        for ext in self.extensions:\n-            self.build_extension(ext)\n+        if not os.environ.has_key('MAKE'):\n+            ncpus = 1\n+        else:\n+            MAKE = os.environ['MAKE']\n+            z = [w[2:] for w in MAKE.split() if w.startswith('-j')]\n+            if len(z) == 0:  # no command line option\n+                ncpus = 1\n+            else:\n+                # Determine number of cpus from command line argument.\n+                # Also, use the OS to cap the number of cpus, in case\n+                # user annoyingly makes a typo and asks to use 10000\n+                # cpus at once.\n+                try:\n+                    ncpus = int(z[0])\n+                    n = 2*number_of_cpus()\n+                    if n:  # prevent dumb typos.\n+                        ncpus = min(ncpus, n)\n+                except ValueError:\n+                    ncpus = 1\n+\n+        import time\n+        t = time.time()\n+        \n+        # See if we're trying out the experimental parallel build\n+        # code.\n+        if ncpus > 1 and os.environ.has_key('SAGE_PARALLEL_DIST'):\n+            extensions_to_compile = []\n+            for ext in self.extensions:\n+                need_to_compile, p = self.prepare_extension(ext)\n+                if need_to_compile:\n+                    extensions_to_compile.append(p)\n+\n+            if extensions_to_compile:\n+               from processing import Pool\n+               p = Pool(min(ncpus, len(extensions_to_compile)))\n+               for r in p.imap(self.build_extension, extensions_to_compile):\n+                   pass\n+            \n+        else:\n+            for ext in self.extensions:\n+                need_to_compile, p = self.prepare_extension(ext)\n+                if need_to_compile:\n+                    self.build_extension(p)\n+\n+        print \"Total time spent compiling C/C++ extensions: \", time.time() - t, \"seconds.\"\n \n-    def build_extension(self, ext):\n+    def prepare_extension(self, ext):\n         sources = ext.sources\n         if sources is None or type(sources) not in (ListType, TupleType):\n             raise DistutilsSetupError, \\\n@@ -443,9 +487,16 @@\n         depends = sources + ext.depends\n         if not (self.force or newer_group(depends, ext_filename, 'newer')):\n             log.debug(\"skipping '%s' extension (up-to-date)\", ext.name)\n-            return\n+            need_to_compile = False\n         else:\n             log.info(\"building '%s' extension\", ext.name)\n+            need_to_compile = True\n+\n+        return need_to_compile, (sources, ext, ext_filename)\n+\n+    def build_extension(self, p):\n+\n+        sources, ext, ext_filename = p\n \n         # First, scan the sources for SWIG definition files (.i), run\n         # SWIG on 'em to create .c files, and modify the sources list\n@@ -715,3 +766,23 @@\n                 return ext.libraries\n \n # class build_ext\n+\n+\n+\n+def number_of_cpus():\n+    \"\"\"\n+    Try to determine the number of cpu's on this system.\n+    If successful return that number.  Otherwise return 0\n+    to indicate failure.\n+\n+    OUTPUT:\n+        int\n+    \"\"\"\n+    if hasattr(os, \"sysconf\") and os.sysconf_names.has_key(\"SC_NPROCESSORS_ONLN\"): # Linux and Unix\n+        n = os.sysconf(\"SC_NPROCESSORS_ONLN\")\n+        if isinstance(n, int) and n > 0:\n+            return n\n+    try:\n+        return int(os.popen2(\"sysctl -n hw.ncpu\")[1].read().strip())\n+    except:\n+        return 0\n```\n",
    "created_at": "2008-11-29T18:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4652#issuecomment-35008",
    "user": "was"
}
```

Attachment [build_ext.py](tarball://root/attachments/some-uuid/ticket4652/build_ext.py) by was created at 2008-11-29 18:37:59

Just out of curiosity, did you try to get this to work without modifying build_ext.py at all, but by simply changing stuff in that module at runtime, like I illustrate in #3765?

Here's the diff of what you did:

```
--- build_ext.py.orig	2008-11-29 10:32:57.000000000 -0800
+++ build_ext.py	2008-11-29 03:38:35.000000000 -0800
@@ -409,13 +409,57 @@
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
@@ -443,9 +487,16 @@
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
@@ -715,3 +766,23 @@
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

archive/issue_comments_035009.json:
```json
{
    "body": "POSITIVE TESTING: I just want to comment that I used this a *lot* all day today on both OS X and Linux, and didn't have a single problem.  I like it!",
    "created_at": "2008-11-30T08:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4652#issuecomment-35009",
    "user": "was"
}
```

POSITIVE TESTING: I just want to comment that I used this a *lot* all day today on both OS X and Linux, and didn't have a single problem.  I like it!



---

archive/issue_comments_035010.json:
```json
{
    "body": "This has been in my tree for more than a week on a Mac OS X 10.5 machine.  I have been doing some fairly heavy development, although most has not been in Cython.  No problems to report; I say merge.\n\n\n```\nsage: version()\n'Sage Version 3.2.1.alpha2, Release Date: 2008-11-26'\n```\n",
    "created_at": "2008-12-09T19:05:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4652#issuecomment-35010",
    "user": "ncalexan"
}
```

This has been in my tree for more than a week on a Mac OS X 10.5 machine.  I have been doing some fairly heavy development, although most has not been in Cython.  No problems to report; I say merge.


```
sage: version()
'Sage Version 3.2.1.alpha2, Release Date: 2008-11-26'
```




---

archive/issue_comments_035011.json:
```json
{
    "body": "There is a slight chicken and egg problem here since we build pyprocessing after python, so if someone sets the wrong environment variable the build of Python itself will blow up.\n\nTo fix this:\n\n* make sure to unset SAGE_PARALLEL_DIST for the python.spkg as well as the pyprocessing.spkg\n* make all the other python based spkgs depend on pyprocessing, so it is immediately build after Python\n\nThen this should work out of the box, even though we should still test this with a couple rounds of builds of Sage with a high parallel level to make sure we do not hit any race conditions.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-11T10:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4652#issuecomment-35011",
    "user": "mabshoff"
}
```

There is a slight chicken and egg problem here since we build pyprocessing after python, so if someone sets the wrong environment variable the build of Python itself will blow up.

To fix this:

* make sure to unset SAGE_PARALLEL_DIST for the python.spkg as well as the pyprocessing.spkg
* make all the other python based spkgs depend on pyprocessing, so it is immediately build after Python

Then this should work out of the box, even though we should still test this with a couple rounds of builds of Sage with a high parallel level to make sure we do not hit any race conditions.

Cheers,

Michael



---

archive/issue_comments_035012.json:
```json
{
    "body": "After some chit chat with Craig we agreed that this should go into the enf of the pyprocessing spkg-install. That way everything is in place even for a fresh build.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-13T10:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4652#issuecomment-35012",
    "user": "mabshoff"
}
```

After some chit chat with Craig we agreed that this should go into the enf of the pyprocessing spkg-install. That way everything is in place even for a fresh build.

Cheers,

Michael



---

archive/issue_comments_035013.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.2/alpha2/pyprocessing-0.52.p0.spkg\n\ncontains the fix. I tested it in various configs and it works for me :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-13T11:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4652#issuecomment-35013",
    "user": "mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.2/alpha2/pyprocessing-0.52.p0.spkg

contains the fix. I tested it in various configs and it works for me :)

Cheers,

Michael



---

archive/issue_comments_035014.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-13T11:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4652#issuecomment-35014",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035015.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-12-13T18:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4652#issuecomment-35015",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_035016.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-12-13T18:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4652#issuecomment-35016",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_035017.json:
```json
{
    "body": "This breaks at least the numpy and scipy build, so I am reverting for now.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-13T18:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4652#issuecomment-35017",
    "user": "mabshoff"
}
```

This breaks at least the numpy and scipy build, so I am reverting for now.

Cheers,

Michael



---

archive/issue_comments_035018.json:
```json
{
    "body": "Some more info: even unsetting SAGE_PARALLEL_DIST does not fix the problem, bot numpy and scipy fail in different work. So while this is useful when merging patches it breaks too easily on -upgrade or a build from scratch.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-13T18:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4652#issuecomment-35018",
    "user": "mabshoff"
}
```

Some more info: even unsetting SAGE_PARALLEL_DIST does not fix the problem, bot numpy and scipy fail in different work. So while this is useful when merging patches it breaks too easily on -upgrade or a build from scratch.

Cheers,

Michael



---

archive/issue_comments_035019.json:
```json
{
    "body": "Attachment [trac-4652-testing.patch](tarball://root/attachments/some-uuid/ticket4652/trac-4652-testing.patch) by craigcitro created at 2009-06-05 08:00:56",
    "created_at": "2009-06-05T08:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4652#issuecomment-35019",
    "user": "craigcitro"
}
```

Attachment [trac-4652-testing.patch](tarball://root/attachments/some-uuid/ticket4652/trac-4652-testing.patch) by craigcitro created at 2009-06-05 08:00:56



---

archive/issue_comments_035020.json:
```json
{
    "body": "Ok, new version of the code is up. This is done differently than last time; rather than patch our python, I'm simply inserting the code in our `setup.py`, and calling distutils with the new code **only** from Sage. \n\nSo, to test this, do the following:\n\n* download and apply trac-4652-testing.patch\n* set the env variable `SAGE_PARALLEL_DIST` to anything\n* set the env variable `MAKE` to something like `make -j168` (where 168 is the number of simultaneous threads you want)\n* `sage -br` or `sage -ba`\n\nIf this seems to work for people, then we can try building Sage from scratch with it. (I'm going to try setting my machine to do that overnight with `4.0.1.rc2`, I think.) If it works fine, I just want to add a little bit of documentation and then I'm happy to have this merged. If it works for a release or so, I'll start working on getting **something** like this upstream. (I have no idea how uphill that battle will be.)",
    "created_at": "2009-06-05T08:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4652#issuecomment-35020",
    "user": "craigcitro"
}
```

Ok, new version of the code is up. This is done differently than last time; rather than patch our python, I'm simply inserting the code in our `setup.py`, and calling distutils with the new code **only** from Sage. 

So, to test this, do the following:

* download and apply trac-4652-testing.patch
* set the env variable `SAGE_PARALLEL_DIST` to anything
* set the env variable `MAKE` to something like `make -j168` (where 168 is the number of simultaneous threads you want)
* `sage -br` or `sage -ba`

If this seems to work for people, then we can try building Sage from scratch with it. (I'm going to try setting my machine to do that overnight with `4.0.1.rc2`, I think.) If it works fine, I just want to add a little bit of documentation and then I'm happy to have this merged. If it works for a release or so, I'll start working on getting **something** like this upstream. (I have no idea how uphill that battle will be.)



---

archive/issue_comments_035021.json:
```json
{
    "body": "Okay, I ran a build from scratch with this in place, and it worked fine. In particular, it doesn't cause scipy or numpy to fail at building, which was the goal.\n\nSo I'm curious what other people say -- if everyone spoke up real fast, should we try to push this into 4.0.1? (I know several developers have been clamoring for it.)",
    "created_at": "2009-06-05T16:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4652#issuecomment-35021",
    "user": "craigcitro"
}
```

Okay, I ran a build from scratch with this in place, and it worked fine. In particular, it doesn't cause scipy or numpy to fail at building, which was the goal.

So I'm curious what other people say -- if everyone spoke up real fast, should we try to push this into 4.0.1? (I know several developers have been clamoring for it.)



---

archive/issue_comments_035022.json:
```json
{
    "body": "I have certainly been clamoring but I'd really like to see this go through an alpha revision and get tested on multiple platforms before we ship it.  Thanks for doing this, Craig!",
    "created_at": "2009-06-05T16:29:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4652#issuecomment-35022",
    "user": "ncalexan"
}
```

I have certainly been clamoring but I'd really like to see this go through an alpha revision and get tested on multiple platforms before we ship it.  Thanks for doing this, Craig!



---

archive/issue_comments_035023.json:
```json
{
    "body": "I've merged trac-4652-testing.patch in 4.0.1.rc3.",
    "created_at": "2009-06-06T00:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4652#issuecomment-35023",
    "user": "mhansen"
}
```

I've merged trac-4652-testing.patch in 4.0.1.rc3.



---

archive/issue_comments_035024.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-12T07:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4652#issuecomment-35024",
    "user": "craigcitro"
}
```

Resolution: fixed

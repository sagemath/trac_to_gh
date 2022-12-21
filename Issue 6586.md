# Issue 6586: [with spkg; needs review] update Sphinx to version 0.6.2

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-07-22 05:07:41

Assignee: mabshoff

CC:  mhansen sage-combinat

As the summary says.  The spkg can be found at

http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.2.p0.spkg


---

Comment by jhpalmieri created at 2009-07-22 05:11:22

Oh, I forgot: you need to apply the patch at #6585 for the reference manual to build.  This version of Sphinx also prints a lot of new warnings, too.


---

Comment by mvngu created at 2009-07-23 01:22:56

I installed the updated SPKG with

```
./sage -f http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.2.p0.spkg
```

and applied the patch at #6585. When doing

```
./sage -docbuild reference html
```

I got the following errors:

```
mvngu`@`sage sage-4.1.1.alpha0-sage.math.washignton.edu-x86_64-Linux]$ ./sage -docbuild reference html
Traceback (most recent call last):
  File "/scratch/mvngu/sage-4.1.1.alpha0-sage.math.washignton.edu-x86_64-Linux/devel/sage/doc/common/builder.py", line 667, in <module>
    getattr(get_builder(name), type)()
  File "/scratch/mvngu/sage-4.1.1.alpha0-sage.math.washignton.edu-x86_64-Linux/devel/sage/doc/common/builder.py", line 348, in _wrapper
    for module_name in self.get_modified_modules():
  File "/scratch/mvngu/sage-4.1.1.alpha0-sage.math.washignton.edu-x86_64-Linux/devel/sage/doc/common/builder.py", line 412, in get_modified_modules
    env = self.get_sphinx_environment()
  File "/scratch/mvngu/sage-4.1.1.alpha0-sage.math.washignton.edu-x86_64-Linux/devel/sage/doc/common/builder.py", line 403, in get_sphinx_environment
    return BuildEnvironment.frompickle(config, env_pickle)
  File "/scratch/mvngu/sage-4.1.1.alpha0-sage.math.washignton.edu-x86_64-Linux/local/lib/python2.6/site-packages/Sphinx-0.6.2-py2.6.egg/sphinx/environment.py", line 210, in frompickle
    env = pickle.load(picklefile)
AttributeError: 'module' object has no attribute 'RedirStream'
```



---

Comment by jhpalmieri created at 2009-07-23 02:28:01

I think I got this error, too.  Once I deleted doc/output, things worked for me.  (I think there is something stored in the old version of the documentation which confuses the new version of Sphinx.)


---

Comment by mvngu created at 2009-07-24 10:38:56

The upgraded Sphinx SPKG can't handle binary encodings in the file:

```
sage/combinat/partition.py
```

In particular, the following sections from that source file:


line:2233

```
sage: p = loads('x\x9c\x85\x8e\xbd\xaa\xc2`@`\x10\x85\x89\xff.>\xc4\x94\xda\x04\x15|\x04\xb1\xb1\x90\x0b[\x87I\x18\x935\xc9\xae\xb33\xda\t\xd7\xc2\xf76"biw\x0e\x9c\x9f\xef\xbfW\x08\x96\x94\x16\xa1\xcd\x9dGM\xcf\x18\xd5\xa9\x0b\xde\x1c>Jv\x91PIt\xbf\xcd|m8Y\xdc\xb9w\xe3\xfe\xdc&\xf5\xbb\x1d\x9d/%u^\xa9\xa4hZ\xac)\xfb\x18\x1e\xd8d\xfd\xf8\xe3\xa1\x1df\x1e[\xe2\x91\xdd|\x97!\x1ca\xb5\x84\n\xaf\xdd\x02\xbc\xbe\x05\x1a\x12\x01\xad\xd0C\x88`@`|\xc1\x064\xc0\x9a\xc7v\x16\xf2\x13\x15\x9a\x15\r\x8a\xf0\xe47\xf9;ixj\x13_u \xd8\x81\x98K\x9e>\x01\x13iVH')
```



line:2294

```
sage: p = loads('x\x9c\x85\x8e\xbd\x0e\x820\x14\x85\x03\x8a?\x8d\x0f\xd1Q\x97\x06y\x07\xe3\xaa&\x9d\xc9\xa5\xb9\x96\n\xb4^Z\xdcLt\xf0\xbd\xc5 qt;\'9?\xdf#V\x1e4\n\xe5\x9a\xc2X\x08\xe2\nm0\xc18\xcb\x0e\xa3\xf2\xfb\x16!\xa0\x0f\xbbcn+F\xd1\xe6I\xf1\x9d&k\x19UC\xbb5V{al`@`\x8d-k\xa0\xc2|44\x95Q\xf6:Q"\x93\xdcB\x834\x93\xe9o\x99\xbb3\xdf\xa6\xbc\x84[\xbf\xc0\xf5\xf7\x87\x7f 8R\x075\x0f\x8eg4\x97+W\\P\x85\\\xd5\xe0=-\xfeC\x0fIFK\x19\xd9\xb2g\x80\x9e\x81u\x85x\x03w\x0eT\xb1')
```



line:2839

```
sage: dmp = 'x\x9ck`J.NLO\xd5K\xce\xcfM\xca\xccK,\xd1+H,*\xc9,\xc9\xcc\xcf\xe3\n\x80\xb1\x8a\xe3\x93\x81DIQbf^I1W!\xa3fc!Sm!\xb3F(7\x92x!Km!k(GnbE<\xc8\x88B6\x88\xb9E\x99y\xe9\xc5z`@`\x05\xa9\xe9\xa9E\\\xb9\x89\xd9\xa9\xf10N!{(\xa3QkP!Gq(c^\x06\x90c\x0c\xe4p\x96&\xe9\x01\x00\xc2\xe53\xfd'
```

When these lines are removed, the HTML version of the reference manual builds OK. So a possible fix for line 2233 is to replace everything in the TEST block starting from that line by:

```
sage: p = PartitionsGreatestLE(10,2)
sage: p == loads(dumps(p))
True
```

We can do something similar for line 2294; replace everything in the TEST block starting from line 2294 by:

```
sage: p = PartitionsGreatestEQ(10,2)
sage: p == loads(dumps(p))
True
```

As for the TEST block starting from line 2839, I have no idea how to fix it so that the reference manual would successfully builds. Someone on the sage-combinat team to the rescue?


---

Comment by jhpalmieri created at 2009-07-24 14:45:55

Replying to [comment:1 jhpalmieri]:
> Oh, I forgot: you need to apply the patch at #6585 for the reference manual to build.  This version of Sphinx also prints a lot of new warnings, too.

I think that this patch fixes the issue with binary encodings; at least it did for me.


---

Comment by mvngu created at 2009-07-25 23:34:14

With the patch at #6585 and the SPKG, building the reference manual on sage.math takes much longer than previously.


---

Comment by jhpalmieri created at 2009-07-26 22:33:26

Replying to [comment:7 mvngu]:
> With the patch at #6585 and the SPKG, building the reference manual on sage.math takes much longer than previously. 

I agree: on my mac, it took 28 minutes to build the html version with the old one, and 43 minutes with the new one.  With the --jsmath option on, the old one took 6 minutes and the new one took 15 minutes.  I was getting similar comparisons on sage.math.  (This is with me deleting devel/sage/doc/output between each build, to level the playing field.) 

It's strange: for the tutorial and developer's guide, building is about the same or slightly faster with the new version. I also made a modified version of the developer's guide by duplicating some sections (so that the resulting PDF file was 559 pages); the new version was slightly faster there, too.  Maybe it's all of the math in the reference manual?  Maybe it's the large number of files?  Maybe it's the autogeneration of files?


---

Comment by mpatel created at 2009-07-30 07:24:41

Cursory [profiling](http://docs.python.org/library/profile.html) with #6187's "testreference" target indicates that the rewritten `autodoc` extension is significantly slower than before.  I think `autodoc` now also uses far more memory.  Attempting to build the full reference manual on my machine, Sphinx "stalled" at 97% of modules read.  I think the kernel was too busy swapping everything but Sphinx to disk.

Perhaps there's a more efficient, parallelizable representation.  Can we subclass and/or Cythonize [sphinx.ext.autodoc.Documenter](http://sphinx.pocoo.org/ext/appapi.html#sphinx.application.Sphinx.add_autodocumenter)?


---

Comment by mpatel created at 2009-08-01 15:05:08

Minor progress:  It seems that a custom [autodoc-skip-member](http://sphinx.pocoo.org/ext/autodoc.html?highlight=inherited%20members#skipping-members) method now _overrides_ Sphinx's default behavior, which is to skip private methods (`__init__`, etc.).  To keep these out of the reference manual, we might use, e.g.,

```
def skip_NestedClass(app, what, name, obj, skip, options):
    """docstring"""
    skip_nested = str(obj).find("sage.misc.misc") != -1 and name.find("MainClass.NestedClass") != -1
    return skip or skip_nested
```

in `conf.py`.  Unfortunately, this does not significantly reduce the build time or memory usage.


---

Comment by mpatel created at 2009-08-01 19:25:38

Apparently, the culprit is `sphinx.pycode`'s Python source analyzer, which `sphinx.ext.autodoc` uses to extract _attribute_ docstrings.  From `Sphinx-0.6.2-py2.6.egg/sphinx/pycode/__init__.py`:

```
    The docstrings can either be in special '#:' comments before the assignment
    or in a docstring after it.
```

According to the analyzer, there are just two places to find such docstrings in the Sage library:
 * `combinat/designs/block_design.py`
 * `schemes/elliptic_curves/ell_field.py`
Still, resource use is high, because there is a *lot* of caching going on.  We can reduce it with [weak references](http://docs.python.org/library/weakref.html):

```
--- __init__.py.orig    2009-08-01 09:58:27.303927239 -0700
+++ __init__.py 2009-08-01 11:35:17.477865562 -0700
`@``@` -120,10 +120,11 `@``@` class PycodeError(Exception):
             res += ' (exception was: %r)' % self.args[1]
         return res
 
-
+import weakref
 class ModuleAnalyzer(object):
     # cache for analyzer objects -- caches both by module and file name
-    cache = {}
+#    cache = {}
+    cache = weakref.WeakValueDictionary()
 
     `@`classmethod
     def for_string(cls, string, modname, srcname='<string>'):
```

This does reduce build time and memory usage, but I don't know if the output is identical.


---

Comment by mpatel created at 2009-08-01 20:00:14

For `sage -docbuild reference html --jsmath`, at least, the results are close:

```
$ du -s output_v0*
95550   output_v051
97392   output_v062
97388   output_v062_mod
```

The differences are in `environmental.pickle` or stem from using a function as a default argument in
 * `combinat/words/word_content.py`
 * `rings/polynomial/groebner_fan.py`


---

Comment by mpatel created at 2009-08-01 20:00:50

Clearly, it's time for a break.


---

Comment by jhpalmieri created at 2009-08-02 00:12:15

Nice observation.  Making the change with weak_references does indeed speed things up: 

```
0.5.1     28 minutes
0.6.2     43 minutes
0.6.2     33 minutes   (version using weakref)
```

With no other changes, it includes all of the private methods, as already pointed out (and I assume it did before using weakref -- this may account for some of the increased time, since it's producing more output), but it also includes (for some classes, anyway), an entry for `__weakref)_`.  See the documentation for sage/algebras/steenrod_algebra.py, for instance: it lists as an attribute of SteenrodAlgebraFactory

```
__weakref__
   list of weak references to the object (if defined)
```



---

Comment by mpatel created at 2009-08-02 01:24:11

Actually, noticing `__weakref__` for that module is what led to the comment about `autodoc-skip-member`.  I think this was before I "patched" Sphinx, but I may be mistaken.  I'm also not sure about why `__weakref__` appears spontaneously.  Perhaps a super class?


---

Comment by mpatel created at 2009-08-02 10:46:50

See #6664 for the `autodoc-skip-member` issue.


---

Comment by mpatel created at 2009-08-02 10:48:56

Also, I've asked about the merits of the `weakref` workaround on [sphinx-dev](http://groups.google.com/group/sphinx-dev).


---

Comment by mpatel created at 2009-08-02 21:17:15

Example inheritance diagram for "The Steenrod algebra".  This is just for fun.


---

Attachment

The new [inheritance diagram](http://sphinx.pocoo.org/ext/inheritance.html?highlight=inheritance#module-sphinx.ext.inheritance_diagram) extension has potential.  I've attached a minimal example.  *Please do not merge it.*

The options are limited, however.  For example, I could not find a directive that auto-generates a diagram for each module.  Also, it seems there's no way to color-code the nodes/classes, e.g., to indicate their modular provenance.  Maybe it's possible to do one or more of these ourselves, in `builder.py`, `conf.py`, or by patching Sphinx.


---

Comment by mpatel created at 2009-08-02 21:26:58

I should add that this requires a local installation of [GraphViz](http://www.graphviz.org/).


---

Comment by mpatel created at 2009-08-05 08:18:58

Replying to [comment:17 mpatel]:
> Also, I've asked about the merits of the `weakref` workaround on [sphinx-dev](http://groups.google.com/group/sphinx-dev).  
The [thread](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6187/trac_6187_testreference.patch).  Preliminary tests indicate that the proposed alternative does not reduce memory use significantly.


---

Comment by mpatel created at 2009-08-05 08:20:57

Replying to [comment:20 mpatel]:
> Replying to [comment:17 mpatel]:
> > Also, I've asked about the merits of the `weakref` workaround on [sphinx-dev](http://groups.google.com/group/sphinx-dev).  
> The [thread](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6187/trac_6187_testreference.patch).  Preliminary tests indicate that the proposed alternative does not reduce memory use significantly.  
[Here](http://groups.google.com/group/sphinx-dev/browse_thread/thread/db7752d5316f699c), actually.


---

Comment by mpatel created at 2009-08-14 12:30:39

There's been no further activity about the workaround on sphinx-dev.  Since weakrefs appear to work for us, should we add a patch to the spkg?


---

Comment by mvngu created at 2009-08-14 12:33:57

Replying to [comment:22 mpatel]:
> There's been no further activity about the workaround on sphinx-dev.  Since weakrefs appear to work for us, should we add a patch to the spkg?
Hmm... could you make an spkg with that workaround?


---

Comment by jhpalmieri created at 2009-08-14 15:01:29

Replying to [comment:23 mvngu]:
> Replying to [comment:22 mpatel]:
> > There's been no further activity about the workaround on sphinx-dev.  Since weakrefs appear to work for us, should we add a patch to the spkg?
> Hmm... could you make an spkg with that workaround?

I can certainly do it, but not until Monday.


---

Comment by mpatel created at 2009-08-20 06:15:36

Does the problem described [here](http://groups.google.com/group/sage-devel/browse_thread/thread/fa1f33186d5fd636#) recur with the new spkg?


---

Comment by jhpalmieri created at 2009-08-20 14:50:35

The new spkg is at

[http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.2.p1.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.2.p1.spkg)

(The old one is still there; it's "...p0.spkg", as listed in the description above.)


---

Comment by jhpalmieri created at 2009-08-23 17:28:50

By the way, note that since this includes the private methods in the reference manual, there are a lot of new warnings when building that document.  (People haven't written all of the docstrings for their `__init__` methods, etc., to conform with proper reST format, since they didn't need to before.)  These should be dealt with in a separate ticket: otherwise, we might feel obliged to keep rebasing this ticket until it was merged.


---

Comment by mpatel created at 2009-08-23 17:31:03

Does #6664 suppress the private methods?


---

Comment by jhpalmieri created at 2009-08-23 18:08:33

> Does #6664 suppress the private methods?

Yes, but do we *want* to suppress the private methods?  I actually prefer that they be included in the reference manual.


---

Comment by jhpalmieri created at 2009-08-23 22:37:57

Uh oh, it seems as though with this spkg, changes to pyx files are not detected.  That is, build the documentation (say, with the jsmath option).  Then edit a .py file and a .pyx file (I chose sage/misc/latex.py and sage/matrix/matrix0.pyx).  Run 'sage -docbuild reference print_modified_modules': the .py file will be listed, but not the .pyx file.  I can't figure out why this is happening :(


---

Comment by mpatel created at 2009-08-26 11:21:08

I also don't know why.  `builder.py` uses Sphinx's `get_outdated_files()` method to get an iterable of modified modules.  However, this method's code is the same in v0.5.1 and v0.6.2.  I did find that the newer Sphinx does not include .so files for .pyx files in `environment.pickle`'s `dependencies` dictionary.  This may "explain" the observed behavior.


---

Comment by jhpalmieri created at 2009-08-27 02:06:23

I played around with the Sphinx code for a while, and I could not figure out what's going on.  Well, I believe that "matrix0.so" was listed as a dependency of "matrix0.pyx" in version 0.5.1, so changing the .pyx file resulted in the modification time for the .so file to be wrong, triggering a rebuild of the docs, but in 0.6.2, the .so file no longer appears to be a dependency of the .pyx file.  I've posted a message to sphinx-dev about how dependencies are determined; we'll see if there are any helpful responses.


---

Comment by jhpalmieri created at 2009-09-02 21:20:56

Okay, I now have a patch which seems to recognize changes to pyx files.  The dependency information is stored in the pickle, so to test this, first delete `SAGEDOC/output/doctrees/`.  The new spkg is available from
[http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.2.p2.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.2.p2.spkg).

Please test thoroughly.  (One thing to watch out for: I thought it wasn't working because I was changing sage/matrix/action.pyx and seeing no notification when the reference manual was built, but then I realized that action.pyx isn't even included in the reference manual.  Doh.)


---

Comment by jhpalmieri created at 2009-09-03 21:05:51

In case anyone downloaded the version posted yesterday, there is a slightly modified version today: the author of Sphinx posted a patch for the Cython problem to the [Sphinx mercurial site](http://bitbucket.org/birkenfeld/sphinx/changeset/8a434cdb511f/), and so the version today uses that patch instead.  (Mine was similar to his, but why not use the official one?)

I've replaced the old one with the new one, so the link is the same: [http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.2.p2.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.2.p2.spkg).


---

Comment by jhpalmieri created at 2009-09-04 02:02:05

Okay, here's another one.  Sphinx was just updated to version 0.6.3, and this is supposed to fix our problems.  In my testing, it doesn't have the Cython problem that the original version of 0.6.2 had; it incorporates the patch in the most recent 0.6.2 spkg.  The 0.6.3 spkg is a bit slower than 0.5.1 and also than our version of 0.6.2 with the unauthorized weakref patch.  It's not nearly as slow and doesn't seem to use nearly as much memory as the unpatched 0.6.2.  Here's the spkg: [http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.3.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.3.p0.spkg).

Some timings in minutes for "sage -docbuild reference html --jsmath", with the patch at #6664 applied:

```
                    Mac      sage.math  ubuntu
Sphinx 0.5.1         6           5        10
Sphinx 0.6.2.p2      6           6        10
Sphinx 0.6.3         8           9        11
```

"Mac" is my Intel iMac running OS X 10.5; "sage.math" is sage.math, and "ubuntu" is an old ubuntu box I have access to.

As I said above, the memory usage seems to stay within reason for all of these, but I'm not using anything sophisticated to test this: with the terrible version, my computer would become very sluggish, and with the versions tested here, that doesn't happen.


---

Comment by mpatel created at 2009-09-04 07:40:11

For Sage 4.1.2.alpha0's HTML reference manual, at least, the new spkg seems to work just as Georg indicated.  I'll try to do more testing soon.

By the way, it might be useful to update spkg-install along the lines of #6598 and [this example](http://wiki.sagemath.org/DavidKirkby).  For example,
{{{#!/usr/bin/env bash

if [ -z "$SAGE_LOCAL" ]; then
   echo "SAGE_LOCAL undefined ... exiting";
   echo "Maybe run 'sage -sh'?"
   exit 1
fi

success() {
    if [ $? -ne 0 ]; then
        echo "Error building Sphinx: '$1'"
        exit 1
    fi
}

set -e

echo "Removing old version..."
rm -rf "$SAGE_LOCAL"/lib/python/site-packages/Sphinx-*
success 'deleting previous version'

[...]
```



---

Comment by jhpalmieri created at 2009-09-04 21:53:59

Replying to [comment:36 mpatel]:
> By the way, it might be useful to update spkg-install along the lines of #6598 and [this example](http://wiki.sagemath.org/DavidKirkby).  For example,

Okay, try this one: [http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.3.p1.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.3.p1.spkg).  (Putting "set -e" in other places made the script exit without printing the custom error message.  With this one, if, for example, I make the directory `"$SAGE_LOCAL"/lib/python/site-packages/Sphinx-*` undeletable, I get the appropriate message.)


---

Comment by mpatel created at 2009-09-05 14:30:32

Thanks very much for pointing that out.  I may need to update the spkgs at #5447...


---

Comment by timdumol created at 2009-09-05 15:58:05

Forgive me if I'm mistaken, but doesn't Sphinx>=0.6 depend on Jinja2?

  Incompatible changes:

    * Templating now requires the Jinja2 library, which is an enhanced version of the old Jinja1 engine.

http://sphinx.pocoo.org/changes.html#release-0-6-mar-24-2009


---

Comment by mpatel created at 2009-09-05 16:21:32

Yes.  I think `site-packages/Jinja2-2.1.1-py2.6-linux-x86_64.egg`, say, is installed automatically (via network) by `python setup.py install` in `spkg-install`.

Should we make it a separate spkg, to supplement or replace `jinja-1.2.p0.spkg`?


---

Comment by mpatel created at 2009-09-05 16:51:06

I checked that Sphinx now incorporates changes to included .py and .pyx files.

For the HTML builder, both `jsmath` and `pngmath` modes appear to work as expected.  

The PDF reference manual's table of contents is missing.  This may stem from #6885 and my invoking LaTeX's batch mode with `b`.


---

Comment by timdumol created at 2009-09-06 01:29:26

Replying to [comment:40 mpatel]:
> Yes.  I think `site-packages/Jinja2-2.1.1-py2.6-linux-x86_64.egg`, say, is installed automatically (via network) by `python setup.py install` in `spkg-install`.
> 
> Should we make it a separate spkg, to supplement or replace `jinja-1.2.p0.spkg`?

I think it would probably best to make a separate spkg so that installation will not require network access. I've made an spkg that I can post if you want.

Also, the spkg for this states that it depends on Jinja>=``1.1``, which is no longer the case.


---

Comment by jhpalmieri created at 2009-09-06 02:09:59

Okay, I've updated the file SPKG.txt (in [http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.3.p1.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.3.p1.spkg)) to say that it depends on Jinja >= 2.  If you want to post a link to an spkg for jinja, that would be great.


---

Comment by timdumol created at 2009-09-06 03:43:56

Here you go: http://drop.io/jinja2_spkg


---

Comment by jhpalmieri created at 2009-09-06 04:35:42

A few issues with the Jinja spkg: the source is under version control but it shouldn't be.  When I install it, I get jinja2-2.1.1, not jinja2-2.2, so the name is wrong.  Also, the part of the spkg-install file which is supposed to remove the old version wasn't removing the right thing (it said "Jinja-2*", but the directory is actually "Jinja2-2.1.1*").

Anyway, here's a modified spkg, much smaller since src is not in the mercurial repository.  This is an updated version of the version 1 jinja spkg, with the new src dropped in, replacing the old src: [http://sage.math.washington.edu/home/palmieri/SPKG/jinja2-2.1.1.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/jinja2-2.1.1.p0.spkg).

Should this have its own ticket?  Will it screw up anything from #6568?  I don't know anything about Jinja, so I don't know what to do to test it; all I see is that the docs are built correctly with the new versions of Sphinx and Jinja.


---

Comment by timdumol created at 2009-09-06 04:41:43

Thanks for the fixes.

Jinja and Jinja2 are totally different, and so it shouldn't affect any current templating routines. In any case, once Sphinx 0.6.3 is included, we can remove the dependency on Jinja by replacing all instances of `import jinja` with `import jinja2`, etc. The API's are pretty much unchanged, and from what I know, none of the changed interfaces are currently used.


---

Comment by cremona created at 2009-09-06 16:58:33

I'm not at all sure what you people are doing here, so perhaps I should have kept away, but (in trying to help with #6820) I tried installing the new sphinx spkg using

```
./sage -f http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.2.p0.spkg
```

and now 

```
john`@`ubuntu%sage -docbuild reference html
Traceback (most recent call last):
  File "/home/john/sage-4.1.1/devel/sage/doc/common/builder.py", line 667, in <module>
    getattr(get_builder(name), type)()
  File "/home/john/sage-4.1.1/devel/sage/doc/common/builder.py", line 348, in _wrapper
    for module_name in self.get_modified_modules():
  File "/home/john/sage-4.1.1/devel/sage/doc/common/builder.py", line 412, in get_modified_modules
    env = self.get_sphinx_environment()
  File "/home/john/sage-4.1.1/devel/sage/doc/common/builder.py", line 403, in get_sphinx_environment
    return BuildEnvironment.frompickle(config, env_pickle)
  File "/home/john/sage-4.1.1/local/lib/python2.6/site-packages/Sphinx-0.6.2-py2.6.egg/sphinx/environment.py", line 210, in frompickle
    env = pickle.load(picklefile)
AttributeError: 'module' object has no attribute 'RedirStream'
```


This is in the main branch, so a vanilla 4.1.1 build.  Should that be 4.1.2.alpha0?


---

Comment by timdumol created at 2009-09-06 17:11:00

Hey.

The first spkg had problems. There are newer spkgs. http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-0.6.3.p1.spkg is the latest.


---

Comment by jhpalmieri created at 2009-09-06 17:26:39

To cremona: sorry about that.  When you switch versions of Sphinx, you have to delete the old output in the docs directory -- it caches some information there, apparently in ways which are not compatible between versions.  So after you install the spkg, delete the directory SAGE_ROOT/devel/sage/doc/output and try again.  I should change the summary on this ticket to reflect this...

To timdumol: I see, jinja and jinja2 can coexist on the same system, so for now we can have both.  That's the best solution now, I agree.  (I tried replacing all of the "import jinja" lines with "import jinja2", but there was a problem with one of them: in sage.ext.gen_interpreters, the line `from jinja.datastructure import ComplainingUndefined` doesn't translate, because there is no jinja2.datastructure.)


---

Comment by cremona created at 2009-09-06 19:16:19

Thanks -- that worked!  (Except that I cannot read and deleted all SAGE_ROOT/devel/sage/doc and not just the output directory, so had to copy the rest from another clone...)

I like the percentage meter and the fact that the output overwrites one line rather than running off the screen.  Minor point here:  it does not overwrite long lines when they are followed by short ones so you see strange garbage characters on the end of te line like this:

```
reading sources... [ 49%] sage/misc/explain_pickle      _densensephismsmpecies
```

Of course this is a triviality.

Otherwise all went well and (from the point of view of an ordinary user/developer) I'm happy with this spkg.  (There are lots of warnings and at least one error in the docstrings, but that is another matter).  I have no objection to this getting a positive review, assuming tha the other issues discussed above have been dealt with.


---

Attachment

new version the file spkg/install (incorporating jinja2)


---

Comment by jhpalmieri created at 2009-09-06 22:00:39

new version of the file spkg/standard/deps (incorporating jinja2)


---

Attachment

diff between old and new install


---

Attachment

diff between old and new deps


---

Comment by mpatel created at 2009-09-11 00:54:52

Both the latest Sphinx and Jinja2 packages appear to install without network activity.  The changes to `install` and `deps` look good to me, but I haven't done a complete installation from scratch.

To the extent that it counts, my review is positive.


---

Comment by timdumol created at 2009-09-22 16:37:17

Documentation builds perfectly. Sphinx 0.6.3 takes only 2 minutes more `sys` time than 0.5.1 to build all the docs, for me.

Haven't done a complete install yet, but I'll do so once I finish downloading the 4.1.2.alpha2 tarball.


---

Comment by mpatel created at 2009-09-25 12:39:02

I updated `spkg/install` and `spkg/standard/deps`, replaced the old Sphinx spkg with the new one in `spkg/standard`, and copied the Jinja2 package to `spkg/standard`.  With these changes, `sage -bdist 100` generates the expected binary distributions on sage.math from both binary and compiled source distributions.  Moreover, `sage -sdist 200` makes a source distribution that compiles as expected.

There's a failed test:

```python
mpatel`@`sage sage-200$ ./sage -t devel/sage/sage/misc/trace.py 
sage -t  "devel/sage/sage/misc/trace.py"                    
**********************************************************************
File "/scratch/mpatel/source/sage-200/devel/sage/sage/misc/trace.py", line 61:
    sage: print s.before[s.before.find('-'):]
Expected:
    ---...
    ipdb> c
    2 * 5
Got:
    --Call--
    > /scratch/mpatel/source/sage-200/local/lib/python2.6/site-packages/sage/rings/arith.py(1944)factor()
       1943 
    -> 1944 def factor(n, proof=None, int_=False, algorithm='pari', verbose=0, **kwds):
       1945     """
    
    ipdb> c
    2 * 5
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_1
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mpatel/source/sage-200/tmp/.doctest_trace.py
         [3.7 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/misc/trace.py"
Total time for all tests: 3.7 seconds
```

I _think_ it's not related to this ticket.


---

Comment by mpatel created at 2009-10-04 14:56:06

Problem: Somehow, Sphinx 0.6.3 breaks the sidebar toggle (cf. #6507) in the _live_ docs.  In Firebug's console:

```js
unexpected end of XML source
<span class="math">('#searchbox').show(0);
```



---

Comment by mpatel created at 2009-10-05 00:16:19

Patching Sphinx 0.6.3 should fix this and perhaps also a similar problem reported on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/bb2d0d7f43efefc9/796d42841bd79c5c?#796d42841bd79c5c): 

```diff
--- sphinx/themes/basic/layout.html.orig        2009-10-04 17:07:16.000000000 -0700
+++ sphinx/themes/basic/layout.html     2009-10-04 17:07:28.000000000 -0700
`@``@` -81,7 +81,7 `@``@`
               {{ _('Enter search terms or a module, class or function name.') }}
               </p>
           </div>
-          <script type="text/javascript">$('#searchbox').show(0);</script>
+          <script type="text/javascript">jQuery('#searchbox').show(0);</script>
           {%- endif %}
           {%- endblock %}
         </div>
```



---

Comment by mpatel created at 2009-10-05 00:22:14

Or perhaps not.


---

Comment by timdumol created at 2009-10-05 18:53:45

mpatel: The problem with the sidebar is caused by compression. Line comments ("//") are used in the sidebar code, therefore when the code is compressed, the entire function is commented out. Changing the line comments to block comments ("/* */") fixed the problem for me.


---

Comment by timdumol created at 2009-10-05 19:04:30

A patch for the doc sidebar problem is now up at #7126.


---

Comment by mpatel created at 2009-10-06 00:26:46

If [comment:ticket:7126:2 this comment] at #7126 is correct, we should still patch `sphinx/themes/basic/layout.html`.  I can do this.


---

Comment by timdumol created at 2009-10-06 15:38:29

Replying to [comment:55 mpatel]:
> Problem: Somehow, Sphinx 0.6.3 breaks the sidebar toggle (cf. #6507) in the _live_ docs.  In Firebug's console:
> {{{
> #!js
> unexpected end of XML source
> <span class="math">('#searchbox').show(0);
> }}}

#7141 adds a patch that fixes this.


---

Comment by mhansen created at 2009-10-16 04:45:42

Resolution: fixed


---

Comment by mhansen created at 2009-10-16 04:45:42

Merged both the jinja2 and sphinx in spkg.

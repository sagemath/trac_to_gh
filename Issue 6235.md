# Issue 6235: set MPLCONFIGDIR environment variable when Sage starts up

Issue created by migration from https://trac.sagemath.org/ticket/6235

Original creator: was

Original creation time: 2009-06-06 19:45:56

Assignee: cwitty

CC:  leif mpatel justin




---

Comment by was created at 2009-06-06 19:47:23


```


2009/6/6 Brian Granger <>:
>
>> I want to reopen this thread.
>
> Great!  matplotlib under Sage is still broken for me because of this
> issue - I would love to see this resolved.
>
>> I have a build farm with many (nearly 20) different OS's that all build and test
>> Sage in parallel.  My home directory on each of those machines is NFS exported
>> and shared.  I sometimes have tests fail because all these different
>> Sage's are trying to write to the same $HOME/.matplotlib directory
>> (for temp files, configuration, etc.).
>> For Sage itself, I set SAGE_HOME to a fast local scratch disk (on each
>> machine), which completely solves any contention problems for
>> *everything* related to Sage temp files, configuration, etc., with the
>> notable exception of matplotlib.
>
> I hadn't thought of this issue, but it is another good reason to not
> use $HOME/.matplotlib for the Sage matplotlib.
>
>> Thus I would also prefer it if
>> Sage's matplotlib directory were under SAGE_HOME instead of it being
>> the default $HOME/.matplotlib.
>>
>> Thoughts?
>
> I think the simplest solution is to have Sage set:
>
> export MPLCONFIGDIR=$SAGE_HOME/matplotlib
>
> But, wait, does SAGE_HOME point to $HOME/.sage by default?  That is
> the right place for this, I just don't remember exactly where
> SAGE_HOME points.

Yep, it does.  We can make sure easily enough by running Sage and asking:

sage: DOT_SAGE
'/Users/wstein/.sage/'

By the way, I just realized it is called "DOT_SAGE", not "SAGE_HOME".

This is now:

http://trac.sagemath.org/sage_trac/ticket/6235

 -- William


>
> I don't even think we need to put a default matplotlibrc file there,
> so we don't have to worry about it becoming out of date.  If people
> want to add their own matplotlibrc file to this directory they can,
> but the default will be that matplotlib works.
>
> Cheers,
>
> Brian
>
>> William
>>
>>
>>>> In the mailing list thread, the option was brought up to have the user
>>>> put in a command in their init.sage file if they wanted a custom Sage
>>>> initialization for matplotlib.  Setting the MATPLOTLIBRC variable in the
>>>> init.sage file should work, I think.
>>>
>>> Yes, but I don't see this file in my .sage directory.  Where would it be?
>>>
>>>> In reality, (I think) the people this affects are the people that have
>>>> already customized their system install of matplotlib.  Those are the
>>>> people that (I think) would be capable of writing another command in
>>>> their init.sage or something to have Sage have a custom matplotlibrc file.
>>>
>>> Yes, for the most part I agree with this.  But it is not quite that
>>> simple.  I still need/want to be able to configure matplotlib for Sage
>>> and my own install separately.  That means I have to copy my own
>>> matplotlibrc file into .sage, make edits and set variables in
>>> init.sage.
>>>
>>>> On the other hand, I can see the nice thing about Sage being totally
>>>> self-contained and not pulling settings from a user's home directory for
>>>> options.
>>>
>>> Yes, I think Sage should "Just Work", even for users that have
>>> matplotlib installed previously.  This is simple enough to fix, I
>>> don't see why we wouldn't.  The only thing is that the matplotlibrc
>>> file needs to be updated anytime that matplotlib itself is updated.
>>>
>>> Cheers,
>>>
>>> Brian
>>>
>>> >
>>>
>>
>>
>>

```



---

Comment by jason created at 2010-09-30 04:51:11

Discussion: http://www.mail-archive.com/sage-devel`@`googlegroups.com/msg23608.html


---

Comment by jason created at 2010-09-30 13:17:23

Problems are cropping up at #9122 dealing with configuration files and font caches, etc.  Any comment on setting MPLCONFIGDIR to be something inside of the Sage hierarchy, maybe SAGE_LOCAL/etc/matplotlib?  For example, the font caches should point to the matplotlib directory in the current Sage being run, but this would not happen usually with multiple Sage instances laying around (or a system matplotlib install) and a global MPLCONFIGDIR (even if that global directory was in the .sage directory).


---

Comment by jason created at 2010-10-20 13:21:58

The problems in #9221 (I mistakenly said #9122 above) were fixed with a patch to the matplotlib spkg that has been applied upstream as well.  The issue on this ticket still stands, but it is not urgent for #9221 anymore.


---

Comment by leif created at 2010-10-20 13:31:58

Replying to [comment:5 jason]:
> The problems in #9221 (I mistakenly said #9122 above) were fixed with a patch to the matplotlib spkg that has been applied upstream as well.  The issue on this ticket still stands, but it is not urgent for #9221 anymore.

I just noticed that _some_ (I don't know yet which, i.e. the one from alpha2 or alpha3) matplotlib 1.0.0 spkg broke *all* previous Sage installations, due to `~/.matplotlib/`...

(And especially made testing #9896 totally useless. :( )


---

Comment by jason created at 2010-10-20 13:34:14

Replying to [comment:6 leif]:


> I just noticed that _some_ (I don't know yet which, i.e. the one from alpha2 or alpha3) matplotlib 1.0.0 spkg broke *all* previous Sage installations, due to `~/.matplotlib/`...

Can you elaborate?  What do you mean "due to `~/.matplotlib/`"?


---

Comment by leif created at 2010-10-20 13:49:06

Replying to [comment:7 jason]:
> Replying to [comment:6 leif]:
> 
> 
> > I just noticed that _some_ (I don't know yet which, i.e. the one from alpha2 or alpha3) matplotlib 1.0.0 spkg broke *all* previous Sage installations, due to `~/.matplotlib/`...
> 
> Can you elaborate?  What do you mean "due to `~/.matplotlib/`"?

Without deleting `~/.matplotlib/`, I get the doctest errors in `sage/plot/` mentioned [here](http://trac.sagemath.org/sage_trac/ticket/9896#comment:128).

Also, I did get compilation errors related to freetype [like you reported](http://trac.sagemath.org/sage_trac/ticket/9221#comment:24).


---

Comment by leif created at 2010-10-20 13:51:55

Replying to [comment:8 leif]:
> Also, I did get compilation errors related to freetype [like you reported](http://trac.sagemath.org/sage_trac/ticket/9221#comment:24).

(Even rebuilding Sage 4.5.3 from scratch failed.)


---

Comment by jhpalmieri created at 2010-10-20 20:20:43

Can we just do

```
MPLCONFIGDIR="$DOT_SAGE/matplotlib"
export MPLCONFIGDIR
```

in sage-env?  I suppose we could add yet another environment variable, like SAGE_MPLCONFIGDIR, and do

```
if [ "$SAGE_MPLCONFIGDIR" = "" ]; then
    MPLCONFIGDIR=$DOT_SAGE/matplotlib
else
    MPLCONFIGDIR=$SAGE_MPLCONFIGDIR
fi
export MPLCONFIGDIR
```

but I don't think that's necessary.  We already have too many environment variables.  I suppose we could test whether MPLCONFIGDIR is set, and if so, print a warning (once) that Sage is not using the user's setting of this variable.  I'm not sure where to test this, though.

If we export our setting for MPLCONFIGDIR, then we also need to document it, probably in the installation guide, saying that Sage uses its own matplotlib config directory, not the default one or whatever the user may have set.


---

Comment by leif created at 2010-10-20 20:40:12

Replying to [comment:10 jhpalmieri]:
> Can we just do

```
MPLCONFIGDIR="$DOT_SAGE/matplotlib"
export MPLCONFIGDIR
```

> in sage-env? 

As mentioned above, the configuration should be inside a _specific Sage installation_ hierarchy, not just yet another _user-specific_ directory, which is (usually) the same for all Sage installations.

I don't understand why the matplotlib developers broke compatibility with older versions; I think it's likely to have different MPL installations included in other software packages, but I might be wrong. IMHO bad design anyway; also the exceptions raised are odd.


---

Comment by jason created at 2010-10-20 20:53:47

Replying to [comment:11 leif]:
> Replying to [comment:10 jhpalmieri]:
> > Can we just do
> {{{
> MPLCONFIGDIR="$DOT_SAGE/matplotlib"
> export MPLCONFIGDIR
> }}}
> > in sage-env? 
> 
> As mentioned above, the configuration should be inside a _specific Sage installation_ hierarchy, not just yet another _user-specific_ directory, which is (usually) the same for all Sage installations.

At the same time, this directory should not be inside a specific Sage installation (i.e., below SAGE_ROOT) since that means system-wide installs can't have individual customizations, and it also breaks system-wide font cache generation (i.e., matplotlib assumes that a user can update the font cache file, I believe).  So where are we now?  Separate matplotlib config directories for each version of Sage inside of the .sage directory?


> 
> I don't understand why the matplotlib developers broke compatibility with older versions; I think it's likely to have different MPL installations included in other software packages, but I might be wrong. IMHO bad design anyway; also the exceptions raised are odd.


---

Comment by leif created at 2010-10-20 21:05:30

Replying to [comment:12 jason]:
> At the same time, this directory should not be inside a specific Sage installation (i.e., below SAGE_ROOT) since that means system-wide installs can't have individual customizations, and it also breaks system-wide font cache generation (i.e., matplotlib assumes that a user can update the font cache file, I believe).  So where are we now?  Separate matplotlib config directories for each version of Sage inside of the .sage directory?

I was thinking of that, too. Not that easy, though. (E.g. using the Sage version as an "index" isn't reliable either.)

Is the font cache the only problem? If so, we could just delete it upon every Sage [script] start-up... (quite ugly, of course)

But older versions of MPL should simply recognize config files from newer versions and e.g. (partially) ignore them. Or at least print an _appropriate_ error message. (Not very pythonic, I know. *SCNR*)


---

Comment by jason created at 2010-10-20 21:23:45

Replying to [comment:13 leif]:
> Replying to [comment:12 jason]:
> > At the same time, this directory should not be inside a specific Sage installation (i.e., below SAGE_ROOT) since that means system-wide installs can't have individual customizations, and it also breaks system-wide font cache generation (i.e., matplotlib assumes that a user can update the font cache file, I believe).  So where are we now?  Separate matplotlib config directories for each version of Sage inside of the .sage directory?
> 
> I was thinking of that, too. Not that easy, though. (E.g. using the Sage version as an "index" isn't reliable either.)
> 
> Is the font cache the only problem? If so, we could just delete it upon every Sage [script] start-up... (quite ugly, of course)

I believe (off the top of my head) that the error "    TypeError: coercing to Unicode: need string or buffer, dict found" comes from the newer matplotlib including some stix fonts, and so it updates the font cache file to include those files.  However, older versions of matplotlib did not deal gracefully with font cache files that referred to nonexistant directories.  So if you install the new Sage, then matplotlib updates the font cache file to include the new fonts in the new matplotlib, then you move the new Sage install, the old Sage install will probably die when trying to open the nonexistant new font.  Of course, matplotlib should just silently regenerate the cache file, and that is what the bugfix in the 1.0.0 spkg is.


---

Comment by jhpalmieri created at 2010-10-20 21:34:34

How about separate matplotlib config directories for each version of matplotlib?  We could read the version from the file `SAGE_ROOT/local/lib/python/site-packages/matplotlib/__init__.py` -- search for `"__version__ = ..."`.  If the file `matplotlib/__init__.py` does not exist, then matplotlib hasn't been installed yet, so we don't care what we set MPLCONFIGDIR to, but if it exists, we can set MPLCONFIGDIR to something like "$DOT_SAGE/matplotlib-$VER".

(We could instead look at the name of the file SAGE_ROOT/local/lib/python/site-packages/matplotlib-VER-py2.6.egg-info, although if we upgrade, there could be several of these files present, and this doesn't seem as safe to me.)


---

Comment by jason created at 2010-10-20 21:35:42

Of course, by the reasoning in my previous post, simply moving an old sage version directory should have caused the same problem.  So I guess my explanation doesn't seem right anymore.


---

Comment by jhpalmieri created at 2010-10-20 21:43:54

In case my idea works, when you install the matplotlib spkg, does it need to know the value of MPLCONFIGDIR, or is it safe to set that only after matplotlib has been installed?


---

Comment by leif created at 2010-10-20 22:07:18

Replying to [comment:15 jhpalmieri]:
> How about separate matplotlib config directories for each version of matplotlib?
> [...]
> we can set `MPLCONFIGDIR` to something like `$DOT_SAGE/matplotlib-$VER`.

Sounds like a good idea to me. (You should suggest similar upstream; they could _read_ `MPLCONFIGDIR` but _write_ incompatible things to a versioned subdirectory of that.)

> In case my idea works, when you install the matplotlib spkg, does it need to know the value of `MPLCONFIGDIR`, or is it safe to set that only after matplotlib has been installed?

I'm not sure if MPL writes anything to that during installation; it's perhaps sufficient to set MPLCONFIGDIR before _using_ MPL (i.e., after installation) to fix the `TypeError` issue with parallel installations of older versions.


---

Comment by leif created at 2010-10-20 22:19:00

Replying to [comment:18 leif]:
> I'm not sure if MPL writes anything to that during installation; it's perhaps sufficient to set MPLCONFIGDIR before _using_ MPL (i.e., after installation) to fix the `TypeError` issue with parallel installations of older versions.

At least our current 1.0.0 doesn't write to / create `$HOME/.matplotlib/` during _installation_.

(I simply renamed the directory and did `./sage -f matplotlib-1.0.0`.)

Doing

```
sage: import matplotlib
```

recreates the directory (`$HOME/.matplotlib/`).


---

Comment by leif created at 2010-10-20 22:29:48

:-) Try:

```sh
$ export MPLCONFIGDIR=/some/non-existent/dir/ && ./sage -c "import matplotlib"
```

(The trailing slash doesn't matter. Also, using `$HOME/non-existent/` doesn't make a difference.)


---

Comment by jhpalmieri created at 2010-10-20 22:36:42

Replying to [comment:20 leif]:
> :-) Try:

```sh
$ export MPLCONFIGDIR=/some/non-existent/dir/ && ./sage -c "import matplotlib"
```

> (The trailing slash doesn't matter. Also, using `$HOME/non-existent/` doesn't make a difference.)

Cool.


---

Comment by jhpalmieri created at 2010-10-20 22:40:47

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-10-20 22:40:47

Here's a patch.  The "sed" business could be done more efficiently by someone who actually knows how to use sed.  You can consider this a first draft if you want, but I'm marking it as ready for review.


---

Comment by leif created at 2010-10-20 23:35:25

Replying to [comment:22 jhpalmieri]:
> Here's a patch.  The "sed" business could be done more efficiently by someone who actually knows how to use sed.  You can consider this a first draft if you want, but I'm marking it as ready for review.


```sh
...

    MPLVER=`sed -n "/^__version__[ ]*=[ ]*'[^']*'/s/[^']*'\([^']*\)'.*$/\1/p" "$SAGE_LOCAL"/lib/python/site-packages/matplotlib/__init__.py`
    # Or just (if we check the result):
    # MPLVER=`sed -n "/^__version__[ ]*=/s/[^']*'\([^']*\)'.*$/\1/p" "$SAGE_LOCAL"/lib/python/site-packages/matplotlib/__init__.py`

    # Hopefully they never switch to double quotes...

...

$MKDIR -p "$MPLCONFIGDIR" # better quote the dir
```


Perhaps also check that `"$MPLVER"` is non-empty.


---

Comment by leif created at 2010-10-20 23:51:45

More funny:

```sh
    eval `sed -n "/^__version__[ ]*=/s/ //gp" "$SAGE_LOCAL"/lib/python/site-packages/matplotlib/__init__.py`
    MPLVER=$__version__
```



---

Comment by jhpalmieri created at 2010-10-21 00:00:02

Here's a new patch using leif's less funny version.  It also does not set MPLCONFIGDIR if the file `matplotlib/__init__.py` is not found, partly because I don't want to have to create $DOT_SAGE/matplotlib early in the installation process.  One small drawback to the current approach is that perhaps during an upgrade from a version of Sage using matplotlib-0.99 to a version using matplotlib-1.0.0, the directory $DOT_SAGE/matplotlib-0.99 will be created first but will remain empty and will never be used.  But I seem to have various subdirectories in $DOT_SAGE which I never pay attention to, so having one more doesn't seem like a big deal.


---

Comment by leif created at 2010-10-21 00:20:46

s/MPLCONFIGIDIR/MPLCONFIGDIR/ (minor; in the comment)

In principle, you can now omit the outer test (`if [ -f ... ]; then`) and simply redirect stderr to `/dev/null` inside the backquotes.

According to Dave, we no longer use variables for simple (POSIX) commands like `mkdir` and `cp` etc., but I don't mind.


---

Comment by jhpalmieri created at 2010-10-21 01:35:02

Replying to [comment:27 leif]:
> s/MPLCONFIGIDIR/MPLCONFIGDIR/ (minor; in the comment)

Fixed.

> In principle, you can now omit the outer test (`if [ -f ... ]; then`) and simply redirect stderr to `/dev/null` inside the backquotes.

Okay, but it also works this way, and seems readable to me this way, so I'm leaving it as is.

> According to Dave, we no longer use variables for simple (POSIX) commands like `mkdir` and `cp` etc., but I don't mind.

You're right, the scripts in local/bin use "mkdir", not "$MKDIR", so I've changed that, too.


---

Attachment

scripts repo


---

Comment by leif created at 2010-10-21 01:50:24

Ok, "dry" positive review. (Not yet tested, but should work and fix the issue). 

(Using also the second minor version number is certainly an overkill though.)


---

Comment by leif created at 2010-10-21 02:35:15

Tested with Sage 4.6.alpha3.

Also works after deletion of `$HOME/.sage/` (i.e., dirs get properly recreated s.t. MPL doesn't raise an error).

Replying to [comment:5 jason]:
> The problems in #9221 (I mistakenly said #9122 above) were fixed with a patch to the matplotlib spkg that has been applied upstream as well. The issue on this ticket still stands, but it is not urgent for #9221 anymore. 

Since this fixes MPL 1.0.0 (#9221) breaking other, older Sage installations, I'm increasing the priority.


---

Comment by leif created at 2010-10-21 02:35:15

Changing priority from minor to critical.


---

Comment by leif created at 2010-10-21 02:35:15

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-10-21 08:44:29

Changing priority from critical to blocker.


---

Comment by mpatel created at 2010-10-21 10:07:34

Resolution: fixed


---

Comment by jhpalmieri created at 2010-10-22 15:30:52

See #10154 for a follow-up: documenting Sage's use of MPLCONFIGDIR.


---

Comment by mpatel created at 2010-10-22 21:58:06

Justin Walker [reports](http://groups.google.com/group/sage-release/browse_thread/thread/daa80febef383120/328ebbaffc728a92#328ebbaffc728a92) a doctest failure in `doc/en/constructions/plotting.rst`:

```python
sage -t  -long -force_lib devel/sage/doc/en/constructions/plotting.rst
**********************************************************************
File "/Users/Sage/sage-4.6.alpha0/devel/sage-main/doc/en/constructions/plotting.rst", line 42:
    sage: f.plot()
Exception raised:
    Traceback (most recent call last):
      File "/Users/Sage/sage-4.6.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/Sage/sage-4.6.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/Sage/sage-4.6.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[7]>", line 1, in <module>
        f.plot()###line 42:
    sage: f.plot()
      File "/Users/Sage/sage-4.6.alpha0/local/lib/python/site-packages/sage/misc/displayhook.py", line 174, in displayhook
        print_obj(sys.stdout, obj)
      File "/Users/Sage/sage-4.6.alpha0/local/lib/python/site-packages/sage/misc/displayhook.py", line 142, in print_obj
        print >>out_stream, `obj`
      File "sage_object.pyx", line 101, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1341)
      File "/Users/Sage/sage-4.6.alpha0/local/lib/python/site-packages/sage/plot/plot.py", line 1080, in _repr_
        self.show()
      File "/Users/Sage/sage-4.6.alpha0/local/lib/python/site-packages/sage/plot/misc.py", line 84, in wrapper
        return func(*args, **kwds)
      File "/Users/Sage/sage-4.6.alpha0/local/lib/python/site-packages/sage/plot/plot.py", line 1727, in show
        self.save(DOCTEST_MODE_FILE, **options)
      File "/Users/Sage/sage-4.6.alpha0/local/lib/python/site-packages/sage/plot/plot.py", line 2388, in save
        figure=self.matplotlib(*args, **kwds)
      File "/Users/Sage/sage-4.6.alpha0/local/lib/python/site-packages/sage/plot/plot.py", line 1927, in matplotlib
        from matplotlib.figure import Figure, figaspect
      File "/Users/Sage/sage-4.6.alpha0/local/lib/python/site-packages/matplotlib/figure.py", line 18, in <module>
        from axes import Axes, SubplotBase, subplot_class_factory
      File "/Users/Sage/sage-4.6.alpha0/local/lib/python/site-packages/matplotlib/axes.py", line 18, in <module>
        import matplotlib.contour as mcontour
      File "/Users/Sage/sage-4.6.alpha0/local/lib/python/site-packages/matplotlib/contour.py", line 21, in <module>
        import matplotlib.texmanager as texmanager
      File "/Users/Sage/sage-4.6.alpha0/local/lib/python/site-packages/matplotlib/texmanager.py", line 72, in <module>
        class TexManager:
      File "/Users/Sage/sage-4.6.alpha0/local/lib/python/site-packages/matplotlib/texmanager.py", line 92, in TexManager
        os.mkdir(texcache)
    OSError: [Errno 17] File exists: '/Users/justin/.sage//matplotlib-1.0.0/tex.cache'
```



---

Comment by mpatel created at 2010-10-22 22:01:44

I wonder if Justin's error occured because matplotlib tried to create `tex.cache` in two or more "simultaneous" test processes.


---

Comment by jhpalmieri created at 2010-10-22 22:12:04

Replying to [comment:35 mpatel]:
> I wonder if Justin's error occured because matplotlib tried to create `tex.cache` in two or more "simultaneous" test processes.

That's just what I posted to sage-release.  The relevant lines in matplotlib/texmanager.py are

```
    if not os.path.exists(texcache):
        os.mkdir(texcache)
```

so that seems a likely explanation.


---

Comment by jhpalmieri created at 2010-10-23 18:35:40

See #10159 for a followup, dealing with the race condition.

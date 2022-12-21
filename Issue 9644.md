# Issue 9644: Make Sage run even when $SAGE_ROOT contains spaces

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-07-30 01:15:46

Assignee: jason

CC:  kcrisman leif ddrake schilly mvngu

Reported by Dan on [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/3694601bc3de1a80):

```
This is an observation about the pre-compiled binaries for Mac OS.

If the (unpacked) sage disk image directory is saved in a folder that has a
space character in its name, for example:

$HOME/Applications/my folder

Then sage will not load properly when the "sage" executable is clicked. The
terminal session begins, but the application doesn't load successfully.

Changing the parent directory name to "my_folder" resolved this issue.

While using space characters in directory names probably isn't all that common
in UNIX or Linux installations, it is more common in Mac OS installations.
Perhaps the installation instructions could be updated to mention this issue? 
```


This actually appears to be a more general problem:

```sh
$ hostname
sage.math.washington.edu
$ pwd
/mnt/usb1/scratch/mpatel/tmp/my sage
$ ./sage
Error setting environment variables by running /mnt/usb1/scratch/mpatel/tmp/my sage/local/bin/sage-env; possibly contact sage-devel (see http://groups.google.com/group/sage-devel).
cat: /bin/sage-banner: No such file or directory
mkdir: cannot create directory `': No such file or directory
cp: cannot create directory `/ipython': Permission denied
Traceback (most recent call last):
  File "./sage-cleaner", line 25, in <module>
    DOT_SAGE = os.environ['DOT_SAGE']
  File "/mnt/usb1/scratch/mpatel/tmp/my sage/local/lib/python2.6/UserDict.py", line 22, in __getitem__
    raise KeyError(key)
KeyError: 'DOT_SAGE'
**********************************************************************
Welcome to IPython. I will try to create a personal configuration directory
where you can customize many aspects of IPython's functionality in:

/ipython
Initializing from configuration /mnt/usb1/scratch/mpatel/tmp/my sage/local/lib/python2.6/site-packages/IPython/UserConfig
WARNING: 

There was a problem with the installation:
[Errno 13] Permission denied: '/ipython'
Try to correct it or contact the developers if you think it's a bug.
IPython will proceed with builtin defaults.
Please press <RETURN> to start IPython.
```



---

Comment by mpatel created at 2010-07-30 01:26:08

After applying 

```diff
diff --git a/sage-sage b/sage-sage
--- a/sage-sage
+++ b/sage-sage
`@``@` -127,7 +127,7 `@``@` usage_advanced() {
     exit 1
 }
 
-. $SAGE_ROOT/local/bin/sage-env   1>/dev/null 2>/dev/null
+. "$SAGE_ROOT/local/bin/sage-env"   1>/dev/null 2>/dev/null
 
 if [ $? -ne 0 ]; then
    echo "Error setting environment variables by running $SAGE_ROOT/local/bin/sage-env; possibly contact sage-devel (see http://groups.google.com/group/sage-devel)."
```

I get

```python
$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
ls: cannot access /mnt/usb1/scratch/mpatel/tmp/my: No such file or directory
ls: cannot access sage/devel/sage: Not a directory
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
| Sage Version 4.5.2.rc0, Release Date: 2010-07-28                   |
| Type notebook() for the GUI, and license() for information.        |
/mnt/usb1/scratch/mpatel/tmp/my sage/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)
     64         reload(sys.modules[modname])
     65     else:
---> 66         __import__(modname)
     67 
     68 

/mnt/usb1/scratch/mpatel/tmp/my sage/ipy_profile_sage.py in <module>()
     14     from sage.misc.interpreter import attached_files
     15 
---> 16     branch = sage.misc.misc.branch_current_hg_notice(sage.misc.misc.branch_current_hg())
     17     if branch:
     18         print branch

/mnt/usb1/scratch/mpatel/tmp/my sage/local/lib/python2.6/site-packages/sage/misc/misc.pyc in branch_current_hg()
   1877     i = s.rfind('->')
   1878     if i == -1:
-> 1879         raise RuntimeError, "unable to determine branch?!"
   1880     s = s[i+2:]
   1881     i = s.find('-')

RuntimeError: unable to determine branch?!
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.

sage: 
```



---

Comment by leif created at 2010-07-30 01:42:08

<flame>

*R T F M ! * ;-)

(Milestone Sage 6.0)

</flame>

It is well documented that `$SAGE_ROOT` (and therefore `$SAGE_LOCAL` *must not* contain spaces; I only wondered a few times if this is checked/catched anywhere, since almost all scripts (especially `spkg-install` scripts) blindly rely on this. So changing this (allowing spaces) is a big task, which is IMHO not worth doing now. It is _in general_ a bad idea to put spaces in _path_ names (filenames are a little different/less problematic).

-Leif


---

Comment by leif created at 2010-07-30 02:48:14

Ok, it could perhaps be documented in more prominent places, but it's (still) twice in `$SAGE_ROOT/README.txt`, the second time a bit to mild:

```
...
MORE DETAILED INSTRUCTIONS TO BUILD FROM SOURCE
-----------------------------------------------
...
3. Extract the Sage source tarball and cd into a directory with no
   spaces in it. [...]

...

RELOCATION
----------

You *should* be able to move the sage-x.y.z directory anywhere you
want. If you copy the sage script or make a symbolic link to it, you
should modify the script to reflect this (as instructed at the top of
the script). It is best if the path to Sage does not have any spaces in
it.
...
```


And afair it is (or at least has been at some time) better documented in the Installation Guide.

So I would open two tickets (one could be this with changed title):

 * Make sure `$SAGE_ROOT` does not contain spaces, e.g. in `sage-env` (blocker).

 * Improve documentation (CAPSLOCK? Add/move remarks to top of files.)


---

Comment by leif created at 2010-07-30 04:06:44

Ouch, I just realized the scripting "logic" is completely insane:

While `sage-env` is intended to be *sourced* (rather than called), and `sage-sage` does this,

 * `sage-sage` redirects stdout and stderr while sourcing `sage-env` to `/dev/null`, though `sage-env` eventually outputs (valuable) error messages
 * `sage-sage` tests its "exit status", though it is sourced, not called
 * `sage-env` actually *exits* with 1 on error

So even when an error is detected in `sage-env`, the user will never see the error message, but Sage will simply "silently" exit.

Argh...


---

Comment by leif created at 2010-07-30 04:42:51

With the attached patch I get:

```sh
leif`@`portland:~/Sage /sage-4.5.2.alpha0-j12$ ./sage
Error: The path to the Sage directory ($SAGE_ROOT) MUST NOT contain spaces.
It is currently "/home/leif/Sage /sage-4.5.2.alpha0-j12".
You must correct this by moving Sage (or renaming some directories) first.
Exiting now...
leif`@`portland:~/Sage /sage-4.5.2.alpha0-j12$ 
```

(Note the spaces in the path, I simply renamed a component of the path to my Sage directories.)


---

Comment by leif created at 2010-07-30 05:53:23

The error message could of course be a bit more friendly, for example:

  _"*Please* correct this by moving Sage (or renaming some directories) first."_


---

Comment by leif created at 2010-07-30 07:50:10

An alternative, perhaps simpler, but "less efficient" test for spaces would be:

```sh
    [ `echo "X${SAGE_ROOT}X" | wc -w` -ne 1 ]
```

(This one catches leading and trailing blanks, too, like the shell function in the patch when called properly. But we usually have leading and trailing slashs/path separators in `$SAGE_ROOT` anyway.)


---

Comment by drkirkby created at 2010-07-30 10:12:43

I know there was one bit of code in sage which removed one space, but not multiple ones. i.e. 


```
sed 's/ //' 
```


rather than 


```
sed 's/ //g'
```


I changed the one occurrence I spotted, but there might be others lucking. 

Of course, the best way to solve this is to not have any hacks like this, and just get Sage to build with spaces in paths. If things are quoted properly, this should be possible. 

Perhaps there should be an environment variable that can be used to bypass that hack which removes spaces. Then we could slowly find the packages that have problems and correct them one by one. Once they were all corrected, the hack could be removed and Sage would build on paths with spaces in them. 

Dave


---

Comment by leif created at 2010-07-30 14:13:37

Gives error message on spaces in $SAGE_ROOT. (Draft, but functional. Slightly more friendly.) Apply to scripts repo.


---

Attachment

We could require people who update/provide new spkgs to at least check if the upstream supports spaces in path names (I really doubt all will), and to harden the corresponding Sage scripts in that way. But I expect this to be a long lasting process, rather than a goal for any release in the nearer future.

And I have absolutely no idea which "inner" parts of Sage (i.e. Python code) might break on spaces in file or path names.

Of course users that only download and install binaries should somehow get informed, too, e.g. directly on the download page.


---

Comment by kcrisman created at 2010-07-30 15:39:16

> 
> Of course users that only download and install binaries should somehow get informed, too, e.g. directly on the download page.

And THAT was the point of the original post - that README.txt should probably also mention this issue for downloads, since he downloaded a *binary*.  

Anyway, I'm glad to see this wasn't a platform-specific issue.  Probably this ticket should get closed by fixing the manual and adding the error messages, as it were, and then one could open a sage-wishlist milestone ticket for supporting spaces in the path.  (The error message may also want to say that certain Sage components would fail otherwise? Or would that be too long?)


---

Comment by leif created at 2010-07-30 16:05:15

Changing status from new to needs_review.


---

Comment by leif created at 2010-07-30 16:05:15

Replying to [comment:11 kcrisman]:
> > 
> > Of course users that only download and install binaries should somehow get informed, too, e.g. directly on the download page.
> 
> And THAT was the point of the original post - that README.txt should probably also mention this issue for downloads, since he downloaded a *binary*.

Although the README.txt (and other scattered pieces of information) are rarely changed/current, I really thought this was a well-known issue, since I came across that in the documentation many times. (I think it once was better placed, s.t. nobody could miss it, though people tend to read READMEs and installation guides - if at all - _after_ they run into problems... ;-) )

> [...] Probably this ticket should get closed by fixing the manual and adding the error messages, as it were, and then one could open a sage-wishlist milestone ticket for supporting spaces in the path.

Yes, that's what I was thinking of, too.

> The error message may also want to say that certain Sage components would fail otherwise? Or would that be too long?

As long as it fits onto a 80x25 screen... Feel free to add a "reviewer patch" or make some suggestion and I'll update the patch. I'm quite sure then this could get into 4.5.2.

Someone volunteering for a revised README?

Harald, ideas for the web page?


---

Comment by leif created at 2010-07-30 16:28:39

Oh, perhaps the Makefile or `spkg/install` should get some early check, too.


---

Comment by schilly created at 2010-07-30 16:42:31

Well, it's possible to add anything somewhere on the webpage, but I think it doesn't look good, or is professional, to list bugs on a download page (especially because it is never read just like the readme).

I don't know the exact problem, but I'm for adding a check at the "sage" script itself -- ahh, i've just seen that above -- and to the early scripts when starting to build sage.


---

Comment by leif created at 2010-07-31 14:22:07

The [Installation Guide](http://www.sagemath.org/doc/installation/) definitely needs to be updated, too:

  _[...] Make sure there are no spaces in the directory name under which you build. Running from a directory with spaces in its name is supported but discouraged. Building is not possible, since several of the components do not build if there are spaces in the path. [...]_

(This snippet is actually from [_Steps to Install from Source_](http://www.sagemath.org/doc/installation/source.html#steps-to-install-from-source).)


---

Comment by mpatel created at 2010-08-01 09:33:37

An aside: For this special situation:

 1. Build Sage with no spaces in `SAGE_ROOT`.
 2. Rename `SAGE_ROOT` to contain space(s).

the patches [here](http://sage.math.washington.edu/home/mpatel/trac/9644) should get Sage to start and get `sage -b`, `sage -clone`, `sage -docbuild`, and `sage -t(p)` commands to work.  Except for some SYMPOW and GAP-related tests, the long doctests pass.  It's likely that fixing these components requires spkg updates.

I'm sure there are other problems to fix, and these patches certainly won't allow Sage to build with spaces in `SAGE_ROOT`.  But the exercise suggests that to fix most (all?) Python code, we should focus on system calls, e.g., `os.{popen*,system}`, `subprocess.{call,Popen}`, etc.  Of course, we can open other tickets for these changes.


---

Comment by mpatel created at 2010-08-20 08:31:38

Thanks, Leif.  I'd like to focus, for now, on releasing 4.5.3 and then on the PARI upgrade for 4.6.alpha0.  I'll try to work on this ticket after 4.5.3 is out.


---

Comment by leif created at 2010-08-20 11:24:22

Btw: If you want to have fun, try _compiling_ Sage with `-O2` contained in `$SAGE_ROOT`.

(It's `libgcrypt` that fails IIRC.)


---

Comment by jhpalmieri created at 2010-09-21 21:35:47

This looks good to me; positive review for "trac_9644-first_aid_for_spaces_in_SAGE_ROOT-scripts_repo.patch". Trying to get Sage to work with spaces in the path can go on another ticket.  Meanwhile, I'm attaching a patch for the installation guide.


---

Comment by drkirkby created at 2010-09-21 22:32:23

John's happy with Leif's patch. I'm happy with John's changes to the installation guide. So positive review.


---

Comment by drkirkby created at 2010-09-21 22:32:23

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-21 22:33:21

Thanks, everyone, for working on this.


---

Comment by leif created at 2010-09-21 23:07:16

So we are all happy. :)

Minor correction: Swap _from_ and _to_ in _"Another approach is to create a symbolic link ..."_.
(This has been in before. IIRC there are somewhere more instances of that, but never mind.)


---

Comment by jhpalmieri created at 2010-09-21 23:31:39

How about this?


---

Comment by leif created at 2010-09-21 23:37:10

Thanks, very good.


---

Comment by jhpalmieri created at 2010-09-22 18:48:37

The invocation of sage-env from the top-level makefile is causing errors.  On sage.math:

```
. local/bin/sage-env && sage-starts && ./sage -tp 0  -sagenb -long devel/sage/doc/common devel/sage/doc/en devel/sage/doc/fr devel/sage/sage 2>&1 | tee -a ptestlong.log
local/bin/sage-env: 70: Syntax error: Bad function name
make: *** [ptestlong] Error 2
```

On my mac:

```
. local/bin/sage-env && sage-starts && ./sage -tp 0  -sagenb -long devel/sage/doc/common devel/sage/doc/en devel/sage/doc/fr devel/sage/sage 2>&1 | tee -a ptestlong.log
local/bin/sage-env: line 77: `contains-spaces': not a valid identifier
make: *** [ptestlong] Error 2
```

On t2.math:

```
. local/bin/sage-env && sage-starts && ./sage -tp 0  -sagenb -long devel/sage/doc/common devel/sage/doc/en devel/sage/doc/fr devel/sage/sage 2>&1 | tee -a ptestlong.log
/bin/sh: contains-spaces: is not an identifier
make: *** [ptestlong] Error 1
```

In all cases, changing "contains-spaces" to "contains_spaces" seems to fix the problem.  I'm attaching a small patch to do this.  (On Solaris systems, I also see a new warning, presumably because we're not redirecting output to /dev/null: after typing "make ptestlong", I see

```
Build finished.  The built documents can be found in /scratch/palmieri/sage-4.5.3.rc0/devel/sage/doc/output/html/fr/a_tour_of_sage
. local/bin/sage-env && sage-starts && ./sage -tp 0  -sagenb -long devel/sage/doc/common devel/sage/doc/en devel/sage/doc/fr devel/sage/sage 2>&1 | tee -a ptestlong.log
/bin/sh: source: not found
Testing that Sage starts...
Yes, Sage starts.
Testing that Sage starts...
Yes, Sage starts.
Global iterations: 1
File iterations: 1
```

Note the line `/bin/sh: source: not found`.  Is this important?  If so, we should deal with it on another ticket...)


---

Comment by jhpalmieri created at 2010-09-22 18:48:37

Changing status from positive_review to needs_work.


---

Comment by jhpalmieri created at 2010-09-22 18:48:46

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-09-22 20:32:47

Thanks, I wanted to make exactly the same change weeks ago... (replacing the dash in the name by an underscore).

Also, `source` should be replaced by `.` (period). (At #9960 or here.)

(Note that this error message has always been there; you just had to look into `/dev/null`... ;-) Redirecting `stderr` to Nirvana is rarely a good idea.)

----

Although the Makefile shouldn't break the assumption that we're using `bash`; so either `sage-env` should be removed there, or the line should be `bash -c ...`, or `/usr/bin/env bash -c ...`. There are various ways to fix that.

I wonder if `sage-starts` shouldn't use `bash` (instead of `sh`) and itself source `sage-env`; then we could drop `. local/bin/sage-env &&` from `TESTPRELIMS`. (This would IMHO be cleaner.)


---

Comment by drkirkby created at 2010-09-22 20:39:08

The changes look fine. 

The `/bin/sh: [`](../tree/master/`) is quite a common error. We should not solve it by redirecting stderr to /dev/null, but removing the word `source` and replacing it with a dot. I suspect there are many instances of this lucking around. The problem is the command does not exist in `/bin/sh` but does in `bash` See below. 

Here my default shell is `bash`, so `source` exists as a built in shell command. 

```
kirkby`@`t2:64 ~$ source
-bash: source: filename argument required
source: usage: source filename [arguments]
```


Now change my shell to /bin/sh


```
kirkby`@`t2:64 ~$ sh
$ source
source: not found
$ 
```


I'd prefer to use the more portable `.` (dot) which will achieve the same, but is not a bashism. These should certainly be addressed on another ticket. The fact they  are not producing any known errors, makes me wonder how important it is to source the files in the first place!


---

Comment by drkirkby created at 2010-09-22 20:39:08

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-09-22 21:06:10

Sourcing `sage-env` in the Makefile is only needed to set up `SAGE_ROOT` for `sage-starts`, which calls a Python script (`sage-location`).

The other Sage scripts source `sage-env` themselves.

As said before, best would be to change `sage-starts` (and the Makefile) on another ticket; replacing `source` by `.` could be done at #9960 I think.

An even nicer solution would just "source" `sage-env` from the _Python_ script (by invoking a shell that does this and echoes the necessary variables), also removing `. sage-env &&` from the Makefile.


You can hardly touch a piece of Sage without experiencing other things to fix... ;-)


---

Comment by mpatel created at 2010-09-29 07:01:32

Could someone please update the commit strings of the "installation" and "ref" patches to be a bit more descriptive and restore the positive review?


---

Comment by mpatel created at 2010-09-29 07:01:42

Changing status from positive_review to needs_work.


---

Attachment

apply on top of other scripts patch


---

Comment by jhpalmieri created at 2010-09-29 16:48:40

Here are new commit strings.  Can we restore the positive review now?


---

Comment by jhpalmieri created at 2010-09-29 16:48:40

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-09-29 21:08:49

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-29 21:08:49

Thanks!


---

Comment by leif created at 2010-09-29 21:49:59

I've updated some Wiki pages a while ago.

Harald said we shouldn't "announce bugs" on the download pages; I think a simple comment on where to currently not install Sage shouldn't be interpreted as such.


---

Comment by mpatel created at 2010-09-29 23:36:41

Resolution: fixed

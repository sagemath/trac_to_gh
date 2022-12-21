# Issue 8679: conventions for spkg names, rewriting sage-spkg

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-04-12 21:21:49

Assignee: tbd

CC:  ddrake mvngu

Some scripts in SAGE_ROOT/local/bin expect spkg names to have the form 

```
my_package-2.3.spkg
```

but not 

```
my-package-2.3.spkg   (first hyphen is bad)
```

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/8597ce93b420afe4) for some discussion.

The attached patches do three things:

 - Rewrite sage-pkg (in python instead of bash) to test whether the name has the right form.
 - Remove sage-pkg-nocompress, using sage-pkg instead (and thus unifying the two scripts sage-pkg and sage-pkg-nocompress).
 - Add some comments about this to the developer's guide (hence the cc for mvngu).

I used python because in the old version of sage-pkg, we were already calling sed and perl, and we might need to call perl again (or something else?) to test whether the name has the right form.  It seems easier to maintain if it's all plain Python.

Here is the standard being suggested by this patch: each Sage spkg should have a name of the following form:

```
BASENAME-VERSION.spkg
```

where BASENAME may lowercase letters, numbers, and underscores, but *no hyphens*.  VERSION *must be present* and *should start with a number*; it may contain numbers, letters, dots, and hyphens; it may end in a string of the form "pNUM", where "NUM" is a non-negative integer.  The new version of sage-pkg sets BASENAME to be everything up to the first hyphen, but it does not check to make sure only numbers, lowercase letters, and underscores are used.  It checks that VERSION is present, starts with a number, and contains only numbers, letters, periods, hyphens.  If not, it prints a warning and creates an spkg anyway.

I've tried to implement the change at #2522, but I'm not sure how to test it.  Any suggestions?  What sort of "OS X junk" should I try to put in my directory, to make sure it is not put into the resulting spkg file?


---

Comment by jhpalmieri created at 2010-04-12 21:23:12

sage repo (documentation)


---

Attachment


---

Comment by jhpalmieri created at 2010-04-12 21:59:11

Changing status from new to needs_review.


---

Comment by was created at 2010-04-13 04:30:04

* I read trac_8679-sage.patch and it looks wonderful!!

* trac_8679-scripts.patch will of course probably cause some other patches to need rebases. 

-- So to finish a review, trac_8679-sage.patch needs to be tested:

1. make an spkg

2. make a non-compressed spkg

3. Do a full build of all of sage.

Anything else?

If somebody (e.g., me) reports the above works, then I would give this a positive review.

And moving to Python is *great*, since now we can use this script in other scripts, and option parsing is done right.


---

Comment by ddrake created at 2010-04-13 12:25:27

I applied the scripts patch, unpacked the fortran spkg, and tried "sage -pkg_nc fortran-...". It didn't go so well:


```
Creating Sage package fortran-20100118 with no compression
Traceback (most recent call last):
  File "/home/drake/s/trac8679/sage-4.3.5/local/bin/sage-pkg", line 130, in <module>
    main()
  File "/home/drake/s/trac8679/sage-4.3.5/local/bin/sage-pkg", line 81, in main
    tar_file(dir, no_compress = options.no_compress)
  File "/home/drake/s/trac8679/sage-4.3.5/local/bin/sage-pkg", line 36, in tar_file
    tar = tarfile.open(file, mode=mode)
  File "/home/drake/s/trac8679/sage-4.3.5/local/lib/python/tarfile.py", line 1682, in open
    return cls.taropen(name, mode, fileobj, **kwargs)
  File "/home/drake/s/trac8679/sage-4.3.5/local/lib/python/tarfile.py", line 1692, in taropen
    return cls(name, mode, fileobj, **kwargs)
  File "/home/drake/s/trac8679/sage-4.3.5/local/lib/python/tarfile.py", line 1519, in __init__
    fileobj = bltn_open(name, self._mode)
TypeError: coercing to Unicode: need string or buffer, type found
```

I think you never defined what "file" is in your "tarfile.open" call.


---

Comment by ddrake created at 2010-04-13 12:25:27

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-04-13 18:19:59

Replying to [comment:4 ddrake]:

> I think you never defined what "file" is in your "tarfile.open" call.

Oops, you're right.  (The tar_file function used to be part of "main", so "file" was defined there.)

Here's a new patch; it just changes `file` to `"%s.spkg" % dir`.


---

Comment by jhpalmieri created at 2010-04-13 18:19:59

Changing status from needs_work to needs_review.


---

Attachment

scripts repo


---

Comment by leif created at 2010-04-13 18:32:58

Funny thing. I'd rather change the _code_ to reflect the common practice of using dashes in package names, i.e. taking the leftmost substring that _starts with a digit_ (and of course is preceded by a hyphen) as the package version part.

IMHO code that's unable to deal with dashes in package names is bad and should be fixed, not the names. We shouldn't introduce or keep restrictions that aren't really necessary, not only but especially if they rule out what's widely used.

-Leif


---

Comment by jhpalmieri created at 2010-04-13 18:51:57

Replying to [comment:6 leif]:
> Funny thing. I'd rather change the _code_ to reflect the common practice of using dashes in package names, i.e. taking the leftmost substring that _starts with a digit_ (and of course is preceded by a hyphen) as the package version part.
> 
> IMHO code that's unable to deal with dashes in package names is bad and should be fixed, not the names. We shouldn't introduce or keep restrictions that aren't really necessary, not only but especially if they rule out what's widely used.

First of all, what's widely used _in Sage_ is the convention here: everything after the first hyphen is the version number.  Look at the names of the standard spkgs to see this.

Second, you might be right, but this is not the right place to discuss design decisions like this: sage-devel is.

Third, this is an issue which will only arise for developers -- people producing new spkgs -- and they should be able to handle using hyphens or underscores according to the conventions.  So it's not a big deal.


---

Comment by leif created at 2010-04-13 22:43:32

Replying to [comment:7 jhpalmieri]:
> First of all, what's widely used _in Sage_ is the convention here
Well, I didn't talk about common _spkg_ names (of course they follow the old rule).
Note that many spkgs are patched upstream packages, so their (original) names won't necessarily follow _Sage's_ naming convention; there are indeed yet packages that had to be renamed.

> Second, you might be right, but this is not the right place to discuss design decisions like this: sage-devel is.
The thread "ends" with a link to this ticket, whose description (re-)states the convention, while the thread's title only mentions the _mode_ package;
but never mind, I'll repost it there. ;-)

> Third, this is an issue which will only arise for developers -- people producing new spkgs -- and they should be able to handle using hyphens or underscores according to the conventions.
I think there's (with intent) no sharp line between Sage developers/contributors/users; think of optional "third party" (s)pkgs.


---

Comment by ddrake created at 2010-04-14 03:23:06

Replying to [comment:3 was]:
> -- So to finish a review, trac_8679-sage.patch needs to be tested:
> 
> 1. make an spkg
> 
> 2. make a non-compressed spkg
> 
> 3. Do a full build of all of sage.

I'm doing a full build of Sage right now. I took all the spkgs in spkg/standard, extracted them, and re-made them with "sage -pkg" (and "sage -pkg_nc") after applying the patch here. I'll report the results of the build, although so far it seems fine.


---

Comment by ddrake created at 2010-04-14 08:07:32

Replying to [comment:9 ddrake]:
> I'm doing a full build of Sage right now. I took all the spkgs in spkg/standard, extracted them, and re-made them with "sage -pkg" (and "sage -pkg_nc") after applying the patch here. I'll report the results of the build, although so far it seems fine.

The build went fine and all tests pass, so the new script produces spkgs that work perfectly well.

Just as an idea, would it make sense to have "sage -pkg" add checksums, as in #329?


---

Comment by jhpalmieri created at 2010-04-14 17:31:44

Replying to [comment:10 ddrake]:
> Just as an idea, would it make sense to have "sage -pkg" add checksums, as in #329?

I think that sounds good, but it belongs on another ticket.

By the way, I also applied this patch and then ran "sage -sdist" and built Sage from the resulting tar file without problems.


---

Comment by ddrake created at 2010-04-15 01:08:08

Replying to [comment:11 jhpalmieri]:
> Replying to [comment:10 ddrake]:
> > Just as an idea, would it make sense to have "sage -pkg" add checksums, as in #329?
> 
> I think that sounds good, but it belongs on another ticket.

Oh, of course. I've created #8690 for that.

It seems we've met William's criteria for a positive review. I've created some spkgs (in Linux and OS X) with this patch applied, and everything works properly. I think we can call this a positive review.


---

Comment by ddrake created at 2010-04-15 01:08:08

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-15 01:21:45

Replying to [comment:8 leif]:
> Replying to [comment:7 jhpalmieri]:
> > First of all, what's widely used _in Sage_ is the convention here
> Well, I didn't talk about common _spkg_ names (of course they follow the old rule).
> Note that many spkgs are patched upstream packages, so their (original) names won't necessarily follow _Sage's_ naming convention; there are indeed yet packages that had to be renamed.
> 
> > Second, you might be right, but this is not the right place to discuss design decisions like this: sage-devel is.
> The thread "ends" with a link to this ticket, whose description (re-)states the convention, while the thread's title only mentions the _mode_ package;
> but never mind, I'll repost it there. ;-)
> 
> > Third, this is an issue which will only arise for developers -- people producing new spkgs -- and they should be able to handle using hyphens or underscores according to the conventions.
> I think there's (with intent) no sharp line between Sage developers/contributors/users; think of optional "third party" (s)pkgs.

jhpalmieri's patch rewrites an existing script with no changes in semantics, except to give an error if the package name breaks other parts of the Sage build system.  I think it should go in as is.  

Your suggestions to change the package naming convention is reasonable consider.  However, I think that should be done independently of this particular ticket.  Keeping focus on one issue at a time is really important in order to make solid progress.


---

Comment by leif created at 2010-04-15 02:04:30

Replying to [comment:13 was]:
> jhpalmieri's patch rewrites an existing script with no changes in semantics, except to give an error if the package name breaks other parts of the Sage build system.  I think it should go in as is.  

I didn't want to blame John's work nor give it a negative review.

Relaxing the naming convention of course requires locating the code parts that (currently can't) deal with such names, so if at all tbd in another ticket.


---

Comment by jhpalmieri created at 2010-04-16 18:57:09

Merged in 4.4.alpha0:
 - trac_8679-sage.patch
 - trac_8679-scripts.patch


---

Comment by jhpalmieri created at 2010-04-16 18:57:09

Resolution: fixed

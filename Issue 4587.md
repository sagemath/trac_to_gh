# Issue 4587: [with patch, needs review] Installation of the latest version of a package

Issue created by migration from https://trac.sagemath.org/ticket/4587

Original creator: SimonKing

Original creation time: 2008-11-23 01:01:01

Assignee: mabshoff

Keywords: installing package latest version

William wrote at http://groups.google.com/group/sage-devel/browse_thread/thread/de91554d761c5f1b?hl=en

''I think nobody every implemented a "install latest version of package foo" 
yet for Sage.  That's been on the todo list for *years*. ''

It is not difficult to implement, using the existing functtions from sage.misc.package, namely `install_package` and `optional_package` etc.

I implemented a function `install_latest_version` in `package.py` and included it in `all.py`.

Now, one can install the optional pil-1.1.6 package with

```
sage: install_latest_version('pi')
```

Repeating the command yields the Traceback

```
ValueError                                Traceback (most recent call last)
...
ValueError: There is no uninstalled package whose name starts with 'pi'.
```

Forced re-installation is then possible with

```
sage: install_latest_version('pi',forced=True)
```


If there is no possible package name extension, a Traceback results. There is also a Traceback if the extension is not unique. In that case, before raising the error, a list of all possible extensions is shown.

```
sage: install_latest_version('p',forced=True)
Possible packages are:
  palp-1.1.p1
  pari-2.3.3.p0
  pexpect-2.0.p1
  polybori-0.5rc.p5
  polytopes_db-20080430
  pycrypto-2.0.1.p2
  pygments-0.11.1
  pynac-0.1.1
  pyprocessing-0.52
  python-2.5.2.p8
  python_gnutls-1.1.4.p3
  pil-1.1.6
...
ValueError: There is more than one package name starting with 'p'. Please specify!
```


Or should this function not raise an error?

Unfortunately I have no idea how to have a non-destructive doc-test. Certainly it'd not be acceptable to have a doc-test installing something.


Unfortunately, I have no idea how a non-destructive doc-test may look like. Certainly it would hardly be acceptable to have a doc-test that installs something.


---

Comment by was created at 2008-11-23 21:53:44

> Unfortunately, I have no idea how a non-destructive doc-test may look like. Certainly > it would hardly be acceptable to have a doc-test that installs something. 

We could have an official "test" spkg.  And it would be marked

```
optional -- admin
```

meaning one must have write privileges to the sage install in order to run it.
The test would install and uninstall that package.

William


---

Comment by SimonKing created at 2008-11-23 22:50:11

Replying to [comment:1 was]:
> We could have an official "test" spkg.  And it would be marked
> {{{
> optional -- admin
> }}}
> meaning one must have write privileges to the sage install in order to run it.
> The test would install and uninstall that package.

Sorry, at that point I have to pass out. So far, I did not produce a new package (hopefully I'll learn it soon), and also I don't how one can un-install a package.


---

Comment by SimonKing created at 2008-11-25 12:14:42

Replying to [comment:1 was]:
> We could have an official "test" spkg.  And it would be marked
> {{{
> optional -- admin
> }}}
> meaning one must have write privileges to the sage install in order to run it.
> The test would install and uninstall that package.

Another idea: Call the test package `tomato.spkg`, and construct it such that the attempt to install it would actually have no effect. 

Hence, there were no need to mark it `optional -- admin`, and also no need to uninstall it. 

That package would just comprise a Makefile with the simple content

```
all:
    echo "Tomato ejects itself"
```


Would it work? At least it would be rather "pythonic"...

Cheers,
     Simon


---

Comment by mabshoff created at 2008-11-25 12:19:17

Please open a ticket for a test-dummy.spkg and I will provide one. Uninstalling spkg per see is not really supported at the moment, but we can delete the entry from $SAGE_ROOT/spkg/installed/ manually.

Cheers,

Michael


---

Comment by SimonKing created at 2008-11-25 12:56:34

Replying to [comment:4 mabshoff]:
> Please open a ticket for a test-dummy.spkg and I will provide one. Uninstalling spkg per see is not really supported at the moment, but we can delete the entry from $SAGE_ROOT/spkg/installed/ manually.

Done, see #4617.

Cheers,
   Simon


---

Comment by was created at 2008-11-27 18:46:22

REFEREE REPORT:

I don't love the design, but a small change could fix it so I would like it.

Can you change it so install_latest_version is *not* exported to the global namespace.  Instead, if one calls install_package('...') with an input that doesn't contain a dash (i.e., doesn't contain any version number), then install_package simply calls install_latest_version.

The whole reason you wrote install_latest_version is because install_package is just really incompletely implemented, so just use it to implement the rest of install_package, and don't add more to the global namespace. 

William


---

Comment by SimonKing created at 2008-11-28 14:19:04

Dear William,

I removed the `install_latest_version`, so the global name space is not further polluted. Instead, I moved the code into `install_package`. 

So, now, `install_package` first tests whether there is a unique package name that starts with the given string (Note: This is done regardless whether it contains a dash or not. I hope this is not a problem). If there is a unique package, it is installed.

If the optional parameter 'forced' is not used, then it is only tried to find the package name among those packages that are not installed. In that way, an unintentional re-install is impossible.

I guess there will be no doc-test unless someone produces a `test_dummy.spkg`


---

Attachment

install_package: If there is a unique package starting with a given string, it gets installed


---

Comment by SimonKing created at 2008-11-28 23:07:38

Fortunately you didn't review the patch that I had submitted a few hours ago. I was in a hurry, didn't test it, and had a mistake... 

But the current patch does what I announced. My tests: 
 * I have pil installed. When I did `install_package('pil')`, it said that there is no package with that name (perhaps it would be better to say 'no uninstalled package').
 * Doing `install_package('pil',True)` did a re-install.
 * Doing `install_package('p')` showed a list of possible extensions and raised an error.

What do you think:
 1. Is it ok that an error is raised if there is no (resp. no not-yet-installed) package?
 2. Is it ok that an error is raised if the package name is not unique, or should simply the list be returned?


---

Comment by was created at 2008-11-28 23:48:50

REFEREE REPORT:

The logic is now somewhat broken, unfortunately.  E.g.,

```
sage: install_package('database_sloane')
... it works ...
```

but then

```
sage: install_package('database_sloane')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/was/build/sage-3.2.1.alpha1/<ipython console> in <module>()

/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/misc/package.pyc in install_package(package, force)
     78         raise ValueError, "There is more than one package name starting with '%s'. Please specify!"%(package)
     79     if len(L)==0:
---> 80         raise ValueError, "There is no package name starting with '%s'."%(package)
     81     os.system('sage -f "%s"'%(L[0]))
     82     __installed_packages = None

ValueError: There is no package name starting with 'database_sloane'.

sage: install_package('database_sloane_oeis-2005-12')
same error as above.
```

which is the wrong error message.


---

Comment by SimonKing created at 2008-11-28 23:59:14

Replying to [comment:9 was]:
> REFEREE REPORT:
> 
> The logic is now somewhat broken, unfortunately.  E.g.,
> ValueError: There is no package name starting with 'database_sloane'.

Yep, this is what I meant when I said in my previous comment "(perhaps it would be better to say 'no uninstalled package')".

The logic is:
 * If force and there is a unique package then install it (regardless whether it is already installed or not)
 * If (not force) and there is a unique _non-installed_ package then install it.
 * Otherwise, raise an error.

I agree that the error message may be clearer. So, back at work...


---

Attachment

To be applied after the first patch: Improving the error message


---

Comment by SimonKing created at 2008-11-29 00:21:42

After applying the second patch:
If the name is non-unique, I get with force install:

```
sage: install_package('p',True)
Possible package names starting with 'p' are:
  palp-1.1.p1
  ...
  pyx-0.8.1
ValueError: There is more than one package name starting with 'p'. Please specify!
```

and without force:

```
sage: install_package('p')
Possible names of non-installed packages starting with 'p':
  phc-2.3.39.p0
  ...
  pyx-0.8.1
ValueError: There is more than one package name starting with 'p'. Please specify!
```


If the package exists, without 'force' I get:

```
sage: install_package('pil')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: Package is already installed. Try install_package('pil',force=True)
```


Is this better?

Remains the doc-test issue. I leave it up to you whether one should wait for the test_dummy.spkg, so, I keep the summary [with patch, needs work].


---

Comment by was created at 2008-11-29 03:20:57

> Remains the doc-test issue. I leave it up to you whether one should wait for the 
> test_dummy.spkg, so, I keep the summary [with patch, needs work]. 

For this sort of thing, I'm not too worried.  100% coverage is critical in cases when it is at least reasonably straightforward how to write the doctests.  Here it is itself pretty confusing.


---

Comment by was created at 2008-11-29 03:26:40

Looks great!!


---

Comment by mabshoff created at 2008-11-29 04:19:42

Merged both patches in Sage 3.2.1.rc0


---

Comment by mabshoff created at 2008-11-29 04:19:42

Resolution: fixed

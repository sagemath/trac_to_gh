# Issue 5994: singular.version() yields an error when first called, has no doctest, and has a strange output imo

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2009-05-06 09:46:52

Assignee: was

CC:  kedlaya

Keywords: singular version

First of all, `singular.version()` does not work. When one starts sage and calls it, there is an error:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: singular.version()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (795, 0))
| Sage Version 3.4.1, Release Date: 2009-04-21                       |
| Type notebook() for the GUI, and license() for information.        |
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/SimonKing/.sage/temp/sage.math.washington.edu/10897/_home_SimonKing__sage_init_sage_0.py in <module>()

/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in version(self)
   1012         EXAMPLES:
   1013         """
-> 1014         return singular_version()
   1015
   1016     def _function_class(self):

/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in singular_version()
   1807     EXAMPLES:
   1808     """
-> 1809     return singular.eval('system("--version");')
   1810
   1811

/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in eval(self, x, allow_semicolon, strip, **kwds)
    541
    542         if s.find("error") != -1 or s.find("Segment fault") != -1:
--> 543             raise RuntimeError, 'Singular error:\n%s'%s
    544
    545         if get_verbose() > 0:

RuntimeError: Singular error:
   ? cannot open `help.cnf`
Singular for x86_64-Linux version 3-0-4 (3044-2009031122)  Mar 11 2009 22:29:08
with
        factory(`@`(#) factoryVersion = 3.0.4),libfac(3.0.4,Mar 2008),
        GMP(4.2),NTL(5.4.2),static readline,Plural,DBM,
        namespaces,dynamic modules,dynamic p_Procs,OM_CHECK=0,OM_TRACK=0,random=1241602325
        CC= gcc -O3 -g -fPIC -pipe -DNDEBUG -DOM_NDEBUG -Dx86_64_Linux -DHAVE_CONFIG_H,
        CXX= g++ -O3 -g -fPIC -pipe -DNDEBUG -DOM_NDEBUG -Dx86_64_Linux -DHAVE_CONFIG_H (4.2.4 (Ubuntu 4.2.4-1ubuntu3))
argv[0]   :     Singular-3-0-4
SearchPath:     /usr/local/sage/local/LIB
Singular  :     /usr/local/sage/local/bin/Singular-3-0-4
BinDir    :     /usr/local/sage/local/bin
RootDir   :     /usr/local/sage/local
DefaultDir:     /usr/local/sage/local
InfoFile  :
IdxFile   :
HtmlDir   :
ManualUrl :     http://www.singular.uni-kl.de/Manual/3-0-4
ExDir     :
Path      :     /usr/local/sage/local/bin:/usr/local/sage/local/polymake/bin:/usr/local/sage:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
EmacsDir  :
Available HelpBrowsers: dummy, emacs,
Current HelpBrowser: dummy
   ? error occurred in STDIN line 3: `system("--version");`
```


Secondly, neither `singular.version` nor `singular_version` have doc tests.

Thirdly, if it is called again, it kind of works:

```
sage: singular.version()
'Singular for x86_64-Linux version 3-0-4 (3044-2009031122)  Mar 11 2009 22:29:08\nwith\n\tfactory(`@`(#) factoryVersion = 3.0.4),libfac(3.0.4,Mar 2008),\n\tGMP(4.2),NTL(5.4.2),static readline,Plural,DBM,\n\tnamespaces,dynamic modules,dynamic p_Procs,OM_CHECK=0,OM_TRACK=0,random=1241602325\n\tCC= gcc -O3 -g -fPIC -pipe -DNDEBUG -DOM_NDEBUG -Dx86_64_Linux -DHAVE_CONFIG_H,\n\tCXX= g++ -O3 -g -fPIC -pipe -DNDEBUG -DOM_NDEBUG -Dx86_64_Linux -DHAVE_CONFIG_H (4.2.4 (Ubuntu 4.2.4-1ubuntu3))\nargv[0]   :\tSingular-3-0-4\nSearchPath:\t/usr/local/sage/local/LIB\nSingular  :\t/usr/local/sage/local/bin/Singular-3-0-4\nBinDir    :\t/usr/local/sage/local/bin\nRootDir   :\t/usr/local/sage/local\nDefaultDir:\t/usr/local/sage/local\nInfoFile  :\t\nIdxFile   :\t\nHtmlDir   :\t\nManualUrl :\thttp://www.singular.uni-kl.de/Manual/3-0-4\nExDir     :\t\nPath      :\t/usr/local/sage/local/bin:/usr/local/sage/local/polymake/bin:/usr/local/sage:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games\nEmacsDir  :\t\nAvailable HelpBrowsers: dummy, emacs, \nCurrent HelpBrowser: dummy '
```


Finally, I believe that the output of `singular.version` is nasty. If I ask for the version of Singular, I expect to get, say, a tuple of integers, for example:

```
sage: def my_singular_version():
....:     return tuple([Integer(x) for x in singular.eval('system("version")')])
....:
sage: my_singular_version()
(3, 0, 4, 4)
```


I suggest to remake `singular.version` so that it returns a tuple of integers, rather than a cryptic string.

Problem though: Would this break code?


---

Comment by SimonKing created at 2009-05-06 09:57:22

Remark:

Apparently the problem is on the side of Singular.

In Singular, freshly started, when you do

```
> system("--version");
```

there is the error (it says "? cannot open `help.cnf`"). 
If you repeat, no error.

If people think that my suggestion would break code, I suggest to have a new method `singular.version_number()`.


---

Comment by SimonKing created at 2009-05-06 12:15:18

Replying to [comment:1 SimonKing]:
> Apparently the problem is on the side of Singular.

And meanwhile it is reported upstream. 

I do not know, however, if the problem still occurs with Singular 3-1-0 (I only have a beta version, and this still shows the error).


---

Comment by SimonKing created at 2009-05-06 12:33:31

Replying to [comment:2 SimonKing]:
> Replying to [comment:1 SimonKing]:
> And meanwhile it is reported upstream. 
> 
> I do not know, however, if the problem still occurs with Singular 3-1-0 (I only have a beta version, and this still shows the error).

"Upstream" answered, and it seems that the problem is fixed in the official release. 

I could verify that on the server in Oberwolfach, the error does not occur in Singular 3-1-0, but it _does_ occur in Oberwolfach in Singular 3-0-4 (as being part of Sage). Opinions?

But there still remains the question if `singular.version()` ought to return a tuple of integers, rather than a lengthy string with all build informations.


---

Comment by AlexGhitza created at 2009-05-06 12:57:34

Replying to [comment:3 SimonKing]:
> 
> "Upstream" answered, and it seems that the problem is fixed in the official release. 
> 
> I could verify that on the server in Oberwolfach, the error does not occur in Singular 3-1-0, but it _does_ occur in Oberwolfach in Singular 3-0-4 (as being part of Sage). Opinions?

We can probably wait until after Sage Days 15 for this?
 
> But there still remains the question if `singular.version()` ought to return a tuple of integers, rather than a lengthy string with all build informations.

My personal preference would be for it to return a tuple of integers, but we could give it an optional argument `with_build_info=True` (or `verbatim=True` or something similar) to make it return the lengthy string.


---

Comment by SimonKing created at 2009-05-06 13:48:14

Replying to [comment:3 SimonKing]:
> I could verify that on the server in Oberwolfach, the error does not occur in Singular 3-1-0, but it _does_ occur in Oberwolfach in Singular 3-0-4 (as being part of Sage). Opinions?

The "Opinions?" bit should be two lines lower. Sorry.

It turned out that the error occurs in _any_ *_Sage-built*_ Singular version that I know: Singular 3-0-4 on sage.math, on two of my computers, in Oberwolfach, and Singular 3-1-0-Beta on sage.math and on one of my computers. 

If Singular is not built by Sage, then the error apparently does not occur: With Singular 3-0-3 (very old) on one of my machines, Singular-3-1-0-Beta on my machine (same sources, modulo the usual patches, as the sage-built version!), and Singular-3-1-0 official release in Oberwolfach.

So, after all, it seems to me that it is all Sage's fault.


> But there still remains the question if `singular.version()` ought to return a tuple of integers, rather than a lengthy string with all build informations.

Here is where I want to know some "Opinions"...


---

Comment by was created at 2010-01-18 13:05:31

Changing status from new to needs_review.


---

Comment by was created at 2010-01-18 13:05:31

The attached patch fixes the output format for version to be more consistent with the other interfaces, e.g., `gp.version()`.  It also programs around the issue with help files, which is *not* fixed in Singular-3-1-0... and I'm not at all clear *why* it is considered a bug in Singular by the people in the thread above.


---

Attachment

Replying to [comment:6 was]:
> It also programs around the issue with help files, which is *not* fixed in Singular-3-1-0... and I'm not at all clear *why* it is considered a bug in Singular by the people in the thread above.  

Note that I originally thought that the issue with help files is a problem of Singular, and clearly a bug: I mean, you ask for the version number and get an error; you ask again, and it works! It had reported it upstream.

But then the impression came across (see my last post) that it only occurs in Singular if it is built by Sage. In this case, it could be a problem with the patched version in Sage, which might be worth another ticket.

Cheers,
Simon


---

Comment by was created at 2010-01-18 22:28:31

I think the first time you ask for the version, singular fires up its help system, and reports a bug about it not being properly configured by *us* for such use.  Then it doesn't report that again, since it already did.  I think it is very sensible behavior by Singular.

So can you review this?


---

Comment by wjp created at 2010-01-19 04:32:12

For the record, adding an empty `$SAGE_ROOT/local/share/singular/help.cnf` suppresses the error. There is actually a `help.cnf` file in the singular sources (, but it doesn't seem to get installed. Its contents don't look to be particularly relevant for sage at first glance, though.


---

Comment by SimonKing created at 2010-01-19 09:23:54

Replying to [comment:8 was]:
> So can you review this?

I'd like to, but the sage-4.3.1.alpha1 that I had built on sage-math seems broken. It used to work, but when I did `./sage -br main`, it failed with 

```
ImportError: /usr/lib/libstdc++.so.6: version `GLIBCXX_3.4.11' not found (required by /home/SimonKing/SAGE/sage-4.3.1.alpha1/local/lib/libgmpxx.so.3)
```


Might `./sage -ba` work?

Anyway, I'd like to see one more doc test, that checks consistency with another way of getting the version number -- just for consistency:

```
sage: tuple([Integer(c) for c in singular.eval('system("version")')][:3] == singular.version()[0]
True
```



---

Comment by SimonKing created at 2010-01-19 09:56:03

Replying to [comment:10 SimonKing]:
> ...
> {{{
> sage: tuple([Integer(c) for c in singular.eval('system("version")')][:3] == singular.version()[0]
> True
> }}}

Oops, apparently I forgot a closing bracket on the left hand side. Anyway, you know what this prospective doc-test is supposed to do...


---

Comment by SimonKing created at 2010-01-19 10:20:22

Replying to [comment:10 SimonKing]:
> 
> Might `./sage -ba` work?
> 

It did not work. I fear that I have to start from scratch, so that it will take some hours before I will be able to review the patch.


---

Comment by SimonKing created at 2010-01-19 15:30:10

Changing status from needs_review to needs_info.


---

Comment by SimonKing created at 2010-01-19 15:30:10

OK, meanwhile I built sage-4.3.1.rc1

The patch applies cleanly.

However, I don't like the doc tests, and I think the return value is wrong.

The tests check that the first version number is 3. OK, it will eventually change, but not in the near future. 

Then they test that the version number is of length 3. Can we rely on it? There used to be two-digit versions. 

In fact, the "official" version number seems to be four digits, not three:

```
sage: singular.eval('system("version")')
'3104'
```


Hence, the first return value of singular.version() should be (3,1,0,4) not (3,1,0). 
Note that according to the Singular homepage there is a version 3-1-0-6 available, so, the last digit does play a role.

So, my questions are:

 * How important is it to have doc tests that remain valid if the Singular version changes?
 * Do we take the patch level version number of Singular serious?


---

Comment by SimonKing created at 2010-07-05 12:13:43

Replying to [comment:13 SimonKing]:
> > So, my questions are:
> 
>  * How important is it to have doc tests that remain valid if the Singular version changes?
>  * Do we take the patch level version number of Singular serious?

Is there an answer, yet?


---

Comment by SimonKing created at 2011-05-28 09:27:47

-- bump --

First question: Do we want that `singular.version()` works? Currently, it fails when first called.

Second question: Do we want that (at least by default) it returns a tuple of three or four numbers (three- resp four-digit vesion numbers), or do people like that the output of `singular.version()` (if it is called again after the initial error) returns a lengthy string with full information on the way Singular has been built?


---

Comment by leif created at 2011-08-07 20:02:40

It shouldn't hurt to install the `help.cnf` file though, in which case we wouldn't need (and _should_ remove) the `try ... except RuntimeError ...` and a second try.


---

Comment by leif created at 2011-08-07 20:02:40

Changing keywords from "singular version" to "singular version help.cnf".


---

Comment by leif created at 2011-08-07 20:07:24

Since he reported this again on a duplicate, #11519.


---

Comment by jmantysalo created at 2015-07-17 06:18:13

Replying to [comment:15 SimonKing]:
 
> Do we want that (at least by default) it returns a tuple of three or four numbers (three- resp four-digit vesion numbers), or do people like that the output of `singular.version()` (if it is called again after the initial error) returns a lengthy string with full information on the way Singular has been built?

As a default I would suggest output similar to `pari.version()`. But for now at least `kash_version()` and `r_version()` gives slightly different output...

Maybe right way could be to remove them, and have something like `version('kash')` for one package and `version()` for all packages?


---

Comment by SimonKing created at 2015-09-06 14:55:15

Gosh, is that still not fixed? Sorry that I spoiled it by asking questions in comment:13 that nobody bothers to answer...


---

Comment by SimonKing created at 2015-09-06 15:05:39

To repeat my questions:

- How important is it to have doc tests that remain valid if the Singular version changes?

My answer: We could at least have a test marked random. In that way, we at least make sure that there is no error raised.

- Do we take the patch level version number of Singular serious? Respectively do we really want the current behaviour (singular.version() returns a lengthy string), or would we prefer to have it return a tuple of integers?

My answer: We have

```
sage: pari.version()
[2, 8, 0]
sage: r.version()
((3, 2, 1), 'R version 3.2.1 (2015-06-18)')
sage: gap.version()
'4.7.8'
sage: sage0.version()
'SageMath Version 6.9.beta3, Release Date: 2015-08-21'
```

Hence, the different interfaces have all kind of different output. Thus, the current behaviour should be fine, but the following output

```
sage: singular.eval('system("version")')
'3170'
```

would be equally fine.

My suggestion is: Use the SHORT version string by default, but provide singular_version and singular.version with an optional "verbose=False" argument, that allows to obtain the lengthy version string. And of course fix the error.


---

Comment by jmantysalo created at 2015-09-06 15:24:07

Replying to [comment:24 SimonKing]:
> To repeat my questions:
> 
> - How important is it to have doc tests that remain valid if the Singular version changes?
> 
> My answer: We could at least have a test marked random. In that way, we at least make sure that there is no error raised.

+1

> My suggestion is: Use the SHORT version string by default, but provide singular_version and singular.version with an optional "verbose=False" argument, that allows to obtain the lengthy version string. And of course fix the error.

Sounds good. Somehow the output of `pari.version()` seems best for me. Maybe this could also be documented in http://doc.sagemath.org/html/en/developer/packaging.html#package-versioning as the recommended way to have `*.version()` commands?


---

Comment by SimonKing created at 2015-09-06 17:54:51

Replying to [comment:25 jmantysalo]:
> Sounds good. Somehow the output of `pari.version()` seems best for me.

Slight problem: The patching level usually is not indicated by a number but by "p" plus a number. So, providing the version as a list of integers is perhaps not what we want. And it is not good, I think, if the default output is a list of integers and the verbose output is a totally different type, namely a string.

From that perspective, the r-output is better.

> Maybe this could also be documented in http://doc.sagemath.org/html/en/developer/packaging.html#package-versioning as the recommended way to have `*.version()` commands?

I didn't know about the existence of a `package_version.txt`. I wonder if we could access these data---after all, the package version of singular is "3.1.7p1.p0", but the version shown by `singular.eval('system("version")')` is "3170". Similarly for r, it should be `3.2.1.p0`, not `(3,2,1)`.

I guess it is time to do a bit bike shedding at sage-devel.


---

Comment by jmantysalo created at 2015-09-07 06:40:52

Replying to [comment:26 SimonKing]:
 
> Slight problem: The patching level usually is not indicated by a number but by "p" plus a number. So, providing the version as a list of integers is perhaps not what we want. And it is not good, I think, if the default output is a list of integers and the verbose output is a totally different type, namely a string.
> 
> From that perspective, the r-output is better.

True.

As a system admin I should be able to answer fast to questions "What is the version of ... in our server ...?". For that it is not so important what is the format. But it gives a little unprofessional feeling if I get `(1,2,3)` from `foo.version()` and `[1,2,3]` from `bar.version()`.


---

Comment by SimonKing created at 2015-09-10 09:56:29

Changing status from needs_info to needs_review.


---

Comment by SimonKing created at 2015-09-10 09:56:29

I work around the bug that results in the error, and I think it is best to return both a version tuple on the one hand (so that one can easily test if the version is enough recent) and the complete version information as provided by Singular as a string.

Hopefully the reviewers agree...


---

Comment by SimonKing created at 2015-09-10 09:57:24

Why is it not possible to click on the attached branch an see the changes?


---

Comment by SimonKing created at 2015-09-10 09:58:14

Arrgh. I forgot to commit before pushing :-/


---

Comment by git created at 2015-09-10 09:58:49

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jdemeyer created at 2015-09-10 10:41:40

The error should be reported upstream and the comment in the code should link to this ticket and the upstream report.


---

Comment by jdemeyer created at 2015-09-10 10:41:40

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2015-09-10 10:54:17

I am not so sure if it requires an uptream report. The error is about a missing file, and according to comment:9, adding an empty `$SAGE_ROOT/local/share/singular/help.cnf` suppresses the error.


---

Comment by jdemeyer created at 2015-09-10 11:35:55

Replying to [comment:34 SimonKing]:
> adding an empty `$SAGE_ROOT/local/share/singular/help.cnf` suppresses the error.

Then that should be done instead of wrapping the call in a `try`/`except` block (which is a really ugly "solution")


---

Comment by jdemeyer created at 2015-09-10 11:41:49

There is actually a `help.cnf` installed in

```
$SAGE_LOCAL/share/singular/LIB/help.cnf
```

so I guess it's a bug in Singular that the file is either installed or looked for in the wrong place.

In any case, copying that file to `$SAGE_LOCAL/share/singular/help.cnf` would be a good solution for this ticket.


---

Comment by SimonKing created at 2015-09-10 12:08:37

Replying to [comment:36 jdemeyer]:
> There is actually a `help.cnf` installed in
> {{{
> $SAGE_LOCAL/share/singular/LIB/help.cnf
> }}}
> so I guess it's a bug in Singular that the file is either installed or looked for in the wrong place.

From reading [this change log](http://www.singular.uni-kl.de:8002/trac/changeset/46e5030de2b6094068cceec4cd764bad1a65a02c/git), I believe that .../share singular/LIB/ is the correct place.

I'll file a ticket in the singular trac server. But for now, we need a work-around in Sage.


---

Comment by SimonKing created at 2015-09-10 12:17:47

I reported it [upstream](http://www.singular.uni-kl.de:8002/trac/ticket/740).


---

Comment by SimonKing created at 2015-09-10 12:24:40

I stand corrected! There used to be `$SAGE_LOCAL/share/singular/help.cnf`, but it is gone. The only help.cnf found under $SAGE_ROOT is upstream/src/latest/Singular/LIB/help.cnf.

So, apparently we don't install it at all!


---

Comment by jdemeyer created at 2015-09-10 12:34:54

Replying to [comment:39 SimonKing]:
> So, apparently we don't install it at all!
You're right, this must have come from some earlier Singular version (note the date):

```
$ ls -l local/share/singular/LIB/help.cnf
-rw-r--r-- 1 jdemeyer jdemeyer 3054 Oct 29  2014 local/share/singular/LIB/help.cnf
```



---

Comment by jdemeyer created at 2015-09-10 12:39:23

Replying to [comment:37 SimonKing]:
> But for now, we need a work-around in Sage.
I suggest you just change `spkg-install` to touch the empty file `$SAGE_SHARE/singular/help.cnf`


---

Comment by SimonKing created at 2015-09-10 12:45:21

Replying to [comment:41 jdemeyer]:
> Replying to [comment:37 SimonKing]:
> > But for now, we need a work-around in Sage.
> I suggest you just change `spkg-install` to touch the empty file `$SAGE_SHARE/singular/help.cnf`

Why not modify spkg-install, so that it installs the missing file? Alternatively, we could patch Singular's Makefile (or whatever it is called) so that it installs the missing file. What is the preferred way?

Also, I'd like to know why Singular's Makefile does not install help.cnf. After all, if I understand correctly, it DOES install all the library files of Singular (which are in the same folder as help.cnf).

Hang on. I just notice that the singular spkg apparently screws completely. Or how would you explain that I find the complete UNPACKED singular source tree in SAGE_LOCAL/upstream/ ? Do we need a new Singular package?


---

Comment by SimonKing created at 2015-09-10 12:47:46

Upstream says that help.cnf should indeed be put into the same folder as all the other library files, i.e., local/share/singular/.


---

Comment by jdemeyer created at 2015-09-10 12:47:59

Replying to [comment:42 SimonKing]:
> Replying to [comment:41 jdemeyer]:
> > Replying to [comment:37 SimonKing]:
> > > But for now, we need a work-around in Sage.
> > I suggest you just change `spkg-install` to touch the empty file `$SAGE_SHARE/singular/help.cnf`
> 
> Why not modify spkg-install, so that it installs the missing file? Alternatively, we could patch Singular's Makefile (or whatever it is called) so that it installs the missing file. What is the preferred way?
I don't really care much.

> Hang on. I just notice that the singular spkg apparently screws completely. Or how would you explain that I find the complete UNPACKED singular source tree in SAGE_LOCAL/upstream/ ?
Probably you once extracted the tarball in `upstream`? It's not the package which does that...


---

Comment by SimonKing created at 2015-09-10 13:08:35

Replying to [comment:44 jdemeyer]:
> > Why not modify spkg-install, so that it installs the missing file? Alternatively, we could patch Singular's Makefile (or whatever it is called) so that it installs the missing file. What is the preferred way?
> I don't really care much.

Then I guess we should do it in spkg-install.
 
> Probably you once extracted the tarball in `upstream`? It's not the package which does that...

Could be. I just deleted it and did "sage -f singular".


---

Comment by leif created at 2015-09-10 13:13:51

There's also `#sagemath` on freenode.  Just saying...


---

Comment by SimonKing created at 2015-09-10 15:31:01

Replying to [comment:46 leif]:
> There's also `#sagemath` on freenode.  Just saying...

Meaning what?


---

Comment by leif created at 2015-09-10 19:52:13

Replying to [comment:47 SimonKing]:
> Replying to [comment:46 leif]:
> > There's also `#sagemath` on freenode.  Just saying...
> 
> Meaning what?

Overfull inbox, TeX would have said. ;-)


---

Comment by SimonKing created at 2015-09-11 09:34:50

It seems the current agreement seems to be to modify spkg-install, so that it copies help.cnf from the singular sources to `$SAGE_SHARE/singular/`. What is the path to the singular sources while spkg-install is executed?


---

Comment by jdemeyer created at 2015-09-11 09:37:13

Replying to [comment:49 SimonKing]:
> What is the path to the singular sources while spkg-install is executed?
It's the current working directory.


---

Comment by jmantysalo created at 2016-10-24 09:23:56

Changing priority from major to minor.


---

Comment by jmantysalo created at 2016-10-24 09:23:56

Error has gone away with Singular 4.

I added doctest.

What goes to output format, I think this should be changed in all `*_version()` commands at once. (Assuming somebody would care, which is propably not true.)
----
New commits:


---

Comment by jmantysalo created at 2016-10-24 09:23:56

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2016-10-26 17:48:20

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-11-02 19:20:02

Resolution: fixed

# Issue 9893: Group cohomology spkg, version 2.1

Issue created by migration from https://trac.sagemath.org/ticket/9894

Original creator: SimonKing

Original creation time: 2010-09-10 23:06:03

Assignee: tbd

CC:  graham.ellis@nuigalway.ie david.green@uni-jena.de

Keywords: modular group cohomology solaris t2

Version 2.1 of the modular group cohomology package is now available. There is extensive [documentation](http://sage.math.washington.edu/home/SimonKing/Cohomology/index.html). The package can be installed with `sage -i http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-2.1.spkg`


*__New Features__*

1. I tried to improve the code quality. For example:

 - Typically one has methods whose result can be cached and needs only be re-computed if the ring approximation changes; this is now being taken care of by decorators.
 - I tried to reduce compiler warnings.
 - Using the package, several bugs in Singular and GAP have been uncovered. The new Singular version 3-1-1 fixes some bugs, so that in some cases more efficient methods can be used. The package tests the available Singular version; it both supports the new features and is able to work around the old Singular bugs.

2. The completeness criteria are further improved. We use three criteria, namely the modified Benson criterion (found by David Green and myself), the Symonds criterion and the Hilbert-Poincaré criterion (suggested by Peter Symonds and worked out by myself). Due to new methods of constructing parameters, the Symonds criterion is now often the best choice - but not always, so that it is good to have three methods to choose from.

3. New functionality includes the computation of preimages of induced homomorphisms, essential ideals and depth essential ideals. Using the package, a new example of a group was found for which the square of the essential ideal does not vanish (this is only the second known example!). So far, a conjecture of Jon Carlson on depth essential ideals can be confirmed.

4. *It works on t2!! * This is a very non-trivial achievement. It involved:
 * Changing the names of several functions from `C-MeatAxe`, since the Sun linker seems to confuse them with functions from pari. This is a problem similar to the one found at #1396.
 * t2 is a big-endian machine. GAP's random generator depends on the endianness (which is a bug). Certain internal data used by the cohomology computations are obtained by randomised algorithms of GAP. The ring presentation found for the cohomology ring depends on these internal data. So, in order to get machine independent computationally well defined results, special care was needed, as discussed on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/623f7291ab7e782e)

5. By oversight, the old test script failed to execute the tests of special methods (such as `__add__` or `__mul__`. The new script now captures all tests, and complains if a class, method or function does not appear to be tested. Also, the test script does parallel tests.

6. We finally achieved *100% doctest coverage!! *

*__Testing__*

As usual, if the environment variable `SAGE_CHECK` is exported and has the value `yes`, the test script is automatically executed and the result saved in `SAGE_ROOT/install.log`.

The script tests parallely. By default, the number of threads is one third of the number of available CPUs. This can be overruled by exporting the environment variable `SAGE_NUMBER_THREADS`.

I successfully installed and tested the package on the following machines and the following versions of Sage and Singular:
 * t2.math, Sage 4.5.1, Singular 3-1-1
 * bsd.math, Sage 4.5.2, Singular 3-1-0, both in 64 and 32 bit mode
 * sage.math, Sage 4.5.1, Singular 3-1-0
 * x86_64 GNU/Linux, Intel Core2 CPU 6700 `@` 2.66GHz, Sage 4.5.2, Singular 3-1-1

On another GNU Linux machine with AMD processors, it builds and seems to work even with Sage 4.2.1, but apparently the interface to the `@`parallel decorator has changed, so that I was not able to run the test script.


---

Comment by kcrisman created at 2010-09-11 08:10:39

On a Mac OS X 10.4 G4 PPC running at 1.25 GHz, 1 GB memory, I get successful installation and mostly passed doctests, but some failure.  See [the relevant bits of the log](http://sage.math.washington.edu/home/kcrisman/RelevantPCohomTest.log).  I didn't post the whole log because there are some non-failures reported as failures due to another spkg update - I checked these individually, and they are definitely ok.  I'm going to try `./sage -ba` and reinstall just to make sure, but it's apparent that at least a few of these things are real differences - different list entries, different orderings, etc.  Happy hunting!


---

Comment by SimonKing created at 2010-09-11 10:15:45

Hi!

Thank you for testing!

I found this error particularly interesting, at the very end of the file

```
    sage: H.sylow_cohomology().Dickson
Expected:
    ['-b_2_0^6 - b_2_2^6 - b_2_2^2*b_4_6^2 + b_2_2^3*c_6_11 + b_4_6^3', None]
Got:
    ['b_4_6^3-b_2_2^2*b_4_6^2-b_2_2^6-b_2_0^6+b_2_2^3*c_6_11', None]
```


What you got is, as much as I see, the result that you would get when computing `H.sylow_cohomology()` from scratch. But in fact it is expected that `H.sylow_cohomology()` is automatically downloaded from a web repository, containing cohomology rings that were computed with an old version of the package and thus have equivalent data (note that the polynomials above are equal) presented in a different form.

Could it be that you worked without internet connection? At least, it would explain that particular error.

Often there is a "list index out of range" in `MODCOHO.find_relations`. This one is a bit obscure to me at the moment. Can you try one of these examples manually and post the full traceback?

There is one error in "BarCode.show"; I have seen this on OS X before, but this seems to be a problem with "show" on OS X in general. 

Could you please post the _entire_ log? It seems that you cut off too much. E.g., I can not see how `COCH.massey_power` fails.

Best regards,

Simon


---

Comment by SimonKing created at 2010-09-11 13:19:00

Changing status from new to needs_work.


---

Comment by SimonKing created at 2010-09-11 13:19:00

Hi!

It seems that there is a problem I hadn't thought of: If one has used the spkg before, then data are accumulated that are later used when doing related computations. Of course, I _did_ use the package before. Now, when testing, it can happen that the old results (potentially obtained with an old program version) are used and spoil the tests.

So, `@`kcrisman, this might be another explanation for the "particularly interesting" failure: There are old data on my computer, and I accidentally used the old data in the tests.

I have to think how to solve that problem. Certainly the tests should work both with and without having old data in the system. I did try to write the tests so that the computations are either done from scratch or use data that I have full control of, but it seems that I missed some exceptions.

Bets regards,
Simon


---

Comment by kcrisman created at 2010-09-11 15:53:56

I did `./sage -ba` to get rid of the erroneous errors (that would include the file you refer to).  I'll upload an updated version of that part of the log.  Also, there *was* internet connection (had to have it to download it, and also to get the gap package I didn't realize I needed until it told me so), but it is true I have never computed these before or used the spkg before.  As far as I can tell, the second run had the same failures, but I didn't bother to check all of them by hand.

Finally, here is one of the typical failures replicated.  I can check some other stuff (possibly not until rather later, though) if you give very explicit instructions as to what commands to run.

```
Crismans-Computer:~ crisman$ Desktop/sage-4.5.3/sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: from pGroupCohomology import CohomologyRing
sage: tmp = tmp_filename()
sage: CohomologyRing.set_user_db(tmp)
sage: G = gap('AlternatingGroup(8)')
sage: H = CohomologyRing(G,prime=2,GroupName='A8')
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
| Sage Version 4.5.3, Release Date: 2010-09-04                       |
| Type notebook() for the GUI, and license() for information.        |
/Users/crisman/<ipython console> in <module>()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/__init__.pyc in __call__(self, *args, **kwds)
   2676             # By now, we have both subgroups and their cohomology rings.
   2677             if not HP.completed:
-> 2678                 HP.make()
   2679             # not needed for HSyl, since it was computed when we did it in the computation of HP
   2680 

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/modular_cohomology.so in pGroupCohomology.modular_cohomology.MODCOHO.make (pGroupCohomology/modular_cohomology.c:46208)()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/modular_cohomology.so in pGroupCohomology.modular_cohomology.MODCOHO.next (pGroupCohomology/modular_cohomology.c:45211)()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/cohomology.so in pGroupCohomology.cohomology.COHO.lift_dickson (pGroupCohomology/cohomology.c:63567)()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/modular_cohomology.so in pGroupCohomology.modular_cohomology.MODCOHO.PrescribedRestrictions (pGroupCohomology/modular_cohomology.c:35570)()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/modular_cohomology.so in pGroupCohomology.modular_cohomology.MODCOHO.decomposable_classes (pGroupCohomology/modular_cohomology.c:33350)()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/modular_cohomology.so in pGroupCohomology.modular_cohomology.MODCOHO.find_relations (pGroupCohomology/modular_cohomology.c:32768)()

IndexError: list index out of range
```



---

Comment by kcrisman created at 2010-09-11 15:55:15

If there are tests that need internet, by the way, those should be marked `# optional - internet`.


---

Comment by SimonKing created at 2010-09-11 17:17:10

Replying to [comment:4 kcrisman]:
> I did `./sage -ba` to get rid of the erroneous errors (that would include the file you refer to).  I'll upload an updated version of that part of the log.  Also, there *was* internet connection (had to have it to download it, and also to get the gap package I didn't realize I needed until it told me so), but it is true I have never computed these before or used the spkg before.

Yes, probably that's why. I moved my old data out of the way, and then I got a couple of errors. It turned out that this could be resolved by doing `CohomologyRing.user_db(...)` when I did `CohomologyRing(...)` (the latter did access old data).

>  As far as I can tell, the second run had the same failures, but I didn't bother to check all of them by hand.

Yes, no surprise. My erroneous tests assumed that you had data on your computer obtained by _previous_ versions of the package.
 
> Finally, here is one of the typical failures replicated.  I can check some other stuff (possibly not until rather later, though) if you give very explicit instructions as to what commands to run.

Thank you! I'll see if I can somehow replicate the error.

Does the error also occur if you do

```
sage: from pGroupCohomology import CohomologyRing
sage: tmp = tmp_filename()
sage: CohomologyRing.set_user_db(tmp)
sage: G = gap('AlternatingGroup(8)')
sage: H = CohomologyRing.user_db(G,prime=2,GroupName='A8')
```

?
 
Best regards,
Simon


---

Comment by SimonKing created at 2010-09-11 17:19:17

Replying to [comment:5 kcrisman]:
> If there are tests that need internet, by the way, those should be marked `# optional - internet`.

Thank you! I didn't know that this is possible.

Best regards,

Simon


---

Comment by SimonKing created at 2010-09-11 20:08:01

Replying to [comment:7 SimonKing]:
> Replying to [comment:5 kcrisman]:
> > If there are tests that need internet, by the way, those should be marked `# optional - internet`.
> 
> Thank you! I didn't know that this is possible.

However, there are only two tests for which the internet accessibility should really make a difference: There, `CohomologyRing.web_db(...)` is explicitly called.

When doing `CohomologyRing(...)` or `CohomologyRing.user_db(...)`, it is tried to download the result from the web repository (unless requested otherwise by the optional argument `websource=False`), and if this fails, the computation is simply started from scratch, without raising an error.

I am now trying to change the tests so that they will work both with or without old data being present.


---

Comment by kcrisman created at 2010-09-12 00:00:16

> Does the error also occur if you do
> {{{
> sage: from pGroupCohomology import CohomologyRing
> sage: tmp = tmp_filename()
> sage: CohomologyRing.set_user_db(tmp)
> sage: G = gap('AlternatingGroup(8)')
> sage: H = CohomologyRing.user_db(G,prime=2,GroupName='A8')
> }}}

It's slightly different:

```
Crismans-Computer:~ crisman$ Desktop/sage-4.5.3/sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: from pGroupCohomology import CohomologyRing
sage:  sage: tmp = tmp_filename()
sage:  sage: CohomologyRing.set_user_db(tmp)
sage:  sage: G = gap('AlternatingGroup(8)')
sage:  sage: H = CohomologyRing.user_db(G,prime=2,GroupName='A8')
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
| Sage Version 4.5.3, Release Date: 2010-09-04                       |
| Type notebook() for the GUI, and license() for information.        |
/Users/crisman/<ipython console> in <module>()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/__init__.pyc in user_db(self, *args, **kwds)
   2991         """
   2992         kwds['root'] = COHO.user_db
-> 2993         return self(*args, **kwds)
   2994 
   2995     def set_web_db(self, s = None):

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/__init__.pyc in __call__(self, *args, **kwds)
   2676             # By now, we have both subgroups and their cohomology rings.
   2677             if not HP.completed:
-> 2678                 HP.make()
   2679             # not needed for HSyl, since it was computed when we did it in the computation of HP
   2680 

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/modular_cohomology.so in pGroupCohomology.modular_cohomology.MODCOHO.make (pGroupCohomology/modular_cohomology.c:46208)()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/modular_cohomology.so in pGroupCohomology.modular_cohomology.MODCOHO.next (pGroupCohomology/modular_cohomology.c:45211)()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/cohomology.so in pGroupCohomology.cohomology.COHO.lift_dickson (pGroupCohomology/cohomology.c:63567)()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/modular_cohomology.so in pGroupCohomology.modular_cohomology.MODCOHO.PrescribedRestrictions (pGroupCohomology/modular_cohomology.c:35570)()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/modular_cohomology.so in pGroupCohomology.modular_cohomology.MODCOHO.decomposable_classes (pGroupCohomology/modular_cohomology.c:33350)()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/modular_cohomology.so in pGroupCohomology.modular_cohomology.MODCOHO.find_relations (pGroupCohomology/modular_cohomology.c:32768)()

IndexError: list index out of range
```

But essentially the same.  Apparently the `find_relations` method is assuming some list has the wrong length.


---

Comment by SimonKing created at 2010-09-12 08:49:58

Replying to [comment:4 kcrisman]:
> Finally, here is one of the typical failures replicated.  I can check some other stuff (possibly not until rather later, though) if you give very explicit instructions as to what commands to run.

There are various lists occuring inside `find_relations`. There is also some Singular commands used to determine coefficients of lists, so, the error could be there as well.

Since I can not replicate it on my computer, can you please do/answer the following?

What version of Sage are you using? What version of Singular is it?

Remove your "private cohomology database" in order to be sure that there is no debris left. You will probably not mind to do it by `rm -r ~/.sage/pGroupCohomology/db/*` (or you can move the contents of the folder to a backup location). The folder itself must be present, though.

Do the following in Sage:

```
sage: from pGroupCohomology import CohomologyRing, _cache
sage: G = gap('AlternatingGroup(8)')
sage: H = CohomologyRing(G,prime=2,GroupName='A8')
sage: for X in _cache.values():
....:     print X.autosave_name(), X.completed
....:
```


This should give something like

```
/home/king/.sage/pGroupCohomology/db/H6gp1mod2.sobj True
/home/king/SAGE/sage-4.4.2/data/pGroupCohomology/8gp3/H8gp3.sobj True
/home/king/SAGE/sage-4.4.2/data/pGroupCohomology/32gp49/H32gp49.sobj True
/home/king/.sage/pGroupCohomology/db/H192gp1493mod2.sobj True
/home/king/SAGE/sage-4.4.2/data/pGroupCohomology/32gp27/H32gp27.sobj True
/home/king/SAGE/sage-4.4.2/data/pGroupCohomology/2gp1/H2gp1.sobj True
/home/king/SAGE/sage-4.4.2/data/pGroupCohomology/64gp138/H64gp138.sobj True
/home/king/.sage/pGroupCohomology/db/HA8mod2.sobj False
/home/king/SAGE/sage-4.4.2/data/pGroupCohomology/16gp14/H16gp14.sobj True
/home/king/SAGE/sage-4.4.2/data/pGroupCohomology/8gp5/H8gp5.sobj True
```

These are all cohomology rings that one needs to know in order to compute `H`. But since the construction of `H` fails for you, the list might be different, and at least the `.../HA8mod2.sobj` should be missing.

You see that the cohomology rings of prime power groups are in the public database `SAGE_ROOT/data/...`, whereas the non prime power groups are in your private database `~/.sage/...`.

Do you get a `False` after a prime power group in the above list?

According to the traceback you got, I expect that you have a `False` after `H192gp1493mod2.sobj`. Can you please post (or send me by e-mail) all files from the above list which are followed by `False`? Then I can do further debugging with them.

Best regards,

Simon


---

Comment by SimonKing created at 2010-09-12 14:58:45

Hi Karl-Dieter,

There is also another way to potentially get more insight: Could you try the computation in protocol mode, i.e., `H = CohomologyRing(G,prime=2,GroupName='A8',options='prot')`? The last few protocol lines before the error will probably help to locate the problem.

Best regards,
Simon


---

Comment by SimonKing created at 2010-09-12 16:26:59

Perhaps I found the solution: In `find_relations` (and various other places), I parsed an ideal M in Singular into a list of strings as follows:

```
singular.eval('print(%s)'%M.name()).split(',\n')
```


I guess that `split(',\n')` is a mistake: There are systems (including OS X?) on which '\n' is not the line break character. So, I should better do

```
[t.strip() for t in singular.eval('print(%s)'%M.name()).split(',')]
```


I am now preparing and testing an updated version. So, until later...

Best regards,

Simon


---

Comment by SimonKing created at 2010-09-12 20:43:11

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2010-09-12 20:43:11

Hi!

I updated the package, changing the tests so that they should work with or without old data being present, and changing the code so that it is not expected that '\n' is the newline character.

I tested it on the desktop computer in my office and am currently running tests on bsd.math, t2.math and sage.math.

So, it is ready for review again.

If you want to re-install and test the package, please don't forget to delete the copy of the _old_ package version, for otherwise the new version would not be downloaded. Hence,

```
rm $SAGE_ROOT/spkg/optional/p_group_cohomology-2.1.spkg
sage -f http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-2.1.spkg
```

Testing with

```
export SAGE_CHECK=yes
```

Bounding the number of parallel tests with, e.g.

```
export SAGE_NUMBER_THREADS=2
```


Cheers,

Simon


---

Comment by SimonKing created at 2010-09-13 07:27:58

There are doctest failures on t2. So, back at work...


---

Comment by SimonKing created at 2010-09-13 07:27:58

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2010-09-13 10:06:45

Replying to [comment:14 SimonKing]:
> There are doctest failures on t2. So, back at work...

But it's strange: _All_ errors come from GAP, and they are like

```
TypeError: Error evaluating $sage81:=IsBoundGlobal("exportMTXLIB");; in Gap
```

or

```
 TypeError: Error evaluating $sage24:="DihedralB";; in Gap
```


Of course, both commands are supposed to work! I could imagine that it is a parallelisation problem. The errors occurred with `SAGE_NUMBER_THREADS=8`. I am now seeing if it works with `SAGE_NUMBER_THREADS=4`.


---

Comment by SimonKing created at 2010-09-13 14:47:17

Replying to [comment:15 SimonKing]:
> Replying to [comment:14 SimonKing]:
> > There are doctest failures on t2. So, back at work...
> 
> But it's strange: _All_ errors come from GAP...

And when I did it again, they vanished. Strange enough. But I think testing on the machine of kcrisman is more important. Can you please try?

Best regards,

Simon


---

Comment by SimonKing created at 2010-09-13 14:47:17

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-09-13 15:01:34

> And when I did it again, they vanished. Strange enough. But I think testing on the machine of kcrisman is more important. Can you please try?

Eventually, but at least not until tonight, possibly not until several evenings from now.  I will try hard to `rm` all relevant stuff, though, before trying all this out :)


---

Comment by kcrisman created at 2010-09-14 00:46:45

> Since I can not replicate it on my computer, can you please do/answer the following?
> 
> What version of Sage are you using? What version of Singular is it?
I have no explanation for the following.

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: singular_version()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
| Sage Version 4.5.3, Release Date: 2010-09-04                       |
| Type notebook() for the GUI, and license() for information.        |
/Users/crisman/<ipython console> in <module>()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/sage/interfaces/singular.pyc in singular_version()
   1916     EXAMPLES:
   1917     """
-> 1918     return singular.eval('system("--version");')
   1919 
   1920 

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/sage/interfaces/singular.pyc in eval(self, x, allow_semicolon, strip, **kwds)
    547 
    548         if s.find("error") != -1 or s.find("Segment fault") != -1:
--> 549             raise RuntimeError, 'Singular error:\n%s'%s
    550 
    551         if get_verbose() > 0:

RuntimeError: Singular error:
   ? cannot open `help.cnf`
Singular for ppcMac-darwin version 3-1-1 (3114-2010090802)  Sep  8 2010 02:24:06
with
        factory(@(#) factoryVersion = 3.1.1),libfac(3.1.1,Feb 2010),
        GMP(4.2),NTL(5.4.2),32bit,static readline,Plural,DBM,
        dynamic modules,OM_NDEBUG,random=1284424481
        CC= gcc -O3 -g -fPIC -pipe -DNDEBUG -DOM_NDEBUG -DppcMac_darwin -DHAVE_CONFIG_H,
        CXX= g++ -O3 -g -fPIC -pipe -DNDEBUG -DOM_NDEBUG -DppcMac_darwin -DHAVE_CONFIG_H (4.0.1 (Apple Computer, Inc. build 5370))
argv[0]   :     Singular-3-1-1
SearchPath:     /Users/crisman/Desktop/sage-4.5.3/local/share/singular:/Users/crisman/Desktop/sage-4.5.3/local/LIB
Singular  :     /Users/crisman/Desktop/sage-4.5.3/local/bin/Singular
BinDir    :     /Users/crisman/Desktop/sage-4.5.3/local/bin
RootDir   :     /Users/crisman/Desktop/sage-4.5.3/local
DefaultDir:     /Users/crisman/Desktop/sage-4.5.3/local
InfoFile  :
IdxFile   :
HtmlDir   :
ManualUrl :     http://www.singular.uni-kl.de/Manual/3-1-1
ExDir     :
Path      :     /Users/crisman/Desktop/sage-4.5.3/local/bin:/Users/crisman/Desktop/sage-4.5.3:/bin:/sbin:/usr/bin:/usr/sbin
EmacsDir  :
Available HelpBrowsers: dummy, emacs, 
Current HelpBrowser: dummy 
   ? error occurred in or before STDIN line 49965: `system("--version");`
```

But as you can see in the error messages, it's the 3.1.1 devel version, and this works:

```
Crismans-Computer:~ crisman$ Desktop/sage-4.5.3/sage -singular
                     SINGULAR                             /  Development
 A Computer Algebra System for Polynomial Computations   /   version 3-1-1
                                                       0<
     by: G.-M. Greuel, G. Pfister, H. Schoenemann        \   Feb 2010
FB Mathematik der Universitaet, D-67653 Kaiserslautern    \
```

> Remove your "private cohomology database" in order to be sure that there is no debris left. You will probably not mind to do it by `rm -r ~/.sage/pGroupCohomology/db/*` (or you can move the contents of the folder to a backup location). The folder itself must be present, though.
> 
> Do the following in Sage:
> {{{
> sage: from pGroupCohomology import CohomologyRing, _cache
> sage: G = gap('AlternatingGroup(8)')
> sage: H = CohomologyRing(G,prime=2,GroupName='A8')
This fails for me earlier:

```
sage: from pGroupCohomology import CohomologyRing, _cache
sage: G = gap('AlternatingGroup(8)')
sage: H = CohomologyRing(G,prime=2,GroupName='A8')
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/Users/crisman/<ipython console> in <module>()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/__init__.pyc in __call__(self, *args, **kwds)
   2676             # By now, we have both subgroups and their cohomology rings.
   2677             if not HP.completed:
-> 2678                 HP.make()
   2679             # not needed for HSyl, since it was computed when we did it in the computation of HP
   2680 

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/modular_cohomology.so in pGroupCohomology.modular_cohomology.MODCOHO.make (pGroupCohomology/modular_cohomology.c:46208)()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/modular_cohomology.so in pGroupCohomology.modular_cohomology.MODCOHO.next (pGroupCohomology/modular_cohomology.c:45211)()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/cohomology.so in pGroupCohomology.cohomology.COHO.lift_dickson (pGroupCohomology/cohomology.c:63567)()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/modular_cohomology.so in pGroupCohomology.modular_cohomology.MODCOHO.PrescribedRestrictions (pGroupCohomology/modular_cohomology.c:35570)()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/modular_cohomology.so in pGroupCohomology.modular_cohomology.MODCOHO.decomposable_classes (pGroupCohomology/modular_cohomology.c:33350)()

/Users/crisman/Desktop/sage-4.5.3/local/lib/python2.6/site-packages/pGroupCohomology/modular_cohomology.so in pGroupCohomology.modular_cohomology.MODCOHO.find_relations (pGroupCohomology/modular_cohomology.c:32768)()

IndexError: list index out of range
```

I'll try the reinstall next.


---

Comment by kcrisman created at 2010-09-14 00:59:30

Replying to [comment:11 SimonKing]:
> Hi Karl-Dieter,
> 
> There is also another way to potentially get more insight: Could you try the computation in protocol mode, i.e., `H = CohomologyRing(G,prime=2,GroupName='A8',options='prot')`? The last few protocol lines before the error will probably help to locate the problem.

Cool documentation of what is going on!   I removed the db stuff (but not the folder) again, and got this before the same error (I assume that up to here it is the same for you):

```

There is no new generator of H^*(SmallGroup(192,1493); GF(2)) in degree 7
  Degree 7 of the visible ring structure of H^*(SmallGroup(192,1493); GF(2)) is computed!
  Saving H^*(SmallGroup(192,1493); GF(2))
  We expect that the Hilbert-Poincare criterion will not apply before degree 11
  Start computation in Degree 8
  All stable cocycles are decomposable
  Determine degree 8 standard monomials of H^*(SmallGroup(192,1493); GF(2))
  Express 48 standard monomials as cocycles
  > Interreduction
  > Determining decomposable subspace
  > Extracting relations
  There is no new relation in degree 8
There is no new generator of H^*(SmallGroup(192,1493); GF(2)) in degree 8
  Try to lift 1st power of 0th Dickson invariant
  Determine degree 8 standard monomials of H^*(SmallGroup(192,1493); GF(2))
  Express 48 standard monomials as cocycles
  > Interreduction
  > Determining decomposable subspace
  > Extracting decomposable cocycles and relations
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
```



---

Comment by kcrisman created at 2010-09-14 01:06:11

> If you want to re-install and test the package, please don't forget to delete the copy of the _old_ package version, for otherwise the new version would not be downloaded. Hence,
> {{{
> rm $SAGE_ROOT/spkg/optional/p_group_cohomology-2.1.spkg
> sage -f http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-2.1.spkg
> }}}
> Testing with
> {{{
> export SAGE_CHECK=yes
> }}}
Currently doing this.  It will take some time.
> {{{
> export SAGE_NUMBER_THREADS=2
> }}}
lol - this processor has one core, and you can't do multiple thread with Sage on it (I've tried).


---

Comment by SimonKing created at 2010-09-14 08:05:44

Hi!

Replying to [comment:19 kcrisman]:
>   > ...
>   > Determining decomposable subspace
>   > Extracting decomposable cocycles and relations

Yep. That confirms my conjecture. Right after that line of protocol, there is a line containing a `split` statement, and IIRC it originally was

```
SelfValues = singular.eval('print(%s)'%DG.name()).split(',\n')
```


In the current version, it is

```
SelfValues = [t.strip() for t in singular.eval('print(%s)'%DG.name()).split(',')]
```

instead.

Could you test the following, please:

```
sage: R = singular.ring(0,'(x,y)','dp')
sage: I = singular.maxideal(3)
sage: singular.eval('print(%s)'%I.name()).split(',\n')
['y^3', 'x*y^2', 'x^2*y', 'x^3']
sage: [t.strip() for t in singular.eval('print(%s)'%I.name()).split(',')]
['y^3', 'x*y^2', 'x^2*y', 'x^3']
```

I reckon that on your computer the two lists are different.

Cheers,

Simon


---

Comment by kcrisman created at 2010-09-14 08:32:58

> Could you test the following, please:
> {{{
> sage: R = singular.ring(0,'(x,y)','dp')
> sage: I = singular.maxideal(3)
> sage: singular.eval('print(%s)'%I.name()).split(',\n')
> ['y^3', 'x*y^2', 'x^2*y', 'x^3']
> sage: [t.strip() for t in singular.eval('print(%s)'%I.name()).split(',')]
> ['y^3', 'x*y^2', 'x^2*y', 'x^3']
> }}}
Well:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R = singular.ring(0,'(x,y)','dp')
sage: I = singular.maxideal(3)
sage: singular.eval('print(%s)'%I.name()).split(',\n')
['y^3', 'x*y^2', 'x^2*y', 'x^3']
sage: [t.strip() for t in singular.eval('print(%s)'%I.name()).split(',')]
['y^3', 'x*y^2', 'x^2*y', 'x^3']
```

But:

```
Successfully installed p_group_cohomology-2.1
Running the test suite.
Testing the package pGroupCohomology...
Will use 1 parallel processes
| Sage Version 4.5.3, Release Date: 2010-09-04                       |
| Type notebook() for the GUI, and license() for information.        |
pGroupCohomology fails
pGroupCohomology.unit_test_64 passes in 585.23 s
pGroupCohomology._IsKeyEquivalent passes in 52.95 s
<snip>
pGroupCohomology.resolution.G_ALG.kG_map passes in 16.91 s
pGroupCohomology.resolution.G_ALG.isAbelian passes in 17.09 s
pGroupCohomology.resolution.MasseyDefiningSystems passes in 15.39 s
pGroupCohomology.resolution.MasseyDefiningSystems.__init__ passes in 15.38 s
pGroupCohomology.resolution.MasseyDefiningSystems._make passes in 15.43 s
pGroupCohomology.resolution.MasseyDefiningSystems.values passes in 17.53 s
There were doctest failures:
pGroupCohomology:
sage -t -optional -long "/Users/crisman/.sage/temp/Crismans_Computer.local/3200/dir_0/file_0.py"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***

         [1803.1 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -optional -long "/Users/crisman/.sage/temp/Crismans_Computer.local/3200/dir_0/file_0.py" # Time out
Total time for all tests: 1803.4 seconds


Summary
-------

The following tests fail:
  pGroupCohomology
Total time: 15702.23 sec
```

So now I'll just 

```
export SAGE_TIMEOUT_LONG=3600
```

and `./sage -f` it again, and hopefully all will be well in the morning.  I have to say, five hours to install and test - that's quite an spkg, quite the computation!


---

Comment by kcrisman created at 2010-09-14 08:35:05

Not sure what happened there - must have formatted wrong.

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R = singular.ring(0,'(x,y)','dp')
sage: I = singular.maxideal(3)
sage: singular.eval('print(%s)'%I.name()).split(',\n')
['y^3', 'x*y^2', 'x^2*y', 'x^3']
sage: [t.strip() for t in singular.eval('print(%s)'%I.name()).split(',')]
['y^3', 'x*y^2', 'x^2*y', 'x^3']
```



---

Comment by kcrisman created at 2010-09-14 08:35:44

If that fails again, I would like to know where these doctests live in the spkg so I can figure out how to run them individually.


---

Comment by SimonKing created at 2010-09-14 08:54:15

Replying to [comment:22 kcrisman]:
> > and `./sage -f` it again, and hopefully all will be well in the morning.  I have to say, five hours to install and test - that's quite an spkg, quite the computation!

Ouch! Five hours is really much. On my desktop computer, the total time for the tests is `2812.09 sec`, and installation takes maybe 10 minutes.

By the way, the test skript runs *all* doctests. So, it always includes the ones marked long. Perhaps in the next version I should provide the possibility to only run the short tests.

But what is the point of having tests that take so long? This is due to the fact that often I was not able to find smaller examples that show the benefit of a particular method.

How to find the doctests? Well, you had a timeout in pGroupCohomology. So, you are in the lucky situation that the test is in a Python file, namely (if you untar'd the package) in `p_group_cohomology-2.1/src/pGroupCohomology/__init__.py`. You could run `sage -t -verbose -long` on that file (that wouldn't work for the Cython files). Using the "verbose" option would show exactly what part of the test takes so long.

It is surprising to me that the two lists in the little `split` test are equal. But anyway, I think `[t.strip() for t in singular.eval('print(%s)'%I.name()).split(',')]` is cleaner than `singular.eval('print(%s)'%I.name()).split(',\n')`

Cheers,

Simon


---

Comment by SimonKing created at 2010-09-14 10:34:20

Replying to [comment:22 kcrisman]:
> > I have to say, five hours to install and test - that's quite an spkg, quite the computation!

PS:

On my machine, the longest _single_ test takes about 90 seconds. Since the documentation of `pGroupCohomology.__init__` contains many examples (it is an introduction how to use the package), it is no surprise that it takes longer, but it is still `pGroupCohomology passes in 242.05 s`.


---

Comment by kcrisman created at 2010-09-14 11:00:17

> On my machine, the longest _single_ test takes about 90 seconds. Since the documentation of `pGroupCohomology.__init__` contains many examples (it is an introduction how to use the package), it is no surprise that it takes longer, but it is still `pGroupCohomology passes in 242.05 s`. 

```
pGroupCohomology passes in 1205.79 s
```

So less than six times slower - not bad ;)

I think the timeout was because I had a heavy other load (watching Carl Witty's video, downloading things) when I ran it the first time.  But remember, this is a 1.25 GHz machine with only 1 GB memory!

Anyway, I can't review this any more because I don't use Singular or GAP much at all (though I still think it's cool that you are calculating the cohomology rings as rings, there has to be a way to apply this nicely to the topology stuff in Sage), but I will at least add myself as a first reviewer.


---

Comment by SimonKing created at 2010-09-14 15:10:55

Replying to [comment:27 kcrisman]:
> I think the timeout was because I had a heavy other load (watching Carl Witty's video, downloading things) when I ran it the first time.  But remember, this is a 1.25 GHz machine with only 1 GB memory!

OK, my machine has 2 GB. But actually keeping the memory consumption low was a driving force behind many things that I did for the first version of the package. As a result, the cohomology for most (but not all) groups of order 128 can be computed with 2 GB.

But I think I should put "find smaller test cases" on my to-do list for version 2.2.

> Anyway, I can't review this any more because I don't use Singular or GAP much at all

What a pity! But thanks for your effort!

> (though I still think it's cool that you are calculating the cohomology rings as rings, there has to be a way to apply this nicely to the topology stuff in Sage),

I wonder if this will be possible. As it is, the package is very much addressed to algebra, and I don't see how this could be changed.

> but I will at least add myself as a first reviewer.

Sure!

Best regards,

Simon


---

Comment by SimonKing created at 2010-09-25 23:01:08

In the meantime, I created a new version of the package (and changed the description accordingly). It was inspired by David Green's complaint that the package would try to load data from SAGE_DATA but would then be unable to do further computations without write permission.


---

Comment by SimonKing created at 2010-09-25 23:01:08

Changing assignee from tbd to SimonKing.


---

Comment by kcrisman created at 2010-12-02 16:34:25

What do you think needs still to be done/checked for positive review?


---

Comment by SimonKing created at 2010-12-02 16:54:53

Replying to [comment:30 kcrisman]:
> What do you think needs still to be done/checked for positive review?

I think the guide line are the new features, which are (according to the project home page):

 * v2.1.1: Usage of symbolic links to the public database, so that one can use (but of course not install) this package even without write permission in SAGE_DATA. Restructuring the code. Parallel testing is now only permitted if ticket #10004 is applied (September 2010).
 * v2.1: Support for big endian machines. 100% doctest coverage, parallel testing. New: Essential and depth essential ideals. Improved completion tests. (September 2010).

In other words, it would be good if someone who is not author (i.e., not I) does parallel tests on a machine like T2 (which is big endian), in the following setting: The package is installed by someone with write permission in SAGE_DATA, but tested by someone _without_ write permission in SAGE_DATA.

And from the mathematical point of view, one might look at essential and depth essential ideals.


---

Comment by kcrisman created at 2010-12-02 17:08:10

Hmm, I don't know how to do # 1 (though I have access to a big endian machine), since I am the only user on the box; I definitely am not enough of a group cohomology expert to do # 2!


---

Comment by SimonKing created at 2010-12-02 17:15:31

Replying to [comment:32 kcrisman]:
> Hmm, I don't know how to do # 1 (though I have access to a big endian machine), since I am the only user on the box; I definitely am not enough of a group cohomology expert to do # 2!

I did it like that: I installed Sage plus the database_gap package plus the cohomology package as root, and then I did computations in my usual account.

Another possibility: Install the package in the usual way, but then change the permissions (recursively, of course) for SAGE_DATA, so that you have read but not write permission - then you should still be able to use the package.


---

Comment by SimonKing created at 2011-05-28 09:31:26

-- bump --

Any reviewer for version 2.1.1 of the optional group cohomology package, after 6 months?


---

Comment by kcrisman created at 2011-06-01 03:12:55

I wish I could.  It seemed to work great at the time, but I just don't have the time to do the things needed to test some of the things you mention above.  It does seem a big shame it's not positively reviewed.


---

Comment by jhpalmieri created at 2011-07-20 00:32:08

I tried this out with SAGE_CHECK=yes, and I'm getting doctest failures on three different platforms: sage.math, OS X, and fulvia (a skynet machine which is OpenSolaris on x86).  I'm attaching logs for them.  On sage.math, this was based on a vanilla copy of 4.7.1.alpha4, and on the other machines, it was on top of 4.7.1.rc0.  I'm also building on the skynet machine mark, but it's abominably slow, so I don't know when it will finish.

Do I need to be concerned about these?


---

Attachment

doctest failures, sage.math.washington.edu


---

Comment by jhpalmieri created at 2011-07-20 00:32:55

doctest failures, OS X box


---

Attachment

doctest failures, OpenSolaris


---

Comment by SimonKing created at 2011-07-20 07:31:39

Hi John!

Replying to [comment:36 jhpalmieri]:
> I tried this out with SAGE_CHECK=yes, and I'm getting doctest failures on three different platforms: sage.math, OS X, and fulvia

Thank you for returning to this!

It is rather unfortunate to have failures. I hope that I will have time to fix them -- I am already in the middle of the next project.


> I'm also building on the skynet machine mark, but it's abominably slow, so I don't know when it will finish.
> 
> Do I need to be concerned about these?

I guess if there are failures on three different machines then you don't need to wait for mark.

One question: Most of the errors look like

```
    sig_on_count()
Expected:
    0
Got:
    15
```


What does that sig_on_count() mean? Does that mean that I forgot `_sig_off` after `_sig_on`?


---

Comment by jhpalmieri created at 2011-07-20 16:18:48

> What does that sig_on_count() mean? Does that mean that I forgot _sig_off after _sig_on?

I have no idea, but it sounds like a good guess to me.


---

Comment by SimonKing created at 2011-07-21 09:29:31

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-07-21 09:29:31

__Speed__

I will use the occasion to slightly modify the `MeatAxe` sources (they already _are_ modified compared with release 2.2.4):

`MeatAxe` uses plain loops to initialise memory. Actually, Michael Ringe did replace memset by such loops, in Revision 2.7. However, he does not explain why he did so.

Since most compilers should be pretty well in optimising memset (or calloc), I re-introduce the usage of memset and also of calloc. With that change, the multiplication time for two 2000x2000 matrices over GF(125) drops from 15 seconds (which already beats the default `Matrix_modn_dense` in Sage by a loooooong way!) to less than 12 seconds on my machine.

In other words, the cohomology computations should now generally be a bit faster.

__`_sig_on/_sig_off`__

Concerning sig_on_count: It is really a nice feature that the balance of _sig_on/_sig_off is automatically tested since sage-4.7.1! I went through the sources, and indeed it seems that there can be situations where an error is raised between _sig_on/_sig_off (which must be avoided).

__The other doctest failures__

- The test `pGroupCohomology.factory.CohomologyRingFactory.get_public_db` verifies that by default the public cohomology data base is in `SAGE_DATA`. Apparently that is not the case for John's Sage installations, and thus I'll remove that test.

- There is one test where non-filter-regular but algebraically independent parameters are not found in the degrees that are expected according to the doc tests. That is because algebraically _dependent_ parameters can be found with a smaller degree sum. Hence, the completion test of Peter Symonds is used, and the program does not bother to try and find the smallest possible independent parameters. So, that test has to change.

I am now preparing an update of the package and test it against sage-4.7.1.rc2. Until that's done, the ticket should be "needs work".


---

Comment by SimonKing created at 2011-07-21 10:50:08

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-07-21 10:50:08

For the record: One failure was due to a change in the `pivots()` method of Sage's matrices: They used to return a list, but apparently now it is a tuple. I took care of it.

The package is updated, so `sage -f http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-2.1.1.spkg` should now give a better result...


---

Comment by SimonKing created at 2011-07-21 10:53:02

It turns out that the documentation does not build fine. So, the reviewing should be stalled until that's fixed as well.


---

Comment by SimonKing created at 2011-07-21 10:53:02

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-07-21 12:35:11

I am now running the test suite, but I think it should be ready for review now.

It turns out that the trouble that I had with building the documentation can hardly be avoided: 

 - If one has Cython code then Python can not determine the argspec.
 - Hence, sage.misc.sageinspect.sage_getargspec tries to parse the argspec by reading the source file.
 - Here, the sources are in an spkg, and thus sage_getargspec can not read the sources.
 - By consequence, the argument list can not be figured out.

Since I define the arguments in the doc string, it is fine though, and it can't be changed anyway.


---

Comment by SimonKing created at 2011-07-21 12:35:11

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-07-21 13:10:14

On my machine, all tests pass. The package is updated, so, feel free to do 

```
sage -f http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-2.1.1.spkg
```

now. Also I have updated the [documentation](http://sage.math.washington.edu/home/SimonKing/Cohomology/)


---

Comment by jhpalmieri created at 2011-08-02 16:54:03

On the two OpenSolaris machines I have access to (David Kirkby's machine hawk, and the skynet machine fulvia), I'm getting one doctest failure:

```
File "/export/home/palmieri/.sage/temp/hawk/619/dir_0/file_14.py", line 8:                         
    sage: if sys.byteorder == 'little':                                                            
        print hash(M) == Integer(7606091044269354279)  # indirect doctest                          
    else:                                                                                          
        print hash(M) == Integer(1060097699)   # indirect doctest                                  
Expected:                                                                                          
    True                                                                                           
Got:                                                                                               
    False 
```

Otherwise, all tests pass on various platforms.


---

Comment by SimonKing created at 2012-02-05 18:21:43

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2012-02-05 18:21:43

It turns out that the package does not work with the latest sage version: It fails to install, since apparently "singular" is undefined in one method, and the new version of Cython complains if stuff is not defined. I think this is going to be 2.1.2, also with some improvements in the underlying meataxe wrapper.


---

Comment by SimonKing created at 2012-02-06 07:22:08

In fact, there are several reasons for this spkg to fail in the current Sage version. The first is the new Cython version, as explained above.

The second is the new Singular version: I see a many errors of the form 

```
// ** int division with `/`: use `div` instead in line >>  sage3687[1,tmp_i]=sage3687[1,tmp_i]**(COHO5dvNew[tmp_i]/COHO5dvOld[tmp_i]); <<
```

raised by Singular.

The third is signal handling: Most doctest failures just complain about the sig_on/sig_off count (they are supposed to come in pairs, but apparently I sometimes forgot to insert sig_off in the correct place. Thus, it seems that the doctest framework did not count sig_on/sig_off yet, when I last tested the cohomology spkg.


---

Comment by SimonKing created at 2012-02-09 20:40:11

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2012-02-09 20:40:11

I have created a new version 2.1.2, available as stated in the ticket description.

There were three independent problems:

 * Singular upgrade: Some commands have changed, and so I had to rewrite some parts of my code
 * Cython upgrade: Some code, that admittedly was buggy, might have resulted in an error at running time, and the new Cython is refusing it during compilation. So, I fixed these bugs.
 * Coercion and category framework: Some recent changes in #9138 or #11900 and related stuff, due to yours truly, have created an incompatibility with the group cohomology package: I shot myself into the foot. Now, the cohomology rings are making better use of category and coercion framework.

For me, the spkg test suite works. I didn't test on t2 or related machines, though.

Anyway, ready for review again!


---

Comment by jhpalmieri created at 2012-03-20 21:37:41

With sage-5.0.beta8-gcc, testing seems to hang on sage.math:

```

Successfully installed p_group_cohomology-2.1.2
Running the test suite for p_group_cohomology-2.1.2...
Testing the package pGroupCohomology...
Will use 9 parallel processes

pGroupCohomology.dickson has no doctest
pGroupCohomology.dickson.DICKSON.__cmp__ passes in 5.80 s
pGroupCohomology.dickson.DICKSON.__call__ passes in 5.79 s
pGroupCohomology.dickson.DICKSON.__init__ passes in 5.89 s
pGroupCohomology.dickson.DICKSON.V passes in 5.92 s
pGroupCohomology.dickson.DICKSON passes in 6.71 s
```

At this point it didn't do anything for half an hour, so I killed it.

On an OS X 10.7 box, same Sage release, I got one doctest failure:

```
There were doctest failures:
pGroupCohomology.cohomology.COHO:
sage -t -optional -long "/Users/palmieri/.sage/temp/jpalmieri538.math.washington.edu/74551/dir_0/file_25.py"
**********************************************************************
File "/Users/palmieri/.sage/temp/jpalmieri538.math.washington.edu/74551/dir_0/file_25.py", line 104:
    sage: H = CohomologyRing(8,3, from_scratch=True)
Expected:
        Computing from scratch
    Group data are rooted at ...
        Initialize cohomology ring of D8
        Computing data for Small Group number 3 of order 8
        > export action matrices
        Inserting SmallGroup(2,1) as a subgroup
        Inserting SmallGroup(4,2) as a subgroup
        Computing Dickson invariants in elementary abelian subgroup of rank 2
Got:
            Computing from scratch
    Group data are rooted at /Users/palmieri/.sage/temp/jpalmieri538.math.washington.edu/6162/tmp_0/
            Initialize cohomology ring of D8
            Computing data for Small Group number 3 of order 8
            > export action matrices
            Inserting SmallGroup(2,1) as a subgroup
            Inserting SmallGroup(4,2) as a subgroup
                The state of this cohomology ring is expected to be provided at /Users/palmieri/.sage/temp/jpalmieri538.math.washington.edu/6162/tmp_0/4gp2/dat/State.sobj
            Computing Dickson invariants in elementary abelian subgroup of rank 2
```

This one looks pretty innocuous to me...

I'm going to run doctests on OpenSolaris soon.


---

Comment by jhpalmieri created at 2012-03-20 21:37:41

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2012-03-21 02:56:25

A number of failures on OpenSolaris. Here is a [log file](http://boxen.math.washington.edu/home/palmieri/misc/p_group_cohomology-2.1.2.log).


---

Comment by SimonKing created at 2012-03-21 15:23:59

Replying to [comment:49 jhpalmieri]:
> A number of failures on OpenSolaris. Here is a [log file](http://boxen.math.washington.edu/home/palmieri/misc/p_group_cohomology-2.1.2.log).

It seems that _all_ tests fail, since there is a very basic problem:

```
ValueError: Can not create a symbolic link to the public database. Please remove /export/home/palmieri/.sage/pGroupCohomology/db/64gp158/
```


Why can the symbolic link not be created? Is that an openSolaris problem?

The rationale for introducing symbolic links was as follows:

 * The package comes with a data base, that is installed into `SAGE_DATA/pGroupCohomology`. The package may be installed by root. But even in that case, it should be possible for _all_ users to read from the database, and to extend partial computations found in the data base.
 * While reading from the data base should not be a problem, extending partial computations IS a problem, if the user has no writing permission in `SAGE_DATA`.
 * However, the user has writing permission in his/her home directory, in particular in DOT_SAGE. So, the basic idea is to put all new data there (in a sub-folder), but get existing data from `SAGE_DATA`.
 * It would be a wast of storage space to actually _copy_ the data from `SAGE_DATA` into `DOT_SAGE`. Therefore I only create links in `DOT_SAGE` that point to data in `SAGE_DATA`.
 * Hard links are problematic, because it may happen that `DOT_SAGE` and `SAGE_DATA` belong to different partitions, but hard links have to stay in one partition. That restriction does not apply to symbolic links.

So, that is why I work with symbolic links. And when I tried on T2 (which is now not available), it did work. Do you know a reason why it fails on your i386-pc-solaris2.11?

Since the error message suggests to remove something from `/export/home/palmieri/.sage/pGroupCohomology/db/`,  could you perhaps try to empty that folder, and repeat the tests?


---

Comment by SimonKing created at 2012-03-21 15:38:29

Replying to [comment:48 jhpalmieri]:
>             Inserting SmallGroup(4,2) as a subgroup
>                 The state of this cohomology ring is expected to be provided at /Users/palmieri/.sage/temp/jpalmieri538.math.washington.edu/6162/tmp_0/4gp2/dat/State.sobj

Hm. That message sounds like data have been moved accross directories.

Anyway. I just see that I get a couple of failures on sage-5.0.beta8, built with the gcc spkg from #12369. In some cases, problems with symbolic links are mentioned, or with files that can't be opened. Not good.

The good news is that I don't need to build Sage on `OpenSolaris` in order to replicated the trouble with symbolic links...


---

Comment by jhpalmieri created at 2012-03-21 21:00:24

On OpenSolaris, I deleted the ./sage/pGroupCohomology directory and reran self-tests. I got just a few failures: see  [the log file](http://sage.math.washington.edu/home/palmieri/misc/p_group_cohomology-2.1.2-new.log). I may be misreading it, but these look like optional doctests failing.


---

Comment by SimonKing created at 2012-03-22 13:58:34

Replying to [comment:52 jhpalmieri]:
> On OpenSolaris, I deleted the ./sage/pGroupCohomology directory and reran self-tests. I got just a few failures: see  [the log file](http://sage.math.washington.edu/home/palmieri/misc/p_group_cohomology-2.1.2-new.log). I may be misreading it, but these look like optional doctests failing.
> 

All but one error comes from a test that requires internet connection and tests whether the package can read download data from some repository on sage.math - and now I wonder: Isn't sage.math down at the moment?

I have just tried myself, but it failed:

```
sage: from pGroupCohomology import CohomologyRing
sage: H=CohomologyRing.web_db('8gp3') 
---------------------------------------------------------------------------
ReadError                                 Traceback (most recent call last)
...
ReadError: file could not be opened successfully
```

Indeed, the problem is on the side of sage.math, and also it doesn't help to change to boxen.math. Namely, Sage is supposed to get a g-zipped tar file out of the data base, but what it receives is an html page saying that the requested page can not be found on the server. I will ask on sage-devel what happened.

One test is about the hash of matrices. The original aim was to test against a specific value, but perhaps that was a bad idea. After all, the specific value depends on whether the machine is big or little endian, and whether it is 32 or 64 bit. So, we have four possible values.

I think the natural solution is to not test against a specific value, but against the construction of the hash.


---

Comment by SimonKing created at 2012-03-22 16:13:09

For the record: William said that the data base at sage.math.washington.edu/home/lmfdb is lost.

I hope I find some backup files, either in my home directory on sage.math, or in Jena.


---

Comment by SimonKing created at 2012-03-22 16:13:09

Remove assignee SimonKing.


---

Comment by SimonKing created at 2012-03-27 13:28:37

I have updated the spkg (at the old location).

Changes: I modified the hash function of my `MeatAxe` matrix wrapper. Before, the hash was based on the triple given by the modulus of the finite field, the dimensions of the matrix, and the contents of the memory block describing the matrix. Now, it is _only_ based on the memory block describing the matrix.

Rationale:

 * In our applications, the field is fixed, and so it does not add useful information to the hash.
 * The size of the block of memory describing the matrix gives some information about the dimensions of the matrix, such that including the _exact_ dimensions is not so important.

Also it is faster in that way:

```
sage: from pGroupCohomology.mtx import MTX
sage: M = MTX(5, [[randint(0,4) for _ in range(15)] for __ in range(15)])
sage: M.set_immutable()
sage: %timeit n = hash(M)
# With the new version
625 loops, best of 3: 750 ns per loop
# With the old version
625 loops, best of 3: 1.61 µs per loop
```


The doc test for the `__hash__` method should now be machine independent. In order to provide an indirect test, I added a method that returns a string that corresponds to the block of memory describing the matrix.

On my computer, all tests pass. Concerning the doctests marked "optional - internet": Apparently they are run by the test suite, and they pass for me as well - even though the group cohomology data base in the Sage cluster is not available anymore. Fortunately, for the single purpose of testing my package, I stored one cohomology ring at sage.math.washington.edu/home/SimonKing/Cohomology/ - and that's enough for the tests to work.

Back to "needs review", then!


---

Comment by SimonKing created at 2012-03-27 13:28:37

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2012-03-27 22:28:18

A few questions:

 - Is it possible (and easy) to build the documentation locally? If so, it would be nice to implement that in spkg-install, using the environment variable `SAGE_SPKG_INSTALL_DOCS` (see #10823).

 - Also, can you provide the code for producing an on-line database, in case people want to host their own? Can people then set a variable to point to a different web site?

 - I think a better way to disable parallel building is `export MAKE="$MAKE -j 1"`. Appending the `-j 1` at the end should override any earlier `-j` flags. But this would require testing. I also think that since you call `make` instead of `$MAKE`, maybe this is irrelevant anyway? This is all pretty minor, since it works as is.

On sage.math and on an OS X Lion box (running the version of Sage from #12369), all tests passed.  On OpenSolaris, I'm getting a few doctest failures. Several are due to the internet tests, and this machine seems to have a very slow internet connection, so I'm not going to worry about that. The remaining failure:

```
pGroupCohomology.mtx.MTX.__hash__:
sage -t -optional -long "/export/home/palmieri/.sage/temp/hawk/17706/dir_0/file_14.py"
**********************************************************************
File "/export/home/palmieri/.sage/temp/hawk/17706/dir_0/file_14.py", line 8:
    sage: if sys.byteorder == 'little':
        print hash(M) == Integer(7606091044269354279)  # indirect doctest
    else:
        print hash(M) == Integer(1060097699)   # indirect doctest
Expected:
    True
Got:
    False
**********************************************************************
```

Any ideas about this one?


---

Comment by SimonKing created at 2012-03-28 00:47:46

Replying to [comment:56 jhpalmieri]:
> A few questions:
> 
>  - Is it possible (and easy) to build the documentation locally? If so, it would be nice to implement that in spkg-install, using the environment variable `SAGE_SPKG_INSTALL_DOCS` (see #10823).

Currently, it is not possible.

For creating the docs, I am using a script that is derived from the script that builds the Sage documentation. It would, of course, be possible to include the script in the spkg

However, that would not be enough. The docs should provide the argument list of each method. In order to determine the argspec of Cython methods, it is needed to be able to read the source code (see sage.misc.sageinspect). This is of course a problem for code that is outside the Sage library. My solution: I patched sage.misc.sageinspect, such that it would find the unpacked source of the spkg locally on my computer. But other users wouldn't have the unpacked spkg lying around.

Hm. I am just thinking: If the documentation is created _during installation_, then one _does_ have the unpacked spkg. Still, I wouldn't like to patch sage.misc.sageinspect for that purpose. But perhaps the documentation builder script could hook into sage.misc.sageinspect.sage_getargspec?

Anyway, it would not be a straight forward solution.

>  - Also, can you provide the code for producing an on-line database, in case people want to host their own? 

There is no ready-made method for that purpose. What one needs to do:

 * Compute the cohomology (by default, the result is stored on disk). Make sure that the computation is "from_scratch" (there is an option of that name).
 * In case of a p-group, the data are for a single cohomology ring are distributed into many different files in a directory. Create a gzipped tar of that directory (for each group separately, I mean). This tar file is then put into the data base.
 * In case of groups that are not of prime power order, the cohomology ring is stored in a single file, and it should be this file that is put into the data base.

Do you think the following syntax (to be implemented) would be a nice addition?

```
sage: H = CohomologyRing(G, to_database="/path/to/database_folder")
sage: H.make()  # would compute the ring and create an entry in the database_folder
```



> Can people then set a variable to point to a different web site?

Yes! See the method `CohomologyRing.set_web_db(...)`.

>  - I think a better way to disable parallel building is `export MAKE="$MAKE -j 1"`. Appending the `-j 1` at the end should override any earlier `-j` flags. But this would require testing. I also think that since you call `make` instead of `$MAKE`, maybe this is irrelevant anyway?

Do I? I thought I had changed it into `$MAKE`. At least, I had the intention at some point.


> pGroupCohomology.mtx.MTX.__hash__:
> sage -t -optional -long "/export/home/palmieri/.sage/temp/hawk/17706/dir_0/file_14.py"
> **********************************************************************
> File "/export/home/palmieri/.sage/temp/hawk/17706/dir_0/file_14.py", line 8:
>     sage: if sys.byteorder == 'little':
>         print hash(M) == Integer(7606091044269354279)  # indirect doctest
>     else:
>         print hash(M) == Integer(1060097699)   # indirect doctest

That's the _old_ version of the test. Yesterday, I posted an update of the spkg, which contains a different (machine independent) test for the hash. Could you reforce installation, making sure you get the current version?


---

Comment by jhpalmieri created at 2012-03-28 04:26:39

Replying to [comment:57 SimonKing]:
> Replying to [comment:56 jhpalmieri]:
> > A few questions:
> > 
> >  - Is it possible (and easy) to build the documentation locally? If so, it would be nice to implement that in spkg-install, using the environment variable `SAGE_SPKG_INSTALL_DOCS` (see #10823).
> 
> Currently, it is not possible.

Perhaps for a future version you might consider it, depending on how much work it would be. A simple short-term solution would be to just include html docs in the spkg; they shouldn't add too much to the size. (Maybe a top-level directory `docs`, not under revision control.)

> >  - Also, can you provide the code for producing an on-line database, in case people want to host their own? 

> Do you think the following syntax (to be implemented) would be a nice addition?
> {{{
> sage: H = CohomologyRing(G, to_database="/path/to/database_folder")
> sage: H.make()  # would compute the ring and create an entry in the database_folder
> }}}

Yes, that sounds good. Maybe also a list somewhere of which specific calculations would make a good database.

> >  - I think a better way to disable parallel building is `export MAKE="$MAKE -j 1"`. Appending the `-j 1` at the end should override any earlier `-j` flags. But this would require testing. I also think that since you call `make` instead of `$MAKE`, maybe this is irrelevant anyway?
> 
> Do I? I thought I had changed it into `$MAKE`. At least, I had the intention at some point.

The spkg-install file says, for example

```
MAKE=make; export MAKE;

cd src

make
```


> > pGroupCohomology.mtx.MTX.__hash__:
> > sage -t -optional -long "/export/home/palmieri/.sage/temp/hawk/17706/dir_0/file_14.py"
> > **********************************************************************
> > File "/export/home/palmieri/.sage/temp/hawk/17706/dir_0/file_14.py", line 8:
> >     sage: if sys.byteorder == 'little':
> >         print hash(M) == Integer(7606091044269354279)  # indirect doctest
> >     else:
> >         print hash(M) == Integer(1060097699)   # indirect doctest
> 
> That's the _old_ version of the test. Yesterday, I posted an update of the spkg, which contains a different (machine independent) test for the hash. Could you reforce installation, making sure you get the current version?

You're right, I don't know how that happened. Anyway, all tests passed this time, including the internet ones.

I'm going to browse the source a bit more, but it all looks very good right now.


---

Comment by SimonKing created at 2012-03-28 05:41:05

Replying to [comment:58 jhpalmieri]:
> Perhaps for a future version you might consider it, depending on how much work it would be. A simple short-term solution would be to just include html docs in the spkg; they shouldn't add too much to the size. (Maybe a top-level directory `docs`, not under revision control.)

It is 3.4MB.

> Yes, that sounds good. Maybe also a list somewhere of which specific calculations would make a good database.

Or perhaps another syntax would be better. My previous suggestion was: "Declare during creation of a specific cohomology ring that it should go into a data base." But the computation of one ring typically involves the computation of rings for several subgroups (elementary abelian, Sylow, ...), and it would be reasonable to have them ALL in the data base.

Therefore, I think it would be better to have a _global_ switch, for example

```
sage: CohomologyRing.create_database("/path/to/data_base")
```

with the effect that all subsequent cohomology computations will work as they usually do, but would additionally write the tar files into the given data base folder.
 
> The spkg-install file says, for example
> {{{
> MAKE=make; export MAKE;

Oops. I will try what happens with parallel make - after all, the comment "Building in parallel is bad" is probably there for a reason (but I can't recall).
 
> I'm going to browse the source a bit more, but it all looks very good right now.

OK. Would it be OK to postpone the doc and data base additon, or would you strongly prefer to have it in 2.1.2 already?


---

Comment by SimonKing created at 2012-03-28 14:10:56

One question: If `$MAKE` is `make -jN`, how can one find the number N?


---

Comment by SimonKing created at 2012-03-28 16:06:03

I have updated th spkg on the old location (hence, if you download it again, make sure that you have the correct version, because sometimes wget is cached!).

Changes:

 * If `SAGE_SPKG_INSTALL_DOCS=yes` then the documentation is locally created, and copyied into SAGE_ROOT/local/share/doc/p_group_cohomology/html.
 * I tried to allow parallel make, but `MeatAxe` would fail. I do not have the energy to fix it right now. At least, I am now reverting the old setting of `MAKE` as soon as `MeatAxe` is built, but apparently for installing the Cython modules it doesn't help.

Ready for review, anyway.


---

Comment by SimonKing created at 2012-03-28 16:14:49

PS: Concerning docs, you will find that certain files such as builder.py, sageinspect.py and sage_autodoc.py are modified versions of the corresponding files from Sage. They are not doctested here. The difference to the files from Sage is that the modified versions are able to find the source files of my cohomology spkg.


---

Comment by jhpalmieri created at 2012-03-29 18:38:43

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2012-03-29 18:38:43

This looks great! Positive review. I appreciate having the documentation locally, too.

At least one thing which ought to be easy to implement in a future version: `additive_order` for elements: `a.additive_order()` should be either `1` (if `a==0`) or `p` (the characteristic of the ground field. If you ever construct cohomology rings over non-fields, you could leave it unimplemented in that case.

I found this a little strange:

```
sage: H0 = CohomologyRing(8,3)
sage: (H0.2 * H0.3).is_zero()
True
sage: (H0.2 * H0.3) == 0
False
```

Maybe comparisons or `__eq__` need to be implemented, too.


---

Comment by SimonKing created at 2012-03-29 19:06:49

Replying to [comment:63 jhpalmieri]:
> This looks great! Positive review.

Thank you very much! Finally, the old version (broken with recent Sage) can be replaced!

> sage: (H0.2 * H0.3).is_zero()
> True
> sage: (H0.2 * H0.3) == 0
> False
> Maybe comparisons or `__eq__` need to be implemented, too.

I think that the answers are consistent, for the following reasons:
 * `H0.2*H0.3` is zero in the cohomology _group_ H<sup>2</sup>(D8). As elements of that group, the product is zero, hence "is_zero()" returns True.
 * However, even though the product vanishes and thus represents a relation of the cohomology ring, it still is a cocycle of degree 2. Thus, it is not equal to `H0.zero_element()`, which is a cocycle of degree 2. Hence, the comparison with the zero of the cohomology _ring_ returns False.


---

Comment by SimonKing created at 2012-03-29 21:28:03

Changing status from positive_review to needs_info.


---

Comment by SimonKing created at 2012-03-29 21:28:03

Dear John,

I am sorry for being late, but I have one question: Would you allow one last-minute change?

Namely, with the package you just reviewed, the computation of the cohomology ring of the Sylow 2-subgroup of some double cover of Suzuki group 8 (this is group number 836 of order 128), the completion test à la Peter Symonds is very time consuming - the problem was in the computation of a small subset of generators over which the ring is finite-dimensional. I found a way to speed it up. Also, I'd like to add protocol output to the method that computes it (which also means I will have to change the expected protocol output in some doc tests).

I think these changes are minor, but helpful. If you say that you would try to install it and run the test suite again, then I would update the spkg a bit later. I would also accept to postpone that change for a later spkg version.

What do you prefer?


---

Comment by jhpalmieri created at 2012-03-29 21:51:03

Hi Simon,

I can run the test suite in the next day or two, once you update the spkg. So it's fine with me if you want to update it. If you do, could you also post a diff here, so I can see the changes? (Just `hg export tip > ...` and post the resulting patch file.)


---

Comment by SimonKing created at 2012-03-29 23:55:57

Diff of the latest changes in the spkg. For reviewing only


---

Attachment

Replying to [comment:66 jhpalmieri]:
> I can run the test suite in the next day or two, once you update the spkg. So it's fine with me if you want to update it. If you do, could you also post a diff here, so I can see the changes?

I have updated my spkg (old location) and have attache a diff with respect to the version that you have reviewed earlier.

Here are the changes:

 * The `useSlimgb` resp. `useStd` options had been used only in one location: There were several places where the default 'groebner'  method of Singular would be used, regardless of the options. That has changed in the last revision.
 * The protocol output of some methods (e.g., `dependent_parameters()`) are now providing protocol output _before_ a potentially time-consuming Gröbner basis computation is started. Background: When I computed the cohomology of `SmallGroup(128,836)` with the previous revision, I thought that it hangs in the computation of the Gröbner basis of the relation ideal - but in fact the problem was in `dependent_parameters()`, which has not been clear from the protocoll output.
 * In Symonds' criterion, parameters in degree one won't contribute to the degree in which the criterion detects completeness. Hence, adding all degree one generators to a given list of parameters will not change the degree bound -- but it may make the computation easier, because killing degree one generators greatly reduces the difficulty of Gröbner basis computations. Thus my changes in `dependent_parameters`


---

Comment by jhpalmieri created at 2012-03-30 21:01:57

Changing status from needs_info to needs_review.


---

Comment by jhpalmieri created at 2012-03-30 21:02:31

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2012-03-30 21:02:31

Okay, still looks good.


---

Comment by schilly created at 2012-04-02 11:57:12

spkg updated on the server + mirros.


---

Comment by jdemeyer created at 2012-04-02 21:10:06

Resolution: fixed

# Issue 9920: nose testing suite as an optional spkg

Issue created by migration from https://trac.sagemath.org/ticket/9921

Original creator: jason

Original creation time: 2010-09-16 17:32:19

Assignee: tbd

CC:  drkirkby jhpalmieri

Several projects we depend on use nose to do self-tests.  In order to test these packages, we'd have to have nose installed.

This is fairly simple without an spkg:


```
wget http://somethingaboutorange.com/mrl/projects/nose/nose-0.11.2.tar.gz
tar xzvf nose-0.11.2.tar.gz
cd nose-0.11.2
sage -python setup.py install  
```


However, it might make sense to have nose be an optional spkg.

Matplotlib relies on nose to do tests (http://matplotlib.sourceforge.net/devel/coding_guide.html#testing), as well as numpy/scipy (http://projects.scipy.org/numpy/wiki/TestingGuidelines).


---

Comment by jason created at 2010-09-16 17:33:20

The current website for nose is: http://code.google.com/p/python-nose/


---

Comment by drkirkby created at 2010-09-16 18:53:45

IMHO it would be sensible to have nose as a *standard* package. 

I suggested that once, and it got a luke warm reception. Having to install an optional item to test a standard package seems a bad idea to me. 

Perhaps if a list of packages which make use of 'nose' could be produced, it might be possible to argue for it to be standard. 

Dave


---

Comment by jason created at 2010-09-16 18:56:53

Yes, I'm thinking (according to guidelines) optional for now, standard after a probationary period.


---

Comment by drkirkby created at 2010-09-16 19:13:49

Replying to [comment:4 jason]:
> Yes, I'm thinking (according to guidelines) optional for now, standard after a probationary period.

Yes, according to guidelines it should be optional for a while. But there have been exceptions to that. Since it does not actually link to anything in Sage, and would only be called when running spkg-check, I think one could argue the risk is minimal. In contrast it would allow a number of packages to be checked. 

I think any such argument would have to be based on how many packages could benefit from it. 

It must be an incredibly low risk package to add. 

Dave


---

Comment by kcrisman created at 2010-09-17 00:28:18

Whether or not it should be standard, I agree that we need to at least have it optional so that it becomes more 'Sage-ic' (totally not the right adjective, but I'm groping here) to test several fundamental python packages from within Sage.  Also, it is needed to test some potential other packages, such as Brian (#9675), which is where I originally found out about this.


---

Comment by uri created at 2010-09-19 18:17:02

Replying to [comment:6 kcrisman]:
> Whether or not it should be standard, I agree that we need to at least have it optional so that it becomes more 'Sage-ic' (totally not the right adjective, but I'm groping here) to test several fundamental python packages from within Sage.  Also, it is needed to test some potential other packages, such as Brian (#9675), which is where I originally found out about this.

I installed the package and tried it to test Brian, and it worked perfectly. However, I think some changes should be made in order to fit the structure of Sage packages: all the code should be in a directory named src/, it lacks the .hg folder, the .hgignore and SPKG.txt files, etc. (see the page [Producing New Sage Packages](http://www.sagemath.org/doc/developer/producing_spkgs.html) to see how it should be).


---

Comment by leif created at 2010-09-20 02:47:01

Replying to [comment:7 uri]:
> [...] However, I think some changes should be made in order to fit the structure of Sage packages: all the code should be in a directory named src/, it lacks the .hg folder, the .hgignore and SPKG.txt files, etc. [...]

? Of course we first have to produce an spkg, be it optional or (later) standard.

Or did I miss something?


---

Comment by leif created at 2010-09-20 02:47:01

Changing type from defect to enhancement.


---

Comment by kcrisman created at 2010-09-20 02:51:36

> > [...] However, I think some changes should be made in order to fit the structure of Sage packages: all the code should be in a directory named src/, it lacks the .hg folder, the .hgignore and SPKG.txt files, etc. [...]
> 
> ? Of course we first have to produce an spkg, be it optional or (later) standard.
> 
> Or did I miss something?

No, I think that uri was perhaps misunderstanding jason's directions to use nose outside of Sage to be a suggestion for how it would become a Sage package.  No harm done in reminding us of the official rules, though :)


---

Comment by leif created at 2010-09-20 03:01:53

Replying to [comment:9 kcrisman]:
> No, I think that uri was perhaps misunderstanding jason's directions to use nose outside of Sage to be a suggestion for how it would become a Sage package.

Yeah, an spkg just containing `spkg-install` which is

```
wget http://code.google.com/p/python-nose/downloads/detail?name=nose-0.11.3.tar.gz
tar xzvf nose-0.11.3.tar.gz
cd nose-0.11.3
sage -python setup.py install  
```


:D


---

Comment by leif created at 2010-09-20 03:04:48

Ok, we should concatenate the lines with `&&` to make it more robust...


---

Comment by uri created at 2010-09-20 08:23:10

Replying to [comment:8 leif]:
> Replying to [comment:7 uri]:
> > [...] However, I think some changes should be made in order to fit the structure of Sage packages: all the code should be in a directory named src/, it lacks the .hg folder, the .hgignore and SPKG.txt files, etc. [...]
> 
> ? Of course we first have to produce an spkg, be it optional or (later) standard.
> 
> Or did I miss something?

Oh, right, I missunderstood... sorry :)


---

Comment by jason created at 2010-09-20 11:10:45

Replying to [comment:9 kcrisman]:
> > > [...] However, I think some changes should be made in order to fit the structure of Sage packages: all the code should be in a directory named src/, it lacks the .hg folder, the .hgignore and SPKG.txt files, etc. [...]
> > 
> > ? Of course we first have to produce an spkg, be it optional or (later) standard.
> > 
> > Or did I miss something?
> 
> No, I think that uri was perhaps misunderstanding jason's directions to use nose outside of Sage to be a suggestion for how it would become a Sage package.  No harm done in reminding us of the official rules, though :)

Yep, the point of the instructions was to show that even without an spkg, using nose "is fairly simple without an spkg".  Of course, you can't download something in the spkg, so those instructions would not work for an spkg.  However, it would be a very generic spkg-install file that would basically do the normal standard checks and then run "python setup.py install".


---

Comment by kcrisman created at 2010-09-21 01:25:07

I tried using nose, and it was very interesting.  Tested Brian on two different boxes, and then tested both numpy and scipy on OS X 10.6 - discovered no errors on the first, and a fair number on the second!  So I think that there should be no doubt this could go straight to optional if an spkg was made.

I couldn't do

```
import matplotlib
matplotlib.test()
```

because for some reason our matplotlib doesn't have this method.

Much less importantly, I should also point out that on OS X `wget` is not a builtin, though I have an alias `curl -O` that seems to accomplish the same purpose.  I just downloaded and double-clicked, actually :)


---

Comment by kcrisman created at 2012-05-26 20:11:26

Nose is now on Github: [https://github.com/nose-devs/nose](https://github.com/nose-devs/nose).


---

Comment by jhpalmieri created at 2012-06-14 23:18:21

I've posted an spkg. It builds well enough for me, but I haven't actually used it to test anything except for itself (in spkg-check).


---

Comment by jhpalmieri created at 2012-06-14 23:18:21

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2012-06-14 23:19:08

scripts repo


---

Attachment


---

Comment by jhpalmieri created at 2012-06-14 23:24:53

By the way, version 1.1.2 was the most recent version for which I could find a tar ball. Or we could use the version from github; would that be better?


---

Comment by jhpalmieri created at 2012-06-14 23:33:45

I've now also prepared a version from git. This one fails its own self tests, though ;)


---

Comment by jhpalmieri created at 2012-06-14 23:39:10

patch for spkg, for review only


---

Attachment

patch for spkg, for review only (version 1.1.3)


---

Comment by kcrisman created at 2012-06-15 01:50:21

> I've now also prepared a version from git. This one fails its own self tests, though ;)
Interesting!

You can try using it with the brian optional spkg, and I believe numpy and mpl also use this?


---

Comment by jason created at 2012-06-15 04:08:41

ipython also uses nose.


---

Comment by jhpalmieri created at 2012-06-15 17:13:11

I tried running self-tests with numpy, using `python -c 'import numpy; numpy.test()'`. The good news: tests ran. The bad news: some tests failed. More bad news: this exited with a return code of zero, so it's hard to tell (within spkg-check, for example), that tests failed. I have the same issue with IPython.


---

Comment by kcrisman created at 2012-06-15 17:17:45

So is that a problem with nose or a problem with the numpy/ipython test suites?  Sounds like nose is ready from this point of view :)


---

Comment by jhpalmieri created at 2012-06-15 23:14:31

Changing keywords from "" to "sd41".


---

Comment by kcrisman created at 2012-07-05 17:20:35

This is ridiculous.  Nose works fine at testing things on sage.math.   It certainly finds various errors and warnings - apparently scipy generates a number as well, I just tried it.

The issue with it not passing its own tests is not so good, and I can confirm this in both cases.  On the plus side, it only breaks the Sage installation process in the 1.1.3, so I would say let's go with the 1.1.2 for now.

----

I do get something weird, hopefully unrelated to nose itself, but instead related to our defaults for matplotlib.

```

kcrisman@sage:~/sage-5.1.beta1-boxen-x86_64-Linux$ ./sage -c 'import matplotlib; matplotlib.test()'
======================================================================
ERROR: Failure: OSError (No such file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/import matplotlib; matplotlib.test())
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/local/lib/python2.7/site-packages/nose-1.1.2-py2.7.egg/nose/failure.py", line 39, in runTest
    raise self.exc_class(self.exc_val)
OSError: No such file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/import matplotlib; matplotlib.test()

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)

sage: import matplotlib  
sage: matplotlib.test()
======================================================================
ERROR: Failure: ValueError (Unable to load tests from file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/sage)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/local/lib/python2.7/site-packages/nose-1.1.2-py2.7.egg/nose/loader.py", line 213, in loadTestsFromFile
    % filename)
ValueError: Unable to load tests from file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/sage

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
False
```



On a computer without nose:

```

sage: matplotlib.test()
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/Users/karl-dietercrisman/Downloads/sage-5.1.beta6/<ipython console> in <module>()

/Users/.../sage-5.1.beta6/local/lib/python2.7/site-packages/matplotlib/__init__.pyc in test(verbosity)
    986 def test(verbosity=0):
    987     """run the matplotlib test suite"""
--> 988     import nose
    989     import nose.plugins.builtin
    990     from testing.noseclasses import KnownFailure

ImportError: No module named nose
```


I think that in matplotlib's lib/__init__.py

```

    success = nose.run( defaultTest=default_test_modules,
                        config=config,
                        )
```

we aren't using the right default modules, they aren't imported or something.  So it goes back to just looking at `.` for the default test module - I get the same thing.

```

sage: nose.run(defaultTest='.')                 
E
======================================================================
ERROR: Failure: ValueError (Unable to load tests from file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/sage)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/local/lib/python2.7/site-packages/nose-1.1.2-py2.7.egg/nose/loader.py", line 213, in loadTestsFromFile
    % filename)
ValueError: Unable to load tests from file /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/sage

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)
False
```


Can you see a reason why this shouldn't have positive review?  I just think this must be a problem in how we're dealing with mpl.  I'm surprised it does this; we only removed the baseline images, not the testing scripts!


---

Comment by mraum created at 2013-01-24 12:47:06

I have also reviewed this ticket, since I think it is important to have it. The matplotlib error is really a bug (or at least laxness) in matplotlib. If we waited for nosetest to be included until all spkg's pass, we would wait until the cows come home.

If nobody objects, I will set this to positive review by next week.


---

Comment by mraum created at 2013-01-29 17:24:50

Changing status from needs_review to positive_review.


---

Comment by schilly created at 2013-01-30 16:31:25

spkg is put on the servers.


---

Comment by jdemeyer created at 2013-01-30 16:35:14

Resolution: fixed

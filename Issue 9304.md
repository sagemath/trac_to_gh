# Issue 9304: trac #8218 (finite_rings) broke all my pickles!

Issue created by migration from https://trac.sagemath.org/ticket/9304

Original creator: was

Original creation time: 2010-06-22 06:33:00

Assignee: was

I have a lot of pickles here (in the data directory):

http://sage.math.washington.edu/home/wstein/db/modsym/

All the ones without "aplist" in their name were broken by trac #8218 which rearranged code without any backwards compatibility imports.    This should have never happened. Sigh.

Anyway, my pickles are fixed by just adding back one file. 


---

Comment by was created at 2010-06-22 06:34:26

Changing status from new to needs_review.


---

Attachment


---

Comment by davidloeffler created at 2010-06-28 18:34:59

This is arguably my fault, since I reviewed #8218. Anyway, we have a much nicer way of fixing unpickling problems now, without all of these annoying file stubs lying around. 

```
sage: load('http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj')
Attempting to load remote file: http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj
Loading: [..................................................]
((1088, 2), (0.69604299999997465, 1.0720680000000016, 8.3885230000000206, 11.104694999999936, 21.261328999999932), Modular Symbols space of dimension 148 for Gamma_0(1088) of weight 2 with sign 1 over Rational Field)
```


You know better than I do whether that's the right output, but at least it isn't raising an error.


---

Comment by cremona created at 2010-10-12 11:35:15

What would be a good way to test this for review?


---

Comment by davidloeffler created at 2010-10-12 12:11:32

Hi John,

Try running the command 

```
sage: load('http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj')
```


with and without the patch (either one!) applied. Without the patch you'll get an error similar to the one Salman Baig reports on sage-devel ([here](http://groups.google.co.uk/group/sage-devel/browse_thread/thread/f208f9d1548564ee/d989b029608fa6ee)). With the patch it should load fine.


---

Comment by cremona created at 2010-10-12 13:20:55

With either patch the load is OK but does give a deprecation warning:

```
sage: load('http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj')
Attempting to load remote file: http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj
Loading: [..................................................]
/home/jec/sage-current/local/lib/python2.6/site-packages/IPython/iplib.py:2073: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
  exec code_obj in self.user_global_ns, self.user_ns
((1088, 2), (0.69604299999997465, 1.0720680000000016, 8.3885230000000206, 11.104694999999936, 21.261328999999932), Modular Symbols space of dimension 148 for Gamma_0(1088) of weight 2 with sign 1 over Rational Field)
```

which is exactly the same warning as I get without the patch.  Am I doing something stupid here?

Of the two patches, I prefer the second ("alternative") since it implements a more general method, and does not need to create that little dummy (almost) file.


---

Comment by cremona created at 2010-10-12 13:20:55

Changing keywords from "" to "pickling".


---

Comment by cremona created at 2010-10-12 13:20:55

Changing status from needs_review to needs_info.


---

Comment by davidloeffler created at 2010-10-12 13:37:05

That's weird: it really shouldn't work without the patch! If I run that command in a clean 4.6.alpha3 build, I get the same DeprecationWarning but it's followed by `ImportError: No module named integer_mod_ring`. Did you try running it _before_ installing either patch? 

If you install William's patch, build, and then qpop it and build again, the file it re-creates will still be lurking in your build directory. If that's the case try switching to a clean branch to see the `ImportError`.


---

Comment by cremona created at 2010-10-12 13:49:03

Changing status from needs_info to needs_review.


---

Comment by cremona created at 2010-10-12 13:49:03

I think you are right.  I tried it before applying patches, saw that something was not right but did not copy the output.  When I tried again after removing the patches (using hg qpop and sage -br) it still works!

But I just tried again on another machine, still 4.6.alpha3, and with no patches the load command gives

```
sage: load('http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj')
Attempting to load remote file: http://sage.math.washington.edu/home/wstein/db/modsym/data/gamma0-1088-2.sobj
Loading: [..................................................]
/home/jec/sage-current/local/lib/python2.6/site-packages/IPython/iplib.py:2073: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
  exec code_obj in self.user_global_ns, self.user_ns
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/home/jec/sage-4.6.alpha3/devel/sage-main/<ipython console> in <module>()

/home/jec/sage-current/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.load (sage/structure/sage_object.c:7486)()

/home/jec/sage-current/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:9052)()

/home/jec/sage-current/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.unpickle_global (sage/structure/sage_object.c:8659)()

ImportError: No module named integer_mod_ring
```


It's a mystery that popping the patches left a setup in which the load works;  and that left open the possibility that the only reason why the second patch worked was that the effect of the first patch was still around (!) so on the second machine I applied the second patch without previously applying the first, and that still worked.

Moreover, then popping the second patch put the system back properly (the load again fails).

So I am giving the *second* patch a positive review.


---

Comment by cremona created at 2010-10-12 13:49:14

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-01 10:06:55

Resolution: fixed


---

Comment by jdemeyer created at 2010-11-01 10:06:55

Merged alternative patch

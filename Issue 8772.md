# Issue 8772: Maxima interface chokes randomly

Issue created by migration from https://trac.sagemath.org/ticket/8772

Original creator: dunfield

Original creation time: 2010-04-26 21:00:59

Assignee: was

CC:  leif mpatel dimpase pbruin @spaghettisalat

Keywords: Maxima

Sufficiently many calls to Maxima eventually causes that interface to throw an exception, some samples of which are given below.    A minimal piece of code exhibiting this problem is


```
def prob(): 
    for i in xrange(1000000): 
        a = var('a') 
        eqn = (a - 1)/(a) 
        eqn.numerator() 
```

This error has been observed in Sage 4.3.* on OS X.5.* (8-core Xeon Mac Pro and 2-core Intel Core 2 Mac Book), and Ubuntu Linux 9.10 (quad-core Intel Core 2).  See the sage-devel thread [http://groups.google.com/group/sage-devel/browse_thread/thread/3b43147e44324c25](http://groups.google.com/group/sage-devel/browse_thread/thread/3b43147e44324c25) for some discussion.  In particular, it may be related to #5662 where the synchronization with Maxima was getting lost on  certain multi-core CPUs because of something related to switching between cores.   It takes some time, e.g. 5-15 minutes for the problem to manifest itself.  

Typical errors:


```
TypeError: unable to make sense of Maxima expression 
'"__SAGE_SYNCHRO_MARKER_202188656"' in Sage 

TypeError: Error executing code in Maxima 
CODE: 
        _tmp_ : -(a0-1)*a1^2*a3$ 
Maxima ERROR: 
_tmp_ : -(a0-1)*a1^2*a3$ 
stdin:57338284:Incorrect syntax: Illegal use of delimiter ) 
(%i832002) 
stdin:57338357:Incorrect syntax: Premature termination of input at ;. 
(%i832003) 
```



---

Comment by drkirkby created at 2010-08-31 16:46:25

On the following system, with Sage 4.5.3.alpha2. 

 * Sun Ultra 27
 * 3.33 GHz Intel Xeon W3580 CPU. 4 cores. 8 threads. (Hyperthreaded)
 * 12 GB of ECC DDR3 RAM
 * 2 x 500 GB disks (both mirrored)
 * 2 x 2 TB disks (both mirrored)
 * ZFS 128-bit file system, which should detect and correct errors
 * OpenSolaris 06/2009.

which is not a cheap PC, but a decent workstation, I see this error 4 times when 


```
make ptestlong
```


was run 100 times. So it's causing  `make ptestlong ` to fail in 4% of cases for me. Since this machine is hyperthreaded and has 4 cores, 8 threads would be run when the doctests were run. I've checked the system logs and there are now reported hardware problems.

The following tests failed one or more times


```
devel/sage-main/sage/modular/overconvergent/weightspace.py (twice)
devel/sage/sage/tests/benchmark.py (once)
devel/sage/sage/calculus/desolvers.py (once)
```


In each case, although the exact error message is different, I always see:


```
Premature termination of input
```


Dave


---

Comment by drkirkby created at 2010-08-31 16:58:36

Replying to [comment:1 drkirkby]:
>  I've checked the system logs and there are now reported hardware problems.

I mean there were *no* reported hardware problems.


---

Comment by drkirkby created at 2010-08-31 17:17:38

I'm removing the 'Author' field, as nobody has actually written anything to solve it yet - or at least if they did, there's nothing on the ticket to indicate they did. 

Dave


---

Comment by mpatel created at 2010-08-31 22:01:51

Could you give the exact messages for each of the failed files?


---

Comment by drkirkby created at 2010-08-31 22:48:34

Replying to [comment:4 mpatel]:
> Could you give the exact messages for each of the failed files?

Sure. I will attach four files


```
run-21-weightspace.py.txt
run-34-benchmark.py.txt
run-60-weightspace.py.txt
run-90-desolvers.py.txt
```


which show the errors on my 21st, 34th, 60th and 90th runs. They correspond to a failure of 


```
devel/sage-main/sage/modular/overconvergent/weightspace.py (21st and 60th run)
devel/sage/sage/tests/benchmark.py (34th run)
devel/sage/sage/calculus/desolvers.py (90th run)
```


Dave


---

Attachment

Failed devel/sage-main/sage/modular/overconvergent/weightspace.py (first of two failures of this test)


---

Comment by drkirkby created at 2010-08-31 23:21:21

Failed devel/sage/sage/tests/benchmark.py


---

Attachment

Failed devel/sage-main/sage/modular/overconvergent/weightspace.py (second failure)


---

Attachment

Failed devel/sage/sage/calculus/desolvers.py


---

Attachment

I was unable to attach the files earlier, as trac was not working correctly (/var was full). 

Note Alex Ghitza said on sage-devel that `modular/overconvergent/weightspace.py` has no reason to use Maxima, so he created a patch to fix that #9843. Of course, that does not help solve the underlying problem here. 

Dave.


---

Comment by leif created at 2010-09-02 01:23:16

I could reproduce Nathan's error with Sage 4.5.3.rc0 on Ubuntu 10.04 x86_64 (Core2), but only in conjunction with heavy system load:

```
13943 a - 1
13944 a - 1
13945---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/leif/Sage/sage-4.5.3.rc0/<ipython console> in <module>()

/home/leif/Sage/sage-4.5.3.rc0/<ipython console> in prob()

/home/leif/Sage/sage-4.5.3.rc0/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.numerator (sage/symbolic/expression.cpp:21226)()

/home/leif/Sage/sage-4.5.3.rc0/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._maxima_ (sage/symbolic/expression.cpp:3382)()

/home/leif/Sage/sage-4.5.3.rc0/local/lib/python2.6/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3501)()

/home/leif/Sage/sage-4.5.3.rc0/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
   1030             
   1031         if isinstance(x, basestring):
-> 1032             return cls(self, x, name=name)
   1033         try:
   1034             return self._coerce_from_special_method(x)

/home/leif/Sage/sage-4.5.3.rc0/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1449             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1450                 self._session_number = -1
-> 1451                 raise TypeError, x
   1452         self._session_number = parent._session_number
   1453 

TypeError: Error executing code in Maxima
CODE:
	sage75684 : ((a)+(-1))*((a)^(-1))$
Maxima ERROR:
	 Incorrect syntax: Illegal use of delimiter )
(%i529800) Incorrect syntax: Premature termination of input at $.
(%i529801) 
 sage: 
```

(I've added `print i, ` to the last line of his example.)

Doctesting in parallel with 32 threads (`ptestlong`) btw. gave no errors. I'll have to inspect the log of the run with 64 threads, but IIRC there was only one "intentional" timeout due to SIGALARM set to 1 second... (128 threads exceeded my physical memory, i.e. caused massive swapping.)

I couldn't post this earlier either because of trac errors... ;-)


---

Comment by leif created at 2010-09-02 02:04:22

Replying to [comment:7 leif]:
> Doctesting in parallel with 32 threads (`ptestlong`) btw. gave no errors. I'll have to inspect the log of the run with 64 threads, but IIRC there was only one "intentional" timeout due to SIGALARM set to 1 second...

Not really (the run with 64 threads):

```
...
 
----------------------------------------------------------------------

The following tests failed:

	sage -t  -long devel/sage/sage/interfaces/expect.py # 1 doctests failed
	sage -t  -long devel/sage/sage/symbolic/expression.pyx # 1 doctests failed
	sage -t  -long devel/sage/sage/schemes/elliptic_curves/heegner.py # 1 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1799.8 seconds
```

The failing tests:

```
sage -t  -long devel/sage/sage/interfaces/expect.py
**********************************************************************
File "/home/leif/Sage/sage-4.5.3.rc0/devel/sage-main/sage/interfaces/expect.py", line 808:
    sage: print sage0.eval("alarm(1); singular._expect_expr('1')")
Expected:
    Control-C pressed.  Interrupting Singular. Please wait a few seconds...
    ...
    KeyboardInterrupt: computation timed out because alarm was set for 1 seconds
Got:
    ---------------------------------------------------------------------------
    KeyboardInterrupt                         Traceback (most recent call last)
    <BLANKLINE>
    /home/leif/Sage/sage-4.5.3.rc0/data/extcode/sage/<ipython console> in <module>()
    <BLANKLINE>
    /home/leif/Sage/sage-4.5.3.rc0/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _expect_expr(self, expr, timeout)
        815             expr = self._prompt_wait
        816         if self._expect is None:
    --> 817             self._start()
        818         try:
        819             if timeout:
    <BLANKLINE>
    /home/leif/Sage/sage-4.5.3.rc0/local/lib/python2.6/site-packages/sage/interfaces/singular.pyc in _start(self, alt_message)
        373         """
        374         self.__libs = []
    --> 375         Expect._start(self, alt_message)
        376         # Load some standard libraries.
        377         self.lib('general')   # assumed loaded by misc/constants.py
    <BLANKLINE>
    /home/leif/Sage/sage-4.5.3.rc0/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _start(self, alt_message, block_during_init)
        449             self._expect = pexpect.spawn(cmd, logfile=self.__logfile)
        450             if self._do_cleaner():
    --> 451                 cleaner.cleaner(self._expect.pid, cmd)
        452             
        453         except (ExceptionPexpect, pexpect.EOF, IndexError):
    <BLANKLINE>
    /home/leif/Sage/sage-4.5.3.rc0/local/lib/python2.6/site-packages/sage/interfaces/cleaner.pyc in cleaner(pid, cmd)
         30     o.write('%s %s\n'%(pid, cmd))
         31     o.close()
    ---> 32     start_cleaner_if_not_running()
         33 
         34 ################
    <BLANKLINE>
    /home/leif/Sage/sage-4.5.3.rc0/local/lib/python2.6/site-packages/sage/interfaces/cleaner.pyc in start_cleaner_if_not_running()
         41         return
         42     except (IOError, OSError, ValueError):
    ---> 43         os.system('sage-cleaner &')   # it has died
         44         
         45 
    <BLANKLINE>
    /home/leif/Sage/sage-4.5.3.rc0/local/lib/python2.6/site-packages/sage/misc/misc.pyc in __mysig(a, b)
       1695 __alarm_time=0
       1696 def __mysig(a,b):
    -> 1697     raise KeyboardInterrupt, "computation timed out because alarm was set for %s seconds"%__alarm_time
       1698 
       1699 def alarm(seconds):
    <BLANKLINE>
    KeyboardInterrupt: computation timed out because alarm was set for 1 seconds
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_15
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/leif/.sage//tmp/.doctest_expect.py
	 [101.9 s]
```

(I think this is ok, as mentioned.)


```
sage -t  -long devel/sage/sage/symbolic/expression.pyx
**********************************************************************
File "/home/leif/Sage/sage-4.5.3.rc0/devel/sage-main/sage/symbolic/expression.pyx", line 1146:
    sage: (x > 2).assume()
Expected nothing
Got:
    Maxima crashed -- automatically restarting.
**********************************************************************
1 items had failures:
   1 of  15 in __main__.example_36
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/leif/.sage//tmp/.doctest_expression.py
	 [564.5 s]
```

This might also simply be a timeout.


```
sage -t  -long devel/sage/sage/schemes/elliptic_curves/heegner.py
**********************************************************************
File "/home/leif/Sage/sage-4.5.3.rc0/devel/sage-main/sage/schemes/elliptic_curves/heegner.py", line 6946:
    sage: QQ[sqrt(-195)].class_number()
Exception raised:
    Traceback (most recent call last):
      File "/home/leif/Sage/sage-4.5.3.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/leif/Sage/sage-4.5.3.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/leif/Sage/sage-4.5.3.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_235[7]>", line 1, in <module>
        QQ[sqrt(-Integer(195))].class_number()###line 6946:
    sage: QQ[sqrt(-195)].class_number()
      File "ring.pyx", line 205, in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2556)
      File "/home/leif/Sage/sage-4.5.3.rc0/local/lib/python/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py", line 343, in PolynomialRing
        R = _single_variate(base_ring, name, sparse, implementation)
      File "/home/leif/Sage/sage-4.5.3.rc0/local/lib/python/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py", line 395, in _single_variate
        name = normalize_names(1, name)
      File "parent_gens.pyx", line 204, in sage.structure.parent_gens.normalize_names (sage/structure/parent_gens.c:2093)
      File "parent_gens.pyx", line 145, in sage.structure.parent_gens._certify_names (sage/structure/parent_gens.c:1650)
    ValueError: variable names must be alphanumeric, but one is 'sqrt(-195)' which is not.
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_235
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/leif/.sage//tmp/.doctest_heegner.py
	 [1178.8 s]
```

No idea. I get the same error if I just type that line in Sage. Doctesting the file succeeds...

Oh wait, that was the Sage session that gave the Maxima error! After restarting Sage, I get the expected result:

```
...
TypeError: Error executing code in Maxima
CODE:
	sage75684 : ((a)+(-1))*((a)^(-1))$
Maxima ERROR:
	 Incorrect syntax: Illegal use of delimiter )
(%i529800) Incorrect syntax: Premature termination of input at $.
(%i529801) 
 sage: 

sage: 
sage: QQ[sqrt(-195)].class_number()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/leif/Sage/sage-4.5.3.rc0/<ipython console> in <module>()

/home/leif/Sage/sage-4.5.3.rc0/local/lib/python2.6/site-packages/sage/rings/ring.so in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:2556)()

/home/leif/Sage/sage-4.5.3.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in PolynomialRing(base_ring, arg1, arg2, sparse, order, names, name, implementation)
    341                 raise TypeError, "if second arguments is a string with no commas, then there must be no other non-optional arguments"
    342             name = arg1
--> 343             R = _single_variate(base_ring, name, sparse, implementation)
    344         else:
    345             # 2-4. PolynomialRing(base_ring, names, order='degrevlex'):

/home/leif/Sage/sage-4.5.3.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.pyc in _single_variate(base_ring, name, sparse, implementation)
    393 def _single_variate(base_ring, name, sparse, implementation):
    394     import sage.rings.polynomial.polynomial_ring as m
--> 395     name = normalize_names(1, name)
    396     key = (base_ring, name, sparse, implementation)
    397     R = _get_from_cache(key)

/home/leif/Sage/sage-4.5.3.rc0/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.normalize_names (sage/structure/parent_gens.c:2093)()

/home/leif/Sage/sage-4.5.3.rc0/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens._certify_names (sage/structure/parent_gens.c:1650)()

ValueError: variable names must be alphanumeric, but one is 'sqrt(-195)' which is not.
sage: 
Exiting Sage (CPU time 1m33.85s, Wall time 1921m38.11s).
Exiting spawned Maxima process.
leif@quadriga:~/Sage/sage-4.5.3.rc0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: QQ[sqrt(-195)].class_number()
4
sage: 
```

(I exited Sage as usual - with Control-D; just in case you wonder.)


---

Comment by rws created at 2018-03-10 07:22:33

FWIW, the original code in the description no longer calls Maxima in `numer()`, so a better example is needed.


---

Comment by mkoeppe created at 2020-07-04 18:22:41

Again seeing similar failures in #22191 (update ECL to 20.4.24) on Cygwin


---

Comment by kcrisman created at 2020-10-08 12:48:18

See https://groups.google.com/forum/#!topic/sage-devel/U1dsVFP-2PA


---

Comment by kcrisman created at 2020-10-08 12:48:18

Changing priority from critical to major.


---

Comment by mkoeppe created at 2021-04-07 19:29:15

Sage development has entered the release candidate phase for 9.3. Setting a new milestone for this ticket based on a cursory review.

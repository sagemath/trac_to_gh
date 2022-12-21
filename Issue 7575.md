# Issue 7575: EllipticCurve.gens: height bounds not handled well in two_descent

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-12-01 21:56:26

Assignee: cremona

The documentation for `EllipticCurve.gens` says:

```
HINT: If you would like to control the height bounds used in the
2-descent, first call the two_descent function with those height
bounds. However that function, while it displays a lot of output,
returns no values.
```


However, this doesn't work, because `EllipticCurve.gens` doesn't know about it:


```
sage: x,y=var('x,y')
sage: E = EllipticCurve(y^2 + x*y + y == x^3 - 10525529*x - 21714803524)
sage: E.two_descent(second_limit=11, verbose=False)
sage: E.gens()
*BOOM*
```


Despite:


```
sage: A = E.mwrank_curve()
sage: A.gens()
[This is the Trac macro *1737553736529419603224344006006032245457891558644991945121564365621L, -1605018042749306385493128932071874233128412498544999275367916849231954L, 2038538889602737161869943561394015059980551394212496529475951L* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1737553736529419603224344006006032245457891558644991945121564365621L, -1605018042749306385493128932071874233128412498544999275367916849231954L, 2038538889602737161869943561394015059980551394212496529475951L-macro)
```



---

Comment by rlm created at 2010-01-02 15:17:25

With the patch `trac_7575-heegner_index_example.patch` applied on top of (sage-4.3 plus) #7576 and #7819, I get the following:


```
sage: E = EllipticCurve('123a1')
sage: E.prove_BSD(verbosity=2)
p = 2: true by 2-descent
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
...<SNIP>...
/Users/rlmill/sage-4.3/local/lib/python2.6/site-packages/sage/libs/mwrank/interface.pyc in gens(self)
    310         """
    311         self.saturate()
--> 312         return eval(self.__two_descent_data().getbasis().replace(":",","))
    313 
    314     def certain(self):

RuntimeError: 
```



---

Comment by rlm created at 2010-01-02 15:17:25

Changing status from new to needs_info.


---

Comment by cremona created at 2010-01-03 18:27:43

In the original example (in this ticket's description), note that calling E.two_descent() produces output to the screen but returns nothing and stores nothing in E which was not there before.  E.gens() by default uses mwrank_shell, which does not allow any passing of parameters (see the TODO block in the docstring), not because it cannot be done but because we have not implemented it.  The non-default option mwrank_lib goes via creation of the associated mwrank_curve which also does not allow changing of the parameters.

What I suggest is that we use mwrank_lib by default;  that we allow passing of all the parameters which the two_descent function of an mwrank elliptic curve allows from all higher level functions which call mwrank (e.g. gens()) and that we use the enquiry functions provided by mwrank to find out how successful it has been:  it can give you a lower and upper bound for the rank, so all is well if they are equal and in any case can give you a number of gens equal to the lower bound.  The only difficulty would be with caching rank and gens -- probably best not to do so at all unless we have certainly found them.

Does this all make sense?  I think it would be much more helpful to have sample curves where things do not work well and sample code which does not go via a call to the (presumably complicated) function prove_BSD()!


---

Comment by cremona created at 2010-01-03 18:29:47

Another thought:  perhaps we should have a class to hold a list of all mwrank-options.


---

Comment by rlm created at 2010-01-19 21:46:20

Here is another part where using the library would help:

```
sage: EllipticCurve([1, 1, 1, -9718914979, 370891890941633]).mwrank()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (47, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (362, 0))

---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/Users/rlmill/sage-4.3.1.rc1/devel/sage-main/<ipython console> in <module>()

/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in mwrank(self, options)
    484             from sage.interfaces.all import Mwrank
    485             mwrank = Mwrank(options=options)
--> 486         return mwrank(list(self.a_invariants()))
    487 
    488     def conductor(self, algorithm="pari"):

/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/interfaces/mwrank.pyc in __call__(self, cmd)
     75 
     76     def __call__(self, cmd):
---> 77         return self.eval(str(cmd))
     78 
     79     def eval(self, *args, **kwds):

/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/interfaces/mwrank.pyc in eval(self, *args, **kwds)
     95             # Doing _start again fixes that always. See trac #5157.
     96             self._start()
---> 97         return Expect.eval(self, *args, **kwds)
     98 
     99     def console(self):

/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in eval(self, code, strip, synchronize, locals, **kwds)
    981         try:
    982             with gc_disabled():
--> 983                 return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
    984         except KeyboardInterrupt:
    985             # DO NOT CATCH KeyboardInterrupt, as it is being caught

/Users/rlmill/sage-4.3.1.rc1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _eval_line(self, line, allow_use_file, wait_for_prompt)
    666                         # we expect to get an EOF if we're quitting.
    667                         return ''
--> 668                     raise RuntimeError, "%s\n%s crashed executing %s"%(msg,self, line)
    669                 out = E.before
    670             else:

RuntimeError: End Of File (EOF) in read_nonblocking(). Empty string style platform.
<pexpect.spawn instance at 0xebec738>
version: 2.0 ($Revision: 1.151 $)
command: /Users/rlmill/sage-4.3.1.rc1/local/bin/mwrank
args: ['/Users/rlmill/sage-4.3.1.rc1/local/bin/mwrank']
patterns:
    Enter curve: 
buffer (last 100 chars): 
before (last 100 chars): up to 232549 (square a first...)
Attempt to round -9608958007.0937 to a long int fails, aborting!

after: <class 'pexpect.EOF'>
match: None
match_index: None
exitstatus: None
flag_eof: 1
pid: 90387
child_fd: 7
timeout: None
delimiter: <class 'pexpect.EOF'>
logfile: None
maxread: 10000
searchwindowsize: None
delaybeforesend: 0
Mwrank crashed executing [1, 1, 1, -9718914979, 370891890941633]
```



---

Comment by cremona created at 2010-01-19 21:56:34

This behaviour is supposed to be caught by mwrank C++ code, so that this can be detected gracefully by using the ok() function.

As we are planning to replace the pexpect interface entirely this will be dealt with.  (There is absolutely no reason to use the interactive interface when everything can be found from the library interface.)


---

Comment by cremona created at 2010-01-19 22:02:04

Replying to [comment:5 cremona]:
> This behaviour is supposed to be caught by mwrank C++ code, so that this can be detected gracefully by using the ok() function.

On looking into it, I see that this will need a patch to the file src/qrank/mrank1.cc, since I just call abort() when I try to round to a long int and it overflows.  Instead I need to catch that properly.  (Pity C++ does not have the try/except functionality of python).

So this particular bug / behaviour needs to be flagged as "report upstream (done) and wait for a patch from upstream (on my todo list)".


> 
> As we are planning to replace the pexpect interface entirely this will be dealt with.  (There is absolutely no reason to use the interactive interface when everything can be found from the library interface.)


---

Comment by rlm created at 2010-01-19 22:11:48

The documentation for `EllipticCurve.gens` says:

```
HINT: If you would like to control the height bounds used in the
2-descent, first call the two_descent function with those height
bounds. However that function, while it displays a lot of output,
returns no values.
```


However, this doesn't work, because `EllipticCurve.gens` doesn't know about it:


```
sage: x,y=var('x,y')
sage: E = EllipticCurve(y^2 + x*y + y == x^3 - 10525529*x - 21714803524)
sage: E.two_descent(second_limit=11, verbose=False)
sage: E.gens()
*BOOM*
```


Despite:


```
sage: A = E.mwrank_curve()
sage: A.gens()
[This is the Trac macro *1737553736529419603224344006006032245457891558644991945121564365621L, -1605018042749306385493128932071874233128412498544999275367916849231954L, 2038538889602737161869943561394015059980551394212496529475951L* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1737553736529419603224344006006032245457891558644991945121564365621L, -1605018042749306385493128932071874233128412498544999275367916849231954L, 2038538889602737161869943561394015059980551394212496529475951L-macro)
```



---

Comment by rlm created at 2010-02-03 05:11:13

Changing status from needs_info to needs_review.


---

Comment by cremona created at 2010-02-04 14:34:41

The 1st and 4th items in the TODO list are implemented in #8184 with a new spkg and subsequent patch,

I think that logically that patch should be reviewed first, and then this one will need so changes (since a lot of the same functions are affected).  I hope others (rlm in particular) will agree!  For that reason (only) I have switched this to "needs work".


---

Comment by cremona created at 2010-02-04 14:34:41

Changing status from needs_review to needs_work.


---

Attachment

depends on #8184, #8155 (and possibly #8124)


---

Comment by rlm created at 2010-02-04 21:02:34

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-02-06 17:58:11

I applied trac_7575.patch successfully to 4.3.2 after first applying everything from 
#8184, #8155 and  #8124 in that order.

The code looks good.  It's great now that we do not have to make embarrassing excuses for mwrank's incomplete output!

I only spotted one thing:  in a couple of places the docstring says that the default search bound is 16, whereas it is in fact 12.  (Certainly 12 is more sensible!)  That needs changing (trivial).  It might be a good idea to alert the user to how expensive (in time) adding one to the bound is, so that (for example) a bound of 20 could lead to the program never ending.

One other comment (to rlm):   when doing descent by 2-isogeny, when the second descent is used and the coefficients are large, it is a good idea to increase the decimal precision a lot (to 100 or 200 digits) because then the reduction of the second descent quartics is done much better.  Now, mwrank will not do that for you (though perhaps it should).  I suggest that when mwrank is used on curves with 2-torsion, we first call mwrank_set_precision(200).  This will not slow anything down (in fact the opposite) -- but that is not the case for 2-descent in general (no 2-torsion).  Perhaps we could do that on another ticket.

I tested the whole library with -long after applying this patch and the earlier ones on which it depends (as well as the new eclib spkg at #8184):  all pass!

I really hope that this sequence of 4 tickets can all be merged quickly into 4.3.3.


---

Comment by cremona created at 2010-02-06 17:58:11

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-02-06 17:59:25

PS Robert, please look at those second descent default search limits:  16 is really large, and when I looked again I saw that you really do have 16 as the default.  I would suggest using 12.


---

Comment by rlm created at 2010-02-07 02:04:42

Fixes default search bounds


---

Attachment

This last patch sets all defaults (and docstrings) to 12.


---

Comment by cremona created at 2010-02-07 11:18:30

With the new version of trac_7575-followup.patch everything is 100% fine.

Recap: apply everything from #8184, #8155 and #8124 in that order and then both patches here in order.  All tests pass, and all looks (very) good!


---

Comment by mpatel created at 2010-02-11 00:16:17

In preparing for 4.3.3.alpha0, I noticed a [minor?] problem : After I run `sage -t ell_rational_field.py`, there's a new untracked file in the repository:

```
$ hg stat
? sage/schemes/elliptic_curves/PRIMES
m
```

It contains `16180561` and sometimes `19047851`.  If this is easy to fix, feel free to add another follow-up patch here.


---

Comment by cremona created at 2010-02-11 09:25:43

Sorry about that.  When eclib programs run they leave behind a file of that name (containing large primes found during the computations, for use in later runs).  And it is left in the working directory.  This is probably leftover from a testrun I did before committing changes.

I think all will be well if you just delete that file.


---

Comment by mpatel created at 2010-02-11 10:37:47

It reappears after `make ptestlong`, or anywhere I run a `sage -t` command that includes `ell_rational_field.py`.  Is it possible to save the file to a fixed location?

We could 

 * Add a line to `.hgignore`.
 * Not add a line to `MANIFEST.in`.

This should ensure the file is not included in a new `sage-*.spkg`.  But users might complain about the new file appearing elsewhere.


---

Comment by mpatel created at 2010-02-11 10:45:57

Add `PRIMES` to `.hgignore`.  Apply in addition to other patches.


---

Attachment

I've attached an "hgignore" patch we can use for 4.3.3.alpha0, if it's OK.


---

Comment by cremona created at 2010-02-11 11:10:06

I'm not quite sure why this has arisen as an issue now, since mwrank/eclib have always used this file.  Was it just that I forgot to delete it when preparing the spkg?  In which case I could just make a small change to the new eclib spkg at #8184?


---

Comment by mpatel created at 2010-02-11 11:47:45

Is it a consequence of

```diff
-             algorithm='mwrank_shell',
+             algorithm='mwrank_lib',
```

in `EllipticCurve_rational_field.gens` and/or `EllipticCurve_rational_field.rank`?


---

Comment by cremona created at 2010-02-11 11:57:48

Replying to [comment:20 mpatel]:
> Is it a consequence of
> {{{
> #!diff
> -             algorithm='mwrank_shell',
> +             algorithm='mwrank_lib',
> }}}
> in `EllipticCurve_rational_field.gens` and/or `EllipticCurve_rational_field.rank`?

No, that should not make any difference.


---

Comment by mpatel created at 2010-02-11 13:02:05

If I replace `algorithm='mwrank_lib'` with `algorithm='mwrank_shell'` in both argspecs and run `sage -b; sage -t ell_rational_field.py`, the `PRIMES` file does not appear.  Am I missing something?


---

Comment by mpatel created at 2010-02-11 14:32:34

Resolution: fixed


---

Comment by mpatel created at 2010-02-11 14:32:34

For the record: The "hgignore" patch is _not_ in 4.3.3.alpha0.


---

Comment by cremona created at 2010-02-11 17:38:59

I have made some progress in tracking this down.   
    1. When the mwrank shell starts up, it looks to see if there is a file in the local directory called PRIMES.  If so, it reads in the contents and uses them (without checking their primality) in a trial division stage of integer factorization.
    2. The function that does that is called initprimes().  This function is wrapped in Sage but as far as I can see is not called when the library is used.  This should possibly be changed.
    3. When integers are factored there is an initial trial division stage.  Primes which are detected this way (e.g. if trial division goes up to their square root) are added to a list which is maintained for the session to help in future trial divisions.
    4. On exit, if there are any primes in the maintained list (which might be there either because they are read at the start or added when found) then that list is output to a file called PRIMES.  In the working directory, and created if it does not already exist, or overwritten if it does.

Now, two of the curves in the doctests for ell_rational_field.rank, namely [1,0,0,0,37455] and [0,0,1,-79,342], have large primes in their discriminants, namely 16180561 and 19047851.  These are added to the maintained list of primes when found, and therefore on exit should be output to the file PRIMES.

I do not know why the output file is only being produced when mwrank_lib is used.  I would expect it to be the other way round!  The writing to file is done by a function called when a global instance of a C++ class has its destructor called.  I know that that happens when a normal binary finishes executing (since the compiler puts in calls to relevant destructors).  But I don't see why those destructors would be called when the library is used.  (Until Sage, I had never used my own C++ code as a library in this way, so my knowledge of C++ runs out here.)

One solution would be to *only* output to the file PRIMES if it already exists.  That way, users of mwrank can still use the functionality it provides (by creating an empty file at the start) but Sage can ignore it.  This would require a new patch to the eclib code, to be applied after the one recently applied (p9).


---

Comment by rlm created at 2010-02-11 17:50:20

Replying to [comment:24 cremona]:
> One solution would be to *only* output to the file PRIMES if it already exists.

Wouldn't it be better to simply set the location to something in `DOT_SAGE`, instead of the current directory?


---

Comment by cremona created at 2010-02-11 19:55:45

Trouble is, eclib currently does not allow this to be changed, it always uses the current dir.  I can change that (as I have changed many other similar hard-wired things specifically for Sage!).  But it also would require another patch to eclib.


---

Comment by mpatel created at 2010-02-15 13:06:49

I inserted diagnostic "cout" statements in `extra_prime_class::~extra_prime_class` and ran a few tests.  It seems the destructor always gets called, but the timing --- and whether `PRIMES` is actually written to the file system, it seems --- depends on whether I use the library or pexpect interface.

The pexpect interface reads `SAGE_ROOT/data/extcode/mwrank/PRIMES`.  But it doesn't update this file when I quit the Sage command line.  However, if I run

```
sage -c "EllipticCurve([1,0,0,0,37455]).rank(proof=False)"
```

then "hg stat", for example, confirms the file has changed.

Would it help to call a `exitprimes` method explicitly, near the end of `main`?  This _might_ avoid problems related to when the runtime calls the destructor.

Disclaimer:  I'm not at all familiar with eclib.


---

Comment by cremona created at 2010-02-25 09:21:35

The quickest quick fix would be just to comment out line 372 in src/procs/marith.cc (in eclib).

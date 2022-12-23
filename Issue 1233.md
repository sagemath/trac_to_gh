# Issue 1233: mwrank wrapper causes crashes and error on non-minimal curves

Issue created by migration from https://trac.sagemath.org/ticket/1233

Original creator: cremona

Original creation time: 2007-11-21 10:25:30

Assignee: jec

I found that elliptic curves which are defined by non-minimal equations cause rank() etc to crash or give error messages.  Possibly only when there is 2-torsion.  Since mwrank itself handles the same curves with no problem, there is a problem with the wrapper code.  First here are two examples of what goes wrong:

sage: E=mwrank_EllipticCurve([-1323,3942])
sage: E.rank()
Result of shifting the point [36:-108:1] is [1:-1:1] which is not a valid point on its curve [0,0,0,-1323,3942]!
Point [1:-1:1], height = 3.1490443504515297201640615419259554770993208565687 --warning: NOT on curve!
1
sage: E=EllipticCurve([-1323,3942])
sage: E.rank()
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/home/jec/tex/papers/<ipython console> in <module>()

/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in rank(self, use_database, verbose, only_use_mwrank, algorithm, proof)
    989         elif algorithm == 'mwrank_shell':
    990             misc.verbose("using mwrank shell")
--> 991             X = self.mwrank()
    992             if not 'The rank and full Mordell-Weil basis have been determined unconditionally' in X:
    993                 if proof:

/home/src/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in mwrank(self, options)
    163             from sage.interfaces.all import Mwrank
    164             mwrank = Mwrank(options=options)
--> 165         return mwrank(self.a_invariants())
    166
    167     def conductor(self, algorithm="pari"):

/home/src/sage/local/lib/python2.5/site-packages/sage/interfaces/mwrank.py in __call__(self, cmd)
     69
     70     def __call__(self, cmd):
---> 71         return self.eval(str(cmd))
     72
     73     def console(self):

/home/src/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in eval(self, code, strip, **kwds)
    705         try:
    706             with gc_disabled():
--> 707                 return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
    708         except KeyboardInterrupt:
    709             # DO NOT CATCH KeyboardInterrupt, as it is being caught

/home/src/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py in _eval_line(self, line, allow_use_file, wait_for_prompt)
    641                         # we expect to get an EOF if we're quitting.
    642                         return ''
--> 643                     raise RuntimeError, "%s\n%s crashed executing %s"%(msg,self, line)
    644                 out = E.before
    645             else:

<type 'exceptions.RuntimeError'>: End Of File (EOF) in read_nonblocking(). Exception style platform.
<pexpect.spawn instance at 0x982f58c>
version: 2.0 ($Revision: 1.151 $)
command: /home/src/sage/local/bin/mwrank
args: ['/home/src/sage/local/bin/mwrank']
patterns:
    Enter curve:
buffer (last 100 chars):
before (last 100 chars): [0, 0, 0, -1323, 3942]

after: <class 'pexpect.EOF'>
match: None
match_index: None
exitstatus: None
flag_eof: 1
pid: 6057
child_fd: 3
timeout: None
delimiter: <class 'pexpect.EOF'>
logfile: None
maxread: 10000
searchwindowsize: None
delaybeforesend: 0
Mwrank crashed executing [0, 0, 0, -1323, 3942]

Explanation:   In the stand-alone mwrank binary (run via !mwrank for example) curves are converted to minimal models after input and any points computed are converted back so that the points output are on the input curve (!).  But the Sage wrapper does not so this and everything gets confused.

One solution would be for me to change the mwrank code itself so that the two_descent class itself handled the minimalization.  That would be cleanest, and would not require any changes to the Sage wrapping.  Otherwise, as with Simon's code, we would run up against the fact that currently Sage has no means of changing models and points itself.

So I guess this lands on my own to-do list.

jec


---

Comment by cremona created at 2007-11-21 10:26:56

Apologies for the hopeless formatting of the above, which looked quite different before I pressed the "submit" button.


---

Comment by robertwb created at 2007-12-05 19:29:39

See model-changing code at #1239


---

Attachment


---

Attachment


---

Attachment


---

Comment by cremona created at 2007-12-19 11:33:26

I have changed the mwrank source code so that non-minimal models are now handled properly.  All the work is done on a minimal model, but opints are mapped back to the input model if that is different.

Note that it is not correct to say that this was a Sage-wrapping problem!   The stand-alone mwrank binary used to manage this properly by converting to a minimal model before calling the two_descent class, and the latter just assumed it was being given a minimal model.  The Sage wrapping went straight into the two_descent.  Now, the two_descent class handles this itself (so that the mwrank.cc program has less to do).

I will attach a bundle which corrects this;  it should be possible to apply this to the cremona*.spkg in Sage 2.9.

No, that failed, since it did not recognise the parent.  Help!


---

Comment by cremona created at 2007-12-19 13:19:56

An updated spkg which solves this and fixes some other bugs is at

http://www.warwick.ac.uk/staff/J.E.Cremona/cremona-20071219.spkg


---

Comment by mabshoff created at 2007-12-19 14:22:42

And 

http://sage.math.washington.edu/home/mabshoff/cremona-20071219.p0.spkg

builds :)

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-19 17:13:02

With the above spkg I get doctest failures for:

```
devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py
devel/sage-main/sage/schemes/elliptic_curves/sha.py
devel/sage-main/sage/libs/mwrank/interface.py
```

One example:

```
sage: EllipticCurve('11a').regulator()
-infinity
sage:
Exiting SAGE (CPU time 0m0.17s, Wall time 0m8.09s).
fatal error:
    Internal error: can't free this _ntl_gbigint
exit...
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-12-20 12:09:46

John Cremona fixed the issue mentioned above. I applied the patch to 

http://sage.math.washington.edu/home/mabshoff/cremona-20071219.p1.spkg

Make also sure to apply #1573 and touch mwrank.pyx due to #1574. -testall passes on sage.math.

Cheers,

Michael


---

Comment by rlm created at 2007-12-20 18:08:15

`cremona-20071219.p1.spkg` and #1573 merged in 2.9.1 alpha2


---

Comment by rlm created at 2007-12-20 18:08:15

Resolution: fixed

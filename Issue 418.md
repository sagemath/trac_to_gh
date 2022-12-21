# Issue 418: Wrap MiniSAT

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-08-10 15:18:34

Assignee: was

CC:  polybori fichtejo abmasse sbulygin

Make an optional SAGE package for MiniSAT (http://www.cs.chalmers.se/Cs/Research/FormalMethods/MiniSat/) an award winning SAT solver. Also implement/port Nicolas Courtois' and Gregory Bard's ANF to CNF converter (http://eprint.iacr.org/2006/402.pdf) to SAGE.


---

Comment by pdenapo created at 2007-09-16 19:49:20

Actually there are many SAT solvers out of there

http://www.cs.ubc.ca/~hoos/SATLIB/solvers.html

and many of them understand a commond format, the conjuntive normal form in the DIMACS format: 

http://www.cs.ubc.ca/~hoos/SATLIB/Benchmarks/SAT/satformat.ps

An important first step, would be creating a method for the symbolic logic class that supports output of a formula in the DIMACS format


---

Comment by mabshoff created at 2009-04-03 00:46:16

#5671 is a duplicate of this ticket.

Cheers,

Michael


---

Comment by was created at 2009-04-03 13:45:51

#5671 a special case of what is asked for in this ticket.  This ticket seems to be about wrapping multiple SAT solvers, and implementing porting ANF and CNF codes to Sage.   By the way, in wrapping minisat the first thing we did was *not* use DIMACS format for the wrapper, since that all goes via string processing, and we want a direct C library interface.  DIMACS format should also be supported at some point though.


---

Comment by malb created at 2009-08-25 19:17:39

Btw. there are two independent open-source ANF2CNF converters available now:

 * http://bitbucket.org/malb/algebraic_attacks/src/tip/anf2cnf.py
 * http://bitbucket.org/brickenstein/polybori-scripts/src/tip/cnf.py

The later will be available in PolyBoRi soon, I am not sure whether the former is completely redundant because of the later. More benchmarks are needed to figure this out I guess.


---

Comment by malb created at 2011-08-25 06:38:08

Changing status from new to needs_review.


---

Comment by malb created at 2011-08-25 06:38:08

an optional SPKG is available here:

    http://sage.math.washington.edu/home/malb/spkgs/cryptominisat-2.9.1.spkg


---

Comment by was created at 2012-01-04 21:22:57

See also #11479.


---

Comment by malb created at 2012-06-03 19:51:57

Changing status from needs_review to needs_work.


---

Comment by malb created at 2012-06-03 19:51:57

See
  https://bitbucket.org/malb/sage-cryptominisat
  https://bitbucket.org/malb/cryptominisat-spkg
for a C++ interface to CryptoMiniSat from !Sage. The basic solver works, but lots of work is still to be done.


---

Comment by malb created at 2012-06-03 19:55:40

New SPKG here: http://sage.math.washington.edu/home/malb/spkgs/cryptominisat-2.9.4.spkg


---

Comment by kcrisman created at 2012-06-04 19:13:59

What is the relationship of this ticket to #5671 and #11479?  I feel like they could be considered dups, but they both have code attached and after all there are other such solvers out there.


---

Comment by kcrisman created at 2012-06-04 20:51:40

At #11479 the suggestion was to make sure there was a generic backend for eventually having interfaces with other solvers (presumably using some of the code there).  Would that be pretty easy to do with this, or pretty challenging?  It sounds like fichtejo is interested in helping with that, if it is practical/meaningful; naturally, it may be the case that combining any of these pieces would be too challenging to be practical.


---

Comment by malb created at 2012-06-15 16:18:25

Changing status from needs_work to needs_review.


---

Comment by malb created at 2012-06-15 16:18:25

Changing keywords from "" to "SAT".


---

Comment by malb created at 2012-06-16 15:28:11

I rebased https://bitbucket.org/malb/sage-cryptominisat to 5.0.1


---

Comment by malb created at 2012-06-28 13:01:51

Anyone up for reviewing this?


---

Comment by AlexanderDreyer created at 2012-06-28 13:21:47

Replying to [comment:15 malb]:
> Anyone up for reviewing this?
I'll have a look at it. What about kcrisman's questions?


---

Comment by kcrisman created at 2012-06-28 13:36:15

> > Anyone up for reviewing this?
> I'll have a look at it. What about kcrisman's questions?
malb considers them more or less dupes (at least #5671), especially since he added DIMACS to this ticket.  I am not knowledgeable enough to say whether that is legitimate, but had just wanted to point it out.


---

Comment by malb created at 2012-06-28 15:13:51

I should mention that I didn't implement reading from DIMACS files. I did implement exporting to DIMACS but perhaps some people would find this interface not that nice. I find it reasonably elegant though because it is quite modular:


```
sage: from sage.sat.converters.polybori import CNFEncoder        
sage: solver = sage.sat.solvers.dimacs.DIMACS(filename="mycnf.cnf")
sage: F,s = mq.SR(1,2,2,4,gf2=True,polybori=True).polynomial_system()
sage: encoder = CNFEncoder(solver, F.ring())
sage: _ = encoder(F)
sage: solver.write()
'mycnf.cnf'
```



---

Comment by Bouillaguet created at 2012-06-29 09:57:34

Installation of the spkg fails on my 32-bit ubuntu 12.04.


```
g++ -DHAVE_CONFIG_H -I. -I.. -I/usr/local/sage/local/include -Wall -I. -I./../MTRand -I./../mtl -fopenmp -I/usr/local/sage/local/include -L/usr/local/sage/local/lib -g -fPIC -Wall -pedantic -O2 -MT DimacsParser.lo -MD -MP -MF .deps/DimacsParser.Tpo -c DimacsParser.cpp  -fPIC -DPIC -o .libs/DimacsParser.o
DimacsParser.cpp: In member function ‘void CMSat::DimacsParser::parse_DIMACS(T) [with T = _IO_FILE*]’:
DimacsParser.cpp:482:60:   instantiated from here
DimacsParser.cpp:461:33: erreur: no matching function for call to ‘StreamBuffer::StreamBuffer(_IO_FILE*&)’
DimacsParser.cpp:461:33: note: candidates are:
StreamBuffer.h:59:5: note: StreamBuffer::StreamBuffer(gzFile)
StreamBuffer.h:59:5: note:   no known conversion for argument 1 from ‘_IO_FILE*’ to ‘gzFile’
StreamBuffer.h:29:7: note: StreamBuffer::StreamBuffer(const StreamBuffer&)
StreamBuffer.h:29:7: note:   no known conversion for argument 1 from ‘_IO_FILE*’ to ‘const StreamBuffer&’
make[2]: *** [DimacsParser.lo] Erreur 1
```



---

Comment by malb created at 2012-06-29 10:07:39

Ah, it's a known issue and the next release of CryptoMiniSat is supposed to fix this:

http://lists.gforge.inria.fr/pipermail/cryptominisat-devel/2012-June/000325.html


---

Comment by malb created at 2012-06-29 10:07:39

Changing status from needs_review to needs_work.


---

Comment by AlexanderDreyer created at 2012-06-29 14:47:51

I have the same issue here. But I can give the sage library part already a positive review.


---

Comment by AlexanderDreyer created at 2012-06-29 14:51:38

PS: It seems that Mate has just release cryptominisat 2.9.5: https://gforge.inria.fr/frs/?group_id=1992&release_id=7438


---

Comment by malb created at 2012-06-29 16:08:20

Changing status from needs_work to needs_review.


---

Comment by malb created at 2012-06-29 16:09:05

I've updated the SPKG to 2.9.5 and I have also added a patch to the Sage interface which deals with GCC 4.7.0 being more strict (I believe) about `return 1;` from void function.


---

Comment by AlexanderDreyer created at 2012-07-01 21:46:17

Changing status from needs_review to needs_work.


---

Comment by AlexanderDreyer created at 2012-07-01 21:46:17

It seems that interfaces had changes, so the spkg doesn't fit with the sage library patches.
It seems that your installation picked up the headers from the old install. Maybe its enough to delete `SAGE_INC+"/cryptominisat/`?

I fixed a few trivial things below, but there's more to be done:
{{{ #!diff
diff -r ef5eaff5d6cd module_list.py
--- a/module_list.py    Fri Jun 29 17:04:34 2012 +0100
+++ b/module_list.py    Sun Jul 01 23:40:53 2012 +0200
`@``@` -1891,12 +1891,12 `@``@`
     ext_modules.extend([
         Extension("sage.sat.solvers.cryptominisat.cryptominisat",
                   ["sage/sat/solvers/cryptominisat/cryptominisat.pyx"],
-                  include_dirs = [SAGE_INC, SAGE_INC+"/cryptominisat/mtl", SAGE_INC+"/cryptominisat/Solver"],
+                  include_dirs = [SAGE_INC, SAGE_INC+"/cmsat/"],
                   language = "c++",
                   libraries = ['cryptominisat', 'z']),
         Extension("sage.sat.solvers.cryptominisat.solverconf",
                   ["sage/sat/solvers/cryptominisat/solverconf.pyx", "sage/sat/solvers/cryptominisat/solverconf_helper.cpp"],
-                  include_dirs = [SAGE_INC, SAGE_INC+"/cryptominisat/mtl", SAGE_INC+"/cryptominisat/Solver"],
+                  include_dirs = [SAGE_INC, SAGE_INC+"/cmsat/"],
                   language = "c++",
                   libraries = ['cryptominisat', 'z'])
         ])
diff -r ef5eaff5d6cd sage/sat/solvers/cryptominisat/solverconf_helper.h
--- a/sage/sat/solvers/cryptominisat/solverconf_helper.h        Fri Jun 29 17:04:34 2012 +0100
+++ b/sage/sat/solvers/cryptominisat/solverconf_helper.h        Sun Jul 01 23:40:53 2012 +0200
`@``@` -14,7 +14,7 `@``@`
  *                  http://www.gnu.org/licenses/
  ****************************************************************************/

-#include <cryptominisat/Solver/SolverConf.h>
+#include <SolverConf.h>

 enum sc_type {
   t_int      = 1<<0,
}}}


---

Comment by malb created at 2012-07-02 14:12:47

I've updated the interface to work with 2.9.5. Thanks for spotting this!


---

Comment by malb created at 2012-07-02 14:12:47

Changing status from needs_work to needs_review.


---

Comment by malb created at 2012-07-11 14:03:48

ping :)


---

Comment by AlexanderDreyer created at 2012-07-11 15:23:02

The spkg installs and I was also able to pull from Sage 5.1(rc0) with automated merge. First tests succeeded, So we are close to a positive review, I'm just waiting for `make ptestlong` to finish.


---

Comment by AlexanderDreyer created at 2012-07-11 21:14:48

Changing status from needs_review to positive_review.


---

Comment by AlexanderDreyer created at 2012-07-11 21:14:48

Ok, tests succeeded, so I can give positive review.


---

Comment by jdemeyer created at 2012-07-13 12:09:16

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-07-13 12:09:16

`_sig_on` and `_sig_off` are deprecated since sage-4.7.  Use `sig_on()` and `sig_off()` instead.  See #10115 (and note the reviewer of that ticket!).


---

Comment by jdemeyer created at 2012-07-13 12:16:32

Changing component from packages to optional packages.


---

Comment by malb created at 2012-07-13 17:00:50

Doh! Fixed: https://bitbucket.org/malb/sage-cryptominisat/changeset/bf994dfe464e


---

Comment by jdemeyer created at 2012-07-13 21:42:01

Changing status from needs_work to positive_review.


---

Comment by schilly created at 2012-07-16 16:50:01

i just put the spkg on the server+mirrors.


---

Comment by jdemeyer created at 2012-07-27 21:03:52

Okay, I'm testing the repo.  *Please don't change it* anymore (unless of course this ticket gets set to needs_work for some reason).


---

Comment by jdemeyer created at 2012-07-31 17:43:36

There is a problem with `sage/sat/solvers/cryptominisat/solverconf_helper.cpp` not showing up in a Sage source distribution, a fix is to appear at #13315.


---

Comment by jdemeyer created at 2012-08-12 18:57:35

Resolution: fixed


---

Comment by jdemeyer created at 2015-09-30 13:13:37

Does anybody remember why this sentence was added to the documentation?

```
        - If the solver was interrupted before deciding satisfiability
          ``None``.
```

I don't believe that this claim is true.


---

Comment by jdemeyer created at 2015-09-30 13:18:17

And even if it were true, I wouldn't like it (interrupts should `raise KeyboardInterrupt`).


---

Comment by malb created at 2015-09-30 13:30:52

You can limit the SAT solver. For example, you can tell it to only do x restarts. In this case, we might not know if the problem is satisfiable, so we return `None`.


---

Comment by jdemeyer created at 2015-09-30 13:32:47

I see, so the interrupts this talks about do not refer to `KeyboardInterrupt`s (a.k.a. CTRL-C)?


---

Comment by malb created at 2015-09-30 13:51:05

IIRC, yep.

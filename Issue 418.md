# Issue 418: Wrap MiniSAT

archive/issues_000418.json:
```json
{
    "body": "Assignee: was\n\nCC:  polybori fichtejo abmasse sbulygin\n\nMake an optional SAGE package for MiniSAT (http://www.cs.chalmers.se/Cs/Research/FormalMethods/MiniSat/) an award winning SAT solver. Also implement/port Nicolas Courtois' and Gregory Bard's ANF to CNF converter (http://eprint.iacr.org/2006/402.pdf) to SAGE.\n\nIssue created by migration from https://trac.sagemath.org/ticket/418\n\n",
    "created_at": "2007-08-10T15:18:34Z",
    "labels": [
        "packages",
        "minor",
        "enhancement"
    ],
    "title": "Wrap MiniSAT",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/418",
    "user": "malb"
}
```
Assignee: was

CC:  polybori fichtejo abmasse sbulygin

Make an optional SAGE package for MiniSAT (http://www.cs.chalmers.se/Cs/Research/FormalMethods/MiniSat/) an award winning SAT solver. Also implement/port Nicolas Courtois' and Gregory Bard's ANF to CNF converter (http://eprint.iacr.org/2006/402.pdf) to SAGE.

Issue created by migration from https://trac.sagemath.org/ticket/418





---

archive/issue_comments_002060.json:
```json
{
    "body": "Actually there are many SAT solvers out of there\n\nhttp://www.cs.ubc.ca/~hoos/SATLIB/solvers.html\n\nand many of them understand a commond format, the conjuntive normal form in the DIMACS format: \n\nhttp://www.cs.ubc.ca/~hoos/SATLIB/Benchmarks/SAT/satformat.ps\n\nAn important first step, would be creating a method for the symbolic logic class that supports output of a formula in the DIMACS format",
    "created_at": "2007-09-16T19:49:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2060",
    "user": "pdenapo"
}
```

Actually there are many SAT solvers out of there

http://www.cs.ubc.ca/~hoos/SATLIB/solvers.html

and many of them understand a commond format, the conjuntive normal form in the DIMACS format: 

http://www.cs.ubc.ca/~hoos/SATLIB/Benchmarks/SAT/satformat.ps

An important first step, would be creating a method for the symbolic logic class that supports output of a formula in the DIMACS format



---

archive/issue_comments_002061.json:
```json
{
    "body": "#5671 is a duplicate of this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-03T00:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2061",
    "user": "mabshoff"
}
```

#5671 is a duplicate of this ticket.

Cheers,

Michael



---

archive/issue_comments_002062.json:
```json
{
    "body": "#5671 a special case of what is asked for in this ticket.  This ticket seems to be about wrapping multiple SAT solvers, and implementing porting ANF and CNF codes to Sage.   By the way, in wrapping minisat the first thing we did was *not* use DIMACS format for the wrapper, since that all goes via string processing, and we want a direct C library interface.  DIMACS format should also be supported at some point though.",
    "created_at": "2009-04-03T13:45:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2062",
    "user": "was"
}
```

#5671 a special case of what is asked for in this ticket.  This ticket seems to be about wrapping multiple SAT solvers, and implementing porting ANF and CNF codes to Sage.   By the way, in wrapping minisat the first thing we did was *not* use DIMACS format for the wrapper, since that all goes via string processing, and we want a direct C library interface.  DIMACS format should also be supported at some point though.



---

archive/issue_comments_002063.json:
```json
{
    "body": "Btw. there are two independent open-source ANF2CNF converters available now:\n\n   * http://bitbucket.org/malb/algebraic_attacks/src/tip/anf2cnf.py\n   * http://bitbucket.org/brickenstein/polybori-scripts/src/tip/cnf.py\n\nThe later will be available in PolyBoRi soon, I am not sure whether the former is completely redundant because of the later. More benchmarks are needed to figure this out I guess.",
    "created_at": "2009-08-25T19:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2063",
    "user": "malb"
}
```

Btw. there are two independent open-source ANF2CNF converters available now:

   * http://bitbucket.org/malb/algebraic_attacks/src/tip/anf2cnf.py
   * http://bitbucket.org/brickenstein/polybori-scripts/src/tip/cnf.py

The later will be available in PolyBoRi soon, I am not sure whether the former is completely redundant because of the later. More benchmarks are needed to figure this out I guess.



---

archive/issue_comments_002064.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-25T06:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2064",
    "user": "malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_002065.json:
```json
{
    "body": "an optional SPKG is available here:\n\n    http://sage.math.washington.edu/home/malb/spkgs/cryptominisat-2.9.1.spkg",
    "created_at": "2011-08-25T06:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2065",
    "user": "malb"
}
```

an optional SPKG is available here:

    http://sage.math.washington.edu/home/malb/spkgs/cryptominisat-2.9.1.spkg



---

archive/issue_comments_002066.json:
```json
{
    "body": "See also #11479.",
    "created_at": "2012-01-04T21:22:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2066",
    "user": "was"
}
```

See also #11479.



---

archive/issue_comments_002067.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-06-03T19:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2067",
    "user": "malb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_002068.json:
```json
{
    "body": "See\n  https://bitbucket.org/malb/sage-cryptominisat\n  https://bitbucket.org/malb/cryptominisat-spkg\nfor a C++ interface to CryptoMiniSat from !Sage. The basic solver works, but lots of work is still to be done.",
    "created_at": "2012-06-03T19:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2068",
    "user": "malb"
}
```

See
  https://bitbucket.org/malb/sage-cryptominisat
  https://bitbucket.org/malb/cryptominisat-spkg
for a C++ interface to CryptoMiniSat from !Sage. The basic solver works, but lots of work is still to be done.



---

archive/issue_comments_002069.json:
```json
{
    "body": "New SPKG here: http://sage.math.washington.edu/home/malb/spkgs/cryptominisat-2.9.4.spkg",
    "created_at": "2012-06-03T19:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2069",
    "user": "malb"
}
```

New SPKG here: http://sage.math.washington.edu/home/malb/spkgs/cryptominisat-2.9.4.spkg



---

archive/issue_comments_002070.json:
```json
{
    "body": "What is the relationship of this ticket to #5671 and #11479?  I feel like they could be considered dups, but they both have code attached and after all there are other such solvers out there.",
    "created_at": "2012-06-04T19:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2070",
    "user": "kcrisman"
}
```

What is the relationship of this ticket to #5671 and #11479?  I feel like they could be considered dups, but they both have code attached and after all there are other such solvers out there.



---

archive/issue_comments_002071.json:
```json
{
    "body": "At #11479 the suggestion was to make sure there was a generic backend for eventually having interfaces with other solvers (presumably using some of the code there).  Would that be pretty easy to do with this, or pretty challenging?  It sounds like fichtejo is interested in helping with that, if it is practical/meaningful; naturally, it may be the case that combining any of these pieces would be too challenging to be practical.",
    "created_at": "2012-06-04T20:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2071",
    "user": "kcrisman"
}
```

At #11479 the suggestion was to make sure there was a generic backend for eventually having interfaces with other solvers (presumably using some of the code there).  Would that be pretty easy to do with this, or pretty challenging?  It sounds like fichtejo is interested in helping with that, if it is practical/meaningful; naturally, it may be the case that combining any of these pieces would be too challenging to be practical.



---

archive/issue_comments_002072.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-06-15T16:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2072",
    "user": "malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_002073.json:
```json
{
    "body": "Changing keywords from \"\" to \"SAT\".",
    "created_at": "2012-06-15T16:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2073",
    "user": "malb"
}
```

Changing keywords from "" to "SAT".



---

archive/issue_comments_002074.json:
```json
{
    "body": "I rebased\u00a0https://bitbucket.org/malb/sage-cryptominisat\u00a0to 5.0.1",
    "created_at": "2012-06-16T15:28:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2074",
    "user": "malb"
}
```

I rebased https://bitbucket.org/malb/sage-cryptominisat to 5.0.1



---

archive/issue_comments_002075.json:
```json
{
    "body": "Anyone up for reviewing this?",
    "created_at": "2012-06-28T13:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2075",
    "user": "malb"
}
```

Anyone up for reviewing this?



---

archive/issue_comments_002076.json:
```json
{
    "body": "Replying to [comment:15 malb]:\n> Anyone up for reviewing this?\nI'll have a look at it. What about kcrisman's questions?",
    "created_at": "2012-06-28T13:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2076",
    "user": "AlexanderDreyer"
}
```

Replying to [comment:15 malb]:
> Anyone up for reviewing this?
I'll have a look at it. What about kcrisman's questions?



---

archive/issue_comments_002077.json:
```json
{
    "body": "> > Anyone up for reviewing this?\n> I'll have a look at it. What about kcrisman's questions?\nmalb considers them more or less dupes (at least #5671), especially since he added DIMACS to this ticket.  I am not knowledgeable enough to say whether that is legitimate, but had just wanted to point it out.",
    "created_at": "2012-06-28T13:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2077",
    "user": "kcrisman"
}
```

> > Anyone up for reviewing this?
> I'll have a look at it. What about kcrisman's questions?
malb considers them more or less dupes (at least #5671), especially since he added DIMACS to this ticket.  I am not knowledgeable enough to say whether that is legitimate, but had just wanted to point it out.



---

archive/issue_comments_002078.json:
```json
{
    "body": "I should mention that I didn't implement reading from DIMACS files. I did implement exporting to DIMACS but perhaps some people would find this interface not that nice. I find it reasonably elegant though because it is quite modular:\n\n\n```\nsage: from sage.sat.converters.polybori import CNFEncoder        \nsage: solver = sage.sat.solvers.dimacs.DIMACS(filename=\"mycnf.cnf\")\nsage: F,s = mq.SR(1,2,2,4,gf2=True,polybori=True).polynomial_system()\nsage: encoder = CNFEncoder(solver, F.ring())\nsage: _ = encoder(F)\nsage: solver.write()\n'mycnf.cnf'\n```\n",
    "created_at": "2012-06-28T15:13:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2078",
    "user": "malb"
}
```

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

archive/issue_comments_002079.json:
```json
{
    "body": "Installation of the spkg fails on my 32-bit ubuntu 12.04.\n\n\n```\ng++ -DHAVE_CONFIG_H -I. -I.. -I/usr/local/sage/local/include -Wall -I. -I./../MTRand -I./../mtl -fopenmp -I/usr/local/sage/local/include -L/usr/local/sage/local/lib -g -fPIC -Wall -pedantic -O2 -MT DimacsParser.lo -MD -MP -MF .deps/DimacsParser.Tpo -c DimacsParser.cpp  -fPIC -DPIC -o .libs/DimacsParser.o\nDimacsParser.cpp: In member function \u2018void CMSat::DimacsParser::parse_DIMACS(T) [with T = _IO_FILE*]\u2019:\nDimacsParser.cpp:482:60:   instantiated from here\nDimacsParser.cpp:461:33: erreur: no matching function for call to \u2018StreamBuffer::StreamBuffer(_IO_FILE*&)\u2019\nDimacsParser.cpp:461:33: note: candidates are:\nStreamBuffer.h:59:5: note: StreamBuffer::StreamBuffer(gzFile)\nStreamBuffer.h:59:5: note:   no known conversion for argument 1 from \u2018_IO_FILE*\u2019 to \u2018gzFile\u2019\nStreamBuffer.h:29:7: note: StreamBuffer::StreamBuffer(const StreamBuffer&)\nStreamBuffer.h:29:7: note:   no known conversion for argument 1 from \u2018_IO_FILE*\u2019 to \u2018const StreamBuffer&\u2019\nmake[2]: *** [DimacsParser.lo] Erreur 1\n```\n",
    "created_at": "2012-06-29T09:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2079",
    "user": "Bouillaguet"
}
```

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

archive/issue_comments_002080.json:
```json
{
    "body": "Ah, it's a known issue and the next release of CryptoMiniSat is supposed to fix this:\n\nhttp://lists.gforge.inria.fr/pipermail/cryptominisat-devel/2012-June/000325.html",
    "created_at": "2012-06-29T10:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2080",
    "user": "malb"
}
```

Ah, it's a known issue and the next release of CryptoMiniSat is supposed to fix this:

http://lists.gforge.inria.fr/pipermail/cryptominisat-devel/2012-June/000325.html



---

archive/issue_comments_002081.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-06-29T10:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2081",
    "user": "malb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_002082.json:
```json
{
    "body": "I have the same issue here. But I can give the sage library part already a positive review.",
    "created_at": "2012-06-29T14:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2082",
    "user": "AlexanderDreyer"
}
```

I have the same issue here. But I can give the sage library part already a positive review.



---

archive/issue_comments_002083.json:
```json
{
    "body": "PS: It seems that Mate has just release cryptominisat 2.9.5: https://gforge.inria.fr/frs/?group_id=1992&release_id=7438",
    "created_at": "2012-06-29T14:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2083",
    "user": "AlexanderDreyer"
}
```

PS: It seems that Mate has just release cryptominisat 2.9.5: https://gforge.inria.fr/frs/?group_id=1992&release_id=7438



---

archive/issue_comments_002084.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-06-29T16:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2084",
    "user": "malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_002085.json:
```json
{
    "body": "I've updated the SPKG to 2.9.5 and I have also added a patch to the Sage interface which deals with GCC 4.7.0 being more strict (I believe) about `return 1;` from void function.",
    "created_at": "2012-06-29T16:09:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2085",
    "user": "malb"
}
```

I've updated the SPKG to 2.9.5 and I have also added a patch to the Sage interface which deals with GCC 4.7.0 being more strict (I believe) about `return 1;` from void function.



---

archive/issue_comments_002086.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-07-01T21:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2086",
    "user": "AlexanderDreyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_002087.json:
```json
{
    "body": "It seems that interfaces had changes, so the spkg doesn't fit with the sage library patches.\nIt seems that your installation picked up the headers from the old install. Maybe its enough to delete `SAGE_INC+\"/cryptominisat/`?\n\nI fixed a few trivial things below, but there's more to be done:\n\n```\n #!diff\ndiff -r ef5eaff5d6cd module_list.py\n--- a/module_list.py    Fri Jun 29 17:04:34 2012 +0100\n+++ b/module_list.py    Sun Jul 01 23:40:53 2012 +0200\n@@ -1891,12 +1891,12 @@\n     ext_modules.extend([\n         Extension(\"sage.sat.solvers.cryptominisat.cryptominisat\",\n                   [\"sage/sat/solvers/cryptominisat/cryptominisat.pyx\"],\n-                  include_dirs = [SAGE_INC, SAGE_INC+\"/cryptominisat/mtl\", SAGE_INC+\"/cryptominisat/Solver\"],\n+                  include_dirs = [SAGE_INC, SAGE_INC+\"/cmsat/\"],\n                   language = \"c++\",\n                   libraries = ['cryptominisat', 'z']),\n         Extension(\"sage.sat.solvers.cryptominisat.solverconf\",\n                   [\"sage/sat/solvers/cryptominisat/solverconf.pyx\", \"sage/sat/solvers/cryptominisat/solverconf_helper.cpp\"],\n-                  include_dirs = [SAGE_INC, SAGE_INC+\"/cryptominisat/mtl\", SAGE_INC+\"/cryptominisat/Solver\"],\n+                  include_dirs = [SAGE_INC, SAGE_INC+\"/cmsat/\"],\n                   language = \"c++\",\n                   libraries = ['cryptominisat', 'z'])\n         ])\ndiff -r ef5eaff5d6cd sage/sat/solvers/cryptominisat/solverconf_helper.h\n--- a/sage/sat/solvers/cryptominisat/solverconf_helper.h        Fri Jun 29 17:04:34 2012 +0100\n+++ b/sage/sat/solvers/cryptominisat/solverconf_helper.h        Sun Jul 01 23:40:53 2012 +0200\n@@ -14,7 +14,7 @@\n  *                  http://www.gnu.org/licenses/\n  ****************************************************************************/\n\n-#include <cryptominisat/Solver/SolverConf.h>\n+#include <SolverConf.h>\n\n enum sc_type {\n   t_int      = 1<<0,\n```\n",
    "created_at": "2012-07-01T21:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2087",
    "user": "AlexanderDreyer"
}
```

It seems that interfaces had changes, so the spkg doesn't fit with the sage library patches.
It seems that your installation picked up the headers from the old install. Maybe its enough to delete `SAGE_INC+"/cryptominisat/`?

I fixed a few trivial things below, but there's more to be done:

```
 #!diff
diff -r ef5eaff5d6cd module_list.py
--- a/module_list.py    Fri Jun 29 17:04:34 2012 +0100
+++ b/module_list.py    Sun Jul 01 23:40:53 2012 +0200
@@ -1891,12 +1891,12 @@
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
@@ -14,7 +14,7 @@
  *                  http://www.gnu.org/licenses/
  ****************************************************************************/

-#include <cryptominisat/Solver/SolverConf.h>
+#include <SolverConf.h>

 enum sc_type {
   t_int      = 1<<0,
```




---

archive/issue_comments_002088.json:
```json
{
    "body": "I've updated the interface to work with 2.9.5. Thanks for spotting this!",
    "created_at": "2012-07-02T14:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2088",
    "user": "malb"
}
```

I've updated the interface to work with 2.9.5. Thanks for spotting this!



---

archive/issue_comments_002089.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-07-02T14:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2089",
    "user": "malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_002090.json:
```json
{
    "body": "ping :)",
    "created_at": "2012-07-11T14:03:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2090",
    "user": "malb"
}
```

ping :)



---

archive/issue_comments_002091.json:
```json
{
    "body": "The spkg installs and I was also able to pull from Sage 5.1(rc0) with automated merge. First tests succeeded, So we are close to a positive review, I'm just waiting for `make ptestlong` to finish.",
    "created_at": "2012-07-11T15:23:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2091",
    "user": "AlexanderDreyer"
}
```

The spkg installs and I was also able to pull from Sage 5.1(rc0) with automated merge. First tests succeeded, So we are close to a positive review, I'm just waiting for `make ptestlong` to finish.



---

archive/issue_comments_002092.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-07-11T21:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2092",
    "user": "AlexanderDreyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_002093.json:
```json
{
    "body": "Ok, tests succeeded, so I can give positive review.",
    "created_at": "2012-07-11T21:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2093",
    "user": "AlexanderDreyer"
}
```

Ok, tests succeeded, so I can give positive review.



---

archive/issue_comments_002094.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-07-13T12:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2094",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_002095.json:
```json
{
    "body": "`_sig_on` and `_sig_off` are deprecated since sage-4.7.  Use `sig_on()` and `sig_off()` instead.  See #10115 (and note the reviewer of that ticket!).",
    "created_at": "2012-07-13T12:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2095",
    "user": "jdemeyer"
}
```

`_sig_on` and `_sig_off` are deprecated since sage-4.7.  Use `sig_on()` and `sig_off()` instead.  See #10115 (and note the reviewer of that ticket!).



---

archive/issue_comments_002096.json:
```json
{
    "body": "Changing component from packages to optional packages.",
    "created_at": "2012-07-13T12:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2096",
    "user": "jdemeyer"
}
```

Changing component from packages to optional packages.



---

archive/issue_comments_002097.json:
```json
{
    "body": "Doh! Fixed: https://bitbucket.org/malb/sage-cryptominisat/changeset/bf994dfe464e",
    "created_at": "2012-07-13T17:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2097",
    "user": "malb"
}
```

Doh! Fixed: https://bitbucket.org/malb/sage-cryptominisat/changeset/bf994dfe464e



---

archive/issue_comments_002098.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-07-13T21:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2098",
    "user": "jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_002099.json:
```json
{
    "body": "i just put the spkg on the server+mirrors.",
    "created_at": "2012-07-16T16:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2099",
    "user": "schilly"
}
```

i just put the spkg on the server+mirrors.



---

archive/issue_comments_002100.json:
```json
{
    "body": "Okay, I'm testing the repo.  **Please don't change it** anymore (unless of course this ticket gets set to needs_work for some reason).",
    "created_at": "2012-07-27T21:03:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2100",
    "user": "jdemeyer"
}
```

Okay, I'm testing the repo.  **Please don't change it** anymore (unless of course this ticket gets set to needs_work for some reason).



---

archive/issue_comments_002101.json:
```json
{
    "body": "There is a problem with `sage/sat/solvers/cryptominisat/solverconf_helper.cpp` not showing up in a Sage source distribution, a fix is to appear at #13315.",
    "created_at": "2012-07-31T17:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2101",
    "user": "jdemeyer"
}
```

There is a problem with `sage/sat/solvers/cryptominisat/solverconf_helper.cpp` not showing up in a Sage source distribution, a fix is to appear at #13315.



---

archive/issue_comments_002102.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-08-12T18:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2102",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_002103.json:
```json
{
    "body": "Does anybody remember why this sentence was added to the documentation?\n\n```\n        - If the solver was interrupted before deciding satisfiability\n          ``None``.\n```\n\nI don't believe that this claim is true.",
    "created_at": "2015-09-30T13:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2103",
    "user": "jdemeyer"
}
```

Does anybody remember why this sentence was added to the documentation?

```
        - If the solver was interrupted before deciding satisfiability
          ``None``.
```

I don't believe that this claim is true.



---

archive/issue_comments_002104.json:
```json
{
    "body": "And even if it were true, I wouldn't like it (interrupts should `raise KeyboardInterrupt`).",
    "created_at": "2015-09-30T13:18:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2104",
    "user": "jdemeyer"
}
```

And even if it were true, I wouldn't like it (interrupts should `raise KeyboardInterrupt`).



---

archive/issue_comments_002105.json:
```json
{
    "body": "You can limit the SAT solver. For example, you can tell it to only do x restarts. In this case, we might not know if the problem is satisfiable, so we return `None`.",
    "created_at": "2015-09-30T13:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2105",
    "user": "malb"
}
```

You can limit the SAT solver. For example, you can tell it to only do x restarts. In this case, we might not know if the problem is satisfiable, so we return `None`.



---

archive/issue_comments_002106.json:
```json
{
    "body": "I see, so the interrupts this talks about do not refer to `KeyboardInterrupt`s (a.k.a. CTRL-C)?",
    "created_at": "2015-09-30T13:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2106",
    "user": "jdemeyer"
}
```

I see, so the interrupts this talks about do not refer to `KeyboardInterrupt`s (a.k.a. CTRL-C)?



---

archive/issue_comments_002107.json:
```json
{
    "body": "IIRC, yep.",
    "created_at": "2015-09-30T13:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/418",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/418#issuecomment-2107",
    "user": "malb"
}
```

IIRC, yep.

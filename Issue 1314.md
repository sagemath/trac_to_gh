# Issue 1314: [graphs] calculate tutte polynomial

archive/issues_001314.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  mvngu lkeough @sdenton4 @nathanncohen stefan azi simonking @nbruin\n\nKeywords: graphs\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1314\n\n",
    "created_at": "2007-11-28T20:02:44Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.1",
    "title": "[graphs] calculate tutte polynomial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1314",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @mwhansen

CC:  mvngu lkeough @sdenton4 @nathanncohen stefan azi simonking @nbruin

Keywords: graphs



Issue created by migration from https://trac.sagemath.org/ticket/1314





---

archive/issue_comments_008252.json:
```json
{
    "body": "Changing component from combinatorics to graph theory.",
    "created_at": "2007-12-17T15:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8252",
    "user": "https://github.com/rlmill"
}
```

Changing component from combinatorics to graph theory.



---

archive/issue_comments_008253.json:
```json
{
    "body": "Changing assignee from @mwhansen to @rlmill.",
    "created_at": "2007-12-17T15:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8253",
    "user": "https://github.com/rlmill"
}
```

Changing assignee from @mwhansen to @rlmill.



---

archive/issue_comments_008254.json:
```json
{
    "body": "Changing keywords from \"graphs\" to \"\".",
    "created_at": "2007-12-17T15:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8254",
    "user": "https://github.com/rlmill"
}
```

Changing keywords from "graphs" to "".



---

archive/issue_comments_008255.json:
```json
{
    "body": "http://homepages.mcs.vuw.ac.nz/~djp/tutte/\n\nThis software could be pretty useful.... But I know nothing about license matters :\n\n\n--------------------------------------------------------------------------------\nThe majority of files are currently under the following simple and quite\nunrestrictive license:\n\n \"(C) Copyright David James Pearce and Gary Haggard, 2007.\n  Permission to copy, use, modify, sell and distribute this software\n  is granted provided this copyright notice appears in all copies.\n  This software is provided \"as is\" without express or implied\n  warranty, and with no claim as to its suitability for any purpose.\n\n  Email: david.pearce`@`mcs.vuw.ac.nz\"\n\nThis license may not be removed from any of the files in question.\n\nThis software makes use of Brendan McKay's excellent \"Nauty\" program\nfor determining (amongst other things) whether two graphs are\nisomorphic or not.  You can find more information about this program\nhere: http://cs.anu.edu.au/~bdm/nauty\n\nAll files from the Nauty program are located in the nauty/\nsubdirectory.  The following license applies to all files in the\nnauty/ directory (see nauty.h for more details):\n\n  \"Copyright (1984-2004) Brendan McKay.  All rights reserved.  Permission\n   is hereby given for use and/or distribution with the exception of\n   sale for profit or application with nontrivial military significance.\n   You must not remove this copyright notice, and you must document any\n   changes that you make to this program.\n   This software is subject to this copyright only, irrespective of\n   any copyright attached to any package of which this is a part.\n\n   This program is only provided \"as is\".  No responsibility will be taken\n   by the author, his employer or his pet rabbit for any misfortune which\n   befalls you because of its use.  I don't think it will delete all your\n   files, burn down your computer room or turn your children against you,\n   but if it does: stiff cheddar.  On the other hand, I very much welcome\n   bug reports, or at least I would if there were any bugs.\n                                                        RIP, 1989\n-----------------------------------------------------------------------------\n\nSo in the end it reads like the license is at least as GPL-uncompatible as Nauty's, and will then have to be included as an external software...",
    "created_at": "2009-05-17T16:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8255",
    "user": "https://github.com/nathanncohen"
}
```

http://homepages.mcs.vuw.ac.nz/~djp/tutte/

This software could be pretty useful.... But I know nothing about license matters :


--------------------------------------------------------------------------------
The majority of files are currently under the following simple and quite
unrestrictive license:

 "(C) Copyright David James Pearce and Gary Haggard, 2007.
  Permission to copy, use, modify, sell and distribute this software
  is granted provided this copyright notice appears in all copies.
  This software is provided "as is" without express or implied
  warranty, and with no claim as to its suitability for any purpose.

  Email: david.pearce`@`mcs.vuw.ac.nz"

This license may not be removed from any of the files in question.

This software makes use of Brendan McKay's excellent "Nauty" program
for determining (amongst other things) whether two graphs are
isomorphic or not.  You can find more information about this program
here: http://cs.anu.edu.au/~bdm/nauty

All files from the Nauty program are located in the nauty/
subdirectory.  The following license applies to all files in the
nauty/ directory (see nauty.h for more details):

  "Copyright (1984-2004) Brendan McKay.  All rights reserved.  Permission
   is hereby given for use and/or distribution with the exception of
   sale for profit or application with nontrivial military significance.
   You must not remove this copyright notice, and you must document any
   changes that you make to this program.
   This software is subject to this copyright only, irrespective of
   any copyright attached to any package of which this is a part.

   This program is only provided "as is".  No responsibility will be taken
   by the author, his employer or his pet rabbit for any misfortune which
   befalls you because of its use.  I don't think it will delete all your
   files, burn down your computer room or turn your children against you,
   but if it does: stiff cheddar.  On the other hand, I very much welcome
   bug reports, or at least I would if there were any bugs.
                                                        RIP, 1989
-----------------------------------------------------------------------------

So in the end it reads like the license is at least as GPL-uncompatible as Nauty's, and will then have to be included as an external software...



---

archive/issue_comments_008256.json:
```json
{
    "body": "Replying to [comment:3 ncohen]:\n> So in the end it reads like the license is at least as GPL-uncompatible as Nauty's, and will then have to be included as an external software...\n\nNot really. Sage includes software which could be used to replace this functionality. We just need to get the *rest* of the software relicensed, if this is possible.",
    "created_at": "2009-05-17T18:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8256",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:3 ncohen]:
> So in the end it reads like the license is at least as GPL-uncompatible as Nauty's, and will then have to be included as an external software...

Not really. Sage includes software which could be used to replace this functionality. We just need to get the *rest* of the software relicensed, if this is possible.



---

archive/issue_comments_008257.json:
```json
{
    "body": "CC myself.",
    "created_at": "2009-10-01T16:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8257",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

CC myself.



---

archive/issue_comments_008258.json:
```json
{
    "body": "Per discussion in Ticket http://trac.sagemath.org/sage_trac/ticket/7052 Pearce and Haggard's code could be included but nauty's license is incompatible. nauty could however be included as a separate optional spkg and the isomorphism function that it is used for replaced with Sage library calls. Then nauty could be used if available or called.\n\nSince Pearce and Haggard's code is extremely efficient at computing the chromatic polynomial as well (between two and three orders of magnitude faster than the current Sage function) it could offer benefit there too.",
    "created_at": "2009-11-06T12:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8258",
    "user": "https://trac.sagemath.org/admin/accounts/users/timmcmillen"
}
```

Per discussion in Ticket http://trac.sagemath.org/sage_trac/ticket/7052 Pearce and Haggard's code could be included but nauty's license is incompatible. nauty could however be included as a separate optional spkg and the isomorphism function that it is used for replaced with Sage library calls. Then nauty could be used if available or called.

Since Pearce and Haggard's code is extremely efficient at computing the chromatic polynomial as well (between two and three orders of magnitude faster than the current Sage function) it could offer benefit there too.



---

archive/issue_comments_008259.json:
```json
{
    "body": "I have written code from scratch to compute the Tutte polynomial of a graph.  I think it is at least correct and maybe even sort of efficient.  Along the way I have written a couple of other routines for the Graph class that might be useful.  I am planning to submit a patch once I figure out how do that (I am brand new at Sage developing....)",
    "created_at": "2012-07-10T21:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8259",
    "user": "https://trac.sagemath.org/admin/accounts/users/jeremy.l.martin"
}
```

I have written code from scratch to compute the Tutte polynomial of a graph.  I think it is at least correct and maybe even sort of efficient.  Along the way I have written a couple of other routines for the Graph class that might be useful.  I am planning to submit a patch once I figure out how do that (I am brand new at Sage developing....)



---

archive/issue_comments_008260.json:
```json
{
    "body": "This ticket requires an edge contraction method; the existing `merge_vertices` method doesn't work properly for the computation of Tutte polynomials. A working method is available at ticket #13239.",
    "created_at": "2012-07-12T16:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8260",
    "user": "https://github.com/dandrake"
}
```

This ticket requires an edge contraction method; the existing `merge_vertices` method doesn't work properly for the computation of Tutte polynomials. A working method is available at ticket #13239.



---

archive/issue_comments_008261.json:
```json
{
    "body": "Tutte polynomial also needs code to determine whether an edge is a cut edge.  You can find this at ticket #13242.",
    "created_at": "2012-07-12T19:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8261",
    "user": "https://trac.sagemath.org/admin/accounts/users/lkeough"
}
```

Tutte polynomial also needs code to determine whether an edge is a cut edge.  You can find this at ticket #13242.



---

archive/issue_comments_008262.json:
```json
{
    "body": "I had some old code from awhile back for computing this which I've attached, along with some commented out possible optimizations.  I think I remember when doing this in practice, avoiding copying the graph saved quite a bit of time (hence the unmerge function).",
    "created_at": "2012-07-13T02:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8262",
    "user": "https://github.com/mwhansen"
}
```

I had some old code from awhile back for computing this which I've attached, along with some commented out possible optimizations.  I think I remember when doing this in practice, avoiding copying the graph saved quite a bit of time (hence the unmerge function).



---

archive/issue_comments_008263.json:
```json
{
    "body": "Replying to [comment:12 mhansen]:\n\n> I had some old code from awhile back for computing this which I've attached, along with some commented out possible optimizations.  I think I remember when doing this in practice, avoiding copying the graph saved quite a bit of time (hence the unmerge function).\n\nmhansen, thanks for sharing this code.  Unfortunately, it does not seem to give the right answer for K_4:\n\nsage: G = graphs.[This is the Trac macro *CompleteGraph* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#CompleteGraph-macro)(4); G.allow_loops(true); G.allow_multiple_edges(true); tp = tutte_polynomial(G,x,y); tp\n\nx<sup>2</sup>*y<sup>2</sup> + x*y<sup>3</sup> + x<sup>3</sup> + x<sup>2</sup>*y + x*y<sup>2</sup> + x<sup>2</sup> + x*y\n\nThe actual Tutte polynomial of K4 is x<sup>3</sup> + 3*x<sup>2</sup> + y<sup>3</sup> + 4*x*y + 3*y<sup>2</sup> + 2*x + 2*y.  \n\nI currently do not see a way to implement the Tutte polynomial without making lots of copies of graphs, but maybe someone else can.",
    "created_at": "2012-07-13T15:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8263",
    "user": "https://trac.sagemath.org/admin/accounts/users/jeremy.l.martin"
}
```

Replying to [comment:12 mhansen]:

> I had some old code from awhile back for computing this which I've attached, along with some commented out possible optimizations.  I think I remember when doing this in practice, avoiding copying the graph saved quite a bit of time (hence the unmerge function).

mhansen, thanks for sharing this code.  Unfortunately, it does not seem to give the right answer for K_4:

sage: G = graphs.[This is the Trac macro *CompleteGraph* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#CompleteGraph-macro)(4); G.allow_loops(true); G.allow_multiple_edges(true); tp = tutte_polynomial(G,x,y); tp

x<sup>2</sup>*y<sup>2</sup> + x*y<sup>3</sup> + x<sup>3</sup> + x<sup>2</sup>*y + x*y<sup>2</sup> + x<sup>2</sup> + x*y

The actual Tutte polynomial of K4 is x<sup>3</sup> + 3*x<sup>2</sup> + y<sup>3</sup> + 4*x*y + 3*y<sup>2</sup> + 2*x + 2*y.  

I currently do not see a way to implement the Tutte polynomial without making lots of copies of graphs, but maybe someone else can.



---

archive/issue_comments_008264.json:
```json
{
    "body": "Sorry -- there was a typo in that one.  I've uploaded a new version which works and implements caching which should save quite a bit of time.",
    "created_at": "2012-07-13T20:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8264",
    "user": "https://github.com/mwhansen"
}
```

Sorry -- there was a typo in that one.  I've uploaded a new version which works and implements caching which should save quite a bit of time.



---

archive/issue_comments_008265.json:
```json
{
    "body": "I timed both Jeremy's code and mhansen's code and it seems that mhansen's is much faster.  \n\nThe two codes give two different looking (but potentially the same) answers on the Petersen graph.\n\nThis is about a third of the tutte.sage output\n14*x^4 + 22*(x + y)^2*x + 8*(x + y)*((x + y)*x + y^2 + x + y)*x + (x^4 +\nx^3 + (x + y)*(x^2 + x + y) + x^2 + x + y)*x^2 + ((x + y)^2*x + (x +\ny)^2 + y^3 + ((x + y)*x^2 + (x + y)*x + y^2 + x + y)*x + y^2 + x +\ny)*x^2 + 22*(x + y)^2 + 13*(y^2 + x + y)^2 + 14*x^3 + 22*y^3 + 14*(x +\ny)*(x^2 + x + y) + 4*(y^2 + x + y)*((x + y)^2 + y^3 + y^2 + x + y) +\n5*((x + y)*x + (x^2 + x + y)*x + y^2 + x + y)*y + 9*((x + y)*x^2 + (x +\ny)*x + y^2 + x + y)*x + 9*(x^4 + x^3 + x^2 + x + y)*x + ((x + y)^2*x +\n(x + y)^2 + y^3 + ((x + y)*x^2 + (x + y)*x + y^2 + x + y)*x + y^2 + x +\ny)*x + (x^4 + (x^4 + x^3 + x^2 + x + y)*x^2 + x^3 + (x + y)*(x^2 + x +\ny) + (x^4 + x^3 + x^2 + x + y)*x + x^2 + x + y)*x + 4*(x^4 + (x + y)^2*x\n+ (x + y)^2 + x^3 + y^3 + (x + y)*(x^2 + x + y) + ((x + y)*x^2 + (x +\ny)*x + y^2 + x + y)*x + (x^4 + x^3 + x^2 + x + y)*x + x^2 + y^2 + 2*x +\n2*y)*x + 2*(x^4 + (x + y)^2*x + (x + y)^2 + x^3 + y^3 + (x + y)*(x^2 + x\n+ y) + ((x + y)*x^2 + (x + y)*x + y^2 + x + y)*x + (x^4 + x^3 + x^2 + x\n+ y)*x + (x^4 + x^3 + (x + y)*(x^2 + x + y) + (x^4 + x^3 + x^2 + x +\ny)*x + x^2 + x + y)*x + x^2 + y^2 + 2*x + 2*y)*x + 2*(x^4 + 2*(x +....\n\nAnd this is the output of Jeremy's:\nx^9 + 6*x^8 + 21*x^7 + 56*x^6 + 12*x^5*y + 114*x^5 + y^6 + 70*x^4*y +\n30*x<sup>3*y</sup>2 + 15*x<sup>2*y</sup>3 + 10*x*y^4 + 170*x^4 + 180*x^3 + 120*x^2 + 9*y^5\n+ 170*x^3*y + 105*x<sup>2*y</sup>2 + 65*x*y^3 + 35*y^4 + 240*x^2*y + 171*x*y^2 +\n75*y^3 + 168*x*y + 84*y^2 + 36*x + 36*y\n\nAlthough they are both showing up funny looking here...\n\nIs there an easy way to multiply out and gather like terms in sage?",
    "created_at": "2012-07-15T20:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8265",
    "user": "https://trac.sagemath.org/admin/accounts/users/lkeough"
}
```

I timed both Jeremy's code and mhansen's code and it seems that mhansen's is much faster.  

The two codes give two different looking (but potentially the same) answers on the Petersen graph.

This is about a third of the tutte.sage output
14*x^4 + 22*(x + y)^2*x + 8*(x + y)*((x + y)*x + y^2 + x + y)*x + (x^4 +
x^3 + (x + y)*(x^2 + x + y) + x^2 + x + y)*x^2 + ((x + y)^2*x + (x +
y)^2 + y^3 + ((x + y)*x^2 + (x + y)*x + y^2 + x + y)*x + y^2 + x +
y)*x^2 + 22*(x + y)^2 + 13*(y^2 + x + y)^2 + 14*x^3 + 22*y^3 + 14*(x +
y)*(x^2 + x + y) + 4*(y^2 + x + y)*((x + y)^2 + y^3 + y^2 + x + y) +
5*((x + y)*x + (x^2 + x + y)*x + y^2 + x + y)*y + 9*((x + y)*x^2 + (x +
y)*x + y^2 + x + y)*x + 9*(x^4 + x^3 + x^2 + x + y)*x + ((x + y)^2*x +
(x + y)^2 + y^3 + ((x + y)*x^2 + (x + y)*x + y^2 + x + y)*x + y^2 + x +
y)*x + (x^4 + (x^4 + x^3 + x^2 + x + y)*x^2 + x^3 + (x + y)*(x^2 + x +
y) + (x^4 + x^3 + x^2 + x + y)*x + x^2 + x + y)*x + 4*(x^4 + (x + y)^2*x
+ (x + y)^2 + x^3 + y^3 + (x + y)*(x^2 + x + y) + ((x + y)*x^2 + (x +
y)*x + y^2 + x + y)*x + (x^4 + x^3 + x^2 + x + y)*x + x^2 + y^2 + 2*x +
2*y)*x + 2*(x^4 + (x + y)^2*x + (x + y)^2 + x^3 + y^3 + (x + y)*(x^2 + x
+ y) + ((x + y)*x^2 + (x + y)*x + y^2 + x + y)*x + (x^4 + x^3 + x^2 + x
+ y)*x + (x^4 + x^3 + (x + y)*(x^2 + x + y) + (x^4 + x^3 + x^2 + x +
y)*x + x^2 + x + y)*x + x^2 + y^2 + 2*x + 2*y)*x + 2*(x^4 + 2*(x +....

And this is the output of Jeremy's:
x^9 + 6*x^8 + 21*x^7 + 56*x^6 + 12*x^5*y + 114*x^5 + y^6 + 70*x^4*y +
30*x<sup>3*y</sup>2 + 15*x<sup>2*y</sup>3 + 10*x*y^4 + 170*x^4 + 180*x^3 + 120*x^2 + 9*y^5
+ 170*x^3*y + 105*x<sup>2*y</sup>2 + 65*x*y^3 + 35*y^4 + 240*x^2*y + 171*x*y^2 +
75*y^3 + 168*x*y + 84*y^2 + 36*x + 36*y

Although they are both showing up funny looking here...

Is there an easy way to multiply out and gather like terms in sage?



---

archive/issue_comments_008266.json:
```json
{
    "body": "Attachment [Tuttepolynomial.sage](tarball://root/attachments/some-uuid/ticket1314/Tuttepolynomial.sage) by lkeough created at 2012-07-15 21:00:01\n\nYou also need the patches from #13242",
    "created_at": "2012-07-15T21:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8266",
    "user": "https://trac.sagemath.org/admin/accounts/users/lkeough"
}
```

Attachment [Tuttepolynomial.sage](tarball://root/attachments/some-uuid/ticket1314/Tuttepolynomial.sage) by lkeough created at 2012-07-15 21:00:01

You also need the patches from #13242



---

archive/issue_comments_008267.json:
```json
{
    "body": "I attached Jeremy's code as Tuttepolynomial.sage in case anyone else wants to timeit.",
    "created_at": "2012-07-15T21:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8267",
    "user": "https://trac.sagemath.org/admin/accounts/users/lkeough"
}
```

I attached Jeremy's code as Tuttepolynomial.sage in case anyone else wants to timeit.



---

archive/issue_comments_008268.json:
```json
{
    "body": "`x` and `y` should ideally be integer polynomials (i.e., `R.<x,y> = ZZ[]`) -- then you don't have to deal with manually \"expanding\".\n\nAdditionally, in the `tuttepolynomial.sage` code, you should probably be caching a canonical label of the graph -- see the `cache_key` method in my patch.",
    "created_at": "2012-07-15T21:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8268",
    "user": "https://github.com/mwhansen"
}
```

`x` and `y` should ideally be integer polynomials (i.e., `R.<x,y> = ZZ[]`) -- then you don't have to deal with manually "expanding".

Additionally, in the `tuttepolynomial.sage` code, you should probably be caching a canonical label of the graph -- see the `cache_key` method in my patch.



---

archive/issue_comments_008269.json:
```json
{
    "body": "Replying to [comment:17 mhansen]:\n> `x` and `y` should ideally be integer polynomials (i.e., `R.<x,y> = ZZ[]`) -- then you don't have to deal with manually \"expanding\".\n> \n\nI see now!  This makes it much better.  If we put R.<x,y> = ZZ[] as the first line in the Tutte polynomial code it does this for us.  Doing that shouldn't mess anything up, right?\n\n> Additionally, in the `tuttepolynomial.sage` code, you should probably be caching a canonical label of the graph -- see the `cache_key` method in my patch.\n\nWill do!",
    "created_at": "2012-07-15T21:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8269",
    "user": "https://trac.sagemath.org/admin/accounts/users/lkeough"
}
```

Replying to [comment:17 mhansen]:
> `x` and `y` should ideally be integer polynomials (i.e., `R.<x,y> = ZZ[]`) -- then you don't have to deal with manually "expanding".
> 

I see now!  This makes it much better.  If we put R.<x,y> = ZZ[] as the first line in the Tutte polynomial code it does this for us.  Doing that shouldn't mess anything up, right?

> Additionally, in the `tuttepolynomial.sage` code, you should probably be caching a canonical label of the graph -- see the `cache_key` method in my patch.

Will do!



---

archive/issue_comments_008270.json:
```json
{
    "body": "I was curious and went ahead an implemented the optimizations at http://homepages.ecs.vuw.ac.nz/~djp/files/TOMS10.pdf .  It seems our primary bottleneck is computing the canonical label of the graphs.",
    "created_at": "2012-07-16T23:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8270",
    "user": "https://github.com/mwhansen"
}
```

I was curious and went ahead an implemented the optimizations at http://homepages.ecs.vuw.ac.nz/~djp/files/TOMS10.pdf .  It seems our primary bottleneck is computing the canonical label of the graphs.



---

archive/issue_comments_008271.json:
```json
{
    "body": "Attachment [tutte.sage](tarball://root/attachments/some-uuid/ticket1314/tutte.sage) by Stefan created at 2012-07-18 04:24:01",
    "created_at": "2012-07-18T04:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8271",
    "user": "https://trac.sagemath.org/admin/accounts/users/Stefan"
}
```

Attachment [tutte.sage](tarball://root/attachments/some-uuid/ticket1314/tutte.sage) by Stefan created at 2012-07-18 04:24:01



---

archive/issue_comments_008272.json:
```json
{
    "body": "What is the current status of this code?",
    "created_at": "2013-05-05T14:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8272",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

What is the current status of this code?



---

archive/issue_comments_008273.json:
```json
{
    "body": "tutte.sage works -- it just needs to be added as a patch, documented, etc.  I haven't had time to do this myself.",
    "created_at": "2013-05-05T14:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8273",
    "user": "https://github.com/mwhansen"
}
```

tutte.sage works -- it just needs to be added as a patch, documented, etc.  I haven't had time to do this myself.



---

archive/issue_comments_008274.json:
```json
{
    "body": "Nice, perhaps I'll do that one time if you wish.\n\nBtw, there is a minor bug in tutte.sage. In the corner case \n\n\n```\n257     if G.num_edges() == 0:\n258         return 1\n```\n\n\nwe should actually still return a polynomial since otherwise:\n\n\n```\ntutte_polynomial(graphs.CompleteGraph(10).complement())(0,3)\n```\n\n\nwould break.",
    "created_at": "2013-05-05T14:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8274",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

Nice, perhaps I'll do that one time if you wish.

Btw, there is a minor bug in tutte.sage. In the corner case 


```
257     if G.num_edges() == 0:
258         return 1
```


we should actually still return a polynomial since otherwise:


```
tutte_polynomial(graphs.CompleteGraph(10).complement())(0,3)
```


would break.



---

archive/issue_comments_008275.json:
```json
{
    "body": "Replying to [comment:24 azi]:\n> Btw, there is a minor bug in tutte.sage. In the corner case \n> \n> {{{\n> 257     if G.num_edges() == 0:\n> 258         return 1\n> }}}\n\nYep.  One of the things that helps a lot is being able to avoid copying the graph.  For the Tutte polynomial code, we just make one copy of the graph on the initial call, but never copy it afterward.  I found context managers useful to manage mutating the graph and restoring it.\n\nAlso, I think the edge selection strategy has a bit of an effect on the speed of the chromatic polynomial computation as well.",
    "created_at": "2013-05-05T15:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8275",
    "user": "https://github.com/mwhansen"
}
```

Replying to [comment:24 azi]:
> Btw, there is a minor bug in tutte.sage. In the corner case 
> 
> {{{
> 257     if G.num_edges() == 0:
> 258         return 1
> }}}

Yep.  One of the things that helps a lot is being able to avoid copying the graph.  For the Tutte polynomial code, we just make one copy of the graph on the initial call, but never copy it afterward.  I found context managers useful to manage mutating the graph and restoring it.

Also, I think the edge selection strategy has a bit of an effect on the speed of the chromatic polynomial computation as well.



---

archive/issue_comments_008276.json:
```json
{
    "body": "I am in the process of integrating this code into Sage. There appears to be a memory issue when calculating the Tutte polynomial of a number of small graphs sequentially. Namely, Sage gets killed by the OS after exhausting all the physical memory.\n\nDo you happen to have an idea where the fault for this could be?",
    "created_at": "2013-05-11T07:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8276",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

I am in the process of integrating this code into Sage. There appears to be a memory issue when calculating the Tutte polynomial of a number of small graphs sequentially. Namely, Sage gets killed by the OS after exhausting all the physical memory.

Do you happen to have an idea where the fault for this could be?



---

archive/issue_comments_008277.json:
```json
{
    "body": "Can you give some code to reproduce this?  I've been running code like\n\n\n```python\nfor g in graphs.nauty_geng(\"7\"):\n    print tutte_polynomial(g, x, y)\n```\n\n\nbut haven't been able to reproduce this.",
    "created_at": "2013-05-11T08:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8277",
    "user": "https://github.com/mwhansen"
}
```

Can you give some code to reproduce this?  I've been running code like


```python
for g in graphs.nauty_geng("7"):
    print tutte_polynomial(g, x, y)
```


but haven't been able to reproduce this.



---

archive/issue_comments_008278.json:
```json
{
    "body": "Sure here is an example.\n\n\n```\nload tutte.sage\nc = 0 \nfor G in graphs.nauty_geng(\"13 39:39\"):\n    \n    if sorted(G.degree_sequence()) != sorted(G.complement().degree_sequence()):\n        c+=1\n        if tutte_polynomial(G,x,y) == tutte_polynomial(G.complement(),x,y):\n            print G.graph6_string()\n            from time import sleep\n            sleep(24*60*60)\n        if c % 1000 == 0:\n            print c\n```\n\n\nThe motivation of this code stems from an open problem that I am now working on.",
    "created_at": "2013-05-11T08:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8278",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

Sure here is an example.


```
load tutte.sage
c = 0 
for G in graphs.nauty_geng("13 39:39"):
    
    if sorted(G.degree_sequence()) != sorted(G.complement().degree_sequence()):
        c+=1
        if tutte_polynomial(G,x,y) == tutte_polynomial(G.complement(),x,y):
            print G.graph6_string()
            from time import sleep
            sleep(24*60*60)
        if c % 1000 == 0:
            print c
```


The motivation of this code stems from an open problem that I am now working on.



---

archive/issue_comments_008279.json:
```json
{
    "body": "My guess is just that the cache in that version isn't reset after each run.  If you add `tutte_polynomial.cache.clear()` before the `if tutte_polynomial(G,x,y) == tutte_polynomial(G.complement(),x,y):` line, you won't have that problem.",
    "created_at": "2013-05-11T18:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8279",
    "user": "https://github.com/mwhansen"
}
```

My guess is just that the cache in that version isn't reset after each run.  If you add `tutte_polynomial.cache.clear()` before the `if tutte_polynomial(G,x,y) == tutte_polynomial(G.complement(),x,y):` line, you won't have that problem.



---

archive/issue_comments_008280.json:
```json
{
    "body": "Good! I'll play with that and see what happens.\n\nBTW, could you add yourself to the main TRAC page at the bottom so that I know what to write in the code under as the author ?",
    "created_at": "2013-05-11T18:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8280",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

Good! I'll play with that and see what happens.

BTW, could you add yourself to the main TRAC page at the bottom so that I know what to write in the code under as the author ?



---

archive/issue_comments_008281.json:
```json
{
    "body": "Attachment [trac_1314_tuttePoly.patch](tarball://root/attachments/some-uuid/ticket1314/trac_1314_tuttePoly.patch) by azi created at 2013-06-22 10:16:12\n\nOkay !\n\nAttached is the nhansen's code factored into Sage. Before having any changes of being positively reviewed I we need to figure out how can we allow the users to use the edge selectors in the code and document that.\n\nLet me know if you have any other comments and of course don't be shy to modify this yourself as well.",
    "created_at": "2013-06-22T10:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8281",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

Attachment [trac_1314_tuttePoly.patch](tarball://root/attachments/some-uuid/ticket1314/trac_1314_tuttePoly.patch) by azi created at 2013-06-22 10:16:12

Okay !

Attached is the nhansen's code factored into Sage. Before having any changes of being positively reviewed I we need to figure out how can we allow the users to use the edge selectors in the code and document that.

Let me know if you have any other comments and of course don't be shy to modify this yourself as well.



---

archive/issue_comments_008282.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-06-22T10:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8282",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_008283.json:
```json
{
    "body": "Just a quick remark! The code computing the Tutte polynomial is correct (I reviewed that) so I only need someone to check if this patch is integrated correctly into Sage.",
    "created_at": "2013-06-27T20:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8283",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

Just a quick remark! The code computing the Tutte polynomial is correct (I reviewed that) so I only need someone to check if this patch is integrated correctly into Sage.



---

archive/issue_comments_008284.json:
```json
{
    "body": "Hellooooooooo !!\n\nIf you just want comments on the integration into Sage, it would be nice if you could add it to the reference manual, perhaps rename the file to `tutte_polynomial.py`, and add documentation to the new functions until `sage -coverage yourfile.py` says that everything is filled. In particular it would be nice if you could be more verbose about what `VertexOrder` and `MinimizeDegree` actually do `:-)`\n\nOh, and people around do not like the `raise ValueError, \"something\"`. They say it's not pep8 or not Python3-ready, and prefer `ValueError(\"something\")`.\n\nThis contextmanager decorator really is a funny thing `:-)`\n\nNathann",
    "created_at": "2013-06-28T22:00:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8284",
    "user": "https://github.com/nathanncohen"
}
```

Hellooooooooo !!

If you just want comments on the integration into Sage, it would be nice if you could add it to the reference manual, perhaps rename the file to `tutte_polynomial.py`, and add documentation to the new functions until `sage -coverage yourfile.py` says that everything is filled. In particular it would be nice if you could be more verbose about what `VertexOrder` and `MinimizeDegree` actually do `:-)`

Oh, and people around do not like the `raise ValueError, "something"`. They say it's not pep8 or not Python3-ready, and prefer `ValueError("something")`.

This contextmanager decorator really is a funny thing `:-)`

Nathann



---

archive/issue_comments_008285.json:
```json
{
    "body": "By the way, could you define what an \"ear\" is somewhere ? You say that it is a \"sequence of vertices\" which is a tad vague, and your code seems to imply somewhere that a vertex of degree 2 adjacent to two vertices of degree 3 is not an ear, while I thought that it was.\n\nWell, .. `:-)`\n\nNathann",
    "created_at": "2013-06-28T22:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8285",
    "user": "https://github.com/nathanncohen"
}
```

By the way, could you define what an "ear" is somewhere ? You say that it is a "sequence of vertices" which is a tad vague, and your code seems to imply somewhere that a vertex of degree 2 adjacent to two vertices of degree 3 is not an ear, while I thought that it was.

Well, .. `:-)`

Nathann



---

archive/issue_comments_008286.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-06-29T08:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8286",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_008287.json:
```json
{
    "body": "here is small clean-up patch. There remains to write doc for all functions.\n\nfor the bot:\n\napply trac_1314_tuttePoly.patch trac_1314_addon_fc.patch",
    "created_at": "2013-07-17T12:24:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8287",
    "user": "https://github.com/fchapoton"
}
```

here is small clean-up patch. There remains to write doc for all functions.

for the bot:

apply trac_1314_tuttePoly.patch trac_1314_addon_fc.patch



---

archive/issue_comments_008288.json:
```json
{
    "body": "Here is a new patch, that includes\n\n* renaming of the file tutte_poly.py into tutte_polynomial.py\n\n* inclusion into the reference manual\n\nThere still remains work to be done to have 100% doctesting and clean documentation",
    "created_at": "2013-07-22T09:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8288",
    "user": "https://github.com/fchapoton"
}
```

Here is a new patch, that includes

* renaming of the file tutte_poly.py into tutte_polynomial.py

* inclusion into the reference manual

There still remains work to be done to have 100% doctesting and clean documentation



---

archive/issue_comments_008289.json:
```json
{
    "body": "Hello!\n\nWhat exactly is still required to be done? Also, is there a reason for renaming it to tutte_polynomial? I am wondering whether we should name it tuttepoly to be consistent with chrompoly?",
    "created_at": "2013-07-29T12:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8289",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

Hello!

What exactly is still required to be done? Also, is there a reason for renaming it to tutte_polynomial? I am wondering whether we should name it tuttepoly to be consistent with chrompoly?



---

archive/issue_comments_008290.json:
```json
{
    "body": "There is nothing like chrompoly, the function is called \n\n```\nG.chromatic_polynomial\n```\n\n\nWhat remains to be done: add explanations, and document every function. See the previous comments (see comments 34 and 35 in particular)",
    "created_at": "2013-07-29T12:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8290",
    "user": "https://github.com/fchapoton"
}
```

There is nothing like chrompoly, the function is called 

```
G.chromatic_polynomial
```


What remains to be done: add explanations, and document every function. See the previous comments (see comments 34 and 35 in particular)



---

archive/issue_comments_008291.json:
```json
{
    "body": "Yes! But the file is called chrompoly.py. And so is the file for the matching polynomial called matchpoly.\n\nOK I'll  look into Nathann's comments!",
    "created_at": "2013-07-29T12:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8291",
    "user": "https://trac.sagemath.org/admin/accounts/users/azi"
}
```

Yes! But the file is called chrompoly.py. And so is the file for the matching polynomial called matchpoly.

OK I'll  look into Nathann's comments!



---

archive/issue_comments_008292.json:
```json
{
    "body": "I have started adding the doc, but there remains several functions with no doc.\n\nIn particular, it is necessary to explain more precisely **what is an ear**.",
    "created_at": "2013-08-31T19:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8292",
    "user": "https://github.com/fchapoton"
}
```

I have started adding the doc, but there remains several functions with no doc.

In particular, it is necessary to explain more precisely **what is an ear**.



---

archive/issue_comments_008293.json:
```json
{
    "body": "more doc, doctest coverage is now 65%",
    "created_at": "2013-09-01T08:13:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8293",
    "user": "https://github.com/fchapoton"
}
```

more doc, doctest coverage is now 65%



---

archive/issue_comments_008294.json:
```json
{
    "body": "more doc, doctest coverage is now **95%**\n\nThere remains only one function to doctest, but this is a decorator and I do not know what to do ! Could anybody please help ?",
    "created_at": "2013-10-01T20:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8294",
    "user": "https://github.com/fchapoton"
}
```

more doc, doctest coverage is now **95%**

There remains only one function to doctest, but this is a decorator and I do not know what to do ! Could anybody please help ?



---

archive/issue_comments_008295.json:
```json
{
    "body": "You could just call a function which is decorated with it, and add a `#indirect doctest` flag to the corresponding doctest line.\n\nNathann",
    "created_at": "2013-10-02T08:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8295",
    "user": "https://github.com/nathanncohen"
}
```

You could just call a function which is decorated with it, and add a `#indirect doctest` flag to the corresponding doctest line.

Nathann



---

archive/issue_comments_008296.json:
```json
{
    "body": "**100 %** doctested and almost ready for review !\n\n*But* the doc of `tutte_polynomial` does not appear, because it is cached (in a custom way, not by the usual `cached_function`) !",
    "created_at": "2013-10-02T18:30:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8296",
    "user": "https://github.com/fchapoton"
}
```

**100 %** doctested and almost ready for review !

*But* the doc of `tutte_polynomial` does not appear, because it is cached (in a custom way, not by the usual `cached_function`) !



---

archive/issue_comments_008297.json:
```json
{
    "body": "Yep, I think this was before cached_function existed.  Anyway, you can add \"`@`sage_wraps(func)\" before \"def wrapper\" to make things nicer on that front.  I also feel that at the end of the tutte_polynomial function, we should add something like \n\n\n```\nif initial_call is True:\n    tutte_polynomial.cache.clear()\n```\n\n\nso that the cache is valid for only the computation of one \"tree\".  This does play bad with threads (which aren't used much).  It might be better to just manually pass the cache along as a default argument throughout the call tree.  I think that's probably best.",
    "created_at": "2013-10-03T08:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8297",
    "user": "https://github.com/mwhansen"
}
```

Yep, I think this was before cached_function existed.  Anyway, you can add "`@`sage_wraps(func)" before "def wrapper" to make things nicer on that front.  I also feel that at the end of the tutte_polynomial function, we should add something like 


```
if initial_call is True:
    tutte_polynomial.cache.clear()
```


so that the cache is valid for only the computation of one "tree".  This does play bad with threads (which aren't used much).  It might be better to just manually pass the cache along as a default argument throughout the call tree.  I think that's probably best.



---

archive/issue_comments_008298.json:
```json
{
    "body": "Attachment [trac_1314_addon_fc.patch](tarball://root/attachments/some-uuid/ticket1314/trac_1314_addon_fc.patch) by @fchapoton created at 2013-10-03 17:02:14\n\nThe docs seems to be ok now, thanks Mike !\n\nI have not taken care of the cache cleaning, as I do not know where to put the lines you suggested.\n\nStill I think it deserves to be \"need review\"",
    "created_at": "2013-10-03T17:02:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8298",
    "user": "https://github.com/fchapoton"
}
```

Attachment [trac_1314_addon_fc.patch](tarball://root/attachments/some-uuid/ticket1314/trac_1314_addon_fc.patch) by @fchapoton created at 2013-10-03 17:02:14

The docs seems to be ok now, thanks Mike !

I have not taken care of the cache cleaning, as I do not know where to put the lines you suggested.

Still I think it deserves to be "need review"



---

archive/issue_comments_008299.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-10-03T17:02:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8299",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_008300.json:
```json
{
    "body": "Changing keywords from \"\" to \"tutte, graph\".",
    "created_at": "2013-10-15T19:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8300",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "tutte, graph".



---

archive/issue_events_003438.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2013-10-15T19:05:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "milestone": "sage-5.13",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1314#event-3438"
}
```



---

archive/issue_comments_008301.json:
```json
{
    "body": "> I have not taken care of the cache cleaning, as I do not know where to put the lines you suggested.\n\nAt the end of the block `if initial_call is True`, you can add the following :\n\n\n```\nans = tutte_polynomial(G, initial_call=False, edge_selector=edge_selector)\ntutte_polynomial.cache.clear()\nreturn ans\n```\n\n\nNathann",
    "created_at": "2013-10-16T15:17:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8301",
    "user": "https://github.com/nathanncohen"
}
```

> I have not taken care of the cache cleaning, as I do not know where to put the lines you suggested.

At the end of the block `if initial_call is True`, you can add the following :


```
ans = tutte_polynomial(G, initial_call=False, edge_selector=edge_selector)
tutte_polynomial.cache.clear()
return ans
```


Nathann



---

archive/issue_comments_008302.json:
```json
{
    "body": "I think it's better to just have a cache=None default keyword.  On the initial call, this can be detected and a new cache can be created or the user could pass in their own to use across multiple runs.",
    "created_at": "2013-10-16T15:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8302",
    "user": "https://github.com/mwhansen"
}
```

I think it's better to just have a cache=None default keyword.  On the initial call, this can be detected and a new cache can be created or the user could pass in their own to use across multiple runs.



---

archive/issue_comments_008303.json:
```json
{
    "body": "Mike, could you please add a review patch implementing what you suggest ? I do not feel able to guess and try to do it myself.",
    "created_at": "2013-10-18T19:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8303",
    "user": "https://github.com/fchapoton"
}
```

Mike, could you please add a review patch implementing what you suggest ? I do not feel able to guess and try to do it myself.



---

archive/issue_comments_008304.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-01-04T20:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8304",
    "user": "https://github.com/fchapoton"
}
```

New commits:



---

archive/issue_comments_008305.json:
```json
{
    "body": "Ping ?",
    "created_at": "2014-01-07T09:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8305",
    "user": "https://github.com/nathanncohen"
}
```

Ping ?



---

archive/issue_comments_008306.json:
```json
{
    "body": "This is now available via matroids.",
    "created_at": "2014-01-07T11:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8306",
    "user": "https://github.com/fchapoton"
}
```

This is now available via matroids.



---

archive/issue_comments_008307.json:
```json
{
    "body": "What does that mean ? `O_o`",
    "created_at": "2014-01-07T11:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8307",
    "user": "https://github.com/nathanncohen"
}
```

What does that mean ? `O_o`



---

archive/issue_comments_008308.json:
```json
{
    "body": "This mean that somebody else has done the job for matroids.\n\n```\nsage: Matroid(graphs.PetersenGraph()).tutte_polynomial()\nx^9 + 6*x^8 + 21*x^7 + 56*x^6 + 12*x^5*y + y^6 + 114*x^5 + 70*x^4*y + 30*x^3*y^2 + 15*x^2*y^3 + 10*x*y^4 + 9*y^5 + 170*x^4 + 170*x^3*y + 105*x^2*y^2 + 65*x*y^3 + 35*y^4 + 180*x^3 + 240*x^2*y + 171*x*y^2 + 75*y^3 + 120*x^2 + 168*x*y + 84*y^2 + 36*x + 36*y\n```\n",
    "created_at": "2014-01-07T11:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8308",
    "user": "https://github.com/fchapoton"
}
```

This mean that somebody else has done the job for matroids.

```
sage: Matroid(graphs.PetersenGraph()).tutte_polynomial()
x^9 + 6*x^8 + 21*x^7 + 56*x^6 + 12*x^5*y + y^6 + 114*x^5 + 70*x^4*y + 30*x^3*y^2 + 15*x^2*y^3 + 10*x*y^4 + 9*y^5 + 170*x^4 + 170*x^3*y + 105*x^2*y^2 + 65*x*y^3 + 35*y^4 + 180*x^3 + 240*x^2*y + 171*x*y^2 + 75*y^3 + 120*x^2 + 168*x*y + 84*y^2 + 36*x + 36*y
```




---

archive/issue_comments_008309.json:
```json
{
    "body": "Oh. Right. They enumerate all spanning trees, though. They would probably be glad to have another implementation `:-P``\n\nNathann",
    "created_at": "2014-01-07T11:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8309",
    "user": "https://github.com/nathanncohen"
}
```

Oh. Right. They enumerate all spanning trees, though. They would probably be glad to have another implementation `:-P``

Nathann



---

archive/issue_comments_008310.json:
```json
{
    "body": "Anyway Frederic, is this patch in `needs_review` or in `needs_work` (cf the caching thing above), and what is left to be reviewed ? Jernej said some time ago that the mathematical part of the algorithm was correct, but as it seems he wrote the code himself that does not count `:-P`\n\nNathann",
    "created_at": "2014-01-07T12:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8310",
    "user": "https://github.com/nathanncohen"
}
```

Anyway Frederic, is this patch in `needs_review` or in `needs_work` (cf the caching thing above), and what is left to be reviewed ? Jernej said some time ago that the mathematical part of the algorithm was correct, but as it seems he wrote the code himself that does not count `:-P`

Nathann



---

archive/issue_comments_008311.json:
```json
{
    "body": "The  Matroid implementation is hopelessly slow, and an optimized implementation as in this ticket would be most welcome for matroids too. Until that day, there is definitely a use for the implementation on this ticket!",
    "created_at": "2014-01-07T12:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8311",
    "user": "https://trac.sagemath.org/admin/accounts/users/Stefan"
}
```

The  Matroid implementation is hopelessly slow, and an optimized implementation as in this ticket would be most welcome for matroids too. Until that day, there is definitely a use for the implementation on this ticket!



---

archive/issue_comments_008312.json:
```json
{
    "body": "Stefan : how should this method be exposed in the matroid code ? It only works for graph, and I guess matroids need something more general ?\n\nNathann",
    "created_at": "2014-01-07T13:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8312",
    "user": "https://github.com/nathanncohen"
}
```

Stefan : how should this method be exposed in the matroid code ? It only works for graph, and I guess matroids need something more general ?

Nathann



---

archive/issue_comments_008313.json:
```json
{
    "body": "Yeah. The main idea (caching small graphs) generalizes to matroids, but the code needs to be changed properly, and probably tweaked a lot to get good speeds.",
    "created_at": "2014-01-07T13:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8313",
    "user": "https://trac.sagemath.org/admin/accounts/users/Stefan"
}
```

Yeah. The main idea (caching small graphs) generalizes to matroids, but the code needs to be changed properly, and probably tweaked a lot to get good speeds.



---

archive/issue_comments_008314.json:
```json
{
    "body": "Okay. Does it mean that the function that this patch implements is of no direct use for Matroids, and that there is no need to expose it anywhere right now ?\n\nNathann",
    "created_at": "2014-01-07T13:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8314",
    "user": "https://github.com/nathanncohen"
}
```

Okay. Does it mean that the function that this patch implements is of no direct use for Matroids, and that there is no need to expose it anywhere right now ?

Nathann



---

archive/issue_comments_008315.json:
```json
{
    "body": "Okayyyyyyy... Let's sum it up : Mike Hansen wrote the initial code, Jernej checked the math and cleaned bits of it, and Fr\u00e9d\u00e9ric cleaned it again and add some documentation.\n\nCool. I just changed the branch as I have a couple of commits to add \n\n* Rebase on 6.1.beta4\n* An option to clean the cache, as mentionned earlier\n\nI agree with the non-mathematical part of what was above. Soooooo we just need somebody to review my two commits and we are done.\n\nHave fuuuuuuuuun !\n\nNathann",
    "created_at": "2014-01-07T16:01:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8315",
    "user": "https://github.com/nathanncohen"
}
```

Okayyyyyyy... Let's sum it up : Mike Hansen wrote the initial code, Jernej checked the math and cleaned bits of it, and Frédéric cleaned it again and add some documentation.

Cool. I just changed the branch as I have a couple of commits to add 

* Rebase on 6.1.beta4
* An option to clean the cache, as mentionned earlier

I agree with the non-mathematical part of what was above. Soooooo we just need somebody to review my two commits and we are done.

Have fuuuuuuuuun !

Nathann



---

archive/issue_comments_008316.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-01-07T16:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8316",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_008317.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-01-07T17:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8317",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_008318.json:
```json
{
    "body": "I've removed the `initial_call` argument since it was prone to be abused (especially since it was the first one), and doing it this way should give some (marginal) speedup. I'm going to run some timings now. I'm also going to now try it by converting to use `cached_function`.\n\nEdit - I just realized I forgot to move the ``@`_cache` to the internal function...",
    "created_at": "2014-01-07T17:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8318",
    "user": "https://github.com/tscrim"
}
```

I've removed the `initial_call` argument since it was prone to be abused (especially since it was the first one), and doing it this way should give some (marginal) speedup. I'm going to run some timings now. I'm also going to now try it by converting to use `cached_function`.

Edit - I just realized I forgot to move the ``@`_cache` to the internal function...



---

archive/issue_comments_008319.json:
```json
{
    "body": "Okay, ``@`cached_function` doesn't work because we can't pass a key function to it... (aside: I think such a feature would be quite useful) Back to the custom ``@`_cache`.\n\nWith my changes (including some other optimizations):\n\n```\nsage: P = graphs.PetersenGraph()\nsage: %timeit P.tutte_polynomial()\n1 loops, best of 3: 256 ms per loop\n```\n\nBefore:\n\n```\nsage: P = graphs.PetersenGraph()\nsage: %timeit P.tutte_polynomial()\n1000 loops, best of 3: 1.08 ms per loop\n```\n\n\nNow I'm currently perplexed...currently the best involves extra if statements, creation of parents, and unused arguments being passed. So we might just want to merge `6ef434e` instead. Still testing stuff...",
    "created_at": "2014-01-07T17:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8319",
    "user": "https://github.com/tscrim"
}
```

Okay, ``@`cached_function` doesn't work because we can't pass a key function to it... (aside: I think such a feature would be quite useful) Back to the custom ``@`_cache`.

With my changes (including some other optimizations):

```
sage: P = graphs.PetersenGraph()
sage: %timeit P.tutte_polynomial()
1 loops, best of 3: 256 ms per loop
```

Before:

```
sage: P = graphs.PetersenGraph()
sage: %timeit P.tutte_polynomial()
1000 loops, best of 3: 1.08 ms per loop
```


Now I'm currently perplexed...currently the best involves extra if statements, creation of parents, and unused arguments being passed. So we might just want to merge `6ef434e` instead. Still testing stuff...



---

archive/issue_comments_008320.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2014-01-07T18:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8320",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_008321.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-01-07T18:23:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8321",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_008322.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-01-07T18:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8322",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_008323.json:
```json
{
    "body": "I put my changes in the branch `u/tscrim/tutte_polynomial-1314` and reverted back the public branch. It seems like I'm making a whole bunch of extra function calls that I have NO idea why...stuff it getting put into the cache as it should, everything is calling the internal function... IMO this is a better way of doing things, but something is being hyper-sensitive.\n\nAnyways, I did make a few tweaks. I put `initial_call` as the last argument to make the user less likely to touch it. I also allowed the cache to take non-keyword arguments. I also made some other micro-optimizations by moving the `if edge_selector is None:` into the `initial_call` block and moved the `x,y = R.gens()`.",
    "created_at": "2014-01-07T18:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8323",
    "user": "https://github.com/tscrim"
}
```

I put my changes in the branch `u/tscrim/tutte_polynomial-1314` and reverted back the public branch. It seems like I'm making a whole bunch of extra function calls that I have NO idea why...stuff it getting put into the cache as it should, everything is calling the internal function... IMO this is a better way of doing things, but something is being hyper-sensitive.

Anyways, I did make a few tweaks. I put `initial_call` as the last argument to make the user less likely to touch it. I also allowed the cache to take non-keyword arguments. I also made some other micro-optimizations by moving the `if edge_selector is None:` into the `initial_call` block and moved the `x,y = R.gens()`.



---

archive/issue_comments_008324.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2014-01-07T19:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8324",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_008325.json:
```json
{
    "body": "Okay, I figured out what was changing. I wasn't caching the final result of the Tutte polynomial, and how it currently is done will overly clear the cache. For example, say you compute the Tutte polynomial on some large graph `G`, then you compute it on a very small graph `H` and ask it to clear the cache. Now the cached data for `G` is gone. I think we should always cache the final results, and with the current implementation, there is the possibility we've already computed the Tutte polynomial of a small graph. However I think this will be infrequent or you should not be clearing the utility cache.\n\nAlthough there is a problem, we get memory leaks. Now one can argue with the previous behavior along with the default implementation, this is not a leak. If the user was deciding to keep the cache, this would be the user knowing what (s)he is doing. Yet I wouldn't want my small computation to destroy the data of my big one, nor store it myself. So which way should we go, and if we go with 2 caches, how usable would the weak caches be? Feedback is needed.\n\nSimon, Nils -- I cc-ed you here because we might need a good weak cache solution here and I'd like your thoughts and expertise.\n----\nNew commits:",
    "created_at": "2014-01-07T19:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8325",
    "user": "https://github.com/tscrim"
}
```

Okay, I figured out what was changing. I wasn't caching the final result of the Tutte polynomial, and how it currently is done will overly clear the cache. For example, say you compute the Tutte polynomial on some large graph `G`, then you compute it on a very small graph `H` and ask it to clear the cache. Now the cached data for `G` is gone. I think we should always cache the final results, and with the current implementation, there is the possibility we've already computed the Tutte polynomial of a small graph. However I think this will be infrequent or you should not be clearing the utility cache.

Although there is a problem, we get memory leaks. Now one can argue with the previous behavior along with the default implementation, this is not a leak. If the user was deciding to keep the cache, this would be the user knowing what (s)he is doing. Yet I wouldn't want my small computation to destroy the data of my big one, nor store it myself. So which way should we go, and if we go with 2 caches, how usable would the weak caches be? Feedback is needed.

Simon, Nils -- I cc-ed you here because we might need a good weak cache solution here and I'd like your thoughts and expertise.
----
New commits:



---

archive/issue_comments_008326.json:
```json
{
    "body": "Ahahahah. So you will not do without a \"local cache\" and a \"global cache\". You want to use the global cache to speedup the results, and you want to clear the local cache only. And merge the two if the user wants to keep it.\n\nAnd what happens if the local cache generates values that exist in the global cache too ? `:-P` What do you cache then ? `:-P`\n\nI think you are overthinking very simple needs `:-)`\n\nNathann",
    "created_at": "2014-01-07T19:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8326",
    "user": "https://github.com/nathanncohen"
}
```

Ahahahah. So you will not do without a "local cache" and a "global cache". You want to use the global cache to speedup the results, and you want to clear the local cache only. And merge the two if the user wants to keep it.

And what happens if the local cache generates values that exist in the global cache too ? `:-P` What do you cache then ? `:-P`

I think you are overthinking very simple needs `:-)`

Nathann



---

archive/issue_comments_008327.json:
```json
{
    "body": "Replying to [comment:71 tscrim]:\n> Okay, ``@`cached_function` doesn't work because we can't pass a key function to it...\n\nI don't understand what you mean with this. Note that in the `@`_cached decorator you are not passing an arbitrary key function either: You have _cache_key hardcoded.",
    "created_at": "2014-01-07T21:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8327",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:71 tscrim]:
> Okay, ``@`cached_function` doesn't work because we can't pass a key function to it...

I don't understand what you mean with this. Note that in the `@`_cached decorator you are not passing an arbitrary key function either: You have _cache_key hardcoded.



---

archive/issue_comments_008328.json:
```json
{
    "body": "Replying to [comment:77 ncohen]:\n> Ahahahah. So you will not do without a \"local cache\" and a \"global cache\". You want to use the global cache to speedup the results, and you want to clear the local cache only. And merge the two if the user wants to keep it.\n\nWhat we should probably do, if we do keep a global cache, is during the computation check if the key is in the global cache as well. However I'm thinking we should not have a global cache because we get a memory leak. Create a graph `G`, compute it's Tutte polynomial, then delete `G`. The polynomial is now stuck in the global cache (that we don't want to have to manually clear). I'm thinking the better way to do things is only have a local cache and make `tutte_polynomial()` a cached method of the graphs. That way when we delete the graph (along with the local cache), the resulting polynomial can be garbage collected. It's probably better to call the local cache the computation cache.\n\n> And what happens if the local cache generates values that exist in the global cache too ? `:-P` What do you cache then ? `:-P`\n\nIn effect what I'm proposing is we keep them completely separate, I think that would create the least amount of problems. One other thing we could do is keep a small fixed-size permanent cache.\n\nThat gives me an idea about something else to do: have an option for the max size of a truly local cache when doing the computations. A priority queue up to some fixed size which keeps track of computed Tutte polynomials (with the priority being most often computed or some other heuristic) from that in the local cache. However the above, which turns it into a paging problem, might be an over-thought approach.\n\nHow big of a concern is it for recomputing Tutte polynomials for isomorphic-but-not-identical graphs?\n\nSimon, I was trying to convert it to use the usual ``@`cached_function` instead of the custom cache.",
    "created_at": "2014-01-07T21:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8328",
    "user": "https://github.com/tscrim"
}
```

Replying to [comment:77 ncohen]:
> Ahahahah. So you will not do without a "local cache" and a "global cache". You want to use the global cache to speedup the results, and you want to clear the local cache only. And merge the two if the user wants to keep it.

What we should probably do, if we do keep a global cache, is during the computation check if the key is in the global cache as well. However I'm thinking we should not have a global cache because we get a memory leak. Create a graph `G`, compute it's Tutte polynomial, then delete `G`. The polynomial is now stuck in the global cache (that we don't want to have to manually clear). I'm thinking the better way to do things is only have a local cache and make `tutte_polynomial()` a cached method of the graphs. That way when we delete the graph (along with the local cache), the resulting polynomial can be garbage collected. It's probably better to call the local cache the computation cache.

> And what happens if the local cache generates values that exist in the global cache too ? `:-P` What do you cache then ? `:-P`

In effect what I'm proposing is we keep them completely separate, I think that would create the least amount of problems. One other thing we could do is keep a small fixed-size permanent cache.

That gives me an idea about something else to do: have an option for the max size of a truly local cache when doing the computations. A priority queue up to some fixed size which keeps track of computed Tutte polynomials (with the priority being most often computed or some other heuristic) from that in the local cache. However the above, which turns it into a paging problem, might be an over-thought approach.

How big of a concern is it for recomputing Tutte polynomials for isomorphic-but-not-identical graphs?

Simon, I was trying to convert it to use the usual ``@`cached_function` instead of the custom cache.



---

archive/issue_comments_008329.json:
```json
{
    "body": "Replying to [comment:77 ncohen]:\n> Ahahahah. So you will not do without a \"local cache\" and a \"global cache\". You want to use the global cache to speedup the results, and you want to clear the local cache only. And merge the two if the user wants to keep it.\n\nWhere are the two merged? I can't see it in the code.\n\n> And what happens if the local cache generates values that exist in the global cache too ?\n\nWhat should happen? You have two caches caching the same value. You clear the first cache. The value is still in the second cache.",
    "created_at": "2014-01-07T21:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8329",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:77 ncohen]:
> Ahahahah. So you will not do without a "local cache" and a "global cache". You want to use the global cache to speedup the results, and you want to clear the local cache only. And merge the two if the user wants to keep it.

Where are the two merged? I can't see it in the code.

> And what happens if the local cache generates values that exist in the global cache too ?

What should happen? You have two caches caching the same value. You clear the first cache. The value is still in the second cache.



---

archive/issue_comments_008330.json:
```json
{
    "body": "Replying to [comment:79 tscrim]:\n> I'm thinking the better way to do things is only have a local cache and make `tutte_polynomial()` a cached method of the graphs.\n\nSounds reasonable.\n\n> Simon, I was trying to convert it to use the usual ``@`cached_function` instead of the custom cache.\n\nCan you use immutable graphs? See #15278, #15603, #15619 and #15622. These can be used as dictionary key and are thus acceptable input for a cached function.",
    "created_at": "2014-01-07T22:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8330",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:79 tscrim]:
> I'm thinking the better way to do things is only have a local cache and make `tutte_polynomial()` a cached method of the graphs.

Sounds reasonable.

> Simon, I was trying to convert it to use the usual ``@`cached_function` instead of the custom cache.

Can you use immutable graphs? See #15278, #15603, #15619 and #15622. These can be used as dictionary key and are thus acceptable input for a cached function.



---

archive/issue_comments_008331.json:
```json
{
    "body": "The problem is we can't currently do any preprocessing  on the arguments for ``@`cached_function`(like we do for `UniqueRepresentation`), or at least that I'm aware of. So if we pass in a mutable graph, we can't convert it into something immutable and ``@`cached_function` returns an error (or do any other form of standardization).",
    "created_at": "2014-01-07T23:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8331",
    "user": "https://github.com/tscrim"
}
```

The problem is we can't currently do any preprocessing  on the arguments for ``@`cached_function`(like we do for `UniqueRepresentation`), or at least that I'm aware of. So if we pass in a mutable graph, we can't convert it into something immutable and ``@`cached_function` returns an error (or do any other form of standardization).



---

archive/issue_comments_008332.json:
```json
{
    "body": "I pushed a change which just makes the cache an optional keyword argument.  All of the sub-calls to tutte_polynomial use the same cache as the top-level one.  Additionally, if the use does not want the cache destroyed at the end of the computation, they just provide their own dictionary to the method.\n----\nNew commits:",
    "created_at": "2014-01-08T01:41:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8332",
    "user": "https://github.com/mwhansen"
}
```

I pushed a change which just makes the cache an optional keyword argument.  All of the sub-calls to tutte_polynomial use the same cache as the top-level one.  Additionally, if the use does not want the cache destroyed at the end of the computation, they just provide their own dictionary to the method.
----
New commits:



---

archive/issue_comments_008333.json:
```json
{
    "body": "I like the elegance of it; so positive review from me. Nathann and anyone else, any objections?",
    "created_at": "2014-01-09T16:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8333",
    "user": "https://github.com/tscrim"
}
```

I like the elegance of it; so positive review from me. Nathann and anyone else, any objections?



---

archive/issue_comments_008334.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2014-01-09T16:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8334",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_008335.json:
```json
{
    "body": "> I like the elegance of it; so positive review from me. Nathann and anyone else, any objections?\n\nNono, it's fine `:-)`\n\nNathann",
    "created_at": "2014-01-09T16:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8335",
    "user": "https://github.com/nathanncohen"
}
```

> I like the elegance of it; so positive review from me. Nathann and anyone else, any objections?

Nono, it's fine `:-)`

Nathann



---

archive/issue_comments_008336.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-01-09T16:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8336",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_008337.json:
```json
{
    "body": "For a future ticket with #15657 - make `Graph.tutte_polynomial` a ``@`cached_method` once ``@`cached_method` can ignore the cache argument.",
    "created_at": "2014-01-09T16:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8337",
    "user": "https://github.com/tscrim"
}
```

For a future ticket with #15657 - make `Graph.tutte_polynomial` a ``@`cached_method` once ``@`cached_method` can ignore the cache argument.



---

archive/issue_events_003439.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-01-11T14:56:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1314#event-3439"
}
```



---

archive/issue_comments_008338.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-01-11T14:56:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1314",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1314#issuecomment-8338",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed

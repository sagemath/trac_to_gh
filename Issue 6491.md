# Issue 6491: [with spkg, needs review] Modular Cohomology Rings of Finite p-Groups

archive/issues_006491.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @jhpalmieri david.green@uni-jena.de\n\nKeywords: cohomology ring finite p-group\n\nI suggest to distribute our package for the computation of modular cohomology rings of finite p-groups as an optional package.\n\n## Authors\n\n- Simon A. King (Since recently at National University of Ireland, Galway)\n- David J. Green (Friedrich-Schiller-Universit\u00e4t Jena)\n\n## Installation\n\nThe package can be installed by \n\n```\nsage -i http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.0.spkg\n```\n\n\n## Purpose\n\nGiven any group of order `p^n` (where `p` is prime), compute the cohomology ring (in terms of minimal generators and relations and also providing various ring theoretic invariants) of the group with coeffients in the finite field of order `p`. Of course, induced homomorphisms can be computed as well.\n\n## Documentation\n\nAn extensive documentation can be found at [http://sage.math.washington.edu/home/SimonKing/Cohomology/](http://sage.math.washington.edu/home/SimonKing/Cohomology/).\n\n## Features\n\nThe package includes the cohomology rings of all groups of order 64. These are actually quite challenging for other software (e.g., the Hap package for Gap, or the Magma programs of Jon F. Carlson with which these cohomology rings were first computed).\n\nOn sage.math, there are the cohomology rings for all groups of order 128, and the package can download them. **Sage is the only CAS that can currently provide such data.** Similarly, the cohomology of the groups of order 243 is available, but six of them are still not completely computed yet.\n\n## Sources\n\nThe comprises\n- a modified old version of the Aachen C-MeatAxe, \n- C-routines and Gap functions of David J. Green for the computation of minimal projective resolutions, and\n- various Cython extension modules and Singular functions written by myself, computing the structure of the cohomology ring according to algorithms of Dave Benson and David J. Green. \n- Data for the cohomology of all groups of order 64.\n\nThe C-MeatAxe is considerably modified, the rest of the sources has never been published yet. Therefore we included all of the sources into the Mercurial repository.\n\n## Dependencies\n\nIt is required that the SmallGroups library is installed.\n\nSince I too often had to work around bugs in the non-commutative part of Singular 3-0-4, it is required that Singular 3-1-0 is available when dealing with a finite p-Group and p>2.\n\n## Testing\n\nI am afraid that there is no separate test suite for the C-sources. The package includes two scripts `spkg-check` and `spkg-check-details`, that both walk through all doc tests. `spkg-check-details` is slower, but in case of errors provides more direct pointers to the failing tests than `spkg-check`. The scripts also verify the presence of doc test in any method.\n\nNote that some tests require internet connection, as data will be downloaded.\n\n## Known issues\n\n- It is not clear to me how one properly works with Licences. I did my very best. But could please some more experienced person check whether everything is alright with the licence?\n\n- A couple of months ago, I tried to build an earlier version of the package on OS X. It failed, which was very likely due to C-MeatAxe, which in fact does not seem to support OS X (even in the most recent version). But this was without distutils. Perhaps someone can test it, as I do not have access to OS X.\n\n- By the way of saving matrices in the MeatAxe format, it is very likely that the porting between big and little endian machines will be impossible. In particular, it could turn out to be impossible to use the data bases with a motorola processor.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6491\n\n",
    "created_at": "2009-07-09T01:38:20Z",
    "labels": [
        "component: packages: optional"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with spkg, needs review] Modular Cohomology Rings of Finite p-Groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6491",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: tbd

CC:  @jhpalmieri david.green@uni-jena.de

Keywords: cohomology ring finite p-group

I suggest to distribute our package for the computation of modular cohomology rings of finite p-groups as an optional package.

## Authors

- Simon A. King (Since recently at National University of Ireland, Galway)
- David J. Green (Friedrich-Schiller-Universität Jena)

## Installation

The package can be installed by 

```
sage -i http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.0.spkg
```


## Purpose

Given any group of order `p^n` (where `p` is prime), compute the cohomology ring (in terms of minimal generators and relations and also providing various ring theoretic invariants) of the group with coeffients in the finite field of order `p`. Of course, induced homomorphisms can be computed as well.

## Documentation

An extensive documentation can be found at [http://sage.math.washington.edu/home/SimonKing/Cohomology/](http://sage.math.washington.edu/home/SimonKing/Cohomology/).

## Features

The package includes the cohomology rings of all groups of order 64. These are actually quite challenging for other software (e.g., the Hap package for Gap, or the Magma programs of Jon F. Carlson with which these cohomology rings were first computed).

On sage.math, there are the cohomology rings for all groups of order 128, and the package can download them. **Sage is the only CAS that can currently provide such data.** Similarly, the cohomology of the groups of order 243 is available, but six of them are still not completely computed yet.

## Sources

The comprises
- a modified old version of the Aachen C-MeatAxe, 
- C-routines and Gap functions of David J. Green for the computation of minimal projective resolutions, and
- various Cython extension modules and Singular functions written by myself, computing the structure of the cohomology ring according to algorithms of Dave Benson and David J. Green. 
- Data for the cohomology of all groups of order 64.

The C-MeatAxe is considerably modified, the rest of the sources has never been published yet. Therefore we included all of the sources into the Mercurial repository.

## Dependencies

It is required that the SmallGroups library is installed.

Since I too often had to work around bugs in the non-commutative part of Singular 3-0-4, it is required that Singular 3-1-0 is available when dealing with a finite p-Group and p>2.

## Testing

I am afraid that there is no separate test suite for the C-sources. The package includes two scripts `spkg-check` and `spkg-check-details`, that both walk through all doc tests. `spkg-check-details` is slower, but in case of errors provides more direct pointers to the failing tests than `spkg-check`. The scripts also verify the presence of doc test in any method.

Note that some tests require internet connection, as data will be downloaded.

## Known issues

- It is not clear to me how one properly works with Licences. I did my very best. But could please some more experienced person check whether everything is alright with the licence?

- A couple of months ago, I tried to build an earlier version of the package on OS X. It failed, which was very likely due to C-MeatAxe, which in fact does not seem to support OS X (even in the most recent version). But this was without distutils. Perhaps someone can test it, as I do not have access to OS X.

- By the way of saving matrices in the MeatAxe format, it is very likely that the porting between big and little endian machines will be impossible. In particular, it could turn out to be impossible to use the data bases with a motorola processor.

Issue created by migration from https://trac.sagemath.org/ticket/6491





---

archive/issue_comments_052379.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-09T10:48:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52379",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from new to assigned.



---

archive/issue_comments_052380.json:
```json
{
    "body": "Changing assignee from tbd to @simon-king-jena.",
    "created_at": "2009-07-09T10:48:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52380",
    "user": "https://github.com/simon-king-jena"
}
```

Changing assignee from tbd to @simon-king-jena.



---

archive/issue_comments_052381.json:
```json
{
    "body": "Some comments: Seems to be installing okay (amd 64 ubuntu 9.04).\n\nBefore installing database_gap*.spkg I got an error reading something like \"cannot access database_gap\" or something. Does it actually require that spkg or merely smallgroup in gap*/pkg?\n\nWaht is the license of the version of Meataxe you are using?\n\nLooks like a *great* contribution Simon!",
    "created_at": "2009-07-10T14:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52381",
    "user": "https://github.com/wdjoyner"
}
```

Some comments: Seems to be installing okay (amd 64 ubuntu 9.04).

Before installing database_gap*.spkg I got an error reading something like "cannot access database_gap" or something. Does it actually require that spkg or merely smallgroup in gap*/pkg?

Waht is the license of the version of Meataxe you are using?

Looks like a *great* contribution Simon!



---

archive/issue_comments_052382.json:
```json
{
    "body": "Replying to [comment:4 wdj]:\n> Some comments: Seems to be installing okay (amd 64 ubuntu 9.04).\n\nCool! That is a system that I didn't try.\n\n> Before installing database_gap*.spkg I got an error reading something like \"cannot access database_gap\" or something. Does it actually require that spkg or merely smallgroup in gap*/pkg?\n\nIt should be possible to do, e.g., `gap('SmallGroup(8,3)')` or `gap('NumberSmallGroups(64)')`. I thought the safest is to test that the spkg is installed, but the essential thing is the smallgroups library.\n\n> Waht is the license of the version of Meataxe you are using?\n\nAs I said, I have no clear idea about licences. Anyway, there is a COPYING file in the Meataxe sources. It starts with\n\n```\n                    GNU GENERAL PUBLIC LICENSE\n                       Version 2, June 1991\n\n Copyright (C) 1989, 1991 Free Software Foundation, Inc.\n                          675 Mass Ave, Cambridge, MA 02139, USA\n Everyone is permitted to copy and distribute verbatim copies\n of this license document, but changing it is not allowed.\n```\n\n\n> Looks like a *great* contribution Simon!\n\nThank you! It was a project extending over two years.\n\nCheers,\n   Simon",
    "created_at": "2009-07-10T14:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52382",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:4 wdj]:
> Some comments: Seems to be installing okay (amd 64 ubuntu 9.04).

Cool! That is a system that I didn't try.

> Before installing database_gap*.spkg I got an error reading something like "cannot access database_gap" or something. Does it actually require that spkg or merely smallgroup in gap*/pkg?

It should be possible to do, e.g., `gap('SmallGroup(8,3)')` or `gap('NumberSmallGroups(64)')`. I thought the safest is to test that the spkg is installed, but the essential thing is the smallgroups library.

> Waht is the license of the version of Meataxe you are using?

As I said, I have no clear idea about licences. Anyway, there is a COPYING file in the Meataxe sources. It starts with

```
                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.
                          675 Mass Ave, Cambridge, MA 02139, USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
```


> Looks like a *great* contribution Simon!

Thank you! It was a project extending over two years.

Cheers,
   Simon



---

archive/issue_comments_052383.json:
```json
{
    "body": "William suggested at sage-devel that I should tell precisely how I think the package should be tested, addressing the following areas:\n\n### What hardware/OS combos should it be tried to install\n\nSo far, I successfully installed the package on Intel Pentium M, two processor types of AMD (Opteron and another one that I can't remember), and Sun X4450 (sage.math). The OS was SuSE Linux on the three machines that I had in Jena.\n\nSo, there are plenty of architectures which aren't tested, yet. As I indicated, I expect that OS X and Motorola processors are most challenging. But I leave it up to you, since so far I did not do extensive porting.\n\n### What commands should be tested, and what should happen?\n\n__A) The test script__ \n\nThere is `spkg-check`, which should of course work without errors. Note that the script needs to be executed in a Sage shell. Note that some tests assume that Singular is present in version 3-1-0, and that there is internet connection. If you get an error of Singular mentioning the timer, this is most likely related with ticket #6412, so please apply the patch...\n\n__B) Groups of order 64 (should be less than 1 hour)__\n\nOne of my favourite benchmarks are the groups of order 64. You can compute the cohomology rings as follows.\n\n```\nsage: from pGroupCohomology import CohomologyRing\nsage: tmp_root = tmp_filename() # chosing a temporary location, or choose a permanent if you like\nsage: CohomologyRing.set_user_db(tmp_root) # For each test, you should choose a different location,\n                                           # since otherwise data would be reloaded from previous computations.\nsage: for i in range(1,268):\n...:      H = CohomologyRing.user_db(64,i,websource=False) # avoid that the complete ring gets downloaded\n...:      H.make() # compute the ring structure\n...:      print H == CohomologyRing(64,i) # this compares H with the pre-computed ring in the 'public' data base \n                                          # that is shipped with the package\n```\n\n\n- The answer should be `True` in all cases. \n- It might also be interesting how long the computation takes.\n- The doc string of `CohomologyRing` mentions various options -- try them out!\n\n__C) Non-abelian case (p!=2)__\n\nIf you have a new Sage version, with Singular 3-1-0, you may also try whether the computation for all groups of order 81 works without error. Note, however, that these rings are not included in the package, hence it makes no sense to test `CohomologyRing.user_db(81,i)` against `CohomologyRing(81,i)`\n\n__D) 1. Groups given in the Gap interface__\n\nConstruct any finite p-Group G (if you only have Singular 3-0-4, p must be 2) in the Gap interface. Try to compute the cohomology ring using `H=CohomologyRing.user_db(G,GroupName='NameOfYourGroup', options='prot')`, followed by `H.make()`. The protocol output might give you a feeling of what happens inside, or, should an error occur, might point to the source of trouble.\n\nNote that *an initial segment of the generator sequence of G must be a minimal generating  set*. Otherwise, the package would complain.\n\n__D) 2. Induced homomorphisms__\n\nIf you have two groups G1, G2 matching the condition on the generating sets, with H1,H2 the respective cohomology rings,  construct a homomorphism G1 -> G2, and try to compute the induced map. See the documentation of H1.hom about how it works.\n\nIn particular, take an __auto__morphism `phi:G1 -> G1`. Compute the induced map `phi_star=H1.hom(phi,H1)`. Try `phi_star^(-1)`, `phi_star^3`, apply phi_star to elements of the cohomology ring, etc.\n\n__E) Test various methods__\n\nIf you don't have Singular 3-1-0, choose a different group:\n\n```\nsage: from pGroupCohomology import CohomologyRing\nsage: ROOT = '/home/SimonKing/CTest'  # choose your own root folder, you need write permissions\nsage: CohomologyRing.set_user_db(ROOT)\nsage: H = CohomologyRing.user_db(27,3, options='prot', websource=False)\n#... some protocol output\nsage: H.make()\n#... tons of protocol output\nsage: H.nil_radical()\n#... some protocol output\na_1_0,\na_1_1,\na_3_4,\na_3_5,\nb_2_0*b_2_3-b_2_0*b_2_1,\nb_2_1^2-b_2_0*b_2_2-b_2_0*b_2_1,\nb_2_1*b_2_2+b_2_0*b_2_2,\nb_2_1*b_2_3-b_2_0*b_2_2-b_2_0*b_2_1,\nb_2_2^2+b_2_0*b_2_2,\nb_2_2*b_2_3+b_2_0*b_2_2\n```\n\n\n\n### RTFM\n\nThere is extensive documentation at [http://sage.math.washington.edu/home/SimonKing/Cohomology/](http://sage.math.washington.edu/home/SimonKing/Cohomology/). Please read some chapters and see whether you find it clearly explained and whether it teaches you how to use the package. If not, please tell me!\n\nI believe the package (should it be possible to install on your system) is already useful. But certainly there are many more things that one might want to know about cohomology rings: More ring theoretic invariants, for example. Please tell me what functionality you are missing, so that later versions of the package might implement it.",
    "created_at": "2009-07-10T14:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52383",
    "user": "https://github.com/simon-king-jena"
}
```

William suggested at sage-devel that I should tell precisely how I think the package should be tested, addressing the following areas:

### What hardware/OS combos should it be tried to install

So far, I successfully installed the package on Intel Pentium M, two processor types of AMD (Opteron and another one that I can't remember), and Sun X4450 (sage.math). The OS was SuSE Linux on the three machines that I had in Jena.

So, there are plenty of architectures which aren't tested, yet. As I indicated, I expect that OS X and Motorola processors are most challenging. But I leave it up to you, since so far I did not do extensive porting.

### What commands should be tested, and what should happen?

__A) The test script__ 

There is `spkg-check`, which should of course work without errors. Note that the script needs to be executed in a Sage shell. Note that some tests assume that Singular is present in version 3-1-0, and that there is internet connection. If you get an error of Singular mentioning the timer, this is most likely related with ticket #6412, so please apply the patch...

__B) Groups of order 64 (should be less than 1 hour)__

One of my favourite benchmarks are the groups of order 64. You can compute the cohomology rings as follows.

```
sage: from pGroupCohomology import CohomologyRing
sage: tmp_root = tmp_filename() # chosing a temporary location, or choose a permanent if you like
sage: CohomologyRing.set_user_db(tmp_root) # For each test, you should choose a different location,
                                           # since otherwise data would be reloaded from previous computations.
sage: for i in range(1,268):
...:      H = CohomologyRing.user_db(64,i,websource=False) # avoid that the complete ring gets downloaded
...:      H.make() # compute the ring structure
...:      print H == CohomologyRing(64,i) # this compares H with the pre-computed ring in the 'public' data base 
                                          # that is shipped with the package
```


- The answer should be `True` in all cases. 
- It might also be interesting how long the computation takes.
- The doc string of `CohomologyRing` mentions various options -- try them out!

__C) Non-abelian case (p!=2)__

If you have a new Sage version, with Singular 3-1-0, you may also try whether the computation for all groups of order 81 works without error. Note, however, that these rings are not included in the package, hence it makes no sense to test `CohomologyRing.user_db(81,i)` against `CohomologyRing(81,i)`

__D) 1. Groups given in the Gap interface__

Construct any finite p-Group G (if you only have Singular 3-0-4, p must be 2) in the Gap interface. Try to compute the cohomology ring using `H=CohomologyRing.user_db(G,GroupName='NameOfYourGroup', options='prot')`, followed by `H.make()`. The protocol output might give you a feeling of what happens inside, or, should an error occur, might point to the source of trouble.

Note that *an initial segment of the generator sequence of G must be a minimal generating  set*. Otherwise, the package would complain.

__D) 2. Induced homomorphisms__

If you have two groups G1, G2 matching the condition on the generating sets, with H1,H2 the respective cohomology rings,  construct a homomorphism G1 -> G2, and try to compute the induced map. See the documentation of H1.hom about how it works.

In particular, take an __auto__morphism `phi:G1 -> G1`. Compute the induced map `phi_star=H1.hom(phi,H1)`. Try `phi_star^(-1)`, `phi_star^3`, apply phi_star to elements of the cohomology ring, etc.

__E) Test various methods__

If you don't have Singular 3-1-0, choose a different group:

```
sage: from pGroupCohomology import CohomologyRing
sage: ROOT = '/home/SimonKing/CTest'  # choose your own root folder, you need write permissions
sage: CohomologyRing.set_user_db(ROOT)
sage: H = CohomologyRing.user_db(27,3, options='prot', websource=False)
#... some protocol output
sage: H.make()
#... tons of protocol output
sage: H.nil_radical()
#... some protocol output
a_1_0,
a_1_1,
a_3_4,
a_3_5,
b_2_0*b_2_3-b_2_0*b_2_1,
b_2_1^2-b_2_0*b_2_2-b_2_0*b_2_1,
b_2_1*b_2_2+b_2_0*b_2_2,
b_2_1*b_2_3-b_2_0*b_2_2-b_2_0*b_2_1,
b_2_2^2+b_2_0*b_2_2,
b_2_2*b_2_3+b_2_0*b_2_2
```



### RTFM

There is extensive documentation at [http://sage.math.washington.edu/home/SimonKing/Cohomology/](http://sage.math.washington.edu/home/SimonKing/Cohomology/). Please read some chapters and see whether you find it clearly explained and whether it teaches you how to use the package. If not, please tell me!

I believe the package (should it be possible to install on your system) is already useful. But certainly there are many more things that one might want to know about cohomology rings: More ring theoretic invariants, for example. Please tell me what functionality you are missing, so that later versions of the package might implement it.



---

archive/issue_comments_052384.json:
```json
{
    "body": "Replying to [comment:5 SimonKing]:\n> > Before installing database_gap*.spkg I got an error reading something like \"cannot access database_gap\" or something. Does it actually require that spkg or merely smallgroup in gap*/pkg?\n> \n> It should be possible to do, e.g., `gap('SmallGroup(8,3)')` or `gap('NumberSmallGroups(64)')`.\n\nPerhaps this formulation is not clear enough: The above commands *must* work, otherwise the cohomology package can not even start with the computation.\n\nCheers, \n   Simon",
    "created_at": "2009-07-10T14:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52384",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:5 SimonKing]:
> > Before installing database_gap*.spkg I got an error reading something like "cannot access database_gap" or something. Does it actually require that spkg or merely smallgroup in gap*/pkg?
> 
> It should be possible to do, e.g., `gap('SmallGroup(8,3)')` or `gap('NumberSmallGroups(64)')`.

Perhaps this formulation is not clear enough: The above commands *must* work, otherwise the cohomology package can not even start with the computation.

Cheers, 
   Simon



---

archive/issue_comments_052385.json:
```json
{
    "body": "Replying to [comment:7 SimonKing]:\n> Replying to [comment:5 SimonKing]:\n> > > Before installing database_gap*.spkg I got an error reading something like \"cannot access database_gap\" or something. Does it actually require that spkg or merely smallgroup in gap*/pkg?\n> > \n> > It should be possible to do, e.g., `gap('SmallGroup(8,3)')` or `gap('NumberSmallGroups(64)')`.\n> \n> Perhaps this formulation is not clear enough: The above commands *must* work, otherwise the cohomology package can not even start with the computation.\n> \n> Cheers, \n>    Simon\n\n\n\nThanks. \n\nIn that case, I think it should be made clear in the installation docs that to install the package you need to have run sage -i database_gap*.\n\nI'm trying to see how this compares with GAP's CRIME package. It seems to me that you using a completely different way of representing the cohomology rings. Is that correct? If not, is there a simple example using your package that can also be used with CRIME to compare their outputs?\nFor example, the dihedral group of order 8. It seems that CRIME wants to truncate the ring at a given degree and you don't (but maybe I'm wrong here?), so I don't see how to easily compare them.\n\nBTW, I am testing the innstallation on an older amd64 ubuntu 8.10 machine. Seems to be going okay there too.",
    "created_at": "2009-07-10T17:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52385",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:7 SimonKing]:
> Replying to [comment:5 SimonKing]:
> > > Before installing database_gap*.spkg I got an error reading something like "cannot access database_gap" or something. Does it actually require that spkg or merely smallgroup in gap*/pkg?
> > 
> > It should be possible to do, e.g., `gap('SmallGroup(8,3)')` or `gap('NumberSmallGroups(64)')`.
> 
> Perhaps this formulation is not clear enough: The above commands *must* work, otherwise the cohomology package can not even start with the computation.
> 
> Cheers, 
>    Simon



Thanks. 

In that case, I think it should be made clear in the installation docs that to install the package you need to have run sage -i database_gap*.

I'm trying to see how this compares with GAP's CRIME package. It seems to me that you using a completely different way of representing the cohomology rings. Is that correct? If not, is there a simple example using your package that can also be used with CRIME to compare their outputs?
For example, the dihedral group of order 8. It seems that CRIME wants to truncate the ring at a given degree and you don't (but maybe I'm wrong here?), so I don't see how to easily compare them.

BTW, I am testing the innstallation on an older amd64 ubuntu 8.10 machine. Seems to be going okay there too.



---

archive/issue_comments_052386.json:
```json
{
    "body": "Replying to [comment:8 wdj]:\n> In that case, I think it should be made clear in the installation docs that to install the package you need to have run sage -i database_gap*.\n\nWhat do you mean by \"installation docs\"? [http://sage.math.washington.edu/home/SimonKing/Cohomology/#installation](http://sage.math.washington.edu/home/SimonKing/Cohomology/#installation) ? Yes, you are right. I will add a few words later today.\n\n> I'm trying to see how this compares with GAP's CRIME package. It seems to me that you using a completely different way of representing the cohomology rings. Is that correct? If not, is there a simple example using your package that can also be used with CRIME to compare their outputs?\n> For example, the dihedral group of order 8. It seems that CRIME wants to truncate the ring at a given degree and you don't (but maybe I'm wrong here?), so I don't see how to easily compare them.\n\nI must admit that I was not aware of CRIME, although Marcus Bishop currently is in Galway (so am I, since very recently). I only knew HAP (from Galway, too), that can also compute cohomology.\n\nLooking at the CRIME manual, I think it compares with our package as follows:\n\n- We work with coefficients GF(p); CRIME allows more general modules.\n- Apparently, when doing `C:=CohomologyObject( G )` in CRIME, you get a not-yet-completed cohomology ring; this is similar to `H=CohomologyRing(G)` or `H=CohomologyRing(q,m)`, if G or SmallGroup(q,m) are not yet in our data base.\n- Both CRIME and our package rely on the construction of minimal projective resolutions. We use David Green's Gr\u00f6bner basis approach, while probably CRIME uses linear algebra.\n- Indeed, CRIME works with truncated rings. For example, `CohomologyGenerators( C, n )` computes the ring out to degree `n` and returns the generators that it found. With our package, one could do the same, doing `H.make(n); H.gens()`. Our `H.make(n)` is similar to `CohomologyRing(G,n)`.\n- `CohomologyGenerators( C, n )` only yields the *degrees* of the generators. `H.gens()` yields the generators themselves, and you can actually do computations with them. Actually, from the documentation, I get the impression that CRIME does provide (truncated) Cohomology Rings, but it does not provide *elements* of Cohomology Rings.\n- The most important difference: Apparently CRIME has no completeness criterion. Section 2.4 states: \"A test or series of tests for completion of the calculation will hopefully be implemented soon. See [CTVZ03] for the details.\" So, there is no analogue for our `H.make()`.\n\nAlso my impression is that we provide more things to do with a cohomology ring:\n\nWe implemented the computation of some ring theoretic invariants: Depth, Poincar\u00e9 series, a-invariants. Also we are able to compute the nil radical. For these operations, we make extensive use of the fact that we have a cohomology ring: We use Benson's completeness criterion, which involves the computation of a filter regular system  of parameters. These parameters allow for an easy computation of depth and Poincare series, and with a slightly extended machinery we also get the a-invariants. The nil radical is obtained by studying the restrictions to the maximal elementary abelian subgroups (which we do anyway when we choose our generators!).\n\nMy impression from the CRIME doc is that the computation would be much more clumsy: \n* Compute the ring structure C (Problem 1: There is no completeness criterion)\n* Create a quotient of a polynomial ring P/I that has this ring structure. \n* Problem 2: On the way you loose the information that C was a cohomology ring. Now you just have an abstract ring presentation P/I, and then the computation of the nil radical or the Poincare series becomes much harder.\n\nBack to your question:\n> I'm trying to see how this compares with GAP's CRIME package. It seems to me that you using a completely different way of representing the cohomology rings. Is that correct? If not, is there a simple example using your package that can also be used with CRIME to compare their outputs?\n\nNote that our favourite example (cohomology of the Dihedral Group of order 8) also appears in the CRIME documentation. Of course, we get essentially the same result -- but we can prove that our result is complete and not just a truncated version of the cohomology ring.\n\nWhat you could always do: Make a complete computation with our package, and use it to get the right truncation degree for CRIME, hence:\n\n```\nsage: G = your favourit p-group\nsage: H = CohomologyRing.user_db(G)\nsage: H.make()\nsage: n=H.knownDeg\n```\n\n\nThe last line means that n tells in what degree we drove our computation before realising that it was complete. So, you could now use CRIME:\n\n``` \nC := CohomologyRing(G,n);\n```\n\nand get the ring structure. \n\nThen you can compare with our result. Of course, in general the relations will look different. But: The number of generators sorted by degree and the number of relations sorted by degree should be the same with CRIME and our package. And, if you are able to compute the Poincar\u00e9 series with CRIME, again the result should be the same.\n\nActually this is how we compared our computational findings with the results of Jon F. Carlson.\n\n> BTW, I am testing the innstallation on an older amd64 ubuntu 8.10 machine. Seems to be going okay there too.\n\nGood news!\n\nCheers,\n   Simon",
    "created_at": "2009-07-10T18:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52386",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:8 wdj]:
> In that case, I think it should be made clear in the installation docs that to install the package you need to have run sage -i database_gap*.

What do you mean by "installation docs"? [http://sage.math.washington.edu/home/SimonKing/Cohomology/#installation](http://sage.math.washington.edu/home/SimonKing/Cohomology/#installation) ? Yes, you are right. I will add a few words later today.

> I'm trying to see how this compares with GAP's CRIME package. It seems to me that you using a completely different way of representing the cohomology rings. Is that correct? If not, is there a simple example using your package that can also be used with CRIME to compare their outputs?
> For example, the dihedral group of order 8. It seems that CRIME wants to truncate the ring at a given degree and you don't (but maybe I'm wrong here?), so I don't see how to easily compare them.

I must admit that I was not aware of CRIME, although Marcus Bishop currently is in Galway (so am I, since very recently). I only knew HAP (from Galway, too), that can also compute cohomology.

Looking at the CRIME manual, I think it compares with our package as follows:

- We work with coefficients GF(p); CRIME allows more general modules.
- Apparently, when doing `C:=CohomologyObject( G )` in CRIME, you get a not-yet-completed cohomology ring; this is similar to `H=CohomologyRing(G)` or `H=CohomologyRing(q,m)`, if G or SmallGroup(q,m) are not yet in our data base.
- Both CRIME and our package rely on the construction of minimal projective resolutions. We use David Green's Gröbner basis approach, while probably CRIME uses linear algebra.
- Indeed, CRIME works with truncated rings. For example, `CohomologyGenerators( C, n )` computes the ring out to degree `n` and returns the generators that it found. With our package, one could do the same, doing `H.make(n); H.gens()`. Our `H.make(n)` is similar to `CohomologyRing(G,n)`.
- `CohomologyGenerators( C, n )` only yields the *degrees* of the generators. `H.gens()` yields the generators themselves, and you can actually do computations with them. Actually, from the documentation, I get the impression that CRIME does provide (truncated) Cohomology Rings, but it does not provide *elements* of Cohomology Rings.
- The most important difference: Apparently CRIME has no completeness criterion. Section 2.4 states: "A test or series of tests for completion of the calculation will hopefully be implemented soon. See [CTVZ03] for the details." So, there is no analogue for our `H.make()`.

Also my impression is that we provide more things to do with a cohomology ring:

We implemented the computation of some ring theoretic invariants: Depth, Poincaré series, a-invariants. Also we are able to compute the nil radical. For these operations, we make extensive use of the fact that we have a cohomology ring: We use Benson's completeness criterion, which involves the computation of a filter regular system  of parameters. These parameters allow for an easy computation of depth and Poincare series, and with a slightly extended machinery we also get the a-invariants. The nil radical is obtained by studying the restrictions to the maximal elementary abelian subgroups (which we do anyway when we choose our generators!).

My impression from the CRIME doc is that the computation would be much more clumsy: 
* Compute the ring structure C (Problem 1: There is no completeness criterion)
* Create a quotient of a polynomial ring P/I that has this ring structure. 
* Problem 2: On the way you loose the information that C was a cohomology ring. Now you just have an abstract ring presentation P/I, and then the computation of the nil radical or the Poincare series becomes much harder.

Back to your question:
> I'm trying to see how this compares with GAP's CRIME package. It seems to me that you using a completely different way of representing the cohomology rings. Is that correct? If not, is there a simple example using your package that can also be used with CRIME to compare their outputs?

Note that our favourite example (cohomology of the Dihedral Group of order 8) also appears in the CRIME documentation. Of course, we get essentially the same result -- but we can prove that our result is complete and not just a truncated version of the cohomology ring.

What you could always do: Make a complete computation with our package, and use it to get the right truncation degree for CRIME, hence:

```
sage: G = your favourit p-group
sage: H = CohomologyRing.user_db(G)
sage: H.make()
sage: n=H.knownDeg
```


The last line means that n tells in what degree we drove our computation before realising that it was complete. So, you could now use CRIME:

``` 
C := CohomologyRing(G,n);
```

and get the ring structure. 

Then you can compare with our result. Of course, in general the relations will look different. But: The number of generators sorted by degree and the number of relations sorted by degree should be the same with CRIME and our package. And, if you are able to compute the Poincaré series with CRIME, again the result should be the same.

Actually this is how we compared our computational findings with the results of Jon F. Carlson.

> BTW, I am testing the innstallation on an older amd64 ubuntu 8.10 machine. Seems to be going okay there too.

Good news!

Cheers,
   Simon



---

archive/issue_comments_052387.json:
```json
{
    "body": "Replying to [comment:8 wdj]:\n> > Perhaps this formulation is not clear enough: The above commands *must* work, otherwise the cohomology package can not even start with the computation.\n> In that case, I think it should be made clear in the installation docs that to install the package you need to have run sage -i database_gap*.\n\nDone, see [http://sage.math.washington.edu/home/SimonKing/Cohomology/#installation](http://sage.math.washington.edu/home/SimonKing/Cohomology/#installation)\n\nCheers,\n   Simon",
    "created_at": "2009-07-10T18:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52387",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:8 wdj]:
> > Perhaps this formulation is not clear enough: The above commands *must* work, otherwise the cohomology package can not even start with the computation.
> In that case, I think it should be made clear in the installation docs that to install the package you need to have run sage -i database_gap*.

Done, see [http://sage.math.washington.edu/home/SimonKing/Cohomology/#installation](http://sage.math.washington.edu/home/SimonKing/Cohomology/#installation)

Cheers,
   Simon



---

archive/issue_comments_052388.json:
```json
{
    "body": "Replying to [comment:9 SimonKing]:\n>  - The most important difference: Apparently CRIME has no completeness criterion. Section 2.4 states: \"A test or series of tests for completion of the calculation will hopefully be implemented soon. See [CTVZ03] for the details.\" So, there is no analogue for our `H.make()`.\n\nSince people don't know the purpose of the `make` method, a little elaboration.\n\nThere are two ways of usage:\n- `H.make(n)`: Compute at most out to degree `n`. This corresponds to the capabilities of CRIME.\n- `H.make()`: Compute in increasing degree, until (our improved version of) Benson's criterion tells us that we can stop. This can't be done in CRIME, but HAP has a completeness criterion.\n\n----\n\nPerhaps it is better to compare HAP (or actually HAPprime), rather than CRIME, with our package.\n\nHAPprime [http://www.gap-system.org/~gap/Manuals/pkg/happrime-0.3.2/doc/userguide/manual.pdf](http://www.gap-system.org/~gap/Manuals/pkg/happrime-0.3.2/doc/userguide/manual.pdf) uses a clever idea: Frst compute the Lyndon-Hoschild-Serre Spectral Sequence until convergence to \ufb01nd the additive structure of the cohomology ring, and then compute the cohomology ring itself, based on projective resolutions, up to and including the maximum necessary generator or relation degree. \n\nThe point is that this completeness criterion is perfect! However, an application of this criterion involves the computation of spectral sequences, which is perhaps not the easiest thing to do.\n\nHere is a random collection of features, and how the three packages compare. Disclaimer: I am rather tired, so, perhaps I do mistakes. Sorry in advance.\n\n \n__Complete computations:__ Possible with HAPprime and our package, impossible with CRIME.\n\n__Induced homomorphisms:__ CRIME can do, we can do, but I didn't find it addressed in the HAPprime manual.\n\n__Ring theoretic invariants:__ CRIME has nothing. HAPprime has Poincar\u00e9 series. We have Poincar\u00e9 series, depth, dimension, a-invariants, and can also compute the nil radical.\n\n__Speed:__ I don't know about CRIME. I was told by Paul Smith that HAPprime needs a few days to compute the cohomology for the groups of order 64. We need less than 60 minutes.\n\n__Coefficients:__ CRIME can do it not only over GF(p) but with higher-dimensional modules. We can do it over GF(p), p a prime that must not be greater than 255. HAPprime can do it over GF(2); Paul Smith says it also works over GF(p), p>2, but Graham Ellis seems to have some doubts.\n\nBest regards,\n   Simon",
    "created_at": "2009-07-10T21:20:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52388",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:9 SimonKing]:
>  - The most important difference: Apparently CRIME has no completeness criterion. Section 2.4 states: "A test or series of tests for completion of the calculation will hopefully be implemented soon. See [CTVZ03] for the details." So, there is no analogue for our `H.make()`.

Since people don't know the purpose of the `make` method, a little elaboration.

There are two ways of usage:
- `H.make(n)`: Compute at most out to degree `n`. This corresponds to the capabilities of CRIME.
- `H.make()`: Compute in increasing degree, until (our improved version of) Benson's criterion tells us that we can stop. This can't be done in CRIME, but HAP has a completeness criterion.

----

Perhaps it is better to compare HAP (or actually HAPprime), rather than CRIME, with our package.

HAPprime [http://www.gap-system.org/~gap/Manuals/pkg/happrime-0.3.2/doc/userguide/manual.pdf](http://www.gap-system.org/~gap/Manuals/pkg/happrime-0.3.2/doc/userguide/manual.pdf) uses a clever idea: Frst compute the Lyndon-Hoschild-Serre Spectral Sequence until convergence to ﬁnd the additive structure of the cohomology ring, and then compute the cohomology ring itself, based on projective resolutions, up to and including the maximum necessary generator or relation degree. 

The point is that this completeness criterion is perfect! However, an application of this criterion involves the computation of spectral sequences, which is perhaps not the easiest thing to do.

Here is a random collection of features, and how the three packages compare. Disclaimer: I am rather tired, so, perhaps I do mistakes. Sorry in advance.

 
__Complete computations:__ Possible with HAPprime and our package, impossible with CRIME.

__Induced homomorphisms:__ CRIME can do, we can do, but I didn't find it addressed in the HAPprime manual.

__Ring theoretic invariants:__ CRIME has nothing. HAPprime has Poincaré series. We have Poincaré series, depth, dimension, a-invariants, and can also compute the nil radical.

__Speed:__ I don't know about CRIME. I was told by Paul Smith that HAPprime needs a few days to compute the cohomology for the groups of order 64. We need less than 60 minutes.

__Coefficients:__ CRIME can do it not only over GF(p) but with higher-dimensional modules. We can do it over GF(p), p a prime that must not be greater than 255. HAPprime can do it over GF(2); Paul Smith says it also works over GF(p), p>2, but Graham Ellis seems to have some doubts.

Best regards,
   Simon



---

archive/issue_comments_052389.json:
```json
{
    "body": "1. Thanks for fixing the installation docs and the detailed comparison. That was very valuable for me anyway.\n\n2. The comparision between crime and your package is a bit more complicated that it first seems I think. For example, we have\n\n\n```\n\nsage: from pGroupCohomology import CohomologyRing\nsage: H = CohomologyRing.user_db(8,3,websource=False)\nsage: print H\n\nCohomology ring of Dihedral group of order 8 with coefficients in GF(2)\n\nComputed up to degree 2\nMinimal list of generators:\n[c_2_2, a 2-Cochain in H^*(D8; GF(2)),\n b_1_0, a 1-Cochain in H^*(D8; GF(2)),\n b_1_1, a 1-Cochain in H^*(D8; GF(2))]\nMinimal list of algebraic relations:\n[b_1_0*b_1_1]\n\nsage: gap('LoadPackage(\"crime\")')            \ntrue \nsage: gap.eval(\"C:=CohomologyObject(DihedralGroup(8))\")\n'<object>'\nsage: gap.eval(\"CohomologyGenerators(C,2)\")\n'[ 1, 1, 2 ]'\nsage: gap.eval(\"CohomologyRelators(C,2)\")\n'[ [ z, y, x ], [ z*y+y^2 ] ]'\n```\n\nThese seem different but I am not an expert. Is this difference easy to explain?\n\n3. Regarding the PoincareSeries in HAP: I think Graham Ellis told me that his PoincareSeries was likely to be true but not guaranteed. Is this right? If so, how sure are you of yours? (I checked in an example that they agree.)\n\n4. Regarding the license: \n\n(a) Can you ask any surviving Meataxe people if they might relicensing the version you used under GPLv2+?\n\n(b) Since David Green is a co-author - he can license the code as he wants:-)\n\n(c) Did you create the database \"Data for the cohomology of all groups of order 64\" yourself? If not, in the US I think this is not an issue, but overseas copyright laws for databases are more complicated. Do you know the distribution license for it?",
    "created_at": "2009-07-10T22:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52389",
    "user": "https://github.com/wdjoyner"
}
```

1. Thanks for fixing the installation docs and the detailed comparison. That was very valuable for me anyway.

2. The comparision between crime and your package is a bit more complicated that it first seems I think. For example, we have


```

sage: from pGroupCohomology import CohomologyRing
sage: H = CohomologyRing.user_db(8,3,websource=False)
sage: print H

Cohomology ring of Dihedral group of order 8 with coefficients in GF(2)

Computed up to degree 2
Minimal list of generators:
[c_2_2, a 2-Cochain in H^*(D8; GF(2)),
 b_1_0, a 1-Cochain in H^*(D8; GF(2)),
 b_1_1, a 1-Cochain in H^*(D8; GF(2))]
Minimal list of algebraic relations:
[b_1_0*b_1_1]

sage: gap('LoadPackage("crime")')            
true 
sage: gap.eval("C:=CohomologyObject(DihedralGroup(8))")
'<object>'
sage: gap.eval("CohomologyGenerators(C,2)")
'[ 1, 1, 2 ]'
sage: gap.eval("CohomologyRelators(C,2)")
'[ [ z, y, x ], [ z*y+y^2 ] ]'
```

These seem different but I am not an expert. Is this difference easy to explain?

3. Regarding the PoincareSeries in HAP: I think Graham Ellis told me that his PoincareSeries was likely to be true but not guaranteed. Is this right? If so, how sure are you of yours? (I checked in an example that they agree.)

4. Regarding the license: 

(a) Can you ask any surviving Meataxe people if they might relicensing the version you used under GPLv2+?

(b) Since David Green is a co-author - he can license the code as he wants:-)

(c) Did you create the database "Data for the cohomology of all groups of order 64" yourself? If not, in the US I think this is not an issue, but overseas copyright laws for databases are more complicated. Do you know the distribution license for it?



---

archive/issue_comments_052390.json:
```json
{
    "body": "Replying to [comment:12 wdj]:\n> 2. The comparision between crime and your package is a bit more complicated that it first seems I think. For example, we have\n...\n> Minimal list of algebraic relations:\n> [b_1_0*b_1_1]\n...\n> sage: gap.eval(\"CohomologyRelators(C,2)\") \n\n> `'[ [ z, y, x ], [ z*y+y^2 ] ]' ` \n\n> These seem different but I am not an expert. Is this difference easy to explain?\n\n\nThis problem is addressed in the package documentation in various places. \n\n__Explanation:__\n\nOf course, isomorphic rings can have different ring representations. In fact, when computing the cohomology with our package, the result depends on the given p-group *together with a choice of a minimal generating set*.\n\nHere is an example:\n\n\n```\nsage: from pGroupCohomology import CohomologyRing\nsage: tmp_root = tmp_filename()\nsage: CohomologyRing.set_user_db(tmp_root)\nsage: G1 = gap('DihedralGroup(8)')\nsage: G2 = gap('SmallGroup(8,3)')\nsage: H1 = CohomologyRing.user_db(G1, GroupName = 'Dihedral')\nsage: H1.make()\nsage: H2 = CohomologyRing.user_db(8,3)\nsage: H2.make()\nsage: H1.rels()\n['b_1_1^2+b_1_0*b_1_1']\nsage: H2.rels()\n['b_1_0*b_1_1']\n```\n\n\nHence, when we apply our algorithm to the dihedral group with generators given by DihedralGroup(8), we get a result as in CRIME. But using generators as provided by the SmallGroups library, the ring presentation is different.\n\nBy the method `group()`, one gets a permutation group that is guaranteed to yield the same presentation of the cohomology ring, and you see: These permutation groups are different, and mapping generators to generators would not provide an isomorphism of groups.\n\n```\nsage: H1.group()\nGroup( [ (1,5)(2,6)(3,8)(4,7), (1,3,2,4)(5,7,6,8) ] )\nsage: H2.group()\nGroup( [ (1,2)(3,8)(4,6)(5,7), (1,3)(2,5)(4,7)(6,8) ] )\n```\n\n\nHowever, the groups *are* isomorphic, so, we can construct an induced homomorphism of the cohomology rings:\n\n```\nsage: phi = G2.IsomorphismGroups(G1) # note that the resulting isomorphism is not unique\nsage: phi.SetName('\"phi\"')\nsage: phi_star = H1.hom(phi,H2)\nsage: phi_star\nphi^*\nsage: [H2.cochain_to_polynomial(phi_star(X)) for X in H1.gens()]\n\n[1, a 0-Cochain in H^*(D8; GF(2)),\n b_1_1^2+c_2_2, a 2-Cochain in H^*(D8; GF(2)),\n b_1_1+b_1_0, a 1-Cochain in H^*(D8; GF(2)),\n b_1_1, a 1-Cochain in H^*(D8; GF(2))]\n```\n\n\nSo, the induced homomorphism is not the identity. Just for fun, let us test whether the preimage of the relation of H2 is really zero in H1:\n\n\n```\nsage: print (phi_star^(-1))(H2('b_1_0')) * (phi_star^(-1))(H2('b_1_1'))\n2-Cochain in H^*(Dihedral; GF(2)),\nrepresented by\n[0 0 0]\n```\n\n \n> 3. Regarding the PoincareSeries in HAP: I think Graham Ellis told me that his PoincareSeries was likely to be true but not guaranteed. Is this right? If so, how sure are you of yours? (I checked in an example that they agree.)\n\nI don't know how reliable it is in HAP.\n\nConcerning reliability in our package: Note that there are two completely different methods for the computation of the Poincar\u00e9 series, namely `poincare_series()` and `poincare_without_parameters`. The second method uses a generic algorithm, but the first uses the parameters that are used in Benson's completeness criterion.\n\nSo, to test the reliability, you may compare the output of the two methods. \n\nNote that both methods do not rely on Hilbert function computations of Singular. The reason for an independent implementation was in fact that Singular is not reliable, it sometimes produces silent integer overflows.\n\n> 4. Regarding the license: \n> \n> (a) Can you ask any surviving Meataxe people if they might relicensing the version you used under GPLv2+?\n\nOnne may try. Perhaps the more recent versions are already GPLv2+. However, we need the old version, or we need to re-implement David Green's code.\n\n> (b) Since David Green is a co-author - he can license the code as he wants:-)\n\nWell, but it would be wise to use a licence that meets the requirements of Sage.\n\n> (c) Did you create the database \"Data for the cohomology of all groups of order 64\" yourself?\n\nWell, the computer helped me a little...\n\nThe data base is not a relational data base (yet!), hence, no SQLAlchemy involved. It is just the result of the computations of our package, applying \"tar -cz\" to the result. Essentially, it is a courtesy, since a computation from scratch would yield that data base in just about 50 minutes.\n\n> Do you know the distribution license for it? \n\nAs I did it myself, I can probably choose. But I don't know how! Can you explain?\n\nCheers,\n   Simon",
    "created_at": "2009-07-10T23:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52390",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:12 wdj]:
> 2. The comparision between crime and your package is a bit more complicated that it first seems I think. For example, we have
...
> Minimal list of algebraic relations:
> [b_1_0*b_1_1]
...
> sage: gap.eval("CohomologyRelators(C,2)") 

> `'[ [ z, y, x ], [ z*y+y^2 ] ]' ` 

> These seem different but I am not an expert. Is this difference easy to explain?


This problem is addressed in the package documentation in various places. 

__Explanation:__

Of course, isomorphic rings can have different ring representations. In fact, when computing the cohomology with our package, the result depends on the given p-group *together with a choice of a minimal generating set*.

Here is an example:


```
sage: from pGroupCohomology import CohomologyRing
sage: tmp_root = tmp_filename()
sage: CohomologyRing.set_user_db(tmp_root)
sage: G1 = gap('DihedralGroup(8)')
sage: G2 = gap('SmallGroup(8,3)')
sage: H1 = CohomologyRing.user_db(G1, GroupName = 'Dihedral')
sage: H1.make()
sage: H2 = CohomologyRing.user_db(8,3)
sage: H2.make()
sage: H1.rels()
['b_1_1^2+b_1_0*b_1_1']
sage: H2.rels()
['b_1_0*b_1_1']
```


Hence, when we apply our algorithm to the dihedral group with generators given by DihedralGroup(8), we get a result as in CRIME. But using generators as provided by the SmallGroups library, the ring presentation is different.

By the method `group()`, one gets a permutation group that is guaranteed to yield the same presentation of the cohomology ring, and you see: These permutation groups are different, and mapping generators to generators would not provide an isomorphism of groups.

```
sage: H1.group()
Group( [ (1,5)(2,6)(3,8)(4,7), (1,3,2,4)(5,7,6,8) ] )
sage: H2.group()
Group( [ (1,2)(3,8)(4,6)(5,7), (1,3)(2,5)(4,7)(6,8) ] )
```


However, the groups *are* isomorphic, so, we can construct an induced homomorphism of the cohomology rings:

```
sage: phi = G2.IsomorphismGroups(G1) # note that the resulting isomorphism is not unique
sage: phi.SetName('"phi"')
sage: phi_star = H1.hom(phi,H2)
sage: phi_star
phi^*
sage: [H2.cochain_to_polynomial(phi_star(X)) for X in H1.gens()]

[1, a 0-Cochain in H^*(D8; GF(2)),
 b_1_1^2+c_2_2, a 2-Cochain in H^*(D8; GF(2)),
 b_1_1+b_1_0, a 1-Cochain in H^*(D8; GF(2)),
 b_1_1, a 1-Cochain in H^*(D8; GF(2))]
```


So, the induced homomorphism is not the identity. Just for fun, let us test whether the preimage of the relation of H2 is really zero in H1:


```
sage: print (phi_star^(-1))(H2('b_1_0')) * (phi_star^(-1))(H2('b_1_1'))
2-Cochain in H^*(Dihedral; GF(2)),
represented by
[0 0 0]
```

 
> 3. Regarding the PoincareSeries in HAP: I think Graham Ellis told me that his PoincareSeries was likely to be true but not guaranteed. Is this right? If so, how sure are you of yours? (I checked in an example that they agree.)

I don't know how reliable it is in HAP.

Concerning reliability in our package: Note that there are two completely different methods for the computation of the Poincaré series, namely `poincare_series()` and `poincare_without_parameters`. The second method uses a generic algorithm, but the first uses the parameters that are used in Benson's completeness criterion.

So, to test the reliability, you may compare the output of the two methods. 

Note that both methods do not rely on Hilbert function computations of Singular. The reason for an independent implementation was in fact that Singular is not reliable, it sometimes produces silent integer overflows.

> 4. Regarding the license: 
> 
> (a) Can you ask any surviving Meataxe people if they might relicensing the version you used under GPLv2+?

Onne may try. Perhaps the more recent versions are already GPLv2+. However, we need the old version, or we need to re-implement David Green's code.

> (b) Since David Green is a co-author - he can license the code as he wants:-)

Well, but it would be wise to use a licence that meets the requirements of Sage.

> (c) Did you create the database "Data for the cohomology of all groups of order 64" yourself?

Well, the computer helped me a little...

The data base is not a relational data base (yet!), hence, no SQLAlchemy involved. It is just the result of the computations of our package, applying "tar -cz" to the result. Essentially, it is a courtesy, since a computation from scratch would yield that data base in just about 50 minutes.

> Do you know the distribution license for it? 

As I did it myself, I can probably choose. But I don't know how! Can you explain?

Cheers,
   Simon



---

archive/issue_comments_052391.json:
```json
{
    "body": "PS: Concerning reliability of Poincare series.\n\nIn some cases, other people provided a Poincare series. For example, David Green provides the Poincare series for the cohomology rings of the groups of order 64. His programs and our package share the computation of resolutions, but the computation of the ring structure is an independent implementation. However, the results coincide (I went through all 267 examples). \n\nAnd the Sylow 2-subgroup of the Higman-Sims group (order 512, see [http://users.minet.uni-jena.de/~king/cohomology/512web/Syl2HS.html](http://users.minet.uni-jena.de/~king/cohomology/512web/Syl2HS.html)) was already computed by Jon F. Carlson and coauthors. They of course obtain a different ring presentation, but: The number of generators and relations, sorted by degree, *and* the Poincar\u00e9 series coincide with our findings.\n\nSo, the cross checks seem to indicate that it is reliable.\n\nCheers,\n   Simon",
    "created_at": "2009-07-10T23:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52391",
    "user": "https://github.com/simon-king-jena"
}
```

PS: Concerning reliability of Poincare series.

In some cases, other people provided a Poincare series. For example, David Green provides the Poincare series for the cohomology rings of the groups of order 64. His programs and our package share the computation of resolutions, but the computation of the ring structure is an independent implementation. However, the results coincide (I went through all 267 examples). 

And the Sylow 2-subgroup of the Higman-Sims group (order 512, see [http://users.minet.uni-jena.de/~king/cohomology/512web/Syl2HS.html](http://users.minet.uni-jena.de/~king/cohomology/512web/Syl2HS.html)) was already computed by Jon F. Carlson and coauthors. They of course obtain a different ring presentation, but: The number of generators and relations, sorted by degree, *and* the Poincaré series coincide with our findings.

So, the cross checks seem to indicate that it is reliable.

Cheers,
   Simon



---

archive/issue_comments_052392.json:
```json
{
    "body": "Okay, thanks for the explanations. To me, everything looks fantastic with this package. Thanks again for contributing this to sage. It's really high quality stuff IMHO.\n\nThe only issue is the license. I think the meataxe license needs to be looked into. I think there are some former meataxe people at or near Aachen aren't there? I expect it would not be a problem to change it from GPLv2 to GPLv2+ but of course you need to ask.\n\nRegarding the license of the database, in the US, I think it is not copyrightable. (I am not a lawyer and this is only my opinion but see http://en.wikipedia.org/wiki/Feist_Publications_v._Rural_Telephone_Service if you are interested in details.) Because of this, I would recommend the creative commons CC0 license http://creativecommons.org/publicdomain/, which I think has the same effect under US and German law (which I think is completely different than US law in this instance since I think German databases are copyrightable). \nYou could also just choose the GFDL for it and not worry about the US law.",
    "created_at": "2009-07-11T00:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52392",
    "user": "https://github.com/wdjoyner"
}
```

Okay, thanks for the explanations. To me, everything looks fantastic with this package. Thanks again for contributing this to sage. It's really high quality stuff IMHO.

The only issue is the license. I think the meataxe license needs to be looked into. I think there are some former meataxe people at or near Aachen aren't there? I expect it would not be a problem to change it from GPLv2 to GPLv2+ but of course you need to ask.

Regarding the license of the database, in the US, I think it is not copyrightable. (I am not a lawyer and this is only my opinion but see http://en.wikipedia.org/wiki/Feist_Publications_v._Rural_Telephone_Service if you are interested in details.) Because of this, I would recommend the creative commons CC0 license http://creativecommons.org/publicdomain/, which I think has the same effect under US and German law (which I think is completely different than US law in this instance since I think German databases are copyrightable). 
You could also just choose the GFDL for it and not worry about the US law.



---

archive/issue_comments_052393.json:
```json
{
    "body": "Replying to [comment:15 wdj]:\n> The only issue is the license. I think the meataxe license needs to be looked into. I think there are some former meataxe people at or near Aachen aren't there? I expect it would not be a problem to change it from GPLv2 to GPLv2+ but of course you need to ask.\n\nIn the next few weeks I will be in a rather remote location, so it is unlikely that I will often be in the internet.\n\nCould perhaps David Green (who is Cc for this ticket) ask in Aachen?\n \n> Regarding the license of the database, in the US, I think it is not copyrightable. (I am not a lawyer and this is only my opinion but see http://en.wikipedia.org/wiki/Feist_Publications_v._Rural_Telephone_Service if you are interested in details.) Because of this, I would recommend the creative commons CC0 license http://creativecommons.org/publicdomain/, which I think has the same effect under US and German law (which I think is completely different than US law in this instance since I think German databases are copyrightable). \n> You could also just choose the GFDL for it and not worry about the US law.\n \nOK, but it still does not explain *how* I put the database under any licence.\n\nProbably these things can be sorted out after juli 22?\n\nCheers,\n    Simon",
    "created_at": "2009-07-11T03:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52393",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:15 wdj]:
> The only issue is the license. I think the meataxe license needs to be looked into. I think there are some former meataxe people at or near Aachen aren't there? I expect it would not be a problem to change it from GPLv2 to GPLv2+ but of course you need to ask.

In the next few weeks I will be in a rather remote location, so it is unlikely that I will often be in the internet.

Could perhaps David Green (who is Cc for this ticket) ask in Aachen?
 
> Regarding the license of the database, in the US, I think it is not copyrightable. (I am not a lawyer and this is only my opinion but see http://en.wikipedia.org/wiki/Feist_Publications_v._Rural_Telephone_Service if you are interested in details.) Because of this, I would recommend the creative commons CC0 license http://creativecommons.org/publicdomain/, which I think has the same effect under US and German law (which I think is completely different than US law in this instance since I think German databases are copyrightable). 
> You could also just choose the GFDL for it and not worry about the US law.
 
OK, but it still does not explain *how* I put the database under any licence.

Probably these things can be sorted out after juli 22?

Cheers,
    Simon



---

archive/issue_comments_052394.json:
```json
{
    "body": "Hi!\n\nBefore I go to the remote place, I can use the internet for a couple of hours.\n\nI am kind of reluctant to accept the positive review, yet. Perhaps it should be \"positive review pending\"?\n\nWe have the following issues.\n\n__Licence__\n\n- As much as I understood, the MeatAxe Licence should be fixed. **Must** or **should**?\n- You said that I should put my data base tar file under a certain licence. I assume this hods both for the stuff included with the package (groups of order 64) and in the internet (groups of order 128 and 243). But HOW can I put them under a licence?\n\n__Porting__\n\nGood news is that it works with Ubuntu. But did anybody try with OS X or on Motorola processors?\n\n__Tests__\n\nDid you run the test suite?\n\n__More Features__\n\nThank you for pointing me to CRIME! It has implemented the Massey products. I think I would just need a day to implement it as well. But due to the expected shortcomings with internet in the near future, it might be a longer way.\n\nSo, what should I do when I have new features? Open a new ticket, with a version 1.1 of the spkg? Or (as long as the package did not become optional yet) stay on *this* ticket?\n\nBest regards,\n   Simon",
    "created_at": "2009-07-12T08:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52394",
    "user": "https://github.com/simon-king-jena"
}
```

Hi!

Before I go to the remote place, I can use the internet for a couple of hours.

I am kind of reluctant to accept the positive review, yet. Perhaps it should be "positive review pending"?

We have the following issues.

__Licence__

- As much as I understood, the MeatAxe Licence should be fixed. **Must** or **should**?
- You said that I should put my data base tar file under a certain licence. I assume this hods both for the stuff included with the package (groups of order 64) and in the internet (groups of order 128 and 243). But HOW can I put them under a licence?

__Porting__

Good news is that it works with Ubuntu. But did anybody try with OS X or on Motorola processors?

__Tests__

Did you run the test suite?

__More Features__

Thank you for pointing me to CRIME! It has implemented the Massey products. I think I would just need a day to implement it as well. But due to the expected shortcomings with internet in the near future, it might be a longer way.

So, what should I do when I have new features? Open a new ticket, with a version 1.1 of the spkg? Or (as long as the package did not become optional yet) stay on *this* ticket?

Best regards,
   Simon



---

archive/issue_comments_052395.json:
```json
{
    "body": "Replying to [comment:17 SimonKing]:\n> Hi!\n> \n> Before I go to the remote place, I can use the internet for a couple of hours.\n> \n> I am kind of reluctant to accept the positive review, yet. Perhaps it should be \"positive review pending\"?\n\n\nThat is fine but I don't see how any of the issues you raise below are important for the inclusion as an *optional* spkg, which is what this ticket is about.\n\n\n> \n> We have the following issues.\n> \n> __Licence__\n> \n>  - As much as I understood, the MeatAxe Licence should be fixed. **Must** or **should**?\n\n\nSince Meataxe is GPLv2 and you compile against it, your package is GPLv2. I assume you are releasing your *code* under GPLv2+, but the package itself inherits what Meataxe is. So, **must** is only if you want your optional package to by GPLv2+. There are all kinds of licenses in the optional spkg's though.\n\n\n>  - You said that I should put my data base tar file under a certain licence. I assume this hods both for the stuff included with the package (groups of order 64) and in the internet (groups of order 128 and 243). But HOW can I put them under a licence?\n> \n\n\nWhy not ad a COPYING or license.txt or README file to \nSAGE_ROOT/local/pGroupCohomology, asssuming that is where the \nDBs are? That's the obvious thing. \n\nBTW, if you type\n\n\n```\nType:           instance\nBase Class:     pGroupCohomology.CohomologyRingFactory\nString Form:    <pGroupCohomology.CohomologyRingFactory instance at 0x58075a8>\nNamespace:      Interactive\nFile:           /home/wdj/sagefiles/sage-4.1.rc1/local/lib/python2.6/site-packages/pGroupCohomology/__init__.py\nDocstring:\n\n    Constructor for modular cohomology rings of finite p-groups\n\n<snip>\n```\n\nAre you happy with that File descriptor? \n\n\n\n> __Porting__\n> \n> Good news is that it works with Ubuntu. But did anybody try with OS X or on Motorola processors?\n\n\nI thought I mentioned that I also tried this on an intel macbook running 10.4.11.\nSorry, I thought I did. Install went fine on an intel macbook.\n\n> \n> __Tests__\n> \n> Did you run the test suite?\n\nDo you mean\nsage: !/home/wdj/sagefiles/p_group_cohomology-1.0/spkg-check ?\n\nIn general, I have very little idea where in the SAGE tree different parts of the spkg get loaded.\nIn one of your earlier comments you mentioned this script but with no indication of where to find it. I had to separately tar xjvf the spkg and run that script since I couldn't find it in any \"obvious\" places in the Sage tree.\n\nI got \n\n\n```\n...\nWriting doc strings to '/home/wdj/.sage//temp/hera/7169/RecDoctest.py' and running 'sage -t -long -verbose'...\nAll tests passed!\nSUMMARY\n-------\nSome doc tests failed or where missing.\nPlease check '*_test.log', with * in ['cohomology']\nTotal time: 9.30 min\n```\n\nThis gives no idea where `cohomology_test.log` is located but I found it. See\nhttp://sage.math.washington.edu/home/wdj/patches/cohomology_test-amd64-ubuntu904.log\nfor the ubuntu test log and \nhttp://sage.math.washington.edu/home/wdj/patches/cohomology_test-mac0s10.4.11.log\nfor the intel macbook test log. In the ubuntu test log example_51 and example_7\nhad failures. I didn't understand the error but it seems to be a problem with Singular.\nThe macbook behaved better (only example_51 was listed as failing) but again the\nproblem was with Singular.\n\n\n> \n> __More Features__\n> \n> Thank you for pointing me to CRIME! It has implemented the Massey products. I think I would just need a day to implement it as well. But due to the expected shortcomings with internet in the near future, it might be a longer way.\n> \n> So, what should I do when I have new features? Open a new ticket, with a version 1.1 of the spkg? Or (as long as the package did not become optional yet) stay on *this* ticket?\n> \n\n\nWhen version 1.1 is ready, open up a new ticket, describe the changes and post the new spkg. With new features, I guess you should have new doctests?\n\n\nIn any case, I think for an optional package, this is fine. If you want to call it \"pending\" and make more changes then that is fine too.\n\n\n> Best regards,\n>    Simon",
    "created_at": "2009-07-12T12:56:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52395",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:17 SimonKing]:
> Hi!
> 
> Before I go to the remote place, I can use the internet for a couple of hours.
> 
> I am kind of reluctant to accept the positive review, yet. Perhaps it should be "positive review pending"?


That is fine but I don't see how any of the issues you raise below are important for the inclusion as an *optional* spkg, which is what this ticket is about.


> 
> We have the following issues.
> 
> __Licence__
> 
>  - As much as I understood, the MeatAxe Licence should be fixed. **Must** or **should**?


Since Meataxe is GPLv2 and you compile against it, your package is GPLv2. I assume you are releasing your *code* under GPLv2+, but the package itself inherits what Meataxe is. So, **must** is only if you want your optional package to by GPLv2+. There are all kinds of licenses in the optional spkg's though.


>  - You said that I should put my data base tar file under a certain licence. I assume this hods both for the stuff included with the package (groups of order 64) and in the internet (groups of order 128 and 243). But HOW can I put them under a licence?
> 


Why not ad a COPYING or license.txt or README file to 
SAGE_ROOT/local/pGroupCohomology, asssuming that is where the 
DBs are? That's the obvious thing. 

BTW, if you type


```
Type:           instance
Base Class:     pGroupCohomology.CohomologyRingFactory
String Form:    <pGroupCohomology.CohomologyRingFactory instance at 0x58075a8>
Namespace:      Interactive
File:           /home/wdj/sagefiles/sage-4.1.rc1/local/lib/python2.6/site-packages/pGroupCohomology/__init__.py
Docstring:

    Constructor for modular cohomology rings of finite p-groups

<snip>
```

Are you happy with that File descriptor? 



> __Porting__
> 
> Good news is that it works with Ubuntu. But did anybody try with OS X or on Motorola processors?


I thought I mentioned that I also tried this on an intel macbook running 10.4.11.
Sorry, I thought I did. Install went fine on an intel macbook.

> 
> __Tests__
> 
> Did you run the test suite?

Do you mean
sage: !/home/wdj/sagefiles/p_group_cohomology-1.0/spkg-check ?

In general, I have very little idea where in the SAGE tree different parts of the spkg get loaded.
In one of your earlier comments you mentioned this script but with no indication of where to find it. I had to separately tar xjvf the spkg and run that script since I couldn't find it in any "obvious" places in the Sage tree.

I got 


```
...
Writing doc strings to '/home/wdj/.sage//temp/hera/7169/RecDoctest.py' and running 'sage -t -long -verbose'...
All tests passed!
SUMMARY
-------
Some doc tests failed or where missing.
Please check '*_test.log', with * in ['cohomology']
Total time: 9.30 min
```

This gives no idea where `cohomology_test.log` is located but I found it. See
http://sage.math.washington.edu/home/wdj/patches/cohomology_test-amd64-ubuntu904.log
for the ubuntu test log and 
http://sage.math.washington.edu/home/wdj/patches/cohomology_test-mac0s10.4.11.log
for the intel macbook test log. In the ubuntu test log example_51 and example_7
had failures. I didn't understand the error but it seems to be a problem with Singular.
The macbook behaved better (only example_51 was listed as failing) but again the
problem was with Singular.


> 
> __More Features__
> 
> Thank you for pointing me to CRIME! It has implemented the Massey products. I think I would just need a day to implement it as well. But due to the expected shortcomings with internet in the near future, it might be a longer way.
> 
> So, what should I do when I have new features? Open a new ticket, with a version 1.1 of the spkg? Or (as long as the package did not become optional yet) stay on *this* ticket?
> 


When version 1.1 is ready, open up a new ticket, describe the changes and post the new spkg. With new features, I guess you should have new doctests?


In any case, I think for an optional package, this is fine. If you want to call it "pending" and make more changes then that is fine too.


> Best regards,
>    Simon



---

archive/issue_comments_052396.json:
```json
{
    "body": "Replying to [comment:18 wdj]:\n\n...\n\n> \n> \n> Since Meataxe is GPLv2 and you compile against it, your package is GPLv2. I assume you are releasing your *code* under GPLv2+, but the package itself inherits what Meataxe is. So, **must** is only if you want your optional package to by GPLv2+. There are all kinds of licenses in the optional spkg's though.\n> \n\n\nI should also say that your SPKG.txt file has merely the generic blurb\n\n\n```\n## License\n\nCopyright (C) 2009 Simon A. King  <simon.king@uni-jena.de> and\n                   David J. Green <david.green@uni-jena.de>\n\nDistributed under the terms of the GNU General Public License (GPL)\n\n   This code is distributed in the hope that it will be useful,\n   but WITHOUT ANY WARRANTY; without even the implied warranty of\n   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU\n   General Public License for more details.\n\nThe full text of the GPL is available at:\n\n                http://www.gnu.org/licenses/\n```\n\n\nHowever, if memory serves, the FSF says that if you do not specify the version of the \nGPL then it is *assumed* to be the latest version (which is at this date GPLv3). \nThis is not what you want, of course. \n\n\n\n> \n> >  - You said that I should put my data base tar file under a certain licence. I assume this hods both for the stuff included with the package (groups of order 64) and in the internet (groups of order 128 and 243). But HOW can I put them under a licence?\n> > \n> \n> \n> Why not ad a COPYING or license.txt or README file to \n> SAGE_ROOT/local/pGroupCohomology, asssuming that is where the \n> DBs are? That's the obvious thing. \n\n\nFor the internet files, you could have a COPYING file in the same directory on the server.",
    "created_at": "2009-07-12T13:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52396",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:18 wdj]:

...

> 
> 
> Since Meataxe is GPLv2 and you compile against it, your package is GPLv2. I assume you are releasing your *code* under GPLv2+, but the package itself inherits what Meataxe is. So, **must** is only if you want your optional package to by GPLv2+. There are all kinds of licenses in the optional spkg's though.
> 


I should also say that your SPKG.txt file has merely the generic blurb


```
## License

Copyright (C) 2009 Simon A. King  <simon.king@uni-jena.de> and
                   David J. Green <david.green@uni-jena.de>

Distributed under the terms of the GNU General Public License (GPL)

   This code is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   General Public License for more details.

The full text of the GPL is available at:

                http://www.gnu.org/licenses/
```


However, if memory serves, the FSF says that if you do not specify the version of the 
GPL then it is *assumed* to be the latest version (which is at this date GPLv3). 
This is not what you want, of course. 



> 
> >  - You said that I should put my data base tar file under a certain licence. I assume this hods both for the stuff included with the package (groups of order 64) and in the internet (groups of order 128 and 243). But HOW can I put them under a licence?
> > 
> 
> 
> Why not ad a COPYING or license.txt or README file to 
> SAGE_ROOT/local/pGroupCohomology, asssuming that is where the 
> DBs are? That's the obvious thing. 


For the internet files, you could have a COPYING file in the same directory on the server.



---

archive/issue_comments_052397.json:
```json
{
    "body": "Replying to [comment:18 wdj]:\n> That is fine but I don't see how any of the issues you raise below are important for the inclusion as an *optional* spkg, which is what this ticket is about.\n\nOK. I thought that this is the distinction between *optional* and *experimental*, the latter being not completely portable and also not completely reliable due to doc test errors.\n\n> Since Meataxe is GPLv2 and you compile against it, your package is GPLv2. I assume you are releasing your *code* under GPLv2+, but the package itself inherits what Meataxe is. So, **must** is only if you want your optional package to by GPLv2+. There are all kinds of licenses in the optional spkg's though.\n\nOK. But then it is conflict with my SPKG.txt, isn't it?\n\n> BTW, if you type\n> \n> {{{\n> Type:           instance\n> Base Class:     pGroupCohomology.CohomologyRingFactory\n> String Form:    <pGroupCohomology.CohomologyRingFactory instance at 0x58075a8>\n> Namespace:      Interactive\n> File:           /home/wdj/sagefiles/sage-4.1.rc1/local/lib/python2.6/site-packages/pGroupCohomology/__init__.py\n> Docstring\n> \n>     Constructor for modular cohomology rings of finite p-groups\n> \n> <snip>\n> }}}\n> Are you happy with that File descriptor? \n\nWhat's wrong with it? In fact, this stuff is defined in ``__init__.py``. The reason is as follows:\n- The user is supposed to construct things with the ring constructor.\n- Hence, it should be easy to import.\n- Hence, it should be on top level: `from pGroupCohomology import CohomologyRing` should be better than `from pGroupCohomology.cohomology import CohomologyRing`\n\n> > __Porting__\n> > \n> > Good news is that it works with Ubuntu. But did anybody try with OS X or on Motorola processors?\n> \n> \n> I thought I mentioned that I also tried this on an intel macbook running 10.4.11.\n> Sorry, I thought I did. Install went fine on an intel macbook.\n\nVery cool!! As I mentioned, a few months ago (Sage Days San Diego) it didn't build at all on a Macbook!\n\n> > __Tests__\n> > \n> > Did you run the test suite?\n> \n> Do you mean\n> sage: !/home/wdj/sagefiles/p_group_cohomology-1.0/spkg-check ?\n\nYes, and this is the usual place for a test suite, or at least this is what I got from the developers guide.\n\n> This gives no idea where `cohomology_test.log` is located but I found it. \n\nSorry. Assuming that the location of the script was clear, when running it, it writes the log simply in the current work directory.\n\n> for the intel macbook test log. In the ubuntu test log example_51 and example_7\n> had failures. I didn't understand the error but it seems to be a problem with Singular.\n> The macbook behaved better (only example_51 was listed as failing) but again the\n> problem was with Singular.\n\nSome of them are. I don't know what happens, yet. I mean, ``def sage10456=COHO6r(1);`` resulting in an error in Singular. These things sometimes go away if the tests are performed in a different order. So, It really seems to me that they are due to Singular and not to the package. I suspect that the number of variable names in Singular is restricted. And 10456 is quite a lot. In fact, while developing the package, I tried to keep the number of autogenerated variable names small, but it doesn't help if you run hundreds of doc tests without restarting singular.\n\nBut something in the Ubuntu log irritates me: There is one example where a wrong ring structure is found. \nCurrently I have no time to analyse it further. \n\nBy the way, there also is a test suite spkg-check-details, that does the doc tests in a different way.\n\n> > __More Features__\n> > ...\n> > \n> > So, what should I do when I have new features? Open a new ticket, with a version 1.1 of the spkg? Or (as long as the package did not become optional yet) stay on *this* ticket?\n> > \n> \n> \n> When version 1.1 is ready, open up a new ticket, describe the changes and post the new spkg. With new features, I guess you should have new doctests?\n\nWell, I would have an additional doctest for *this* new feature, the rest would be the same.\n\n> In any case, I think for an optional package, this is fine. If you want to call it \"pending\" and make more changes then that is fine too.\n\nWell, I think the Massey product should go in, and I definitely want to see what happens with the doc tests.\n\nSo, I think it would hurt to keep it pending until my return end of July. Or are there different opinions?\n\nCheers,\n   Simon",
    "created_at": "2009-07-12T14:56:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52397",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:18 wdj]:
> That is fine but I don't see how any of the issues you raise below are important for the inclusion as an *optional* spkg, which is what this ticket is about.

OK. I thought that this is the distinction between *optional* and *experimental*, the latter being not completely portable and also not completely reliable due to doc test errors.

> Since Meataxe is GPLv2 and you compile against it, your package is GPLv2. I assume you are releasing your *code* under GPLv2+, but the package itself inherits what Meataxe is. So, **must** is only if you want your optional package to by GPLv2+. There are all kinds of licenses in the optional spkg's though.

OK. But then it is conflict with my SPKG.txt, isn't it?

> BTW, if you type
> 
> {{{
> Type:           instance
> Base Class:     pGroupCohomology.CohomologyRingFactory
> String Form:    <pGroupCohomology.CohomologyRingFactory instance at 0x58075a8>
> Namespace:      Interactive
> File:           /home/wdj/sagefiles/sage-4.1.rc1/local/lib/python2.6/site-packages/pGroupCohomology/__init__.py
> Docstring
> 
>     Constructor for modular cohomology rings of finite p-groups
> 
> <snip>
> }}}
> Are you happy with that File descriptor? 

What's wrong with it? In fact, this stuff is defined in ``__init__.py``. The reason is as follows:
- The user is supposed to construct things with the ring constructor.
- Hence, it should be easy to import.
- Hence, it should be on top level: `from pGroupCohomology import CohomologyRing` should be better than `from pGroupCohomology.cohomology import CohomologyRing`

> > __Porting__
> > 
> > Good news is that it works with Ubuntu. But did anybody try with OS X or on Motorola processors?
> 
> 
> I thought I mentioned that I also tried this on an intel macbook running 10.4.11.
> Sorry, I thought I did. Install went fine on an intel macbook.

Very cool!! As I mentioned, a few months ago (Sage Days San Diego) it didn't build at all on a Macbook!

> > __Tests__
> > 
> > Did you run the test suite?
> 
> Do you mean
> sage: !/home/wdj/sagefiles/p_group_cohomology-1.0/spkg-check ?

Yes, and this is the usual place for a test suite, or at least this is what I got from the developers guide.

> This gives no idea where `cohomology_test.log` is located but I found it. 

Sorry. Assuming that the location of the script was clear, when running it, it writes the log simply in the current work directory.

> for the intel macbook test log. In the ubuntu test log example_51 and example_7
> had failures. I didn't understand the error but it seems to be a problem with Singular.
> The macbook behaved better (only example_51 was listed as failing) but again the
> problem was with Singular.

Some of them are. I don't know what happens, yet. I mean, ``def sage10456=COHO6r(1);`` resulting in an error in Singular. These things sometimes go away if the tests are performed in a different order. So, It really seems to me that they are due to Singular and not to the package. I suspect that the number of variable names in Singular is restricted. And 10456 is quite a lot. In fact, while developing the package, I tried to keep the number of autogenerated variable names small, but it doesn't help if you run hundreds of doc tests without restarting singular.

But something in the Ubuntu log irritates me: There is one example where a wrong ring structure is found. 
Currently I have no time to analyse it further. 

By the way, there also is a test suite spkg-check-details, that does the doc tests in a different way.

> > __More Features__
> > ...
> > 
> > So, what should I do when I have new features? Open a new ticket, with a version 1.1 of the spkg? Or (as long as the package did not become optional yet) stay on *this* ticket?
> > 
> 
> 
> When version 1.1 is ready, open up a new ticket, describe the changes and post the new spkg. With new features, I guess you should have new doctests?

Well, I would have an additional doctest for *this* new feature, the rest would be the same.

> In any case, I think for an optional package, this is fine. If you want to call it "pending" and make more changes then that is fine too.

Well, I think the Massey product should go in, and I definitely want to see what happens with the doc tests.

So, I think it would hurt to keep it pending until my return end of July. Or are there different opinions?

Cheers,
   Simon



---

archive/issue_comments_052398.json:
```json
{
    "body": "Replying to [comment:20 SimonKing]:\n...\n> So, I think it would hurt to keep it pending until my return end of July. Or are there different opinions?\n\nOoops, I meant to write \"it would *not* hurt\".",
    "created_at": "2009-07-12T15:45:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52398",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:20 SimonKing]:
...
> So, I think it would hurt to keep it pending until my return end of July. Or are there different opinions?

Ooops, I meant to write "it would *not* hurt".



---

archive/issue_comments_052399.json:
```json
{
    "body": "Replying to [comment:20 SimonKing]:\n> Replying to [comment:18 wdj]:\n\n...\n\n> \n> > Since Meataxe is GPLv2 and you compile against it, your package is GPLv2. I assume you are releasing your *code* under GPLv2+, but the package itself inherits what Meataxe is. So, **must** is only if you want your optional package to by GPLv2+. There are all kinds of licenses in the optional spkg's though.\n> \n> OK. But then it is conflict with my SPKG.txt, isn't it?\n\n\nYes, the license of your package is still an issue. You can either (a) rewrite SPKG.txt to say it is GPLv2, or (b) ask any surviving Meataxe people you can find (maybe Alexander Hulpke or Thomas Breuer or other GAP people know who to contact?) if they will relicense or dual-licence it as GPLv2+ (at least the part of it that you use), then revise SPKG.txt after that.\n\nIt would be helpful to have a README or something which explains where what parts of your package go in what part of the Sage tree and what license they have.\n\n\n> \n> > BTW, if you type\n> > \n> > {{{\n> > Type:           instance\n> > Base Class:     pGroupCohomology.CohomologyRingFactory\n> > String Form:    <pGroupCohomology.CohomologyRingFactory instance at 0x58075a8>\n> > Namespace:      Interactive\n> > File:           /home/wdj/sagefiles/sage-4.1.rc1/local/lib/python2.6/site-packages/pGroupCohomology/__init__.py\n> > Docstring\n> > \n> >     Constructor for modular cohomology rings of finite p-groups\n> > \n> > <snip>\n> > }}}\n> > Are you happy with that File descriptor? \n> \n> What's wrong with it? \n\n\nWell, I'm used to seeing __init__.py as a file which users don't read which imports stuff from other modules that readers do read (__mymodule__.py is more private than mymodule.py). Also, it's not very descriptive. Still, it's up to you.\n\n\n> \n> > > __Tests__\n> > > \n> > > Did you run the test suite?\n> > \n\n...\n\n\n> \n> But something in the Ubuntu log irritates me: There is one example where a wrong ring structure is found. \n> Currently I have no time to analyse it further. \n> \n> By the way, there also is a test suite spkg-check-details, that does the doc tests in a different way.\n\n\nI posted the shell history to \nhttp://sage.math.washington.edu/home/wdj/patches/cohomology-test-details.log \nIf I read it correctly, all tests passed.\n\n\n> \n> > > __More Features__\n> > > \n\n\n...\n\n\n> \n> So, I think it would not hurt to keep it pending until my return end of July. \n> Or are there different opinions?\n\n\nNo problem. The end of July is fine.\n\n\n> \n> Cheers,\n>    Simon",
    "created_at": "2009-07-12T17:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52399",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:20 SimonKing]:
> Replying to [comment:18 wdj]:

...

> 
> > Since Meataxe is GPLv2 and you compile against it, your package is GPLv2. I assume you are releasing your *code* under GPLv2+, but the package itself inherits what Meataxe is. So, **must** is only if you want your optional package to by GPLv2+. There are all kinds of licenses in the optional spkg's though.
> 
> OK. But then it is conflict with my SPKG.txt, isn't it?


Yes, the license of your package is still an issue. You can either (a) rewrite SPKG.txt to say it is GPLv2, or (b) ask any surviving Meataxe people you can find (maybe Alexander Hulpke or Thomas Breuer or other GAP people know who to contact?) if they will relicense or dual-licence it as GPLv2+ (at least the part of it that you use), then revise SPKG.txt after that.

It would be helpful to have a README or something which explains where what parts of your package go in what part of the Sage tree and what license they have.


> 
> > BTW, if you type
> > 
> > {{{
> > Type:           instance
> > Base Class:     pGroupCohomology.CohomologyRingFactory
> > String Form:    <pGroupCohomology.CohomologyRingFactory instance at 0x58075a8>
> > Namespace:      Interactive
> > File:           /home/wdj/sagefiles/sage-4.1.rc1/local/lib/python2.6/site-packages/pGroupCohomology/__init__.py
> > Docstring
> > 
> >     Constructor for modular cohomology rings of finite p-groups
> > 
> > <snip>
> > }}}
> > Are you happy with that File descriptor? 
> 
> What's wrong with it? 


Well, I'm used to seeing __init__.py as a file which users don't read which imports stuff from other modules that readers do read (__mymodule__.py is more private than mymodule.py). Also, it's not very descriptive. Still, it's up to you.


> 
> > > __Tests__
> > > 
> > > Did you run the test suite?
> > 

...


> 
> But something in the Ubuntu log irritates me: There is one example where a wrong ring structure is found. 
> Currently I have no time to analyse it further. 
> 
> By the way, there also is a test suite spkg-check-details, that does the doc tests in a different way.


I posted the shell history to 
http://sage.math.washington.edu/home/wdj/patches/cohomology-test-details.log 
If I read it correctly, all tests passed.


> 
> > > __More Features__
> > > 


...


> 
> So, I think it would not hurt to keep it pending until my return end of July. 
> Or are there different opinions?


No problem. The end of July is fine.


> 
> Cheers,
>    Simon



---

archive/issue_comments_052400.json:
```json
{
    "body": "Hi!\n\nIt turned out that there is some internet access here, so, to some extent I can work.\n\nReplying to [comment:22 wdj]:\n...\n> Yes, the license of your package is still an issue. You can either (a) rewrite SPKG.txt to say it is GPLv2, or (b) ask any surviving Meataxe people you can find (maybe Alexander Hulpke or Thomas Breuer or other GAP people know who to contact?) if they will relicense or dual-licence it as GPLv2+ (at least the part of it that you use), then revise SPKG.txt after that.\n\n\nDavid Green took care of it and asked in Aachen.\n\n\n> It would be helpful to have a README or something which explains where what parts of your package go in what part of the Sage tree and what license they have.\n\nI  think nothing goes to the Sage tree, where I understand that \"Sage tree\" is everything inside SAGE_ROOT/devel/sage/\n\nBut a README might indeed be helpful.\n\n> Well, I'm used to seeing __init__.py as a file which users don't read which imports stuff from other modules that readers do read (__mymodule__.py is more private than mymodule.py). Also, it's not very descriptive. Still, it's up to you.\n\nI see. You are right, I should put the code for CohomologyRing into a different file (say, cohomology_constructor.py), so that __init__.py only contains the import statement \"from pGroupCohomology.cohomology_constructor import CohomologyRing\". In that way, it is still possible for the user to do \"from pGroupCohomology import CohomologyRing\". OK, I will do so.\n\n> > But something in the Ubuntu log irritates me: There is one example where a wrong ring structure is found. \n> > Currently I have no time to analyse it further. \n> > \n> > By the way, there also is a test suite spkg-check-details, that does the doc tests in a different way.\n> \n> \n> I posted the shell history to \n> http://sage.math.washington.edu/home/wdj/patches/cohomology-test-details.log \n> If I read it correctly, all tests passed.\n\nGood! Was it on Ubuntu? \n\nspkg-check-details does the same tests as spkg-check, but it does them one after the other. In particular, sage, singular and gap are re-started for each test. That might explain why the Singular error disappeared.\n\nBut I see that the last line says \"some items have no doc test\". I just realise that spkg-check-details should tell the user that (if there are errors or missing doc tests) the script produces a file \"test.log\" in the current directory that gives details for all doc test errors and that gives a list of all items without doc tests. Could you please post the test.log?\n\nThings to do for me: \n- Replace spkg-check by spkg-check-details, since it avoids some trouble with Singular.\n- There should be a pointer to test.log.\n\n> > So, I think it would not hurt to keep it pending until my return end of July. \n> > Or are there different opinions?\n> \n> No problem. The end of July is fine.\n\nAnd then probably also including the Massey products!\n\nCheers, \n    Simon",
    "created_at": "2009-07-13T20:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52400",
    "user": "https://github.com/simon-king-jena"
}
```

Hi!

It turned out that there is some internet access here, so, to some extent I can work.

Replying to [comment:22 wdj]:
...
> Yes, the license of your package is still an issue. You can either (a) rewrite SPKG.txt to say it is GPLv2, or (b) ask any surviving Meataxe people you can find (maybe Alexander Hulpke or Thomas Breuer or other GAP people know who to contact?) if they will relicense or dual-licence it as GPLv2+ (at least the part of it that you use), then revise SPKG.txt after that.


David Green took care of it and asked in Aachen.


> It would be helpful to have a README or something which explains where what parts of your package go in what part of the Sage tree and what license they have.

I  think nothing goes to the Sage tree, where I understand that "Sage tree" is everything inside SAGE_ROOT/devel/sage/

But a README might indeed be helpful.

> Well, I'm used to seeing __init__.py as a file which users don't read which imports stuff from other modules that readers do read (__mymodule__.py is more private than mymodule.py). Also, it's not very descriptive. Still, it's up to you.

I see. You are right, I should put the code for CohomologyRing into a different file (say, cohomology_constructor.py), so that __init__.py only contains the import statement "from pGroupCohomology.cohomology_constructor import CohomologyRing". In that way, it is still possible for the user to do "from pGroupCohomology import CohomologyRing". OK, I will do so.

> > But something in the Ubuntu log irritates me: There is one example where a wrong ring structure is found. 
> > Currently I have no time to analyse it further. 
> > 
> > By the way, there also is a test suite spkg-check-details, that does the doc tests in a different way.
> 
> 
> I posted the shell history to 
> http://sage.math.washington.edu/home/wdj/patches/cohomology-test-details.log 
> If I read it correctly, all tests passed.

Good! Was it on Ubuntu? 

spkg-check-details does the same tests as spkg-check, but it does them one after the other. In particular, sage, singular and gap are re-started for each test. That might explain why the Singular error disappeared.

But I see that the last line says "some items have no doc test". I just realise that spkg-check-details should tell the user that (if there are errors or missing doc tests) the script produces a file "test.log" in the current directory that gives details for all doc test errors and that gives a list of all items without doc tests. Could you please post the test.log?

Things to do for me: 
- Replace spkg-check by spkg-check-details, since it avoids some trouble with Singular.
- There should be a pointer to test.log.

> > So, I think it would not hurt to keep it pending until my return end of July. 
> > Or are there different opinions?
> 
> No problem. The end of July is fine.

And then probably also including the Massey products!

Cheers, 
    Simon



---

archive/issue_comments_052401.json:
```json
{
    "body": "Replying to [comment:23 SimonKing]:\n> Hi!\n> \n> It turned out that there is some internet access here, so, to some extent I can work.\n> \n> Replying to [comment:22 wdj]:\n> ...\n\n> \n> \n> \n> \n> > I posted the shell history to \n> > http://sage.math.washington.edu/home/wdj/patches/cohomology-test-details.log \n> > If I read it correctly, all tests passed.\n> \n> Good! Was it on Ubuntu? \n\n\nYes.\n\n\n> \n> spkg-check-details does the same tests as spkg-check, but it does them one after the other. In particular, sage, singular and gap are re-started for each test. That might explain why the Singular error disappeared.\n> \n> But I see that the last line says \"some items have no doc test\". I just realise that spkg-check-details should tell the user that (if there are errors or missing doc tests) the script produces a file \"test.log\" in the current directory that gives details for all doc test errors and that gives a list of all items without doc tests. Could you please post the test.log?\n> \n\n\nDone (adain, on an amd64 ubuntu 9.04 machine):\nhttp://sage.math.washington.edu/home/wdj/patches/test.log\n\n> \n\n...\n\n> Cheers, \n>     Simon",
    "created_at": "2009-07-13T21:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52401",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:23 SimonKing]:
> Hi!
> 
> It turned out that there is some internet access here, so, to some extent I can work.
> 
> Replying to [comment:22 wdj]:
> ...

> 
> 
> 
> 
> > I posted the shell history to 
> > http://sage.math.washington.edu/home/wdj/patches/cohomology-test-details.log 
> > If I read it correctly, all tests passed.
> 
> Good! Was it on Ubuntu? 


Yes.


> 
> spkg-check-details does the same tests as spkg-check, but it does them one after the other. In particular, sage, singular and gap are re-started for each test. That might explain why the Singular error disappeared.
> 
> But I see that the last line says "some items have no doc test". I just realise that spkg-check-details should tell the user that (if there are errors or missing doc tests) the script produces a file "test.log" in the current directory that gives details for all doc test errors and that gives a list of all items without doc tests. Could you please post the test.log?
> 


Done (adain, on an amd64 ubuntu 9.04 machine):
http://sage.math.washington.edu/home/wdj/patches/test.log

> 

...

> Cheers, 
>     Simon



---

archive/issue_comments_052402.json:
```json
{
    "body": "Replying to [comment:24 wdj]:\n> > Good! Was it on Ubuntu? \n> \n> Yes.\n\nOK. Then the doc tests errors (including the very disturbing one, where the ring structure was wrong) seems to be due to Singular being overworked.\n\n> Done (adain, on an amd64 ubuntu 9.04 machine):\n> http://sage.math.washington.edu/home/wdj/patches/test.log\n\nOK. So, the doc tests passed, and the missing doc tests mainly concern some inherited methods. \nThe only \"new\" method without doc test is CohomologyHomset._repr_, which I will fix. The other missing doc tests concern classes, and I  understood that the *methods* suffice for having 100% doc test coverage.\n\nBest regards,\n   Simon",
    "created_at": "2009-07-13T22:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52402",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:24 wdj]:
> > Good! Was it on Ubuntu? 
> 
> Yes.

OK. Then the doc tests errors (including the very disturbing one, where the ring structure was wrong) seems to be due to Singular being overworked.

> Done (adain, on an amd64 ubuntu 9.04 machine):
> http://sage.math.washington.edu/home/wdj/patches/test.log

OK. So, the doc tests passed, and the missing doc tests mainly concern some inherited methods. 
The only "new" method without doc test is CohomologyHomset._repr_, which I will fix. The other missing doc tests concern classes, and I  understood that the *methods* suffice for having 100% doc test coverage.

Best regards,
   Simon



---

archive/issue_comments_052403.json:
```json
{
    "body": "There's news about licences:\n\nMichael Ringe kindly agreed to provide mtx-2.2.3 with a new licence \"GPL v2 or later\", hence, he put a version mtx-2.2.4 on the download page, and as much as I see it differs from mtx-2.2.3 only by a new COPYING file.\n\nSo, I guess that in the documentation of our package I should replace all references to mtx-2.2.3 by a reference to mtx-2.2.4, and I should provide the new original sources in the folder 'mtxoriginal/' of our package.\n\nMy questions:\n- Look at the folder 'src/mtx-2.2.3'. Does it suffice to rename that folder to 'src/mtx-2.2.4' and replace the old COPYING file by the new one?\n- Specifically: Is it a problem that we use files showing cvs (or svn?) numbers that are different from those on the MeatAxe download page? For example, the *official*  'zzz.c' from the download page starts with\n  {{{\n/* ========================== C MeatAxe =============================\n   Finite field arithmetic and common functions. `Small' version for\n   field orders q <= 256. Originally based on the `hprout.c' written\n   by Klaus Lux.\n\n   (C) Copyright 1993 Michael Ringe, Lehrstuhl D fuer Mathematik,\n   RWTH Aachen, Germany  <mringe`@`tiffy.math.rwth-aachen.de>\n   This program is free software; see the file COPYING for details.\n   ================================================================== */\n\n\n/* $Id: zzz.c,v 2.20 1995/06/22 13:19:45 mringe Exp $\n *\n* $Log: zzz.c,v $\n* Revision 2.20  1995/06/22  13:19:45  mringe\n* Teste, ob MeatAxeBinDir != 0\n *\n* Revision 2.19  1995/05/12  10:07:20  mringe\n* Benutze MeatAxeBinDir beim Aufruf von maketab.\n *\n* Revision 2.18  1994/11/28  16:38:00  mringe\n* Neue Namen: SFOpen() und SFSeek().\n *\n   }}}\n   while we have the corresponding file starting with \n   {{{\n/* ========================== C MeatAxe =============================\n   Finite field arithmetic and common functions. `Small' version for\n   field orders q <= 256. Originally based on the `hprout.c' written\n   by Klaus Lux.\n\n   (C) Copyright 1993 Michael Ringe, Lehrstuhl D fuer Mathematik,\n   RWTH Aachen, Germany  <mringe`@`tiffy.math.rwth-aachen.de>\n   This program is free software; see the file COPYING for details.\n   ================================================================== */\n\n\n/* $Id: zzz.c,v 1.2 1997/09/11 15:44:42 gap Exp $\n *\n* $Log: zzz.c,v $\n* Revision 1.2  1997/09/11 15:44:42  gap\n* New version 2.2.3. AH\n *\n* Revision 2.20  1995/06/22  13:19:45  mringe\n* Teste, ob MeatAxeBinDir != 0\n *\n* Revision 2.19  1995/05/12  10:07:20  mringe\n* Benutze MeatAxeBinDir beim Aufruf von maketab.\n  }}}\n\n  So, my question is: Must these file headers match in order to conform with the licence? If this were the case, I had a lot of dull work to do...\n\n- My files start with a header such as\n  {{{\n#*****************************************************************************\n#\n#    Cohomology Rings of Finite p-Groups\n#\n#    Copyright (C) 2009 Simon A. King <simon.king`@`uni-jena.de>\n#\n#  Distributed under the terms of the GNU General Public License (GPL)\n#\n#    This code is distributed in the hope that it will be useful,\n#    but WITHOUT ANY WARRANTY; without even the implied warranty of\n#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU\n#    General Public License for more details.\n#\n#  The full text of the GPL is available at:\n#\n#                  http://www.gnu.org/licenses/\n#*****************************************************************************\n   }}}\n   Does this already mean that my code is *correctly* (whatever that means) licenced under GPL? Or do I need to provide a COPYING file as well?\n\nPlease excuse if these questions are stupid. But my impression is that licences are taken serious, and I have *no idea whatsoever* on that matter.",
    "created_at": "2009-07-17T21:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52403",
    "user": "https://github.com/simon-king-jena"
}
```

There's news about licences:

Michael Ringe kindly agreed to provide mtx-2.2.3 with a new licence "GPL v2 or later", hence, he put a version mtx-2.2.4 on the download page, and as much as I see it differs from mtx-2.2.3 only by a new COPYING file.

So, I guess that in the documentation of our package I should replace all references to mtx-2.2.3 by a reference to mtx-2.2.4, and I should provide the new original sources in the folder 'mtxoriginal/' of our package.

My questions:
- Look at the folder 'src/mtx-2.2.3'. Does it suffice to rename that folder to 'src/mtx-2.2.4' and replace the old COPYING file by the new one?
- Specifically: Is it a problem that we use files showing cvs (or svn?) numbers that are different from those on the MeatAxe download page? For example, the *official*  'zzz.c' from the download page starts with
  {{{
/* ========================== C MeatAxe =============================
   Finite field arithmetic and common functions. `Small' version for
   field orders q <= 256. Originally based on the `hprout.c' written
   by Klaus Lux.

   (C) Copyright 1993 Michael Ringe, Lehrstuhl D fuer Mathematik,
   RWTH Aachen, Germany  <mringe`@`tiffy.math.rwth-aachen.de>
   This program is free software; see the file COPYING for details.
   ================================================================== */


/* $Id: zzz.c,v 2.20 1995/06/22 13:19:45 mringe Exp $
 *
* $Log: zzz.c,v $
* Revision 2.20  1995/06/22  13:19:45  mringe
* Teste, ob MeatAxeBinDir != 0
 *
* Revision 2.19  1995/05/12  10:07:20  mringe
* Benutze MeatAxeBinDir beim Aufruf von maketab.
 *
* Revision 2.18  1994/11/28  16:38:00  mringe
* Neue Namen: SFOpen() und SFSeek().
 *
   }}}
   while we have the corresponding file starting with 
   {{{
/* ========================== C MeatAxe =============================
   Finite field arithmetic and common functions. `Small' version for
   field orders q <= 256. Originally based on the `hprout.c' written
   by Klaus Lux.

   (C) Copyright 1993 Michael Ringe, Lehrstuhl D fuer Mathematik,
   RWTH Aachen, Germany  <mringe`@`tiffy.math.rwth-aachen.de>
   This program is free software; see the file COPYING for details.
   ================================================================== */


/* $Id: zzz.c,v 1.2 1997/09/11 15:44:42 gap Exp $
 *
* $Log: zzz.c,v $
* Revision 1.2  1997/09/11 15:44:42  gap
* New version 2.2.3. AH
 *
* Revision 2.20  1995/06/22  13:19:45  mringe
* Teste, ob MeatAxeBinDir != 0
 *
* Revision 2.19  1995/05/12  10:07:20  mringe
* Benutze MeatAxeBinDir beim Aufruf von maketab.
  }}}

  So, my question is: Must these file headers match in order to conform with the licence? If this were the case, I had a lot of dull work to do...

- My files start with a header such as
  {{{
#*****************************************************************************
#
#    Cohomology Rings of Finite p-Groups
#
#    Copyright (C) 2009 Simon A. King <simon.king`@`uni-jena.de>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#
#    This code is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    General Public License for more details.
#
#  The full text of the GPL is available at:
#
#                  http://www.gnu.org/licenses/
#*****************************************************************************
   }}}
   Does this already mean that my code is *correctly* (whatever that means) licenced under GPL? Or do I need to provide a COPYING file as well?

Please excuse if these questions are stupid. But my impression is that licences are taken serious, and I have *no idea whatsoever* on that matter.



---

archive/issue_comments_052404.json:
```json
{
    "body": "Replying to [comment:26 SimonKing]:\n> There's news about licences:\n> \n> Michael Ringe kindly agreed to provide mtx-2.2.3 with a new licence \"GPL v2 or later\", hence, he put a version mtx-2.2.4 on the download page, and as much as I see it differs from mtx-2.2.3 only by a new COPYING file.\n> \n\n\nGood news!\n\n\n> So, I guess that in the documentation of our package I should replace all references to mtx-2.2.3 by a reference to mtx-2.2.4, and I should provide the new original sources in the folder 'mtxoriginal/' of our package.\n> \n> My questions:\n>  - Look at the folder 'src/mtx-2.2.3'. Does it suffice to rename that folder to 'src/mtx-2.2.4' and replace the old COPYING file by the new one?\n\n\nThat seems fine.\n\n\n>  - Specifically: Is it a problem that we use files showing cvs (or svn?) numbers that are different from those on the MeatAxe download page? For example, the \n\n\nI don't see how this is a problem.\n\n\n> *official*  'zzz.c' from the download page starts with\n>    {{{\n> /* ========================== C MeatAxe =============================\n>    Finite field arithmetic and common functions. `Small' version for\n>    field orders q <= 256. Originally based on the `hprout.c' written\n>    by Klaus Lux.\n> \n>    (C) Copyright 1993 Michael Ringe, Lehrstuhl D fuer Mathematik,\n>    RWTH Aachen, Germany  <mringe`@`tiffy.math.rwth-aachen.de>\n>    This program is free software; see the file COPYING for details.\n>    ================================================================== */\n> \n> \n> /* $Id: zzz.c,v 2.20 1995/06/22 13:19:45 mringe Exp $\n>  *\n>  * $Log: zzz.c,v $\n>  * Revision 2.20  1995/06/22  13:19:45  mringe\n>  * Teste, ob MeatAxeBinDir != 0\n>  *\n>  * Revision 2.19  1995/05/12  10:07:20  mringe\n>  * Benutze MeatAxeBinDir beim Aufruf von maketab.\n>  *\n>  * Revision 2.18  1994/11/28  16:38:00  mringe\n>  * Neue Namen: SFOpen() und SFSeek().\n>  *\n>    }}}\n>    while we have the corresponding file starting with \n>    {{{\n> /* ========================== C MeatAxe =============================\n>    Finite field arithmetic and common functions. `Small' version for\n>    field orders q <= 256. Originally based on the `hprout.c' written\n>    by Klaus Lux.\n> \n>    (C) Copyright 1993 Michael Ringe, Lehrstuhl D fuer Mathematik,\n>    RWTH Aachen, Germany  <mringe`@`tiffy.math.rwth-aachen.de>\n>    This program is free software; see the file COPYING for details.\n>    ================================================================== */\n> \n> \n> /* $Id: zzz.c,v 1.2 1997/09/11 15:44:42 gap Exp $\n>  *\n>  * $Log: zzz.c,v $\n>  * Revision 1.2  1997/09/11 15:44:42  gap\n>  * New version 2.2.3. AH\n>  *\n>  * Revision 2.20  1995/06/22  13:19:45  mringe\n>  * Teste, ob MeatAxeBinDir != 0\n>  *\n>  * Revision 2.19  1995/05/12  10:07:20  mringe\n>  * Benutze MeatAxeBinDir beim Aufruf von maketab.\n>    }}}\n> \n>    So, my question is: Must these file headers match in order to conform with the licence? If this were the case, I had a lot of dull work to do...\n> \n>  - My files start with a header such as\n>    {{{\n> #*****************************************************************************\n> #\n> #    Cohomology Rings of Finite p-Groups\n> #\n> #    Copyright (C) 2009 Simon A. King <simon.king`@`uni-jena.de>\n> #\n> #  Distributed under the terms of the GNU General Public License (GPL)\n> #\n> #    This code is distributed in the hope that it will be useful,\n> #    but WITHOUT ANY WARRANTY; without even the implied warranty of\n> #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU\n> #    General Public License for more details.\n> #\n> #  The full text of the GPL is available at:\n> #\n> #                  http://www.gnu.org/licenses/\n> #*****************************************************************************\n>    }}}\n>    Does this already mean that my code is *correctly* (whatever that means) licenced under GPL? Or do I need to provide a COPYING file as well?\n\n\nYou should change \"#  Distributed under the terms of the GNU General Public License (GPL)\" to \"#  Distributed under the terms of the GNU General Public License (GPL), version 2 or later (at your choice)\" or something like that.\n\nIf you don't specify the version of the GPL you use then it defaults to the latest version (which is version 3 currently). You don't want that.\n\n\n> \n> Please excuse if these questions are stupid. But my impression is that licences are taken serious, and I have *no idea whatsoever* on that matter.",
    "created_at": "2009-07-18T07:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52404",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:26 SimonKing]:
> There's news about licences:
> 
> Michael Ringe kindly agreed to provide mtx-2.2.3 with a new licence "GPL v2 or later", hence, he put a version mtx-2.2.4 on the download page, and as much as I see it differs from mtx-2.2.3 only by a new COPYING file.
> 


Good news!


> So, I guess that in the documentation of our package I should replace all references to mtx-2.2.3 by a reference to mtx-2.2.4, and I should provide the new original sources in the folder 'mtxoriginal/' of our package.
> 
> My questions:
>  - Look at the folder 'src/mtx-2.2.3'. Does it suffice to rename that folder to 'src/mtx-2.2.4' and replace the old COPYING file by the new one?


That seems fine.


>  - Specifically: Is it a problem that we use files showing cvs (or svn?) numbers that are different from those on the MeatAxe download page? For example, the 


I don't see how this is a problem.


> *official*  'zzz.c' from the download page starts with
>    {{{
> /* ========================== C MeatAxe =============================
>    Finite field arithmetic and common functions. `Small' version for
>    field orders q <= 256. Originally based on the `hprout.c' written
>    by Klaus Lux.
> 
>    (C) Copyright 1993 Michael Ringe, Lehrstuhl D fuer Mathematik,
>    RWTH Aachen, Germany  <mringe`@`tiffy.math.rwth-aachen.de>
>    This program is free software; see the file COPYING for details.
>    ================================================================== */
> 
> 
> /* $Id: zzz.c,v 2.20 1995/06/22 13:19:45 mringe Exp $
>  *
>  * $Log: zzz.c,v $
>  * Revision 2.20  1995/06/22  13:19:45  mringe
>  * Teste, ob MeatAxeBinDir != 0
>  *
>  * Revision 2.19  1995/05/12  10:07:20  mringe
>  * Benutze MeatAxeBinDir beim Aufruf von maketab.
>  *
>  * Revision 2.18  1994/11/28  16:38:00  mringe
>  * Neue Namen: SFOpen() und SFSeek().
>  *
>    }}}
>    while we have the corresponding file starting with 
>    {{{
> /* ========================== C MeatAxe =============================
>    Finite field arithmetic and common functions. `Small' version for
>    field orders q <= 256. Originally based on the `hprout.c' written
>    by Klaus Lux.
> 
>    (C) Copyright 1993 Michael Ringe, Lehrstuhl D fuer Mathematik,
>    RWTH Aachen, Germany  <mringe`@`tiffy.math.rwth-aachen.de>
>    This program is free software; see the file COPYING for details.
>    ================================================================== */
> 
> 
> /* $Id: zzz.c,v 1.2 1997/09/11 15:44:42 gap Exp $
>  *
>  * $Log: zzz.c,v $
>  * Revision 1.2  1997/09/11 15:44:42  gap
>  * New version 2.2.3. AH
>  *
>  * Revision 2.20  1995/06/22  13:19:45  mringe
>  * Teste, ob MeatAxeBinDir != 0
>  *
>  * Revision 2.19  1995/05/12  10:07:20  mringe
>  * Benutze MeatAxeBinDir beim Aufruf von maketab.
>    }}}
> 
>    So, my question is: Must these file headers match in order to conform with the licence? If this were the case, I had a lot of dull work to do...
> 
>  - My files start with a header such as
>    {{{
> #*****************************************************************************
> #
> #    Cohomology Rings of Finite p-Groups
> #
> #    Copyright (C) 2009 Simon A. King <simon.king`@`uni-jena.de>
> #
> #  Distributed under the terms of the GNU General Public License (GPL)
> #
> #    This code is distributed in the hope that it will be useful,
> #    but WITHOUT ANY WARRANTY; without even the implied warranty of
> #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
> #    General Public License for more details.
> #
> #  The full text of the GPL is available at:
> #
> #                  http://www.gnu.org/licenses/
> #*****************************************************************************
>    }}}
>    Does this already mean that my code is *correctly* (whatever that means) licenced under GPL? Or do I need to provide a COPYING file as well?


You should change "#  Distributed under the terms of the GNU General Public License (GPL)" to "#  Distributed under the terms of the GNU General Public License (GPL), version 2 or later (at your choice)" or something like that.

If you don't specify the version of the GPL you use then it defaults to the latest version (which is version 3 currently). You don't want that.


> 
> Please excuse if these questions are stupid. But my impression is that licences are taken serious, and I have *no idea whatsoever* on that matter.



---

archive/issue_comments_052405.json:
```json
{
    "body": "I am about to produce a version 1.0.1, that will essentially be an attempt to fix the licence.\n\n- I took the COPYING file from the MeatAxe 2.2.4 and put it on top of our modified MeatAxe version. Since the licence allows redistribution of the modified work, as long as the COPYING file isn't touched, this should be alright.\n- The C-code of David Green got a similar COPYING file. So, this is GPL 2+ as well.\n- Each of my files starts with a header, referring to the GPL, version 2 or later.\n- I think it should be appropriate to put the data bases under a Creative Commons Attribution-Share Alike licence. \n\n__Questions:__\n\n- In order to put the data bases under the mentioned licence, does it suffice to state it in the documentation, as I now did in http://sage.math.washington.edu/home/SimonKing/Cohomology/#licence ?  You suggested to put a 'LICENSE.txt' into the package; but the major part of the data base is not included in the package, but only available in the internet. So, I thought that the package documentation is the right place for stating the licence. Is this OK? Or perhaps I should add some words concerning the data bases in the file 'SPKG.txt', that has a licence section anyway?\n- It is also stated that the documentation itself is under CC Attribution-Share Alike. But: The documentation is mainly auto-generated using the source code of our package, which means that the documentation is derived work from something that is under GPL 2+. So, is it legal to use another licence for the documentation, or am I shooting myself in the foot?\n\nOnce theses questions are addressed, I will put a version 1.0.1 of our package online, so that hopefully the last reviewing steps can be done.\n\nBest regards,\n   Simon",
    "created_at": "2009-07-20T23:38:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52405",
    "user": "https://github.com/simon-king-jena"
}
```

I am about to produce a version 1.0.1, that will essentially be an attempt to fix the licence.

- I took the COPYING file from the MeatAxe 2.2.4 and put it on top of our modified MeatAxe version. Since the licence allows redistribution of the modified work, as long as the COPYING file isn't touched, this should be alright.
- The C-code of David Green got a similar COPYING file. So, this is GPL 2+ as well.
- Each of my files starts with a header, referring to the GPL, version 2 or later.
- I think it should be appropriate to put the data bases under a Creative Commons Attribution-Share Alike licence. 

__Questions:__

- In order to put the data bases under the mentioned licence, does it suffice to state it in the documentation, as I now did in http://sage.math.washington.edu/home/SimonKing/Cohomology/#licence ?  You suggested to put a 'LICENSE.txt' into the package; but the major part of the data base is not included in the package, but only available in the internet. So, I thought that the package documentation is the right place for stating the licence. Is this OK? Or perhaps I should add some words concerning the data bases in the file 'SPKG.txt', that has a licence section anyway?
- It is also stated that the documentation itself is under CC Attribution-Share Alike. But: The documentation is mainly auto-generated using the source code of our package, which means that the documentation is derived work from something that is under GPL 2+. So, is it legal to use another licence for the documentation, or am I shooting myself in the foot?

Once theses questions are addressed, I will put a version 1.0.1 of our package online, so that hopefully the last reviewing steps can be done.

Best regards,
   Simon



---

archive/issue_comments_052406.json:
```json
{
    "body": "Replying to [comment:28 SimonKing]:\n> I am about to produce a version 1.0.1, that will essentially be an attempt to fix the license.\n> \n>  - I took the COPYING file from the MeatAxe 2.2.4 and put it on top of our modified MeatAxe version. Since the licence allows redistribution of the modified work, as long as the COPYING file isn't touched, this should be alright.\n>  - The C-code of David Green got a similar COPYING file. So, this is GPL 2+ as well.\n>  - Each of my files starts with a header, referring to the GPL, version 2 or later.\n>  - I think it should be appropriate to put the data bases under a Creative Commons Attribution-Share Alike licence. \n> \n> __Questions:__\n> \n>  - In order to put the data bases under the mentioned licence, does it suffice to state \n> it in the documentation, as I now did in http://sage.math.washington.edu/home/SimonKing/Cohomology/#licence ?  \n> You suggested to put a 'LICENSE.txt' into the package; but the major part of the data base is not \n> included in the package, but only available in the internet. So, I thought that the package \n> documentation is the right place for stating the licence. Is this OK? Or perhaps I should add \n> some words concerning the data bases in the file 'SPKG.txt', that has a licence section anyway?\n\n\nI'm not crazy about putting the database license statement in the docs or in SPKG.txt, though it\nis fine to mention them there. I prefer a separate file, say in the same directory or tarball\nthe database is stored in. I don't think it's important enough to argue about.\n\n\n>  - It is also stated that the documentation itself is under CC Attribution-Share Alike. But: \n> The documentation is mainly auto-generated using the source code of our package, which means that \n> the documentation is derived work from something that is under GPL 2+. So, is it legal to use another \n> licence for the documentation, or am I shooting myself in the foot?\n\n\nThe code snippets are (I presume) yours and you can relicense or dual license it as you wish.\n\n\nBTW, I think \"licence\" should be \"license\".\n\n\n> \n> Once theses questions are addressed, I will put a version 1.0.1 of our package online, so that hopefully the last reviewing steps can be done.\n> \n> Best regards,\n>    Simon",
    "created_at": "2009-07-21T00:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52406",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:28 SimonKing]:
> I am about to produce a version 1.0.1, that will essentially be an attempt to fix the license.
> 
>  - I took the COPYING file from the MeatAxe 2.2.4 and put it on top of our modified MeatAxe version. Since the licence allows redistribution of the modified work, as long as the COPYING file isn't touched, this should be alright.
>  - The C-code of David Green got a similar COPYING file. So, this is GPL 2+ as well.
>  - Each of my files starts with a header, referring to the GPL, version 2 or later.
>  - I think it should be appropriate to put the data bases under a Creative Commons Attribution-Share Alike licence. 
> 
> __Questions:__
> 
>  - In order to put the data bases under the mentioned licence, does it suffice to state 
> it in the documentation, as I now did in http://sage.math.washington.edu/home/SimonKing/Cohomology/#licence ?  
> You suggested to put a 'LICENSE.txt' into the package; but the major part of the data base is not 
> included in the package, but only available in the internet. So, I thought that the package 
> documentation is the right place for stating the licence. Is this OK? Or perhaps I should add 
> some words concerning the data bases in the file 'SPKG.txt', that has a licence section anyway?


I'm not crazy about putting the database license statement in the docs or in SPKG.txt, though it
is fine to mention them there. I prefer a separate file, say in the same directory or tarball
the database is stored in. I don't think it's important enough to argue about.


>  - It is also stated that the documentation itself is under CC Attribution-Share Alike. But: 
> The documentation is mainly auto-generated using the source code of our package, which means that 
> the documentation is derived work from something that is under GPL 2+. So, is it legal to use another 
> licence for the documentation, or am I shooting myself in the foot?


The code snippets are (I presume) yours and you can relicense or dual license it as you wish.


BTW, I think "licence" should be "license".


> 
> Once theses questions are addressed, I will put a version 1.0.1 of our package online, so that hopefully the last reviewing steps can be done.
> 
> Best regards,
>    Simon



---

archive/issue_comments_052407.json:
```json
{
    "body": "Hi David!\n\nReplying to [comment:29 wdj]:\n> I'm not crazy about putting the database license statement in the docs or in SPKG.txt, though it\n> is fine to mention them there. I prefer a separate file, say in the same directory or tarball\n> the database is stored in. I don't think it's important enough to argue about.\n \nOK. \n\nI think it is more likely that people read the docs than manually enter http://sage.math.washington.edu/home/SimonKing/Cohomology/db/ where the main part of the data base currently sits. So, it seems logical to me to point out the licence in the docs rather than in the directory.\n\n> The code snippets are (I presume) yours and you can relicense or dual license it as you wish.\n\nAll Python and Cython code, including the documentation, is 100% written by myself.\n\n> BTW, I think \"licence\" should be \"license\".\n\nYou know, David Green is from England, and he told me that he wants to *licenSe* our package under a certain *licenCe*... :-)\n\nUsually I try to use British English. Only when I directly refer to the \"GNU Public License\", I spell it the US way -- since I think of it as the *name* of the licence.\n\nCheers,\n   Simon",
    "created_at": "2009-07-21T01:33:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52407",
    "user": "https://github.com/simon-king-jena"
}
```

Hi David!

Replying to [comment:29 wdj]:
> I'm not crazy about putting the database license statement in the docs or in SPKG.txt, though it
> is fine to mention them there. I prefer a separate file, say in the same directory or tarball
> the database is stored in. I don't think it's important enough to argue about.
 
OK. 

I think it is more likely that people read the docs than manually enter http://sage.math.washington.edu/home/SimonKing/Cohomology/db/ where the main part of the data base currently sits. So, it seems logical to me to point out the licence in the docs rather than in the directory.

> The code snippets are (I presume) yours and you can relicense or dual license it as you wish.

All Python and Cython code, including the documentation, is 100% written by myself.

> BTW, I think "licence" should be "license".

You know, David Green is from England, and he told me that he wants to *licenSe* our package under a certain *licenCe*... :-)

Usually I try to use British English. Only when I directly refer to the "GNU Public License", I spell it the US way -- since I think of it as the *name* of the licence.

Cheers,
   Simon



---

archive/issue_comments_052408.json:
```json
{
    "body": "I created a new version 1.0.1 of our package. You can install and test it by\n\n```\nsage -i http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.0.1\n```\n\n\nI did not open a new ticket for the new package version, since the changes mainly concern the points that were discussed here: Licenc/se...\n\n- The (modified) MeatAxe version in our package is now GPL2+. Many thanks to Michael Ringe for making this happen!\n- As I point out in the file SPKG.txt (that you find after opening the package with \"tar -xj\"), the licence of the package is GPL2+, while the data base and the documentation are CC By-SA.\n- The licence is also stated in the package's documentation, namely at http://sage.math.washington.edu/home/SimonKing/Cohomology/#licence\n- When the package gets installed, a file LICENCE is copied into the folder containing the data base (SAGE_ROOT/local/pGroupCohomology/db/), and a similar file is also at http://sage.math.washington.edu/home/SimonKing/Cohomology/db/\n\nNow you certainly think I am paranoid.\n\nApart from that, I did the following changes:\n\n- There is a new method for cochains, returning the right multiplication by that cochain as a map of cohomology rings. So, this is a map that is not of degree zero and couldn't be dealt with before. There are new doc tests for composition of those maps.\n- The test suite \"spkg-check\" (in the standard location, i.e. after opening the package with \"tar -xj\") now does the tests one at a time, so that Singular will not be overworked. The new test suite \"spkg-check-quickly\" is quicker, but may result in the Singular errors that David found on some machines. Both test suites have to be executed in a Sage shell.\n- The Massey products are not included yet, I need a lot more time for them.\n\nI ask the reviewer(s) to do the following:\n\n- Install the new package version, including platforms such as OS X (I am really happy and surprised that it worked with the first version!!)\n- Run the test suite(s)\n- Do some reading in the documentation http://sage.math.washington.edu/home/SimonKing/Cohomology/ and see if you find it useful\n\nShould a positive review result: Must I start a voting on sage-devel before it can become an optional package?\n\nBest regards\n   Simon",
    "created_at": "2009-07-22T03:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52408",
    "user": "https://github.com/simon-king-jena"
}
```

I created a new version 1.0.1 of our package. You can install and test it by

```
sage -i http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.0.1
```


I did not open a new ticket for the new package version, since the changes mainly concern the points that were discussed here: Licenc/se...

- The (modified) MeatAxe version in our package is now GPL2+. Many thanks to Michael Ringe for making this happen!
- As I point out in the file SPKG.txt (that you find after opening the package with "tar -xj"), the licence of the package is GPL2+, while the data base and the documentation are CC By-SA.
- The licence is also stated in the package's documentation, namely at http://sage.math.washington.edu/home/SimonKing/Cohomology/#licence
- When the package gets installed, a file LICENCE is copied into the folder containing the data base (SAGE_ROOT/local/pGroupCohomology/db/), and a similar file is also at http://sage.math.washington.edu/home/SimonKing/Cohomology/db/

Now you certainly think I am paranoid.

Apart from that, I did the following changes:

- There is a new method for cochains, returning the right multiplication by that cochain as a map of cohomology rings. So, this is a map that is not of degree zero and couldn't be dealt with before. There are new doc tests for composition of those maps.
- The test suite "spkg-check" (in the standard location, i.e. after opening the package with "tar -xj") now does the tests one at a time, so that Singular will not be overworked. The new test suite "spkg-check-quickly" is quicker, but may result in the Singular errors that David found on some machines. Both test suites have to be executed in a Sage shell.
- The Massey products are not included yet, I need a lot more time for them.

I ask the reviewer(s) to do the following:

- Install the new package version, including platforms such as OS X (I am really happy and surprised that it worked with the first version!!)
- Run the test suite(s)
- Do some reading in the documentation http://sage.math.washington.edu/home/SimonKing/Cohomology/ and see if you find it useful

Should a positive review result: Must I start a voting on sage-devel before it can become an optional package?

Best regards
   Simon



---

archive/issue_comments_052409.json:
```json
{
    "body": "1. \n\n```\nI see. You are right, I should put the code for CohomologyRing? into a different file (say, cohomology_constructor.py), so that init.py only contains the import statement \"from pGroupCohomology.cohomology_constructor import CohomologyRing?\". In that way, it is still possible for the user to do \"from pGroupCohomology import CohomologyRing?\". OK, I will do so. \n```\n\nYou didn't do this, as far as I can tell.\n\n2. There is no indication that I can find that you got permission to license meataxe as GPLv2+.\n\n3. The package is (IMHO) very disorganized. Files are scattered over various directories without rhyme or reason. I cannot find a guide in the docs as to how the unpacking is done, so one can find the source and read it if one desired details on the algorithms implemented. (For example, why not just put everything in python2.6/site-packages?)\n\n4. I cannot find the test files spkg-check in the sage tree. Or do you expact people who want to run tests to download your package and unpack it separately (as I did before)?",
    "created_at": "2009-07-25T14:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52409",
    "user": "https://github.com/wdjoyner"
}
```

1. 

```
I see. You are right, I should put the code for CohomologyRing? into a different file (say, cohomology_constructor.py), so that init.py only contains the import statement "from pGroupCohomology.cohomology_constructor import CohomologyRing?". In that way, it is still possible for the user to do "from pGroupCohomology import CohomologyRing?". OK, I will do so. 
```

You didn't do this, as far as I can tell.

2. There is no indication that I can find that you got permission to license meataxe as GPLv2+.

3. The package is (IMHO) very disorganized. Files are scattered over various directories without rhyme or reason. I cannot find a guide in the docs as to how the unpacking is done, so one can find the source and read it if one desired details on the algorithms implemented. (For example, why not just put everything in python2.6/site-packages?)

4. I cannot find the test files spkg-check in the sage tree. Or do you expact people who want to run tests to download your package and unpack it separately (as I did before)?



---

archive/issue_comments_052410.json:
```json
{
    "body": "Another clarifying comment or two.\n\nPossibly I cannot find files but you have clearly indicated where they are somewhere in the sage tree. (Note I said in the sage tree, not in your package spkg file.) If so, there might not be serious problems with your license. If not, I think there could be serious problems. \n\nExample: I write a GPL program. You use it in yours but allow for it to be downloaded and installed without the license. IMHO this is a violation of the GPL. Maybe you are violating the GPL or maybe not, but for me it is hard to find what files are loaded where in the sage tree so I really can't tell what is licensed how.",
    "created_at": "2009-07-25T15:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52410",
    "user": "https://github.com/wdjoyner"
}
```

Another clarifying comment or two.

Possibly I cannot find files but you have clearly indicated where they are somewhere in the sage tree. (Note I said in the sage tree, not in your package spkg file.) If so, there might not be serious problems with your license. If not, I think there could be serious problems. 

Example: I write a GPL program. You use it in yours but allow for it to be downloaded and installed without the license. IMHO this is a violation of the GPL. Maybe you are violating the GPL or maybe not, but for me it is hard to find what files are loaded where in the sage tree so I really can't tell what is licensed how.



---

archive/issue_comments_052411.json:
```json
{
    "body": "Replying to [comment:32 wdj]:\n> 1. \n> {{{\n> I see. You are right, I should put the code for CohomologyRing? into a different file (say, cohomology_constructor.py), so that init.py only contains the import statement \"from pGroupCohomology.cohomology_constructor import CohomologyRing?\". In that way, it is still possible for the user to do \"from pGroupCohomology import CohomologyRing?\". OK, I will do so. \n> }}}\n> You didn't do this, as far as I can tell.\n\nYes, after thinking it over, my impression was that the old solution was better: Loading the package would still require some initialisation - no matter whether it is done in __init__.py or somewhere else. So, there is no gain in startup time. And if the user is importing by \"from pGroupCohomology import CohomologyRing\", but in fact the code is in \"pGrouCohomology.SomeSubmodule\", the user might be confused. \n \n> 2. There is no indication that I can find that you got permission to license meataxe as GPLv2+.\n\nAs stated in SPKG.txt (the usual place where those informations are provided), the package contains the original meataxe sources of the version 2.2.4 (folder \"mtxoriginal\"), including the COPYING file, that I also provide in our modified meataxe version (folder \"src/mtx2.2.4\"). And the documentation refers to the MeatAxe download page, where version 2.2.4 (differing from 2.2.3 only by its licence) is available. I don't see how the licence could be made clearer than by providing the original sources.\n\n> 3. The package is (IMHO) very disorganized. Files are scattered over various directories without rhyme or reason.\n\nI think it is very clear. There is \"mtxoriginal/\", providing the original source of a third party package. There is \"src/\", which contains all code that is used in the package. The package is based on three components: Meataxe (c-code, in \"mtx2.2.4/\"), some executables written in C for computing some basic data (\"present/\"), and the Cython modules (in \"pGroupCohomology/\"), together with some c-files the cython code is linked with (\"pGroupCohomology/c_sources/\").\n\n> I cannot find a guide in the docs as to how the unpacking is done, so one can find the source and read it if one desired details on the algorithms implemented. \n\nOf course it is not covered in the docs of the package, because unpacking an spkg is something that a user usually doesn't. And a user who *does* unpack it for reading the code is usually aware of the fact that any spkg can be opened with \"tar -xjf\"; this is pointed out in the Sage developer's guide.\n\n> (For example, why not just put everything in python2.6/site-packages?)\n\nI don't understand the question. Of course, neither Cython code nor c-code is supposed to be in python2.6/site-packages! Nor are the executables of meataxe and the additional executables from \"present/\". And the compiled extension modules *are*, of course, in python2.6/site-packages. \n\n> 4. I cannot find the test files spkg-check in the sage tree. Or do you expact people who want to run tests to download your package and unpack it separately (as I did before)?\n\nJust read the relevant chapter in the developer's guide, [http://www.sagemath.org/doc/developer/producing_spkgs.html](http://www.sagemath.org/doc/developer/producing_spkgs.html).\n\nspkg-check is not supposed to be in the Sage tree. \n\nRead also a thread on sage-devel, where I raised some related questions, at [http://groups.google.com/group/sage-devel/browse_thread/thread/5e286c6ec0d90879/40e55782bbb0e144?lnk=gst&q=spkg-check#40e55782bbb0e144](http://groups.google.com/group/sage-devel/browse_thread/thread/5e286c6ec0d90879/40e55782bbb0e144?lnk=gst&q=spkg-check#40e55782bbb0e144). I think that this thread makes clear that if a user wants to test the package then (s)he is supposed to open it and run the test suite provided in the package.\n\nBest regards,\n    Simon",
    "created_at": "2009-07-25T22:00:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52411",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:32 wdj]:
> 1. 
> {{{
> I see. You are right, I should put the code for CohomologyRing? into a different file (say, cohomology_constructor.py), so that init.py only contains the import statement "from pGroupCohomology.cohomology_constructor import CohomologyRing?". In that way, it is still possible for the user to do "from pGroupCohomology import CohomologyRing?". OK, I will do so. 
> }}}
> You didn't do this, as far as I can tell.

Yes, after thinking it over, my impression was that the old solution was better: Loading the package would still require some initialisation - no matter whether it is done in __init__.py or somewhere else. So, there is no gain in startup time. And if the user is importing by "from pGroupCohomology import CohomologyRing", but in fact the code is in "pGrouCohomology.SomeSubmodule", the user might be confused. 
 
> 2. There is no indication that I can find that you got permission to license meataxe as GPLv2+.

As stated in SPKG.txt (the usual place where those informations are provided), the package contains the original meataxe sources of the version 2.2.4 (folder "mtxoriginal"), including the COPYING file, that I also provide in our modified meataxe version (folder "src/mtx2.2.4"). And the documentation refers to the MeatAxe download page, where version 2.2.4 (differing from 2.2.3 only by its licence) is available. I don't see how the licence could be made clearer than by providing the original sources.

> 3. The package is (IMHO) very disorganized. Files are scattered over various directories without rhyme or reason.

I think it is very clear. There is "mtxoriginal/", providing the original source of a third party package. There is "src/", which contains all code that is used in the package. The package is based on three components: Meataxe (c-code, in "mtx2.2.4/"), some executables written in C for computing some basic data ("present/"), and the Cython modules (in "pGroupCohomology/"), together with some c-files the cython code is linked with ("pGroupCohomology/c_sources/").

> I cannot find a guide in the docs as to how the unpacking is done, so one can find the source and read it if one desired details on the algorithms implemented. 

Of course it is not covered in the docs of the package, because unpacking an spkg is something that a user usually doesn't. And a user who *does* unpack it for reading the code is usually aware of the fact that any spkg can be opened with "tar -xjf"; this is pointed out in the Sage developer's guide.

> (For example, why not just put everything in python2.6/site-packages?)

I don't understand the question. Of course, neither Cython code nor c-code is supposed to be in python2.6/site-packages! Nor are the executables of meataxe and the additional executables from "present/". And the compiled extension modules *are*, of course, in python2.6/site-packages. 

> 4. I cannot find the test files spkg-check in the sage tree. Or do you expact people who want to run tests to download your package and unpack it separately (as I did before)?

Just read the relevant chapter in the developer's guide, [http://www.sagemath.org/doc/developer/producing_spkgs.html](http://www.sagemath.org/doc/developer/producing_spkgs.html).

spkg-check is not supposed to be in the Sage tree. 

Read also a thread on sage-devel, where I raised some related questions, at [http://groups.google.com/group/sage-devel/browse_thread/thread/5e286c6ec0d90879/40e55782bbb0e144?lnk=gst&q=spkg-check#40e55782bbb0e144](http://groups.google.com/group/sage-devel/browse_thread/thread/5e286c6ec0d90879/40e55782bbb0e144?lnk=gst&q=spkg-check#40e55782bbb0e144). I think that this thread makes clear that if a user wants to test the package then (s)he is supposed to open it and run the test suite provided in the package.

Best regards,
    Simon



---

archive/issue_comments_052412.json:
```json
{
    "body": "Replying to [comment:33 wdj]:\n> Another clarifying comment or two.\n> \n> Possibly I cannot find files but you have clearly indicated where they are somewhere in the sage tree. (Note I said in the sage tree, not in your package spkg file.) If so, there might not be serious problems with your license. If not, I think there could be serious problems. \n\nI don't see what you mean. The sources of an spkg are not supposed to be in the sage tree. Executables built by an spkg are supposed to be in SAGE_ROOT/local/bin, extension modules in SAGE_ROOT/local/bin/python2.6/site-packages/, and local data (e.g., data bases) in a subfolder of SAGE_ROOT/local, whose name is given by the name of the extension module (here: pGroupCohomology). And of course, when you install the package, then you get a copy of the (unpacked) spkg in SAGE_ROOT/spkg/optional/.\n\nSo, I don't think that I make anything different from any other spkg in that regard.\n\nBest regards,\n   Simon",
    "created_at": "2009-07-25T22:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52412",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:33 wdj]:
> Another clarifying comment or two.
> 
> Possibly I cannot find files but you have clearly indicated where they are somewhere in the sage tree. (Note I said in the sage tree, not in your package spkg file.) If so, there might not be serious problems with your license. If not, I think there could be serious problems. 

I don't see what you mean. The sources of an spkg are not supposed to be in the sage tree. Executables built by an spkg are supposed to be in SAGE_ROOT/local/bin, extension modules in SAGE_ROOT/local/bin/python2.6/site-packages/, and local data (e.g., data bases) in a subfolder of SAGE_ROOT/local, whose name is given by the name of the extension module (here: pGroupCohomology). And of course, when you install the package, then you get a copy of the (unpacked) spkg in SAGE_ROOT/spkg/optional/.

So, I don't think that I make anything different from any other spkg in that regard.

Best regards,
   Simon



---

archive/issue_comments_052413.json:
```json
{
    "body": "Replying to [comment:35 SimonKing]:\n> And of course, when you install the package, then you get a copy of the (unpacked) spkg in SAGE_ROOT/spkg/optional/.\n\nOops, typo. Of course, you get a copy of the *packed* spkg, that you can unpack with \"tar -xjf\".",
    "created_at": "2009-07-25T22:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52413",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:35 SimonKing]:
> And of course, when you install the package, then you get a copy of the (unpacked) spkg in SAGE_ROOT/spkg/optional/.

Oops, typo. Of course, you get a copy of the *packed* spkg, that you can unpack with "tar -xjf".



---

archive/issue_comments_052414.json:
```json
{
    "body": "Thanks for all this info. I have been too busy to read every thread and missed the one you mentioned. I guess I forgot the (compressed) package was in SAGE_ROOT/spkg/optional/. I think everything is okay now as far as licenses are concerned.\n\nAs far as the test, I am running the test on the machine I'm typing on now (an amd64 9.04 ubuntu). It passes all tests. The test will not run on my intel macbook (an import error of some type I think, but I don't remember the error - let me know if you want the exact details and I'll post a message from that machine with the traceback).\n\nI give this a positive review. Let me know if you want more testing.",
    "created_at": "2009-07-25T23:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52414",
    "user": "https://github.com/wdjoyner"
}
```

Thanks for all this info. I have been too busy to read every thread and missed the one you mentioned. I guess I forgot the (compressed) package was in SAGE_ROOT/spkg/optional/. I think everything is okay now as far as licenses are concerned.

As far as the test, I am running the test on the machine I'm typing on now (an amd64 9.04 ubuntu). It passes all tests. The test will not run on my intel macbook (an import error of some type I think, but I don't remember the error - let me know if you want the exact details and I'll post a message from that machine with the traceback).

I give this a positive review. Let me know if you want more testing.



---

archive/issue_comments_052415.json:
```json
{
    "body": "Replying to [comment:37 wdj]:\n> Thanks for all this info. I have been too busy to read every thread and missed the one you mentioned. I guess I forgot the (compressed) package was in SAGE_ROOT/spkg/optional/. I think everything is okay now as far as licenses are concerned.\n\nGood!\n\n> As far as the test, I am running the test on the machine I'm typing on now (an amd64 9.04 ubuntu). It passes all tests. The test will not run on my intel macbook (an import error of some type I think, but I don't remember the error - let me know if you want the exact details and I'll post a message from that machine with the traceback).\n\nYes, please! An import error probably indicates that the package did not built. Of course I wonder why the previous version used to work on your macbook.\n \n> I give this a positive review. Let me know if you want more testing.\n\nI guess the Macbook thing should be understood (although, as I mentioned, it was expected that Macbook is a problem).\n\nBest regards,\n    Simon",
    "created_at": "2009-07-26T00:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52415",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:37 wdj]:
> Thanks for all this info. I have been too busy to read every thread and missed the one you mentioned. I guess I forgot the (compressed) package was in SAGE_ROOT/spkg/optional/. I think everything is okay now as far as licenses are concerned.

Good!

> As far as the test, I am running the test on the machine I'm typing on now (an amd64 9.04 ubuntu). It passes all tests. The test will not run on my intel macbook (an import error of some type I think, but I don't remember the error - let me know if you want the exact details and I'll post a message from that machine with the traceback).

Yes, please! An import error probably indicates that the package did not built. Of course I wonder why the previous version used to work on your macbook.
 
> I give this a positive review. Let me know if you want more testing.

I guess the Macbook thing should be understood (although, as I mentioned, it was expected that Macbook is a problem).

Best regards,
    Simon



---

archive/issue_comments_052416.json:
```json
{
    "body": "Replying to [comment:38 SimonKing]:\n> Replying to [comment:37 wdj]:\n\n...\n\n> \n> > As far as the test, I am running the test on the machine I'm typing on now (an amd64 9.04 ubuntu). It passes all tests. The test will not run on my intel macbook (an import error of some type I think, but I don't remember the error - let me know if you want the exact details and I'll post a message from that machine with the traceback).\n\n\n\n```\nsage: !/Users/davidjoyner/sagefiles/p_group_cohomology-1.0.1/spkg-check\nTraceback (most recent call last):\n  File \"/Users/davidjoyner/sagefiles/p_group_cohomology-1.0.1/spkg-check\", line 99, in <module>\n    import pGroupCohomology\nImportError: No module named pGroupCohomology\n```\n\nand\n\n\n```\nzeus:~/sagefiles/sage-4.1.1.alpha0 davidjoyner$ ls local/lib/python2.6/site-packages/p_*\nls: local/lib/python2.6/site-packages/p_*: No such file or directory\n```\n\n\n\n> \n> Yes, please! An import error probably indicates that the package did not built. Of course I wonder why the previous version used to work on your macbook.\n>  \n> > I give this a positive review. Let me know if you want more testing.\n> \n> I guess the Macbook thing should be understood (although, as I mentioned, it was expected that Macbook is a problem).\n\n\nI think you are right. It is strange that installation does not trigger an error though, isn't it?\n\n\n> \n> Best regards,\n>     Simon",
    "created_at": "2009-07-26T03:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52416",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:38 SimonKing]:
> Replying to [comment:37 wdj]:

...

> 
> > As far as the test, I am running the test on the machine I'm typing on now (an amd64 9.04 ubuntu). It passes all tests. The test will not run on my intel macbook (an import error of some type I think, but I don't remember the error - let me know if you want the exact details and I'll post a message from that machine with the traceback).



```
sage: !/Users/davidjoyner/sagefiles/p_group_cohomology-1.0.1/spkg-check
Traceback (most recent call last):
  File "/Users/davidjoyner/sagefiles/p_group_cohomology-1.0.1/spkg-check", line 99, in <module>
    import pGroupCohomology
ImportError: No module named pGroupCohomology
```

and


```
zeus:~/sagefiles/sage-4.1.1.alpha0 davidjoyner$ ls local/lib/python2.6/site-packages/p_*
ls: local/lib/python2.6/site-packages/p_*: No such file or directory
```



> 
> Yes, please! An import error probably indicates that the package did not built. Of course I wonder why the previous version used to work on your macbook.
>  
> > I give this a positive review. Let me know if you want more testing.
> 
> I guess the Macbook thing should be understood (although, as I mentioned, it was expected that Macbook is a problem).


I think you are right. It is strange that installation does not trigger an error though, isn't it?


> 
> Best regards,
>     Simon



---

archive/issue_comments_052417.json:
```json
{
    "body": "Replying to [comment:39 wdj]:\n> ImportError: No module named pGroupCohomology\n\nOK, then something very fundamental went wrong.\n\n> {{{\n> zeus:~/sagefiles/sage-4.1.1.alpha0 davidjoyner$ ls local/lib/python2.6/site-packages/p_*\n> ls: local/lib/python2.6/site-packages/p_*: No such file or directory\n> }}}\n\nIt should not be p_* but pG*:\nThere is a difference between the name of the spkg (p_group_cohomology-1.0.1) and the name of the extension module it provides (pGroupCohomology, and this is also how the folder in site-packages is called). Compare this with another optional spkg: The spkg is called pil-1.1.6, but the module is PIL.\n\nNevertheless, if it can't be imported then it's bad. Is there any informative error message if you start a sage session and try manually\n\n```\nsage: import pGroupCohomology\n```\n\nthat tells at what point the problem occurs?\n\n> > I guess the Macbook thing should be understood (although, as I mentioned, it was expected that Macbook is a problem).\n> \n> \n> I think you are right. It is strange that installation does not trigger an error though, isn't it?\n\nYes, but sometimes strange things can happen. For example, on one of my machines, the build process failed for no apparent reason; then I tried again, and it simply worked. Is it the same sage installation on which you installed the previous version of our spkg? On my machines, I did not experience a conflict when installing one version after the other; but perhaps this is different on a Macbook?\n\nPlease try to install the package again (with sage -f instead of sage -i), try to save the text output during the build process into a file, and provide a link to it. Perhaps it gives some clue. Perhaps it is useful to remove p_group_cohomology*.spkg from SAGE_ROOT/spkg/optional before doing the installation: In that way it is forced to download the sources again.\n\nThere is the possibility that it \"simply works\" when you try the installation a second time. If not: You might remove SAGE_ROOT/local/lib/python2.6/site-packages/pGroupCohomoloy* and try again (this is to avoid conflict with previous builds).\n\nUnfortunately I have no access to Macbooks, so, I can't try myself.",
    "created_at": "2009-07-26T04:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52417",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:39 wdj]:
> ImportError: No module named pGroupCohomology

OK, then something very fundamental went wrong.

> {{{
> zeus:~/sagefiles/sage-4.1.1.alpha0 davidjoyner$ ls local/lib/python2.6/site-packages/p_*
> ls: local/lib/python2.6/site-packages/p_*: No such file or directory
> }}}

It should not be p_* but pG*:
There is a difference between the name of the spkg (p_group_cohomology-1.0.1) and the name of the extension module it provides (pGroupCohomology, and this is also how the folder in site-packages is called). Compare this with another optional spkg: The spkg is called pil-1.1.6, but the module is PIL.

Nevertheless, if it can't be imported then it's bad. Is there any informative error message if you start a sage session and try manually

```
sage: import pGroupCohomology
```

that tells at what point the problem occurs?

> > I guess the Macbook thing should be understood (although, as I mentioned, it was expected that Macbook is a problem).
> 
> 
> I think you are right. It is strange that installation does not trigger an error though, isn't it?

Yes, but sometimes strange things can happen. For example, on one of my machines, the build process failed for no apparent reason; then I tried again, and it simply worked. Is it the same sage installation on which you installed the previous version of our spkg? On my machines, I did not experience a conflict when installing one version after the other; but perhaps this is different on a Macbook?

Please try to install the package again (with sage -f instead of sage -i), try to save the text output during the build process into a file, and provide a link to it. Perhaps it gives some clue. Perhaps it is useful to remove p_group_cohomology*.spkg from SAGE_ROOT/spkg/optional before doing the installation: In that way it is forced to download the sources again.

There is the possibility that it "simply works" when you try the installation a second time. If not: You might remove SAGE_ROOT/local/lib/python2.6/site-packages/pGroupCohomoloy* and try again (this is to avoid conflict with previous builds).

Unfortunately I have no access to Macbooks, so, I can't try myself.



---

archive/issue_comments_052418.json:
```json
{
    "body": "Replying to [comment:40 SimonKing]:\n> Replying to [comment:39 wdj]:\n> > ImportError: No module named pGroupCohomology\n> \n> OK, then something very fundamental went wrong.\n> \n> > {{{\n> > zeus:~/sagefiles/sage-4.1.1.alpha0 davidjoyner$ ls local/lib/python2.6/site-packages/p_*\n> > ls: local/lib/python2.6/site-packages/p_*: No such file or directory\n> > }}}\n> \n> It should not be p_* but pG*:\n\n\nThere is definitely nothing related to your package in that directory. \n\n\n> \n> Nevertheless, if it can't be imported then it's bad. Is there any informative error message if you start a sage session and try manually\n> {{{\n> sage: import pGroupCohomology\n> }}}\n> that tells at what point the problem occurs?\n>\n\n\n\n\n```\nsage: import pGroupCohomology\n---------------------------------------------------------------------------\nImportError                               Traceback (most recent call last)\n\n/Users/davidjoyner/.sage/temp/zeus.home/27292/_Users_davidjoyner__sage_init_sage_0.py in <module>()\n\nImportError: No module named pGroupCohomology\n```\n \n\n\n> \n> There is the possibility that it \"simply works\" when you try the installation a second time. If not: You might remove SAGE_ROOT/local/lib/python2.6/site-packages/pGroupCohomoloy* and try again (this is to avoid conflict with previous builds).\n> \n\nYou are absolutely right. I installed it again using sage -f and now it works. The test (spkg-check) ran fine and \neverything looks good (all tests passed on the macbook and the ubuntu machine). Very strange that it needed to be\nreinstalled.",
    "created_at": "2009-07-26T04:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52418",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:40 SimonKing]:
> Replying to [comment:39 wdj]:
> > ImportError: No module named pGroupCohomology
> 
> OK, then something very fundamental went wrong.
> 
> > {{{
> > zeus:~/sagefiles/sage-4.1.1.alpha0 davidjoyner$ ls local/lib/python2.6/site-packages/p_*
> > ls: local/lib/python2.6/site-packages/p_*: No such file or directory
> > }}}
> 
> It should not be p_* but pG*:


There is definitely nothing related to your package in that directory. 


> 
> Nevertheless, if it can't be imported then it's bad. Is there any informative error message if you start a sage session and try manually
> {{{
> sage: import pGroupCohomology
> }}}
> that tells at what point the problem occurs?
>




```
sage: import pGroupCohomology
---------------------------------------------------------------------------
ImportError                               Traceback (most recent call last)

/Users/davidjoyner/.sage/temp/zeus.home/27292/_Users_davidjoyner__sage_init_sage_0.py in <module>()

ImportError: No module named pGroupCohomology
```
 


> 
> There is the possibility that it "simply works" when you try the installation a second time. If not: You might remove SAGE_ROOT/local/lib/python2.6/site-packages/pGroupCohomoloy* and try again (this is to avoid conflict with previous builds).
> 

You are absolutely right. I installed it again using sage -f and now it works. The test (spkg-check) ran fine and 
everything looks good (all tests passed on the macbook and the ubuntu machine). Very strange that it needed to be
reinstalled.



---

archive/issue_comments_052419.json:
```json
{
    "body": "Replying to [comment:41 wdj]:\n...\n> > There is the possibility that it \"simply works\" when you try the installation a second time. If not: You might remove SAGE_ROOT/local/lib/python2.6/site-packages/pGroupCohomoloy* and try again (this is to avoid conflict with previous builds).\n> > \n> \n> You are absolutely right. I installed it again using sage -f and now it works. The test (spkg-check) ran fine and \n> everything looks good (all tests passed on the macbook and the ubuntu machine). Very strange that it needed to be\n> reinstalled.\n\nStrange indeed. As I mentioned, on one of my machines I had to try installation a second time. In this case, I think the problem was that the installation took more than 50% of the memory, but the machine was busy with differnt things, so it failed. But it resulted in an error during the installation, as it should!\n\nDid you delete the copy of the package in spkg/optional before reinstallation? Then I could imagine that the download for the first installation was corrupted. Anyway, good that it works now.\n\nBest regards, \n   Simon",
    "created_at": "2009-07-26T05:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52419",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:41 wdj]:
...
> > There is the possibility that it "simply works" when you try the installation a second time. If not: You might remove SAGE_ROOT/local/lib/python2.6/site-packages/pGroupCohomoloy* and try again (this is to avoid conflict with previous builds).
> > 
> 
> You are absolutely right. I installed it again using sage -f and now it works. The test (spkg-check) ran fine and 
> everything looks good (all tests passed on the macbook and the ubuntu machine). Very strange that it needed to be
> reinstalled.

Strange indeed. As I mentioned, on one of my machines I had to try installation a second time. In this case, I think the problem was that the installation took more than 50% of the memory, but the machine was busy with differnt things, so it failed. But it resulted in an error during the installation, as it should!

Did you delete the copy of the package in spkg/optional before reinstallation? Then I could imagine that the download for the first installation was corrupted. Anyway, good that it works now.

Best regards, 
   Simon



---

archive/issue_comments_052420.json:
```json
{
    "body": "Replying to [comment:42 SimonKing]:\n\n\n> \n> Did you delete the copy of the package in spkg/optional before reinstallation? Then I could imagine that the download for the first installation was corrupted. Anyway, good that it works now.\n> \n\n\nI think sage -f does that automatically.\n\n\nAny more testing to be done? Or is the package ready to be moved from \"need review\" to \"positive review\"?\n\nI don't think optional packages require a vote on sage-devel.\n\n> Best regards, \n>    Simon",
    "created_at": "2009-07-26T11:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52420",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:42 SimonKing]:


> 
> Did you delete the copy of the package in spkg/optional before reinstallation? Then I could imagine that the download for the first installation was corrupted. Anyway, good that it works now.
> 


I think sage -f does that automatically.


Any more testing to be done? Or is the package ready to be moved from "need review" to "positive review"?

I don't think optional packages require a vote on sage-devel.

> Best regards, 
>    Simon



---

archive/issue_comments_052421.json:
```json
{
    "body": "Replying to [comment:43 wdj]:\n> > Did you delete the copy of the package in spkg/optional before reinstallation? Then I could imagine that the download for the first installation was corrupted. Anyway, good that it works now.\n>  \n> I think sage -f does that automatically.\n\nAs much as I know, sage -f of course does a re-installation. But *if* SAGE_ROOT/spkg/optional/ contains a file xyz.spkg then it will use this file for re-installation; it will not attempt to download a new copy of that file.\n\n> Any more testing to be done? Or is the package ready to be moved from \"need review\" to \"positive review\"?\n\nOn the bright side: It passes testing on various platforms, including some for which this is a good surprise. In addition, using the package I did a lot of computations that went smoothly, reproduce known results, but go much beyond the previously known.\n\nSo, from this point of view, I think it is OK to move it to \"positive review\" (but I think *you* should do, because you are the reviewer, and don't forget to insert your name in the \"Reviewer\" field).\n\nOn the dark side: Apparently nobody here has access to a computer with Motorola chips. Martin Albrecht said it is extremely likely that our package will not work on Motorola. \n\nI am about to write an email to William with you as Cc, and ask whether he can provide testing on Motorola, and if not, whether it is crucial for an optional package being tested on it.\n\nBest regards, \n    Simon",
    "created_at": "2009-07-26T13:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52421",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:43 wdj]:
> > Did you delete the copy of the package in spkg/optional before reinstallation? Then I could imagine that the download for the first installation was corrupted. Anyway, good that it works now.
>  
> I think sage -f does that automatically.

As much as I know, sage -f of course does a re-installation. But *if* SAGE_ROOT/spkg/optional/ contains a file xyz.spkg then it will use this file for re-installation; it will not attempt to download a new copy of that file.

> Any more testing to be done? Or is the package ready to be moved from "need review" to "positive review"?

On the bright side: It passes testing on various platforms, including some for which this is a good surprise. In addition, using the package I did a lot of computations that went smoothly, reproduce known results, but go much beyond the previously known.

So, from this point of view, I think it is OK to move it to "positive review" (but I think *you* should do, because you are the reviewer, and don't forget to insert your name in the "Reviewer" field).

On the dark side: Apparently nobody here has access to a computer with Motorola chips. Martin Albrecht said it is extremely likely that our package will not work on Motorola. 

I am about to write an email to William with you as Cc, and ask whether he can provide testing on Motorola, and if not, whether it is crucial for an optional package being tested on it.

Best regards, 
    Simon



---

archive/issue_comments_052422.json:
```json
{
    "body": "William reported one doc test error on PowerPC OS X. Thank you for testing!\n\nAnd I found a severe memory leak in my favourite benchmark: The cohomology of the groups of order 64. This is:\n\n```\nsage: from pGroupCohomology import CohomologyRing\nsage: tmp_root = tmp_filename()\nsage: CohomologyRing.set_user_db(tmp_root)\nsage: for i in range(1,268):\n....:     H = CohomologyRing.user_db(64,i, websource=False) # Compute the ring from scratch\n....:     H.make()\n....:     K = CohomologyRing(64,i)  # Compare with the ring in the data base\n....:     if H is K:\n....:         raise RuntimeError, \"H is K\" # 'public' and 'private' data base are different...\n....:     if H!=K:\n....:         raise RuntimeError, \"H != K\" # ... but they contain the same data.\n```\n\n\nThe above used to run in about 45 minutes. But now, the computation time and the memory consumption increased dramatically. Currently I try to find out whether the problem is the change from sage-4.0 to sage-4.1 or the change from p_group_cohomology-1.0 to  p_group_cohomology-1.0.1; probably it is the latter. \n\nSo: Until I solved the problem (famous last words...) I give it the tag \"needs work\".",
    "created_at": "2009-07-27T21:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52422",
    "user": "https://github.com/simon-king-jena"
}
```

William reported one doc test error on PowerPC OS X. Thank you for testing!

And I found a severe memory leak in my favourite benchmark: The cohomology of the groups of order 64. This is:

```
sage: from pGroupCohomology import CohomologyRing
sage: tmp_root = tmp_filename()
sage: CohomologyRing.set_user_db(tmp_root)
sage: for i in range(1,268):
....:     H = CohomologyRing.user_db(64,i, websource=False) # Compute the ring from scratch
....:     H.make()
....:     K = CohomologyRing(64,i)  # Compare with the ring in the data base
....:     if H is K:
....:         raise RuntimeError, "H is K" # 'public' and 'private' data base are different...
....:     if H!=K:
....:         raise RuntimeError, "H != K" # ... but they contain the same data.
```


The above used to run in about 45 minutes. But now, the computation time and the memory consumption increased dramatically. Currently I try to find out whether the problem is the change from sage-4.0 to sage-4.1 or the change from p_group_cohomology-1.0 to  p_group_cohomology-1.0.1; probably it is the latter. 

So: Until I solved the problem (famous last words...) I give it the tag "needs work".



---

archive/issue_comments_052423.json:
```json
{
    "body": "I did an update of my package. You can install it by\n\n```\nsage -f http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.0.2.spkg\n```\n\nor without the http stuff as soon as William has moved it into the repository of experimental spkgs.\n\nI am not sure if it is reasonable to have yet another version number (1.0.2 instead of 1.0.1). Opinions?\n\nHere are my comments and questions on the new version:\n\n* In this version, I finally use _sig_on/_sig_off. Hence, you should be able to keyboard interrupt a lengthy computation of a projective resolution (which was impossible before). Question:\n  * I know that _sig_on and _sig_off must come in pairs. So, if a method has _sig_on, then _sig_off should be used before return. But is it also required to have _sig_off before leaving the method by raising an error?\n\n* As usual, you can run the test suite if before installation you do `export SAGE_CHECK=1`.\n\n* Install and test is fine on \n  * AMD Athlon(tm) 64 Processor 3700+, GNU Linux openSUSE 10.2 (X86-64), gcc version 4.2.1, sage 4.0.2\n  * Intel(R) Core(TM)2 CPU, GNU Linux openSUSE 11.0, gcc version 4.3.1, sage 4.1\n\n Please test on as many platforms as possible!\n\n* In addition to the test suite, I did the following test, that revealed a time regression that is now fixed:\n  {{{\nsage: from pGroupCohomology import CohomologyRing\nsage: tmp_root = tmp_filename()\nsage: CohomologyRing.set_user_db(tmp_root)\nsage: for i in range(1,268):  # testing the performance\n....:     H = CohomologyRing.user_db(64,i,options='nosave',websource=False)\n....:     H.make()\n....:     save(H, H.autosave_name())\nsage: for i in range(1,268): # unit tests\n....:     H = CohomologyRing.user_db(64,i)\n....:     if not H.completed:\n....:         raise RuntimeError,\"Forgot to save!\"\n....:     K = CohomologyRing(64,i)\n....:     if H is K:\n....:         raise RuntimeError, \"H is K\"\n....:     if H!=K:\n....:         raise RuntimeError, \"H!=K\"\n   }}}\n* On the AMD Athlon, the above performance test takes roughly 25 CPU minutes or 45 \"real\" minutes.\n\n* On the Intel Core 2, it is only about 19 CPU minutes or 37 \"real\" minutes. As far as I know, this is a new **world record** for the cohomology computation of the groups of order 64.\n\n**__News and Changes__**\n\n* Fixing a severe time regression\n* Fixing some error that William revealed by the doc tests on PPC Macbook\n* Fixing a minor memory leak\n* Using _sig_on/_sig_off\n* My Email address has changed, and I provide the new address in the package.\n\nIf no objections arise from the version number and _sig_off questions, then I think it is ready for review!",
    "created_at": "2009-07-30T11:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52423",
    "user": "https://github.com/simon-king-jena"
}
```

I did an update of my package. You can install it by

```
sage -f http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.0.2.spkg
```

or without the http stuff as soon as William has moved it into the repository of experimental spkgs.

I am not sure if it is reasonable to have yet another version number (1.0.2 instead of 1.0.1). Opinions?

Here are my comments and questions on the new version:

* In this version, I finally use _sig_on/_sig_off. Hence, you should be able to keyboard interrupt a lengthy computation of a projective resolution (which was impossible before). Question:
  * I know that _sig_on and _sig_off must come in pairs. So, if a method has _sig_on, then _sig_off should be used before return. But is it also required to have _sig_off before leaving the method by raising an error?

* As usual, you can run the test suite if before installation you do `export SAGE_CHECK=1`.

* Install and test is fine on 
  * AMD Athlon(tm) 64 Processor 3700+, GNU Linux openSUSE 10.2 (X86-64), gcc version 4.2.1, sage 4.0.2
  * Intel(R) Core(TM)2 CPU, GNU Linux openSUSE 11.0, gcc version 4.3.1, sage 4.1

 Please test on as many platforms as possible!

* In addition to the test suite, I did the following test, that revealed a time regression that is now fixed:
  {{{
sage: from pGroupCohomology import CohomologyRing
sage: tmp_root = tmp_filename()
sage: CohomologyRing.set_user_db(tmp_root)
sage: for i in range(1,268):  # testing the performance
....:     H = CohomologyRing.user_db(64,i,options='nosave',websource=False)
....:     H.make()
....:     save(H, H.autosave_name())
sage: for i in range(1,268): # unit tests
....:     H = CohomologyRing.user_db(64,i)
....:     if not H.completed:
....:         raise RuntimeError,"Forgot to save!"
....:     K = CohomologyRing(64,i)
....:     if H is K:
....:         raise RuntimeError, "H is K"
....:     if H!=K:
....:         raise RuntimeError, "H!=K"
   }}}
* On the AMD Athlon, the above performance test takes roughly 25 CPU minutes or 45 "real" minutes.

* On the Intel Core 2, it is only about 19 CPU minutes or 37 "real" minutes. As far as I know, this is a new **world record** for the cohomology computation of the groups of order 64.

**__News and Changes__**

* Fixing a severe time regression
* Fixing some error that William revealed by the doc tests on PPC Macbook
* Fixing a minor memory leak
* Using _sig_on/_sig_off
* My Email address has changed, and I provide the new address in the package.

If no objections arise from the version number and _sig_off questions, then I think it is ready for review!



---

archive/issue_comments_052424.json:
```json
{
    "body": "I'll wait until the PPC Macbook is checked since that was the most serious problem with the last version.",
    "created_at": "2009-07-30T14:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52424",
    "user": "https://github.com/wdjoyner"
}
```

I'll wait until the PPC Macbook is checked since that was the most serious problem with the last version.



---

archive/issue_comments_052425.json:
```json
{
    "body": "Replying to [comment:47 wdj]:\n> I'll wait until the PPC Macbook is checked since that was the most serious problem with the last version.\n\nI am sorry for the invention of a \"PPC Macbook\". William just pointed out to me that there is no \"PPC Macbook\", and that the error occured on a power pc with OS X. Anyway, I hope that it is be fixed...",
    "created_at": "2009-07-30T15:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52425",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:47 wdj]:
> I'll wait until the PPC Macbook is checked since that was the most serious problem with the last version.

I am sorry for the invention of a "PPC Macbook". William just pointed out to me that there is no "PPC Macbook", and that the error occured on a power pc with OS X. Anyway, I hope that it is be fixed...



---

archive/issue_comments_052426.json:
```json
{
    "body": "Replying to [comment:48 SimonKing]:\n> I am sorry for the invention of a \"PPC Macbook\". William just pointed out to me that there is no \"PPC Macbook\", and that the error occured on a power pc with OS X. Anyway, I hope that it is be fixed...\n\nAparently, it is!!\n\nWilliam wrote to me off list:\n  In fact, the install finished on OS X 10.4 PPC  and all tests pass! (Total time: 85.98 minutes).\n\n\nIt is of course a good news that the tests pass; perhaps someone can test it with OS X 10.5\n\nBut at first I wondered why the tests took so long! I never had a machine where the test suite took more than 20 minutes. However, William explained the PowerPC OS X is known to be slow.\n\nAs far as I understood, William is currently testing on various platforms, so I hope that soon we will have an overview of what is possible.",
    "created_at": "2009-07-30T21:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52426",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:48 SimonKing]:
> I am sorry for the invention of a "PPC Macbook". William just pointed out to me that there is no "PPC Macbook", and that the error occured on a power pc with OS X. Anyway, I hope that it is be fixed...

Aparently, it is!!

William wrote to me off list:
  In fact, the install finished on OS X 10.4 PPC  and all tests pass! (Total time: 85.98 minutes).


It is of course a good news that the tests pass; perhaps someone can test it with OS X 10.5

But at first I wondered why the tests took so long! I never had a machine where the test suite took more than 20 minutes. However, William explained the PowerPC OS X is known to be slow.

As far as I understood, William is currently testing on various platforms, so I hope that soon we will have an overview of what is possible.



---

archive/issue_comments_052427.json:
```json
{
    "body": "Installed fine, passed sage -testall and spkg-check on an amd64 ubuntu 9.04 machine.",
    "created_at": "2009-07-31T09:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52427",
    "user": "https://github.com/wdjoyner"
}
```

Installed fine, passed sage -testall and spkg-check on an amd64 ubuntu 9.04 machine.



---

archive/issue_comments_052428.json:
```json
{
    "body": "Replying to [comment:50 wdj]:\n> Installed fine, passed sage -testall and spkg-check on an amd64 ubuntu 9.04 machine.\n\nThank you very much!\n\nBy the way, I meanwhile learned that it is not needed to start spkg-check manually. Probably the easiest way to test the package is to do\n`export SAGE_CHECK=1` before installing the package, since spkg-check will then be started automatically.\n\nSo, according to reports of David Joyner, William Stein and myself, we currently have install tests pass on\n- Amd64, Ubuntu 9.0.4 \n- AMD Athlon 64 3700+, openSUSE 10.2 \n- Dual Core AMD Opteron 270, openSUSE 10.2\n- Intel Core Duo, openSUSE 11.0 \n- Intel X7460, Ubuntu 8.04.2 (this is sage.math)\n- PowerPC, OS X 10.4\nand I understood that William is currently doing further tests.\n\nThe previous version used to work on your Macbook, you said. Does the new version as well?\n\nHas anybody tried it under Windows (I mean, via a virtual machine) yet? I have no Windows machine handy.\n\nI expected far more installation problems. The portability is, I guess, mainly due to distutils. So, kudos to whoever developed distutils!",
    "created_at": "2009-07-31T12:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52428",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:50 wdj]:
> Installed fine, passed sage -testall and spkg-check on an amd64 ubuntu 9.04 machine.

Thank you very much!

By the way, I meanwhile learned that it is not needed to start spkg-check manually. Probably the easiest way to test the package is to do
`export SAGE_CHECK=1` before installing the package, since spkg-check will then be started automatically.

So, according to reports of David Joyner, William Stein and myself, we currently have install tests pass on
- Amd64, Ubuntu 9.0.4 
- AMD Athlon 64 3700+, openSUSE 10.2 
- Dual Core AMD Opteron 270, openSUSE 10.2
- Intel Core Duo, openSUSE 11.0 
- Intel X7460, Ubuntu 8.04.2 (this is sage.math)
- PowerPC, OS X 10.4
and I understood that William is currently doing further tests.

The previous version used to work on your Macbook, you said. Does the new version as well?

Has anybody tried it under Windows (I mean, via a virtual machine) yet? I have no Windows machine handy.

I expected far more installation problems. The portability is, I guess, mainly due to distutils. So, kudos to whoever developed distutils!



---

archive/issue_comments_052429.json:
```json
{
    "body": "William reported (off list) that the package builds on all platforms that he tested (I don't know which these are exactly).",
    "created_at": "2009-07-31T23:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52429",
    "user": "https://github.com/simon-king-jena"
}
```

William reported (off list) that the package builds on all platforms that he tested (I don't know which these are exactly).



---

archive/issue_comments_052430.json:
```json
{
    "body": "That is good new. But here is some bad news:\n\nAll my computers shut down this afternoon due to a big thunder storm which took out all the power. This happened in the middle of a sage -testall. I will have to retest my intel macbook OS 10.4.11 again, if you think it is necessary. Note that in one month Apple will release 10.6, so if 10.5 was already tested, we can probably skip 10.4.11 anyway. In any case, it did pass the spkg-check part of the test on 10.4.11.",
    "created_at": "2009-07-31T23:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52430",
    "user": "https://github.com/wdjoyner"
}
```

That is good new. But here is some bad news:

All my computers shut down this afternoon due to a big thunder storm which took out all the power. This happened in the middle of a sage -testall. I will have to retest my intel macbook OS 10.4.11 again, if you think it is necessary. Note that in one month Apple will release 10.6, so if 10.5 was already tested, we can probably skip 10.4.11 anyway. In any case, it did pass the spkg-check part of the test on 10.4.11.



---

archive/issue_comments_052431.json:
```json
{
    "body": "Replying to [comment:53 wdj]:\n> That is good new. But here is some bad news:\n> \n> All my computers shut down this afternoon due to a big thunder storm which took out all the power.\n\nToo bad! I hope that at least you are safe!\n\n> This happened in the middle of a sage -testall. I will have to retest my intel macbook OS 10.4.11 again, if you think it is necessary. Note that in one month Apple will release 10.6, so if 10.5 was already tested, we can probably skip 10.4.11 anyway. In any case, it did pass the spkg-check part of the test on 10.4.11.\n\nWell, if it passed spkg-check (showing the bottom line \"All tests passed!\"), then the work is done, and a retest wouldn't be needed. `sage -testall` would test all of Sage,  not just our package.\n\nI don't know if William's tests also included Macbook OS 10.4.11; I think it *did* include PowerPC OS X 10.4.\n\nThanks to both you and William for the help on getting the project finally finished!\n\nCheers,\n    Simon",
    "created_at": "2009-07-31T23:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52431",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:53 wdj]:
> That is good new. But here is some bad news:
> 
> All my computers shut down this afternoon due to a big thunder storm which took out all the power.

Too bad! I hope that at least you are safe!

> This happened in the middle of a sage -testall. I will have to retest my intel macbook OS 10.4.11 again, if you think it is necessary. Note that in one month Apple will release 10.6, so if 10.5 was already tested, we can probably skip 10.4.11 anyway. In any case, it did pass the spkg-check part of the test on 10.4.11.

Well, if it passed spkg-check (showing the bottom line "All tests passed!"), then the work is done, and a retest wouldn't be needed. `sage -testall` would test all of Sage,  not just our package.

I don't know if William's tests also included Macbook OS 10.4.11; I think it *did* include PowerPC OS X 10.4.

Thanks to both you and William for the help on getting the project finally finished!

Cheers,
    Simon



---

archive/issue_comments_052432.json:
```json
{
    "body": "Sounds like this can be changed to \"positive review\" as far as including this as an optional package is concerned. Agreed?",
    "created_at": "2009-07-31T23:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52432",
    "user": "https://github.com/wdjoyner"
}
```

Sounds like this can be changed to "positive review" as far as including this as an optional package is concerned. Agreed?



---

archive/issue_comments_052433.json:
```json
{
    "body": "Replying to [comment:55 wdj]:\n> Sounds like this can be changed to \"positive review\" as far as including this as an optional package is concerned. Agreed?\n\nThis time I would not oppose :)\n\nI am currently not aware of serious issues that should be fixed. And everything else should be done in a forthcoming version, on a different ticket.\n\nCheers,\n   Simon",
    "created_at": "2009-08-01T00:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52433",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:55 wdj]:
> Sounds like this can be changed to "positive review" as far as including this as an optional package is concerned. Agreed?

This time I would not oppose :)

I am currently not aware of serious issues that should be fixed. And everything else should be done in a forthcoming version, on a different ticket.

Cheers,
   Simon



---

archive/issue_comments_052434.json:
```json
{
    "body": "This sucker works and passes tests everywhere.",
    "created_at": "2009-08-01T01:21:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52434",
    "user": "https://github.com/williamstein"
}
```

This sucker works and passes tests everywhere.



---

archive/issue_comments_052435.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-01T01:21:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52435",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_015326.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-08-01T01:21:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6491#event-15326"
}
```



---

archive/issue_comments_052436.json:
```json
{
    "body": "Oh, and I posted it to the optional spkg repo.",
    "created_at": "2009-08-01T01:21:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52436",
    "user": "https://github.com/williamstein"
}
```

Oh, and I posted it to the optional spkg repo.



---

archive/issue_comments_052437.json:
```json
{
    "body": "Replying to [comment:57 was]:\n> This sucker works and passes tests everywhere. \n\nThanks again!\n\nI inserted David Joyner and William Stein in the \"Reviewer\" form. I hope you both agree.",
    "created_at": "2009-08-01T01:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6491#issuecomment-52437",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:57 was]:
> This sucker works and passes tests everywhere. 

Thanks again!

I inserted David Joyner and William Stein in the "Reviewer" form. I hope you both agree.

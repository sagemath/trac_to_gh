# Issue 1101: new gap_packages*

archive/issues_001101.json:
```json
{
    "body": "Assignee: wdj\n\nI made a new optional gap_packages* at\nhttp://sage.math.washington.edu/home/wdj/patches/gap_packages-4.4.10_2.spkg\n\nSummary:\n\nThis directory contains several \"official\" and \"undeposited\"\nGAP packages available from \nhttp://www.gap-system.org/Packages/packages.html. They are\nall released under the GPL with the following exception:\n(*) grape contains Brendon McKay's nauty program. \n\nTo load a package, for example grape, into SAGE type\n\nsage: gap('LoadPackage(\"grape\")')\n\nAll these packages come with documentation in the\ndoc or htm subdirectory (e.g., for grape, it would be in\nSAGEHOME/local/lib/gap-4.4.10/pkg/grape/htm). After loading all\nthe packages, you can type gap_reset_workspace()\nso you don't have to reload them again.\n\nA brief description of each package follows:\n\nbraid is a GAP package for computing with braids, covering curves, \nand Hurwitz spaces.\n(Authors: K. Magaard, S. Shpectorov and H. Voelklein)\n\ncrime - package to compute the cohomology ring of finite\np-groups, induced maps, and Massey products.\n(Author: Marcus Bishop)\n\ncryst - Computing with crystallographic groups\n(Authors: Bettina Eick, Franz G\u00e4hler, Werner Nickel)\n\nCTblLib - The GAP Character Table Library\n(Author: Thomas Breuer)\n\nDESIGN is a package for classifying, partitioning and studying block designs.\n(Author: Leonard H. Soicher)\n\nFactInt is a package providing routines for factoring integers, in particular:\n* Pollard's p-1\n* Williams' p+1\n* Elliptic Curves Method (ECM)\n* Continued Fraction Algorithm (CFRAC)\n* Multiple Polynomial Quadratic Sieve (MPQS)\n(Author: Stefan Kohl)\n\nGAPDoc is a package containing a definition of a structure for \nGAP documentation, based on XML. It also contains conversion \nprograms for producing text-, DVI-, PDF- or HTML-versions of such \ndocuments, with hyperlinks if possible.\n(Authors: Frank Luebeck, Max Neunhoeffer)\n\nGRAPE is a package for computing with graphs and groups, and is primarily \ndesigned for constructing and analysing graphs related to groups, \nfinite geometries, and designs.\n(Author: Leonard H. Soicher)\n\nHAP (Homological Algebra Programming) is a GAP package \nproviding some functions for group cohomology computation. \n(Author: Graham Ellis)\n\nHAPcryst - an extension package for HAP, which allows for\ngroup cohomology computation for a wider class of groups.\n(Author: Marc Roeder)\n\nLAGUNA - this package provides functionality for calculation of the \nnormalized unit group of the modular group algebra of the finite \np-group and for investigation of Lie algebra associated with group \nalgebras and other associative algebras.\n(Authors :Victor Bovdi, Alexander Konovalov, Richard Rossmanith, \nCsaba Schneider)\n\npolymake - an interface with the (standalone) polymake program\nused by HAPcryst. \n(Author: Marc Roeder)\n\nSONATA (\"System Of Nearrings And Their Applications\") is a package \nwhich constructs finite nearrings and related objects.\n(Authors: Erhard Aichinger, Franz Binder, J\u00fcrgen Ecker, Peter Mayr, \nChristof Noebauer)\n\nTORIC is a GAP package for computing with toric varieties.\n(Author: David Joyner)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1101\n\n",
    "created_at": "2007-11-04T22:01:06Z",
    "labels": [
        "packages: standard",
        "minor",
        "enhancement"
    ],
    "title": "new gap_packages*",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1101",
    "user": "wdj"
}
```
Assignee: wdj

I made a new optional gap_packages* at
http://sage.math.washington.edu/home/wdj/patches/gap_packages-4.4.10_2.spkg

Summary:

This directory contains several "official" and "undeposited"
GAP packages available from 
http://www.gap-system.org/Packages/packages.html. They are
all released under the GPL with the following exception:
(*) grape contains Brendon McKay's nauty program. 

To load a package, for example grape, into SAGE type

sage: gap('LoadPackage("grape")')

All these packages come with documentation in the
doc or htm subdirectory (e.g., for grape, it would be in
SAGEHOME/local/lib/gap-4.4.10/pkg/grape/htm). After loading all
the packages, you can type gap_reset_workspace()
so you don't have to reload them again.

A brief description of each package follows:

braid is a GAP package for computing with braids, covering curves, 
and Hurwitz spaces.
(Authors: K. Magaard, S. Shpectorov and H. Voelklein)

crime - package to compute the cohomology ring of finite
p-groups, induced maps, and Massey products.
(Author: Marcus Bishop)

cryst - Computing with crystallographic groups
(Authors: Bettina Eick, Franz Gähler, Werner Nickel)

CTblLib - The GAP Character Table Library
(Author: Thomas Breuer)

DESIGN is a package for classifying, partitioning and studying block designs.
(Author: Leonard H. Soicher)

FactInt is a package providing routines for factoring integers, in particular:
* Pollard's p-1
* Williams' p+1
* Elliptic Curves Method (ECM)
* Continued Fraction Algorithm (CFRAC)
* Multiple Polynomial Quadratic Sieve (MPQS)
(Author: Stefan Kohl)

GAPDoc is a package containing a definition of a structure for 
GAP documentation, based on XML. It also contains conversion 
programs for producing text-, DVI-, PDF- or HTML-versions of such 
documents, with hyperlinks if possible.
(Authors: Frank Luebeck, Max Neunhoeffer)

GRAPE is a package for computing with graphs and groups, and is primarily 
designed for constructing and analysing graphs related to groups, 
finite geometries, and designs.
(Author: Leonard H. Soicher)

HAP (Homological Algebra Programming) is a GAP package 
providing some functions for group cohomology computation. 
(Author: Graham Ellis)

HAPcryst - an extension package for HAP, which allows for
group cohomology computation for a wider class of groups.
(Author: Marc Roeder)

LAGUNA - this package provides functionality for calculation of the 
normalized unit group of the modular group algebra of the finite 
p-group and for investigation of Lie algebra associated with group 
algebras and other associative algebras.
(Authors :Victor Bovdi, Alexander Konovalov, Richard Rossmanith, 
Csaba Schneider)

polymake - an interface with the (standalone) polymake program
used by HAPcryst. 
(Author: Marc Roeder)

SONATA ("System Of Nearrings And Their Applications") is a package 
which constructs finite nearrings and related objects.
(Authors: Erhard Aichinger, Franz Binder, Jürgen Ecker, Peter Mayr, 
Christof Noebauer)

TORIC is a GAP package for computing with toric varieties.
(Author: David Joyner)


Issue created by migration from https://trac.sagemath.org/ticket/1101





---

archive/issue_comments_006663.json:
```json
{
    "body": "NOTE to self: when putting this package into the optional repo, be sure\nto modify spkg-install to touch $SAGE_LOCAL/bin/gap_stamp",
    "created_at": "2007-11-04T22:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1101#issuecomment-6663",
    "user": "was"
}
```

NOTE to self: when putting this package into the optional repo, be sure
to modify spkg-install to touch $SAGE_LOCAL/bin/gap_stamp



---

archive/issue_comments_006664.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-22T15:14:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1101#issuecomment-6664",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006665.json:
```json
{
    "body": "The optional spkg has been put in the repo and mirrored out.",
    "created_at": "2007-12-22T15:14:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1101#issuecomment-6665",
    "user": "mabshoff"
}
```

The optional spkg has been put in the repo and mirrored out.

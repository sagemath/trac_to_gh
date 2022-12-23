# Issue 8251: traceback when computing E.torsion_subgroup() for an elliptic curve E

archive/issues_008251.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  robertwb was\n\nIt's possible to get a traceback for some dumb reason in some cases when computing the torsion subgroup of an elliptic curve:\n\n```\n...\nTraceback (most recent call last):           for K in J.unramified_outside([i],3):\n  File \"\", line 1, in <module>\n    \n  File \"/tmp/tmpSAW9n5/___code___.py\", line 6, in <module>\n    T=E.torsion_subgroup()\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 3515, in torsion_subgroup\n    self.__torsion_subgroup = ell_torsion.EllipticCurveTorsionSubgroup(self, algorithm)\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_torsion.py\", line 159, in __init__\n    if self.__K is RationalField() and algorithm in pari_torsion_algorithms:\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/rational_field.py\", line 208, in __init__\n    self._assign_names(('x',),normalize=False) # ???\n  File \"parent_gens.pyx\", line 327, in sage.structure.parent_gens.ParentWithGens._assign_names (sage/structure/parent_gens.c:2854)\n  File \"category_object.pyx\", line 336, in sage.structure.category_object.CategoryObject._assign_names (sage/structure/category_object.c:3286)\nValueError: variable names cannot be changed after object creation.\n```\n\n\nThe above is caused by running this script:\n\n```\nJ=JonesDatabase()\nP=Primes()\nfor E in cremona_optimal_curves([0..50]):\n    T=E.torsion_subgroup()\n    i=E.conductor()\n    if i.is_prime():\n       for K in J.unramified_outside([i],3):\n                F=E.base_extend(K)\n                T_1=F.torsion_subgroup() \n\n                if T != T_1:\n                    E.label();\n                    K.is_galois();\n                    T;\n                    T_1;\n    else:\n        j=2 \n        while j < i :\n            if j.is_prime():\n                n=i/j\n                if n.is_integral():\n                    for K in J.unramified_outside([j],3):\n                        F=E.base_extend(K)\n\n                        T_1=F.torsion_subgroup() \n                        if T != T_1:\n                            E.label();\n\n                            K.is_galois();\n                            T;\n                            T_1;\n            j=P.next(j)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8251\n\n",
    "created_at": "2010-02-12T15:29:39Z",
    "labels": [
        "elliptic curves",
        "critical",
        "bug"
    ],
    "title": "traceback when computing E.torsion_subgroup() for an elliptic curve E",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8251",
    "user": "was"
}
```
Assignee: cremona

CC:  robertwb was

It's possible to get a traceback for some dumb reason in some cases when computing the torsion subgroup of an elliptic curve:

```
...
Traceback (most recent call last):           for K in J.unramified_outside([i],3):
  File "", line 1, in <module>
    
  File "/tmp/tmpSAW9n5/___code___.py", line 6, in <module>
    T=E.torsion_subgroup()
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 3515, in torsion_subgroup
    self.__torsion_subgroup = ell_torsion.EllipticCurveTorsionSubgroup(self, algorithm)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_torsion.py", line 159, in __init__
    if self.__K is RationalField() and algorithm in pari_torsion_algorithms:
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/rings/rational_field.py", line 208, in __init__
    self._assign_names(('x',),normalize=False) # ???
  File "parent_gens.pyx", line 327, in sage.structure.parent_gens.ParentWithGens._assign_names (sage/structure/parent_gens.c:2854)
  File "category_object.pyx", line 336, in sage.structure.category_object.CategoryObject._assign_names (sage/structure/category_object.c:3286)
ValueError: variable names cannot be changed after object creation.
```


The above is caused by running this script:

```
J=JonesDatabase()
P=Primes()
for E in cremona_optimal_curves([0..50]):
    T=E.torsion_subgroup()
    i=E.conductor()
    if i.is_prime():
       for K in J.unramified_outside([i],3):
                F=E.base_extend(K)
                T_1=F.torsion_subgroup() 

                if T != T_1:
                    E.label();
                    K.is_galois();
                    T;
                    T_1;
    else:
        j=2 
        while j < i :
            if j.is_prime():
                n=i/j
                if n.is_integral():
                    for K in J.unramified_outside([j],3):
                        F=E.base_extend(K)

                        T_1=F.torsion_subgroup() 
                        if T != T_1:
                            E.label();

                            K.is_galois();
                            T;
                            T_1;
            j=P.next(j)
```


Issue created by migration from https://trac.sagemath.org/ticket/8251





---

archive/issue_comments_072988.json:
```json
{
    "body": "This may be related to #7930.  In both cases, a sequence of elliptic curves and number fields and reduction mod primes is carried out, and something is getting confused about all the finite fields which getting created.\n\nIt would be a great help if we could simplify the script which causes this.  There's an outer look through curves and an inner loop through certain fields, depending on the curve, and then the torsion of the curve over that field is computed.  I'll try to do that.",
    "created_at": "2010-02-13T18:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-72988",
    "user": "cremona"
}
```

This may be related to #7930.  In both cases, a sequence of elliptic curves and number fields and reduction mod primes is carried out, and something is getting confused about all the finite fields which getting created.

It would be a great help if we could simplify the script which causes this.  There's an outer look through curves and an inner loop through certain fields, depending on the curve, and then the torsion of the curve over that field is computed.  I'll try to do that.



---

archive/issue_comments_072989.json:
```json
{
    "body": "This error has (a) nothing to do with elliptic curve code and (b) nothing to do with number fields at all!\n\nIt is arising because in several places in Sage source code the field of rational numbers is referred to as `RationalField()` instead of as QQ.  This should not matter, since the `RationalField()` call is supposed to return the unique object of its class, which is pre-assigned to QQ, but apparently sometimes it does go through the process of running the code in `RationalField.__init__()`.  That code contains the mysterious line\n\n```\n        self._assign_names(('x',),normalize=False) # ???\n```\n\n-- note that some one (not me) has added those ??? -- I cannot see any reason for assigning any \"names\" to QQ.  It is this call to the _assign_names() function which sometimes raises the error.  I do not know why it only happens sometimes.\n\nIt might therefore be a good idea to change the title of this ticket.  I will ask other people for their opinion.  Robert?  (You added the ???)  William?  (You added the assign_names line!)\n\nI would like to try commenting out that line and testing the entire Sage library.",
    "created_at": "2010-06-25T07:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-72989",
    "user": "cremona"
}
```

This error has (a) nothing to do with elliptic curve code and (b) nothing to do with number fields at all!

It is arising because in several places in Sage source code the field of rational numbers is referred to as `RationalField()` instead of as QQ.  This should not matter, since the `RationalField()` call is supposed to return the unique object of its class, which is pre-assigned to QQ, but apparently sometimes it does go through the process of running the code in `RationalField.__init__()`.  That code contains the mysterious line

```
        self._assign_names(('x',),normalize=False) # ???
```

-- note that some one (not me) has added those ??? -- I cannot see any reason for assigning any "names" to QQ.  It is this call to the _assign_names() function which sometimes raises the error.  I do not know why it only happens sometimes.

It might therefore be a good idea to change the title of this ticket.  I will ask other people for their opinion.  Robert?  (You added the ???)  William?  (You added the assign_names line!)

I would like to try commenting out that line and testing the entire Sage library.



---

archive/issue_comments_072990.json:
```json
{
    "body": "Easier to reproduce.\n\n\n```\nsage: RationalField()\nRational Field\nsage: list(JonesDatabase().unramified_outside([3], 3))\n[Number Field in a with defining polynomial x^3 - 3*x + 1, Number Field in a with defining polynomial x^3 - 3]\nsage: RationalField()\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (436, 0))\n\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/Users/sekhon/<ipython console> in <module>()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/rings/rational_field.pyc in __init__(self)\n    212         print id(self)\n    213         ParentWithGens.__init__(self, self, category = Fields())\n--> 214         self._assign_names(('x',),normalize=False) # ???\n    215         self._populate_coercion_lists_(element_constructor=rational.Rational, init_no_parent=True)\n    216 \n\n/Applications/sage/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens._assign_names (sage/structure/parent_gens.c:2869)()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/structure/category_object.so in sage.structure.category_object.CategoryObject._assign_names (sage/structure/category_object.c:3287)()\n\nValueError: variable names cannot be changed after object creation.\n\n```\n",
    "created_at": "2010-06-25T20:49:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-72990",
    "user": "robertwb"
}
```

Easier to reproduce.


```
sage: RationalField()
Rational Field
sage: list(JonesDatabase().unramified_outside([3], 3))
[Number Field in a with defining polynomial x^3 - 3*x + 1, Number Field in a with defining polynomial x^3 - 3]
sage: RationalField()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (436, 0))

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/sekhon/<ipython console> in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/rings/rational_field.pyc in __init__(self)
    212         print id(self)
    213         ParentWithGens.__init__(self, self, category = Fields())
--> 214         self._assign_names(('x',),normalize=False) # ???
    215         self._populate_coercion_lists_(element_constructor=rational.Rational, init_no_parent=True)
    216 

/Applications/sage/local/lib/python2.6/site-packages/sage/structure/parent_gens.so in sage.structure.parent_gens.ParentWithGens._assign_names (sage/structure/parent_gens.c:2869)()

/Applications/sage/local/lib/python2.6/site-packages/sage/structure/category_object.so in sage.structure.category_object.CategoryObject._assign_names (sage/structure/category_object.c:3287)()

ValueError: variable names cannot be changed after object creation.

```




---

archive/issue_comments_072991.json:
```json
{
    "body": "Changing assignee from cremona to nthiery.",
    "created_at": "2010-06-25T21:01:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-72991",
    "user": "robertwb"
}
```

Changing assignee from cremona to nthiery.



---

archive/issue_comments_072992.json:
```json
{
    "body": "Changing component from elliptic curves to categories.",
    "created_at": "2010-06-25T21:01:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-72992",
    "user": "robertwb"
}
```

Changing component from elliptic curves to categories.



---

archive/issue_comments_072993.json:
```json
{
    "body": "Even easier to reproduce:\n\n\n```\nRationalField()\nx = load(SAGE_ROOT + \"/data/jones/jones.sobj\")\nRationalField()\n```\n",
    "created_at": "2011-01-08T21:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-72993",
    "user": "wjp"
}
```

Even easier to reproduce:


```
RationalField()
x = load(SAGE_ROOT + "/data/jones/jones.sobj")
RationalField()
```




---

archive/issue_comments_072994.json:
```json
{
    "body": "As far as I can tell, `jones.sobj` contains a `RationalField` with `_names` equal to `'x'`, while in current versions of sage, `QQ._names` equals `('x',)`.",
    "created_at": "2011-01-08T21:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-72994",
    "user": "wjp"
}
```

As far as I can tell, `jones.sobj` contains a `RationalField` with `_names` equal to `'x'`, while in current versions of sage, `QQ._names` equals `('x',)`.



---

archive/issue_comments_072995.json:
```json
{
    "body": "As suggested by William, I've converted the pickle `data/jones/jones.sobj` to be less dependent on the version of Sage by storing the polynomials as lists of python ints rather than as actual polynomials. This solves the problem encountered in this ticket, and also prevents similar things in the future.\n\nI'll try to create a new jones spkg soon, but for now I'm attaching the sage patch and the updated `data/jones/jones.sobj`.\n\nThere was also a new polynomial on John Jones' webpage, so the contents of this new sobj are slightly different than the previous version of the database.",
    "created_at": "2011-01-09T06:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-72995",
    "user": "wjp"
}
```

As suggested by William, I've converted the pickle `data/jones/jones.sobj` to be less dependent on the version of Sage by storing the polynomials as lists of python ints rather than as actual polynomials. This solves the problem encountered in this ticket, and also prevents similar things in the future.

I'll try to create a new jones spkg soon, but for now I'm attaching the sage patch and the updated `data/jones/jones.sobj`.

There was also a new polynomial on John Jones' webpage, so the contents of this new sobj are slightly different than the previous version of the database.



---

archive/issue_comments_072996.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-01-09T06:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-72996",
    "user": "wjp"
}
```

Attachment



---

archive/issue_comments_072997.json:
```json
{
    "body": "Attachment\n\nIt would also be possible to fix unpickling the old sobj (and any other potentially broken old pickles) by creating an empty `RationalField.__setstate__(state)`.",
    "created_at": "2011-01-09T23:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-72997",
    "user": "wjp"
}
```

Attachment

It would also be possible to fix unpickling the old sobj (and any other potentially broken old pickles) by creating an empty `RationalField.__setstate__(state)`.



---

archive/issue_comments_072998.json:
```json
{
    "body": "See https://groups.google.com/forum/#!topic/sage-devel/U1dsVFP-2PA  Is this still even relevant?  I assume the database exists somewhere still.",
    "created_at": "2020-10-08T12:47:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-72998",
    "user": "kcrisman"
}
```

See https://groups.google.com/forum/#!topic/sage-devel/U1dsVFP-2PA  Is this still even relevant?  I assume the database exists somewhere still.



---

archive/issue_comments_072999.json:
```json
{
    "body": "Replying to [comment:13 kcrisman]:\n> See https://groups.google.com/forum/#!topic/sage-devel/U1dsVFP-2PA  Is this still even relevant?  I assume the database exists somewhere still.\n\nhttps://hobbes.la.asu.edu/NFDB/",
    "created_at": "2020-10-08T12:50:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-72999",
    "user": "cremona"
}
```

Replying to [comment:13 kcrisman]:
> See https://groups.google.com/forum/#!topic/sage-devel/U1dsVFP-2PA  Is this still even relevant?  I assume the database exists somewhere still.

https://hobbes.la.asu.edu/NFDB/



---

archive/issue_comments_073000.json:
```json
{
    "body": "John, does that mean the bug in question still is a problem?  I only updated this since *you* mentioned it in the sage-devel thread :-) hope the downgrade is okay.\n\nI just risked destroying my Sage build (computer OS upgrade) to try this out, but I think it might not be a problem any longer.\n\n\n```\nsage: RationalField()\nRational Field\nsage: from sage.env import SAGE_SHARE\nsage: x = load(os.path.join(SAGE_SHARE, 'jones', 'jones.sobj'))\nsage: RationalField()\nRational Field\n```\n\n\nDo you think that is the 'modern' equivalent of comment:5?  For what it's worth, apparently I `sage -i' and loaded the database correctly:\n\n```\nsage: list(JonesDatabase().unramified_outside([3], 3))\n[Number Field in a with defining polynomial x^3 - 3*x + 1,\n Number Field in a with defining polynomial x^3 - 3]\n```\n",
    "created_at": "2020-10-08T15:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-73000",
    "user": "kcrisman"
}
```

John, does that mean the bug in question still is a problem?  I only updated this since *you* mentioned it in the sage-devel thread :-) hope the downgrade is okay.

I just risked destroying my Sage build (computer OS upgrade) to try this out, but I think it might not be a problem any longer.


```
sage: RationalField()
Rational Field
sage: from sage.env import SAGE_SHARE
sage: x = load(os.path.join(SAGE_SHARE, 'jones', 'jones.sobj'))
sage: RationalField()
Rational Field
```


Do you think that is the 'modern' equivalent of comment:5?  For what it's worth, apparently I `sage -i' and loaded the database correctly:

```
sage: list(JonesDatabase().unramified_outside([3], 3))
[Number Field in a with defining polynomial x^3 - 3*x + 1,
 Number Field in a with defining polynomial x^3 - 3]
```




---

archive/issue_comments_073001.json:
```json
{
    "body": "I know nothing about the bug, and have never installed the optional Jones-Roberts database.  I only posted here to answer the question about whether that database still exists.  It does, and is being maintained, as it can do some things not yet available in the LMFDB though John Jones also maintains the number field collection there.\n\nIt seems that you haves tested that the package database_jones_numfield does work, and I am also now installing it....done, and I see no problem.\n\nLet's close this issue.",
    "created_at": "2020-10-08T16:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-73001",
    "user": "cremona"
}
```

I know nothing about the bug, and have never installed the optional Jones-Roberts database.  I only posted here to answer the question about whether that database still exists.  It does, and is being maintained, as it can do some things not yet available in the LMFDB though John Jones also maintains the number field collection there.

It seems that you haves tested that the package database_jones_numfield does work, and I am also now installing it....done, and I see no problem.

Let's close this issue.



---

archive/issue_comments_073002.json:
```json
{
    "body": "Did you try the `RationalField()` before and after using it like in comment:15?  I agree that we can close it if that succeeds.  I only assumed you knew something about it since you were already on this ticket.",
    "created_at": "2020-10-08T16:35:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-73002",
    "user": "kcrisman"
}
```

Did you try the `RationalField()` before and after using it like in comment:15?  I agree that we can close it if that succeeds.  I only assumed you knew something about it since you were already on this ticket.



---

archive/issue_comments_073003.json:
```json
{
    "body": "Replying to [comment:17 kcrisman]:\n> Did you try the `RationalField()` before and after using it like in comment:15?  \nyes\n> I agree that we can close it if that succeeds.  I only assumed you knew something about it since you were already on this ticket.\nI was on the ticket since (I think) William first caused the failure while doing somthing with elliptic curves, so he fingered me.  I then pointed out that the failure had nothing to do with elliptic curves!\n\n```\nsage: RationalField()\nRational Field\nsage: from sage.env import SAGE_SHARE\nsage: x = load(os.path.join(SAGE_SHARE, 'jones', 'jones.sobj'))\nsage: RationalField()\nRational Field\nsage: list(JonesDatabase().unramified_outside([3], 3))\n[Number Field in a with defining polynomial x^3 - 3*x + 1,\n Number Field in a with defining polynomial x^3 - 3]\nsage: RationalField()\nRational Field\n```\n",
    "created_at": "2020-10-08T17:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-73003",
    "user": "cremona"
}
```

Replying to [comment:17 kcrisman]:
> Did you try the `RationalField()` before and after using it like in comment:15?  
yes
> I agree that we can close it if that succeeds.  I only assumed you knew something about it since you were already on this ticket.
I was on the ticket since (I think) William first caused the failure while doing somthing with elliptic curves, so he fingered me.  I then pointed out that the failure had nothing to do with elliptic curves!

```
sage: RationalField()
Rational Field
sage: from sage.env import SAGE_SHARE
sage: x = load(os.path.join(SAGE_SHARE, 'jones', 'jones.sobj'))
sage: RationalField()
Rational Field
sage: list(JonesDatabase().unramified_outside([3], 3))
[Number Field in a with defining polynomial x^3 - 3*x + 1,
 Number Field in a with defining polynomial x^3 - 3]
sage: RationalField()
Rational Field
```




---

archive/issue_comments_073004.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-10-08T17:13:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-73004",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073005.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-10-08T17:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-73005",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073006.json:
```json
{
    "body": "If there is still a bug, at any rate we didn't find it :-)",
    "created_at": "2020-10-08T17:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-73006",
    "user": "kcrisman"
}
```

If there is still a bug, at any rate we didn't find it :-)



---

archive/issue_comments_073007.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-10-08T18:23:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8251#issuecomment-73007",
    "user": "chapoton"
}
```

Resolution: invalid

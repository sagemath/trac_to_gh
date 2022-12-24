# Issue 3852: create or adapt or include a units package

archive/issues_003852.json:
```json
{
    "body": "Assignee: jkantor\n\nHere are three possibilities:\n\n* ScientificPython's PhysicalQuantities package: http://dirac.cnrs-orleans.fr/ScientificPython/ScientificPythonManual/Scientific.Physics.PhysicalQuantities-module.html\n\nIt looks like this package is part of an actively maintained library, ScientificPython (http://dirac.cnrs-orleans.fr/plone/software/scientificpython/).  Here is a link for a printing package for this module: http://python.net/crew/bhoel/PyLaTeX-0.2/html/PyLaTeX.UnitPrint.html\n\n\n\n* Unum: http://home.scarlet.be/be052320/Unum.html\n\nIt looks like this package is dead; last release was in 2005.  It is GPL.\n\n* The Pyre units package (http://www.cacr.caltech.edu/projects/pyre/).  This was last updated in 2005, I think (you have to check out pythia 0.8).\n\n* The enthought units package (which is apparently based on the pyre package), as well as the blockcanvas unit functions.\n\nA thread about adding a units package to scipy: http://projects.scipy.org/pipermail/scipy-user/2005-March/004263.html\n\nAnother thread: http://aspn.activestate.com/ASPN/Mail/Message/scipy-user/3176352\n\nAnother page in a book mentioning two packages: http://books.google.com/books?id=j7QbD83-h8AC&pg=PA157&lpg=PA157&dq=python+physicalquantities&source=web&ots=C-JZyCFWn2&sig=x62bQ0jWyQerBGAvgJOBQuMQeWM&hl=en&sa=X&oi=book_result&resnum=10&ct=result\n\nA recent (July 2008!) trac ticket about the enthought units package: https://svn.enthought.com/enthought/ticket/1524  Related checkins seem to include: https://svn.enthought.com/enthought/changeset/21093\n\nApparently the enthought units code is undergoing refactorization.  See https://mail.enthought.com/pipermail/enthought-dev/2008-July/015717.html\n\n\nI'd say we ought to keep our eye (or help out with) the enthought package refactorization.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3852\n\n",
    "created_at": "2008-08-14T17:47:02Z",
    "labels": [
        "numerical",
        "major",
        "enhancement"
    ],
    "title": "create or adapt or include a units package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3852",
    "user": "jason"
}
```
Assignee: jkantor

Here are three possibilities:

* ScientificPython's PhysicalQuantities package: http://dirac.cnrs-orleans.fr/ScientificPython/ScientificPythonManual/Scientific.Physics.PhysicalQuantities-module.html

It looks like this package is part of an actively maintained library, ScientificPython (http://dirac.cnrs-orleans.fr/plone/software/scientificpython/).  Here is a link for a printing package for this module: http://python.net/crew/bhoel/PyLaTeX-0.2/html/PyLaTeX.UnitPrint.html



* Unum: http://home.scarlet.be/be052320/Unum.html

It looks like this package is dead; last release was in 2005.  It is GPL.

* The Pyre units package (http://www.cacr.caltech.edu/projects/pyre/).  This was last updated in 2005, I think (you have to check out pythia 0.8).

* The enthought units package (which is apparently based on the pyre package), as well as the blockcanvas unit functions.

A thread about adding a units package to scipy: http://projects.scipy.org/pipermail/scipy-user/2005-March/004263.html

Another thread: http://aspn.activestate.com/ASPN/Mail/Message/scipy-user/3176352

Another page in a book mentioning two packages: http://books.google.com/books?id=j7QbD83-h8AC&pg=PA157&lpg=PA157&dq=python+physicalquantities&source=web&ots=C-JZyCFWn2&sig=x62bQ0jWyQerBGAvgJOBQuMQeWM&hl=en&sa=X&oi=book_result&resnum=10&ct=result

A recent (July 2008!) trac ticket about the enthought units package: https://svn.enthought.com/enthought/ticket/1524  Related checkins seem to include: https://svn.enthought.com/enthought/changeset/21093

Apparently the enthought units code is undergoing refactorization.  See https://mail.enthought.com/pipermail/enthought-dev/2008-July/015717.html


I'd say we ought to keep our eye (or help out with) the enthought package refactorization.

Issue created by migration from https://trac.sagemath.org/ticket/3852





---

archive/issue_comments_027395.json:
```json
{
    "body": "Okay, so that was four projects!",
    "created_at": "2008-08-14T17:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27395",
    "user": "jason"
}
```

Okay, so that was four projects!



---

archive/issue_comments_027396.json:
```json
{
    "body": "Changing assignee from jkantor to somebody.",
    "created_at": "2008-08-14T17:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27396",
    "user": "jason"
}
```

Changing assignee from jkantor to somebody.



---

archive/issue_comments_027397.json:
```json
{
    "body": "Changing component from numerical to basic arithmetic.",
    "created_at": "2008-08-14T17:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27397",
    "user": "jason"
}
```

Changing component from numerical to basic arithmetic.



---

archive/issue_comments_027398.json:
```json
{
    "body": "yet another project recently started: \n\nhttp://sourceforge.net/mailarchive/forum.php?thread_name=200808051930.57498.dsdale24%40gmail.com&forum_name=matplotlib-devel",
    "created_at": "2008-08-20T06:03:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27398",
    "user": "jason"
}
```

yet another project recently started: 

http://sourceforge.net/mailarchive/forum.php?thread_name=200808051930.57498.dsdale24%40gmail.com&forum_name=matplotlib-devel



---

archive/issue_comments_027399.json:
```json
{
    "body": "Attachment [trac_3852.patch](tarball://root/attachments/some-uuid/ticket3852/trac_3852.patch) by was created at 2009-10-04 18:54:58\n\nFIRST REFEREE REPORT on trac_3852.patch:\n\n1. The doctest coverage is still very bad (38%):\n\n\n```\nwstein@sage:~/build/sage-4.1.1$ ./sage -coverage devel/sage/sage/symbolic/units.py \n----------------------------------------------------------------------\ndevel/sage/sage/symbolic/units.py\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE devel/sage/sage/symbolic/units.py: 38% (5 of 13)\n\nMissing documentation:\n         * evalunitdict():\n         * unit_derivations_expr(v):\n         * _sage_doc_(self):\n         * str_to_unit(name):\n         * __init__(self, data):\n         * trait_names(self):\n         * __getattr__(self, name):\n\n\nMissing doctests:\n         * vars_in_str(s):\n\n\nPossibly wrong (function name doesn't occur in doctests):\n         * convert_temperature(expr, target):\n\n----------------------------------------------------------------------\n\n```\n\n\n\n\n2. The new code fails numerous doctests:\n\n```\n        sage -t  devel/sage/sage/symbolic/units.py # 4 doctests failed\n        sage -t  devel/sage/sage/symbolic/expression.pyx # 2 doctests failed\n```\n\n\nThe actual failures:\n\n```\n\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.1.1/devel/sage/sage/symbolic/expression.pyx\", line 5399:\n    sage: (units.pressure.pascal*units.si_prefixes.kilo).convert(units.pressure.pounds_per_square_inch)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_137[10]>\", line 1, in <module>\n        (units.pressure.pascal*units.si_prefixes.kilo).convert(units.pressure.pounds_per_square_inch)###line 5399:\n    sage: (units.pressure.pascal*units.si_prefixes.kilo).convert(units.pressure.pounds_per_square_inch)\n      File \"expression.pyx\", line 5424, in sage.symbolic.expression.Expression.convert (sage/symbolic/expression.cpp:21250\n)\n      File \"/scratch/wstein/build/sage-4.1.1/local/lib/python/site-packages/sage/symbolic/units.py\", line 1064, in convert\n        expr = expr.subs(z)\n      File \"expression.pyx\", line 2777, in sage.symbolic.expression.Expression.substitute (sage/symbolic/expression.cpp:13\n700)\n      File \"expression.pyx\", line 1517, in sage.symbolic.expression.Expression.coerce_in (sage/symbolic/expression.cpp:959\n1)\n      File \"parent_old.pyx\", line 331, in sage.structure.parent_old.Parent._coerce_ (sage/structure/parent_old.c:4673)\n      File \"parent.pyx\", line 429, in sage.structure.parent.Parent.coerce (sage/structure/parent.c:4806)\n    TypeError: no canonical coercion from <type 'str'> to Symbolic Ring\n\n...\n\nFile \"/scratch/wstein/build/sage-4.1.1/devel/sage/sage/symbolic/units.py\", line 31:\n    e: units.force.dyne?\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[6]>\", line 1\n         units.force.dyne?###line 31:\n    e: units.force.dyne?\n                         ^\n     SyntaxError: invalid syntax\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.1.1/devel/sage/sage/symbolic/units.py\", line 52:\n\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.1.1/devel/sage/sage/symbolic/units.py\", line 52:\n    e: t.convert(unit.charge.coulomb)\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: Incompatible units\nGot:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.1.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.1.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[11]>\", line 1, in <module>\n        t.convert(unit.charge.coulomb)###line 52:\n    e: t.convert(unit.charge.coulomb)\n    NameError: name 'unit' is not defined\n\n\n...\n```\n",
    "created_at": "2009-10-04T18:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27399",
    "user": "was"
}
```

Attachment [trac_3852.patch](tarball://root/attachments/some-uuid/ticket3852/trac_3852.patch) by was created at 2009-10-04 18:54:58

FIRST REFEREE REPORT on trac_3852.patch:

1. The doctest coverage is still very bad (38%):


```
wstein@sage:~/build/sage-4.1.1$ ./sage -coverage devel/sage/sage/symbolic/units.py 
----------------------------------------------------------------------
devel/sage/sage/symbolic/units.py
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE devel/sage/sage/symbolic/units.py: 38% (5 of 13)

Missing documentation:
         * evalunitdict():
         * unit_derivations_expr(v):
         * _sage_doc_(self):
         * str_to_unit(name):
         * __init__(self, data):
         * trait_names(self):
         * __getattr__(self, name):


Missing doctests:
         * vars_in_str(s):


Possibly wrong (function name doesn't occur in doctests):
         * convert_temperature(expr, target):

----------------------------------------------------------------------

```




2. The new code fails numerous doctests:

```
        sage -t  devel/sage/sage/symbolic/units.py # 4 doctests failed
        sage -t  devel/sage/sage/symbolic/expression.pyx # 2 doctests failed
```


The actual failures:

```

**********************************************************************
File "/scratch/wstein/build/sage-4.1.1/devel/sage/sage/symbolic/expression.pyx", line 5399:
    sage: (units.pressure.pascal*units.si_prefixes.kilo).convert(units.pressure.pounds_per_square_inch)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_137[10]>", line 1, in <module>
        (units.pressure.pascal*units.si_prefixes.kilo).convert(units.pressure.pounds_per_square_inch)###line 5399:
    sage: (units.pressure.pascal*units.si_prefixes.kilo).convert(units.pressure.pounds_per_square_inch)
      File "expression.pyx", line 5424, in sage.symbolic.expression.Expression.convert (sage/symbolic/expression.cpp:21250
)
      File "/scratch/wstein/build/sage-4.1.1/local/lib/python/site-packages/sage/symbolic/units.py", line 1064, in convert
        expr = expr.subs(z)
      File "expression.pyx", line 2777, in sage.symbolic.expression.Expression.substitute (sage/symbolic/expression.cpp:13
700)
      File "expression.pyx", line 1517, in sage.symbolic.expression.Expression.coerce_in (sage/symbolic/expression.cpp:959
1)
      File "parent_old.pyx", line 331, in sage.structure.parent_old.Parent._coerce_ (sage/structure/parent_old.c:4673)
      File "parent.pyx", line 429, in sage.structure.parent.Parent.coerce (sage/structure/parent.c:4806)
    TypeError: no canonical coercion from <type 'str'> to Symbolic Ring

...

File "/scratch/wstein/build/sage-4.1.1/devel/sage/sage/symbolic/units.py", line 31:
    e: units.force.dyne?
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[6]>", line 1
         units.force.dyne?###line 31:
    e: units.force.dyne?
                         ^
     SyntaxError: invalid syntax
**********************************************************************
File "/scratch/wstein/build/sage-4.1.1/devel/sage/sage/symbolic/units.py", line 52:

**********************************************************************
File "/scratch/wstein/build/sage-4.1.1/devel/sage/sage/symbolic/units.py", line 52:
    e: t.convert(unit.charge.coulomb)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: Incompatible units
Got:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[11]>", line 1, in <module>
        t.convert(unit.charge.coulomb)###line 52:
    e: t.convert(unit.charge.coulomb)
    NameError: name 'unit' is not defined


...
```




---

archive/issue_comments_027400.json:
```json
{
    "body": "Google also turns up this existing module: [http://www.inference.phy.cam.ac.uk/dimpy/](http://www.inference.phy.cam.ac.uk/dimpy/)",
    "created_at": "2009-11-04T21:22:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27400",
    "user": "edrex"
}
```

Google also turns up this existing module: [http://www.inference.phy.cam.ac.uk/dimpy/](http://www.inference.phy.cam.ac.uk/dimpy/)



---

archive/issue_comments_027401.json:
```json
{
    "body": "dimpy helped me with my e&m hw. positive review :)",
    "created_at": "2009-11-04T21:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27401",
    "user": "edrex"
}
```

dimpy helped me with my e&m hw. positive review :)



---

archive/issue_comments_027402.json:
```json
{
    "body": "Do you mean that tongue-in-cheek, or do you mean that you've gone through and made sure all of the objections above were taken care of?",
    "created_at": "2009-11-04T21:44:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27402",
    "user": "jason"
}
```

Do you mean that tongue-in-cheek, or do you mean that you've gone through and made sure all of the objections above were taken care of?



---

archive/issue_comments_027403.json:
```json
{
    "body": "my apologies, I hadn't properly read the issue, much less the patch, and I meant to retract the post. \n\nI was actually referring to the dimpy module, not the patch above, and it was definitely tongue-in-cheek. Upon further investigation I found that dimpy doesn't integrate well with sage's types system.\n\nI've now read the patch and will try to find time to run the tests.",
    "created_at": "2009-11-05T03:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27403",
    "user": "edrex"
}
```

my apologies, I hadn't properly read the issue, much less the patch, and I meant to retract the post. 

I was actually referring to the dimpy module, not the patch above, and it was definitely tongue-in-cheek. Upon further investigation I found that dimpy doesn't integrate well with sage's types system.

I've now read the patch and will try to find time to run the tests.



---

archive/issue_comments_027404.json:
```json
{
    "body": "Attachment [trac_3852-part2.patch](tarball://root/attachments/some-uuid/ticket3852/trac_3852-part2.patch) by was created at 2010-01-21 02:54:02",
    "created_at": "2010-01-21T02:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27404",
    "user": "was"
}
```

Attachment [trac_3852-part2.patch](tarball://root/attachments/some-uuid/ticket3852/trac_3852-part2.patch) by was created at 2010-01-21 02:54:02



---

archive/issue_comments_027405.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-26T07:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27405",
    "user": "was"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_027406.json:
```json
{
    "body": "Attachment [trac_3852-part3.patch](tarball://root/attachments/some-uuid/ticket3852/trac_3852-part3.patch) by schymans created at 2010-01-26 15:26:44\n\nHm, it is not easy to find out what units() is actually supposed to be used for.. \nIn the notebook, units? gives:\n\nFile: /Users/sschym/Programs/sage/local/lib/python2.6/site-packages/sage/symbolic/units.py\n\nType: <type \u2018instance\u2019>\n\nDefinition: units( [noargspec] )\n\nDocstring:\n\n    A collection of units of a some type.\n\n        EXAMPLES:\n\n        sage: units.power\n        Collection power of units: cheval_vapeur horsepower watt\n\nI could not find anything useful in the documentation, either. Do I have to compile the documentation separately? \n\nCheers\nStan",
    "created_at": "2010-01-26T15:26:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27406",
    "user": "schymans"
}
```

Attachment [trac_3852-part3.patch](tarball://root/attachments/some-uuid/ticket3852/trac_3852-part3.patch) by schymans created at 2010-01-26 15:26:44

Hm, it is not easy to find out what units() is actually supposed to be used for.. 
In the notebook, units? gives:

File: /Users/sschym/Programs/sage/local/lib/python2.6/site-packages/sage/symbolic/units.py

Type: <type ‘instance’>

Definition: units( [noargspec] )

Docstring:

    A collection of units of a some type.

        EXAMPLES:

        sage: units.power
        Collection power of units: cheval_vapeur horsepower watt

I could not find anything useful in the documentation, either. Do I have to compile the documentation separately? 

Cheers
Stan



---

archive/issue_comments_027407.json:
```json
{
    "body": "All three patches still apply fine to sage-4.3.5.",
    "created_at": "2010-04-03T09:10:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27407",
    "user": "was"
}
```

All three patches still apply fine to sage-4.3.5.



---

archive/issue_comments_027408.json:
```json
{
    "body": "I'm working on reviewing this and noticed that much of the part2 and part3 patches is simply removing tabs and doing minor whitespace fixups. The three main patches leave some tabs in the relevant files, so I fixed that up. Hooray for emacs' untabify.\n\nattachment:trac_3852_fix_whitespace.patch is big but makes no functional changes.",
    "created_at": "2010-04-07T04:35:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27408",
    "user": "ddrake"
}
```

I'm working on reviewing this and noticed that much of the part2 and part3 patches is simply removing tabs and doing minor whitespace fixups. The three main patches leave some tabs in the relevant files, so I fixed that up. Hooray for emacs' untabify.

attachment:trac_3852_fix_whitespace.patch is big but makes no functional changes.



---

archive/issue_comments_027409.json:
```json
{
    "body": "Some questions and comments:\n\nIn `unit_derivations_expr` (in units.py), why the check to see that Z is a string? We get Z by looking up something in a dictionary whose values are all strings, so either Z is a string, or we threw a ValueError and aren't executing the rest of the function anyway. It looks like the \"if isinstance\" bit can be deleted. Am I misunderstanding something?\n\nA minor point: the string representation of collections of units uses strange/incorrect grammar. \"Collection area of units\" sounds like units do collecting in a certain area. I think \"Collection of units of area\" is better. How about something like\n\n```\nname = ' of ' + self.__name if self.__name else ''\nreturn \"Collection of units%s: %s\"%(name, ' '.join(sorted([str(x) for x in self.__data])))\n```\n\nin the `__repr___` method for Units?\n\nIn the descriptions of the mass units, the solar mass refers to the size of the earth -- but you mean the mass of the earth. Size is length, area, or volume; different units!\n\nPerhaps we should include \"metre\" and \"litre\" as synonyms; it seems that the official spelling, according to the SI Brochure, is \"metre\", and that's a common spelling anyway. The liter/litre isn't an official SI unit, but it is frequently spelled as litre, so might as well put in both. This would also allow non-Americans putting units into their LaTeX documents to get correctly-spelled units.\n\nThis module should get added to the reference manual (perhaps we can do that in another ticket), and a bunch of little bits in the docstrings need to be fixed up. One suggestion: change the title at the very top of units.py to \"Units of measurement\" to avoid confusion with multiplicatively invertible elements of a ring.\n\nLine 600 or so: I would find it much less confusing if ton_force was described with \"Defined to be 2000 pounds of force\".\n\nIn line 685: the documentation for candela has some goofy stuff near the end. According to the official brochure, you need \"1/683 watt per steradian\".\n\nOverall, I think this is a great addition to Sage. The code is pretty simple, works well, and is thoroughly doctested. Once the above issues are addressed, this can get a positive review. I can whip up a patch making the above changes, or can review someone else's patch.",
    "created_at": "2010-04-09T03:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27409",
    "user": "ddrake"
}
```

Some questions and comments:

In `unit_derivations_expr` (in units.py), why the check to see that Z is a string? We get Z by looking up something in a dictionary whose values are all strings, so either Z is a string, or we threw a ValueError and aren't executing the rest of the function anyway. It looks like the "if isinstance" bit can be deleted. Am I misunderstanding something?

A minor point: the string representation of collections of units uses strange/incorrect grammar. "Collection area of units" sounds like units do collecting in a certain area. I think "Collection of units of area" is better. How about something like

```
name = ' of ' + self.__name if self.__name else ''
return "Collection of units%s: %s"%(name, ' '.join(sorted([str(x) for x in self.__data])))
```

in the `__repr___` method for Units?

In the descriptions of the mass units, the solar mass refers to the size of the earth -- but you mean the mass of the earth. Size is length, area, or volume; different units!

Perhaps we should include "metre" and "litre" as synonyms; it seems that the official spelling, according to the SI Brochure, is "metre", and that's a common spelling anyway. The liter/litre isn't an official SI unit, but it is frequently spelled as litre, so might as well put in both. This would also allow non-Americans putting units into their LaTeX documents to get correctly-spelled units.

This module should get added to the reference manual (perhaps we can do that in another ticket), and a bunch of little bits in the docstrings need to be fixed up. One suggestion: change the title at the very top of units.py to "Units of measurement" to avoid confusion with multiplicatively invertible elements of a ring.

Line 600 or so: I would find it much less confusing if ton_force was described with "Defined to be 2000 pounds of force".

In line 685: the documentation for candela has some goofy stuff near the end. According to the official brochure, you need "1/683 watt per steradian".

Overall, I think this is a great addition to Sage. The code is pretty simple, works well, and is thoroughly doctested. Once the above issues are addressed, this can get a positive review. I can whip up a patch making the above changes, or can review someone else's patch.



---

archive/issue_comments_027410.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-09T03:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27410",
    "user": "ddrake"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_027411.json:
```json
{
    "body": "One more comment: `convert()` in `expression.pyx` should perhaps mention that it just returns the variable if the variable is not a unit -- since we now have a convert() method on every single symbolic variable, it will be helpful to users to explain that, unless you have a unit, convert won't do anything:\n\n```\nsage: x = var('x')\nsage: x - x.convert() \n0\n```\n",
    "created_at": "2010-04-09T03:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27411",
    "user": "ddrake"
}
```

One more comment: `convert()` in `expression.pyx` should perhaps mention that it just returns the variable if the variable is not a unit -- since we now have a convert() method on every single symbolic variable, it will be helpful to users to explain that, unless you have a unit, convert won't do anything:

```
sage: x = var('x')
sage: x - x.convert() 
0
```




---

archive/issue_comments_027412.json:
```json
{
    "body": "attachment:trac_3852_referee.patch adds the units module to the reference manual and makes some minor changes to docstrings. It doesn't change any code.\n\nI'm marking this as \"needs review\"; if someone could look over my referee patch, we can give this entire ticket a positive review.",
    "created_at": "2010-04-12T07:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27412",
    "user": "ddrake"
}
```

attachment:trac_3852_referee.patch adds the units module to the reference manual and makes some minor changes to docstrings. It doesn't change any code.

I'm marking this as "needs review"; if someone could look over my referee patch, we can give this entire ticket a positive review.



---

archive/issue_comments_027413.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-12T07:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27413",
    "user": "ddrake"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_027414.json:
```json
{
    "body": "Thanks for pushing this ticket closer to the finish Dan.\n\nThough I don't think fixing the whitespace problems of `sage/symbolic/expression.pyx` in attachment:trac_3852_fix_whitespace.patch is a good idea. There are many positively reviewed symbolics tickets waiting to be merged on trac and many of them touch the same file. Pushing the patch on my queue, I get\n\n\n```\napplying trac_3852_fix_whitespace.patch\npatching file sage/symbolic/expression.pyx\nHunk #7 succeeded at 317 with fuzz 1 (offset -2 lines).\nHunk #208 FAILED at 6448\nHunk #215 FAILED at 6699\nHunk #216 FAILED at 6713\n3 out of 236 hunks FAILED -- saving rejects to file sage/symbolic/expression.pyx.rej\n```\n\n\nI don't think rebasing the patch on the other changes is worth it. We should either have an understanding that this ticket is merged after all the other actual bug fixes, and the failures in applying this patch are ignored, or change this patch to fix only the relevant sections of the file. (Actually, I wouldn't mind if this was a general policy on whitespace fixes.)\n\n\nOtherwise, I'm willing to give Dan's changes and this ticket a positive review.",
    "created_at": "2010-04-12T23:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27414",
    "user": "burcin"
}
```

Thanks for pushing this ticket closer to the finish Dan.

Though I don't think fixing the whitespace problems of `sage/symbolic/expression.pyx` in attachment:trac_3852_fix_whitespace.patch is a good idea. There are many positively reviewed symbolics tickets waiting to be merged on trac and many of them touch the same file. Pushing the patch on my queue, I get


```
applying trac_3852_fix_whitespace.patch
patching file sage/symbolic/expression.pyx
Hunk #7 succeeded at 317 with fuzz 1 (offset -2 lines).
Hunk #208 FAILED at 6448
Hunk #215 FAILED at 6699
Hunk #216 FAILED at 6713
3 out of 236 hunks FAILED -- saving rejects to file sage/symbolic/expression.pyx.rej
```


I don't think rebasing the patch on the other changes is worth it. We should either have an understanding that this ticket is merged after all the other actual bug fixes, and the failures in applying this patch are ignored, or change this patch to fix only the relevant sections of the file. (Actually, I wouldn't mind if this was a general policy on whitespace fixes.)


Otherwise, I'm willing to give Dan's changes and this ticket a positive review.



---

archive/issue_comments_027415.json:
```json
{
    "body": "Replying to [comment:19 burcin]:\n> Though I don't think fixing the whitespace problems of `sage/symbolic/expression.pyx` in attachment:trac_3852_fix_whitespace.patch is a good idea. There are many positively reviewed symbolics tickets waiting to be merged on trac and many of them touch the same file.\n\nI see. If the big whitespace patch messes up a bunch of other patches, then we should postpone it. I'll take out the hunks that affect expression.pyx, and confine all the changes to units.py, since I don't think there are any other tickets that depend on this one.\n\nI would like to see some tab/whitespace cleanup -- there are (again) tons of tabs in the Sage library. I understand that coordinating this sort of thing is difficult, though.",
    "created_at": "2010-04-13T02:46:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27415",
    "user": "ddrake"
}
```

Replying to [comment:19 burcin]:
> Though I don't think fixing the whitespace problems of `sage/symbolic/expression.pyx` in attachment:trac_3852_fix_whitespace.patch is a good idea. There are many positively reviewed symbolics tickets waiting to be merged on trac and many of them touch the same file.

I see. If the big whitespace patch messes up a bunch of other patches, then we should postpone it. I'll take out the hunks that affect expression.pyx, and confine all the changes to units.py, since I don't think there are any other tickets that depend on this one.

I would like to see some tab/whitespace cleanup -- there are (again) tons of tabs in the Sage library. I understand that coordinating this sort of thing is difficult, though.



---

archive/issue_comments_027416.json:
```json
{
    "body": "Attachment [trac_3852_fix_whitespace.patch](tarball://root/attachments/some-uuid/ticket3852/trac_3852_fix_whitespace.patch) by ddrake created at 2010-04-13 03:04:05\n\nremove tabs, trailing whitespace from units.py",
    "created_at": "2010-04-13T03:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27416",
    "user": "ddrake"
}
```

Attachment [trac_3852_fix_whitespace.patch](tarball://root/attachments/some-uuid/ticket3852/trac_3852_fix_whitespace.patch) by ddrake created at 2010-04-13 03:04:05

remove tabs, trailing whitespace from units.py



---

archive/issue_comments_027417.json:
```json
{
    "body": "Attachment [trac_3852_referee.patch](tarball://root/attachments/some-uuid/ticket3852/trac_3852_referee.patch) by ddrake created at 2010-04-13 03:04:25",
    "created_at": "2010-04-13T03:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27417",
    "user": "ddrake"
}
```

Attachment [trac_3852_referee.patch](tarball://root/attachments/some-uuid/ticket3852/trac_3852_referee.patch) by ddrake created at 2010-04-13 03:04:25



---

archive/issue_comments_027418.json:
```json
{
    "body": "The new fix_whitespace patch only affects units.py, and the referee patch only touches the convert() function in expression.pyx. Burcin, do these patches play nicely with the other symbolics tickets?",
    "created_at": "2010-04-13T03:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27418",
    "user": "ddrake"
}
```

The new fix_whitespace patch only affects units.py, and the referee patch only touches the convert() function in expression.pyx. Burcin, do these patches play nicely with the other symbolics tickets?



---

archive/issue_comments_027419.json:
```json
{
    "body": "Replying to [comment:18 ddrake]:\n> attachment:trac_3852_referee.patch adds the units module to the reference manual and makes some minor changes to docstrings. It doesn't change any code.\n> \n> I'm marking this as \"needs review\"; if someone could look over my referee patch, we can give this entire ticket a positive review.\n\nI definitely give that referee patch a positive review.  Very nice!  It's going to be great getting this code into Sage.",
    "created_at": "2010-04-13T03:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27419",
    "user": "was"
}
```

Replying to [comment:18 ddrake]:
> attachment:trac_3852_referee.patch adds the units module to the reference manual and makes some minor changes to docstrings. It doesn't change any code.
> 
> I'm marking this as "needs review"; if someone could look over my referee patch, we can give this entire ticket a positive review.

I definitely give that referee patch a positive review.  Very nice!  It's going to be great getting this code into Sage.



---

archive/issue_comments_027420.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-13T10:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27420",
    "user": "burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_027421.json:
```json
{
    "body": "The new white space fix patch (attachment:trac_3852_fix_whitespace.patch) applies cleanly, and all tests pass. I give a positive review to the referee patch (attachment:trac_3852_referee.patch).\n\nThanks a lot for fixing this Dan!\n\nPatches to be applied are:\n* attachment:trac_3852.patch\n* attachment:trac_3852-part2.patch\n* attachment:trac_3852-part3.patch\n* attachment:trac_3852_fix_whitespace.patch\n* attachment:trac_3852_referee.patch",
    "created_at": "2010-04-13T10:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27421",
    "user": "burcin"
}
```

The new white space fix patch (attachment:trac_3852_fix_whitespace.patch) applies cleanly, and all tests pass. I give a positive review to the referee patch (attachment:trac_3852_referee.patch).

Thanks a lot for fixing this Dan!

Patches to be applied are:
* attachment:trac_3852.patch
* attachment:trac_3852-part2.patch
* attachment:trac_3852-part3.patch
* attachment:trac_3852_fix_whitespace.patch
* attachment:trac_3852_referee.patch



---

archive/issue_comments_027422.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n\n* attachment:trac_3852.patch\n* attachment:trac_3852-part2.patch\n* attachment:trac_3852-part3.patch\n* attachment:trac_3852_fix_whitespace.patch\n* attachment:trac_3852_referee.patch\n\n(I think these patches cause some warning when building the reference manual.  Those can be fixed on a follow-up ticket.)",
    "created_at": "2010-04-15T06:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27422",
    "user": "jhpalmieri"
}
```

Merged in 4.4.alpha0:

* attachment:trac_3852.patch
* attachment:trac_3852-part2.patch
* attachment:trac_3852-part3.patch
* attachment:trac_3852_fix_whitespace.patch
* attachment:trac_3852_referee.patch

(I think these patches cause some warning when building the reference manual.  Those can be fixed on a follow-up ticket.)



---

archive/issue_comments_027423.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T06:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3852#issuecomment-27423",
    "user": "jhpalmieri"
}
```

Resolution: fixed

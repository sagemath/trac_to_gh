# Issue 3852: create or adapt or include a units package

Issue created by migration from https://trac.sagemath.org/ticket/3852

Original creator: jason

Original creation time: 2008-08-14 17:47:02

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


---

Comment by jason created at 2008-08-14 17:53:19

Okay, so that was four projects!


---

Comment by jason created at 2008-08-14 17:54:13

Changing assignee from jkantor to somebody.


---

Comment by jason created at 2008-08-14 17:54:13

Changing component from numerical to basic arithmetic.


---

Comment by jason created at 2008-08-20 06:03:25

yet another project recently started: 

http://sourceforge.net/mailarchive/forum.php?thread_name=200808051930.57498.dsdale24%40gmail.com&forum_name=matplotlib-devel


---

Attachment

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

Comment by edrex created at 2009-11-04 21:22:31

Google also turns up this existing module: [http://www.inference.phy.cam.ac.uk/dimpy/](http://www.inference.phy.cam.ac.uk/dimpy/)


---

Comment by edrex created at 2009-11-04 21:29:43

dimpy helped me with my e&m hw. positive review :)


---

Comment by jason created at 2009-11-04 21:44:45

Do you mean that tongue-in-cheek, or do you mean that you've gone through and made sure all of the objections above were taken care of?


---

Comment by edrex created at 2009-11-05 03:32:15

my apologies, I hadn't properly read the issue, much less the patch, and I meant to retract the post. 

I was actually referring to the dimpy module, not the patch above, and it was definitely tongue-in-cheek. Upon further investigation I found that dimpy doesn't integrate well with sage's types system.

I've now read the patch and will try to find time to run the tests.


---

Attachment


---

Comment by was created at 2010-01-26 07:17:48

Changing status from needs_work to needs_review.


---

Attachment

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

Comment by was created at 2010-04-03 09:10:26

All three patches still apply fine to sage-4.3.5.


---

Comment by ddrake created at 2010-04-07 04:35:57

I'm working on reviewing this and noticed that much of the part2 and part3 patches is simply removing tabs and doing minor whitespace fixups. The three main patches leave some tabs in the relevant files, so I fixed that up. Hooray for emacs' untabify.

attachment:trac_3852_fix_whitespace.patch is big but makes no functional changes.


---

Comment by ddrake created at 2010-04-09 03:13:16

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

Comment by ddrake created at 2010-04-09 03:13:16

Changing status from needs_review to needs_work.


---

Comment by ddrake created at 2010-04-09 03:17:25

One more comment: `convert()` in `expression.pyx` should perhaps mention that it just returns the variable if the variable is not a unit -- since we now have a convert() method on every single symbolic variable, it will be helpful to users to explain that, unless you have a unit, convert won't do anything:

```
sage: x = var('x')
sage: x - x.convert() 
0
```



---

Comment by ddrake created at 2010-04-12 07:08:18

attachment:trac_3852_referee.patch adds the units module to the reference manual and makes some minor changes to docstrings. It doesn't change any code.

I'm marking this as "needs review"; if someone could look over my referee patch, we can give this entire ticket a positive review.


---

Comment by ddrake created at 2010-04-12 07:08:18

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2010-04-12 23:18:26

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

Comment by ddrake created at 2010-04-13 02:46:27

Replying to [comment:19 burcin]:
> Though I don't think fixing the whitespace problems of `sage/symbolic/expression.pyx` in attachment:trac_3852_fix_whitespace.patch is a good idea. There are many positively reviewed symbolics tickets waiting to be merged on trac and many of them touch the same file.

I see. If the big whitespace patch messes up a bunch of other patches, then we should postpone it. I'll take out the hunks that affect expression.pyx, and confine all the changes to units.py, since I don't think there are any other tickets that depend on this one.

I would like to see some tab/whitespace cleanup -- there are (again) tons of tabs in the Sage library. I understand that coordinating this sort of thing is difficult, though.


---

Attachment

remove tabs, trailing whitespace from units.py


---

Attachment


---

Comment by ddrake created at 2010-04-13 03:08:16

The new fix_whitespace patch only affects units.py, and the referee patch only touches the convert() function in expression.pyx. Burcin, do these patches play nicely with the other symbolics tickets?


---

Comment by was created at 2010-04-13 03:22:56

Replying to [comment:18 ddrake]:
> attachment:trac_3852_referee.patch adds the units module to the reference manual and makes some minor changes to docstrings. It doesn't change any code.
> 
> I'm marking this as "needs review"; if someone could look over my referee patch, we can give this entire ticket a positive review.

I definitely give that referee patch a positive review.  Very nice!  It's going to be great getting this code into Sage.


---

Comment by burcin created at 2010-04-13 10:51:29

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2010-04-13 10:51:29

The new white space fix patch (attachment:trac_3852_fix_whitespace.patch) applies cleanly, and all tests pass. I give a positive review to the referee patch (attachment:trac_3852_referee.patch).

Thanks a lot for fixing this Dan!

Patches to be applied are:
 * attachment:trac_3852.patch
 * attachment:trac_3852-part2.patch
 * attachment:trac_3852-part3.patch
 * attachment:trac_3852_fix_whitespace.patch
 * attachment:trac_3852_referee.patch


---

Comment by jhpalmieri created at 2010-04-15 06:02:12

Merged in 4.4.alpha0:

  * attachment:trac_3852.patch
  * attachment:trac_3852-part2.patch
  * attachment:trac_3852-part3.patch
  * attachment:trac_3852_fix_whitespace.patch
  * attachment:trac_3852_referee.patch

(I think these patches cause some warning when building the reference manual.  Those can be fixed on a follow-up ticket.)


---

Comment by jhpalmieri created at 2010-04-15 06:02:12

Resolution: fixed

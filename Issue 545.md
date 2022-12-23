# Issue 545: polish the new symbolic logic code.

Issue created by migration from https://trac.sagemath.org/ticket/545

Original creator: was

Original creation time: 2007-08-31 21:07:33

Assignee: chrisgorecki




---

Comment by was created at 2007-08-31 21:32:42

To do:

 1. log.statement(...) could return a "LogicalStatement" object, which has a nice print  method -- __repr__(self) --, and a _latex_ method.  

```
   class LogicalStatement:
      def __init__(self, ...)
          ...
```

Then this might work:

```
    sage: s = log.statement("a&b|!(c|a)")
    sage: s
    a&b|!(c|a)
    sage: s & s
    a&b|!(c|a)&a&b|!(c|a)
    sage: s.truthtable()
    ...
    sage: show(s.truthtable())    # calls _latex
    nice typeset version
```


 2. Here:

```
  sage: s = log.statement("a&&b")
  Malformed Statement
```

    instead of printing, do 

```
       raise ValueError, "malformed statement"
```



3. Don't use "eval" for a name, since that's a builtin Python.  

4. Shift this over to line up with the r:

```
def eval(toks):
    r"""
        This function is for internal use by the class SymbollicLogic.
        It returns 'True' if the exression contained in toks would
```


5. Every function should have example doctests.  And to test do this:

```
$ cd SAGE_ROOT/devel/sage/sage/logic
$ sage -t logic.py    
```


6.  varaibles --> variables

7. Delete the vars stuff from the inputs in the docs here and clarify how they are used elsewhere:

```

        INPUT:
            self -- the calling object
            s -- a string containing the logic expression to be manipulated
            global vars -- a dictionary with the variable names and
                          their current boolean value
            global vars_order -- a list of the variable names in
                                the order they were found
```

   Also, at the top of the file document that vars and vars_order are used
to simplify passing information around between various eval* functions.
Or better just make all the eval functions be methods of the LogicalStatement class, if that makes sense. 

8. Possibly clarify what valid variable names are -- in the error message.


---

Comment by was created at 2007-08-31 21:38:17

9. Write something in the docstring at the very top just summarizes the very basic of proposition calculus / symbolic logic / boolean algebra, with examples.


---

Comment by was created at 2007-09-11 22:56:52

I've uploaded a new tarball that addresses all the todo's above.  This should be integrated into the SAGE 
codebase and tried out by some people very soon.  

Note that probably sage/logic/all.py and sage/all.py will need to be modified so that the doctests
will actually work.


---

Comment by was created at 2007-09-11 22:57:40

By the way, this shouldn't definitely stay at milestone 2.9, since it shouldn't be too difficult.


---

Comment by pdenapo created at 2007-09-16 19:44:50

Some comments/ideas on this:

1) I'm not sure if SymbolicLogic is the proper name for this class. A more accurate name would be 
PropositionalCalculus (since there are other important theories in symbolic logic like PredicateCalculus, i.e. first order logic) that we could support in the future. 

2) An important feature to have would be computing the conjuntive normal form, and the output of this form in the DIMACS format used by SAT solvers, see

http://www.cs.ubc.ca/~hoos/SATLIB/Benchmarks/SAT/satformat.ps

(see also ticket #418 on wrapping minisat)


---

Comment by pdenapo created at 2007-09-16 20:33:51

Another comment: why using OPAREN and CPAREN as tokens?
using just '(' and ')' would be much more clear, and faster to process (since they are a
single character)


---

Comment by was created at 2008-01-23 04:29:46

Comment from the author about the new version

```
Hi William,

Sorry about the long delay with getting this code to you, I got a little sidetracked with school and all.  But, here it is.  At this point I believe I've fixed all the issues listed in ticket 545 as well as incorporating all of Pablo De Napoli's ideas and implementing cnf conversions and a DIMACS satformat output method.  I'm not sure if you want to post the code on the trac ticket, or in the repository, or elsewhere.  If you could let me know where it goes I can start soliciting advice on the devel group though.

I have some ideas/questions for where the code should go next, but getting this release accepted first is probably at the top of the list.

-Chris Gorecki
```



---

Comment by was created at 2008-01-25 17:16:47

From Pablo De Napoli:

```
Chris: many thanks for sending the new version of your code.
I think that it is a great work. Actually I see that you have
implemented many of
my previous suggestions like: using the the builting True/False
from python instead of strings, using a tree to parse propositional
formulas, avoid using the OPAN/CPAN tokens, etc.) and thank you for adding me
as an author (eventhough
I've not actually writen a single line of the code)

 I'll review it in more detail and tell you if I see something that can
be still improved.

Pablo
```



---

Attachment

this is from chris gorecki


---

Comment by AlexGhitza created at 2008-04-15 02:58:59

I *think* I managed to turn the bundle into a patch against sage-3.0.alpha4.  I also tried to fiddle with the patch's header so that Chris Gorecki appears as its author.


---

Comment by robertwb created at 2008-05-14 17:45:45

While browsing the code I noticed lots of stuff that seemed overly verbose (and inefficient), e.g. 


```
        124     def eval_ifthen_op(lval, rval): 
 	125	    r""" 
 	126	    This function returns the logical 'ifthen' operator applied to lval and rval. 
 	127	 
 	128	    INPUT: 
 	129	        lval -- boolean value to the left of the ifthen operator. 
 	130	        rval -- boolean value appearing to the right of the ifthen operator. 
 	131	                                     
 	132	    OUTPUT: 
 	133	        Returns the logical 'ifthen' operator applied to lval and rval.   
 	134	 
 	135	    EXAMPLES: 
 	136	        sage: import booleval 
 	137	        sage: booleval.eval_ifthen_op(True, False) 
 	138	        False 
 	139	        sage: booleval.eval_ifthen_op(False, False) 
 	140	        True 
 	141	    """ 
 	142	    if(lval == False and rval == False): 
 	143	        return True 
 	144	    elif(lval == False and rval == True): 
 	145	        return True 
 	146	    elif(lval == True and rval == False): 
 	147	        return False 
 	148	    elif(lval == True and rval == True): 
 	149	        return True 
```


which could be summarized as 

```
return not lval or rval
```


Also, the operators are passed around (and compared) as strings everywhere (sometimes '&', sometimes 'and'). I think it would be better to use `operator.not_`, `operator.and_`, etc. and use `is` to compare, and then one can also write stuff like 

```
return op(lval, rval)
```


rather than having big if-then-else statements. 

Having a global `__vars` seems fragile as well. 

Sorry it's taken so long to get this in, the boolean formula simplification stuff looks good, I just think some of it could be greatly improved.


---

Comment by craigcitro created at 2008-06-15 21:23:15

Changing keywords from "" to "editor_wstein".


---

Attachment

This is the referee report


---

Comment by was created at 2008-06-15 22:07:19

REFEREE REPORT:
 See the attached file sekine.pdf.


---

Comment by was created at 2008-06-19 22:57:52

Chris is too busy for the next two weeks to work on this, I think.


---

Comment by goreckc created at 2008-09-11 02:51:44

latest release


---

Attachment

This release should address all the issues in sekine.pdf.


---

Comment by mvngu created at 2008-10-28 02:25:18

For the patch *logic.patch*, below are some possible fixes for improving its documentation. I was reviewing the plain text version of the diff, not the online version. This accounts for the number that precedes each line in the diffs below. In other words, such a number refers to the line number in the downloaded, plain text diff file, which should simplify the task of reviewing my suggestions.



1.

```
36 -    Evaluates the tree using the boolean values contained in dictinary
36 +    Evaluates the tree using the boolean values contained in dictionary
```


2.

```
40 -        tree -- a list of three elements corrospsponding to a branch of a
40 +        tree -- a list of three elements corresponding to a branch of a
```


3.

```
67 -        tree -- a list of three elements corrospsponding to a branch of a
67 +        tree -- a list of three elements corresponding to a branch of a
```


4.

```
201 -    underscores and aplphanumerics.  Parentheses may be used to
201 +    underscores and alphanumerics.  Parentheses may be used to
```


5.

```
320 -            tree -- a list continaing the parse tree of the expression.
320 +            tree -- a list containing the parse tree of the expression.
```


6.

```
322 -                  with each variable occuring only once.
322 +                  with each variable occurring only once.
```


7.

```
486 -        Returns two statements atatched by the -> operator.
486 +        Returns two statements attached by the -> operator.
```


8.

```
494 -            ithen'ed together.
494 +            ifthen'ed together.
```


9.

```
563 -            start -- an interger representing the row of the truth
563 +            start -- an integer representing the row of the truth
```


10.

```
564 -                     table from which to start intilized to 0 which
564 +                     table from which to start initialized to 0, which
```


11.

```
568 -                   to be created.  It is intilized to the last row of the
568 +                   to be created.  It is initialized to the last row of the
```


12.

```
601 -            When sent with no start or end paramaters this is an
601 +            When sent with no start or end parameters, this is an
```


13.

```
680 -        It does this by applying a set of rules that are gaurenteed to convert the
680 +        It does this by applying a set of rules that are guaranteed to convert the
```


14.

```
700 -            is typically prefered, but results can vary.
700 +            is typically preferred, but results can vary.
```


15.

```
718 -            A string representing the satformat represetatin of this object.
718 +            A string representing the satformat representation of this object.
```


16.

```
881 -            Returns a new statement that is the first statement attatched to
881 +            Returns a new statement that is the first statement attached to
```


17.

```
950 -        if-thens, and xor opperations to operations only involving and/or operations.
950 +        if-then, and xor operations to operations only involving and/or operations.
```


18.

```
954 -            tree -- a list of three elements corrospsponding to a branch of a
954 +            tree -- a list of three elements corresponding to a branch of a
```


19.

```
1068 -        This function converts the string expression asscociated with an instance
1068 +        This function converts the string expression associated with an instance
```


20.

```
1902 -        # FUTHER REDUCE COVER WITH EPI
1902 +        # FURTHER REDUCE COVER WITH EPI
```


21.

```
1948 -    An unforunate side affect of the Quine-McCluskey system is that x !=
1948 +    An unfortunate side effect of the Quine-McCluskey system is that x !=
```


22.

```
1977 -Module that creates and modifys parse trees of well formed
1977 +Module that creates and modifies parse trees of well formed
```


23.

```
2003 -    This function produces a parse tree from a boolen formula s.
2003 +    This function produces a parse tree from a boolean formula s.
```


24.

```
2042 -        Returns a list of tokens corrosponding to s.
2042 +        Returns a list of tokens corresponding to s.
```


25.

```
2137 -             are occuring.
2137 +             are occurring.
```


26.

```
2267 -It is not an error to use nonsenical numeric inputs.
2267 +It is not an error to use nonsensical numeric inputs.
```


27.

```
2326 -                  with each variable occuring only once.
2326 +                  with each variable occurring only once.
```


28.

```
2370 -        Strange paramaters can lead to the table header with no body.
2370 +        Strange parameters can lead to the table header with no body.
```


29.

```
2415 -        Strange paramaters can lead to the table header with no body.
2415 +        Strange parameters can lead to a table header with no body.
```


30.

```
2478 -    Formulas consist of the operators &, |, ~, ^, ->, <->, corrosponding
2478 +    Formulas consist of the operators &, |, ~, ^, ->, <->, corresponding
```


31.

```
2481 -    underscores and aplphanumerics.  Parentheses may be used to
2481 +    underscores and alphanumerics.  Parentheses may be used to
```


32.

```
362 -        Returns a latex representation of this statement.
362 +        Returns a LaTeX representation of this statement.
```


33.

```
368 -            Returns the latex representation of this statement.
368 +            Returns the LaTeX representation of this statement.
```


34.

```
384 +            other --the left hand side statement.
384 +            other -- the left hand side statement.
```


35.

```
404 +            other --the left hand side statement.
404 +            other -- the left hand side statement.
```


36.

```
425 -            other --the left hand side statement.
425 +            other -- the left hand side statement.
```


37.

```
446 -            other --the left hand side statement.
446 +            other -- the left hand side statement.
```


38.

```
467 -            other --the left hand side statement.
467 +            other -- the left hand side statement.
```


39.

```
490 -            other --the left hand side statement.
490 +            other -- the left hand side statement.
```


40.

```
511 -            other --the left hand side statement.
511 +            other -- the left hand side statement.
```


41.

```
533 -            other --the left hand side statement.
533 +            other -- the left hand side statement.
```


42.

```
537 -            right hand side and false otherwise.
537 +            right hand side, and false otherwise.
```


43.

```
558 -        start inclusive and end exclusive so a truthtable(0, 2) will include
558 +        start inclusive and end exclusive so truthtable(0, 2) will include
```


44.

```
572 -            Returns the truthtable (a 2-d array with the creating statement
572 +            Returns the truthtable (a 2-D array with the creating statement
```


45. Please carefully read through the following snippet from the original diff file:

```
590 +        We can now create truthtable of rows 1 to 5
591 +            sage: s.truthtable(1, 5)
592 +            a      b      c      value
593 +            False  False  True   False
594 +            False  True   False  True
595 +            False  True   True   False
596 +            True   False  False  False
```

Why "rows 1 to 5" when you're using the command `s.truthtable(1, 5)`? My understanding is that `s.truthtable(1, 5)` includes row 1 all the way up to but excluding row 5. In effect, that command actually creates 4 rows, excluding the standard header row. Perhaps you might want to consider this diff:

```
590 -        We can now create truthtable of rows 1 to 5
590 +        We can now create a truth table of rows 1 to 4, inclusive.
```

or this one:

```
590 -        We can now create truthtable of rows 1 to 5
590 +        We can now create a truth table of rows 1 to 5, exclusive.
```



46.

```
637 -        It does this by examining the truthtable of the formula.
637 +        It does this by examining the truth table of the formula.
```


47.

```
653 -            This method creates the cnf parse tree by examining the logic
653 +            This method creates the CNF parse tree by examining the logic
```


48.

```
699 -            Unless a formula is already in (or close to) being in cnf convert_cnf()
699 +            Unless a formula is already in (or close to) being in CNF, convert_cnf()
```


49. No tabs, please. This issue is especially important since we're using Python and most folks who program in Python use only spaces --- NOT tabs --- for their indentation. For official reasons why tabs are not used, please refer to [PEP 666](http://www.python.org/dev/peps/pep-0666/). The [Sage Developer's Guide](http://www.sagemath.org/doc/prog/prog.html) provides various general guidelines to be adhered to when writing code (and documentation) to be included within Sage itself. In particular, you might want to consult [this section](http://www.sagemath.org/doc/prog/node6.html). If you feel that my comment is unfair to you, please don't flame me. Instead, provide me with reasons why it's unfair (to you). If your reasons turn out to be valid and they show that I'm being unfair, I'd stand corrected and offer you my apology.

```
711 -	    See www.cs.ubc.ca/~hoos/SATLIB/Benchmarks/SAT/satformat.ps for a
711 +        See www.cs.ubc.ca/~hoos/SATLIB/Benchmarks/SAT/satformat.ps for a
```


50.

```
730 -            cnf form by a call to convert_cnf() or convert_cnf_recur()
730 +            CNF form by a call to convert_cnf() or convert_cnf_recur(),
```


51.

```
806 -            cnf form by a call to convert_cnf() or convert_cnf_recur()
806 +            CNF form by a call to convert_cnf() or convert_cnf_recur(),
```


52.

```
838 -        '~', operators.
838 +        '~' operators.
```


53.

```
1117 -            The next operator in the string
1117 +            The next operator in the string.
```


54.

```
1276 -        Will create a composite functor which will add 1, multiply by
1276 +        will create a composite functor which will add 1, multiply by
```


55.

```
1343 -    is defined so that that tc(ast) returns the count of ts.  The
1343 +    is defined so that tc(ast) returns the count of ts.  The
```


56.

```
1575 -    The exclusive-or operator, will turn into:
1575 +    The exclusive-or operator will turn into:
```


57.

```
1945 -    DNF formulae generated from prepositional logic ASTs as described
1945 +    DNF formulae generated from propositional logic ASTs as described
```


58.

```
2216 -A logic table is essentially a 2-d array that is created by the statement class
2216 +A logic table is essentially a 2-D array that is created by the statement class
```


59.

```
2221 -For instance, with the variables A, B, and C the truthtable looks like:
2221 +For instance, with the variables A, B, and C the truth table looks like:
```


60.

```
2233 -This is equivalent to counting in binary, where a table would appear thusly;
2233 +This is equivalent to counting in binary, where a table would appear thus:
```


61.

```
2279 -If one argument is provided truthtable defaults to the end.
2279 +If one argument is provided, truthtable defaults to the end.
```


62.

```
2291 -If the second argument is negative truthtable defaults to the end.
2291 +If the second argument is negative, truthtable defaults to the end.
```


63.

```
2324 -            t -- a 2-d array containing the table values
2324 +            t -- a 2-D array containing the table values.
```


64.

```
2396 -            self -- the calling object: not used
2396 +            self -- the calling object: not used.
```


65.

```
2454 -            self -- the calling object: not used
2454 +            self -- the calling object: not used.
```


66.

```
2592 -    Formula returns an instance if BooleanFormula if possible, and throws
2592 +    Formula returns an instance of BooleanFormula if possible, and throws
```



---

Comment by mabshoff created at 2008-10-28 02:29:34

Minh,

you should really post patches on top of given patches to make it easier to apply your changes.

Cheers,

Michael


---

Comment by mvngu created at 2008-10-28 02:41:22

Replying to [comment:23 mabshoff]:
> you should really post patches on top of given patches to make it easier to apply your changes.
You mean like applying the original patch first, then upload a patch of the patched file? Is that what you mean?


---

Comment by mabshoff created at 2008-10-28 02:43:49

Replying to [comment:24 mvngu]:

> You mean like applying the original patch first, then upload a patch of the patched file? Is that what you mean?

Yes, exactly.

Cheers,

Michael


---

Attachment

Chris,

do *not* attach tgz files to trac since it causes massive problems. Instead post plain hg patches.

Cheers,

Michael


---

Comment by mvngu created at 2008-10-28 05:15:28

Replying to [comment:25 mabshoff]:
> Replying to [comment:24 mvngu]:
> 
> > You mean like applying the original patch first, then upload a patch of the patched file? Is that what you mean?
> 
> Yes, exactly.


I'm having trouble applying the patch *logic.hg*. For example, I've received this abort message:

```
sage: hg_sage.patch("/home/mvngu/usr/bin/sage-3.1.4/devel/sage-mvngu-review/patch-review/logic.hg")
cd "/home/mvngu/usr/bin/sage-3.1.4/devel/sage" && hg status
cd "/home/mvngu/usr/bin/sage-3.1.4/devel/sage" && hg status
cd "/home/mvngu/usr/bin/sage-3.1.4/devel/sage" && hg import   "/home/mvngu/usr/bin/sage-3.1.4/devel/sage-mvngu-review/patch-review/logic.hg"
applying /home/mvngu/usr/bin/sage-3.1.4/devel/sage-mvngu-review/patch-review/logic.hg
abort: no diffs found
```

OK, so perhaps it's because *logic.hg* is bzip2 compressed:

```
$ file logic.hg 
logic.hg: Mercurial changeset bundle (bzip2 compressed)
```

But why can't I do bunzip2:

```
$ bunzip2 logic.hg 
bunzip2: Can't guess original name for logic.hg -- using logic.hg.out
bunzip2: logic.hg is not a bzip2 file.
```

Any other way(s) of getting the diff file(s) bundled in *logic.hg*?


---

Attachment

Having trouble with the patch, don't use logic.patch.


---

Comment by goreckc created at 2008-11-24 02:33:00

Fixed documentation.


---

Attachment

All of mvngu's changes have been incorporated into logic2.patch.


---

Attachment

Improve latex output for boolean formulas, fix a few spelling mistakes


---

Comment by was created at 2008-11-27 08:19:33

Bizarrely this patch put *all* the new code in a bunch of files in SAGE_ROOT/devel/sage/!?  This code should go in SAGE_ROOT/devel/sage/sage/logic and be properly imported.  I'm really confused about what happened here.


```
was@sage:~/build/sage-3.2.rc1/devel/sage$ ls
booleval.py     build     c_lib    install         MANIFEST.in      PKG-INFO     README.txt    sage-push          spkg-delauto
boolformula.py  build.py  clib.py  logicparser.py  module_list.py   propcalc.py  sage          setup.py           spkg-dist
boolopt.py      bundle    export   logictable.py   module_list.pyc  pull         sagebuild.py  spkg-debian-maybe  spkg-install
```


Note the boolformula.py, etc., above.


---

Comment by mabshoff created at 2008-11-27 08:29:08

Once there are new patches someone please clean up the old deadwood.

Cheers,

Michael


---

Comment by goreckc created at 2008-12-01 00:54:02

Changed directory.


---

Attachment

I believe this patch should output to SAGE_ROOT/devel/sage/sage/logic.  I'm not sure if it is being imported properly.  

It doesn't have the trac_545_latex.patch applied against it either.  Should this be done?


---

Comment by GeorgSWeber created at 2008-12-29 21:14:11

Target time for the review: January 11th


---

Comment by GeorgSWeber created at 2009-01-20 22:55:20

Apply only this patch and then "trac_545_latex.patch"


---

Attachment

Positive review, this should go into the 3.3 series.

`@`Michael:
For this ticket, only two of the patches are to be applied (I tested against Sage3.3.alpha0 on my Mac) to the Sage Library (devel/sage-main):

* "logic4.patch" (should apply cleanly, credit: Chris Gorecki)

* "trac_545_latex.patch" (should apply, but with one hunk succeeding only with fuzz, credit: Wilfried Huss)

Note 1: The "logic4.patch" is essentially the "logic3.patch", but such that the files do not go into "devel/sage/logic/", but into "devel/sage/sage/logic", where they belong. For the doctests to pass I also changed lines like "sage: import propcalc" into "sage: import sage.logic.propcalc as propcalc", and I removed linebreaks/backslashes in the "Expected Output" so that the true output now does match the expected output. Probably one should adjust the "all.py" in the "sage/logic" subdirectory in an appropriate way, but I wanted to do only minimal invasive changes to the original ("logic3") patch.

Note 2: I have not tried any ReSTification. But I would rather have it in 3.4 without Sphinx documentation, than having to rewrite the patches for this ticket for 3.4.1 again, given the age of the ticket. Wil might have an opinion on that.

Note 3: One of the six new files, the file "boolopt.py", says in it: "Copyright 2006 (c) Michael Greenberg.  NewBSD license, listed below ...". The terms listed are definitely compatible with GPLv2+, as far as I can tell, but IANAL. (The other five files are entirely written by Chris Gorecki, and are "Distributed under the terms of the GNU General Public License (GPL)".)

Note 4: This "other" file boolopt.py misses doctests on its own, but the functionality provided is well tested implicitly by using it in other ones of these six files. This is OK from my side, but probably a """nodoctests""" should be added --- or the code has to be refactored on a larger scale --- or this one file would have to be put in its own micro-spkg.

Note 5: There definitely is further work to be done on the "sage/logic/" part of Sage, e.g. the old "logic.py" file most probably should be thrown out, "all.py" should be adjusted, and so on. But please, please, please open new tickets for that!


---

Comment by mabshoff created at 2009-01-23 01:41:38

Resolution: fixed


---

Comment by mabshoff created at 2009-01-23 01:41:38

Merged logic4.patch and trac_545_latex.patch in Sage 3.3.alpha1. Note that two long doctests are broken, but they ought to be fixed before the final Sage 3.3 release. Merging this code is more important than letting it go staler.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 01:45:18

Reopened: The coverage of this code *sucks*:

```
mabshoff@geom:/scratch/mabshoff/sage-3.3.alpha1$ ./sage -coverageall devel//sage/sage/logic/
booleval.py: 100% (3 of 3)
boolformula.py: 93% (30 of 32)
boolopt.py: 0% (0 of 55)
logic.py: 16% (3 of 18)
logicparser.py: 100% (5 of 5)
logictable.py: 100% (4 of 4)
propcalc.py: 100% (1 of 1)
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 01:45:18

Resolution changed from fixed to 


---

Comment by mabshoff created at 2009-01-23 01:45:18

Changing status from closed to reopened.


---

Comment by GeorgSWeber created at 2009-01-23 20:27:15

Thanks for catching the two "long" doctest failures I let slip by. They're indeed trivial to fix.

Concerning the coverage: I'm at a loss here.

Please see my "Note 4" from above about the file "boolopt.py", which would have either to be refactored (i.e. rewritten) completely, or one would have to add lots of meaningless doctests, look at the following code snippet:

```
    def visit_prop(self, node, children):
        self.props.add(children[0])

    def visit_notprop(self, node, children):
        self.props.add(children[0])

    def transform_node(self, node, children):
        return [[tuple([node] + children)]]

    def transform_or(self, node, children):
        return children[0] + children[1]


```


Thoughts?

Cheers, gsw


---

Attachment

Apply first "logic4" then the "latex" one and after that this one patch


---

Comment by GeorgSWeber created at 2009-01-23 21:23:09

Urgh.

Currently this ticket already has three different patches to be applied from three different guys.

I've made my case, please another one step in and review this, thanks!

(The long doctests now do pass --- but there is the coverage problem, which is essentially a hen-and-egg problem: the code does not go into Sage because of the coverage, but who would work on code not being in Sage to make the coverage higher?)


---

Comment by robertwb created at 2009-01-23 21:33:38

In my experience, the motivation to increase coverage is the highest when trying to get something in. 

How essential is boolopt.py to the rest of the package? Could it be pushed to a separate ticket (enhancement). 

boolformula.py could probably be brought up to 100% without too much effort.


---

Comment by GeorgSWeber created at 2009-01-24 13:31:14

Ahh, excellent idea, this was just the input needed here. Robert, thank you very much!

So now what's to do (if nobody else does it, I'll do it):

- move the file "boolopt.py" to its own (enhancement) ticket "with patch, needs work" (easy)

- adjust the other five files of this patch so that they are stand-alone (rather easy, essentially only the "simplify" function in boolformula.py is concerned)

- add the two missing doctests to boolformula.py (very easy)

Please note that the file "logic.py" which has missing doctests according to the coverage report above is not among the new files, but already a part of Sage!
(So it couldn't possibly block this ticket to finally go in. But of course, it needs to be cleaned up itself.)


---

Comment by mabshoff created at 2009-01-24 13:39:33

Georg,

thanks for working on this since this is an incredible messy ticket. The main point here is that added functionality must be doctested while it is nice to increase the coverage on existing code that is being worked on. So I agree with the approach here. In addition you should open an enhancement ticket to get coverage of logic.py to 100%, too.

Cheers,

Michael


---

Attachment

Bring doctest coverage of boolformula.py up to 100%


---

Comment by mvngu created at 2009-02-25 10:16:50

Replying to [comment:42 GeorgSWeber]:
> - add the two missing doctests to boolformula.py (very easy)
This is done by `trac_545_boolformula-doctests.patch`.


---

Comment by mvngu created at 2009-02-25 10:23:53

So what happens here is one should apply the following in the specified order as suggested by Georg:


 1. first apply `logic4.patch`
 1. then `trac_545_latex.patch`
 1. and finally `trac_545_long-doctests-fixed.patch`

Now `trac_545_latex.patch` applied fine, but hunk #2 suceeded with fuzz, as reported by Georg. Apart from this fuzz, all the above three patches applied OK in the specified order against 3.4-alpha0. Doctests including `-long` passed. Having done so, one can then apply `trac_545_boolformula-doctests.patch` (based on 3.4-alpha0) which adds two missing doctests to `boolformula.py`.


---

Comment by mvngu created at 2009-04-27 13:03:13

based on sage-3.4.2.alpha0


---

Attachment

based on sage-3.4.2.alpha0


---

Attachment

based on sage-3.4.2.alpha0


---

Comment by mvngu created at 2009-04-27 13:07:14

Apply patches in the following order:
 1. `trac_545-logic5.patch` -- Basically the same as `logic4.patch`, but without including those diff lines for `boolopt.py`. The module `boolopt.py` is now moved to ticket #5910 as an enhancement.
 1. `trac_545-latex2.patch` -- Essentially the same as `trac_545_latex.patch`, but you won't see any fuzz when applying it.
 1. `trac_545_long-doctests-fixed.patch`
 1. `trac_545_boolformula-doctests.patch` -- This should bring doctest coverage of `boolformula.py` up to 100%.
 1. `trac_545-adjust-simplify.patch` -- This adjusts the method `simplify()` in `boolformula.py` and all doctests that uses `simplify()`. So this patch only touches `boolformula.py` and `propcalc.py`.
If I read this ticket correctly, I think only `trac_545_boolformula-doctests.patch` and `trac_545-adjust-simplify.patch` need to be reviewed.


---

Comment by whuss created at 2009-04-27 16:33:41

In the class BooleanFormula there is a spelling mistake in a function name,
"equivlant" instead of equivalent. The same mistake is repeated a few times
in the documentation.


---

Comment by whuss created at 2009-04-27 16:35:28

fix spelling mistakes


---

Attachment

apply after the other five patches instead of "equivlant.patch"


---

Comment by GeorgSWeber created at 2009-04-28 19:35:56

Minh, thanks for your good work!
After applying the five patches Minh mentioned in the correct order to Sage-3.4.2.alpha0, the equivlant.patch didn't apply. So I rebased and made it such that Wilfried's name appears in it as originator.

Positive review to the sequence of five patches Minh mentioned. And positive review to the changes of Wilfried (I really did nothing but rebase them). The main author here is Chris Gorecki, of course.

After this ticket is finally closed (Requiescat In Pacem), the next steps would be to dismiss "logic.py" (I think it becomes mostly obsolete by this patch here), add the "rest" as a logic chapter to the Sphinx documentation (probably this needs some work, but hopefully some scripts will be available to help), and finally work on/solve #5910. 

Cheers, gsw


---

Comment by mabshoff created at 2009-04-30 03:20:38

Merged 

 * trac_545-logic5.patch
 * trac_545-latex2.patch
 * trac_545_long-doctests-fixed.patch
 * trac_545_boolformula-doctests.patch
 * trac_545-adjust-simplify.patch
 * trac_545-equivlant_rebased.patch

in Sage 3.4.2.rc0. Note that there are some odd whitespace issues in those files, so if someone could take care of that at #5910 it would be splendid :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 03:20:38

Resolution: fixed

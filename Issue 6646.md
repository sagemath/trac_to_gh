# Issue 6646: R doctest failed

Issue created by migration from https://trac.sagemath.org/ticket/6646

Original creator: adavid

Original creation time: 2009-07-28 05:54:48

Assignee: was

Keywords: doctest


```
sage -t  "devel/sage/sage/interfaces/r.py"                  
**********************************************************************
File "/home/anthonyd/sage-4.1.1.alpha0/devel/sage/sage/interfaces/r.py", line 83
8:
    sage: r.completions('tes')
Expected:
    ['testPlatformEquivalence', 'testVirtual']
Got:
    <BLANKLINE>
    Building R command completion list (this takes
    a few seconds only the first time you do it).
    To force rebuild later, delete /home/anthonyd/.sage//r_commandlist.sobj.
    ['testPlatformEquivalence', 'testVirtual']
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_34
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/anthonyd/sage-4.1.1.alpha0/tmp/.doctest_r.py


cat /home/anthonyd/sage-4.1.1.alpha0/tmp/.doctest_r.py
sage -t  "devel/sage/sage/interfaces/r.py" 
# -*- coding: utf-8 -*-
from sage.all_cmdline import *; 
import sage.plot.plot; sage.plot.plot.DOCTEST_MODE=True

def warning_function(f):
    import warnings

    def doctest_showwarning(message, category, filename, lineno, file=f, line=None):
        try:
            file.write(warnings.formatwarning(message, category, 'doctest', lineno, line))
        except IOError:
            pass # the file (probably stdout) is invalid
    return doctest_showwarning

def change_warning_output(file):
    import warnings
    warnings.showwarning = warning_function(file)
def example_0():	r""">>> set_random_seed(0L)

>>> change_warning_output(sys.stdout)


   T-Test using R

   Arguments:
      x, y -- vectors of same length
      conf_level -- confidence level of the interval, [0,1) in percent

   Result:
      Tuple: (p-value, R return object)

   Example:
      >>> a, b = ttest([Integer(1),Integer(2),Integer(3),Integer(4),Integer(5)],[Integer(1),Integer(2),Integer(3),RealNumber('3.5'),RealNumber('5.121')]); a###line 30:_sage_    >>> a, b = ttest([1,2,3,4,5],[1,2,3,3.5,5.121]); a
      0.941026372027427
   """


if __name__ ==  '__main__':
    verbose = False
    do_timeit = False
    output_filename = '/home/anthonyd/sage-4.1.1.alpha0/devel/sage/sage/stats/r.py.timeit.sobj'

    import sys
    sys.path = sys.path + ['/home/anthonyd/sage-4.1.1.alpha0/local/bin']
    import sagedoctest

    # execfile('/home/anthonyd/sage-4.1.1.alpha0/devel/sage/sage/stats/r.py')
    m = sys.modules[__name__]
    m.__file__ = '/home/anthonyd/sage-4.1.1.alpha0/devel/sage/sage/stats/r.py'

    # configure special sage doc test runner
    runner = sagedoctest.SageDocTestRunner(checker=None, verbose=verbose, optionflags=0)
    runner._collect_timeit_stats = do_timeit
    runner._reset_random_seed = True

    runner = sagedoctest.testmod_returning_runner(m,
                   # filename='/home/anthonyd/sage-4.1.1.alpha0/devel/sage/sage/stats/r.py',
                   verbose=verbose,
                   globs=globals(),
                   runner=runner)
    runner.save_timeit_stats_to_file_named(output_filename)
    quit_sage(verbose=False)
    sys.exit(runner.failures)
```



---

Comment by GeorgSWeber created at 2009-07-28 17:08:40

That looks like #6594, fixed in Sage-4.1.1.alpha1.

The paths displayed in the output above indicate that Sage-4.1.1.alpha0 was tested, where the bug definitely occured.

So IMHO this ticket can safely be closed as a dupe.

Cheers,
Georg


---

Comment by mvngu created at 2009-07-28 18:11:15

The path name looks like it's Sage 4.1.1.alpha0. But it may be that adavid upgraded to Sage 4.1.1.alpha1 with that version and then ran doctests. One way to make sure is for adavid to have a look at the patch for #6594 and compare that with the file `sage/interfaces/r.py` in the version he doctested.


---

Comment by mvngu created at 2009-08-12 16:10:36

Resolution: duplicate


---

Comment by mvngu created at 2009-08-12 16:10:36

This is a duplicate of #6594.

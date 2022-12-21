# Issue 7197: basic statistics functions

Issue created by migration from Trac.

Original creator: amhou

Original creation time: 2009-10-12 23:26:09

Assignee: mhampton

Keywords: statistics, mean, median, mode, standard deviation

Basic statistics functions for a new class in Sage. Only descriptive statistics right now.


---

Comment by amhou created at 2009-10-14 02:52:45

Changing status from new to needs_review.


---

Comment by jason created at 2009-10-14 21:33:32

Some comments:

1. The arguments for std and variance don't seem very user-friendly.  I think it would be much better to have "sample=True/False" or "population=True/False", or maybe something more general like numpy: "ddof=<number>" (delta degrees of freedom), where the denominator is n-ddof (so ddof=1 is sample, ddof=0 is population).

2. When calling the std or variance methods of the object, the population vs. sample distinction is ignored.

2. Why are these methods in a class?  They don't seem to use any benefits of a class; they just seem to be standalone functions.  It seems like it would make much more sense to me to have these methods be just functions inside of the module.  We can still import them into a namespace called "stats".


---

Comment by jason created at 2009-10-14 21:33:32

Changing status from needs_review to needs_work.


---

Comment by jason created at 2009-10-14 21:34:34

I should also say I'm glad you are working on these!  I was very surprised to learn a few weeks ago that Sage did not have a generic standard deviation function.  We needed it in the class I was teaching!


---

Comment by amhou created at 2009-10-26 06:05:30

Changing status from needs_work to needs_review.


---

Attachment

Patch added. 

Arguments for std and variance changed to "bias = True/False" for division by n and n-1 respectively.


---

Comment by amhou created at 2009-10-26 06:05:42

Changing assignee from mhampton to amhou.


---

Comment by jason created at 2009-10-26 14:00:15

Is there any way to have "std_sample" and "std_population" (and same for variance)?  When teaching very basic classes statistics, we just refer to them as population and sample std or variance.  Having specific functions (as excel or their calculators do) would make more sense to students.


---

Attachment


---

Comment by was created at 2009-10-26 23:37:59

Changing status from needs_review to needs_work.


---

Comment by was created at 2009-10-26 23:37:59

REFEREE REPORT:

  0. All tests pass in the entire tree after applying this.

  1. I'm OK with not adding std_sample and std_population simply because R, matlab, mathematica all don't and the instructor can easily add some alias's for their class. 

  2. Add copyright header block.

  3. Add a docstring section at the top with AUTHOR, overview of capabilities, etc. 

  4. Don't import numpy at top level; it'll just get moved later since we should not import numpy/matplotlib/etc. at startup. 

  5. For `def std(v, bias=False):` and any other function that handles special types, put in examples that illustrate that your code for handling these types works. 

Fix all the above and I'll be happy with this patch!


---

Attachment


---

Comment by amhou created at 2009-11-08 00:50:20

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by was created at 2009-11-12 22:43:23

REPORT 2:

1. a little too spartan:

```
"""
Basic Statistics

This file contains basic descriptive functions.

AUTHOR:
    - Andrew Hou (11/06/2009)
...
"""
```


2. Make sure there is a test that tests this code:

```
    """
    if hasattr(v, 'mean'): return v.mean()
```


3. Same for mode:

```
    if hasattr(v, 'mode'): return v.mode()
```


4. Same for this:

```
    if hasattr(v, 'standard_deviation'): return v.standard_deviation(bias=bias)
```


5. Type checking in python should always use isinstance:

```
    if type(v) is numpy.ndarray:
    if type(v) == numpy.ndarray:
```

should be

```
     if isinstance(v, numpy.ndarray):
```


6. Test this:

```
    if hasattr(v, 'variance'): return v.variance(bias = bias)
```


7. Change this:

```
    if bias == True:
        # population variance
        if isinstance(x, (int,long)):
            return x/ZZ(len(v))
        return x/len(v)
    elif bias == False:
```

to

```
    if bias:
        # population variance
        if isinstance(x, (int,long)):
            return x/ZZ(len(v))
        return x/len(v)
    else:
```



8. Make sure this is tested:

```
    if hasattr(v, 'median'): return v.median()
```


9. Weird """ in moving_average:
{{{ 	318	                                                                                    """ 
 	319	    x = []    
}}}

10. Change

```
    bin_size = len(v)/bins     
```

to floor division:

```
    bin_size = int(len(v)//bins)
```


11. You can do this at the very end of each docstring if you want...

```
    AUTHOR:

       - Andrew Hou (11/06/2009)
```



---

Comment by was created at 2009-11-12 22:43:39

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by amhou created at 2009-11-16 08:15:50

Changing status from needs_work to needs_review.


---

Comment by was created at 2009-11-17 00:30:55

Issues:

 * Delete "Included as of 11/06/2009" and reword.

 * Fix: "returns the most common occuring member of a sample."  (and occurring is the right spelling)

 * "Functions have also been imported under the namespace 'stats'."  Change to not use the passive voice.  I.e., "The functions are available in the namespace _stats_, i.e., you can use them by typing _stats.mean_, _stats.median_, etc."

 * Change all ' to _ in the top section.   _ (two single quotes as separate characters) means "monospace" in ReST markup.


---

Attachment


---

Attachment


---

Attachment


---

Comment by was created at 2009-11-24 01:04:03

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-25 06:45:35

All of the above patches folded together.  Apply only this patch.


---

Attachment


---

Comment by mhansen created at 2009-11-29 05:07:20

Resolution: fixed

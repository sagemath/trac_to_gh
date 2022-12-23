# Issue 5606: complex color plotting

Issue created by migration from https://trac.sagemath.org/ticket/5606

Original creator: robertwb

Original creation time: 2009-03-25 03:50:59

Assignee: was

It's really a shame Sage can't produce graphics like http://commons.wikimedia.org/wiki/User:Jan_Homann/Mathematics yet. 


---

Attachment


---

Comment by robertwb created at 2009-03-25 04:03:18

It's still a bit slow, #5093 should fix this.


---

Comment by was created at 2009-04-09 06:37:37

REFEREE REPORT:

* Coverage isn't 100%:


```
teragon:sage-3.4 wstein$ sage -coverage devel/sage/sage/plot/complex_plot.pyx 
----------------------------------------------------------------------
devel/sage/sage/plot/complex_plot.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE devel/sage/sage/plot/complex_plot.pyx: 85% (6 of 7)

Missing doctests:
	 * get_minmax_data(self):


Possibly wrong (function name doesn't occur in doctests):
	 * _render_on_subplot(self, subplot):

```


* I was puzzled why I couldn't change the aspect ratio (this is *not* a general problem with contour plots (say) in Sage):

```
time complex_plot(zeta, (-5, 5), (-5, 5)).show(aspect_ratio=4)
```


Otherwise the code looks very *very* good.


---

Comment by robertwb created at 2009-04-09 07:45:28

I added a doctest to get coverage up to 100%. 

As for the aspect ratio issue, no idea. The same happens with density_plot: 


```
sage: density_plot(sin(x) - sin(y), (-5,5), (-5,5)).show(aspect_ratio=4)
```


Maybe we could move that to a new ticket.


---

Comment by mabshoff created at 2009-04-10 02:34:03

The second and third hunk in 5606-complex-plot.patch are already in Sage via another patch, so I am attaching the version I merged (assuming doctests pass for me).

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-10 02:37:27

Hmm, there are also the following two doctest failures:

```
sage -t -long devel/sage/sage/plot/complex_plot.pyx
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage-main/sage/plot/complex_plot.pyx", line 146:
    sage: p = complex_plot(x^2-1, (-2, 2), (-2, 2))
Expected nothing
Got:
    doctest:325: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)
    doctest:5554: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)
    doctest:5545: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage-main/sage/plot/complex_plot.pyx", line 162:
    sage: p.get_minmax_data()
Expected:
    {'xmax': 2.0, 'xmin': -1.0, 'ymax': 4.0, 'ymin': -3.0}
Got:
    {'xmin': -1.0, 'ymin': -3.0, 'ymax': 4.0, 'xmax': 2.0}
**********************************************************************
```


The first one is trivial to fix by adding the variables to the plot ranges, the second one is caused by the dictionary being printing differently, so it might be a good idea to print the minmax_data as a list in a consistent format.

I am bumping this ticket to 3.4.2 - if it is fixed it can still go into 3.4.1.

Cheers,

Michael


---

Attachment


---

Comment by robertwb created at 2009-04-10 06:41:59

I've updated the patch, should pass doctests now.


---

Comment by was created at 2009-04-10 14:33:26

> I've updated the patch, should pass doctests now. 

As a reviewer I am finding this very annoying.  It means I have to somehow revert the patch in my own tree before I can safely apply yours *and* it makes it very very hard for me to see what you actually changed.  I would *much* rather have a part 2 patch that applies on top of the first one. 

On a clean 3.4.1.rc1 build (which I think never had #5606 applied, so far as I can tell) I get:

```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/5606/5606-complex-plot.patch'
)
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5606/5606-complex-plot.patch
Loading: [..]
cd "/scratch/wstein/build/sage-3.4.1.rc1/devel/sage" && hg status
cd "/scratch/wstein/build/sage-3.4.1.rc1/devel/sage" && hg status
cd "/scratch/wstein/build/sage-3.4.1.rc1/devel/sage" && hg import   "/scratch/wstein/sage/temp/sage.math.washington.edu/1031/tmp_2.patch"
applying /scratch/wstein/sage/temp/sage.math.washington.edu/1031/tmp_2.patch
patching file sage/misc/log.py
Hunk #1 FAILED at 64
1 out of 1 hunks FAILED -- saving rejects to file sage/misc/log.py.rej
patching file sage/misc/mathml.py
Hunk #1 FAILED at 26
1 out of 1 hunks FAILED -- saving rejects to file sage/misc/mathml.py.rej
file sage/plot/complex_plot.pyx already exists
1 out of 1 hunks FAILED -- saving rejects to file sage/plot/complex_plot.pyx.rej
abort: patch failed to apply

sage: hg_sage.log()
changeset:   11933:470a0a0e9a2c
tag:         tip
user:        mabshoff@sage.math.washington.edu
date:        Sun Apr 05 23:49:53 2009 -0700
summary:     3.4.1.rc1

...
```



---

Comment by mabshoff created at 2009-04-10 17:34:45

Just FYI: As mentioned above two hunk that delete and import of "sage.plot.all" in log.py and mathml.py need to be deleted since they are already gone in 3.4.1.rc1. Then the patch applies and passes doctests for me.

Cheers,

Michael


---

Comment by robertwb created at 2009-04-10 18:15:48

Sorry, I will post a separate patch next time. Ironically, I've had people complain to me about that behavior too, but usually it's when the list of patches gets cumbersome.


---

Attachment

This version of the patch removes the two hunk in Robert's patch that are already in 3.4.1.rc1


---

Comment by mabshoff created at 2009-04-10 20:39:27

trac_5606-complex-plot.patch does apply to my merge tree and pass long doctests.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-11 00:10:59

Merged rac_5606-complex-plot.patch in Sage 3.4.1.rc2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-11 00:10:59

Resolution: fixed

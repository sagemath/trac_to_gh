# Issue 6648: [with patch, needs review] adds riemann mapping and complex interpolation

Issue created by migration from https://trac.sagemath.org/ticket/6648

Original creator: evanandel

Original creation time: 2009-07-28 17:10:46

Assignee: evanandel

CC:  robertwb

Keywords: complex

This patch add's Riemann mapping functionality to sage: http://en.wikipedia.org/wiki/Riemann_mapping_theorem

It can compute numerical maps and has multiple utilities for plotting/visualizing the maps.

It also includes 2 functions to parametrically interpolate lists of complex points. This makes it far easier for the user to define the boundary of the figure that they wish to Riemann map.


---

Comment by evanandel created at 2009-07-28 17:11:20

patch for riemann and comp interpolation


---

Attachment

Replying to [ticket:6648 evanandel]:
> This patch add's Riemann mapping functionality to sage: http://en.wikipedia.org/wiki/Riemann_mapping_theorem
> 
> It can compute numerical maps and has multiple utilities for plotting/visualizing the maps.
> 
> It also includes 2 functions to parametrically interpolate lists of complex points. This makes it far easier for the user to define the boundary of the figure that they wish to Riemann map.


---

Comment by wdj created at 2009-07-28 17:33:40

On an intel macbook running 10.4.11, I got this:


```
zeus:~/sagefiles/sage-4.1.1.alpha0 davidjoyner$ ./sage 
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: rmap
sage: hg_sage.apply("/Users/davidjoyner/sagefiles/12659.patch")
cd "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage" && hg status
/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.
  x = os.popen3(s)
cd "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage" && hg status
cd "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage" && hg import   "/Users/davidjoyner/sagefiles/12659.patch"
applying /Users/davidjoyner/sagefiles/12659.patch
sage: 
Exiting SAGE (CPU time 0m0.18s, Wall time 0m45.59s).
zeus:~/sagefiles/sage-4.1.1.alpha0 davidjoyner$ ./sage -br
| Sage Version 4.1.1.alpha0, Release Date: 2009-07-22                |
| Type notebook() for the GUI, and license() for information.        |
----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Building modified file sage/calculus/riemann.pyx.
Building modified file sage/calculus/interpolators.pyx.
python `which cython` --embed-positions --incref-local-binop -I/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage-rmap -o sage/calculus/riemann.c sage/calculus/riemann.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...

cdef class Riemann_Map:
    cdef int N, B, ncorners
    cdef f
    cdef opp
    cdef double complex a
                       ^
------------------------------------------------------------

/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage-rmap/sage/calculus/riemann.pyx:62:24: Syntax error in C variable declaration
Error running command, failed with status 256.
sage: There was an error installing modified sage library code.

```



Any idea what the problem is?


---

Attachment


---

Comment by evanandel created at 2009-07-29 13:57:36

> Error converting Pyrex file to C:
> ------------------------------------------------------------
> ...
> 
> cdef class Riemann_Map:
>     cdef int N, B, ncorners
>     cdef f
>     cdef opp
>     cdef double complex a
>                        ^
> ------------------------------------------------------------
> 
> /Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage-rmap/sage/calculus/riemann.pyx:62:24: Syntax error in C variable declaration
> Error running command, failed with status 256.
> sage: There was an error installing modified sage library code.
> 
> }}}
> 
> 
> Any idea what the problem is?

That's a problem with sage's cython version. You need to update to 0.11.2. 
According to Mike Hanson:

" There is a ticket to update Cython in Sage at
http://trac.sagemath.org/sage_trac/ticket/6438.  If you download
http://sage.math.washington.edu/home/robertwb/cython/cython-0.11.2.spkg
and run "sage -f /path/to/cython-0.11.2.spkg", then Cython 0.11.2 will
be used.

--Mike "


---

Comment by wdj created at 2009-07-30 12:14:40

I applied only the 2nd patch to 4.1.1.a0. It seemed to work fine trying out several examples form the docstrings by had. However, on an intel macbook running 10.4.11 there were several failures of sage -testall:


```
        sage -t  "devel/sage/doc/en/bordeaux_2008/birds_other.rst"
        sage -t  "devel/sage/sage/calculus/interpolators.pyx"
        sage -t  "devel/sage/sage/interfaces/psage.py"
        sage -t  "devel/sage/sage/interfaces/sage0.py"
        sage -t  "devel/sage/sage/parallel/decorate.py"
        sage -t  "devel/sage/sage/symbolic/expression.pyx"
```


Some of these are probably spurious but some are not:


```
zeus:~/sagefiles/sage-4.1.1.alpha0 davidjoyner$ ./sage -t  "devel/sage/sage/calculus/interpolators.pyx"
sage -t  "devel/sage/sage/calculus/interpolators.pyx"       
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/calculus/interpolators.pyx", line 89:
    sage: ps.value(10)
Expected:
    (0.2676045526483728+1j)
Got:
    (0.26760455264837191+1j)
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/calculus/interpolators.pyx", line 146:
    sage: cs.derivative(2)
Expected:
    (-0.049776540658333007+0.15109500643420509j)
Got:
    (-0.049776539604289502+0.15109500674962709j)
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/calculus/interpolators.pyx", line 221:
    sage: cs.derivative(3/5)
Expected:
    (1.4057889232733602-0.22541713632654017j)
Got:
    (1.4057889243877602-0.22541713160563243j)
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/calculus/interpolators.pyx", line 225:
    sage: cs.derivative(-6)
Expected:
    (2.5204769294914593-1.8939258831078529j)
Got:
    (2.5204768628640499-1.8939257072489877j)
**********************************************************************
3 items had failures:
   1 of   7 in __main__.example_2
   1 of  12 in __main__.example_4
   2 of   7 in __main__.example_6
***Test Failed*** 4 failures.
For whitespace errors, see the file /Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/tmp/.doctest_interpolators.py
         [45.7 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/calculus/interpolators.pyx"
```


This looks like numerical noise but I'm not sure. In any case, it is in a file you modified, so it
is probably not spurious.


---

Comment by evanandel created at 2009-07-30 13:56:35

I'm not sure about the ps.value failure, that does look like numerical noise. The cs ones were my mistake when creating the new patch. There's yet another version up now that should *fingers crossed* work better. 

The whole package is highly dependent on numerical methods, so noise wouldn't surprise me, but maybe it should.


---

Attachment


---

Comment by wdj created at 2009-07-30 18:33:24

The patch 12659.3.patch applied fine (after upgrading cython as mentioned already).
However, sage -testall failed again, this time on an amd64 ubuntu 9.04 machine:


```
wdj@hera:~/sagefiles/sage-4.1.1.alpha1$ ./sage -t  "devel/sage/sage/calculus/interpolators.pyx"
sage -t  "devel/sage/sage/calculus/interpolators.pyx"                                          
**********************************************************************                         
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/calculus/interpolators.pyx", line 89:
    sage: ps.value(10)                                                                           
Expected:                                                                                        
    (0.2676045526483728+1j)                                                                      
Got:                                                                                             
    (0.26760455264837191+1j)                                                                     
**********************************************************************                           
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/calculus/interpolators.pyx", line 146:
    sage: cs.derivative(2)                                                                        
Expected:                                                                                         
    (-0.049776540658333007+0.15109500643420509j)                                                  
Got:                                                                                              
    (-0.049776540658333021+0.15109500643420506j)                                                  
**********************************************************************
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/calculus/interpolators.pyx", line 221:
    sage: cs.derivative(3/5)
Expected:
    (1.4057889232733602-0.22541713632654017j)
Got:
    (1.4057889232733602-0.22541713632654015j)
**********************************************************************
3 items had failures:
   1 of   7 in __main__.example_2
   1 of  12 in __main__.example_4
   1 of   7 in __main__.example_6
***Test Failed*** 3 failures.
For whitespace errors, see the file /home/wdj/sagefiles/sage-4.1.1.alpha1/tmp/.doctest_interpolators.py
         [6.4 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/calculus/interpolators.pyx"
Total time for all tests: 6.4 seconds
```



---

Comment by evanandel created at 2009-07-30 19:18:39

Hmm... It runs fine for me, intel t3200, ubuntu 9.04

I'm afraid I'm not knowledgeable enough to pinpoint the exact source of the differences. Is there some sort of flag that can make the test routine ignore numerical differences of a certain size?

Is there some other way that it should be fixed?


---

Comment by wdj created at 2009-07-30 19:39:52

Replying to [comment:7 evanandel]:
> Hmm... It runs fine for me, intel t3200, ubuntu 9.04
> 
> I'm afraid I'm not knowledgeable enough to pinpoint the exact source of the differences. Is there some sort of flag that can make the test routine ignore numerical differences of a certain size?
> 
> Is there some other way that it should be fixed?

Yes there is such a "flag" but I am the wrong person to ask! I would ask Carl Witty, if you can get a hold of him. If that fails, just post to sage-support something about keeping track of numerical noise doctest failures.


---

Comment by evanandel created at 2009-07-31 14:03:07

Alright, new patch up. It truncates the required precision a bit.


---

Attachment

This passes sage -testall (except for the known failures for 4.1.1.a1 on an amd64 ubuntu 9.04 machine).

Positive review from me. Should it undergo more testing?


---

Comment by evanandel created at 2009-07-31 20:02:06

If that question is directed to me (I'm new to this), I don't _think_ so. Do I need to do anything other than change the summary to [with patch, positive review]?

Regardless, thank you for the time you spent.


---

Comment by wdj created at 2009-07-31 22:36:16

I'm changing this to postive review.

Minh - if you want me to wait until a warnignless version of sage is released, please let me know and I'll be happy to retest.


---

Comment by malb created at 2009-08-04 11:28:41

This patch needs work:


```
malb@sage:~/sage-4.1/devel$ sage -coverage sage/sage/calculus/interpolators.pyx
----------------------------------------------------------------------
sage/sage/calculus/interpolators.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE sage/sage/calculus/interpolators.pyx: 75% (6 of 8)

Missing documentation:
         * __init__(self,pts,shift = (0,0)):
         * __init__(self,pts):

----------------------------------------------------------------------
```




```
malb@sage:~/sage-4.1/devel$ sage -coverage sage/sage/calculus/riemann.pyx
----------------------------------------------------------------------
sage/sage/calculus/riemann.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE sage/sage/calculus/riemann.pyx: 50% (7 of 14)

Missing documentation:
         * _repr_(self):
         * __init__(self, z_values, xrange, yrange):
         * get_minmax_data(self):
         * _allowed_options(self):
         * _repr_(self):
         * _render_on_subplot(self, subplot):


Missing doctests:
         * __init__(self,fs,fprimes,a,int N = 500,int ncorners = 4,opp = False):
```


Also, should these files be added to the reference manual?


---

Attachment

Alright, new patch is up that fixes the missing documentation.

What would adding the files to the reference manual entail?


---

Comment by wdj created at 2009-08-15 21:37:29

> What would adding the files to the reference manual entail?

http://www.sagemath.org/doc/developer/sage_manuals.html#editing-the-manuals

Also: is it correct that only the last (of the five) patch is to be applied?


---

Comment by evanandel created at 2009-08-16 04:23:05

Correct, only the last patch should be applied.

From a quick look it seems that this should be added to the basic reference manual, but nowhere else. I'm on vacation now, so those edits may take a bit. I'll probably put them in a separate patch.


---

Comment by wdj created at 2009-08-16 15:19:48

I applied the 5th patch to 4.1.1.rc2 on an intel macbook runing 10.4.11. I got


```
The following tests failed:


        sage -t  "devel/sage/doc/en/bordeaux_2008/birds_other.rst"
        sage -t  "devel/sage/sage/interfaces/maxima.py"
        sage -t  "devel/sage/sage/symbolic/expression.pyx"
```

None of these failures seem related. So this patch seems to be okay except for the reference manual addition. The patch author (in an offlist email)  said he would add another patch soon for the ref manual, so I am changing this to "needs work" for that reason.  I cannot vouch for the Cython or mathematics, though from the experimentation I did, I cn't find a problem.


---

Comment by evanandel created at 2009-08-27 17:36:41

New Patch, should add it to the reference manual properly (I hope).
This patch is independent from the prefious ones, that is you need to install both the latest 12659 and the 12660.


---

Attachment

Passes as before, so I give this a positive review again. However, I don't know how to check the reference docs, or what should be checked. Or is that part of the refereeing processing?


---

Comment by wdj created at 2009-08-30 15:29:18

I checked that the html built as part of the reference manual.


---

Comment by mvngu created at 2009-08-31 07:40:08

I assume that patches should be merged in this order:

 1. `12659.5.patch`
 1. `12660.patch`

These patches apply OK against Sage 4.1.1, with `12660.patch` resulting in some fuzz:

```
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6648/12660.patch && hg qpush
adding 12660.patch to series file
applying 12660.patch
patching file module_list.py
Hunk #1 succeeded at 125 with fuzz 2 (offset 8 lines).
patching file sage/calculus/all.py
Hunk #1 succeeded at 20 with fuzz 2 (offset 4 lines).
Now at: 12660.patch
```

Don't worry about the fuzz. However, building the reference manual results in 17 warnings:

```
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: :0: (ERROR/3) Unexpected indentation.
WARNING: :0: (ERROR/3) Unexpected indentation.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/calculus/riemann.so:docstring of sage.calculus.riemann:3: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/calculus/riemann.so:docstring of sage.calculus.riemann:5: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/calculus/riemann.so:docstring of sage.calculus.riemann:3: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/calculus/riemann.so:docstring of sage.calculus.riemann:5: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/calculus/riemann.so:docstring of sage.calculus.riemann.ColorPlot.get_minmax_data:5: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
pickling environment... done
checking consistency... done
preparing documents... done
writing output... calculus index sage/calculus/interpolators sage/calculus/riemann 
writing additional files... genindex modindex search
copying static files... done
dumping search index... done
dumping object inventory... done
build succeeded, 17 warnings.
```

Two crucial doctests are missing:

```
[mvngu@sage sage-4.1.1]$ ./sage -coverage devel/sage-main/sage/calculus/interpolators.pyx
----------------------------------------------------------------------
devel/sage-main/sage/calculus/interpolators.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE devel/sage-main/sage/calculus/interpolators.pyx: 100% (8 of 8)
----------------------------------------------------------------------

[mvngu@sage sage-4.1.1]$ ./sage -coverage devel/sage-main/sage/calculus/riemann.pyx
----------------------------------------------------------------------
devel/sage-main/sage/calculus/riemann.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE devel/sage-main/sage/calculus/riemann.pyx: 100% (14 of 14)

Possibly wrong (function name doesn't occur in doctests):
         * _render_on_subplot(self, subplot):

----------------------------------------------------------------------
```

And I get some doctest failure, which are mostly numerical noise:

```
sage -t -long devel/sage-main/sage/calculus/riemann.pyx
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/calculus/riemann.pyx", line 459:
    sage: m.inverse_riemann_map(.95) #long time
Expected:
    (0.486319431795...-4.90019052414...e-06j)
Got:
    (0.48631943179594372-4.9001905240969853e-06j)
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/calculus/riemann.pyx", line 394:
    sage: m.riemann_map(1.3*I) #long time
Expected:
    (-1.56102939636...e-05+0.989694535737...j)
Got:
    (-1.5610293963970239e-05+0.98969453573774413j)
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/calculus/riemann.pyx", line 398:
    sage: m.riemann_map(.4) #long time
Expected:
    (0.733242677182...+3.50767714620...e-06j)
Got:
    (0.73324267718245462+3.5076771462558728e-06j)
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/calculus/riemann.pyx", line 402:
    sage: m.riemann_map(np.complex(-3,.0001)) #long time
Expected:
    (1.40575713549...e-05+1.05106170694...e-09j)
Got:
    (1.4057571354958779e-05+1.0510616458088591e-09j)
**********************************************************************
2 items had failures:
   1 of   8 in __main__.example_10
   3 of   9 in __main__.example_8
***Test Failed*** 4 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_riemann.py
	 [76.3 s]
```



---

Comment by wdj created at 2009-08-31 09:42:11

I don't think I saw any of these latex/noise problems with an intel mac 10.4.11. (I'll be upgrading very soon to 10.6, whcih might help though.) However, I did see the "fuzz" on applying 12660.patch. I didn't know that was a problem though.


---

Comment by evanandel created at 2009-10-03 18:18:52

Alright, I'm back to working on this again.
Questions:

How far should I tell the doctests to ignore the numerical noise? 
Is there some point where I should start trying to track down and fix the cause? 
Is that even possible?

Should I be worried about the reference manual compilation warnings?


---

Attachment

based on Sage 4.3.alpha1


---

Comment by mvngu created at 2009-12-05 19:57:28

*Referee Report*



I have attached the reviewer patch `trac_6648-reviewer.patch`. My changes include:

 1. Proper ReST formatting to resolve dozens of warnings when building the HTML version of the reference manual.
 1. Fix various typos.
 1. Some formatting of the docstrings to keep them less than 80 characters wide. Beyond 80 characters, the docstring can be difficult to read from the command line interface.
 1. Proper formatting of code so it conforms to Python coding conventions as covered in the [Developers' Guide](http://www.sagemath.org/doc/developer/conventions.html#python-coding-conventions).
 1. In the file `sage/calculus/riemann.pyx`, don't redefine `xrange`, which is a built-in command of Python. Instead, define `x_range` and similarly define `y_range`. Also, don't use the name `list` as a parameter to the function `comp_pt()` because `list` is the name of the Python function for creating a list data structure. I have changed it to `clist` instead.
 1. For the file `sage/calculus/riemann.pyx`, in the `__init__()` method of the class `Riemann_Map`, I changed the test
 {{{
if <= 2:
    ...
 }}}
 to raise an exception instead. That is, if the number of collocations points is less than 3, then you don't want to proceed any further with initializing the `Riemann_Map` object.


You should apply patches in this order:

 1. `12659.5.patch`
 1. `12660.patch`
 1. `trac_6648-reviewer.patch`
 
The reviewer patch should resolve doctest failures and reference manual build warnings that I reported above. So my patch needs some reviewing. Also, here are some required changes once patches are applied in the above order:

 1. In the file `sage/calculus/riemann.pyx`, you need to explain what the function `_render_on_subplot` does.
 1. Also, you need to explain the purpose of the class `ColorPlot` and provide examples in the docstring of that class.
 1. In the file `sage/calculus/interpolators.pyx`, explain the purpose of the class `PSpline` and provide examples in the docstring of that class.
 1. Explain the purpose of the class `CCSpline` and provide examples in its docstring.


---

Comment by wdj created at 2009-12-05 23:00:20

I don't mind refereeing this after next week, but would first like to know
the author's response to this patch. Possibly another patch needs to be added?

Also, thanks Minh!

Replying to [comment:24 mvngu]:
> *Referee Report*
> 

> 
> I have attached the reviewer patch `trac_6648-reviewer.patch`. My changes include:
> 
>  1. Proper ReST formatting to resolve dozens of warnings when building the HTML version of the reference manual.
>  1. Fix various typos.
>  1. Some formatting of the docstrings to keep them less than 80 characters wide. Beyond 80 characters, the docstring can be difficult to read from the command line interface.
>  1. Proper formatting of code so it conforms to Python coding conventions as covered in the [Developers' Guide](http://www.sagemath.org/doc/developer/conventions.html#python-coding-conventions).
>  1. In the file `sage/calculus/riemann.pyx`, don't redefine `xrange`, which is a built-in command of Python. Instead, define `x_range` and similarly define `y_range`. Also, don't use the name `list` as a parameter to the function `comp_pt()` because `list` is the name of the Python function for creating a list data structure. I have changed it to `clist` instead.
>  1. For the file `sage/calculus/riemann.pyx`, in the `__init__()` method of the class `Riemann_Map`, I changed the test
>  {{{
> if <= 2:
>     ...
>  }}}
>  to raise an exception instead. That is, if the number of collocations points is less than 3, then you don't want to proceed any further with initializing the `Riemann_Map` object.
> 
> 
> You should apply patches in this order:
> 
>  1. `12659.5.patch`
>  1. `12660.patch`
>  1. `trac_6648-reviewer.patch`
>  
> The reviewer patch should resolve doctest failures and reference manual build warnings that I reported above. So my patch needs some reviewing. Also, here are some required changes once patches are applied in the above order:
> 
>  1. In the file `sage/calculus/riemann.pyx`, you need to explain what the function `_render_on_subplot` does.
>  1. Also, you need to explain the purpose of the class `ColorPlot` and provide examples in the docstring of that class.
>  1. In the file `sage/calculus/interpolators.pyx`, explain the purpose of the class `PSpline` and provide examples in the docstring of that class.
>  1. Explain the purpose of the class `CCSpline` and provide examples in its docstring.


---

Comment by evanandel created at 2009-12-09 05:37:27

Thank you Minh. 
I will happily put up another patch with the doc additions you suggested. However, exams are starting for me, so I probably won't be able to get around to it for 2 weeks or so.

In addition, it's not clear to me that your patch fixes the primary problem, namely that the class doesn't know how to dump/save itself, and therefore wont pass the TestSuite test. Fixing that is outside my abilities.


---

Comment by mvngu created at 2009-12-09 05:39:53

Replying to [comment:26 evanandel]:
> In addition, it's not clear to me that your patch fixes the primary problem, namely that the class doesn't know how to dump/save itself, and therefore wont pass the TestSuite test. Fixing that is outside my abilities.

Ah... I forgot about the dump/save test. I'll work on that.


---

Comment by evanandel created at 2010-03-20 02:37:11

Replying to [comment:27 mvngu]:
> Replying to [comment:26 evanandel]:
> > In addition, it's not clear to me that your patch fixes the primary problem, namely that the class doesn't know how to dump/save itself, and therefore wont pass the TestSuite test. Fixing that is outside my abilities.
> 
> Ah... I forgot about the dump/save test. I'll work on that.
Sorry for the delay, this project has been buried for a while for me. I should have my patch up in a week or so.

Minh, did you ever have any luck addressing the TestSuite issue?
I'd really like to see this get finalized and out there.


---

Comment by mvngu created at 2010-03-20 02:48:44

Replying to [comment:28 evanandel]:
> Minh, did you ever have any luck addressing the TestSuite issue?
> I'd really like to see this get finalized and out there.

I must apologize for the delay. I'm just as stuck as you are concerning the TestSuite thing. Please see my post to [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/2d84701b47e6d3ee).


---

Comment by evanandel created at 2010-03-31 04:13:57

Doc fixes


---

Attachment

Ok, I've put up a patch that fixes the missing documentation. Note that the relatively sparse documentation in the ColorPlot and _render_on_subplot is more than exists in the complex_plot module from which I obtained the code.

At this point all that is required is some kind knowledgeable soul to implement dump/load functionality so that the modules can pass the TestSuite requirement. Alternately direct me to a resource that provides an in depth tutorial on how to implement it. I appreciate all the help so far, and I would really like to get this published. If there's anything that I can do to speed it up, let me know.


---

Comment by wdj created at 2010-04-01 12:22:21

Changing status from needs_work to needs_info.


---

Comment by wdj created at 2010-04-01 12:22:21

I applied 12659.5.patch, 12660.patch, trac_6648-reviewer.patch without much problem (there were some fuzz warnings). However, 12661.patch failed to apply. This is on a 10.6.2 mac running sage 4.3.5.

There is no indication which patches to apply, so maybe this is not the intended sequence?


---

Comment by evanandel created at 2010-04-20 01:40:34

New Monolithic patch. Apply only this one.


---

Comment by evanandel created at 2010-04-20 01:41:00

Changing status from needs_info to needs_work.


---

Attachment

My apologies, I apparently made some mistakes with mercurial and somehow produced someone else's patch. Regardless, I have created a new, monolithic patch that should be applied INSTEAD of applying the previous patches. It incorporates all the changes so far including the ones that I intended to be in 12661.


---

Comment by wdj created at 2010-04-22 11:30:46

Changing status from needs_work to needs_review.


---

Comment by wdj created at 2010-04-22 11:30:46

This patch applies fine to 4.4.a1 and passes sage -testall on a 10.6.2 mac (except for the already reported and unrelated r.py failure). Also, sage -coverage reports 100%. It produces some cool graphs and I think will help people doing teaching or research in classical complex analysis.

Positive review from me.


---

Comment by wdj created at 2010-04-22 11:33:39

Changing status from needs_review to positive_review.


---

Comment by wdj created at 2010-04-22 11:33:39

As far as I can see, the author has addressed the comments of Martin and Minh above.


---

Comment by jason created at 2010-04-24 00:47:51

I'm excited to explore this functionality and show it to a fellow faculty member who does projects with students in complex analysis.

Things could probably be sped up quite a bit if the class used fast_callable to "compile" the functions.  For example:


```
sage: ff=fast_callable(e^(I*t),domain=CDF,vars=['t'])
sage: gg=fast_callable(I*e^(I*t),domain=CDF,vars=['t'])
sage: %time m = Riemann_Map([ff], [gg], 0, 1000)
CPU times: user 2.44 s, sys: 0.12 s, total: 2.56 s
Wall time: 2.57 s
sage: %time m = Riemann_Map([lambda t: e^(I*t)], [lambda t: I*e^(I*t)], 0, 1000) 
CPU times: user 21.25 s, sys: 0.25 s, total: 21.50 s
Wall time: 23.13 s
```


Notice that the fast_callable version is an order of magnitude faster.

I don't think this patch ought to be delayed for this, but it would be a good additional ticket to speed up this functionality quite a bit by using fast_callable.


---

Comment by evanandel created at 2010-04-24 04:40:53

Good point Jason.

Starting next fall I plan to develop this further as my senior project in math and CS. I have several ideas planned including parallelization and fast-callable. However, if it would be helpful to have it sooner rather than later, I have no problem doing some basic work now (or having someone else do it if that is preferred).


---

Comment by was created at 2010-04-29 05:32:08

Resolution: fixed

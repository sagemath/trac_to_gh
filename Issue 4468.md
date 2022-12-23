# Issue 4468: assertion error when (some) bad color map given

Issue created by migration from https://trac.sagemath.org/ticket/4468

Original creator: slabbe

Original creation time: 2008-11-08 06:38:21

Assignee: slabbe

Keywords: cmap

The following example works well :


```
sage: matrix_plot(random_matrix(RDF, 50), cmap='hsv')
```


But the next one doesn't which is fine because 'jolies' doesn't correspond to a color map.


```
sage: matrix_plot(random_matrix(RDF, 50), cmap='jolies')
verbose 0 (2212: plot.py, _render_on_subplot) The possible color maps include: Spectral, summer, pink_r, Set1, Set2, Set3, Dark2, prism, PuOr_r, PuBuGn_r, RdPu, gist_ncar_r, Dark2_r, YlGnBu, RdYlBu, hot_r, gist_rainbow_r, gist_stern, cool_r, cool, gray, copper_r, Greens_r, GnBu, gist_ncar, spring_r, gist_rainbow, gist_heat_r, summer_r, OrRd_r, bone, gist_stern_r, RdYlGn, Pastel2_r, spring, Accent, YlOrRd_r, Set2_r, PuBu, RdGy_r, spectral, flag_r, jet_r, RdPu_r, gist_yarg, BuGn, Paired_r, hsv_r, YlOrRd, Greens, PRGn, gist_heat, spectral_r, Paired, hsv, Oranges_r, prism_r, Pastel2, Pastel1_r, Pastel1, gray_r, PuRd_r, Spectral_r, BuPu, YlGnBu_r, copper, gist_earth_r, Set3_r, OrRd, PuBu_r, winter_r, RdBu, jet, bone_r, gist_earth, Oranges, RdYlGn_r, PiYG, YlGn, binary_r, gist_gray_r, gist_gray, flag, RdBu_r, BrBG, Reds, GnBu_r, BrBG_r, Reds_r, RdGy, PuRd, Accent_r, Blues, Greys, autumn, PRGn_r, Greys_r, pink, binary, winter, gist_yarg_r, RdYlBu_r, hot, YlOrBr, BuPu_r, Purples_r, PiYG_r, YlGn_r, Blues_r, YlOrBr_r, Purples, autumn_r, BuGn_r, Set1_r, PuOr, PuBuGn
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last):
...
RuntimeError: Color map jolies not known
```


What about 'mpl' which as well doesn't correspond to a color map :


```
sage: matrix_plot(random_matrix(RDF, 50), cmap='mpl')
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last):
...
AssertionError: 
```


An assertion error : why ? Because in plot.py, we test only if the given cmap is a key of a certain dictionary but not *all* the key of this dictionary correspond to a color map. In fact, there are 18 exceptions as shown below.


```
sage: from matplotlib import cm                                 
sage: d = cm.__dict__                                           
sage: from matplotlib.colors import LinearSegmentedColormap as C
sage: 'mpl' in [x for x in d.keys() if not isinstance(d[x], C)]       
True
sage: [x for x in d.keys() if not isinstance(d[x], C)]          

['colors',
 'cmapname_r',
 'ScalarMappable',
 'LUTSIZE',
 'cmapname',
 'cbook',
 '__file__',
 'cmapnames',
 'cmapdat_r',
 '__builtins__',
 '__name__',
 'get_cmap',
 '__doc__',
 'revcmap',
 'ma',
 'np',
 'mpl',
 'datad']
sage: len(_)
18
```


a patch to come...


---

Attachment


---

Comment by slabbe created at 2008-11-08 06:45:07

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-11-08 20:39:06

Hi Sebastian,

please also add a doctest(s) for this patch.

Cheers,

Michael


---

Comment by slabbe created at 2008-11-08 22:28:37

This patch replace the precedent.


---

Attachment

I just added two doctests in a second patch (witch replace the precedent). I tested those doctests in another and smaller file because sage -t plot.py takes a while. On my computer, I am not able to end it...


```
***sage/plot$ sage -t all.py axes.py
sage -t  devel/sage-word/sage/plot/all.py                   
	 [2.9 s]
sage -t  devel/sage-word/sage/plot/axes.py                  
	 [8.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 11.2 seconds
***sage/plot$ sage -t plot.py
sage -t  sage/plot/plot.py                  *** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
	 [602.3 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  devel/sage-word/sage/plot/plot.py
Total time for all tests: 602.3 seconds
```



---

Comment by mhansen created at 2008-11-21 17:00:27

Looks good and passes tests for me.


---

Comment by mabshoff created at 2008-11-21 20:19:20

Sebastian,

please make sure to post a proper hg patch and not a diff. I checked in your changes under your name, so credit goes where credit is due :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-21 20:22:12

Merged cmap_4468-2.patch in Sage 3.2.1.alpha0


---

Comment by mabshoff created at 2008-11-21 20:22:12

Resolution: fixed

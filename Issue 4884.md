# Issue 4884: Make colormap handling better

Issue created by migration from https://trac.sagemath.org/ticket/4884

Original creator: abergeron

Original creation time: 2008-12-27 23:02:04

Assignee: abergeron

The colormap code is currently ad hoc and copied in all GraphicsPrimitive subclasses that need it.

This patch fixes this by introducing a get_cmap() function in sage.plot.misc that the graphic primitives can call to make sense of what they are passed.

It also adds the option to specify a sequence of colors and use that as the colormap.

For the documentation I added a cmap_help() function which is imported in the global namespace that the docstrings can point to and that will explain what are the possible options, the valid names and everything since the names change rather often.


---

Comment by abergeron created at 2008-12-27 23:03:15

Changing status from new to assigned.


---

Attachment


---

Comment by wdj created at 2008-12-28 01:59:03

I think this patch is a great idea. (In fact, I wonder if a similar plot_help() and plot3d_help() function might be useful.)

However, after the patch is applied, using 3.2.2 on an amd64 ubuntu 8.10 machine, this test failure occurs:


```
wdj@hera:~/sagefiles/sage-3.2.2$ ./sage -t /home/wdj/sagefiles/sage-3.2.2/devel/sage-density_plot/sage/plot/matrix_plot.py 
sage -t  "devel/sage-density_plot/sage/plot/matrix_plot.py"                                                                
**********************************************************************                                                     
File "/home/wdj/sagefiles/sage-3.2.2/devel/sage-density_plot/sage/plot/matrix_plot.py", line 114:                          
    sage: matrix_plot(random_matrix(RDF, 50), cmap='jolies')                                                               
Expected:                                                                                                                  
    Traceback (most recent call last):                                                                                     
    ...                                                                                                                    
    RuntimeError: Color map jolies not known                                                                               
Got:                                                                                                                       
    Traceback (most recent call last):                                                                                     
      File "/home/wdj/sagefiles/sage-3.2.2/local/bin/ncadoctest.py", line 1231, in run_one_test                            
        self.run_one_example(test, example, filename, compileflags)                                                        
      File "/home/wdj/sagefiles/sage-3.2.2/local/bin/sagedoctest.py", line 38, in run_one_example                          
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                                     
      File "/home/wdj/sagefiles/sage-3.2.2/local/bin/ncadoctest.py", line 1172, in run_one_example                         
        compileflags, 1) in test.globs                                                                                     
      File "<doctest __main__.example_3[10]>", line 1, in <module>                                                         
        matrix_plot(random_matrix(RDF, Integer(50)), cmap='jolies')###line 114:                                            
    sage: matrix_plot(random_matrix(RDF, 50), cmap='jolies')                                                               
      File "sage_object.pyx", line 92, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1082)                                                                                                                          
      File "/home/wdj/sagefiles/sage-3.2.2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 685, in _repr_       
        self.show()                                                                                                        
      File "/home/wdj/sagefiles/sage-3.2.2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1039, in show        
        hgridlinesstyle=hgridlinesstyle)                                                                                   
      File "/home/wdj/sagefiles/sage-3.2.2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1176, in save        
        g._render_on_subplot(subplot)                                                                                      
      File "/home/wdj/sagefiles/sage-3.2.2/local/lib/python2.5/site-packages/sage/plot/matrix_plot.py", line 54, in _render_on_subplot                                                                                                                
        cmap = get_cmap(options['cmap'])                                                                                   
      File "/home/wdj/sagefiles/sage-3.2.2/local/lib/python2.5/site-packages/sage/plot/misc.py", line 119, in get_cmap     
        raise RuntimeError, "Color map %s not known (type cmap_help() for valid names)"%cmap                               
    RuntimeError: Color map jolies not known (type cmap_help() for valid names)                                            
**********************************************************************                                                     
File "/home/wdj/sagefiles/sage-3.2.2/devel/sage-density_plot/sage/plot/matrix_plot.py", line 119:                          
    sage: matrix_plot(random_matrix(RDF, 50), cmap='mpl')                                                                  
Expected:                                                                                                                  
    Traceback (most recent call last):                                                                                     
    ...                                                                                                                    
    RuntimeError: Color map mpl not known                                                                                  
Got:                                                                                                                       
    Traceback (most recent call last):                                                                                     
      File "/home/wdj/sagefiles/sage-3.2.2/local/bin/ncadoctest.py", line 1231, in run_one_test                            
        self.run_one_example(test, example, filename, compileflags)                                                        
      File "/home/wdj/sagefiles/sage-3.2.2/local/bin/sagedoctest.py", line 38, in run_one_example                          
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)                                     
      File "/home/wdj/sagefiles/sage-3.2.2/local/bin/ncadoctest.py", line 1172, in run_one_example                         
        compileflags, 1) in test.globs                                                                                     
      File "<doctest __main__.example_3[11]>", line 1, in <module>                                                         
        matrix_plot(random_matrix(RDF, Integer(50)), cmap='mpl')###line 119:                                               
    sage: matrix_plot(random_matrix(RDF, 50), cmap='mpl')                                                                  
      File "sage_object.pyx", line 92, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1082)
      File "/home/wdj/sagefiles/sage-3.2.2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 685, in _repr_
        self.show()
      File "/home/wdj/sagefiles/sage-3.2.2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1039, in show
        hgridlinesstyle=hgridlinesstyle)
      File "/home/wdj/sagefiles/sage-3.2.2/local/lib/python2.5/site-packages/sage/plot/plot.py", line 1176, in save
        g._render_on_subplot(subplot)
      File "/home/wdj/sagefiles/sage-3.2.2/local/lib/python2.5/site-packages/sage/plot/matrix_plot.py", line 54, in _render_on_subplot
        cmap = get_cmap(options['cmap'])
      File "/home/wdj/sagefiles/sage-3.2.2/local/lib/python2.5/site-packages/sage/plot/misc.py", line 119, in get_cmap
        raise RuntimeError, "Color map %s not known (type cmap_help() for valid names)"%cmap
    RuntimeError: Color map mpl not known (type cmap_help() for valid names)
**********************************************************************
1 items had failures:
   2 of  16 in __main__.example_3
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/wdj/sagefiles/sage-3.2.2/tmp/.doctest_matrix_plot.py
         [5.1 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage-density_plot/sage/plot/matrix_plot.py"
Total time for all tests: 5.1 seconds

```


Am I missing something? Mybe I need a more recent version of Sage or ... ?

On the other hand, I love this helpful info:


```
sage: cmap_help()
A colormap can either be a string giving the name of a predefined colormap,
a sequence of color describing a custom one, or an instance of a matplotlib
Colormap.

The valid colormap names are:
Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r,PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, autumn, autumn_r, binary, binary_r, bone, bone_r, cool, cool_r, copper, copper_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gray, gray_r, hot, hot_r, hsv, hsv_r, jet, jet_r, pink, pink_r, prism, prism_r, spectral, spectral_r, spring, spring_r, summer, summer_r, winter,winter_r

If it is a list of colors, the colors can be specified by name, by a 3-tuple
of floats, or by an HTML hex color string.

The valid color names are:
blue, brown, gray, purple, grey, yellow, green, lightblue, orange, black, white, automatic, red
```



---

Comment by abergeron created at 2008-12-28 03:03:57

I don't think you need another version of Sage since I developed it on 3.2.2.  

There is a part in the patch which removes these tests from matrix_plot.py, so I can only guess that the patch didn't apply properly.

Maybe try again with a clean tree.


---

Comment by wdj created at 2008-12-28 03:20:28

Yes, that was my mistake. It passes tests after all. Very nice patch - thanks!


---

Comment by was created at 2008-12-29 06:16:21

(I copied this from what I posted to #4878 to make sure viewers of this ticket see it.)

> The thing about cmap options is that every time we update matplotlib 
> new colormap names become available. The docstrings are just a fixed 
> list and we do not update them every time we update matplotlib. 

At a bare minimum, the docstring should explain precisely what one needs to type to get a list of all valid colormaps.  This could be included in a docstring, so that when matplotlib changes the colormap options, the docstring will suddenly break, and we will know to fix it.

Incidentally, right now one way to get a list of valid colormaps is to just make a mistake with the cmap option, and a list of all valid options is displayed.

```
sage: var('x,y')
sage: z = contour_plot(cos(x^2+y^2), (-4, 4), (-4, 4),cmap='foobar')  
sage: z.save('a.png')                                               
```



---

Comment by abergeron created at 2008-12-29 06:41:22

This reply was meant for here (as the one above):

I am not sure what you mean with your comment.

The proposed patch add a mention to the docstring saying that you have to type cmap_help() to get detailed info on colormaps. This function contains a list of all defined colormaps in the installed matplotlib version. The list is automatically fetched just like the current error code for cmap does right now.

Is this what you want? If not, what do you want?


---

Comment by wdj created at 2008-12-29 11:54:16

Copied from comment in #4878, modulo spelling errors:

Arnaud: I think you have addressed William's complaint in your second patch in #4878. (I was basically arguing the same thing there, though maybe not so clearly.) You describe cmap as one of the options to density_plot and "Type "cmap_help() for more information". The patch #4884 (which I gave a positive review) implements that.


---

Comment by was created at 2008-12-29 17:45:34

> Is this what you want? If not, what do you want? 

I was suggesting not dotting out the output of `cmap_help()`.  We run the test suite before any release, and if the cmap actually does change in matplotlib, then we'll know since the relevant doctest will fail.    The Sage library and its test suite is designed to work with precisely one version of matplotlib -- the one we ship with Sage -- so you don't have to worry about making the doctest example work with numerous different versions. 

In short, I was suggesting a way that the list of all valid colormaps could be safely displayed in the docstrings of the functions that use them.  This would avoid having to have a function `cmap_help()` in the global namespace, and means that people can instantly just see the list of colormaps instead of having to carefully read the docstring, figure out that there is a function cmap_help, then call it, etc., which to some would feel like an awkward workflow.


---

Attachment

To address was' comments (I hope), I killed the cmap_help() function, put the appropriate info in all the relevant docstrings and added a mention about how to obtain the colormap names.

I know you said you would prefer to include the list directly in the docstring, but I don't think this would be productive as it would require adding a doctest somewhere to check that the list has not changed and then when that breaks, have the one responsible manually update all the colormap lists, making sure to not forget every place where this info could have been copy and pasted and to fix the doctest.

In short, it might be better, but I don't feel it is maintainable.  Now if there was some way to automatically include the current list in the docstrings, then that is another story.


---

Comment by was created at 2008-12-30 01:26:03

> I know you said you would prefer to include the list 
> directly in the docstring, but I don't think this would be 
> productive as it would require adding a doctest somewhere 
> to check that the list has not changed and then when that 
> breaks, have the one responsible manually update all the 
> colormap lists, making sure to not forget every place where
> this info could have been copy and pasted and to fix the doctest.
> In short, it might be better, but I don't feel it is 
> maintainable. 

I very strongly disagree.   I think you are saying the above because you don't understand what I'm proposing.  I'm just stating that the list should appear in 1 or 2 places *only* in a doctest and nowhere else.  This is trivial to maintain. 

> Now if there was some way to automatically 
> include the current list in the docstrings, then that is 
> another story. 

That could certainly be done in Python (e.g., by playing tricks with the method that gives the docstring), but it wouldn't necessarily be a good idea.  It would be fun as a challenge though :-)

Just for clarification, I'm 100% ok with this patch going in as is if somebody else gave it a positive review.  I don't think my suggestions are at all something that should stop this getting a positive review!


---

Comment by abergeron created at 2008-12-30 01:50:17

Since it seems I misunderstood was, this gets its positive review back.  Apply only the first patch, though.


---

Comment by mabshoff created at 2009-01-12 01:56:05

Resolution: fixed


---

Comment by mabshoff created at 2009-01-12 01:56:05

Merged both patches in Sage 3.3.alpha0


---

Comment by kcrisman created at 2009-01-24 02:11:12

Questions: 

1. abergeron's last statement makes it sound like he *wants* the cmap_help function back in, yet both patches were applied.

2. was' review implied that abergeron should let the ellipses below

```       
                <BLANKLINE> 
	        The valid colormap names are: 
	        ... 
```

be replaced by the actual output of cmap_help.

3. was' review also implies that for every function (e.g. matrix_plot) where cmap is an option, that function's docstring should have as a doctest a full call of cmap_help with its output, and that the review also said it was okay if that didn't happen for this patch to go in.  That sounds like someone should have opened another ticket for this behavior.

Are any of these correct?  Just checking; there has been a monumental amount of fantastic work in 3.3!


---

Comment by kcrisman created at 2009-01-24 02:11:12

Changing status from closed to reopened.


---

Comment by kcrisman created at 2009-01-24 02:11:12

Resolution changed from fixed to 


---

Comment by mabshoff created at 2009-01-24 02:17:44

Please do not reopen merged ticket, but open a followup ticket. The `...` were left in intentionally and supposed to be done via followup since the patch would bitrot very quickly.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 02:17:44

Resolution: fixed


---

Comment by kcrisman created at 2009-01-24 19:35:07

Any interested parties please see #5083 for further tracking of this discussion and what the best way to document colormap options from matplotlib is.  Sorry for reopening.

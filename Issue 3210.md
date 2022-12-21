# Issue 3210: [with patch, needs review] plotting Z_p as a fractal image

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-05-15 06:45:24

Assignee: was

See:

Albert A. Cuoco, Visualizing the p-adic Integers, The American Mathematical Monthly, Vol. 98, No. 4 (Apr., 1991), pp. 355-364

http://www.jstor.org/stable/2323809?&Search=yes&term=numbers&term=p-adic&list=hide&searchUri=%2Faction%2FdoBasicSearch%3FQuery%3Dp-adic%2Bnumbers%26jc%3Dj100069&item=2&ttl=190&returnArticleService=showArticle



---

Attachment


---

Attachment

cool, quick comment, there is a typo in the docstring: "algebraic an topological"


---

Attachment


---

Comment by robertwb created at 2008-05-15 08:52:54

Attached an updated patch with typo fixed.


---

Comment by wdj created at 2008-05-15 18:01:16

This is a very neat feature, useful if you are teaching number theory or topology, say.

I didn't realize that the second patch was a replacement for the 1st patch, so I tried to 
apply them both and of course failed. The 1st patch works as claimed and passes sage -testall.
(Actually, on my old machine, 


```
The following tests failed:


        sage -t  devel/sage/sage/matrix/benchmark.py
        sage -t  devel/sage/sage/server/notebook/worksheet.py
```

but then they passes on retesting.)

My suggestion, and it really a very minor one, is that the "radius"
where the points are plotted should be a parameter the user can reset. 
For example, if you graph a p=3 and a p=7 then they overlap maybe more
that some would like. Not that I see this as important for teaching but might
be a fun option for making cool pictures. Just an idea.


---

Comment by wdj created at 2008-05-15 18:17:26

FYI, I added another example of the bottom of http://wiki.sagemath.org/pics.


---

Comment by robertwb created at 2008-05-15 18:38:19

Cool image at http://wiki.sagemath.org/pics. :)

The "radius" can be changed with the pointsize parameter. Also, you could plot it with fewer points (as for p=3 or 7, the "points" you're seeing are probably a cluster of even smaller ones).


---

Comment by wdj created at 2008-05-15 19:12:34

I am talking about a dufferent radius I think. To me

```
sage: P1 = Zp(3).plot(pointsize=1,rgbcolor=(0,1,0))
sage: P2 = Zp(7).plot(pointsize=2,rgbcolor=(1,0,0))
```

and

```
sage: P1 = Zp(3).plot(pointsize=1,rgbcolor=(0,1,0))
sage: P2 = Zp(7).plot(pointsize=3,rgbcolor=(1,0,0))
```

Look the same. I was wondering about a scaling parameter 
"distance", say, where 


```
sage: P1 = Zp(3).plot(distance=1,rgbcolor=(0,1,0))
```

would plot the 3 triangles at (say) a circle of radius 1 from (0,0)
as it does now, and 


```
sage: P1 = Zp(3).plot(distance=2,rgbcolor=(0,1,0))
```

would plot the 3 triangles at (say) a circle of radius 2 from (0,0).

Is this possible without introducing a new parameter?


---

Comment by craigcitro created at 2008-06-15 21:44:39

Changing keywords from "" to "editor_craigcitro".


---

Comment by craigcitro created at 2008-06-19 21:37:58

This looks good, barring the extra feature request wdj has. I'm going to give this positive review, and file another ticket with the extra feature request as an enhancement and assign it to robertwb. 

I'm also adding a patch which adds an "r" to the docstring, in the hopes that this will cause less heartache with the reference manual.

Apply 3210-plot-Zp-typo-fix.patch followed by trac-3210-add-r.patch.


---

Attachment

The new ticket is #3474.


---

Comment by mabshoff created at 2008-06-23 10:20:58

Merged 3210-plot-Zp-typo-fix.patch and trac-3210-add-r.patch in Sage 3.0.4.alpha0


---

Comment by mabshoff created at 2008-06-23 10:20:58

Resolution: fixed

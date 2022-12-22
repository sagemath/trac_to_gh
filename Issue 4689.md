# Issue 4689: Documentation documenting the wrong thing

Issue created by migration from Trac.

Original creator: ljpk

Original creation time: 2008-12-03 22:37:41

Assignee: tbd

CC:  mhansen

The examples in the documentation for the save method seems to be broken. If I try


```
sage: E=EllipticCurve([1,0])
sage: Eplot=E.plot()
sage: Eplot.save?
```


then I get


``` 
EXAMPLES:
                sage: c = circle((1,1),1,rgbcolor=(1,0,0))
                sage: c.show(xmin=-1,xmax=3,ymin=-1,ymax=3)

                To correct the apect ratio of certain graphics, it is necessary
                to show with a 'figsize' of square dimensions.

                sage: c.show(figsize=[5,5],xmin=-1,xmax=3,ymin=-1,ymax=3)

                sage: point((-1,1),pointsize=30, rgbcolor=(1,0,0))
```


which never mentions "save" at all. Presumably there should be an extra line, something like


```
sage: c.save("example.png")
```



---

Comment by mabshoff created at 2008-12-03 22:44:01

Hi,

which Sage release is that? If it is 3.2.1 this might be #4672. There is a patch over there that needs one doctest fix to be merged into 3.2.2.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-03 22:44:17

Changing assignee from tbd to tba.


---

Comment by mabshoff created at 2008-12-03 22:44:17

Changing component from algebra to documentation.


---

Comment by ljpk created at 2008-12-03 22:48:29

It's in both 3.1.4 and 3.2.1, but that bug report does look relevant; hopefully fixing that will sort this out too.


---

Comment by mabshoff created at 2008-12-04 17:35:16

With #4672 appplied:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: E=EllipticCurve([1,0])
sage: Eplot=E.plot()
sage: Eplot.save?
```

results in

```
Type:           instancemethod
Base Class:     <type 'instancemethod'>
String Form:    <bound method Graphics.save of >
Namespace:      Interactive
File:           /scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/lib/python2.5/site-packages/sage/plot/plot.py
Definition:     Eplot.save(self, filename=None, xmin=None, xmax=None, ymin=None, ymax=None, figsize=(6, 3.7082039324993699), figure=None, sub=None, savenow=True, dpi=100, axes=None, axes_labels=None, fontsize=None, frame=False, verify=True, aspect_ratio=None, gridlines=None, gridlinesstyle=None, vgridlinesstyle=None, hgridlinesstyle=None)
Docstring:
    
            Save the graphics to an image file of type: PNG, PS, EPS, SVG, SOBJ,
            depending on the file extension you give the filename.
                Extension types can be: file{.png}, file{.ps}, file{.eps}, file{.svg},
                and file{.sobj} (for a SAGE object you can load later). 
    
            EXAMPLES:
                sage: c = circle((1,1),1,rgbcolor=(1,0,0))
                sage: c.show(xmin=-1,xmax=3,ymin=-1,ymax=3)
    
                To correct the apect ratio of certain graphics, it is necessary
                to show with a 'figsize' of square dimensions.
    
                sage: c.show(figsize=[5,5],xmin=-1,xmax=3,ymin=-1,ymax=3)
                
                sage: point((-1,1),pointsize=30, rgbcolor=(1,0,0))
```

Rereading the original ticket I now get your main point: the docstring does not contain "save", but "show" does save the png and then pops up a viewer. We could resolve this by adding a example that uses the save method as you suggested, but my guess would be that such example (in case it did exist) was either changed or removed since "save('foo.png')" saves in the current working directory which is bad for doctesting as a non-owner. 
| Sage Version 3.2.1, Release Date: 2008-12-01                       |
| Type notebook() for the GUI, and license() for information.        |
So, what do you want to do? Close this ticket as "wontfix" or we add a doctest that saves an image in SAGE_TMP - which is the clean way to deal with temporary files.

Cheers,

Michael


---

Comment by ljpk created at 2008-12-04 21:38:08

I think your idea of having a doctest which saves an image somewhere temporary would be the best idea as it would give the reader the idea of how to use the method and reassure them that it is the correct help function.


---

Attachment


---

Comment by jason created at 2010-01-20 06:56:22

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-01-20 07:28:52

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-20 07:28:52

Looks good to me.


---

Comment by mvngu created at 2010-01-23 15:25:43

Resolution: fixed

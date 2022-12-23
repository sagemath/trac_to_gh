# Issue 3106: Add an "image" link for a screenshot of the JMOL applet in the notebook

Issue created by migration from https://trac.sagemath.org/ticket/3106

Original creator: jason

Original creation time: 2008-05-05 16:56:10

Assignee: boothby

From sage-devel:


```
>  >>  is it possible to export the plots created by plot3d and
> >  >>  parametric_plot3d to (say) postcript or png or whatever?
> >  >>
> >  >
> >  > The easy options I know of right now:
> >  >
> >  > (1) Take a screen shot.
> >  >
> >  > (2) Use the option viewer='tachyon' to generate a
> >  > png instead of an interactive dynamic 3d plot.  Then just save
> >  > the png to a file.
> >  >
> >  > Someday there should be a 3rd option to directly export
> >  > what jmol produces, but I don't know how to do it.
> >  > I personally always do (1), since taking screen shots in
> >  > OS X is so incredibly easy.   I think it is also easy
> >  > in Linux with say GIMP.
> >
> >
> >  Here are two solutions for getting images from JMOL.  One (easy)
> >  solution is using the JMOL application (i.e., from the sage command
> >  line); the other is using the applet and requires a bit more work.  We
> >  could probably make the applet version a link under the image in the
> >  notebook.
> >
> >  http://wiki.jmol.org/index.php/File_formats#Images
> >
> >  Jason
> >

I think we certainly need to implement the second method.  It's been
requested a _lot_.  Could you make a trac ticket for this?

 -- William
```



---

Comment by jason created at 2008-05-05 16:57:38

Related to this would be to make the "Print" link automatically take a screenshot and use the image in the printed page.


---

Comment by AlexGhitza created at 2009-01-23 02:49:53

Changing type from defect to enhancement.


---

Attachment


---

Comment by jason created at 2009-02-14 09:50:18

Both patches are identical;  you can delete one.


---

Comment by jason created at 2009-02-14 10:04:03

Changing assignee from boothby to jason.


---

Comment by jason created at 2009-02-14 10:04:03

Changing status from new to assigned.


---

Comment by TimothyClemans created at 2009-02-14 11:09:29

works for me


---

Comment by mabshoff created at 2009-02-14 14:51:30

Resolution: fixed


---

Comment by mabshoff created at 2009-02-14 14:51:30

Merged jmol-save-image.patch in Sage 3.3.rc1.

Cheers,

Michael

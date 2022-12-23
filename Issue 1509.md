# Issue 1509: plotting -- improve text support

Issue created by migration from https://trac.sagemath.org/ticket/1509

Original creator: was

Original creation time: 2007-12-14 18:05:28

Assignee: was


```

Since axes_label is broken in plot(), one must resort to adding your
own custom labels to a plot().

It would be nice in this application, and others, if one could rotate
text objects.  For example, it
would be nice to be able to make a custom y-axis label that was
parallel to the y-axis.  I guess,
in general, the ability to rotate text would be a useful feature.

```


For Sage, make sure to look up how Mathematica does text rotation, etc.,
and use that interface instead of making something up at random. 


---

Comment by mrtrumbe created at 2009-08-17 17:51:26

Regarding text rotation, can we just pass through the rotation option?  This option is already available on the underlying matplotlib text objects, so it seems like a layup.  I've attached a patch which accomplishes just that (it is a very minor change).  This seems to work quite well here.

As for how Mathematica accomplishes it, take a look at their page:  http://demonstrations.wolfram.com/HowTextRotationWorksInMathematica/

I think a solution like that would be pretty easy in sage.  For example, this might work: a function which takes a text graphics primative and an angle and properly applies the rotation to the underlying matplotlib text object.


---

Attachment

Replying to [comment:1 mrtrumbe]:
> Regarding text rotation, can we just pass through the rotation option?  
> This option is already available on the underlying matplotlib text objects, 
> so it seems like a layup.  I've attached a patch which accomplishes just that 
> (it is a very minor change).  This seems to work quite well here.


I tried to download it and got a strange method. I guess it is not an hg patch but a diff?

Also, did you include an example in the docstring to illustrate your new feature?


---

Comment by mrtrumbe created at 2009-08-18 21:08:34

Replying to [comment:2 wdj]:
> I tried to download it and got a strange method. I guess it is not an hg patch but a diff?
> 
> Also, did you include an example in the docstring to illustrate your new feature?
> 

Sorry, I'm new to sage dev practices...is there documentation on generating a standard patch?  I used diff to generate the attached patch.

I didn't include an example usage in the docstrings, but did include explanation of the feature.  I'll update the docstring accordingly and update the patch.


---

Comment by wdj created at 2009-08-18 21:13:00

Replying to [comment:3 mrtrumbe]:
> Replying to [comment:2 wdj]:
> > I tried to download it and got a strange method. I guess it is not an hg patch but a diff?
> > 
> > Also, did you include an example in the docstring to illustrate your new feature?
> > 
> 
> Sorry, I'm new to sage dev practices...is there documentation on generating a standard patch?  I used diff to generate the attached patch.

http://www.sagemath.org/doc/developer/conventions.html
and
http://www.sagemath.org/doc/developer/producing_patches.html

> 
> I didn't include an example usage in the docstrings, but did include explanation of the feature.  I'll update the docstring accordingly and update the patch.

Thanks.


---

Comment by mrtrumbe created at 2009-08-19 18:52:08

Patch was premature.  Accidental revert of other changes.  Will fix shortly.


---

Attachment

Ugh.  Can't seem to delete patch files.  Sorry for the clutter.


---

Comment by mrtrumbe created at 2009-08-19 20:43:48

This is a proper hg patch.  Code is docstring tested.


---

Attachment

This is really neat, as the graphic says! It makes good sense to get more of the mpl functionality exposed, even if axes_labels now works again.  Positive review.  Apply only most recent patch.


---

Comment by mhansen created at 2009-10-15 05:22:22

Resolution: fixed

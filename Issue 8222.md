# Issue 8222: sagenb -- misc improvements to the notebook graph editor

Issue created by migration from https://trac.sagemath.org/ticket/8222

Original creator: was

Original creation time: 2010-02-09 20:04:59

Assignee: rlm

CC:  was chapoton




---

Comment by kevinc created at 2010-02-09 20:17:54

this is a very ugly first draft


---

Attachment

a quick test (gets reverted in following patch)


---

Attachment

cleaned up code, added orientation slider and auto maximize checkbox


---

Attachment

Fixed crashes when calling graph_editor for graphs with multiple components or fewer than 4 vertices, increased graph editor size.


---

Comment by rkirov created at 2010-03-21 05:01:33

I added 8222.patch but then both 8222-part2.patch and 8222-part3.patch failed. Maybe I am doing something wrong?!? 

Kevin, can you make one big patch (here is how to do that http://stackoverflow.com/questions/1224379/exporting-mercurial-patch-against-an-old-revision).

Rado


---

Comment by rkirov created at 2010-03-21 05:57:09

Alright got it to work. I am uploading a big patch that contains part1,2,3 for the sagenb spkg. Part4 still needs to be applied separately to the sage tree.

Everything looks great, I will post a proper review tomorrow.


---

Comment by rkirov created at 2010-03-21 06:33:41

contains part1,2,3 of kevin's patches


---

Comment by rkirov created at 2010-03-22 00:08:07

Changing status from new to needs_work.


---

Attachment

Great work! I loved the spring-electric layout with auto-max (that's how I imagined it all along). Everything worked as expect, so the patch is basically ready to go. However, since we are making basically an User Interface, I have some comments on the design decisions.

I am mostly guided by the mantra that passing UI decisions to the user is not a solution. We should man up and fix the most useful behavior that 99% of users will use (and maybe add the sliders hidden behind a "tweak" button or skip them all together).


- Correct me if wrong but Live with auto-max, spring-el. and default sliders give exactly what I expect on 99% of the graphs. I suggest we make this default (and get rid or hide everything else).


- Similarly, I see no reason for live behavior that shoots vertices out of screen. Link auto-max along with live. At the same time, when graph is paused (not live) auto-max should be off.


- Numbering for vertices should be off by default (graph theorists seldom number their vertices).


- I see only two useful vertex sizes, one for unnumbered vertices and one for numbered. The vertex size slider can be skipped (or hidder by "tweaks" button).


- Unnumbered vertices should be filled black.


- There should be a warning (use JS confirm) with circle layout, since it can potentially destroy a carefully planned layout and there is no undo.

Rado


---

Comment by rkirov created at 2010-03-22 20:58:12

I have implemented my vision (all of the comments above) at http://www.math.uiuc.edu/~rkirov2/js-graph-editor/ and also at the repo http://bitbucket.org/radokirov/js-graph-editor .


---

Attachment

contains kevin's code, my improvements and the new processing library.


---

Attachment

contains kevin's patch, and my JSON-fication of the graph editor code


---

Comment by rbeezer created at 2010-03-26 17:45:48

I tried applying 8222-sagenb.patch and 8222-sage.patch to 4.3.4.  The "sage" patch applied fine, but I got several failures with the sagenb patch.

Finding no hg repo for the notebook I initiated one where I thought it belonged, at

`local/lib/python2.6/site-packages/sagenb-0.7.<something>-py2.6.egg`

(I can't recall the version number on the notebook and am not on the right machine).

Do I need to install the development version of the notebook? (I've done this before, the drill with python setup.py -develop......)  Or do I need to apply more than just the two patches?

Anyway, any guidance in testing this on a stock Sage install would be welcome.

Thanks,
Rob


---

Comment by rkirov created at 2010-03-26 21:01:02

due to complaint I made replacement for sagenb-big patch. Based on sagenb-0.7.5.3


---

Comment by rkirov created at 2010-03-26 21:09:35

Changing status from needs_work to needs_review.


---

Attachment

Hi Rob,

You are the second person complaining for the sagenb patch so I probably made the wrong patch. So I erased my sagenb folder, pasted the new code and made a new patch. Try 8222-sagenb-mega.patch. It has everything to make the graph_editor look like the one on my website. Also has fix for the loop bug you found, which the old one didn't have.

There is a hg repo for the notebook, you don't need to recreate anything. Just extract and go to /sagenb-0.7.5.3/src/sagenb . Now all your "hg patch" commands should work.

Here is a summary of everything needed to make this run:
1) apply 8222-sage.patch to Sage.
2) untar sagenb (with tar -xvf sagenb-0.7.5.3.spgk)
3) apply 8222-sagenb-mega.patch in sagenb-0.7.5.3/src/sagenb with "hg patch 8222-sagenb-mega.patch"
4) run SAGEPATH/sage -python setup.py -develop in sagenb-0.7.5.3/src/sagenb
5) run sage and enjoy!

Rado


---

Comment by rbeezer created at 2010-03-27 04:15:04

Hi Rado,

Thanks - those instructions worked just fine for me and it is running nicely.  Comments later after some testing.

For anybody else - two minor items - I could only find 0.7.5.1 in the directory specified on the notebook project page (which is what I used), and step (4) doesn't have a dash before "develop".

Rob


---

Comment by rbeezer created at 2010-03-28 22:24:49

Hi Rado and Kevin,

Been experimenting with this over the weekend - very, very nice.  I think I've learned enough about the pieces to be able to review this now.

Were you going to

(1) disable red edges?

(2) turn-off auto-maximize?

One suggestion I have right now (without having done a 100% thorough review) is to perhaps check very early on to see if the input is even a graph?  Right now totally wrong input results in a traceback on getting the position dictionary (which is not very informative to the newbie).

Let me know the status of this (ie will you be making more changes?) and I'll see about doing a careful review.  I've got some longer-term, broader comments that I'll post to sage-devel right now.

Rob


---

Comment by pang created at 2010-03-31 12:34:39

The line defining graph_to_json is duplicate in graph_editor.py, that's all.


---

Comment by rkirov created at 2010-04-03 17:14:07

Changing status from needs_review to needs_work.


---

Attachment

Hi Rob,

I was waiting to see what Kevin has to say (since I basically took his code and tweaked with my personal preferences, without consulting with him). However, I haven't heard back from him. You are right we should add some type checking.

I wanted to remove auto-maximize, but since it has Kevin's original work, I wanted to hear back from him. Are you in favor of removing it? If nobody else, says something, I will just make final patch with:

1) removed red-edges
2) removed buttons for maximize and auto-maximize
3) switch delete to keyboard 'd'

on the sage side:

1) add type checking
2) incorporate pang's patch (thanks for patch, that was very sloppy of me)

Then Rob can review it and have the new (in my opinion much superior version of graph editor) in Sage.


---

Comment by rbeezer created at 2010-04-03 18:02:48

Replying to [comment:10 rkirov]:
> Hi Rob,
> 
> I was waiting to see what Kevin has to say (since I basically took his code and tweaked with my personal preferences, without consulting with him). However, I haven't heard back from him. 

I'd suggest proceeding with changes and a review, and hope Kevin checks-in if he feels strongly.  If there is a change he's not happy with it, it could get reverted before being merged (or afterward).  I won't do a review immediately (but will do it soon), so he'll have a chance to weigh-in if he'd like.  

> I wanted to remove auto-maximize, but since it has Kevin's original work, I wanted to hear back from him. Are you in favor of removing it? 

It struck me that it was the source of a lot of wild behavior, without being crucial to proper functioning, so yes, I'd vote for leaving it out for right now.  It could come back later in a different form.

> If nobody else, says something, I will just make final patch with:
> 
> 1) removed red-edges
> 2) removed buttons for maximize and auto-maximize
> 3) switch delete to keyboard 'd'
> 
> on the sage side:
> 
> 1) add type checking
> 2) incorporate pang's patch (thanks for patch, that was very sloppy of me)
> 
> Then Rob can review it and have the new (in my opinion much superior version of graph editor) in Sage.

Sounds like a good plan.

Rob


---

Attachment

requires 8222-sage.patch contains type check and pang's patch


---

Comment by rkirov created at 2010-04-04 07:36:52

requires 8222-sagenb-mega.patch , has rob's suggested improvements


---

Attachment

all ready for review


---

Comment by rkirov created at 2010-04-04 07:41:30

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-04-15 05:28:15

Dialog string change


---

Attachment

All-in-one patch for notebook code


---

Attachment

All-in-one patch for sage library


---

Attachment

Great improvements!  The "live" layout works great, and I really like the way dragging a vertex against the edge makes it appear to bounce off the wall.  Turning off auto-maximize was a good idea, I think.

Tested with 4.3.4 and sagenb-0.7.5.1.  sagenb was updated with all patches available to date.

Passes all tests in sage/graphs, HTML docs build without warnings.

I have added a reviewer patch.  There was a misspelling on the dialog warning about the circular layout change and while I was there I made a little change to the tail end of the string.  the patch file is just to make it easy to see the change.

There are also two new comprehensive patches, wrapping everything up (including reviewer patch).  Apply `trac_8222-sagenb-graph-editor.patch` to the notebook code and apply `trac_8222-sage-graph-editor.patch` to the sage library repo.

Rado - This is all ready for a positive review, subject to approval of the reviewer patch.  Have a look at that, and if everything looks OK with the combined patches, please mark this as positive review and add yourself as an author.  Great work! - Rob


---

Comment by rkirov created at 2010-04-15 16:14:56

Thanks Rob, for catching the typos (i should have spellcheck on next time). Big thanks to Kevin for the spring-repel algo and the auto-max. The big final patches worked fine, everything is in place. It is ready to be merged.

next thing to tackle is the graph interact !!! I hope this gets merged soon so when working on the graph interact we all have the current graph_editor as base (no need to build on this).


---

Comment by rkirov created at 2010-04-15 16:14:56

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2010-04-15 16:44:51

Hi Rado,

Yes, I forgot to add that the next target is definitely the graph-control for interacts.  I'll try to get my experiment together as a patch and post it there.  Also, I have my sights on the graph/latex/tikz stuff.

And yes again - Kevin's contributions here are great!

Thanks for getting this ready to merge so quickly.

Rob


---

Comment by was created at 2010-04-24 19:20:41

Changing status from positive_review to needs_work.


---

Comment by was created at 2010-04-24 19:20:41

I tried this as part of #8725 -- and it doesn't work at all; totally broken.  Tim Dumol says the problem is "a missing script".  So, needs work.


---

Comment by rkirov created at 2010-04-24 19:55:32

Replying to [comment:17 was]:
> I tried this as part of #8725 -- and it doesn't work at all; totally broken.  Tim Dumol says the problem is "a missing script".  So, needs work. 

hmm, weird, it is all working on my setup. I downloaded sagenb-0.8 from #8725, applied rob's all-in-one patch, ran setup.py develop and there was nothing broken.

Can Tim send me some more info on how to reproduce that bug, so I can work on fixing it?


---

Comment by timdumol created at 2010-04-24 22:46:25

Actually, I got it working on my machine already without touching anything. William's still having trouble though.


---

Comment by rkirov created at 2010-04-25 00:19:50

Replying to [comment:19 timdumol]:
> Actually, I got it working on my machine already without touching anything. William's still having trouble though.

Maybe it was a caching issue. Also i have only tested it on Firefox and Chrome, so maybe there is some browser specific issue?


---

Comment by timdumol created at 2010-04-27 06:12:13

Since this has been confirmed to work, can this be marked positive review now?


---

Comment by kcrisman created at 2012-06-29 15:32:04

This was not merged, as far as I can tell.  The Sage library patch definitely isn't in, and the end of [the upstream sagenb graph_editor.html](https://github.com/sagemath/sagenb/blob/master/sagenb/data/graph_editor/graph_editor.html) indicates it wasn't merged there either.


---

Comment by kcrisman created at 2012-10-23 13:36:23

Notice that the graph editor hasn't worked in a long time, but [this pull request](https://github.com/sagemath/sagenb/pull/104) fixes it!


---

Comment by chapoton created at 2014-07-25 12:18:40

Changing keywords from "" to "graph editor".


---

Comment by jdemeyer created at 2014-10-16 08:32:00

Changing component from graph theory to notebook.


---

Comment by kcrisman created at 2014-10-16 13:05:38

See [this sagenb issue](https://github.com/sagemath/sagenb/issues/244), in case anyone ever wants to port this to the latest.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2020-08-25 09:38:27

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-10-26 11:11:08

Resolution: invalid

# Issue 4705: Make in-line wysiwyg editor for text cells using TinyMCE

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-12-05 01:13:31

Assignee: boothby

This ticket splits off part of #4267.

It depends on #4704


---

Attachment


---

Comment by jason created at 2008-12-05 01:14:41

The spkg is at http://sage.math.washington.edu/home/jason/notebook/tinyMCE-3.2.0.2.spkg


---

Comment by jason created at 2008-12-05 01:15:38

Changing assignee from boothby to jason.


---

Comment by jason created at 2008-12-05 01:15:38

Changing status from new to assigned.


---

Comment by TimothyClemans created at 2008-12-20 21:16:07

Works for me Apply #4674, #3767, #4704, #4705


---

Comment by TimothyClemans created at 2008-12-20 21:16:07

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2008-12-20 21:18:48

This needs to be tested with a wide variety of browsers and OS combinations before this goes in. So please list what browser/OS combo worked for you.

It will likely have to wait for 3.4 anyway.

Cheers,

Michael


---

Comment by TimothyClemans created at 2008-12-20 21:24:59

SHIFT-CLICK on new cell bar doesn't work in Safari on Mac.


---

Comment by jason created at 2008-12-20 21:29:12

This is likely due to bugs in the extendedclicks jquery plugin.  The author is willing to work on this, we just need to isolate the problem.


---

Comment by jason created at 2008-12-22 17:30:40

The bugs in Safari are not from the extendedclicks jquery plugin.  Timothy let me have access to his mac the other day and we determined that it has to do with Safari not evaluating javascript in any html that is inserted into the DOM on-the-fly.  Basically, in this patch, the new cell bar code has been changed from a mousedown event in the html code to a separate javascript function.  That javascript function is not evaluated by default in Safari (but is in FF).  So we need to add the html to the DOM, and then explicitly evaluate the javascript.  There is code to something similar to this, and I'm working on modifications to the patch.


---

Comment by jason created at 2008-12-22 21:17:31

Some documentation:

http://www.vulgarisoip.com/2007/06/22/execute-javascript-injected-using-innerhtml-attribute-even-with-safari/

http://piecesofrakesh.blogspot.com/2008/10/understanding-eval-scope-spoiler-its.html

http://snipplr.com/view/2325/ajax-insert-dynamic-script-into-head/

http://www.webdeveloper.com/forum/archive/index.php/t-117817.html

http://www.webmaster-talk.com/javascript-forum/116306-safari-pc-3-0-4-css.html

http://www.optimalworks.net/blog/2007/web-development/javascript/innerhtml-alternative

http://zeta-puppis.com/2006/03/07/javascript-script-execution-in-innerhtml-the-revenge/


---

Attachment

apply on top of previous patch


---

Comment by jason created at 2008-12-22 23:07:36

safari-fix seems to take care of all of the Safari issues.

Okay, everyone, hit this with everything that you have.  I've also updated the tinyMCE spkg (available from the above URL) to make the default font style inherit from the notebook.


---

Comment by TimothyClemans created at 2008-12-22 23:11:56

Works with FF 3.0.5 and Safari on Mac OS X.


---

Comment by jason created at 2008-12-22 23:14:22

To test this on supported browsers, we should test it on Firefox, Opera, and Safari.  I've tested it on FF 3.0.5 on Ubuntu 8.10 and the tinyMCE spkg and this patch seem to work okay.


---

Comment by jason created at 2008-12-24 14:19:59

Here are complete instructions to apply and test the tinymce patch:

Apply the following patches from 4674, 3767, 4704, and 4705, in order:

jsmath-spkg.patch
jquery-and-friends-spkg.2.patch
jquery-javascript-cleanup.patch
tinymce-editable.patch
safari-fix.patch

Install the following packages from the above tickets.  You may have to do ./sage -f <spkg URL> to force an installation if you've already installed an spkg.

http://sage.math.washington.edu/home/jason/notebook/jquery-1.2.6.spkg
http://sage.math.washington.edu/home/jason/notebook/jqueryui-1.6r807svn.spkg
http://sage.math.washington.edu/home/jason/notebook/jsmath-3.6a.spkg
http://sage.math.washington.edu/home/jason/notebook/tinyMCE-3.2.0.2.spkg

Optionally, you can also install the jsmath image fonts by installing:
http://sage.math.washington.edu/home/jason/notebook/jsmath-image-fonts-1.3p0.spkg

Now you should be able to shift-click on a new cell bar to create a text cell using tinyMCE.  You should also be able to double-click on an existing text cell to edit it in-place.


---

Comment by mhampton created at 2008-12-24 16:17:17

I tested this on Safari and Firefox on OS X (10.5).  Everything looks good to me so far.  I will keep using this and see if I run into any problems.

-Marshall


---

Comment by mabshoff created at 2008-12-24 17:47:23

The spkg looks good to me. A slightly cleaned up version is at

http://sage.math.washington.edu/home/mabshoff/spkgs/tinyMCE-3.2.0.2.p0.spkg

Cheers,

Michael


---

Comment by ddrake created at 2009-01-09 02:18:31

I followed the instructions in [comment:14 comment 14] and there's at least one small problem. If I shift-click on the new cell bar, I get the TinyMCE editor thingy. If I click "cancel" without entering any text, the tooltip text ("Doubleclick to edit...") gets put into a text cell at that location.

If I choose "Edit" at the top, the text "Doubleclick to edit..." doesn't show up in the notebook, and if I click "Save changes", the extraneous text goes away.

This happens in Firefox, Opera, IE7, and Chrome. I applied all the patches and spkgs to 3.2.3.


---

Comment by jason created at 2009-01-09 02:25:37

Replying to [comment:17 ddrake]:
> I followed the instructions in [comment:14 comment 14] and there's at least one small problem. If I shift-click on the new cell bar, I get the TinyMCE editor thingy. If I click "cancel" without entering any text, the tooltip text ("Doubleclick to edit...") gets put into a text cell at that location.
> 
> If I choose "Edit" at the top, the text "Doubleclick to edit..." doesn't show up in the notebook, and if I click "Save changes", the extraneous text goes away.
> 
> This happens in Firefox, Opera, IE7, and Chrome. I applied all the patches and spkgs to 3.2.3.

Yes, that sounds like the intended behavior.  Whether or not that should be what happens may be up for debate, though.  The idea is that if you create a text cell, but put nothing in it, it is impossible to edit by double-clicking.  If you make any edits to the cell, though, the filler text goes away.


---

Comment by ddrake created at 2009-01-09 10:41:32

Replying to [comment:18 jason]:
> Replying to [comment:17 ddrake]:
> > I followed the instructions in [comment:14 comment 14] and there's at least one small problem. If I shift-click on the new cell bar, I get the TinyMCE editor thingy. If I click "cancel" without entering any text, the tooltip text ("Doubleclick to edit...") gets put into a text cell at that location.
> > 
> > If I choose "Edit" at the top, the text "Doubleclick to edit..." doesn't show up in the notebook, and if I click "Save changes", the extraneous text goes away.
> > 
> > This happens in Firefox, Opera, IE7, and Chrome. I applied all the patches and spkgs to 3.2.3.
> 
> Yes, that sounds like the intended behavior.  Whether or not that should be what happens may be up for debate, though.  The idea is that if you create a text cell, but put nothing in it, it is impossible to edit by double-clicking.  If you make any edits to the cell, though, the filler text goes away.
> 

Hrm, it may be intended, but I don't like it at all. When I clicked "cancel", I wanted the entire business -- text cell and all -- to go away and, well, be cancelled. I had done one thing (shift-click) and when I clicked cancel, I wanted that one thing to be undone. I do see your point though, that shift-clicking (1) creates a text cell, and (2) starts the tinymce editor on it -- and the cancel button cancels (2).

I'm also bothered by the text being "ghostly", in that you see it when viewing the notebook normally, but it doesn't show up in the usual text-based "Edit".


---

Comment by ddrake created at 2009-01-09 12:26:00

I have tested this and it appears to work fine with the following browser/OS combinations:

Ubuntu 8.10:

  * Firefox 3.0

Win XP SP3:

  * Firefox 3.1 beta
  * IE 7
  * Opera (whatever the current version is)
  * Chrome

OS X 10.5:

  * Firefox 3.0
  * Safari

Just to screw around, I tried [iCab](http://www.icab.de/), which edited existing fields just fine, but the shift-click on the new cell bar didn't work. I think we can safely ignore the iCab browser market. :)


---

Comment by was created at 2009-01-10 20:53:51

> I'm also bothered by the text being "ghostly", in that you see it when 
> viewing the notebook normally, but it doesn't show up in the usual text-based "Edit". 

I do not like either.  Actually, I'm very puzzled how it is possible that it wouldn't show up in Edit, since when one quits a notebook server and restarts it later, worksheets are loaded from disk entirely using their plane text representation (i.e., what you see in Edit), so it seems to me that if the text created is indeed "ghostly" as you claim, it will surely vanish when the server is restarted.


---

Comment by mhampton created at 2009-01-10 23:10:17

Maybe there is some confusion here - I think the only "ghostly" stuff is the "Doubleclick to edit..." message.  It doesn't appear in a view-page-source window.  It does block cell mergers.  It goes away after switching to Edit and saving, but not switching to Edit and canceling.  

I don't think this annoyance is enough to block the inclusion of this functionality - I think we should put it in and make a follow-up ticket to try to change this.  It should be possible to easily delete at least.


---

Comment by mhampton created at 2009-01-11 00:11:52

In trying to track down some of the behavior discussed above, I noticed that normal text cells (i.e. non-ghostly ones, with some content) do not have unique ids.  I am not sure if that is relevant to the ghost issue but it does seem like a bad thing and may induce other bugs.  I.e. normal executable cells have and outer id such as "cell_outer_1" and an inner id such as "cell_1".  The text cells have nested div elements with identical ids, for example both being "cell_text_1".


---

Comment by jason created at 2009-01-11 00:23:56

The ghostly text that is referred to is a TinyMCE setting.  Check the configuration for TinyMCE, right after the TinyMCE is included as a javascript file.  Somewhere in those configuration settings, there is the text "Double click to edit" (or whatever the text is).


---

Comment by jason created at 2009-01-13 15:54:42

Here are the things that still need to be done to get this in.

  * testing with IE 6 on Windows
  * testing with FF 2.0.x on Windows, OSX and Linux
  * testing with Safari on 10.4
  * testing with Opera 9.5 on OSX,  Linux
  * review of the patches themselves
  * review of mabshoff's changes to the spkgs
  * trivial one-line patch to fix the "ghostly text" issue (just make the placeholder string the empty string in cell.py (search for "placeholder" in cell.py).
  * (maybe can wait for another patch): figure out what is going on with divs with the same id.  My guess is that it is an issue with setting the innerHTMl of an object, rather than replacing the object itself.  When the page is "Edit"ed and then reloaded, the duplicate nested IDs go away.  This points to the javascript code that inserts text cells as the problem.

From mabshoff:
> In the end having your assurance that you will available to fix some
> of the inevitable issues would also be assuring.

You have my assurance.


---

Comment by mhampton created at 2009-01-13 16:47:09

It seems a little too demanding to ask that this works on IE 6 on Windows.  Other things don't work on that platform either, or are a little strange.  Is that really officially supported?  If so there should be a lot of tickets for it.  

On Safari on OS 10.4, I had some oddness inserting a text cell at the very top of a worksheet - nothing seemed to happen but when I re-opened it things were OK, the text cell was there.  That should be a followup ticket if anyone can reproduce it, but not enough to block this ticket getting merged in my opinion.

Things seem to work fine on firefox 2.0.0.13 on my mac and windows machines.

The ghost text problem is gone, but there should be an easy way to delete an empty cell.  Currently if you open the text editor and delete all text, there is still some residual empty text cell that you can't see but which blocks cell mergers.  This can be deleted in "Edit" mode for the worksheet but a followup ticket should be made to make it easier.  Again, I don't think that should block this ticket.

I used mabshoff's version of the tinymce spkg, seems fine.  I have not inspected it in detail.


---

Comment by kcrisman created at 2009-01-13 20:22:46

Experience on Sage 3.2.1 with all patches and spkgs installed, using PPC OSX.4.

General: Works great, including tables and lists.  Recommend adding the font-size drop-down menu, perhaps also blockquote, to the standard TinyMCE installation for Sage, since presumably these will often be projected in class and finer control of size outside <h1> style tags would be useful.  Only general problems are known issue that Sage text cells are simply area between math cells, and I had some trouble getting added images to actually show up (but that could be me not knowing how to do them right).  So overall positive, and I would say positive review for Safari 3.2.1.  BUT...

On Firefox 2.0.0.13, encountered *terrible* bug of some kind, was reproducible on my machine.  When a larger text cell was opened using TinyMCE the rendering engine somehow did not do the scrolling properly, and multiple (six, seven, more) images of the same text showed up below or above the text cell; in addition, I could no longer find the editing panel in this situation and only by luck with scrolling found the save/cancel area to even exit this surreal landscape.  This seems to be a major problem, but I have no idea what the issue is, and am puzzled that Marshall did not encounter it.  If this is reproducible, it should probably be a blocker.


---

Comment by mhampton created at 2009-01-13 20:59:17

I could not reproduce the larger text cell problem.  Could you post an sws file somewhere that shows that behavior?  How big are you talking about?  I've pasted in a couple of pages worth of text of different types and didn't have a problem.


---

Comment by ddrake created at 2009-01-14 01:22:12

I tested Firefox 2.0.0.20 on Ubuntu Hardy and it appears to work fine. I couldn't reproduce the large text cell problem reported by kcrisman.

Note that Firefox 2.0 has apparently been EOL'ed: [http://www.mozilla.com/en-US/firefox/all-older.html](http://www.mozilla.com/en-US/firefox/all-older.html). How long should we continue testing on that browser? (I'm not being sarcastic, I'm genuinely curious.)


---

Comment by kcrisman created at 2009-01-14 17:04:20

Replying to [comment:29 ddrake]:
> I tested Firefox 2.0.0.20 on Ubuntu Hardy and it appears to work fine. I couldn't reproduce the large text cell problem reported by kcrisman.
> 
> Note that Firefox 2.0 has apparently been EOL'ed: [http://www.mozilla.com/en-US/firefox/all-older.html](http://www.mozilla.com/en-US/firefox/all-older.html). How long should we continue testing on that browser? (I'm not being sarcastic, I'm genuinely curious.)

I updated to 2.0.0.20 and the problem persists. However, I downloaded FF3.0.5 and the problem is not there, so it's definitely FF2-specific.  My guess is that a lot of people using FF only on occasion (which might be quite a few PC and Mac people, as opposed to Linux) may not even be aware that FF3 is out there (it was very dimly on my radar), so it would be worth at least some testing.

[Here is a worksheet](http://www.math.uchicago.edu/~crisman/TinyMCE_Test.sws) - click on the "Here is a problem" area and then scroll up and down, assuming that area appears toward the bottom of your initial browser window.

I am not sure what the problem is - presumably something Aqua+OSX.4+PPC+FF2 related.  It would be nice for people to check out whether this problem shows up in any other less heavily used browsers - Konqueror, for example, if that's still in use.  If this is the only place it happens, perhaps it's not the worst thing ever - though it IS really hard to use in this one case.


---

Comment by mhampton created at 2009-01-15 01:30:44

I guess I can reproduce this - if I edit your "Here is a problem area" text cell, and then try to scroll the entire worksheet, the lower cells get messed up - sort of like tracers.  This is not good, but doesn't seem awful to me - if you are editing a text cell, you usually don't need to scroll around the whole worksheet?  

Like some other things mentioned in this ticket, I think this deserves a followup ticket but shouldn't block the inclusion of this.  I think the only reason to block this patch is if it messes up some existing functionality or doctests.


---

Comment by mabshoff created at 2009-01-15 01:37:22

Replying to [comment:31 mhampton]:

> Like some other things mentioned in this ticket, I think this deserves a followup ticket but shouldn't block the inclusion of this.  I think the only reason to block this patch is if it messes up some existing functionality or doctests.

Yes, if the patch here in question does not mess up existing functionality, but has issues with the new functionality with some browsers this can be dealt with via a followup ticket. Getting this in working 99% now is much better than it bitrotting and I think Jason will be much happier, too :)

So someone give this a final positive review and it is in.

Cheers,

Michael


---

Comment by mhampton created at 2009-01-15 02:10:10

I think now that people have hit this on a variety of platform combinations it should be merged.  Whatever alpha or release candidate it comes out on, I think it should be highlighted as something people should pound on, and we can make the necessary followup tickets.  But to move this forward it should go in.


---

Comment by kcrisman created at 2009-01-15 02:19:48

Replying to [comment:33 mhampton]:
> I think now that people have hit this on a variety of platform combinations it should be merged.  Whatever alpha or release candidate it comes out on, I think it should be highlighted as something people should pound on, and we can make the necessary followup tickets.  But to move this forward it should go in.
I wasn't sure how picky to be.  Yes, and mabshoff's comment about Jason not wanting bitrot is certainly reasonable.

Does this mean that 

>   * testing with IE 6 on Windows
>   * testing with Opera 9.5 on OSX,  Linux
>   * review of the patches themselves
>   * review of mabshoff's changes to the spkgs

is all done?  I only looked at functionality, not the code.  

Let the followup tickets begin!


---

Comment by jason created at 2009-01-15 02:54:59

Most of my entire next week is devoted to Sage at SD12.  FYI, I can certainly make followup tickets to this a priority in the next week.

I most certainly second the comment that Jason will be very happy to see this finally go in!


---

Attachment


---

Comment by jason created at 2009-01-16 17:54:01

The ghost-text.patch corrects the ghostly text mentioned above and should be applied on top of the other patches.


---

Comment by mabshoff created at 2009-01-19 08:11:02

Resolution: fixed


---

Comment by mabshoff created at 2009-01-19 08:11:02

Merged tinymce-editable.patch,  safari-fix.patch, ghost-text.patch in Sage 3.3.alpha0.

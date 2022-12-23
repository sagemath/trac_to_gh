# Issue 7501: notebook -- include codemirror in sage

Issue created by migration from https://trac.sagemath.org/ticket/7501

Original creator: was

Original creation time: 2009-11-20 09:20:21

Assignee: boothby

After an extensive evaluation, we all decided that codemirror http://marijn.haverbeke.nl/codemirror/ is the best Javascript code editor to include in Sage.  It's faster and more robust than editarea.  Initially, we will include it *only* for editing `Data --> file`, then maybe later adapt it for input cells. 

See this screenshot:  http://wstein.org/home/wstein/patches/codemirror.png


---

Attachment


---

Comment by jason created at 2009-11-20 09:28:40

Positive review to William's patch, as a proof-of-concept patch.

In the end, codemirror gets included on every page---that shouldn't be.


---

Comment by jason created at 2009-11-20 11:25:49

For the next step:  these people apparently worked on an autocompletion function:

http://groups.google.com/group/codemirror/browse_frm/thread/37a078e69b26a213#


---

Comment by mpatel created at 2010-02-04 05:56:54

I can rebase this and try to include it in SageNB 0.7.x (cf. #8051) or, perhaps, 0.8.


---

Comment by mpatel created at 2010-02-05 07:09:13

Changing status from new to needs_work.


---

Comment by mpatel created at 2010-02-05 16:12:00

See the description for links to rebased patches.  I've adjusted line numbers' style so they line up with the lines in the editor.


---

Comment by mpatel created at 2010-02-05 16:12:00

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-02-07 12:56:48

I should have said that the "rebased" patches are actually new.  It seem easier to do this given the extent of changes to SageNB since the original patches were made.  Also, the original set

 * Includes `codemirror.js` on every page.
 * Refers to `parsesage.js` and `sage/css/pythoncolors.css`, which seem to be missing.  The new patches just use CodeMirror's Python parser and style.
 * Does not align the automatic line numbers with lines of text in the editor.

Part A just adds CodeMirror to the repository.  Part B configures it for the data file page.


---

Comment by mpatel created at 2010-02-07 12:59:23

Replying to [comment:7 mpatel]:
>  * Includes `codemirror.js` on every page.

Or more pages than necessary, at least.


---

Comment by drkirkby created at 2010-02-22 00:14:34

Has any of this been tested on Solaris?


---

Comment by drkirkby created at 2010-02-22 00:14:34

Changing status from needs_review to needs_info.


---

Comment by mpatel created at 2010-02-22 00:42:36

Replying to [comment:9 drkirkby]:
> Has any of this been tested on Solaris? 
I haven't.  But if you have a spare moment, please test the patches and let us know!  

Note: CodeMirror runs entirely in the browser.


---

Comment by mpatel created at 2010-02-22 00:42:36

Changing status from needs_info to needs_review.


---

Comment by drkirkby created at 2010-02-22 01:05:47

I would never have enough time to test individuals patches. But William is keen a Solaris port is completed very soon and if things don't get checked, then it hampers that port. 

Dave


---

Comment by timdumol created at 2010-03-19 16:58:16

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-03-19 16:58:16

Looks ok to me, and it is extremely unlikely that this can have any negative effect on *any* platform, since, as Mitesh said, it's totally in the browser.


---

Comment by timdumol created at 2010-05-04 04:44:19

Resolution: fixed

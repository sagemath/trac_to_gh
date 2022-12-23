# Issue 5447: upgrade to jquery 1.3 and jqueryui 1.7

Issue created by migration from https://trac.sagemath.org/ticket/5447

Original creator: jason

Original creation time: 2009-03-06 03:19:53

Assignee: tbd

CC:  jason

Apparently these new releases are much faster (like an order of magnitude for some operations).

http://docs.jquery.com/Release:jQuery_1.3


---

Comment by jason created at 2009-03-06 03:20:07

Changing type from defect to enhancement.


---

Comment by jason created at 2009-03-06 03:20:07

Changing assignee from tbd to boothby.


---

Comment by jason created at 2009-03-06 03:20:07

Changing component from algebra to notebook.


---

Comment by jason created at 2009-03-12 22:49:56

Changing status from new to assigned.


---

Comment by jason created at 2009-03-12 22:49:56

Changing assignee from boothby to jason.


---

Attachment

For p0 spkgs.


---

Comment by mpatel created at 2009-08-03 04:00:28

A first take on a much-desired jQuery / UI upgrade:

 * http://sage.math.washington.edu/home/mpatel/trac/5447/jquery-1.3.2.p0.spkg
 * http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p0.spkg

Install both packages and apply [attachment:trac_5447-jquery_upgrade.patch this patch] to the sage repository.  The patch

 * Updates the paths to scripts and stylesheets.
 * Tweaks `interact.py`'s `html_slider()` and `html_rangeslider()` just enough to get the sliders to work with the new spkgs.
 * Cleans up `notebook.py`, somewhat.

I've tested the examples listed in `interact?` with success.  However, the libraries have changed significantly and there may be *many* other ways to break the notebook and ``@`interacts`.  Please test away and provide feeback!


---

Comment by mpatel created at 2009-08-03 18:19:43

Reminder: Apply tips from [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/d69332ec6ec92128/90edc4cc5cad2dd5?lnk=gst&q=improved+spkg+install#90edc4cc5cad2dd5) to the next revisions of `spkg-install`.


---

Comment by mpatel created at 2009-08-04 07:09:41

Replying to [comment:4 mpatel]:
> Reminder: Apply tips from [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/d69332ec6ec92128/90edc4cc5cad2dd5?lnk=gst&q=improved+spkg+install#90edc4cc5cad2dd5) to the next revisions of `spkg-install`.
If necessary, rebase the patch against #6568.


---

Attachment

For p1 spkgs. Depends on #6568, #6840.


---

Comment by mpatel created at 2009-09-01 08:15:45

Changes in v2:

 * Rebased against #6568, #6840.
 * Updated `spkg-install`s along the lines of [D. Kirby's example](http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p0.spkg).

New spkgs:

 * http://sage.math.washington.edu/home/mpatel/trac/5447/jquery-1.3.2.p1.spkg
 * http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p1.spkg

Note: When "downgrading" back to jQuery 1.2.6 and jQuery UI 1.6, it may help to delete `local/notebook/javascript/jquery*` manually, since their `spkg-install`s just overwrite the previous installation.


---

Comment by mpatel created at 2009-09-05 14:56:34

Updated spkgs with fixed "set -e" problem (cf. [comment:ticket:6586:37 this comment]):

 * http://sage.math.washington.edu/home/mpatel/trac/5447/jquery-1.3.2.p2.spkg
 * http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p2.spkg


---

Attachment

apply instead of previous patches


---

Comment by jason created at 2009-09-15 19:05:07

Great work!

There are still two places that the old location of jquery is referenced:


```
~/sage/devel/sage/sage/server/notebook$ grep -r jquery.js *
notebook.py:           <script type="text/javascript" src="/javascript_local/jquery/jquery.js"></script>
templates/notebook/worksheet.html:<script type="text/javascript" src="/javascript_local/jquery/jquery.js"></script>
```



---

Comment by jason created at 2009-09-15 21:15:59

Also, can you post a picture of the new sliders up on sage-devel?  Last time I updated jqueryui, there was concern about having the squarish sliders.


---

Comment by jason created at 2009-09-15 21:16:27

(except for the two comments from me above, this has a positive review from me).


---

Comment by mpatel created at 2009-09-18 03:44:07

Apply only this patch.


---

Attachment

Thanks very much for pointing out those places.  [attachment:trac_5447-jquery_upgrade_v3.patch Patch v3] should cover them.  I've also [inquired](http://groups.google.com/group/sage-devel/browse_thread/thread/372c917e59b713f4) on sage-devel about the sliders.


---

Comment by mpatel created at 2009-09-19 06:22:01

I've uploaded a new jQuery UI package that tweaks `patches/sage/jquery-ui-1.7.2.custom.css` to set up thinner handles for both horizontal and vertical sliders (cf. "the middle one" at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/372c917e59b713f4)):

 * http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p3.spkg


---

Comment by jason created at 2009-09-22 15:45:33

Okay, positive review.

However, please use http://sage.math.washington.edu/home/jason/jqueryui-1.7.2.p3.spkg

I just deleted one file that was leftover (a .orig file) and removed said file from the repository.

Nice work!!


---

Comment by mpatel created at 2009-09-23 00:49:14

Thanks!  Sorry about not being explicit about my not wanting to fiddle further with the sliders.


---

Comment by mpatel created at 2009-09-23 23:13:23

If the new jQuery UI package needs a review:  Positive.


---

Comment by mpatel created at 2009-10-16 19:36:04

SageNB patches rebased against #7196, plus this queue: #7158, #4551, #3646, #6459.  For this ticket, apply only the following patches, in order: 

 * http://sage.math.washington.edu/home/mpatel/trac/5447/trac_5447-sagenb_jquery_upgrade_A.patch
 * http://sage.math.washington.edu/home/mpatel/trac/5447/trac_5447-sagenb_jquery_upgrade_B.patch


---

Comment by was created at 2009-10-17 07:43:09

Merged into sagenb-0.3.2 (i.e., sage-4.2).


---

Comment by was created at 2009-10-17 07:43:09

Resolution: fixed

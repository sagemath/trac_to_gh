# Issue 5447: upgrade to jquery 1.3 and jqueryui 1.7

archive/issues_005447.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @jasongrout\n\nApparently these new releases are much faster (like an order of magnitude for some operations).\n\nhttp://docs.jquery.com/Release:jQuery_1.3\n\nIssue created by migration from https://trac.sagemath.org/ticket/5447\n\n",
    "created_at": "2009-03-06T03:19:53Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "upgrade to jquery 1.3 and jqueryui 1.7",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5447",
    "user": "https://github.com/jasongrout"
}
```
Assignee: tbd

CC:  @jasongrout

Apparently these new releases are much faster (like an order of magnitude for some operations).

http://docs.jquery.com/Release:jQuery_1.3

Issue created by migration from https://trac.sagemath.org/ticket/5447





---

archive/issue_comments_042026.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-03-06T03:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42026",
    "user": "https://github.com/jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_042027.json:
```json
{
    "body": "Changing assignee from tbd to boothby.",
    "created_at": "2009-03-06T03:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42027",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from tbd to boothby.



---

archive/issue_comments_042028.json:
```json
{
    "body": "Changing component from algebra to notebook.",
    "created_at": "2009-03-06T03:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42028",
    "user": "https://github.com/jasongrout"
}
```

Changing component from algebra to notebook.



---

archive/issue_comments_042029.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-12T22:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42029",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042030.json:
```json
{
    "body": "Changing assignee from boothby to @jasongrout.",
    "created_at": "2009-03-12T22:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42030",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from boothby to @jasongrout.



---

archive/issue_comments_042031.json:
```json
{
    "body": "Attachment [trac_5447-jquery_upgrade.patch](tarball://root/attachments/some-uuid/ticket5447/trac_5447-jquery_upgrade.patch) by @qed777 created at 2009-08-03 03:28:23\n\nFor p0 spkgs.",
    "created_at": "2009-08-03T03:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42031",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_5447-jquery_upgrade.patch](tarball://root/attachments/some-uuid/ticket5447/trac_5447-jquery_upgrade.patch) by @qed777 created at 2009-08-03 03:28:23

For p0 spkgs.



---

archive/issue_comments_042032.json:
```json
{
    "body": "A first take on a much-desired jQuery / UI upgrade:\n\n* http://sage.math.washington.edu/home/mpatel/trac/5447/jquery-1.3.2.p0.spkg\n* http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p0.spkg\n\nInstall both packages and apply [attachment:trac_5447-jquery_upgrade.patch this patch] to the sage repository.  The patch\n\n* Updates the paths to scripts and stylesheets.\n* Tweaks `interact.py`'s `html_slider()` and `html_rangeslider()` just enough to get the sliders to work with the new spkgs.\n* Cleans up `notebook.py`, somewhat.\n\nI've tested the examples listed in `interact?` with success.  However, the libraries have changed significantly and there may be **many** other ways to break the notebook and ``@`interacts`.  Please test away and provide feeback!",
    "created_at": "2009-08-03T04:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42032",
    "user": "https://github.com/qed777"
}
```

A first take on a much-desired jQuery / UI upgrade:

* http://sage.math.washington.edu/home/mpatel/trac/5447/jquery-1.3.2.p0.spkg
* http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p0.spkg

Install both packages and apply [attachment:trac_5447-jquery_upgrade.patch this patch] to the sage repository.  The patch

* Updates the paths to scripts and stylesheets.
* Tweaks `interact.py`'s `html_slider()` and `html_rangeslider()` just enough to get the sliders to work with the new spkgs.
* Cleans up `notebook.py`, somewhat.

I've tested the examples listed in `interact?` with success.  However, the libraries have changed significantly and there may be **many** other ways to break the notebook and ``@`interacts`.  Please test away and provide feeback!



---

archive/issue_comments_042033.json:
```json
{
    "body": "Reminder: Apply tips from [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/d69332ec6ec92128/90edc4cc5cad2dd5?lnk=gst&q=improved+spkg+install#90edc4cc5cad2dd5) to the next revisions of `spkg-install`.",
    "created_at": "2009-08-03T18:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42033",
    "user": "https://github.com/qed777"
}
```

Reminder: Apply tips from [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/d69332ec6ec92128/90edc4cc5cad2dd5?lnk=gst&q=improved+spkg+install#90edc4cc5cad2dd5) to the next revisions of `spkg-install`.



---

archive/issue_comments_042034.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> Reminder: Apply tips from [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/d69332ec6ec92128/90edc4cc5cad2dd5?lnk=gst&q=improved+spkg+install#90edc4cc5cad2dd5) to the next revisions of `spkg-install`.\nIf necessary, rebase the patch against #6568.",
    "created_at": "2009-08-04T07:09:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42034",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:4 mpatel]:
> Reminder: Apply tips from [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/d69332ec6ec92128/90edc4cc5cad2dd5?lnk=gst&q=improved+spkg+install#90edc4cc5cad2dd5) to the next revisions of `spkg-install`.
If necessary, rebase the patch against #6568.



---

archive/issue_comments_042035.json:
```json
{
    "body": "Attachment [trac_5447-jquery_upgrade_v2.patch](tarball://root/attachments/some-uuid/ticket5447/trac_5447-jquery_upgrade_v2.patch) by @qed777 created at 2009-09-01 08:05:14\n\nFor p1 spkgs. Depends on #6568, #6840.",
    "created_at": "2009-09-01T08:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42035",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_5447-jquery_upgrade_v2.patch](tarball://root/attachments/some-uuid/ticket5447/trac_5447-jquery_upgrade_v2.patch) by @qed777 created at 2009-09-01 08:05:14

For p1 spkgs. Depends on #6568, #6840.



---

archive/issue_comments_042036.json:
```json
{
    "body": "Changes in v2:\n\n* Rebased against #6568, #6840.\n* Updated `spkg-install`s along the lines of [D. Kirby's example](http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p0.spkg).\n\nNew spkgs:\n\n* http://sage.math.washington.edu/home/mpatel/trac/5447/jquery-1.3.2.p1.spkg\n* http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p1.spkg\n\nNote: When \"downgrading\" back to jQuery 1.2.6 and jQuery UI 1.6, it may help to delete `local/notebook/javascript/jquery*` manually, since their `spkg-install`s just overwrite the previous installation.",
    "created_at": "2009-09-01T08:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42036",
    "user": "https://github.com/qed777"
}
```

Changes in v2:

* Rebased against #6568, #6840.
* Updated `spkg-install`s along the lines of [D. Kirby's example](http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p0.spkg).

New spkgs:

* http://sage.math.washington.edu/home/mpatel/trac/5447/jquery-1.3.2.p1.spkg
* http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p1.spkg

Note: When "downgrading" back to jQuery 1.2.6 and jQuery UI 1.6, it may help to delete `local/notebook/javascript/jquery*` manually, since their `spkg-install`s just overwrite the previous installation.



---

archive/issue_comments_042037.json:
```json
{
    "body": "Updated spkgs with fixed \"set -e\" problem (cf. [comment:ticket:6586:37 this comment]):\n\n* http://sage.math.washington.edu/home/mpatel/trac/5447/jquery-1.3.2.p2.spkg\n* http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p2.spkg",
    "created_at": "2009-09-05T14:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42037",
    "user": "https://github.com/qed777"
}
```

Updated spkgs with fixed "set -e" problem (cf. [comment:ticket:6586:37 this comment]):

* http://sage.math.washington.edu/home/mpatel/trac/5447/jquery-1.3.2.p2.spkg
* http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p2.spkg



---

archive/issue_comments_042038.json:
```json
{
    "body": "Attachment [trac_5447-jquery_upgrade_v2-rebased.patch](tarball://root/attachments/some-uuid/ticket5447/trac_5447-jquery_upgrade_v2-rebased.patch) by @jasongrout created at 2009-09-15 18:56:38\n\napply instead of previous patches",
    "created_at": "2009-09-15T18:56:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42038",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_5447-jquery_upgrade_v2-rebased.patch](tarball://root/attachments/some-uuid/ticket5447/trac_5447-jquery_upgrade_v2-rebased.patch) by @jasongrout created at 2009-09-15 18:56:38

apply instead of previous patches



---

archive/issue_comments_042039.json:
```json
{
    "body": "Great work!\n\nThere are still two places that the old location of jquery is referenced:\n\n\n```\n~/sage/devel/sage/sage/server/notebook$ grep -r jquery.js *\nnotebook.py:           <script type=\"text/javascript\" src=\"/javascript_local/jquery/jquery.js\"></script>\ntemplates/notebook/worksheet.html:<script type=\"text/javascript\" src=\"/javascript_local/jquery/jquery.js\"></script>\n```\n",
    "created_at": "2009-09-15T19:05:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42039",
    "user": "https://github.com/jasongrout"
}
```

Great work!

There are still two places that the old location of jquery is referenced:


```
~/sage/devel/sage/sage/server/notebook$ grep -r jquery.js *
notebook.py:           <script type="text/javascript" src="/javascript_local/jquery/jquery.js"></script>
templates/notebook/worksheet.html:<script type="text/javascript" src="/javascript_local/jquery/jquery.js"></script>
```




---

archive/issue_comments_042040.json:
```json
{
    "body": "Also, can you post a picture of the new sliders up on sage-devel?  Last time I updated jqueryui, there was concern about having the squarish sliders.",
    "created_at": "2009-09-15T21:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42040",
    "user": "https://github.com/jasongrout"
}
```

Also, can you post a picture of the new sliders up on sage-devel?  Last time I updated jqueryui, there was concern about having the squarish sliders.



---

archive/issue_comments_042041.json:
```json
{
    "body": "(except for the two comments from me above, this has a positive review from me).",
    "created_at": "2009-09-15T21:16:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42041",
    "user": "https://github.com/jasongrout"
}
```

(except for the two comments from me above, this has a positive review from me).



---

archive/issue_comments_042042.json:
```json
{
    "body": "Apply only this patch.",
    "created_at": "2009-09-18T03:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42042",
    "user": "https://github.com/qed777"
}
```

Apply only this patch.



---

archive/issue_comments_042043.json:
```json
{
    "body": "Attachment [trac_5447-jquery_upgrade_v3.patch](tarball://root/attachments/some-uuid/ticket5447/trac_5447-jquery_upgrade_v3.patch) by @qed777 created at 2009-09-18 03:49:24\n\nThanks very much for pointing out those places.  [attachment:trac_5447-jquery_upgrade_v3.patch Patch v3] should cover them.  I've also [inquired](http://groups.google.com/group/sage-devel/browse_thread/thread/372c917e59b713f4) on sage-devel about the sliders.",
    "created_at": "2009-09-18T03:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42043",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_5447-jquery_upgrade_v3.patch](tarball://root/attachments/some-uuid/ticket5447/trac_5447-jquery_upgrade_v3.patch) by @qed777 created at 2009-09-18 03:49:24

Thanks very much for pointing out those places.  [attachment:trac_5447-jquery_upgrade_v3.patch Patch v3] should cover them.  I've also [inquired](http://groups.google.com/group/sage-devel/browse_thread/thread/372c917e59b713f4) on sage-devel about the sliders.



---

archive/issue_comments_042044.json:
```json
{
    "body": "I've uploaded a new jQuery UI package that tweaks `patches/sage/jquery-ui-1.7.2.custom.css` to set up thinner handles for both horizontal and vertical sliders (cf. \"the middle one\" at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/372c917e59b713f4)):\n\n* http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p3.spkg",
    "created_at": "2009-09-19T06:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42044",
    "user": "https://github.com/qed777"
}
```

I've uploaded a new jQuery UI package that tweaks `patches/sage/jquery-ui-1.7.2.custom.css` to set up thinner handles for both horizontal and vertical sliders (cf. "the middle one" at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/372c917e59b713f4)):

* http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p3.spkg



---

archive/issue_comments_042045.json:
```json
{
    "body": "Okay, positive review.\n\nHowever, please use http://sage.math.washington.edu/home/jason/jqueryui-1.7.2.p3.spkg\n\nI just deleted one file that was leftover (a .orig file) and removed said file from the repository.\n\nNice work!!",
    "created_at": "2009-09-22T15:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42045",
    "user": "https://github.com/jasongrout"
}
```

Okay, positive review.

However, please use http://sage.math.washington.edu/home/jason/jqueryui-1.7.2.p3.spkg

I just deleted one file that was leftover (a .orig file) and removed said file from the repository.

Nice work!!



---

archive/issue_comments_042046.json:
```json
{
    "body": "Thanks!  Sorry about not being explicit about my not wanting to fiddle further with the sliders.",
    "created_at": "2009-09-23T00:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42046",
    "user": "https://github.com/qed777"
}
```

Thanks!  Sorry about not being explicit about my not wanting to fiddle further with the sliders.



---

archive/issue_comments_042047.json:
```json
{
    "body": "If the new jQuery UI package needs a review:  Positive.",
    "created_at": "2009-09-23T23:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42047",
    "user": "https://github.com/qed777"
}
```

If the new jQuery UI package needs a review:  Positive.



---

archive/issue_comments_042048.json:
```json
{
    "body": "SageNB patches rebased against #7196, plus this queue: #7158, #4551, #3646, #6459.  For this ticket, apply only the following patches, in order: \n\n* http://sage.math.washington.edu/home/mpatel/trac/5447/trac_5447-sagenb_jquery_upgrade_A.patch\n* http://sage.math.washington.edu/home/mpatel/trac/5447/trac_5447-sagenb_jquery_upgrade_B.patch",
    "created_at": "2009-10-16T19:36:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42048",
    "user": "https://github.com/qed777"
}
```

SageNB patches rebased against #7196, plus this queue: #7158, #4551, #3646, #6459.  For this ticket, apply only the following patches, in order: 

* http://sage.math.washington.edu/home/mpatel/trac/5447/trac_5447-sagenb_jquery_upgrade_A.patch
* http://sage.math.washington.edu/home/mpatel/trac/5447/trac_5447-sagenb_jquery_upgrade_B.patch



---

archive/issue_comments_042049.json:
```json
{
    "body": "Merged into sagenb-0.3.2 (i.e., sage-4.2).",
    "created_at": "2009-10-17T07:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42049",
    "user": "https://github.com/williamstein"
}
```

Merged into sagenb-0.3.2 (i.e., sage-4.2).



---

archive/issue_comments_042050.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-17T07:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42050",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed

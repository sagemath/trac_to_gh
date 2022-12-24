# Issue 5447: upgrade to jquery 1.3 and jqueryui 1.7

archive/issues_005447.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jason\n\nApparently these new releases are much faster (like an order of magnitude for some operations).\n\nhttp://docs.jquery.com/Release:jQuery_1.3\n\nIssue created by migration from https://trac.sagemath.org/ticket/5447\n\n",
    "created_at": "2009-03-06T03:19:53Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "upgrade to jquery 1.3 and jqueryui 1.7",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5447",
    "user": "jason"
}
```
Assignee: tbd

CC:  jason

Apparently these new releases are much faster (like an order of magnitude for some operations).

http://docs.jquery.com/Release:jQuery_1.3

Issue created by migration from https://trac.sagemath.org/ticket/5447





---

archive/issue_comments_042108.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-03-06T03:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42108",
    "user": "jason"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_042109.json:
```json
{
    "body": "Changing assignee from tbd to boothby.",
    "created_at": "2009-03-06T03:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42109",
    "user": "jason"
}
```

Changing assignee from tbd to boothby.



---

archive/issue_comments_042110.json:
```json
{
    "body": "Changing component from algebra to notebook.",
    "created_at": "2009-03-06T03:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42110",
    "user": "jason"
}
```

Changing component from algebra to notebook.



---

archive/issue_comments_042111.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-12T22:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42111",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042112.json:
```json
{
    "body": "Changing assignee from boothby to jason.",
    "created_at": "2009-03-12T22:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42112",
    "user": "jason"
}
```

Changing assignee from boothby to jason.



---

archive/issue_comments_042113.json:
```json
{
    "body": "Attachment [trac_5447-jquery_upgrade.patch](tarball://root/attachments/some-uuid/ticket5447/trac_5447-jquery_upgrade.patch) by mpatel created at 2009-08-03 03:28:23\n\nFor p0 spkgs.",
    "created_at": "2009-08-03T03:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42113",
    "user": "mpatel"
}
```

Attachment [trac_5447-jquery_upgrade.patch](tarball://root/attachments/some-uuid/ticket5447/trac_5447-jquery_upgrade.patch) by mpatel created at 2009-08-03 03:28:23

For p0 spkgs.



---

archive/issue_comments_042114.json:
```json
{
    "body": "A first take on a much-desired jQuery / UI upgrade:\n\n* http://sage.math.washington.edu/home/mpatel/trac/5447/jquery-1.3.2.p0.spkg\n* http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p0.spkg\n\nInstall both packages and apply [attachment:trac_5447-jquery_upgrade.patch this patch] to the sage repository.  The patch\n\n* Updates the paths to scripts and stylesheets.\n* Tweaks `interact.py`'s `html_slider()` and `html_rangeslider()` just enough to get the sliders to work with the new spkgs.\n* Cleans up `notebook.py`, somewhat.\n\nI've tested the examples listed in `interact?` with success.  However, the libraries have changed significantly and there may be **many** other ways to break the notebook and ``@`interacts`.  Please test away and provide feeback!",
    "created_at": "2009-08-03T04:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42114",
    "user": "mpatel"
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

archive/issue_comments_042115.json:
```json
{
    "body": "Reminder: Apply tips from [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/d69332ec6ec92128/90edc4cc5cad2dd5?lnk=gst&q=improved+spkg+install#90edc4cc5cad2dd5) to the next revisions of `spkg-install`.",
    "created_at": "2009-08-03T18:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42115",
    "user": "mpatel"
}
```

Reminder: Apply tips from [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/d69332ec6ec92128/90edc4cc5cad2dd5?lnk=gst&q=improved+spkg+install#90edc4cc5cad2dd5) to the next revisions of `spkg-install`.



---

archive/issue_comments_042116.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> Reminder: Apply tips from [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/d69332ec6ec92128/90edc4cc5cad2dd5?lnk=gst&q=improved+spkg+install#90edc4cc5cad2dd5) to the next revisions of `spkg-install`.\nIf necessary, rebase the patch against #6568.",
    "created_at": "2009-08-04T07:09:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42116",
    "user": "mpatel"
}
```

Replying to [comment:4 mpatel]:
> Reminder: Apply tips from [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/d69332ec6ec92128/90edc4cc5cad2dd5?lnk=gst&q=improved+spkg+install#90edc4cc5cad2dd5) to the next revisions of `spkg-install`.
If necessary, rebase the patch against #6568.



---

archive/issue_comments_042117.json:
```json
{
    "body": "Attachment [trac_5447-jquery_upgrade_v2.patch](tarball://root/attachments/some-uuid/ticket5447/trac_5447-jquery_upgrade_v2.patch) by mpatel created at 2009-09-01 08:05:14\n\nFor p1 spkgs. Depends on #6568, #6840.",
    "created_at": "2009-09-01T08:05:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42117",
    "user": "mpatel"
}
```

Attachment [trac_5447-jquery_upgrade_v2.patch](tarball://root/attachments/some-uuid/ticket5447/trac_5447-jquery_upgrade_v2.patch) by mpatel created at 2009-09-01 08:05:14

For p1 spkgs. Depends on #6568, #6840.



---

archive/issue_comments_042118.json:
```json
{
    "body": "Changes in v2:\n\n* Rebased against #6568, #6840.\n* Updated `spkg-install`s along the lines of [D. Kirby's example](http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p0.spkg).\n\nNew spkgs:\n\n* http://sage.math.washington.edu/home/mpatel/trac/5447/jquery-1.3.2.p1.spkg\n* http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p1.spkg\n\nNote: When \"downgrading\" back to jQuery 1.2.6 and jQuery UI 1.6, it may help to delete `local/notebook/javascript/jquery*` manually, since their `spkg-install`s just overwrite the previous installation.",
    "created_at": "2009-09-01T08:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42118",
    "user": "mpatel"
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

archive/issue_comments_042119.json:
```json
{
    "body": "Updated spkgs with fixed \"set -e\" problem (cf. [comment:ticket:6586:37 this comment]):\n\n* http://sage.math.washington.edu/home/mpatel/trac/5447/jquery-1.3.2.p2.spkg\n* http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p2.spkg",
    "created_at": "2009-09-05T14:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42119",
    "user": "mpatel"
}
```

Updated spkgs with fixed "set -e" problem (cf. [comment:ticket:6586:37 this comment]):

* http://sage.math.washington.edu/home/mpatel/trac/5447/jquery-1.3.2.p2.spkg
* http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p2.spkg



---

archive/issue_comments_042120.json:
```json
{
    "body": "Attachment [trac_5447-jquery_upgrade_v2-rebased.patch](tarball://root/attachments/some-uuid/ticket5447/trac_5447-jquery_upgrade_v2-rebased.patch) by jason created at 2009-09-15 18:56:38\n\napply instead of previous patches",
    "created_at": "2009-09-15T18:56:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42120",
    "user": "jason"
}
```

Attachment [trac_5447-jquery_upgrade_v2-rebased.patch](tarball://root/attachments/some-uuid/ticket5447/trac_5447-jquery_upgrade_v2-rebased.patch) by jason created at 2009-09-15 18:56:38

apply instead of previous patches



---

archive/issue_comments_042121.json:
```json
{
    "body": "Great work!\n\nThere are still two places that the old location of jquery is referenced:\n\n\n```\n~/sage/devel/sage/sage/server/notebook$ grep -r jquery.js *\nnotebook.py:           <script type=\"text/javascript\" src=\"/javascript_local/jquery/jquery.js\"></script>\ntemplates/notebook/worksheet.html:<script type=\"text/javascript\" src=\"/javascript_local/jquery/jquery.js\"></script>\n```\n",
    "created_at": "2009-09-15T19:05:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42121",
    "user": "jason"
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

archive/issue_comments_042122.json:
```json
{
    "body": "Also, can you post a picture of the new sliders up on sage-devel?  Last time I updated jqueryui, there was concern about having the squarish sliders.",
    "created_at": "2009-09-15T21:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42122",
    "user": "jason"
}
```

Also, can you post a picture of the new sliders up on sage-devel?  Last time I updated jqueryui, there was concern about having the squarish sliders.



---

archive/issue_comments_042123.json:
```json
{
    "body": "(except for the two comments from me above, this has a positive review from me).",
    "created_at": "2009-09-15T21:16:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42123",
    "user": "jason"
}
```

(except for the two comments from me above, this has a positive review from me).



---

archive/issue_comments_042124.json:
```json
{
    "body": "Apply only this patch.",
    "created_at": "2009-09-18T03:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42124",
    "user": "mpatel"
}
```

Apply only this patch.



---

archive/issue_comments_042125.json:
```json
{
    "body": "Attachment [trac_5447-jquery_upgrade_v3.patch](tarball://root/attachments/some-uuid/ticket5447/trac_5447-jquery_upgrade_v3.patch) by mpatel created at 2009-09-18 03:49:24\n\nThanks very much for pointing out those places.  [attachment:trac_5447-jquery_upgrade_v3.patch Patch v3] should cover them.  I've also [inquired](http://groups.google.com/group/sage-devel/browse_thread/thread/372c917e59b713f4) on sage-devel about the sliders.",
    "created_at": "2009-09-18T03:49:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42125",
    "user": "mpatel"
}
```

Attachment [trac_5447-jquery_upgrade_v3.patch](tarball://root/attachments/some-uuid/ticket5447/trac_5447-jquery_upgrade_v3.patch) by mpatel created at 2009-09-18 03:49:24

Thanks very much for pointing out those places.  [attachment:trac_5447-jquery_upgrade_v3.patch Patch v3] should cover them.  I've also [inquired](http://groups.google.com/group/sage-devel/browse_thread/thread/372c917e59b713f4) on sage-devel about the sliders.



---

archive/issue_comments_042126.json:
```json
{
    "body": "I've uploaded a new jQuery UI package that tweaks `patches/sage/jquery-ui-1.7.2.custom.css` to set up thinner handles for both horizontal and vertical sliders (cf. \"the middle one\" at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/372c917e59b713f4)):\n\n* http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p3.spkg",
    "created_at": "2009-09-19T06:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42126",
    "user": "mpatel"
}
```

I've uploaded a new jQuery UI package that tweaks `patches/sage/jquery-ui-1.7.2.custom.css` to set up thinner handles for both horizontal and vertical sliders (cf. "the middle one" at [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/372c917e59b713f4)):

* http://sage.math.washington.edu/home/mpatel/trac/5447/jqueryui-1.7.2.p3.spkg



---

archive/issue_comments_042127.json:
```json
{
    "body": "Okay, positive review.\n\nHowever, please use http://sage.math.washington.edu/home/jason/jqueryui-1.7.2.p3.spkg\n\nI just deleted one file that was leftover (a .orig file) and removed said file from the repository.\n\nNice work!!",
    "created_at": "2009-09-22T15:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42127",
    "user": "jason"
}
```

Okay, positive review.

However, please use http://sage.math.washington.edu/home/jason/jqueryui-1.7.2.p3.spkg

I just deleted one file that was leftover (a .orig file) and removed said file from the repository.

Nice work!!



---

archive/issue_comments_042128.json:
```json
{
    "body": "Thanks!  Sorry about not being explicit about my not wanting to fiddle further with the sliders.",
    "created_at": "2009-09-23T00:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42128",
    "user": "mpatel"
}
```

Thanks!  Sorry about not being explicit about my not wanting to fiddle further with the sliders.



---

archive/issue_comments_042129.json:
```json
{
    "body": "If the new jQuery UI package needs a review:  Positive.",
    "created_at": "2009-09-23T23:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42129",
    "user": "mpatel"
}
```

If the new jQuery UI package needs a review:  Positive.



---

archive/issue_comments_042130.json:
```json
{
    "body": "SageNB patches rebased against #7196, plus this queue: #7158, #4551, #3646, #6459.  For this ticket, apply only the following patches, in order: \n\n* http://sage.math.washington.edu/home/mpatel/trac/5447/trac_5447-sagenb_jquery_upgrade_A.patch\n* http://sage.math.washington.edu/home/mpatel/trac/5447/trac_5447-sagenb_jquery_upgrade_B.patch",
    "created_at": "2009-10-16T19:36:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42130",
    "user": "mpatel"
}
```

SageNB patches rebased against #7196, plus this queue: #7158, #4551, #3646, #6459.  For this ticket, apply only the following patches, in order: 

* http://sage.math.washington.edu/home/mpatel/trac/5447/trac_5447-sagenb_jquery_upgrade_A.patch
* http://sage.math.washington.edu/home/mpatel/trac/5447/trac_5447-sagenb_jquery_upgrade_B.patch



---

archive/issue_comments_042131.json:
```json
{
    "body": "Merged into sagenb-0.3.2 (i.e., sage-4.2).",
    "created_at": "2009-10-17T07:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42131",
    "user": "was"
}
```

Merged into sagenb-0.3.2 (i.e., sage-4.2).



---

archive/issue_comments_042132.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-17T07:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5447#issuecomment-42132",
    "user": "was"
}
```

Resolution: fixed

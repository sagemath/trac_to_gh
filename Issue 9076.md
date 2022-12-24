# Issue 9076: plot Arc of circle and ellipse

archive/issues_009076.json:
```json
{
    "body": "Assignee: vdelecroix\n\nCC:  sage-combinat kcrisman jason\n\nKeywords: plot, arc, ellipse, circle\n\nImplementation of arc plot \n\nThis just wraps the matplotlib functionnality Arc\nhttp://matplotlib.sourceforge.net/api/artist_api.html#matplotlib.patches.Arc\n\nthere is not yet fill capabilities (due to matplotlib).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9076\n\n",
    "created_at": "2010-05-28T20:12:41Z",
    "labels": [
        "geometry",
        "major",
        "bug"
    ],
    "title": "plot Arc of circle and ellipse",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9076",
    "user": "vdelecroix"
}
```
Assignee: vdelecroix

CC:  sage-combinat kcrisman jason

Keywords: plot, arc, ellipse, circle

Implementation of arc plot 

This just wraps the matplotlib functionnality Arc
http://matplotlib.sourceforge.net/api/artist_api.html#matplotlib.patches.Arc

there is not yet fill capabilities (due to matplotlib).

Issue created by migration from https://trac.sagemath.org/ticket/9076





---

archive/issue_comments_084236.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-05T11:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84236",
    "user": "vdelecroix"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084237.json:
```json
{
    "body": "I cannot review this as I know nothing about matplotlib (or graphics) and only learned 2 days ago how to draw a circle -- but what I really wanted was semicircles, so I will be happy when this is ready!",
    "created_at": "2010-06-05T15:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84237",
    "user": "cremona"
}
```

I cannot review this as I know nothing about matplotlib (or graphics) and only learned 2 days ago how to draw a circle -- but what I really wanted was semicircles, so I will be happy when this is ready!



---

archive/issue_comments_084238.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-10T00:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84238",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_084239.json:
```json
{
    "body": "This patch is corrupt (in a sense) and has two copies of each changeset.   The second changeset seems to be a little more complete, so perhaps that is the correct one?    This will certainly be very easy to fix.",
    "created_at": "2010-06-10T00:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84239",
    "user": "kcrisman"
}
```

This patch is corrupt (in a sense) and has two copies of each changeset.   The second changeset seems to be a little more complete, so perhaps that is the correct one?    This will certainly be very easy to fix.



---

archive/issue_comments_084240.json:
```json
{
    "body": "I fixed the patch (and I created another one #9203 for plotting ellipse).",
    "created_at": "2010-06-10T13:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84240",
    "user": "vdelecroix"
}
```

I fixed the patch (and I created another one #9203 for plotting ellipse).



---

archive/issue_comments_084241.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-10T13:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84241",
    "user": "vdelecroix"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084242.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-14T13:23:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84242",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_084243.json:
```json
{
    "body": "In general, I like this.  Here are some specific suggestions to make it tip-top.\n\n* line 26 - \"an arc\", not just \"arc\"\n\n* There should be some examples for the class def, since that is in reference\n\n* allowed options docs has circle a couple times rather than arc\n\n* The '_repr_' method should have an explanation of radius, maybe even to the point of checking whether it is a circle or an ellipse (and then returning an appropriate string)\n\n* Should be a plot3d method, or open a ticket to add one - though really one could just ape circle.py with x+r*cos(t*dt) and y+r*sin(t*dt) changed appropriately - and if not, then we should test the `NotImplementedError` raised in the base class.\n\n* in arc(), we should have a few changes.  First, a few more of the options should be shown in the examples.  Second, I think a 2-uple is a 2-tuple (?).  Third, clearly the radii don't need to be floats, thought presumably they should be nonnegative.  Next, the sector should be clearly pointed out to be a 2-tuple in the input.  Finally, of the two examples shown, the red one isn't!  It would be good to give an explicit example of how angle (as opposed to sector) works, perhaps similarly to the one in get_min_max_data.  One should test the `NotImplementedError` at the end (under TESTS::, I guess)",
    "created_at": "2010-06-14T13:23:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84243",
    "user": "kcrisman"
}
```

In general, I like this.  Here are some specific suggestions to make it tip-top.

* line 26 - "an arc", not just "arc"

* There should be some examples for the class def, since that is in reference

* allowed options docs has circle a couple times rather than arc

* The '_repr_' method should have an explanation of radius, maybe even to the point of checking whether it is a circle or an ellipse (and then returning an appropriate string)

* Should be a plot3d method, or open a ticket to add one - though really one could just ape circle.py with x+r*cos(t*dt) and y+r*sin(t*dt) changed appropriately - and if not, then we should test the `NotImplementedError` raised in the base class.

* in arc(), we should have a few changes.  First, a few more of the options should be shown in the examples.  Second, I think a 2-uple is a 2-tuple (?).  Third, clearly the radii don't need to be floats, thought presumably they should be nonnegative.  Next, the sector should be clearly pointed out to be a 2-tuple in the input.  Finally, of the two examples shown, the red one isn't!  It would be good to give an explicit example of how angle (as opposed to sector) works, perhaps similarly to the one in get_min_max_data.  One should test the `NotImplementedError` at the end (under TESTS::, I guess)



---

archive/issue_comments_084244.json:
```json
{
    "body": "Changing component from geometry to graphics.",
    "created_at": "2010-06-14T13:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84244",
    "user": "kcrisman"
}
```

Changing component from geometry to graphics.



---

archive/issue_comments_084245.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-14T19:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84245",
    "user": "vdelecroix"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084246.json:
```json
{
    "body": "I get two problems in arc/ellipse:\n  \n* there is an uncompatiblity of option names between disk and arc/ellipse. The function disk uses **angle** as the angle of the sector to draw as arc/ellipse uses angle but arc uses **sector**. Moreover the word **angle** is reserved for the angle between the horizontal and the angle of the first axis\n\n  * I did not find any function that allows to make some calculus modulo 2pi. I created a dummy function mod2pi that does the reduction.",
    "created_at": "2010-06-14T19:28:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84246",
    "user": "vdelecroix"
}
```

I get two problems in arc/ellipse:
  
* there is an uncompatiblity of option names between disk and arc/ellipse. The function disk uses **angle** as the angle of the sector to draw as arc/ellipse uses angle but arc uses **sector**. Moreover the word **angle** is reserved for the angle between the horizontal and the angle of the first axis

  * I did not find any function that allows to make some calculus modulo 2pi. I created a dummy function mod2pi that does the reduction.



---

archive/issue_comments_084247.json:
```json
{
    "body": "Replying to [comment:10 vdelecroix]:\n> \n>     * I did not find any function that allows to make some calculus modulo 2pi. I created a dummy function mod2pi that does the reduction.\n\n\n```\nsage: math.fmod(10,2*pi)\n3.7168146928204138\n```\n\n\nSee http://docs.python.org/library/math.html#math.fmod",
    "created_at": "2010-06-14T19:32:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84247",
    "user": "jason"
}
```

Replying to [comment:10 vdelecroix]:
> 
>     * I did not find any function that allows to make some calculus modulo 2pi. I created a dummy function mod2pi that does the reduction.


```
sage: math.fmod(10,2*pi)
3.7168146928204138
```


See http://docs.python.org/library/math.html#math.fmod



---

archive/issue_comments_084248.json:
```json
{
    "body": "I am sorry for the following laundry list.  I want to reiterate that in general this is very nice, but the hope is that this will be the best possible!  Thanks for your patience.\n\n* I think that the current algorithm for the bounding box is not the same as that in the worksheet, which seems to be pretty good.  The ellipse part works; I did find one example where the arc one didn't quite work:\n\n```\nmy_arc=arc((1,-2),2,5,-pi/5,(3*pi/2,pi/4),thickness=2)\nmy_d=my_arc[0].get_minmax_data()\nmy_arc+polygon([(my_d['xmin'],my_d['ymin']),\n          (my_d['xmin'],my_d['ymax']),\n          (my_d['xmax'],my_d['ymax']),\n          (my_d['xmax'],my_d['ymin'])],rgbcolor='red')\n```\n\n\n```\nmy_arc=arc((0,0),2,5,-pi/5,(3*pi/2,pi/4),thickness=2)\nmy_xmin,my_ymin,my_xmax,my_ymax=arc_bounding_box(2,5,-pi/5,3*pi/2,pi/4)\nmy_arc+polygon([(my_xmin,my_ymin),\n          (my_xmin,my_ymax),\n          (my_xmax,my_ymax),\n          (my_xmax,my_ymin)],rgbcolor='red')\n```\n\nMaybe the part of the algorithm that checks whether to use the sector endpoints is too lax?\n\n* The worksheet is REALLY COOL, by the way; I strongly encourage you to add more commentary, turn the graphics into interacts, and advertise it as a great way to use Sage to demonstrate basic uses of parametric calculus!\n\n* With respect to `fmod` - yes, this makes sense to use.  (Otherwise we'd have to document the dummy function!)\n\n* I'd also point out that since you already imported pi from math, there should be no need to float it (? I think?); this happens a lot in this code.\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: from math import pi\nsage: pi\n3.1415926535897931\nsage: float(pi)\n3.1415926535897931\n```\n\n| Sage Version 4.4.2, Release Date: 2010-05-19                       |\n| Type notebook() for the GUI, and license() for information.        |\n* On a related point, the constructor should be as minimal as possible; why not wait to float the radii etc. until `_render_on_subplot_()` and `get_minmax_data()`?  That would also make the representation string much easier on the eyes (and intelligible).\n\n* Space missing in the sage/plot/plot.py reference\n\n* My sense is that the point of having ``@`rename_keyword(color='rgbcolor')` is so that \n\n```\nsage: arc((0,0), 2, 1, 0, (0,pi/2), color=\"red\") \n```\n\nwould work, which is more natural to the user (though I may be misunderstanding the documentation for sage.plot.misc.rename_keyword).   I realize that circle.py doesn't really take advantage of this... and really an rgbcolor should be a 3-tuple, morally speaking... That example doesn't have linestyle='--', incidentally.\n\n* Center should still be 2-tuple, not 2-uple\n \n* One may want to point out that alpha refers to transparency.\n\n* Minh will surely point out that we wish uniformity on 2-d, 2D, 2-D, or whatever.  I think the current convention is 2-D, though some docs have 2d or 2D.  But at any rate within a file it should be consistent.\n\n* Again, in the docs for `arc()`, the radii do NOT have to be floats.\n\n* should there be a check for negative radii, like in the patch for ellipse.py?  `arc((1,1),1,-1,pi,(pi/2,pi))` is logically correct but maybe would allow bugs in code of people using `arc` to slip through.\n\nBut again all of this takes nothing away from what is in general a great contribution.",
    "created_at": "2010-06-16T14:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84248",
    "user": "kcrisman"
}
```

I am sorry for the following laundry list.  I want to reiterate that in general this is very nice, but the hope is that this will be the best possible!  Thanks for your patience.

* I think that the current algorithm for the bounding box is not the same as that in the worksheet, which seems to be pretty good.  The ellipse part works; I did find one example where the arc one didn't quite work:

```
my_arc=arc((1,-2),2,5,-pi/5,(3*pi/2,pi/4),thickness=2)
my_d=my_arc[0].get_minmax_data()
my_arc+polygon([(my_d['xmin'],my_d['ymin']),
          (my_d['xmin'],my_d['ymax']),
          (my_d['xmax'],my_d['ymax']),
          (my_d['xmax'],my_d['ymin'])],rgbcolor='red')
```


```
my_arc=arc((0,0),2,5,-pi/5,(3*pi/2,pi/4),thickness=2)
my_xmin,my_ymin,my_xmax,my_ymax=arc_bounding_box(2,5,-pi/5,3*pi/2,pi/4)
my_arc+polygon([(my_xmin,my_ymin),
          (my_xmin,my_ymax),
          (my_xmax,my_ymax),
          (my_xmax,my_ymin)],rgbcolor='red')
```

Maybe the part of the algorithm that checks whether to use the sector endpoints is too lax?

* The worksheet is REALLY COOL, by the way; I strongly encourage you to add more commentary, turn the graphics into interacts, and advertise it as a great way to use Sage to demonstrate basic uses of parametric calculus!

* With respect to `fmod` - yes, this makes sense to use.  (Otherwise we'd have to document the dummy function!)

* I'd also point out that since you already imported pi from math, there should be no need to float it (? I think?); this happens a lot in this code.

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: from math import pi
sage: pi
3.1415926535897931
sage: float(pi)
3.1415926535897931
```

| Sage Version 4.4.2, Release Date: 2010-05-19                       |
| Type notebook() for the GUI, and license() for information.        |
* On a related point, the constructor should be as minimal as possible; why not wait to float the radii etc. until `_render_on_subplot_()` and `get_minmax_data()`?  That would also make the representation string much easier on the eyes (and intelligible).

* Space missing in the sage/plot/plot.py reference

* My sense is that the point of having ``@`rename_keyword(color='rgbcolor')` is so that 

```
sage: arc((0,0), 2, 1, 0, (0,pi/2), color="red") 
```

would work, which is more natural to the user (though I may be misunderstanding the documentation for sage.plot.misc.rename_keyword).   I realize that circle.py doesn't really take advantage of this... and really an rgbcolor should be a 3-tuple, morally speaking... That example doesn't have linestyle='--', incidentally.

* Center should still be 2-tuple, not 2-uple
 
* One may want to point out that alpha refers to transparency.

* Minh will surely point out that we wish uniformity on 2-d, 2D, 2-D, or whatever.  I think the current convention is 2-D, though some docs have 2d or 2D.  But at any rate within a file it should be consistent.

* Again, in the docs for `arc()`, the radii do NOT have to be floats.

* should there be a check for negative radii, like in the patch for ellipse.py?  `arc((1,1),1,-1,pi,(pi/2,pi))` is logically correct but maybe would allow bugs in code of people using `arc` to slip through.

But again all of this takes nothing away from what is in general a great contribution.



---

archive/issue_comments_084249.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-16T14:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84249",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_084250.json:
```json
{
    "body": "Attachment [trac_9076-arc.patch](tarball://root/attachments/some-uuid/ticket9076/trac_9076-arc.patch) by vdelecroix created at 2010-06-26 14:01:54",
    "created_at": "2010-06-26T14:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84250",
    "user": "vdelecroix"
}
```

Attachment [trac_9076-arc.patch](tarball://root/attachments/some-uuid/ticket9076/trac_9076-arc.patch) by vdelecroix created at 2010-06-26 14:01:54



---

archive/issue_comments_084251.json:
```json
{
    "body": ">  * I think that the current algorithm for the bounding box is not the same as that in the worksheet, which seems to be pretty good.  The ellipse part works; I did find one example where the arc one didn't quite work:\n\nThere was a mistake... this now works on a lot (all?) examples.\n\n>  * The worksheet is REALLY COOL, by the way; I strongly encourage you to add more commentary, turn the graphics into interacts, and advertise it as a great way to use Sage to demonstrate basic uses of parametric calculus!\n\nI tried to enhanced the worksheet. I do not know what I can do more.\n \n>  * On a related point, the constructor should be as minimal as possible; why not wait to float the radii etc. until `_render_on_subplot_()` and `get_minmax_data()`?  That would also make the representation string much easier on the eyes (and intelligible).\n\nHere, I disagree because all plotting functions convert in the constructor. I do not know why, but for consistency I find it better to do this way. An other argument for this option is to get an error as soon as possible if the constructor is called with wrong argument.\n\nI corrected all the other points in the way you suggested.",
    "created_at": "2010-06-26T14:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84251",
    "user": "vdelecroix"
}
```

>  * I think that the current algorithm for the bounding box is not the same as that in the worksheet, which seems to be pretty good.  The ellipse part works; I did find one example where the arc one didn't quite work:

There was a mistake... this now works on a lot (all?) examples.

>  * The worksheet is REALLY COOL, by the way; I strongly encourage you to add more commentary, turn the graphics into interacts, and advertise it as a great way to use Sage to demonstrate basic uses of parametric calculus!

I tried to enhanced the worksheet. I do not know what I can do more.
 
>  * On a related point, the constructor should be as minimal as possible; why not wait to float the radii etc. until `_render_on_subplot_()` and `get_minmax_data()`?  That would also make the representation string much easier on the eyes (and intelligible).

Here, I disagree because all plotting functions convert in the constructor. I do not know why, but for consistency I find it better to do this way. An other argument for this option is to get an error as soon as possible if the constructor is called with wrong argument.

I corrected all the other points in the way you suggested.



---

archive/issue_comments_084252.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-26T14:06:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84252",
    "user": "vdelecroix"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084253.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-10T14:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84253",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084254.json:
```json
{
    "body": "Okay, the constructor is not so important anyway.  If we get reports that the representation string is annoying, though, I'll open another ticket.  \n\nOtherwise ENTHUSIASTIC positive review for a great addition.  Very minor changes (including putting a helper function somewhere it won't hurt doctest coverage, and a few typesetting things) attached in a reviewer patch.  Documentation now looks great, passes tests.",
    "created_at": "2010-08-10T14:47:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84254",
    "user": "kcrisman"
}
```

Okay, the constructor is not so important anyway.  If we get reports that the representation string is annoying, though, I'll open another ticket.  

Otherwise ENTHUSIASTIC positive review for a great addition.  Very minor changes (including putting a helper function somewhere it won't hurt doctest coverage, and a few typesetting things) attached in a reviewer patch.  Documentation now looks great, passes tests.



---

archive/issue_comments_084255.json:
```json
{
    "body": "Attachment [trac_9076-arc-reviewer.patch](tarball://root/attachments/some-uuid/ticket9076/trac_9076-arc-reviewer.patch) by kcrisman created at 2010-08-10 14:49:02\n\nApply after initial patch",
    "created_at": "2010-08-10T14:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84255",
    "user": "kcrisman"
}
```

Attachment [trac_9076-arc-reviewer.patch](tarball://root/attachments/some-uuid/ticket9076/trac_9076-arc-reviewer.patch) by kcrisman created at 2010-08-10 14:49:02

Apply after initial patch



---

archive/issue_comments_084256.json:
```json
{
    "body": "To release manager - this should apply fine to 4.5.2.  Apply `arc` patch first, then `arc-reviewer` patch.",
    "created_at": "2010-08-10T14:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84256",
    "user": "kcrisman"
}
```

To release manager - this should apply fine to 4.5.2.  Apply `arc` patch first, then `arc-reviewer` patch.



---

archive/issue_comments_084257.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-08-15T09:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84257",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_084258.json:
```json
{
    "body": "Please update [attachment:trac_9076-arc.patch] with a more descriptive commit string.",
    "created_at": "2010-08-15T09:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84258",
    "user": "mpatel"
}
```

Please update [attachment:trac_9076-arc.patch] with a more descriptive commit string.



---

archive/issue_comments_084259.json:
```json
{
    "body": "Replying to [comment:16 mpatel]:\n> Please update [attachment:trac_9076-arc.patch] with a more descriptive commit string.\nThis should get in, so here is a hand-edited version.  If this doesn't apply, we'll have to wait for the original author to do it, since I can never get an actual created patch to have someone else's information.  Release manager can revert to positive review if this works.",
    "created_at": "2010-08-16T12:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84259",
    "user": "kcrisman"
}
```

Replying to [comment:16 mpatel]:
> Please update [attachment:trac_9076-arc.patch] with a more descriptive commit string.
This should get in, so here is a hand-edited version.  If this doesn't apply, we'll have to wait for the original author to do it, since I can never get an actual created patch to have someone else's information.  Release manager can revert to positive review if this works.



---

archive/issue_comments_084260.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-16T12:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84260",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084261.json:
```json
{
    "body": "Same as other one, but better commit message",
    "created_at": "2010-08-16T12:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84261",
    "user": "kcrisman"
}
```

Same as other one, but better commit message



---

archive/issue_comments_084262.json:
```json
{
    "body": "Attachment [trac_9076-arc.2.patch](tarball://root/attachments/some-uuid/ticket9076/trac_9076-arc.2.patch) by mpatel created at 2010-08-16 21:16:42",
    "created_at": "2010-08-16T21:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84262",
    "user": "mpatel"
}
```

Attachment [trac_9076-arc.2.patch](tarball://root/attachments/some-uuid/ticket9076/trac_9076-arc.2.patch) by mpatel created at 2010-08-16 21:16:42



---

archive/issue_comments_084263.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-16T21:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84263",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084264.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:40:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9076#issuecomment-84264",
    "user": "mpatel"
}
```

Resolution: fixed

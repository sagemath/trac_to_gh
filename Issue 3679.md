# Issue 3679: Range Slider Control

archive/issues_003679.json:
```json
{
    "body": "Assignee: itolkov\n\nAllows to select a range using a slider with two handles. Includes a jQuery patch.\n\nDepends on #3599 and #3636.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3679\n\n",
    "created_at": "2008-07-19T06:27:37Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "Range Slider Control",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3679",
    "user": "itolkov"
}
```
Assignee: itolkov

Allows to select a range using a slider with two handles. Includes a jQuery patch.

Depends on #3599 and #3636.

Issue created by migration from https://trac.sagemath.org/ticket/3679





---

archive/issue_comments_026050.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-19T06:28:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3679#issuecomment-26050",
    "user": "itolkov"
}
```

Attachment



---

archive/issue_comments_026051.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-19T06:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3679#issuecomment-26051",
    "user": "itolkov"
}
```

Attachment



---

archive/issue_comments_026052.json:
```json
{
    "body": "Why did you need to patch jquery?  Would it be sufficient to upgrade to the newest jqueryui, which has slider controls with multiple sliders?  I'd rather not maintain a fork of jquery here.",
    "created_at": "2008-07-21T22:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3679#issuecomment-26052",
    "user": "jason"
}
```

Why did you need to patch jquery?  Would it be sufficient to upgrade to the newest jqueryui, which has slider controls with multiple sliders?  I'd rather not maintain a fork of jquery here.



---

archive/issue_comments_026053.json:
```json
{
    "body": "I wouldn't need to generally, but #3735 makes it hard to do anything Javascript-related. The old version works for some reason.\n\nOf course, the best thing for me to do here is fix #3735.",
    "created_at": "2008-07-28T20:00:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3679#issuecomment-26053",
    "user": "itolkov"
}
```

I wouldn't need to generally, but #3735 makes it hard to do anything Javascript-related. The old version works for some reason.

Of course, the best thing for me to do here is fix #3735.



---

archive/issue_comments_026054.json:
```json
{
    "body": "REFEREE REPORT:\n\n* Add documentation to interact? that illustrates how to use range_slider.\n\n* Doing range_slider? gives help on slider instead of range_slider. \n\n* I tried one example -- see http://sage.math.washington.edu/home/was/patches/3679.png and the displayed positions were different than the values of the variable when I first pressed shift enter.  Dragging the slider fixed this.\n\n```\n@interact\ndef _(t1=range_slider(2, 5, 1/5, (3,4), 'alpha')):\n    print t1\n    show(plot(sin,t1[0], t1[1]),xmin=t1[0])\n```\n\n\n* In the above example, it seems like the order of the two sliders is reversed?",
    "created_at": "2008-07-29T18:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3679#issuecomment-26054",
    "user": "was"
}
```

REFEREE REPORT:

* Add documentation to interact? that illustrates how to use range_slider.

* Doing range_slider? gives help on slider instead of range_slider. 

* I tried one example -- see http://sage.math.washington.edu/home/was/patches/3679.png and the displayed positions were different than the values of the variable when I first pressed shift enter.  Dragging the slider fixed this.

```
@interact
def _(t1=range_slider(2, 5, 1/5, (3,4), 'alpha')):
    print t1
    show(plot(sin,t1[0], t1[1]),xmin=t1[0])
```


* In the above example, it seems like the order of the two sliders is reversed?



---

archive/issue_comments_026055.json:
```json
{
    "body": "Attachment\n\nAppend to sage.patch",
    "created_at": "2008-07-29T20:33:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3679#issuecomment-26055",
    "user": "itolkov"
}
```

Attachment

Append to sage.patch



---

archive/issue_comments_026056.json:
```json
{
    "body": "Points 1 and 2 are addressed.\n\n3 and 4 - did you apply the extcode patch?",
    "created_at": "2008-07-29T20:37:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3679#issuecomment-26056",
    "user": "itolkov"
}
```

Points 1 and 2 are addressed.

3 and 4 - did you apply the extcode patch?



---

archive/issue_comments_026057.json:
```json
{
    "body": "> 3 and 4 - did you apply the extcode patch? \n\nNo, I messed up and didn't apply it.  Now everything works perfectly and the improved docs are great!  Very positive review!",
    "created_at": "2008-07-29T23:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3679#issuecomment-26057",
    "user": "was"
}
```

> 3 and 4 - did you apply the extcode patch? 

No, I messed up and didn't apply it.  Now everything works perfectly and the improved docs are great!  Very positive review!



---

archive/issue_comments_026058.json:
```json
{
    "body": "Is the jQuery patch being upstreamed? Otherwise we will have problems once we upgrade to a newer release of jQuery.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-31T01:23:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3679#issuecomment-26058",
    "user": "mabshoff"
}
```

Is the jQuery patch being upstreamed? Otherwise we will have problems once we upgrade to a newer release of jQuery.

Cheers,

Michael



---

archive/issue_comments_026059.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-31T01:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3679#issuecomment-26059",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026060.json:
```json
{
    "body": "Merged all three patches in Sage 3.1.alpha0",
    "created_at": "2008-07-31T01:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3679#issuecomment-26060",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.1.alpha0



---

archive/issue_comments_026061.json:
```json
{
    "body": "I see that 3735 is fixed now.  Does that mean that the patches above to jquery should be reverted (as per the comment above)?",
    "created_at": "2008-08-12T21:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3679#issuecomment-26061",
    "user": "jason"
}
```

I see that 3735 is fixed now.  Does that mean that the patches above to jquery should be reverted (as per the comment above)?

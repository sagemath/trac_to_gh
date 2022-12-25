# Issue 3251: plot level is really weird -- points, etc., are difficult to control whether they are above or below other plot elements

archive/issues_003251.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout @kcrisman\n\n\n```\nOn Sat, May 10, 2008 at 9:35 AM, Hector Villafuerte <hectorvd@gmail.com> wrote:\n>\n> On Sat, May 10, 2008 at 9:14 AM, louie <loufervillegas@hotmail.com> wrote:\n>>\n>> I made a custom polar grid based on circles and lines and then plotted\n>> some points but the points appeared behind the grid. I tried the\n>> documentation on these primitives and also show() but nothing on the\n>> subject.\n>\n>\n> I was sure that it depended on the order of the plots when adding\n> them... but it doesn't work for me here, since p1+p0 gives the same\n> result as p0+p1:\n>\n> sage: p0 = polar_plot(lambda t: 1, 0, 2*pi, thickness=5)\n> sage: p1 = sum([point( [cos(k), sin(k)], pointsize=70, rgbcolor='red')\n> for k in srange(0,2*pi,pi/4)])\n> sage: (p1+p0).show(aspect_ratio=1)\n> sage: (p0+p1).show(aspect_ratio=1)\n>\n> Some of the more knowledgeable users might want to comment on this.\n> Best,\n> --\n>  Hector\n\nI don't know of any way to fix this at present.   It was in Alex Clemesha's\noriginal implementation of plotting, and he never fixed it.  Somebody will\nlikely have to spend some time understanding why Sage's \"plotting using\nmatplotlib\" organizers overlaps in such a weird way and fix it.  If anybody\nalready has, please speak up.\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3251\n\n",
    "created_at": "2008-05-18T03:29:42Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "plot level is really weird -- points, etc., are difficult to control whether they are above or below other plot elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3251",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @jasongrout @kcrisman


```
On Sat, May 10, 2008 at 9:35 AM, Hector Villafuerte <hectorvd@gmail.com> wrote:
>
> On Sat, May 10, 2008 at 9:14 AM, louie <loufervillegas@hotmail.com> wrote:
>>
>> I made a custom polar grid based on circles and lines and then plotted
>> some points but the points appeared behind the grid. I tried the
>> documentation on these primitives and also show() but nothing on the
>> subject.
>
>
> I was sure that it depended on the order of the plots when adding
> them... but it doesn't work for me here, since p1+p0 gives the same
> result as p0+p1:
>
> sage: p0 = polar_plot(lambda t: 1, 0, 2*pi, thickness=5)
> sage: p1 = sum([point( [cos(k), sin(k)], pointsize=70, rgbcolor='red')
> for k in srange(0,2*pi,pi/4)])
> sage: (p1+p0).show(aspect_ratio=1)
> sage: (p0+p1).show(aspect_ratio=1)
>
> Some of the more knowledgeable users might want to comment on this.
> Best,
> --
>  Hector

I don't know of any way to fix this at present.   It was in Alex Clemesha's
original implementation of plotting, and he never fixed it.  Somebody will
likely have to spend some time understanding why Sage's "plotting using
matplotlib" organizers overlaps in such a weird way and fix it.  If anybody
already has, please speak up.

```


Issue created by migration from https://trac.sagemath.org/ticket/3251





---

archive/issue_comments_022446.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3251#issuecomment-22446",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_022447.json:
```json
{
    "body": "#6249 is related, though apparently slightly different.",
    "created_at": "2011-06-02T03:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3251#issuecomment-22447",
    "user": "https://github.com/kcrisman"
}
```

#6249 is related, though apparently slightly different.



---

archive/issue_events_007306.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3251",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3251#event-7306"
}
```



---

archive/issue_events_007307.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3251",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3251#event-7307"
}
```



---

archive/issue_events_007308.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3251",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3251#event-7308"
}
```



---

archive/issue_events_007309.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3251",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3251#event-7309"
}
```



---

archive/issue_events_007310.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3251",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3251#event-7310"
}
```



---

archive/issue_events_007311.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3251",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3251#event-7311"
}
```



---

archive/issue_events_007312.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3251",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3251#event-7312"
}
```

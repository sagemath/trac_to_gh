# Issue 2633: Notebook tweaks

archive/issues_002633.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @embray @jdemeyer @kiwifb\n\nMinor fixes/improvements for a more professional and smooth user \nexperience. \n\n1) Change the font on the links \"Toggle\", \"Home\", \"Published\", to the same sans-serif font used elsewhere in the interface. Currently, it is the only serif font present. \n\n2) The indentation of evaluated vs. never evaluated cells is slightly different, withe the former indented about 5 pixels more, at least on Firefox (OS X). \n\n3) Balance the amount of whitespace above and below the text inside the input boxes. Currently, there is more space above the input text than below it.  Probably the bottom space should be shrunk to match the top. \n\n4) There is an awful lot of white space after a cell like \"a = 1 + 1\" which has no output. This should be reduced so that more cells can be shown on screen at one time. \n\n5) The \"Js Math\" box in the lower left corner of the window can get in the way of other, more important text cells. Move it to a better location, perhaps to the lower right, or into the toolbar. \n\n6) The second row of buttons actually fall into two categories: \n\n a) Changing views of the worksheet: \"Use\", \"Edit\", \"Text\", \"Revisions\" \n\n b) Actions: \"Share\", \"Publish\". \n\nIt makes sense for the first kind to be \"tabs\" (a la the current Google docs) since you're switching between views, but the other to buttons should probably be moved up a line and put with \"Save\", \"Save & Quit\", and \"Discard & Quit\" since those are also actions.   Doing so would help solve part a) of Ticket #2632.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2633\n\n",
    "closed_at": "2019-06-16T20:07:50Z",
    "created_at": "2008-03-21T16:15:33Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Notebook tweaks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2633",
    "user": "https://github.com/NathanDunfield"
}
```
Assignee: boothby

CC:  @embray @jdemeyer @kiwifb

Minor fixes/improvements for a more professional and smooth user 
experience. 

1) Change the font on the links "Toggle", "Home", "Published", to the same sans-serif font used elsewhere in the interface. Currently, it is the only serif font present. 

2) The indentation of evaluated vs. never evaluated cells is slightly different, withe the former indented about 5 pixels more, at least on Firefox (OS X). 

3) Balance the amount of whitespace above and below the text inside the input boxes. Currently, there is more space above the input text than below it.  Probably the bottom space should be shrunk to match the top. 

4) There is an awful lot of white space after a cell like "a = 1 + 1" which has no output. This should be reduced so that more cells can be shown on screen at one time. 

5) The "Js Math" box in the lower left corner of the window can get in the way of other, more important text cells. Move it to a better location, perhaps to the lower right, or into the toolbar. 

6) The second row of buttons actually fall into two categories: 

 a) Changing views of the worksheet: "Use", "Edit", "Text", "Revisions" 

 b) Actions: "Share", "Publish". 

It makes sense for the first kind to be "tabs" (a la the current Google docs) since you're switching between views, but the other to buttons should probably be moved up a line and put with "Save", "Save & Quit", and "Discard & Quit" since those are also actions.   Doing so would help solve part a) of Ticket #2632.

Issue created by migration from https://trac.sagemath.org/ticket/2633





---

archive/issue_events_006171.json:
```json
{
    "actor": "https://github.com/garyfurnish",
    "created_at": "2008-03-21T16:34:59Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2633#event-6171"
}
```



---

archive/issue_comments_018049.json:
```json
{
    "body": "This ticket addresses too many issues. Also, (5) is done. Please split this into multiple tickets.",
    "created_at": "2009-11-15T15:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2633#issuecomment-18049",
    "user": "https://github.com/TimDumol"
}
```

This ticket addresses too many issues. Also, (5) is done. Please split this into multiple tickets.



---

archive/issue_events_006172.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2633#event-6172"
}
```



---

archive/issue_events_006173.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2633#event-6173"
}
```



---

archive/issue_events_006174.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2633#event-6174"
}
```



---

archive/issue_events_006175.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2633#event-6175"
}
```



---

archive/issue_events_006176.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2633#event-6176"
}
```



---

archive/issue_events_006177.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2633#event-6177"
}
```



---

archive/issue_events_006178.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2633#event-6178"
}
```



---

archive/issue_events_006179.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2633#event-6179"
}
```



---

archive/issue_events_006180.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2019-06-16T17:04:24Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2633#event-6180"
}
```



---

archive/issue_events_006181.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2019-06-16T17:04:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2633#event-6181"
}
```



---

archive/issue_comments_018050.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2019-06-16T17:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2633#issuecomment-18050",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_018051.json:
```json
{
    "body": "The notebook is deprecated, so maybe we can close this old ticket ?",
    "created_at": "2019-06-16T17:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2633#issuecomment-18051",
    "user": "https://github.com/fchapoton"
}
```

The notebook is deprecated, so maybe we can close this old ticket ?



---

archive/issue_comments_018052.json:
```json
{
    "body": "Replying to [comment:7 chapoton]:\n> The notebook is deprecated, so maybe we can close this old ticket ?\n\n\nYes, definitely.",
    "created_at": "2019-06-16T18:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2633#issuecomment-18052",
    "user": "https://github.com/NathanDunfield"
}
```

Replying to [comment:7 chapoton]:
> The notebook is deprecated, so maybe we can close this old ticket ?


Yes, definitely.



---

archive/issue_comments_018053.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2019-06-16T18:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2633#issuecomment-18053",
    "user": "https://github.com/NathanDunfield"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_018054.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2019-06-16T20:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2633#issuecomment-18054",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_events_006182.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2019-06-16T20:07:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2633#event-6182"
}
```

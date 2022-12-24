# Issue 2633: Notebook tweaks

archive/issues_002633.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @embray @jdemeyer @kiwifb\n\nMinor fixes/improvements for a more professional and smooth user \nexperience. \n\n1) Change the font on the links \"Toggle\", \"Home\", \"Published\", to the same sans-serif font used elsewhere in the interface. Currently, it is the only serif font present. \n\n2) The indentation of evaluated vs. never evaluated cells is slightly different, withe the former indented about 5 pixels more, at least on Firefox (OS X). \n\n3) Balance the amount of whitespace above and below the text inside the input boxes. Currently, there is more space above the input text than below it.  Probably the bottom space should be shrunk to match the top. \n\n4) There is an awful lot of white space after a cell like \"a = 1 + 1\" which has no output. This should be reduced so that more cells can be shown on screen at one time. \n\n5) The \"Js Math\" box in the lower left corner of the window can get in the way of other, more important text cells. Move it to a better location, perhaps to the lower right, or into the toolbar. \n\n6) The second row of buttons actually fall into two categories: \n\n a) Changing views of the worksheet: \"Use\", \"Edit\", \"Text\", \"Revisions\" \n\n b) Actions: \"Share\", \"Publish\". \n\nIt makes sense for the first kind to be \"tabs\" (a la the current Google docs) since you're switching between views, but the other to buttons should probably be moved up a line and put with \"Save\", \"Save & Quit\", and \"Discard & Quit\" since those are also actions.   Doing so would help solve part a) of Ticket #2632.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2633\n\n",
    "created_at": "2008-03-21T16:15:33Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Notebook tweaks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2633",
    "user": "@NathanDunfield"
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

archive/issue_comments_018088.json:
```json
{
    "body": "This ticket addresses too many issues. Also, (5) is done. Please split this into multiple tickets.",
    "created_at": "2009-11-15T15:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2633#issuecomment-18088",
    "user": "@TimDumol"
}
```

This ticket addresses too many issues. Also, (5) is done. Please split this into multiple tickets.



---

archive/issue_comments_018089.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2019-06-16T17:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2633#issuecomment-18089",
    "user": "@fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_018090.json:
```json
{
    "body": "The notebook is deprecated, so maybe we can close this old ticket ?",
    "created_at": "2019-06-16T17:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2633#issuecomment-18090",
    "user": "@fchapoton"
}
```

The notebook is deprecated, so maybe we can close this old ticket ?



---

archive/issue_comments_018091.json:
```json
{
    "body": "Replying to [comment:7 chapoton]:\n> The notebook is deprecated, so maybe we can close this old ticket ?\n\nYes, definitely.",
    "created_at": "2019-06-16T18:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2633#issuecomment-18091",
    "user": "@NathanDunfield"
}
```

Replying to [comment:7 chapoton]:
> The notebook is deprecated, so maybe we can close this old ticket ?

Yes, definitely.



---

archive/issue_comments_018092.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2019-06-16T18:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2633#issuecomment-18092",
    "user": "@NathanDunfield"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_018093.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2019-06-16T20:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2633#issuecomment-18093",
    "user": "@fchapoton"
}
```

Resolution: invalid

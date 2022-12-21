# Issue 2633: Notebook tweaks

Issue created by migration from Trac.

Original creator: dunfield

Original creation time: 2008-03-21 16:15:33

Assignee: boothby

CC:  embray jdemeyer fbissey

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


---

Comment by timdumol created at 2009-11-15 15:56:58

This ticket addresses too many issues. Also, (5) is done. Please split this into multiple tickets.


---

Comment by chapoton created at 2019-06-16 17:04:24

Changing status from new to needs_review.


---

Comment by chapoton created at 2019-06-16 17:04:24

The notebook is deprecated, so maybe we can close this old ticket ?


---

Comment by dunfield created at 2019-06-16 18:23:23

Replying to [comment:7 chapoton]:
> The notebook is deprecated, so maybe we can close this old ticket ?

Yes, definitely.


---

Comment by dunfield created at 2019-06-16 18:23:23

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2019-06-16 20:07:50

Resolution: invalid

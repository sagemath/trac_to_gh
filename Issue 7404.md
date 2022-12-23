# Issue 7404: Display as much of a worksheet's title for which there's room

Issue created by migration from https://trac.sagemath.org/ticket/7404

Original creator: mpatel

Original creation time: 2009-11-06 16:00:29

Assignee: boothby

CC:  jason timdumol was kcrisman

From [sage-devel](http://groups.google.com/group/sage-devel/msg/2973d4d2f3c2406a):

```
Jason Grout wrote:
> William Stein wrote:
>> Alex Ghitza wrote:
>>> 3. long worksheet titles get cut off even if there would be enough
>>> room to display them in their entirety (in my case, I had "Victorian
>>> Algebra Conference 2009" which appeared as "Victorian Algebra
>>> Conference 2...")

>> True.  It is tricky because fonts are proportionally spaced.

> Why does that make it tricky?  Make the div/table cell the maximum width
> possible (and expand as the browser window expands), and let the browser
> worry about when to cut off the text by setting the CSS style to chop
> off the text.  I suppose we'll miss the "..."; is that the tricky part? 
```




---

Comment by mpatel created at 2009-11-06 16:22:35

A first take that probably overdoes it.  Apply to sagenb repo.


---

Comment by mpatel created at 2009-11-06 16:37:20

Changing status from new to needs_review.


---

Attachment

The [attachment:trac_7404-css_worksheet_title.patch first take] appears to work, although a _very_ long title is visible under and beyond the "Save/Discard" buttons.

I'm sure this is just one way to [attempt to] do it --- I'm not a CSS expert.  Please feel to free to replace it.  Either way, we should check that a candidate works in IE.

By the way, this patch may depend on other recent sagenb patches.  Here's my current queue (ignore the version numbers):

```
trac_7316-sageinspect_defn.patch
trac_7318-sphinxify_confdir.patch
trac_7309-javascript-sage_v2.patch
trac_7310-modals.6.patch
trac_7332-css-escape.2.patch
trac_sagenb-7341.patch                          # Tab completion.
trac_sagenb-7346.patch                          # Vertical scrollbars.
trac_7339-sagenb_cell_bugs.patch
trac_7343-selenium-tests.4.patch
trac_7390-sagenb_test_report_A.patch
trac_7390-sagenb_test_report_B.patch
trac_7404-css_worksheet_title.patch             # This ticket!
trac_7385-renaming-published-worksheets.patch
trac_7384-sphinxify-docstrings.patch
trac_7354-jsmath_undo_revision.patch
trac_7322-jsmath_upgrade.patch
trac_7106-paren_match_doc.patch
```

But it's likely that several of these commute.


---

Comment by mpatel created at 2009-11-11 17:41:27

Replying to [comment:3:ticket6939 kcrisman]:
> Sweet.  I love CSS.


---

Comment by mpatel created at 2009-11-11 17:47:08

Replying to [comment:2 mpatel]:
> Replying to [comment:3:ticket:6939 kcrisman]:
> > Sweet.  I love CSS.
That's from [comment:3:ticket:6939 this comment], by the way.


---

Comment by kcrisman created at 2009-11-11 19:30:35

I should point out that I only love CSS, but am (also) not by any means an expert in it.  Sorry.


---

Comment by was created at 2009-11-11 23:57:29

Changing status from needs_review to needs_work.


---

Comment by was created at 2009-11-11 23:57:29

REFEREE REPORT:

 (1) Looking at and reading the code -- it looks good.

 (2) You should always set a milestone for the ticket.  It helps a *lot* in keeping tickets from getting totally lost. 

 (3) This patch makes all the worksheet titles in the homescreen vanish, so that's a serious bug.  See http://wstein.org/home/wstein/tmp/7404-a.png

 (4) This patch also makes the top bar area look ridiculous (in my opinion) when the title is really long.  See http://wstein.org/home/wstein/tmp/7404-b.png


---

Comment by mpatel created at 2009-11-25 17:14:33

A [related] possibility: Use [tablesorter](http://tablesorter.com/docs/) to sort in the browser.


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets

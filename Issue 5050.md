# Issue 5050: clean up how the percent directives at the top of cells are processed

Issue created by migration from https://trac.sagemath.org/ticket/5050

Original creator: mhansen

Original creation time: 2009-01-22 06:31:45

Assignee: boothby




---

Attachment


---

Comment by jason created at 2009-01-22 15:17:51

Notes from Mike looking at this:

  * Docs for parse_percent_directives needs to give what is returned
  * is_html doesn't need to call parse_percent_directives
  * url_to_self should have at least one line of documentation besides the examples
  * %hide and %hideall can also be cleaned up from the html and html_in methods (maybe other places)


---

Attachment


---

Comment by jason created at 2009-01-22 16:08:56

One positive review.  It's probably important enough that at least one other person ought to review it as well.

Mike and I stepped through the changes, they all look good, and I tested for about 20 minutes with various combinations of the directives and things seemed to work.  I had one glitch, but I can't reproduce it.  I had a cell that looked like:


```
%hide
%hideall
print "hi"
```


I closed the cell, reopened it, then deleted all output, then did a few more things I can't remember.  At one point, the cell changed to:


```
%hide
%hid
```


If we can't reproduce something like this, though, I give it a positive review.


---

Comment by jason created at 2009-01-22 16:10:14

In the above glitch, I mean to say that I closed the *worksheet*, reopened it, etc...


---

Comment by rlm created at 2009-01-22 16:12:09

Applies cleanly to Sage 3.3.alpha0, passes doctests, and seems to be working when I test it out. This is on Intel OSX 10.5.


---

Comment by mabshoff created at 2009-01-23 02:55:04

Resolution: fixed


---

Comment by mabshoff created at 2009-01-23 02:55:04

Merged in Sage 3.3.alpha1

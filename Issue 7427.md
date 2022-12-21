# Issue 7427: angle "wheel" widget for interacts

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-11-11 04:01:57

Assignee: boothby

CC:  mpatel

I find myself lots of times needing an angle for input in an interact.  It would be cool to have a "wheel" widget like this:

http://wiki.jqueryui.com/Wheel

See also http://maninblack.info/_proj/jquery-ui-wheel/demos/wheel/


---

Comment by mpatel created at 2009-11-11 18:35:48

An aside about the rapid-fire update problem mentioned at [comment:1:ticket:7267 #7267].  Even if `auto_update=False`, the browser piles on callbacks.  This is understandable.  But clicking "Update" before the browser runs through the backlog --- when the "spinner" is still active --- sends the queued events to the server.


---

Comment by mpatel created at 2009-11-16 18:54:10

Are the any objections to trying out [the demo mentioned above](http://maninblack.info/_proj/jquery-ui-wheel/demos/wheel/)?  It may be our only option!


---

Comment by jason created at 2009-11-16 18:59:10

definitely no objections!


---

Comment by jdemeyer created at 2017-07-04 14:27:48

This should be moved to ipywidgets.


---

Comment by jdemeyer created at 2017-07-04 14:27:48

Resolution: invalid

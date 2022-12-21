# Issue 7480: SageNB -- Move inline and <head> javascript from the templates to separate files (worksheet.js), etc.

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-11-17 11:58:03

Assignee: boothby

This will ease maintenance of javascript. Also, we can compress these and put them in one file later on, with [Juicer](http://cjohansen.no/en/ruby/juicer_a_css_and_javascript_packaging_tool), [Sprockets](http://getsprockets.com/) or [JSTools](http://pypi.python.org/pypi/JSTools/0.1b).


---

Comment by mpatel created at 2009-11-26 06:01:27

Ticket #4714 (cf. [attachment:trac_4714-sagenb_jsmath_init.patch:ticket:4714 this patch]) moves jsMath initialization from `head.tmpl` to `jsmath.js`.


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets

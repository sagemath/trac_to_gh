# Issue 6483: jsmath font broken in Firefox 3.5 on Linux

Issue created by migration from https://trac.sagemath.org/ticket/6483

Original creator: mpatel

Original creation time: 2009-07-08 13:26:34

Assignee: boothby

CC:  was

In Firefox 3.5 on Linux, jsMath's `cmmi10` font appears to be decoded improperly.  Try this [test](http://www.math.union.edu/~dpvc/jsMath/symbols/cmmi10.html).  Other fonts seem fine.

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/61bf1226d39ecf1d/c330223e1970d9c6?#c330223e1970d9c6) for more.


---

Comment by mpatel created at 2009-07-08 13:32:07

$SAGE_ROOT/local/notebook/javascript/jsmath/cmmi10.js


---

Attachment

Test worksheet.


---

Comment by mpatel created at 2009-07-08 13:48:26

I've attached a preliminary workaround.  Suggested directions:

 * Save `cmmi10.js` as `$SAGE_ROOT/local/notebook/javascript/jsmath/cmmi10.js`
 * Around line 1750 of `$SAGE_ROOT/devel/sage/sage/server/notebook/notebook.py`, replace

```
            head += '<script type="text/javascript" src="/javascript_local/jsmath/jsMath.js"></script>\n'
```

with

```
            head += '<script type="text/javascript" src="/javascript_local/jsmath/jsMath.js"></script>\n'
            head += '<script type="text/javascript">jsMath.Setup.UserEvent["pre-font"] = function () { jsMath.Setup.Script("cmmi10.js"); };</script>\n'
```

 * `sage -br`
 * Optional tests: Load and execute `cmmi10.txt` as a worksheet in the notebook.

This seems to work for me, but I haven't accounted for every character.  Feel free to improve the code or tests!


---

Comment by mpatel created at 2009-07-08 14:25:10

Note: This approach substitutes the font `cmmi10` for `jsMath-cmmi10`, which, for some reason, Firefox 3.5 is unable to decode properly.  It may help to check the system for `cmmi10.ttf`.  The relevant Fedora 10 package is `mathml-fonts`.

Some Unicode links:

[Symbols](http://www.unicode.org/charts/symbols.html)

[UTF-8 conversion tool](http://www.unicode.org/charts/symbols.html)

[Index, search, categories](http://www.fileformat.info/info/unicode/index.htm)


---

Comment by mpatel created at 2009-07-08 14:32:11

That should be [UTF-8 conversion tool](http://www.ltg.ed.ac.uk/~richard/utf-8.cgi).


---

Comment by jason created at 2009-07-18 20:39:39

Davide has updated his fonts at http://www.math.union.edu/~dpvc/jsMath/download/jsMath-fonts.html to include a special one from Firefox 3.5 on Linux.  I've been using his special font, and it seems to work great.


---

Comment by jason created at 2009-07-18 20:54:50

I've also asked Davide of his opinion of this workaround, as compared to downloading the new font he created.  I'll post here what he says if he does not post directly to sage-devel.


---

Comment by mpatel created at 2009-07-19 04:24:26

Using the new font, I think, is a much better _solution_.  I view the workaround mainly as a byproduct of trying to learn a bit more about how jsMath works.  Its modular design and lazy-loading feature, in particular, could be useful examples for other projects.  Then again, I'm more of a library user than a writer.

Please feel free to close this ticket.


---

Comment by jason created at 2009-07-19 07:20:04

Can someone invalidate this ticket?  I apparently don't have permissions to close it.


---

Comment by mvngu created at 2009-10-01 05:49:42

Resolution: invalid


---

Comment by mvngu created at 2009-10-01 05:49:42

Closing this as invalid. Use the latest jsMath fonts from http://www.math.union.edu/~dpvc/jsMath/download/jsMath-fonts.html.

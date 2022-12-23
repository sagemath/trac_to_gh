# Issue 6370: notebook -- REST search of docs in live mode is completely broken

Issue created by migration from https://trac.sagemath.org/ticket/6370

Original creator: was

Original creation time: 2009-06-20 15:38:51

Assignee: boothby

Try this:

1. Start the sage notebook and go to this URL:

```
http://localhost:8000/doc/live/reference/sage/games/sudoku.html
```

You can do that, e.g, by just clicking on Help, Reference Manual, etc.

2. Try to search for anything, e.g, integer.  

3. It doesn't work at all. 



I consider this a pretty serious bug.  Some ideas:

  * make the search box actually bring up the static docs instead, where search *DOES* work

  * disable search in the live docs.

  * fix the real problem so search works in the live docs as it should.

Any of the above would be way way better than the current situation.


---

Comment by jason created at 2010-05-15 20:58:28

I don't see the search box on that page anymore.  However, if you go to the table of contents, there is a search page listed (for example, at /doc/live/tutorial/index.html).  Clicking on the link to the search page gives the error:

Please activate JavaScript to enable the search functionality. 

Of course, javascript is already enabled.


---

Comment by kcrisman created at 2014-09-17 18:58:07

Now the javascript message is also gone, but still no search box.  This is already open upstream at https://github.com/sagemath/sagenb/issues/79.


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid

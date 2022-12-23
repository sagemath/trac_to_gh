# Issue 7445: Have jmol export a standalone html page with 3d applet

Issue created by migration from https://trac.sagemath.org/ticket/7445

Original creator: mhampton

Original creation time: 2009-11-12 17:10:27

Assignee: boothby

Keywords: jmol, graphics, 3d, applet

This ticket is analogous to #3106, but in addition to exporting a 2d image there should be a way to export a html page with the 3d applet script embedded.  

It would be assumed that the user has a jmol/ directory in the same directory as the html file - I don't see an easy way to be more flexible about that. 


---

Comment by was created at 2009-11-12 17:12:45


```
I thought this might be of some interest to people since I'm not sure
how well the process is documented.

I wanted to make some vector field plots using Jmol and then put them
on a web page.  To do that, you have to get the zipped script file
from the cell, unzip it, and put it on your web server.  The server
also has to have the jmol directory with the standard jmol .jar files
and Jmol.js (downloaded from the jmol site).

Instead of trying to explain it in detail, it may be more helpful to
look at the result:
```


http://www.d.umn.edu/~mhampton/m3298f9/vfieldplots.html

```
...for the lab the students are given a list of vector fields that
they must match to the plots.

It would be nice if this could be automated in some way, with some
sort of "export to html page" command, analogous to the "Get Image"
command currently supported.

-Marshall Hampton
```



---

Comment by rbeezer created at 2009-11-12 22:42:27

A suggestion for anybody who might implement this.  It might be nice to be able to add a caption, or explanatory text, as part of an automated conversion to an HTML page.  Maybe a command to use at the command line could include a "caption" keyword, or from the notebook a dialog might pop-up to ask?


---

Comment by ddrake created at 2009-11-12 23:33:15

It might be a good idea to look at GeoGebra's export facility -- it's really nice. It lets you select a title, author, date, and some text above and below the applet, and then drops all the files you need in a directory. I don't know if we want to copy their method, but it's a good place to get ideas. To experiment with this, just visit http://geogebra.org and do the "webstart".


---

Comment by robertwb created at 2010-01-07 06:32:27

See discussion at http://groups.google.com/group/sage-edu/browse_thread/thread/d497a28ac9dcac11?hl=en

In particular, in the latest versions of jmol one can set defaultdirectory to be inside the zip file, negating the need for an external script that does (only) that.


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid

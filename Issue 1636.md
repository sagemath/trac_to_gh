# Issue 1636: jmol 3d graphics -- make 3d output dynamically resizable

Issue created by migration from https://trac.sagemath.org/ticket/1636

Original creator: was

Original creation time: 2007-12-29 06:33:53

Assignee: was

CC:  jason


```
Robert,

It is possible to have _very_ nice dynamically resizable 3d jmol applets embedded in the Sage
notebook.  The attached demo Sage worksheet illustrates this.  To try it, do the following:

(1) Upload the worksheet.

(2) Evaluate the cell with the Torus plot in it.

(3) Refresh and view source to find the path to the actual jmol data file that defines the Torus plot.

(4) In Edit mode put that path where this is:

<script>jmolApplet(["100%","100%"], "script /home/admin/27/cells/2/sage0-size400.jmol?");</script>

(5) Use the worksheet (and maybe press refresh).  You'll get a 2-torus plot in the upper left with 
grey bars on the bottom and right of the plot -- resize them to resize the torus plot.  This even 
works fine if you start the plot spinning, view it stereographically, etc.  I.e., it is very robust.

This is just a neat proof of concept though.  To really do this right, search
for other possible resize javascript libraries, or modify the code in the sws
to be more generic. 

This resizing stuff could also be very nice for notebook output cells :-).

 -- William
```



---

Attachment

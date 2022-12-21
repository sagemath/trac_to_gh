# Issue 3702: Improve exporting 3d plots as X3D

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2008-07-21 23:46:34

Assignee: was

CC:  robertwb jpflori

After a little experimentation with viewing X3D files produced by SAGE, I found a couple of things that could hugely improve the usefulness:

 - Viewpoint: The standard viewpoint that gets written into X3D files does not seem to lead to a very good view. We could improve the ability to set the viewpoint (currently, <plot object>.viewpoint() gives a "not implemented" error), together with an orientation vector. A better default (and perhaps even some effort to compute a reasonable default) is a good idea.

 - Opacity: Currently this does not get written into X3D files at all.

 - Lighting: I couldn't find if that is supported at all at the moment.

 - Facet orientation: There is at least one viewer out there that "optimizes" its rendering by leaving out facets that are negatively/positively oriented from the viewpoint. We should check the X3D spec on whether this is a legitimate optimization in X3D. Even if it is not, it may still be a good idea to be "robust" in this respect by having an option to include facets in both orientation for, for instance, mesh objects.

 - Offering X3D files in the browser using the appropriate MIME type: When I tried writing an X3D string to a file in the notebook, the file appears, but when opened, it opens as a text file. If I save the file and approach the file locally via the browser, firefox does recognise the file as an X3D file and opens it using the preconfigured X3D viewer. This leads me to believe that the notebook serves the x3d file as a "text" file rather than an "x3d" file (why would it not?) If there is a way to tell the notebook to serve the link using the correct MIME type (the ".x3d" extension is a bit of a hint), viewing the X3D file (in this case, on a wall-filling screen, using 3D glasses) would be only one click away!


---

Comment by chapoton created at 2014-09-26 07:55:59

Changing keywords from "" to "X3D".


---

Comment by chapoton created at 2014-12-27 17:58:19

Here is a first step: transparency in x3d. Please review #7744 for the export of x3d files.
----
New commits:


---

Comment by git created at 2015-03-16 20:42:37

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by robertwb created at 2015-03-19 05:23:28

Looks mostly good. Is there any reason not to always print an opacity of 1 (to avoid repetitiveness of the code)?


---

Comment by git created at 2019-02-19 19:27:14

Branch pushed to git repo; I updated commit sha1. New commits:

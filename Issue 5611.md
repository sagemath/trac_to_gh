# Issue 5611: [with spkg; needs review] blackboard bold font for jsMath

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-03-25 21:54:28

Assignee: jhpalmieri

CC:  jason

To create this spkg, I took the file [http://www.math.union.edu/~dpvc/jsMath/download/extra-fonts/bbold10/bbold10.zip](http://www.math.union.edu/~dpvc/jsMath/download/extra-fonts/bbold10/bbold10.zip) and unzipped it.  The resulting directory gets installed into SAGE_LOCAL/notebook/javascript/jsMath/fonts; thus jsMath must be installed first.

I've never submitted an spkg before, so let me know what I need to fix.  (For example, there is no mercurial repository here; does it need one?)

This is intended to be a required part of the Sage install; it is necessary for #5610.



---

Comment by mabshoff created at 2009-03-26 00:28:15

Two things:

 * this might be better to put in the jsmath.spkg - it is certainly simpler
 * please do not attach spkgs to trac since it will be backed up daily until the end of time and a 0.5 MB spkg is rather large and does not compress well.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-26 00:29:23

John's spkg can now be found at

 http://sage.math.washington.edu/home/mabshoff/SPKG/jsmath-bbold10-0.1.spkg

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-03-26 02:48:41

Okay, if you want an updated jsMath package instead, it's here: [http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6a.p1.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6a.p1.spkg)

(I just renamed it from ...p0.spkg to ...p1.spkg. Is that the right thing to do?)


---

Comment by jhpalmieri created at 2009-03-27 17:03:55

In case we also want to upgrade jsMath from 3.6a to 3.6b (see [jsMath change log](http://www.math.union.edu/~dpvc/jsMath/changes.html)), here's another jsMath package:

[http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b.p0.spkg)

(I'll keep both the 3.6a and the 3.6b versions around for a while.)


---

Comment by jhpalmieri created at 2009-03-27 17:48:48

This may be a duplicate of another ticket, or at least of work someone is doing which will appear in another ticket, so I'm marking this as "not ready for review".  Once the situation is worked out one way or the other, I'll change this to "needs review" or else mark it as a duplicate.


---

Comment by jhpalmieri created at 2009-04-01 00:37:12

I may have been wrong about what's needed for blackboard bold: I think I want the font msbm10, not bbold10. Here are two possible jsmath spkgs:

[http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b-bbold10.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b-bbold10.p0.spkg)  (old one: bbold10)

[http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b-msbm10.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b-msbm10.p0.spkg)  (new one: msbm10)

After installing the spkg, test it by adding one line to the file sage/server/notebook/notebook.py:

```
diff -r 0a59c5ea9cac -r 9d482703384d sage/server/notebook/notebook.py
--- a/sage/server/notebook/notebook.py	Wed Mar 25 09:33:27 2009 -0700
+++ b/sage/server/notebook/notebook.py	Wed Mar 25 14:07:43 2009 -0700
`@``@` -1754,6 +1754,7 `@``@`
          jsMath.Extension.Require("verb");
          jsMath.Extension.Require("moreArrows");
          jsMath.Extension.Require("AMSmath");
+         jsMath.Extension.Require("AMSsymbols");
 </script>'''
 
         # import latex macros
```

Then in the notebook, try

```
%html
$\mathbb{R}$
```



---

Attachment


---

Comment by jhpalmieri created at 2009-04-14 21:08:18

> After installing the spkg, test it by adding one line to the file sage/server/notebook/notebook.py:

The attached patch adds this single line.  So apply the patch, install the spkg (msbm version), and try

```
%html
$\mathbb{R}$
```



---

Comment by jhpalmieri created at 2009-04-14 21:29:03

I need to clear up one thing: the correct spkg to download is here:

[http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b.p0.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/jsmath-3.6b.p0.spkg)

This is the version with the msbm font.  (The one I mentioned earlier also has this font, but the name of the spkg is wrong -- it's not just "jsmath-3.6b.p0" -- and that confuses sage.  The correct one is just a renamed version of the earlier one.)

Install this, install the patch, and things should work...

> This may be a duplicate of another ticket, or at least of work someone is doing which will appear in another ticket

I think we've waited long enough for the other ticket to appear. I'm giving up and opening this one up for review.


---

Comment by jason created at 2009-04-14 21:39:36

I agree we've waited long enough (thanks for your patience!).  I'll review it.


---

Comment by mabshoff created at 2009-04-15 22:47:22

I will review this tonight unless someone beats me to it ;). Either way - let's get this into 3.4.1.

Cheers,

Michael


---

Comment by jason created at 2009-04-16 08:36:25

I cleaned up the spkg just a tiny bit (put the fonts directory in the src/ folder and split up the changelog).  The new spkg is here: http://sage.math.washington.edu/home/jason/jsmath-3.6b.p1.spkg

Positive review on the spkg and patch.  It seems to work as advertised.


---

Comment by mabshoff created at 2009-04-16 10:39:07

Merged jsmath-3.6b.p1.spkg and jsmath-amssymbols.patch in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-16 10:39:07

Resolution: fixed

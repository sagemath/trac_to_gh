# Issue 4729: fix gnuplot execution issue

Issue created by migration from https://trac.sagemath.org/ticket/4729

Original creator: was

Original creation time: 2008-12-06 20:56:03

Assignee: was

The patch for #4657 did *not* fix the problem reported by the user, and shouldn't have got a positive review.  From the user:

```

~/bash$sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2.1, Release Date: 2008-12-01                       |
| Type notebook() for the GUI, and license() for information.        |
sage: gnuplot_console()
dyld: Symbol not found: __cg_png_create_info_struct
 Referenced from: /System/Library/Frameworks/
ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/
Versions/A/ImageIO
 Expected in: /Users/ww/Applications/Scientific/sage/local/lib//
libpng12.0.dylib

Only one function in gnuplot.py -- interact -- was fixed. However, the
gnuplot_console() function needs it too. It should read:

def gnuplot_console():
   os.system('sage-native-execute gnuplot')

With that fix, gnuplot_console() now works for me.

Wayne
```



---

Attachment


---

Comment by mabshoff created at 2008-12-07 00:31:07

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-07 09:07:01

Merged in Sage 3.2.2.alpha1


---

Comment by mabshoff created at 2008-12-07 09:07:01

Resolution: fixed

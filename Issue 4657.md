# Issue 4657: OSXL: gnuplot doesn't start due to dreaded libpng conflict

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-29 22:13:41

Assignee: mabshoff

In http://groups.google.com/group/sage-support/browse_thread/thread/9b61a7cf8fbfac7a Wayne reported:

```
/WW/Projects/Heart/bash$sage 
---------------------------------------------------------------------- 
---------------------------------------------------------------------- 
sage: gnuplot_console() 
dyld: Symbol not found: __cg_png_create_info_struct 
  Referenced from: /System/Library/Frameworks/ 
ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/ 
Versions/A/ImageIO 
  Expected in: /Users/ww/Applications/Scientific/sage/local/lib// 
libpng12.0.dylib 
sage: 
```

| Sage Version 3.2, Release Date: 2008-11-20                         | 
| Type notebook() for the GUI, and license() for information.        | 
The fix should be obvious by now.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-11-29 22:35:14

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-11-29 22:35:14

The problem only manifests itself when using a system wide gnuplot, i.e. for example a Fink one. The patch should fix that. The experimental gnuplot-4.0.0.spkg in our repo is currently slightly broken on OSX since it calls Emacs at some point and then blows up due to the same libpng issues. Oh well ...

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-30 05:40:33

Merged in Sage 3.2.1.rc1


---

Comment by mabshoff created at 2008-11-30 05:40:33

Resolution: fixed

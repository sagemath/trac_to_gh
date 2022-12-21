# Issue 4216: [with patch, needs review] use sage-native-execute to run 'convert' in animate.py

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2008-09-29 18:16:30

Assignee: somebody

Keywords: animate, convert, sage-native-execute

On my Mac, I was getting this error with the animate command:

```
sage: a = animate([sin(x + float(k)) for k in srange(0,2*pi,0.3)],
xmin=0, xmax=2*pi, figsize=[2,1])
sage: a.show()
dyld: Symbol not found: __cg_png_create_info_struct
  Referenced from:
/System/Library/Frameworks/ApplicationServices.framework/Versions/A/
Frameworks/ImageIO.framework/Versions/A/ImageIO
  Expected in: /Applications/sage/local/lib//libPng.dylib

sh: line 1: 75999 Trace/BPT trap          convert -delay 20 -loop 0
*.png
"/Users/palmieri/.sage/sage_notebook/worksheets/admin/46/cells/37/
sage0.gif" 
```

In the discussion <http://groups.google.com/group/sage-support/browse_frm/thread/526afa1bcc4b7ad5>, it was suggested that 'sage-native-execute' should be used to run the 'convert' command, and this seems to fix the problems.

Please check this on several different platforms.



---

Attachment


---

Comment by mabshoff created at 2008-09-29 19:00:56

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-29 19:01:49

Resolution: fixed


---

Comment by mabshoff created at 2008-09-29 19:01:49

Merged in Sage 3.1.3.alpha2


---

Comment by mhansen created at 2008-09-29 22:07:26

These are related: #3012 and #767

# Issue 4678: hg_sage.commit() Error on OS X 10.5.5. Conflict in libPng.dylib?

Issue created by migration from https://trac.sagemath.org/ticket/4678

Original creator: tjlahey

Original creation time: 2008-12-02 18:14:53

Assignee: cwitty

Keywords: hg, libpng

When trying hg_sage.commit() on OS X 10.5.5. I get the following error

``` 
sage: hg_sage.commit()
cd "/Users/tjlahey/sage/devel/sage" && hg diff  | less
cd "/Users/tjlahey/sage/devel/sage" && hg commit  
dyld: Symbol not found: __cg_png_create_info_struct
  Referenced from: /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/ImageIO
  Expected in: /Users/tjlahey/sage/local/lib//libPng.dylib

transaction abort!
rollback completed
abort: edit failed: mate killed by signal 5
```

So, for some reason, there is a conflict with the system frameworks. Unfortunately, this can't be commented out like Macports or Fink.


---

Comment by mabshoff created at 2008-12-02 19:28:37

Can you supply some more info, i.e. how did you build Sage, i.e. is this a FrameWork build for example. What is EDITOR set to in your environment.

In general do not open tickets unless it is clear what the bug is. This case is clearly such a case since we will need some discussion what is wrong and trac is the wrong place to do that. For that you should use sage-support instead.

Cheers,

Michael


---

Comment by tjlahey created at 2008-12-02 19:36:38

This is just a regular build of Sage on OS X 10.5.5 (using make) after moving /opt out of the way. EDITOR is set to:

``` 
EDITOR=mate -w
```

which calls TextMate, but it is crashing before then. If I use a Macports build of mercurial, I can run hg commit just fine (which is what I did after this crashed).

I'll keep your statements about tickets in mind for the future. Sorry.


---

Comment by mabshoff created at 2008-12-02 19:43:01

Resolution: wontfix


---

Comment by mabshoff created at 2008-12-02 19:43:01

Yep, mate crahes since when mercurial executes EDITOR for some stupid reason when applying patches it picks up the libpng.dylib provided by Sage. There are two solutions here: 

 * patch hg to use sage-native-execute
 * you add a dummy script into $SAGE_LOCAL/bin called mate that passes all options to the real mate, but set DYLD_LIBRARY_PATH to the original.

This should be discussed on sage-devel if we want to patch hg to use sage-native-execute for its EDITOR command, but this ticket is closed as wontfix.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-02 19:43:28

Sorry I forgot: In case we decide to patch hg this would be a new ticket.

Cheers,

Michael

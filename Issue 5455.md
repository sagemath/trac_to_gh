# Issue 5455: gap-4.4.12 -- broken on iras (itanium Linux)

Issue created by migration from https://trac.sagemath.org/ticket/5455

Original creator: was

Original creation time: 2009-03-08 05:53:51

Assignee: mabshoff

Saving and loading workspaces is broke in gap Itanium (SUSE). Also, loading of any packages is now mysteriously broken:


```
sage: !gap
    
            #########           ######         ###########           ###  
         #############          ######         ############         ####  
        ##############         ########        #############       #####  
       ###############         ########        #####   ######      #####  
      ######         #         #########       #####    #####     ######  
     ######                   ##########       #####    #####    #######  
     #####                    ##### ####       #####   ######   ########  
     ####                    #####  #####      #############   ###  ####  
     #####     #######       ####    ####      ###########    ####  ####  
     #####     #######      #####    #####     ######        ####   ####  
     #####     #######      #####    #####     #####         #############
      #####      #####     ################    #####         #############
      ######     #####     ################    #####         #############
      ################    ##################   #####                ####  
       ###############    #####        #####   #####                ####  
         #############    #####        #####   #####                ####  
          #########      #####          #####  #####                ####  
                                                                          
     Information at:  http://www.gap-system.org
     Try '?help' for help. See also  '?copyright' and  '?authors'
    
   Loading the library. Please be patient, this may take a while.
GAP4, Version: 4.4.12 of 17-Dec-2008, ia64-unknown-linux-gnu-gcc
gap> LoadPackage("braid");
fail
```



---

Comment by was created at 2009-03-08 06:09:05

Basically the filename option to SaveWorkspace seems to be randomly corrupted.


---

Attachment

I've posted a patch that just disables the workspace caching optimization completely for Itanium.    I wrote workspace caching for gap (long ago) and it is 100% just an optimization -- things should be functionally equivalent but just the first time one does "gap(...)" it is slower.  


NOTE: I also tried compiling gap with -O0 and that didn't fix this problem.


---

Comment by was created at 2009-03-08 06:13:18

Changing priority from major to blocker.


---

Comment by was created at 2009-03-08 06:16:06

I'm testing my patch.  I noticed that this fails:

```
File "/home/wstein/iras/build/sage-3.4.alpha0/devel/sage/doc/en/constructions/linear_codes.rst", line 29:
    sage: C.minimum_distance()
Exception raised:
    RuntimeError: Gap produced error output
    Variable: 'GeneratorMatCode' must have a value
```


I'm guessing the problem is that when use_workspace_cache is False, then certain packages don't get loaded, maybe.   This would be another separate bug in the gap interface.


---

Comment by mabshoff created at 2009-03-09 19:45:39

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-10 16:23:28

Merged in Sage 3.4.final.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-10 16:23:28

Resolution: fixed

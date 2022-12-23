# Issue 2150: vmware sage image -- switch to using optimal 7zip compression

Issue created by migration from https://trac.sagemath.org/ticket/2150

Original creator: was

Original creation time: 2008-02-13 20:18:22

Assignee: mabshoff


```
The best compression I got was with the following command


c:\"program files"\7-zip\7z a -t7z sage.7z sage -mx=9 -mfb=256


this breaks down as follows :  c:\"program files"\7-zip\7z : path to the executable
                           : 7z requires "dll's" 7za is complete
                           : a : this is the add command
                           : -t7z : use LZMA compression
                           : sage.7z : output file name
                           : sage  : input directory name
                           : -mx9  : use ultra compression options
                           : -mfb=256 : increase bit compare string to 256 bytes
time differential from base compression is roughly 30% 1:20 VS 1:00

this cuts the size from 522 to about 467

I hope this is useful It should save your downloaders 10min to who knows what


```



---

Comment by mabshoff created at 2008-03-20 04:24:18

For 2.10.4 we the 7z compressed image is ` sage-vmware-2.10.3.7z   11-Mar-2008 21:35  486M ` in size. So it looks like this might have been fixed. 

William, can you gives me some input on this? If you fixed this ticket please close it.

Cheers,

Michael


---

Comment by was created at 2008-03-20 10:29:51

Resolution: fixed

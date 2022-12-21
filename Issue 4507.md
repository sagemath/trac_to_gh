# Issue 4507: compile warning for planarity code

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-11-13 01:24:07

Assignee: rlm

CC:  ekirkman bober

I get the following compile warning:


```
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/home/jason/sage/local//include -I/home/jason/sage/local//include/csage -I/home/jason/sage/devel//sage/sage/ext -I/home/jason/sage/local/include/python2.5 -c sage/graphs/planarity/graphEmbed.c -o build/temp.linux-i686-2.5/sage/graphs/planarity/graphEmbed.o
sage/graphs/planarity/graphEmbed.c: In function ‘_CreateSortedSeparatedDFSChildLists’:
sage/graphs/planarity/graphEmbed.c:84: warning: implicit declaration of function ‘memset’
sage/graphs/planarity/graphEmbed.c:84: warning: incompatible implicit declaration of built-in function ‘memset’

```


I fixed this by adding #include <string.h> (which declares the memset function) to listcoll.h (where the LCReset macro is defined).



---

Attachment


---

Comment by mabshoff created at 2008-11-13 03:24:11

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-13 04:50:00

Merged in Sage 3.2.rc1


---

Comment by mabshoff created at 2008-11-13 04:50:00

Resolution: fixed

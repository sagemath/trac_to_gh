# Issue 7632: Add to developer's guide information how to write portable code.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-12-09 00:12:00

Assignee: drkirkby

As discussed on sage-devel, we need to document how to write portable POSIX conforming code, using best-practices. One such example, which started the discussion, was using 


```
test "$1" && test "$2" 
```


and NOT 


```
test "$1" -a 	"$2"
```



It would be wise to cite the URL for the 2004 POSIX standard (IEEE Std 1003.1, 2004 Edition), in the developers guide. The URL is:  

http://www.opengroup.org/onlinepubs/009695399/

(There is a later 2008 POSIX standard, but some of changes in this may not be implemented in everyone's operating system, whereas most operating systems will implement the 2004 standard). 

Unfortunately, due to what I believe is probably the use of frames, all URLs on this site appear to be the same. As such, if directing people to a URL, right-click on the item required, and copy the URL. E.g for the 'test' tool, it is:

http://www.opengroup.org/onlinepubs/009695399/utilities/test.html

For 'cp' it is

http://www.opengroup.org/onlinepubs/009695399/utilities/cp.html


---

Comment by mvngu created at 2009-12-09 00:53:02

As discussed on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/bc1ea5faa96eea13), we need to document how to write portable POSIX conforming code, using best-practices. One such example, which started the discussion, was using 


```
test "$1" && test "$2" 
```


and NOT 


```
test "$1" -a 	"$2"
```



It would be wise to cite the URL for the 2004 POSIX standard (IEEE Std 1003.1, 2004 Edition), in the developers guide. The URL is:  

http://www.opengroup.org/onlinepubs/009695399/

(There is a later 2008 POSIX standard, but some of changes in this may not be implemented in everyone's operating system, whereas most operating systems will implement the 2004 standard). 

Unfortunately, due to what I believe is probably the use of frames, all URLs on this site appear to be the same. As such, if directing people to a URL, right-click on the item required, and copy the URL. E.g for the 'test' tool, it is:

http://www.opengroup.org/onlinepubs/009695399/utilities/test.html

For 'cp' it is

http://www.opengroup.org/onlinepubs/009695399/utilities/cp.html


---

Comment by mvngu created at 2009-12-09 01:04:47

I was inattentive and put the modified ticket description in the ticket body. I have restored the ticket description with the modification. Sorry for this mistake.

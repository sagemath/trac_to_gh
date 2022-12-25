# Issue 7632: Add to developer's guide information how to write portable code.

archive/issues_007632.json:
```json
{
    "body": "Assignee: drkirkby\n\nAs discussed on sage-devel, we need to document how to write portable POSIX conforming code, using best-practices. One such example, which started the discussion, was using \n\n\n```\ntest \"$1\" && test \"$2\" \n```\n\n\nand NOT \n\n\n```\ntest \"$1\" -a \t\"$2\"\n```\n\n\n\nIt would be wise to cite the URL for the 2004 POSIX standard (IEEE Std 1003.1, 2004 Edition), in the developers guide. The URL is:  \n\nhttp://www.opengroup.org/onlinepubs/009695399/\n\n(There is a later 2008 POSIX standard, but some of changes in this may not be implemented in everyone's operating system, whereas most operating systems will implement the 2004 standard). \n\nUnfortunately, due to what I believe is probably the use of frames, all URLs on this site appear to be the same. As such, if directing people to a URL, right-click on the item required, and copy the URL. E.g for the 'test' tool, it is:\n\nhttp://www.opengroup.org/onlinepubs/009695399/utilities/test.html\n\nFor 'cp' it is\n\nhttp://www.opengroup.org/onlinepubs/009695399/utilities/cp.html\n\nIssue created by migration from https://trac.sagemath.org/ticket/7632\n\n",
    "created_at": "2009-12-09T00:12:00Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Add to developer's guide information how to write portable code.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7632",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/7632





---

archive/issue_comments_065100.json:
```json
{
    "body": "As discussed on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/bc1ea5faa96eea13), we need to document how to write portable POSIX conforming code, using best-practices. One such example, which started the discussion, was using \n\n\n```\ntest \"$1\" && test \"$2\" \n```\n\n\nand NOT \n\n\n```\ntest \"$1\" -a \t\"$2\"\n```\n\n\n\nIt would be wise to cite the URL for the 2004 POSIX standard (IEEE Std 1003.1, 2004 Edition), in the developers guide. The URL is:  \n\nhttp://www.opengroup.org/onlinepubs/009695399/\n\n(There is a later 2008 POSIX standard, but some of changes in this may not be implemented in everyone's operating system, whereas most operating systems will implement the 2004 standard). \n\nUnfortunately, due to what I believe is probably the use of frames, all URLs on this site appear to be the same. As such, if directing people to a URL, right-click on the item required, and copy the URL. E.g for the 'test' tool, it is:\n\nhttp://www.opengroup.org/onlinepubs/009695399/utilities/test.html\n\nFor 'cp' it is\n\nhttp://www.opengroup.org/onlinepubs/009695399/utilities/cp.html",
    "created_at": "2009-12-09T00:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7632#issuecomment-65100",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

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

archive/issue_comments_065101.json:
```json
{
    "body": "I was inattentive and put the modified ticket description in the ticket body. I have restored the ticket description with the modification. Sorry for this mistake.",
    "created_at": "2009-12-09T01:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7632#issuecomment-65101",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I was inattentive and put the modified ticket description in the ticket body. I have restored the ticket description with the modification. Sorry for this mistake.

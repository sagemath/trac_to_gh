# Issue 1157: make sure the sage vmware image files are < 2GB

Issue created by migration from https://trac.sagemath.org/ticket/1157

Original creator: was

Original creation time: 2007-11-12 20:54:29

Assignee: mabshoff


```

That is the problem, as the file is 2.2GB.  

-rw------- 1 sage sage 2.2G 2007-11-07 09:52 Ubuntu.vmdk

I think it's supposed to be easy (and sometimes very desirable)
to convert a filesystem in Windows from FAT32 to NTFS.  This
will make the filesystem journaled, which means the person won't
see the "checking the file system" blue screen whenever Windows
crashes and reboots.     

That said -- vmware has an option to split virtual disks into files
that are all < 2GB.  I will definitely fix the vmware machine when
i get back to Seattle to only include files that are < 2GB. However,
this will have to wait about a week.   
```



---

Comment by was created at 2007-11-15 07:24:59

Changing assignee from mabshoff to was*.


---

Comment by was created at 2007-11-15 07:24:59


```
This is ticket #1157  - see http://sagetrac.org/sage_trac/ticket/1157

William: you can convert the image using vdiskmanager. There is even a
GUI for OSX to do that - see  http://communities.vmware.com/message/674493
- that way I don't have to upload the images to sagemath. I am not
sure why I got this ticket assigned, but now the ball is back in your
court ;)

Cheers,

Michael
```



---

Comment by was created at 2007-11-15 07:25:06

Changing assignee from was* to was.


---

Comment by was created at 2007-11-15 07:25:06

Changing status from new to assigned.


---

Comment by was created at 2007-11-22 04:24:32

Resolution: fixed

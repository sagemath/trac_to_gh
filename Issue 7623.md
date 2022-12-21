# Issue 7623: Name OS X distributions automatically for PPC or Intel

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-12-08 15:29:09

Assignee: tbd

CC:  iandrus georgsweber

This was first requested in #5261, but no one is quite sure how to do it yet.   This would be the last thing to make OSX stuff more or less automatic.


---

Comment by GeorgSWeber created at 2010-02-08 22:40:05

On can do:

```
prompt$ /usr/sbin/system_profiler SPHardwareDataType
Hardware:

    Hardware Overview:

      Model Name: MacBook
      Model Identifier: MacBook2,1
      Processor Name: Intel Core 2 Duo
      Processor Speed: 2 GHz
      Number Of Processors: 1
      Total Number Of Cores: 2
      L2 Cache (per processor): 4 MB
      Memory: 2 GB
      Bus Speed: 667 MHz
      Boot ROM Version: MB21.00A5.B07
      SMC Version: 1.13f3
      Serial Number: 4H7074T5WGL
      Sudden Motion Sensor:
          State: Enabled
```

The only thing one should extract is the CPU type ("G4", "G5", or neither).

But since "uname -m" already gives you either "i386" or "PowerMacintosh", I fear that the ticket title is misleading. As far as I remember, we wanted to check whether a binary build tries to run on a system it is not made for ...


---

Comment by jdemeyer created at 2016-04-11 09:54:12

I doubt that we still support old OS X PPC.


---

Comment by jdemeyer created at 2016-04-11 09:54:12

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2016-04-11 09:54:18

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-06-12 12:02:30

Resolution: fixed

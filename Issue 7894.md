# Issue 7894: bzip2 does not always clear up before building

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-01-11 06:16:45

Assignee: GeorgSWeber

I just noticed something odd on Solaris 8. bzip2 built fine, but I started the build after modifying one a file in 'prereq'. Then I get:


```
cp -f libbz2.a /export/home/drkirkby/sage-4.3/spkg/../local/lib
chmod a+r /export/home/drkirkby/sage-4.3/spkg/../local/lib/libbz2.a
cp -f bzgrep /export/home/drkirkby/sage-4.3/spkg/../local/bin/bzgrep
ln -s -f /export/home/drkirkby/sage-4.3/spkg/../local/bin/bzgrep /export/home/drkirkby/sage-4.3/spkg/../local/bin/bzegrep
ln: cannot create /export/home/drkirkby/sage-4.3/spkg/../local/bin/bzegrep: File exists
make[2]: *** [install] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/bzip2-1.0.5'
Error installing bzip2
make[1]: *** [installed/bzip2-1.0.5] Error 1
make[1]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg'

real    0m13.366s
user    0m7.790s
sys     0m3.090s
Error building Sage. 
```


It actually leaves several files starting with the letters 'bz' in local/bin. 


---

Comment by jdemeyer created at 2014-01-09 09:32:56

Fixed in #12102


---

Comment by jdemeyer created at 2014-01-09 09:32:56

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-01-09 09:33:01

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-01-10 08:49:00

Resolution: duplicate

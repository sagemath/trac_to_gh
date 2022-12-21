# Issue 7800: dsage -- re-enable use of openssl to certificate keys, if openssl is installed  (why the notebook in secure mode is so slow to generate initial kesy!)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-31 17:19:50

Assignee: tbd

Keywords: notebook secure dsage

For some mysterious reason somebody disabled use of openssl with dsage to create certificates. This new spkg fixes this problem. The actual patch is a simple 1-liner: 

```
wstein`@`boxen:~/build/referee/sage-4.3/spkg/standard/dsage-1.0.1.p0/src/dsage/scripts$ hg diff
diff --git a/dsage/scripts/dsage_setup.py b/dsage/scripts/dsage_setup.py
--- a/dsage/scripts/dsage_setup.py
+++ b/dsage/scripts/dsage_setup.py
`@``@` -174,7 +174,7 `@``@`
     print DELIMITER
     print "Generating SSL certificate for server..."
     
-    if False and os.uname()[0] != 'Darwin' and cmd_exists('openssl'):
+    if os.uname()[0] != 'Darwin' and cmd_exists('openssl'):
         # We use openssl by default if it exists, since it is *vastly*
         # faster on Linux.
         cmd = ['openssl genrsa > %s' % privkey_file]
```


Without this, on many platforms -- e.g., sage.math -- it takes hours to generate keys, since GNUtls's key generation program is crap.


---

Comment by was created at 2009-12-31 17:21:27

Changing status from new to needs_review.


---

Comment by was created at 2009-12-31 17:21:27

The new spkg is here:

  http://wstein.org/home/wstein/patches/dsage-1.0.1.p1.spkg


---

Comment by was created at 2009-12-31 17:25:27

Post on mailing list:


```

Hi,

I kept suggesting the above, because long ago I wrote this code in dsage:

-------------
    if os.uname()[0] != 'Darwin' and cmd_exists('openssl'):
        # We use openssl by default if it exists, since it is *vastly*
        # faster on Linux.
        cmd = ['openssl genrsa > %s' % privkey_file]
        print "Using openssl to generate key"
        print cmd[0]
        subprocess.call(cmd, shell=True)
-------------

So I thought people were having issues with slow keys since they didn't have openssl installed.  However, I just checked and the above code mysteriously morphed into:

-------------
    if False and os.uname()[0] != 'Darwin' and cmd_exists('openssl'):
        # We use openssl by default if it exists, since it is *vastly*
        # faster on Linux.
        cmd = ['openssl genrsa > %s' % privkey_file]
        print "Using openssl to generate key"
        print cmd[0]
        subprocess.call(cmd, shell=True)
    else:...
-------------

I'm guessing somebody tested certtool on one platform where they got luck and certtool seemed to actually work in a reasonable amount of time, and concluded the issue was fixed.  Nope. 

Please referee

   http://trac.sagemath.org/sage_trac/ticket/7800

which reverts this behavior, switching back to using openssl if available. 
```



---

Comment by mvngu created at 2010-01-05 22:47:14

Can you check in all existing changes?

```
[mvngu`@`boxen dsage-1.0.1.p1]$ hg st
M SPKG.txt
```



---

Comment by mvngu created at 2010-01-06 01:34:00

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-06 01:34:00

I took the source tarball of Sage 4.3.1.alpha1, replaced `dsage-1.0.1.p0.spkg` with `dsage-1.0.1.p1.spkg`, and built Sage 4.3.1.alpha1 on mod.math with this updated dsage spkg. The build went OK, the only doctest failure is

```
sage -t -long devel/sage/sage/misc/sagedoc.py # 1 doctests failed
```

which is already reported at [sage-devel](http://groups.google.com/group/sage-devel/msg/4c7635baffe9b1f3). I then set the variable DOT_SAGE to a directory other than my home directory, loaded the newly compiled Sage, and started the notebook. As advertised, the RSA key generation process now uses openssl (which is available on mod.math). Using openssl, the key generation process is now much faster than previously (almost instantaneous). Before merging the updated dsage spkg, all outstanding changes need to be checked in. This is a positive review, provided that the check in issue is taken care of.


---

Comment by was created at 2010-01-06 03:42:45

> Before merging the updated dsage spkg, all outstanding changes need to 
> be checked in. This is a positive review, provided that the check in 
> issue is taken care of. 

Done.


---

Comment by rlm created at 2010-01-14 07:17:19

Resolution: fixed

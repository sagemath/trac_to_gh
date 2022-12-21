# Issue 8070: New  pycrypto-2.0.1.p5.spkg works with Open Solaris 64 bit

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2010-01-26 00:27:10

Assignee: drkirkby

Let SAGE64="yes" work with Open Solaris 64 bit too.

The spkg is here:
[http://boxen.math.washington.edu/home/jsp/ports/pycrypto-2.0.1.p5.spkg](http://boxen.math.washington.edu/home/jsp/ports/pycrypto-2.0.1.p5.spkg)



```
byte-compiling /export/home/jaap/Downloads/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/__init__.py to __init__.pyc
running install_egg_info
Writing /export/home/jaap/Downloads/sage-4.3.1/local/lib/python2.6/site-packages/pycrypto-2.0.1-py2.6.egg-info

real	0m5.851s
user	0m4.285s
sys	0m0.920s
Successfully installed pycrypto-2.0.1.p5
You can safely delete the temporary build directory
/export/home/jaap/Downloads/sage-4.3.1/spkg/build/pycrypto-2.0.1.p5
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing pycrypto-2.0.1.p5.spkg
jaap`@`opensolaris:~/Downloads/sage-4.3.1$ 

```



Jaap




---

Comment by jsp created at 2010-01-26 00:27:22

Changing status from new to needs_review.


---

Attachment


---

Comment by drkirkby created at 2010-01-27 12:25:26

It has 'echo "64 bit MacIntel" which is not correct.


---

Comment by drkirkby created at 2010-01-27 12:25:26

Changing status from needs_review to needs_work.


---

Comment by jsp created at 2010-01-27 14:07:55

Changing status from needs_work to needs_review.


---

Attachment

Done.

Jaap


---

Comment by drkirkby created at 2010-01-27 16:39:24

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-01-27 16:39:24

That's fine. In future, it would be helpful if you could show evidence that the package is building ok, as 


```
Successfully installed pycrypto-2.0.1.p5
```


does not prove very much. Plenty of packages claim to 'sucessfully' install in Open Solaris, yet in practice they do not. In this case, we can see:


```
copying build/lib.solaris-2.11-i86pc-2.6/Crypto/Cipher/AES.so -> /export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher
copying build/lib.solaris-2.11-i86pc-2.6/Crypto/Cipher/DES3.so -> /export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher
copying build/lib.solaris-2.11-i86pc-2.6/Crypto/Cipher/DES.so -> /export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher
```


and using 'file' in the directory, I can indeed see the binaries are now 64-bit. 


```
drkirkby`@`hawk:~/sage-4.3.1$ file /export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/*
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/AES.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/ARC2.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/ARC4.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/Blowfish.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/CAST.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/DES3.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/DES.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/IDEA.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/__init__.py:	English text
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/__init__.pyc:	data
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/RC5.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/XOR.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
drkirkby`@`hawk:~/sage-4.3.1$ 
```


So a positive review from me. 

Sorry to sometimes ask for extra things, but it is easier for the reviewer if he can see evidence this fixes the bug. As I've done many of these Solaris fixes, and see some from  you, I can see ways of improving some things. 

Dave


---

Comment by mpatel created at 2010-02-11 15:17:47

Resolution: fixed

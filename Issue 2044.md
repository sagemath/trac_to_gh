# Issue 2044: make sage -upgrade work with caching proxy servers

Issue created by migration from https://trac.sagemath.org/ticket/2044

Original creator: mabshoff

Original creation time: 2008-02-04 04:39:10

Assignee: mabshoff

In http://groups.google.com/group/sage-devel/t/e88f02da4c345cb7 Phil reports the following problem:

```
Hello,

I had many troubles getting the upgrade through a caching proxy on
which I've no control.
When running sage -upgrade, the proxy didn't let me getting the latest
versions, which made troubles with the critical files:
http://www.sagemath.org/packages/standard/list
http://www.sagemath.org/packages/standard/deps
http://www.sagemath.org/packages/standard/newest_version
http://www.sagemath.org/packages/standard/README
http://www.sagemath.org/packages/install

I could get around by providing manually the files and skipping the
download in local/bin/sage-update

But would it be possible to add some anti-caching headers to the
official sage server for those files?
It'd help a lot all people like me with a sage install behind caching
proxy.
Sth like:
 Expires: Mon, 26 Jul 1997 05:00:00 GMT"
 Cache-Control: no-store, no-cache, must-revalidate"
 Cache-Control: post-check=0, pre-check=0", false
 Pragma: no-cache

Phil 
```



---

Comment by mabshoff created at 2008-02-08 21:33:52

Some more info from Phil:

```
Apparently your server is an Apache so after googling myself I found
those pages:
http://www.askapache.com/htaccess/speed-up-sites-with-htaccess-cachin...
http://httpd.apache.org/docs/2.0/mod/mod_expires.html
http://httpd.apache.org/docs/2.0/mod/mod_headers.html#header
http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9

So I guess having a .htaccess in packages/ with sth like that is good
enough
(be sure to have modules expire and headers and to allow .htaccess
files)
<FilesMatch "(list|deps|newest_version|README)$">
<IfModule mod_expires.c>
  # any Expires Directives go here
  ExpiresActive On
  ExpiresDefault access
</IfModule>
<IfModule mod_headers.c>
  # any Header directives go here
  Header set Cache-Control "no-store, no-cache, must-revalidate, max-
age=0"
  Header set Pragma "no-cache"
</IfModule>
</FilesMatch>

And same for ../install

To be tested with sth like:
 wget -O /dev/null -S http://www.sagemath.org/packages/standard/list
to see the headers returned by the Apache server 
```


Cheers,

Michael


---

Comment by jdemeyer created at 2013-12-31 11:16:53

Changing component from distribution to website/wiki.


---

Comment by mkoeppe created at 2021-08-26 03:44:58

outdated, should close


---

Comment by mkoeppe created at 2021-08-26 03:44:58

Changing status from new to needs_review.


---

Comment by lorenz created at 2021-08-27 04:52:57

Indeed, none of those URLs exist anymore (and we can assume that neither does the proxy).


---

Comment by lorenz created at 2021-08-27 04:52:57

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2021-09-02 18:48:47

Resolution: invalid

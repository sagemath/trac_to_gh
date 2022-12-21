# Issue 2351: sagenb.org SSL certificate is expired

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-02-29 02:45:25

Assignee: was

The certificate expired earlier in February 2008.

It seems that the certificate was only good for a month.


---

Comment by was created at 2008-03-01 06:29:06

This requires somehow updating the apache-ssl certificate on sage.math and restarting apachessl.  This happens in 

```
/etc/apache-ssl
```

on sage.math.


---

Comment by jason created at 2008-03-02 01:49:17

From http://www.apache-ssl.org/


```
Now I've got my server installed, how do I create a test certificate?

Step one - create the key and request:

  openssl req -new > new.cert.csr

Step two - remove the passphrase from the key (optional):

  openssl rsa -in privkey.pem -out new.cert.key

Step three - convert request into signed cert:

   openssl x509 -in new.cert.csr -out new.cert.cert -req -signkey new.cert.key -days 365

The Apache-SSL directives that you need to use the resulting cert are:

  SSLCertificateFile /path/to/certs/new.cert.cert
  SSLCertificateKeyFile /path/to/certs/new.cert.key

How do I create a client certificate?

Step one - create a CA certificate/key pair, as above.

Step two - sign the client request with the CA key:

  openssl x509 -req -in client.cert.csr -out client.cert.cert -signkey my.CA.key -CA my.CA.cert -CAkey my.CA.key -CAcreateserial -days 365

Step three - issue the file 'client.cert.cert' to the requester.

The Apache-SSL directives that you need to validate against this cert are:

  SSLCACertificateFile /path/to/certs/my.CA.cert
  SSLVerifyClient 2
```



---

Comment by mabshoff created at 2008-03-19 04:08:17

This is still a problem, at least according to Firefox 3.0b4:

```
Secure Connection Failed

sagenb.com uses an invalid security certificate.

The certificate is not trusted because it is self signed.
The certificate is only valid for www.sagenb.org.
The certificate expired on 02/20/2008 06:22 AM.

(Error code: sec_error_expired_issuer_certificate)
```



---

Comment by mabshoff created at 2008-03-19 04:08:30

Changing priority from major to blocker.


---

Comment by was created at 2008-03-19 11:10:39

You have to fix this on sagemath.org by editing files in /etc/apache-ssl, I think.


---

Comment by was created at 2008-04-02 13:16:57

I may have just fixed this by typing

```
sage:/etc/apache-ssl# openssl req -new -x509 -days 365 -nodes -out apache.pem -keyout apache.pem
```


on sage.math.washington.edu.  Can somebody check if the certificate is now no longer expired.  If so, this ticket can be closed.


---

Comment by mabshoff created at 2008-04-02 13:29:19

I still get after a clearing of the cache and a couple reloads:

```
www.sagenb.org uses an invalid security certificate.

The certificate is not trusted because it is self signed.
The certificate expired on 02/20/2008 06:22 AM.

(Error code: sec_error_expired_issuer_certificate)
```

Maybe you need to restart the webserver?

Cheers,

Michael


---

Comment by robertwb created at 2008-04-18 08:39:39

I am also getting an error because the certificate is issued to "William Stein" rather than "sagenb.org"


---

Comment by mabshoff created at 2008-06-09 06:38:37

Well, I both points have been addressed:

 * the certificate is now sigened by www.sagenb.org
 * it no longer is expired

But since the certificate will expire a month after creation, i.e. 7/2/2008 we might want to create a certificate valid for longer than a months :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-10 00:35:55

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-06-10 00:35:55

I created a new ticket that will expire in 06/08/2013, so I consider this closed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-10 00:35:55

Changing assignee from was to mabshoff.


---

Comment by gfurnish created at 2008-06-10 00:37:44

verified


---

Comment by mabshoff created at 2008-06-10 00:39:15

Resolution: fixed


---

Comment by mabshoff created at 2008-06-10 00:39:15

Fixed during the Sage 3.0.3 release cycle.

Cheers,

Michael

# Issue 2351: sagenb.org SSL certificate is expired

archive/issues_002351.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe certificate expired earlier in February 2008.\n\nIt seems that the certificate was only good for a month.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2351\n\n",
    "created_at": "2008-02-29T02:45:25Z",
    "labels": [
        "component: website/wiki",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "sagenb.org SSL certificate is expired",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2351",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

The certificate expired earlier in February 2008.

It seems that the certificate was only good for a month.

Issue created by migration from https://trac.sagemath.org/ticket/2351





---

archive/issue_comments_015758.json:
```json
{
    "body": "This requires somehow updating the apache-ssl certificate on sage.math and restarting apachessl.  This happens in \n\n```\n/etc/apache-ssl\n```\n\non sage.math.",
    "created_at": "2008-03-01T06:29:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2351#issuecomment-15758",
    "user": "https://github.com/williamstein"
}
```

This requires somehow updating the apache-ssl certificate on sage.math and restarting apachessl.  This happens in 

```
/etc/apache-ssl
```

on sage.math.



---

archive/issue_comments_015759.json:
```json
{
    "body": "From http://www.apache-ssl.org/\n\n\n```\nNow I've got my server installed, how do I create a test certificate?\n\nStep one - create the key and request:\n\n  openssl req -new > new.cert.csr\n\nStep two - remove the passphrase from the key (optional):\n\n  openssl rsa -in privkey.pem -out new.cert.key\n\nStep three - convert request into signed cert:\n\n   openssl x509 -in new.cert.csr -out new.cert.cert -req -signkey new.cert.key -days 365\n\nThe Apache-SSL directives that you need to use the resulting cert are:\n\n  SSLCertificateFile /path/to/certs/new.cert.cert\n  SSLCertificateKeyFile /path/to/certs/new.cert.key\n\nHow do I create a client certificate?\n\nStep one - create a CA certificate/key pair, as above.\n\nStep two - sign the client request with the CA key:\n\n  openssl x509 -req -in client.cert.csr -out client.cert.cert -signkey my.CA.key -CA my.CA.cert -CAkey my.CA.key -CAcreateserial -days 365\n\nStep three - issue the file 'client.cert.cert' to the requester.\n\nThe Apache-SSL directives that you need to validate against this cert are:\n\n  SSLCACertificateFile /path/to/certs/my.CA.cert\n  SSLVerifyClient 2\n```\n",
    "created_at": "2008-03-02T01:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2351#issuecomment-15759",
    "user": "https://github.com/jasongrout"
}
```

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

archive/issue_comments_015760.json:
```json
{
    "body": "This is still a problem, at least according to Firefox 3.0b4:\n\n```\nSecure Connection Failed\n\nsagenb.com uses an invalid security certificate.\n\nThe certificate is not trusted because it is self signed.\nThe certificate is only valid for www.sagenb.org.\nThe certificate expired on 02/20/2008 06:22 AM.\n\n(Error code: sec_error_expired_issuer_certificate)\n```\n",
    "created_at": "2008-03-19T04:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2351#issuecomment-15760",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

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

archive/issue_comments_015761.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-03-19T04:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2351#issuecomment-15761",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_events_005541.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-19T04:08:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2351",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2351#event-5541"
}
```



---

archive/issue_comments_015762.json:
```json
{
    "body": "You have to fix this on sagemath.org by editing files in /etc/apache-ssl, I think.",
    "created_at": "2008-03-19T11:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2351#issuecomment-15762",
    "user": "https://github.com/williamstein"
}
```

You have to fix this on sagemath.org by editing files in /etc/apache-ssl, I think.



---

archive/issue_comments_015763.json:
```json
{
    "body": "I may have just fixed this by typing\n\n```\nsage:/etc/apache-ssl# openssl req -new -x509 -days 365 -nodes -out apache.pem -keyout apache.pem\n```\n\n\non sage.math.washington.edu.  Can somebody check if the certificate is now no longer expired.  If so, this ticket can be closed.",
    "created_at": "2008-04-02T13:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2351#issuecomment-15763",
    "user": "https://github.com/williamstein"
}
```

I may have just fixed this by typing

```
sage:/etc/apache-ssl# openssl req -new -x509 -days 365 -nodes -out apache.pem -keyout apache.pem
```


on sage.math.washington.edu.  Can somebody check if the certificate is now no longer expired.  If so, this ticket can be closed.



---

archive/issue_comments_015764.json:
```json
{
    "body": "I still get after a clearing of the cache and a couple reloads:\n\n```\nwww.sagenb.org uses an invalid security certificate.\n\nThe certificate is not trusted because it is self signed.\nThe certificate expired on 02/20/2008 06:22 AM.\n\n(Error code: sec_error_expired_issuer_certificate)\n```\n\nMaybe you need to restart the webserver?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-02T13:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2351#issuecomment-15764",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

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

archive/issue_comments_015765.json:
```json
{
    "body": "I am also getting an error because the certificate is issued to \"William Stein\" rather than \"sagenb.org\"",
    "created_at": "2008-04-18T08:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2351#issuecomment-15765",
    "user": "https://github.com/robertwb"
}
```

I am also getting an error because the certificate is issued to "William Stein" rather than "sagenb.org"



---

archive/issue_comments_015766.json:
```json
{
    "body": "Well, I both points have been addressed:\n\n* the certificate is now sigened by www.sagenb.org\n* it no longer is expired\n\nBut since the certificate will expire a month after creation, i.e. 7/2/2008 we might want to create a certificate valid for longer than a months :)\n\nCheers,\n\nMichael",
    "created_at": "2008-06-09T06:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2351#issuecomment-15766",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Well, I both points have been addressed:

* the certificate is now sigened by www.sagenb.org
* it no longer is expired

But since the certificate will expire a month after creation, i.e. 7/2/2008 we might want to create a certificate valid for longer than a months :)

Cheers,

Michael



---

archive/issue_comments_015767.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-10T00:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2351#issuecomment-15767",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015768.json:
```json
{
    "body": "I created a new ticket that will expire in 06/08/2013, so I consider this closed.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-10T00:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2351#issuecomment-15768",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I created a new ticket that will expire in 06/08/2013, so I consider this closed.

Cheers,

Michael



---

archive/issue_comments_015769.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2008-06-10T00:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2351#issuecomment-15769",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_015770.json:
```json
{
    "body": "verified",
    "created_at": "2008-06-10T00:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2351#issuecomment-15770",
    "user": "https://github.com/garyfurnish"
}
```

verified



---

archive/issue_comments_015771.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-10T00:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2351#issuecomment-15771",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005542.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-10T00:39:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2351",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2351#event-5542"
}
```



---

archive/issue_comments_015772.json:
```json
{
    "body": "Fixed during the Sage 3.0.3 release cycle.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-10T00:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2351#issuecomment-15772",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed during the Sage 3.0.3 release cycle.

Cheers,

Michael

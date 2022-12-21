# Issue 8182: Camino browser crashed when notebook started using Mac OSX

Issue created by migration from Trac.

Original creator: jhelffrich

Original creation time: 2010-02-03 23:45:58

Assignee: was

Keywords: OSX, Snow Leopard

I just installed SAGE on a Macbook Pro running Snow Leopard.  I got sage running in Terminal and typed notebook().  A notebook came up in Camino (which I use) and asked for me to set a password.  After I did that the browser crashed with this bug report:

2/3/10 5:26:47 PM	Camino[480]	*** Terminating app due to uncaught exception 'JavaNativeException', reason: 'java.lang.NoClassDefFoundError: sun/plugin/javascript/webkit/JSObject'
*** Call stack at first throw:
(
	0   CoreFoundation                      0x969d240a __raiseError + 410
	1   libobjc.A.dylib                     0x922ed509 objc_exception_throw + 56
	2   CoreFoundation                      0x96a1ca21 -[NSException raise] + 17
	3   JavaPluginCocoa                     0x197438ce registerNatives + 129
	4   JavaEmbeddingPlugin                 0x1cd5da65 Java_callRegisterNatives + 402
	5   ???                                 0x3100b839 0x0 + 822130745
)


---

Comment by kcrisman created at 2014-12-10 21:44:30

Given that [Camino itself says it has come to an end](http://caminobrowser.org/), I guess it's time to close this ticket.


---

Comment by kcrisman created at 2014-12-10 21:44:30

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-12-10 21:44:54

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2014-12-10 21:44:54

Not that there couldn't be a bug here!  But how could we find it...


---

Comment by vbraun created at 2014-12-11 18:35:16

Resolution: wontfix

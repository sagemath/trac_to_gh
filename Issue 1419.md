# Issue 1419: notebook java3d plotting requires Internet access

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-12-07 16:31:39

Assignee: robertwb

When my laptop is disconnected from the Internet, I can still run a local notebook on https://localhost:8000/ and access it with almost full functionality.  However, the java3d plotting fails.  In the Java console, I get a backtrace:

```
java.net.ConnectException: Network is unreachable
	at java.net.PlainSocketImpl.socketConnect(Native Method)
	at java.net.PlainSocketImpl.doConnect(PlainSocketImpl.java:333)
	at java.net.PlainSocketImpl.connectToAddress(PlainSocketImpl.java:195)
	at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:182)
	at java.net.Socket.connect(Socket.java:519)
	at sun.net.NetworkClient.doConnect(NetworkClient.java:155)
	at sun.net.www.http.HttpClient.openServer(HttpClient.java:388)
	at sun.net.www.http.HttpClient.openServer(HttpClient.java:500)
	at sun.net.www.http.HttpClient.<init>(HttpClient.java:233)
	at sun.net.www.http.HttpClient.New(HttpClient.java:306)
	at sun.net.www.http.HttpClient.New(HttpClient.java:318)
	at sun.net.www.protocol.http.HttpURLConnection.getNewHttpClient(HttpURLConnection.java:792)
	at sun.net.www.protocol.http.HttpURLConnection.plainConnect(HttpURLConnection.java:733)
	at sun.net.www.protocol.http.HttpURLConnection.connect(HttpURLConnection.java:658)
	at org.jdesktop.applet.util.JNLPAppletLauncher.processNativeJar(JNLPAppletLauncher.java:1527)
	at org.jdesktop.applet.util.JNLPAppletLauncher.initResources(JNLPAppletLauncher.java:1342)
	at org.jdesktop.applet.util.JNLPAppletLauncher.initAndStartApplet(JNLPAppletLauncher.java:1246)
	at org.jdesktop.applet.util.JNLPAppletLauncher.access$000(JNLPAppletLauncher.java:650)
	at org.jdesktop.applet.util.JNLPAppletLauncher$1.run(JNLPAppletLauncher.java:899)
Dec 7, 2007 8:11:30 AM org.jdesktop.applet.util.JNLPAppletLauncher displayError
SEVERE: java.net.ConnectException: Network is unreachable
```



---

Comment by cwitty created at 2007-12-07 20:59:25

More information:

If I'm in the middle of a notebook session, and then disconnect from the Internet, then plotting functionality continues to work.  To make it fail, I follow these steps:

1) reload the page

2) in the Java Console, press 'x' ("clear classloader cache")

3) click on a "Click for interactive view." java3d link.

(I follow these steps whenever I change sage3d.jar, to make the changes take effect.)


---

Comment by was created at 2008-04-05 20:47:57


```
13:47 < wstein-2813> re: 1419 -- that java3d plotting is completely different than jmol.
13:47 < wstein-2813> I think it's deprecated, though robertwb might think differently.
```



---

Comment by robertwb created at 2008-04-06 07:22:42

Yes, jmol is completely different from the java3d stuff. We can probably change this to won't fix, but I think we should leave the java3d stuff in there (as it is much faster for complicated scenes)


---

Comment by robertwb created at 2009-05-18 21:38:04

We're now using jmol for everything.


---

Comment by robertwb created at 2009-05-18 21:38:04

Resolution: wontfix

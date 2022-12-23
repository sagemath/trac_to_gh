# Issue 3573: Finance - Implementation of opentick

Issue created by migration from https://trac.sagemath.org/ticket/3573

Original creator: cswiercz

Original creation time: 2008-07-06 21:45:34

Assignee: cswiercz

CC:  robertwb

Keywords: finance, opentick,

opentick is a collection of APIs for obtaining free real-time and historical market data for trading systems and trading platforms. With these APIs, we will enable Sage to be able to stream and manipulate real-time market data.


---

Comment by cswiercz created at 2008-07-11 04:11:46

Ignore that patch. Messed up with hg. Accidentally overwrote a patch that this one depended on.


---

Comment by cswiercz created at 2008-07-16 13:41:11

Typo. Put the files in OTHeaders.tar.bz2 in /usr/local/include, _NOT_ in /usr/local/bin.


---

Comment by mabshoff created at 2008-07-16 13:59:43

Hi, 

please do not attach binaries to trac tickets since those will be backup up daily until the end of time :). I have deleted both the library and the headers.

Instead link them from the safe place, i.e. you sage.math account. In general your approach is completely wrong. What you need to do is to build an optinal OpenTick.spkg.

Cheers,

Michael


---

Attachment


---

Attachment


---

Comment by cswiercz created at 2008-08-28 18:30:35

Changing status from new to assigned.


---

Comment by cswiercz created at 2008-08-28 19:36:03

This ticket comes with an spkg. Alas, I don't have administrative privileges on Trac so I can't attach it here. You can find the spkg on `sage.math` at `/home/cswiercz/opentick1.1.spkg`. I will also post it at the top of http://cswiercz.blogspot.com.


---

Comment by mvngu created at 2008-10-26 13:08:28

For the documentation in the patch `sage-3573-opentick2.patch`, here are some possible fixes to typos:

1. The word "minutely" is usually associated with considering something in close details. The expression "by minute" (or something similar) more accurately describes a time interval.

```
-data on a variety of time intervals: hourly, minutely, or even
+data on a variety of time intervals: hourly, by minute, or even
```



2. Again, a similar comment to that in 1. applies here. I would use "by second" or something similar, but not "secondly", which hardly describes a time interval.

```
-hourly, minutely, and even secondly. To enable use of opentick, enter
+hourly, by minute, and even by second. To enable use of opentick, enter 
```



3. Again, a similar comment to that in 2. applies here.

```
-to obtain data on an hourly, minutely, or even secondly rate. This
+to obtain data on an hourly rate, or by minute, or even by second. This
```



4. 

```
-enddate are \code{datetime.date} objects. Retreives data using the
+enddate are \code{datetime.date} objects. Retrieves data using the
```



5.

```
-Return string representation of Opentick interface.
+Return a string representation of Opentick interface.
```



6.

```
-in once of the following two formats where the time
+in one of the following two formats where the time
```



7.

```
-Where 'Mon' is the first three letters of the coressponding month.
+where 'Mon' is the first three letters of the corresponding month.
```



Disclaimer: I'm an Australian, so maybe my suggestions don't make sense.


---

Comment by TimothyClemans created at 2008-11-30 01:03:14

sage-3573-opentick2.patch doesn't apply with sage-3.2 and with #3621 applied


---

Comment by slelievre created at 2019-05-13 05:45:52

Changing keywords from "finance, opentick," to "finance, opentick".


---

Comment by slelievre created at 2019-05-13 05:45:52

The link in comment:8 no longer works but see an archived version at

- https://web.archive.org/web/20080924232257/http://cswiercz.blogspot.com:80/2008/07/sage-update-opentick-situation.html


---

Comment by mkoeppe created at 2021-10-10 20:30:15

Changing status from needs_work to needs_review.


---

Comment by mkoeppe created at 2021-10-10 20:30:15

outdated after sage.finance deprecation in #32427


---

Comment by slelievre created at 2021-10-25 10:59:47

Ok.


---

Comment by slelievre created at 2021-10-25 10:59:47

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2021-10-25 15:39:21

Resolution: invalid

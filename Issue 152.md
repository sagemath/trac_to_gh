# Issue 152: errors with building givaro on RHEL 64-bit

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-10-25 21:14:27

Assignee: was


```
X-Gmail-Received: a5eccaa1e1cc40ab40a82f0fa02754a4078e0da6
Delivered-To: wstein`@`gmail.com
Received: by 10.67.22.12 with SMTP id z12cs205108ugi;
        Wed, 25 Oct 2006 10:16:25 -0700 (PDT)
Received: by 10.70.91.16 with SMTP id o16mr1455182wxb;
        Wed, 25 Oct 2006 10:16:25 -0700 (PDT)
Return-Path: <grbounce-CbSScAUAAADjaquLOqNz6IZE8tY0BxJ7=wstein=gmail.com`@`googlegroups.com>
Received: from wr-out-0304.google.com (wr-out-0708.google.com [64.233.184.241])
        by mx.google.com with ESMTP id i38si3547753wxd.2006.10.25.10.16.24;
        Wed, 25 Oct 2006 10:16:25 -0700 (PDT)
Received-SPF: pass (google.com: domain of grbounce-CbSScAUAAADjaquLOqNz6IZE8tY0BxJ7=wstein=gmail.com`@`googlegroups.com designates 64.233.184.241 as permitted sender)
DomainKey-Status: bad (test mode)
Received: by wr-out-0304.google.com with SMTP id 63so1664wra
        for <wstein`@`gmail.com>; Wed, 25 Oct 2006 10:16:24 -0700 (PDT)
Received: by 10.35.85.1 with SMTP id n1mr2238179pyl;
        Wed, 25 Oct 2006 10:15:58 -0700 (PDT)
Received: by 10.11.8.19 with SMTP id 19gr62cwh;
	Wed, 25 Oct 2006 10:15:58 -0700 (PDT)
X-Sender: kate01123`@`gmail.com
X-Apparently-To: sage-support`@`googlegroups.com
Received: by 10.36.33.2 with SMTP id g2mr689282nzg; Wed, 25 Oct 2006 10:15:57 -0700 (PDT)
Return-Path: <kate01123`@`gmail.com>
Received: from wx-out-0506.google.com (wx-out-0506.google.com [66.249.82.232]) by mx.google.com with ESMTP id h71si222978nzf.2006.10.25.10.15.56; Wed, 25 Oct 2006 10:15:57 -0700 (PDT)
Received-SPF: pass (google.com: domain of kate01123`@`gmail.com designates 66.249.82.232 as permitted sender)
DomainKey-Status: good (test mode)
Received: by wx-out-0506.google.com with SMTP id i29so186255wxd for <sage-support`@`googlegroups.com>; Wed, 25 Oct 2006 10:15:56 -0700 (PDT)
DomainKey-Signature: a=rsa-sha1; q=dns; c=nofws; s=beta; d=gmail.com; h=received:message-id:date:from:to:subject:mime-version:content-type:content-transfer-encoding:content-disposition; b=eImJgvQ4IGKD6TjJRM4nrynYb0kjrc8hvXum43gBSj2V6ZlRpvqG0ELvfbNg4IMOgtRpwWXzZxUyQ4VaemgsQpSYPl+2rGiBcEz0ldAfz/arg4fcRS0dg65o7iFc6n2Xdr2Vs7RlqnFOYB7xQYi4Cs3uvC59W08c0sks2Cv0cfw=
Received: by 10.70.29.2 with SMTP id c2mr1371954wxc; Wed, 25 Oct 2006 10:15:56 -0700 (PDT)
Received: by 10.70.74.9 with HTTP; Wed, 25 Oct 2006 10:15:56 -0700 (PDT)
Message-ID: <9c27041b0610251015q2c0c0249ifffb07f52f99654e`@`mail.gmail.com>
Date: Wed, 25 Oct 2006 13:15:56 -0400
From: "Kate Minola" <kate01123`@`gmail.com>
To: sage-support`@`googlegroups.com
Subject: [sage-support] givaro build problem and fix
Mime-Version: 1.0
Content-Type: text/plain
Reply-To: sage-support`@`googlegroups.com
Sender: sage-support`@`googlegroups.com
Precedence: bulk
X-Google-Loop: groups
Mailing-List: list sage-support`@`googlegroups.com;
	contact sage-support-owner`@`googlegroups.com
List-Id: <sage-support.googlegroups.com>
List-Post: <mailto:sage-support`@`googlegroups.com>
List-Help: <mailto:sage-support-help`@`googlegroups.com>
List-Unsubscribe: <http://googlegroups.com/group/sage-support/subscribe>,
	<mailto:sage-support-unsubscribe`@`googlegroups.com>


When I build sage-1.4.1.2 on my x86_64-Linux machine (Red
Hat Enterprise Linux 4 - As edition), I get the following
error during the givaro build:

: /usr/local/gcc-4.1.1/x86_64-Linux/lib/../lib/libstdc++.so: could not read symb
ols: File in wrong format

This is happening because the code is incorrectly trying to use

  /usr/local/gcc-4.1.1/x86_64-Linux/lib/libstdc++.so

when it should be using

  /usr/local/gcc-4.1.1/x86_64-Linux/lib64/libstdc++.so

In other words, my machine is a "multilib" machine - it has
libraries for both 32-bit and 64-bit code.  Unfortunately
the code in givaro is incorrectly trying to use 32-bit
code together with 64-bit code.

I have tracked down that the problem is due to the macro
AC_LIBTOOL_SYS_DYNAMIC_LINKER in aclocal.m4. (aclocal.m4
is used to create configure).  I reported the problem to
the libtool folks and suggested a possible solution.  It
looks like they have incorporated my solution into the
stable branch of libtool (currently libtool-1.5.23a).

Until the givaro developers start to use an updated version
of autotools (autoconf, automake, libtool), here is how
to modify givaro for SAGE.

1. Go to www.gnu.org/software/libtool and download the
latest snapshot of the stable branch of libtool.

2. Replace the macro AC_LIBTOOL_SYS_DYNAMIC_LINKER in
givaro/aclocal.m4 (lines 1190-1776) with the code for
the same macro in libtool.m4.

3. Remove configure

4. Run 'autoconf'.  This will create a new configure that
will use the new macro code.

Kate Minola
University of Maryland, College Park
```



---

Comment by malb created at 2007-02-08 21:30:01

Resolution: fixed


---

Comment by malb created at 2007-02-08 21:30:01

Fixed. Thanks so much for the detailed description and bugfix.

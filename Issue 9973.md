# Issue 9973: The current (rather old) version of GnuTLS fails to install on AIX 5.3

archive/issues_009973.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  mvngu pjeremy weger@us.ibm.com\n\nI've CC'ed Alan at IBM, so he can see I am actually looking at an AIX port of Sage, though access to faster hardware would be useful for this. Also I thought Minh might be interested, as like myself he signed up for a free AIX account at [Metamodul](http://www.metamodul.com/) though I personally found the software was not installed optimally. \n\nUsing my own rather old server. \n\n* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)\n* 4 x 332 MHz 32-bit PowerPC CPUs\n* 3 GB RAM\n* A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)\n* AIX 5.3 (A POSIX certified operating system)\n* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)\n* DDS-4 tape drive \n\nI found [GnuTLS](http://www.gnu.org/software/gnutls/) would not install. The reason for the failure is not obvious, but I can't be bothered to look into this in any depth, as the version of GnuTLS in Sage is very old. A ticket will be created to update GnuTLS.\n\nSince \n\n* IBM have expressed an interest in an AIX port of Sage and may be willing to donate hardware or provide remote access. \n* Porting software to other platforms often discovers errors\n\ngetting GnuTLS to work on AIX is worthwhile.  \n\nI've marked it as a low priority, as an AIX port is not currently being seriously worked on, but that might change, especially once the 64-bit Solaris ports are complete. I've actually spent the US equivalent of a few hundred dollars in fixing my own RS/6000 (PSU had below up), adding RAM. changing the non-functional DDS-3 tape drive for a DDS-4 tape drive and adding disk space, \n\nNote, AIX 5.3 is not the latest release (6.1 is), but AIX 6.1 will not run on 32-bit hardware. AIX 5.3 is the previous version of AIX, since there was no version 5.4 or 6.0. (IBM's version numbers seem even stranger than those used by Sage, which are themselves very strange.)\n\n\n```\ngcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -o ex-serv-anon ex-serv-anon.o  -L\n/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/lib/.libs ./.libs/libexamples.a ../../gl/.libs/libgnu.a -L/home/users/drkirkby/sage-4.6.alpha1/local/lib -L/opt/pware/lib \n-L../../lib/.libs -L../../libextra/.libs -lgnutls-extra -lopencdk -lgnutls -lz -lgcrypt -lgpg-error -lintl -liconv -lpthread -lc  -Wl,-blibpath:/home/users/drkirkby/sage-4.6.alpha1/spkg/buil\nd/gnutls-2.2.1.p5/src/lib/.libs:/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/libextra/.libs:/home/users/drkirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib:/home/users/d\nrkirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4/../../..:/usr/lib:/lib \n/bin/sh ../../libtool --tag=CC   --mode=link gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-po\ninter-sign -no-install  -o ex-client-tlsia ex-client-tlsia.o libexamples.la ../../gl/libgnu.la ../../lib/libgnutls.la ../../libextra/libgnutls-extra.la \n/bin/sh ../../libtool --tag=CC   --mode=link gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-po\ninter-sign -no-install  -o ex-serv-pgp ex-serv-pgp.o libexamples.la ../../gl/libgnu.la ../../lib/libgnutls.la ../../libextra/libgnutls-extra.la \n/bin/sh ../../libtool --tag=CC   --mode=link gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-po\ninter-sign -no-install  -o ex-client-srp ex-client-srp.o libexamples.la ../../gl/libgnu.la ../../lib/libgnutls.la ../../libextra/libgnutls-extra.la \n/bin/sh ../../libtool --tag=CC   --mode=link gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-po\ninter-sign -no-install  -o ex-serv-srp ex-serv-srp.o libexamples.la ../../gl/libgnu.la ../../lib/libgnutls.la ../../libextra/libgnutls-extra.la \ngcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -o ex-serv-pgp ex-serv-pgp.o  -L/h\nome/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/lib/.libs ./.libs/libexamples.a ../../gl/.libs/libgnu.a -L/home/users/drkirkby/sage-4.6.alpha1/local/lib -L/opt/pware/lib -L\n../../lib/.libs -L../../libextra/.libs -lgnutls-extra -lopencdk -lgnutls -lz -lgcrypt -lgpg-error -lintl -liconv -lpthread -lc  -Wl,-blibpath:/home/users/drkirkby/sage-4.6.alpha1/spkg/build/\ngnutls-2.2.1.p5/src/lib/.libs:/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/libextra/.libs:/home/users/drkirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib:/home/users/drk\nirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4/../../..:/usr/lib:/lib \ngcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -o ex-client-tlsia ex-client-tlsia\n.o  -L/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/lib/.libs ./.libs/libexamples.a ../../gl/.libs/libgnu.a -L/home/users/drkirkby/sage-4.6.alpha1/local/lib -L/opt/pwar\ne/lib -L../../lib/.libs -L../../libextra/.libs -lgnutls-extra -lopencdk -lgnutls -lz -lgcrypt -lgpg-error -lintl -liconv -lpthread -lc  -Wl,-blibpath:/home/users/drkirkby/sage-4.6.alpha1/spk\ng/build/gnutls-2.2.1.p5/src/lib/.libs:/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/libextra/.libs:/home/users/drkirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib:/home/u\nsers/drkirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4/../../..:/usr/lib:/lib \ngcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -o ex-serv-srp ex-serv-srp.o  -L/h\nome/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/lib/.libs ./.libs/libexamples.a ../../gl/.libs/libgnu.a -L/home/users/drkirkby/sage-4.6.alpha1/local/lib -L/opt/pware/lib -L\n../../lib/.libs -L../../libextra/.libs -lgnutls-extra -lopencdk -lgnutls -lz -lgcrypt -lgpg-error -lintl -liconv -lpthread -lc  -Wl,-blibpath:/home/users/drkirkby/sage-4.6.alpha1/spkg/build/\ngnutls-2.2.1.p5/src/lib/.libs:/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/libextra/.libs:/home/users/drkirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib:/home/users/drk\nirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4/../../..:/usr/lib:/lib \ngcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -o ex-client-srp ex-client-srp.o  \n-L/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/lib/.libs ./.libs/libexamples.a ../../gl/.libs/libgnu.a -L/home/users/drkirkby/sage-4.6.alpha1/local/lib -L/opt/pware/li\nb -L../../lib/.libs -L../../libextra/.libs -lgnutls-extra -lopencdk -lgnutls -lz -lgcrypt -lgpg-error -lintl -liconv -lpthread -lc  -Wl,-blibpath:/home/users/drkirkby/sage-4.6.alpha1/spkg/bu\nild/gnutls-2.2.1.p5/src/lib/.libs:/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/libextra/.libs:/home/users/drkirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib:/home/users\n/drkirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4/../../..:/usr/lib:/lib \nmake[6]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/examples'\nMaking all in scripts\nmake[6]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/scripts'\nmake[6]: warning: -jN forced in submake: disabling jobserver mode.\nmake[6]: Nothing to be done for `all'.\nmake[6]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/scripts'\nMaking all in manpages\nmake[6]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/manpages'\nmake[6]: warning: -jN forced in submake: disabling jobserver mode.\nmake[6]: Nothing to be done for `all'.\nmake[6]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/manpages'\nMaking all in credentials\nmake[6]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials'\nmake[6]: warning: -jN forced in submake: disabling jobserver mode.\nMaking all in openpgp\nmake[7]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials/openpgp'\nmake[7]: warning: -jN forced in submake: disabling jobserver mode.\nmake[7]: Nothing to be done for `all'.\nmake[7]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials/openpgp'\nMaking all in srp\nmake[7]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials/srp'\nmake[7]: warning: -jN forced in submake: disabling jobserver mode.\nmake[7]: Nothing to be done for `all'.\nmake[7]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials/srp'\nMaking all in x509\nmake[7]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials/x509'\nmake[7]: warning: -jN forced in submake: disabling jobserver mode.\nmake[7]: Nothing to be done for `all'.\nmake[7]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials/x509'\nmake[7]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials'\nmake[7]: warning: -jN forced in submake: disabling jobserver mode.\nmake[7]: Nothing to be done for `all-am'.\nmake[7]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials'\nmake[6]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials'\nmake[6]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc'\nmake[6]: warning: -jN forced in submake: disabling jobserver mode.\nmake[6]: Nothing to be done for `all-am'.\nmake[6]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc'\nmake[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc'\nmake[4]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc'\nMaking all in tests\nmake[4]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests'\nmake[4]: warning: -jN forced in submake: disabling jobserver mode.\nMaking all in rsa-md5-collision\nmake[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/rsa-md5-collision'\nmake[5]: warning: -jN forced in submake: disabling jobserver mode.\nmake[5]: Nothing to be done for `all'.\nmake[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/rsa-md5-collision'\nMaking all in pkcs1-padding\nmake[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/pkcs1-padding'\nmake[5]: warning: -jN forced in submake: disabling jobserver mode.\nmake[5]: Nothing to be done for `all'.\nmake[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/pkcs1-padding'\nMaking all in pkcs8-decode\nmake[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/pkcs8-decode'\nmake[5]: warning: -jN forced in submake: disabling jobserver mode.\nmake[5]: Nothing to be done for `all'.\nmake[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/pkcs8-decode'\nMaking all in pkcs12-decode\nmake[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/pkcs12-decode'\nmake[5]: warning: -jN forced in submake: disabling jobserver mode.\nmake[5]: Nothing to be done for `all'.\nmake[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/pkcs12-decode'\nMaking all in userid\nmake[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/userid'\nmake[5]: warning: -jN forced in submake: disabling jobserver mode.\nmake[5]: Nothing to be done for `all'.\nmake[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/userid'\nMaking all in pathlen\nmake[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/pathlen'\nmake[5]: warning: -jN forced in submake: disabling jobserver mode.\nmake[5]: Nothing to be done for `all'.\nmake[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/pathlen'\nMaking all in key-id\nmake[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/key-id'\nmake[5]: warning: -jN forced in submake: disabling jobserver mode.\nmake[5]: Nothing to be done for `all'.\nmake[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/key-id'\nMaking all in sha2\nmake[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/sha2'\nmake[5]: warning: -jN forced in submake: disabling jobserver mode.\nmake[5]: Nothing to be done for `all'.\nmake[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/sha2'\nMaking all in hostname-check\nmake[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/hostname-check'\nmake[5]: warning: -jN forced in submake: disabling jobserver mode.\nmake[5]: Nothing to be done for `all'.\nmake[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/hostname-check'\nMaking all in openpgp\nmake[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/openpgp'\nmake[5]: warning: -jN forced in submake: disabling jobserver mode.\nmake[5]: Nothing to be done for `all'.\nmake[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/openpgp'\nmake[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests'\nmake[5]: warning: -jN forced in submake: disabling jobserver mode.\n/bin/sh ../libtool --tag=CC   --mode=compile gcc -std=gnu99 -DHAVE_CONFIG_H -I. -I..  -I../lgl -I../lgl -I../gl -I../gl -I../includes -I../includes -I../doc/examples -I/home/users/drkirkby/s\nage-4.6.alpha1/local/include -I/opt/pware/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign\n -MT utils.lo -MD -MP -MF .deps/utils.Tpo -c -o utils.lo utils.c\nmkdir .libs\n gcc -std=gnu99 -DHAVE_CONFIG_H -I. -I.. -I../lgl -I../lgl -I../gl -I../gl -I../includes -I../includes -I../doc/examples -I/home/users/drkirkby/sage-4.6.alpha1/local/include -I/opt/pware/inc\nlude -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -MT utils.lo -MD -MP -MF .deps/utils.Tpo -c \nutils.c  -DPIC -o .libs/utils.o\nmv -f .deps/utils.Tpo .deps/utils.Plo\n/bin/sh ../libtool --tag=CC   --mode=link gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-point\ner-sign -no-install  -o libutils.la  utils.lo  \nar cru .libs/libutils.a .libs/utils.o\nranlib .libs/libutils.a\ncreating libutils.la\n(cd .libs && rm -f libutils.la && ln -s ../libutils.la libutils.la)\nmake[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests'\nmake[4]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests'\nMaking all in po\nmake[4]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/po'\nmake[4]: warning: -jN forced in submake: disabling jobserver mode.\nmake[4]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/po'\nmake[4]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src'\nmake[4]: warning: -jN forced in submake: disabling jobserver mode.\nmake[4]: Nothing to be done for `all-am'.\nmake[4]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src'\nmake[3]: *** [all-recursive] Error 1\nmake[3]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src'\nmake[2]: *** [all] Error 2\nmake[2]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src'\nfailed to build GNUTLS\n\nreal    21m9.822s\nuser    14m6.587s\nsys     3m56.694s\nsage: An error occurred while installing gnutls-2.2.1.p5\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9974\n\n",
    "created_at": "2010-09-23T09:03:18Z",
    "labels": [
        "porting: AIX or HP-UX",
        "minor",
        "bug"
    ],
    "title": "The current (rather old) version of GnuTLS fails to install on AIX 5.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9973",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  mvngu pjeremy weger@us.ibm.com

I've CC'ed Alan at IBM, so he can see I am actually looking at an AIX port of Sage, though access to faster hardware would be useful for this. Also I thought Minh might be interested, as like myself he signed up for a free AIX account at [Metamodul](http://www.metamodul.com/) though I personally found the software was not installed optimally. 

Using my own rather old server. 

* IBM [RS/6000 7025 F50](http://publib.boulder.ibm.com/infocenter/pseries/v5r3/index.jsp?topic=/com.ibm.pseries.doc/hardware_docs/rs6000_7025f50series.htm)
* 4 x 332 MHz 32-bit PowerPC CPUs
* 3 GB RAM
* A fair wide mixture of disks sizes (3 x 9 GB, 1 x 18 GB, 2 x 36 GB and 1 x 73 GB)
* AIX 5.3 (A POSIX certified operating system)
* gcc 4.2.4 downloaded from [pware](http://pware.hvcc.edu/)
* DDS-4 tape drive 

I found [GnuTLS](http://www.gnu.org/software/gnutls/) would not install. The reason for the failure is not obvious, but I can't be bothered to look into this in any depth, as the version of GnuTLS in Sage is very old. A ticket will be created to update GnuTLS.

Since 

* IBM have expressed an interest in an AIX port of Sage and may be willing to donate hardware or provide remote access. 
* Porting software to other platforms often discovers errors

getting GnuTLS to work on AIX is worthwhile.  

I've marked it as a low priority, as an AIX port is not currently being seriously worked on, but that might change, especially once the 64-bit Solaris ports are complete. I've actually spent the US equivalent of a few hundred dollars in fixing my own RS/6000 (PSU had below up), adding RAM. changing the non-functional DDS-3 tape drive for a DDS-4 tape drive and adding disk space, 

Note, AIX 5.3 is not the latest release (6.1 is), but AIX 6.1 will not run on 32-bit hardware. AIX 5.3 is the previous version of AIX, since there was no version 5.4 or 6.0. (IBM's version numbers seem even stranger than those used by Sage, which are themselves very strange.)


```
gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -o ex-serv-anon ex-serv-anon.o  -L
/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/lib/.libs ./.libs/libexamples.a ../../gl/.libs/libgnu.a -L/home/users/drkirkby/sage-4.6.alpha1/local/lib -L/opt/pware/lib 
-L../../lib/.libs -L../../libextra/.libs -lgnutls-extra -lopencdk -lgnutls -lz -lgcrypt -lgpg-error -lintl -liconv -lpthread -lc  -Wl,-blibpath:/home/users/drkirkby/sage-4.6.alpha1/spkg/buil
d/gnutls-2.2.1.p5/src/lib/.libs:/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/libextra/.libs:/home/users/drkirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib:/home/users/d
rkirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4/../../..:/usr/lib:/lib 
/bin/sh ../../libtool --tag=CC   --mode=link gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-po
inter-sign -no-install  -o ex-client-tlsia ex-client-tlsia.o libexamples.la ../../gl/libgnu.la ../../lib/libgnutls.la ../../libextra/libgnutls-extra.la 
/bin/sh ../../libtool --tag=CC   --mode=link gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-po
inter-sign -no-install  -o ex-serv-pgp ex-serv-pgp.o libexamples.la ../../gl/libgnu.la ../../lib/libgnutls.la ../../libextra/libgnutls-extra.la 
/bin/sh ../../libtool --tag=CC   --mode=link gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-po
inter-sign -no-install  -o ex-client-srp ex-client-srp.o libexamples.la ../../gl/libgnu.la ../../lib/libgnutls.la ../../libextra/libgnutls-extra.la 
/bin/sh ../../libtool --tag=CC   --mode=link gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-po
inter-sign -no-install  -o ex-serv-srp ex-serv-srp.o libexamples.la ../../gl/libgnu.la ../../lib/libgnutls.la ../../libextra/libgnutls-extra.la 
gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -o ex-serv-pgp ex-serv-pgp.o  -L/h
ome/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/lib/.libs ./.libs/libexamples.a ../../gl/.libs/libgnu.a -L/home/users/drkirkby/sage-4.6.alpha1/local/lib -L/opt/pware/lib -L
../../lib/.libs -L../../libextra/.libs -lgnutls-extra -lopencdk -lgnutls -lz -lgcrypt -lgpg-error -lintl -liconv -lpthread -lc  -Wl,-blibpath:/home/users/drkirkby/sage-4.6.alpha1/spkg/build/
gnutls-2.2.1.p5/src/lib/.libs:/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/libextra/.libs:/home/users/drkirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib:/home/users/drk
irkby/sage-4.6.alpha1/local/lib:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4/../../..:/usr/lib:/lib 
gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -o ex-client-tlsia ex-client-tlsia
.o  -L/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/lib/.libs ./.libs/libexamples.a ../../gl/.libs/libgnu.a -L/home/users/drkirkby/sage-4.6.alpha1/local/lib -L/opt/pwar
e/lib -L../../lib/.libs -L../../libextra/.libs -lgnutls-extra -lopencdk -lgnutls -lz -lgcrypt -lgpg-error -lintl -liconv -lpthread -lc  -Wl,-blibpath:/home/users/drkirkby/sage-4.6.alpha1/spk
g/build/gnutls-2.2.1.p5/src/lib/.libs:/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/libextra/.libs:/home/users/drkirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib:/home/u
sers/drkirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4/../../..:/usr/lib:/lib 
gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -o ex-serv-srp ex-serv-srp.o  -L/h
ome/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/lib/.libs ./.libs/libexamples.a ../../gl/.libs/libgnu.a -L/home/users/drkirkby/sage-4.6.alpha1/local/lib -L/opt/pware/lib -L
../../lib/.libs -L../../libextra/.libs -lgnutls-extra -lopencdk -lgnutls -lz -lgcrypt -lgpg-error -lintl -liconv -lpthread -lc  -Wl,-blibpath:/home/users/drkirkby/sage-4.6.alpha1/spkg/build/
gnutls-2.2.1.p5/src/lib/.libs:/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/libextra/.libs:/home/users/drkirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib:/home/users/drk
irkby/sage-4.6.alpha1/local/lib:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4/../../..:/usr/lib:/lib 
gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -o ex-client-srp ex-client-srp.o  
-L/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/lib/.libs ./.libs/libexamples.a ../../gl/.libs/libgnu.a -L/home/users/drkirkby/sage-4.6.alpha1/local/lib -L/opt/pware/li
b -L../../lib/.libs -L../../libextra/.libs -lgnutls-extra -lopencdk -lgnutls -lz -lgcrypt -lgpg-error -lintl -liconv -lpthread -lc  -Wl,-blibpath:/home/users/drkirkby/sage-4.6.alpha1/spkg/bu
ild/gnutls-2.2.1.p5/src/lib/.libs:/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/libextra/.libs:/home/users/drkirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib:/home/users
/drkirkby/sage-4.6.alpha1/local/lib:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4:/opt/pware/lib/gcc/powerpc-ibm-aix5.3.0.0/4.2.4/../../..:/usr/lib:/lib 
make[6]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/examples'
Making all in scripts
make[6]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/scripts'
make[6]: warning: -jN forced in submake: disabling jobserver mode.
make[6]: Nothing to be done for `all'.
make[6]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/scripts'
Making all in manpages
make[6]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/manpages'
make[6]: warning: -jN forced in submake: disabling jobserver mode.
make[6]: Nothing to be done for `all'.
make[6]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/manpages'
Making all in credentials
make[6]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials'
make[6]: warning: -jN forced in submake: disabling jobserver mode.
Making all in openpgp
make[7]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials/openpgp'
make[7]: warning: -jN forced in submake: disabling jobserver mode.
make[7]: Nothing to be done for `all'.
make[7]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials/openpgp'
Making all in srp
make[7]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials/srp'
make[7]: warning: -jN forced in submake: disabling jobserver mode.
make[7]: Nothing to be done for `all'.
make[7]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials/srp'
Making all in x509
make[7]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials/x509'
make[7]: warning: -jN forced in submake: disabling jobserver mode.
make[7]: Nothing to be done for `all'.
make[7]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials/x509'
make[7]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials'
make[7]: warning: -jN forced in submake: disabling jobserver mode.
make[7]: Nothing to be done for `all-am'.
make[7]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials'
make[6]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc/credentials'
make[6]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc'
make[6]: warning: -jN forced in submake: disabling jobserver mode.
make[6]: Nothing to be done for `all-am'.
make[6]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc'
make[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc'
make[4]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/doc'
Making all in tests
make[4]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests'
make[4]: warning: -jN forced in submake: disabling jobserver mode.
Making all in rsa-md5-collision
make[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/rsa-md5-collision'
make[5]: warning: -jN forced in submake: disabling jobserver mode.
make[5]: Nothing to be done for `all'.
make[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/rsa-md5-collision'
Making all in pkcs1-padding
make[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/pkcs1-padding'
make[5]: warning: -jN forced in submake: disabling jobserver mode.
make[5]: Nothing to be done for `all'.
make[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/pkcs1-padding'
Making all in pkcs8-decode
make[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/pkcs8-decode'
make[5]: warning: -jN forced in submake: disabling jobserver mode.
make[5]: Nothing to be done for `all'.
make[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/pkcs8-decode'
Making all in pkcs12-decode
make[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/pkcs12-decode'
make[5]: warning: -jN forced in submake: disabling jobserver mode.
make[5]: Nothing to be done for `all'.
make[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/pkcs12-decode'
Making all in userid
make[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/userid'
make[5]: warning: -jN forced in submake: disabling jobserver mode.
make[5]: Nothing to be done for `all'.
make[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/userid'
Making all in pathlen
make[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/pathlen'
make[5]: warning: -jN forced in submake: disabling jobserver mode.
make[5]: Nothing to be done for `all'.
make[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/pathlen'
Making all in key-id
make[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/key-id'
make[5]: warning: -jN forced in submake: disabling jobserver mode.
make[5]: Nothing to be done for `all'.
make[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/key-id'
Making all in sha2
make[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/sha2'
make[5]: warning: -jN forced in submake: disabling jobserver mode.
make[5]: Nothing to be done for `all'.
make[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/sha2'
Making all in hostname-check
make[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/hostname-check'
make[5]: warning: -jN forced in submake: disabling jobserver mode.
make[5]: Nothing to be done for `all'.
make[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/hostname-check'
Making all in openpgp
make[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/openpgp'
make[5]: warning: -jN forced in submake: disabling jobserver mode.
make[5]: Nothing to be done for `all'.
make[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests/openpgp'
make[5]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests'
make[5]: warning: -jN forced in submake: disabling jobserver mode.
/bin/sh ../libtool --tag=CC   --mode=compile gcc -std=gnu99 -DHAVE_CONFIG_H -I. -I..  -I../lgl -I../lgl -I../gl -I../gl -I../includes -I../includes -I../doc/examples -I/home/users/drkirkby/s
age-4.6.alpha1/local/include -I/opt/pware/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign
 -MT utils.lo -MD -MP -MF .deps/utils.Tpo -c -o utils.lo utils.c
mkdir .libs
 gcc -std=gnu99 -DHAVE_CONFIG_H -I. -I.. -I../lgl -I../lgl -I../gl -I../gl -I../includes -I../includes -I../doc/examples -I/home/users/drkirkby/sage-4.6.alpha1/local/include -I/opt/pware/inc
lude -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -MT utils.lo -MD -MP -MF .deps/utils.Tpo -c 
utils.c  -DPIC -o .libs/utils.o
mv -f .deps/utils.Tpo .deps/utils.Plo
/bin/sh ../libtool --tag=CC   --mode=link gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/users/drkirkby/sage-4.6.alpha1/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-point
er-sign -no-install  -o libutils.la  utils.lo  
ar cru .libs/libutils.a .libs/utils.o
ranlib .libs/libutils.a
creating libutils.la
(cd .libs && rm -f libutils.la && ln -s ../libutils.la libutils.la)
make[5]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests'
make[4]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/tests'
Making all in po
make[4]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/po'
make[4]: warning: -jN forced in submake: disabling jobserver mode.
make[4]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src/po'
make[4]: Entering directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src'
make[4]: warning: -jN forced in submake: disabling jobserver mode.
make[4]: Nothing to be done for `all-am'.
make[4]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/home/users/drkirkby/sage-4.6.alpha1/spkg/build/gnutls-2.2.1.p5/src'
failed to build GNUTLS

real    21m9.822s
user    14m6.587s
sys     3m56.694s
sage: An error occurred while installing gnutls-2.2.1.p5
```


Issue created by migration from https://trac.sagemath.org/ticket/9974





---

archive/issue_comments_100069.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2012-10-05T09:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9973#issuecomment-100069",
    "user": "jdemeyer"
}
```

Resolution: invalid



---

archive/issue_comments_100070.json:
```json
{
    "body": "GNUTLS is no longer part of Sage.",
    "created_at": "2012-10-05T09:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9973#issuecomment-100070",
    "user": "jdemeyer"
}
```

GNUTLS is no longer part of Sage.

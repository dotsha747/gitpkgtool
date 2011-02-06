#
# Makefile for gitpkgtool
#

world: build

build:
	# nothing to compile

distclean:
	# no temporary files generated

test:
	# nothing to test

# install files into $(DESTDIR)
install:
	install -D gitpkgtool $(DESTDIR)/usr/bin/gitpkgtool
	



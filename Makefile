# Name of the package
PACKAGE=fetch
BIN_DIR=/usr/local/bin/
MAN_DIR = /usr/local/share/man/man1/

all:

install: make-install-dirs
	install -m 755 $(PACKAGE).py $(DESTDIR)$(BIN_DIR)$(PACKAGE)
	install -m 644 $(PACKAGE).1 $(DESTDIR)$(MAN_DIR)

make-install-dirs:
	mkdir -p $(DESTDIR)$(BIN_DIR)
	mkdir -p $(DESTDIR)$(MAN_DIR)

uninstall:
	rm $(DESTDIR)$(BIN_DIR)$(PACKAGE)
	rm $(DESTDIR)$(MAN_DIR)$(PACKAGE).1

clean:
	rm -f *-stamp
	rm -rf debian/$(PACKAGE)
	rm -f debian/files
	find . -type f -iregex '.*~$$'  -print | xargs rm -rf
	find . -type f -iregex '.*\.pyc$$'  -print | xargs rm -rf
	find . -type f -iregex '.*\.bak$$'  -print | xargs rm -rf



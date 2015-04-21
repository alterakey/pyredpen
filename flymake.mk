redpendir=/path/to/redpen

check-syntax:
	for i in $(CHK_SOURCES); do python $(redpendir)/redpen.py --doc=$$i; done

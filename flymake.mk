redpendir=/path/to/redpen

check-syntax:
	(cd $(redpendir) && for i in $(CHK_SOURCES); do python redpen.py --doc=$$i; done)

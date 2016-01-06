
import.xml:
	rm -f $@
	cat header.xml > $@
	PGPASSWORD=kuq psql -qAt -h192.168.99.100 -U stefan -d stefan < authors.sql >> $@
	PGPASSWORD=kuq psql -qAt -h192.168.99.100 -U stefan -d stefan < posts.sql >> $@
	PGPASSWORD=kuq psql -qAt -h192.168.99.100 -U stefan -d stefan < attachments.sql >> $@
	cat footer.xml >> $@

photos.sh:
	rm -f $@
	PGPASSWORD=kuq psql -qAt -h192.168.99.100 -U stefan -d stefan < photos.sql > $@

.PHONY: import.xml photos.sh
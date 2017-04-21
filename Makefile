install:
	python setup.py install
	cp etc/wazo-admin-ui/conf.d/cdr.yml /etc/wazo-admin-ui/conf.d
	systemctl restart wazo-admin-ui

uninstall:
	pip uninstall wazo-admin-ui-cdr
	rm /etc/wazo-admin-ui/conf.d/cdr.yml
	systemctl restart wazo-admin-ui

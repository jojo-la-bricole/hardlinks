import logging
import os
import uuid

from os.path import join as opj

_logger = logging.getLogger(__name__)

db = os.environ['PGDATABASE']
build = os.environ.get('BUILD')

if not build:
    _logger.info("BUILD not deteted")
else:
    target = '/home/odoo/data/filestore/%s/ef' % db
    files = os.listdir(target)
    _logger.info("Got files: %s", files)
    for i, fname in enumerate(files):
        if i == 0:
            _logger.info("RENAME")
            os.rename(opj(target, fname), opj(target, fname) + '.renamed')
        elif i == 1:
            _logger.info("WRITING")
            with open(opj(target, fname), 'w') as f:
                f.write("written")
        else:
            _logger.info("UNKLINK")
            os.unlink(opj(target, fname))

    _logger.info("CREATE")
    with open(opj(target, 'new.%s' % uuid.uuid4()), 'w') as f:
        f.write('new')

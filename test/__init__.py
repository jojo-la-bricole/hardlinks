import os
import uuid

from os.path import join as opj

target = '/home/odoo/data/filestore/%s/ff' % os.environ['PGDATABASE']
for i, fname in os.listdir(target):
    if i == 0:
        os.rename(opj(target, fname), opj(target, fname) + '.renamed')
    else:
        os.unlink(opj(target, fname))

with open(opj(target, 'new.%s' % uuid.uuid4())) as f:
    f.write('new')

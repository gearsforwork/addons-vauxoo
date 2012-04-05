# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2011 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
############################################################################
#    Coded by: moylop260 (moylop260@vauxoo.com)
#    Coded by: isaac (isaac@vauxoo.com)
#    Financed by: http://www.sfsoluciones.com (aef@sfsoluciones.com)
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields, osv
import wizard
import netsvc
import pooler
import time
import base64
import StringIO
import csv
import tempfile
import os
import sys
import codecs
from tools.misc import ustr
try:
    from SOAPpy import WSDL
except:
    print "Package SOAPpy missed"
    pass
import time


class wizard_cancel_invoice_pac_sf(osv.osv_memory):
    _name='wizard.cancel.invoice.pac.sf'

    def _get_cancel_invoice_id(self, cr, uid, data, context = {}):
        res = {}
        invoice_obj = self.pool.get('account.invoice')
        res = invoice_obj._get_file_cancel(cr, uid, data['active_ids'])
        return res['file']

    def upload_cancel_to_pac(self, cr, uid, ids, context ={}):
        res = {}
        invoice_obj = self.pool.get('account.invoice')
        res = invoice_obj.sf_cancel(cr, uid, context['active_ids'], context=None)
        self.write(cr, uid, ids, {'message': res['message'] }, context=None)
        return True


    _columns = {
        'file': fields.binary('File', readonly=True),
        'message': fields.text('text', readonly=True),
    }

    _defaults= {
        'message': 'Seleccione el botón Cancelar Factura enviar la cancelacion al PAC',
        'file': _get_cancel_invoice_id,
    }
wizard_cancel_invoice_pac_sf()


from openerp.tests.common import TransactionCase
from openerp.exceptions import AccessError
from openerp.osv.orm import except_orm
from openerp import SUPERUSER_ID

class TestAnalytic(TransactionCase):

    def setUp(self):
        super(TestAnalytic, self).setUp()
        self.analytic = self.registry('account.analytic.account')
        self.message = self.registry('mail.message')
        self.user = self.registry('res.users')


    def test_log_terms_conditions(self):
        '''
        Check if the log about terms and conditions field was created
        '''
        cr, uid = self.cr, self.uid
        user_brw = self.user.browse(cr, uid, uid)
        partner_brw = user_brw.partner_id
        analytic_id = self.analytic.create(cr, uid, {
            'name': 'Test Terms and Conditions Log',
            'code': 'TERMANDCONDITIONS',
            'description': 'Firs Condition',
            })
        message_ids = self.message.search(cr, uid,
                                 [('res_id', '=', analytic_id),
                                  ('model', '=', 'account.analytic.account'),
                                  ('body', 'ilike', '%'+'Firs Condition'+'%')])

        self.assertGreaterEqual(len(message_ids),
                                1,
                                "The log was not created")
        self.analytic.write(cr, uid, [analytic_id], {
            'description': 'Term Changed'
            })

        message_ids = self.message.search(cr, uid,
                                 [('res_id', '=', analytic_id),
                                  ('model', '=', 'account.analytic.account'),
                                  ('body', 'ilike', '%'+'Term Changed'+'%')])

        self.assertGreaterEqual(len(message_ids),
                                1,
                                "The log was not created")

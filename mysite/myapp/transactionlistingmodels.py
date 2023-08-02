from django.db import models
from myapp.transactionlistingmodels import *
class TransactionListingCDB(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(default=0)
    payee = models.CharField(max_length=150, default=' ')
    cv_no = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    date_trans = models.DateField(default='0000-00-00')
    id_code = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    sl_acct = models.CharField(max_length=150, default=' ')
    guarantor_id = models.PositiveIntegerField(default=0)
    guarantor = models.CharField(max_length=150, default=' ')
    primary_code = models.PositiveIntegerField(default=0)
    secondary_code = models.PositiveIntegerField(default=0)
    acct_code = models.PositiveIntegerField(default=0)
    subsidiary_code = models.PositiveIntegerField(default=0)
    acct_title = models.CharField(max_length=150, default=' ')
    debit_amount = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    credit_amount = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    active = models.CharField(max_length=2, default='')
    posted_by = models.CharField(max_length=100, default=' ')
    date_posted = models.DateField(default='0000-00-00')
    sl_type = models.CharField(max_length=1, default='')
    check_no = models.CharField(max_length=50, default='0')
    sys_type = models.CharField(max_length=4, default='')
    doc_type = models.CharField(max_length=10, default='CV')
    payment_status = models.CharField(max_length=10, default='')
    transtype_status = models.CharField(max_length=20, default='')
    cleared_amount = models.DecimalField(max_digits=21, decimal_places=3, default='0.000')
    cleared_date = models.CharField(max_length=25, default='0000-00-00 00:00:00')
    expiry_date = models.CharField(max_length=25, default='0000-00-00 00:00:00')
    status_stale = models.CharField(max_length=1, default='N')
    check_status = models.CharField(max_length=1, default='0')

    class Meta:
        db_table = 'tbl_transaction_listing_cdb'
        indexes = [
            models.Index(fields=['cv_no', 'id_code', 'sl_acct', 'ul_code', 'primary_code', 'secondary_code',
                                 'acct_code', 'subsidiary_code', 'acct_title', 'debit_amount', 'credit_amount',
                                 'date_trans', 'sl_type'], name='psasadcds'),
            models.Index(fields=['id_code', 'cv_no', 'active', 'date_trans', 'primary_code', 'secondary_code',
                                 'acct_code', 'subsidiary_code', 'acct_title'], name='icadpsasa'),
            models.Index(fields=['cv_no'], name='doc_no'),
            models.Index(fields=['date_trans'], name='date_trans'),
            models.Index(fields=['id_code'], name='id_code'),
            models.Index(fields=['sl_acct'], name='sl_acct'),
            models.Index(fields=['guarantor_id'], name='guarantor_id'),
            models.Index(fields=['guarantor'], name='guarantor'),
            models.Index(fields=['primary_code'], name='primary_code'),
            models.Index(fields=['secondary_code'], name='secondary_code'),
            models.Index(fields=['acct_code'], name='acct_code'),
            models.Index(fields=['subsidiary_code'], name='subsidiary_code'),
            models.Index(fields=['acct_title'], name='acct_title'),
            models.Index(fields=['debit_amount'], name='debit_amount'),
            models.Index(fields=['credit_amount'], name='credit_amount'),
            models.Index(fields=['active'], name='active'),
            models.Index(fields=['sl_type'], name='sl_type'),
        ]
        
        
# class TransactionListingAPV(models.Model):
#     autonum = models.BigAutoField(primary_key=True)
#     ul_code = models.SmallIntegerField(default=0)
#     supplier = models.CharField(max_length=150, default=' ')
#     apv_no = models.DecimalField(max_digits=12, decimal_places=0, default=0)
#     date_trans = models.DateField(default='0000-00-00')
#     id_code = models.DecimalField(max_digits=15, decimal_places=0, default=0)
#     sl_acct = models.CharField(max_length=150, default=' ')
#     primary_code = models.SmallIntegerField(default=0)
#     secondary_code = models.SmallIntegerField(default=0)
#     acct_code = models.SmallIntegerField(default=0)
#     subsidiary_code = models.SmallIntegerField(default=0)
#     acct_title = models.CharField(max_length=150, default=' ')
#     debit_amount = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
#     credit_amount = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
#     terms_payment = models.SmallIntegerField(default=0)
#     due_date = models.DateField(default='0000-00-00')
#     active = models.CharField(max_length=2, default='')
#     posted_by = models.CharField(max_length=100, default=' ')
#     date_posted = models.DateField(default='0000-00-00')
#     sl_type = models.CharField(max_length=1, default='')
#     sys_type = models.CharField(max_length=4, default='')
#     doc_type = models.CharField(max_length=10, default='APV')
#     payment_status = models.CharField(max_length=10, default='')
#     transtype_status = models.CharField(max_length=20, default='')

#     class Meta:
#         db_table = 'tbl_transaction_listing_apv'

#     # Define indexes if needed
#     # For example:
#     class Meta:
#         indexes = [
#             models.Index(fields=['apv_no', 'id_code', 'sl_acct', 'primary_code', 'secondary_code', 'acct_code', 'subsidiary_code', 'acct_title', 'date_trans']),
#             models.Index(fields=['id_code', 'apv_no', 'active', 'date_trans', 'primary_code', 'secondary_code', 'acct_code', 'subsidiary_code', 'acct_title']),
#             models.Index(fields=['apv_no']),
#             models.Index(fields=['date_trans']),
#             models.Index(fields=['id_code']),
#             models.Index(fields=['sl_acct']),
#             models.Index(fields=['primary_code']),
#             models.Index(fields=['secondary_code']),
#             models.Index(fields=['acct_code']),
#             models.Index(fields=['subsidiary_code']),
#             models.Index(fields=['acct_title']),
#             models.Index(fields=['debit_amount']),
#             models.Index(fields=['credit_amount']),
#             models.Index(fields=['active']),
#             models.Index(fields=['sl_type']),
#         ]
    

class TransactionListingAPV(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(default=0)
    supplier = models.CharField(max_length=150, default=' ')
    apv_no = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    date_trans = models.DateField(default='2001-01-01')
    id_code = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    sl_acct = models.CharField(max_length=150, default=' ')
    primary_code = models.PositiveSmallIntegerField(default=0)
    secondary_code = models.PositiveSmallIntegerField(default=0)
    acct_code = models.PositiveSmallIntegerField(default=0)
    subsidiary_code = models.PositiveSmallIntegerField(default=0)
    acct_title = models.CharField(max_length=150, default=' ')
    debit_amount = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    credit_amount = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    terms_payment = models.PositiveSmallIntegerField(default=0)
    due_date = models.DateField(default='2001-01-01')
    active = models.CharField(max_length=2, default='')
    posted_by = models.CharField(max_length=100, default=' ')
    date_posted = models.DateField(default='2001-01-01')
    sl_type = models.CharField(max_length=1, default='')
    sys_type = models.CharField(max_length=4, default='')
    doc_type = models.CharField(max_length=10, default='APV')
    payment_status = models.CharField(max_length=10, default='')
    transtype_status = models.CharField(max_length=20, default='')

    class Meta:
        # Define the database table name explicitly if needed
        db_table = 'tbl_transaction_listing_apv'

    def __str__(self):
        return f"{self.apv_no} - {self.acct_title}"
class TransactionListingAR(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.SmallIntegerField(default=0)
    customer = models.CharField(max_length=150, default=' ')
    ci_no = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    date_trans = models.DateField(default='0000-00-00')
    id_code = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    sl_acct = models.CharField(max_length=150, default=' ')
    guarantor_id = models.PositiveIntegerField(default=0)
    guarantor = models.CharField(max_length=150, default=' ')
    primary_code = models.PositiveIntegerField(default=0)
    secondary_code = models.PositiveIntegerField(default=0)
    acct_code = models.PositiveIntegerField(default=0)
    subsidiary_code = models.PositiveIntegerField(default=0)
    acct_title = models.CharField(max_length=150, default=' ')
    debit_amount = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    credit_amount = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    terms_payment = models.SmallIntegerField(default=0)
    due_date = models.DateField(default='0000-00-00')
    active = models.CharField(max_length=2, default='')
    posted_by = models.CharField(max_length=100, default=' ')
    date_posted = models.DateField(default='0000-00-00')
    sl_type = models.CharField(max_length=1, default='')
    sys_type = models.CharField(max_length=4, default='')
    terminal_no = models.CharField(max_length=21, default='0')
    doc_type = models.CharField(max_length=10, default='CI')
    payment_status = models.CharField(max_length=10, default='')
    transtype_status = models.CharField(max_length=20, default='')

    class Meta:
        db_table = 'tbl_transaction_listing_ar'

    # Define indexes if needed
    # For example:
    class Meta:
        indexes = [
            models.Index(fields=['ul_code', 'customer', 'ci_no', 'date_trans', 'id_code', 'sl_acct', 'guarantor', 'primary_code', 'secondary_code', 'acct_code', 'subsidiary_code', 'acct_title', 'debit_amount', 'credit_amount']),
            models.Index(fields=['id_code', 'ci_no', 'active', 'date_trans', 'primary_code', 'secondary_code', 'acct_code', 'subsidiary_code', 'acct_title']),
            models.Index(fields=['ci_no']),
            models.Index(fields=['date_trans']),
            models.Index(fields=['id_code']),
            models.Index(fields=['sl_acct']),
            models.Index(fields=['guarantor_id']),
            models.Index(fields=['guarantor']),
            models.Index(fields=['primary_code']),
            models.Index(fields=['secondary_code']),
            models.Index(fields=['acct_code']),
            models.Index(fields=['subsidiary_code']),
            models.Index(fields=['acct_title']),
            models.Index(fields=['debit_amount']),
            models.Index(fields=['credit_amount']),
            models.Index(fields=['active']),
            models.Index(fields=['sl_type']),
        ]



class TransactionListingCRB(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.SmallIntegerField(default=0)
    payor = models.CharField(max_length=150, default=' ')
    ref_or_no = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    date_trans = models.DateField(default='0000-00-00')
    id_code = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    sl_acct = models.CharField(max_length=150, default=' ')
    guarantor_id = models.PositiveIntegerField(default=0)
    guarantor = models.CharField(max_length=150, default=' ')
    primary_code = models.PositiveIntegerField(default=0)
    secondary_code = models.PositiveIntegerField(default=0)
    acct_code = models.PositiveIntegerField(default=0)
    subsidiary_code = models.PositiveIntegerField(default=0)
    acct_title = models.CharField(max_length=150, default=' ')
    debit_amount = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    credit_amount = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    terms_payment = models.SmallIntegerField(default=0)
    due_date = models.DateField(default='0000-00-00')
    active = models.CharField(max_length=2, default='')
    posted_by = models.CharField(max_length=100, default=' ')
    date_posted = models.DateField(default='0000-00-00')
    trans_type = models.CharField(max_length=2, default='')
    sl_type = models.CharField(max_length=1, default='')
    sys_type = models.CharField(max_length=4, default='')
    doc_type = models.CharField(max_length=10, default='OR')
    payment_status = models.CharField(max_length=10, default='')
    transtype_status = models.CharField(max_length=20, default='')
    terminal_no = models.CharField(max_length=21, default='0')
    collected_amount = models.DecimalField(max_digits=21, decimal_places=3, default='0.000')

    class Meta:
        db_table = 'tbl_transaction_listing_crb'

    # Define indexes if needed
    # For example:
    class Meta:
        indexes = [
            models.Index(fields=['ref_or_no', 'id_code', 'sl_acct', 'ul_code', 'primary_code', 'secondary_code', 'acct_code', 'subsidiary_code', 'acct_title', 'debit_amount', 'credit_amount', 'autonum']),
            models.Index(fields=['id_code', 'ref_or_no', 'active', 'date_trans', 'primary_code', 'secondary_code', 'acct_code', 'subsidiary_code', 'acct_title']),
            models.Index(fields=['ref_or_no']),
            models.Index(fields=['date_trans']),
            models.Index(fields=['id_code']),
            models.Index(fields=['sl_acct']),
            models.Index(fields=['guarantor_id']),
            models.Index(fields=['guarantor']),
            models.Index(fields=['primary_code']),
            models.Index(fields=['secondary_code']),
            models.Index(fields=['acct_code']),
            models.Index(fields=['subsidiary_code']),
            models.Index(fields=['acct_title']),
            models.Index(fields=['debit_amount']),
            models.Index(fields=['credit_amount']),
            models.Index(fields=['active']),
            models.Index(fields=['sl_type']),
        ]

class TransactionListingGeneralJournal(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.SmallIntegerField(default=0)
    jv_no = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    date_trans = models.DateField(default='0000-00-00')
    id_code = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    sl_acct = models.CharField(max_length=150, default=' ')
    guarantor_id = models.PositiveIntegerField(default=0)
    guarantor = models.CharField(max_length=150, default=' ')
    primary_code = models.PositiveIntegerField(default=0)
    secondary_code = models.PositiveIntegerField(default=0)
    acct_code = models.PositiveIntegerField(default=0)
    subsidiary_code = models.PositiveIntegerField(default=0)
    acct_title = models.CharField(max_length=150, default=' ')
    debit_amount = models.DecimalField(max_digits=21, decimal_places=3, default='0.000')
    credit_amount = models.DecimalField(max_digits=21, decimal_places=3, default='0.000')
    active = models.CharField(max_length=2, default='')
    posted_by = models.CharField(max_length=100, default=' ')
    date_posted = models.DateField(default='0000-00-00')
    sl_type = models.CharField(max_length=1, default='')
    sys_type = models.CharField(max_length=4, default='')
    doc_type = models.CharField(max_length=10, default='JV')
    payment_status = models.CharField(max_length=10, default='')
    transtype_status = models.CharField(max_length=20, default='')

    class Meta:
        db_table = 'tbl_transaction_listing_gj'

    # Define indexes if needed
    # For example:
    # class Meta:
    #     indexes = [
    #         models.Index(fields=['jv_no', 'id_code', 'sl_acct', 'primary_code', 'secondary_code', 'acct_code', 'subsidiary_code', 'acct_title', 'debit_amount', 'credit_amount', 'date_trans', 'sl_type']),
    #         models.Index(fields=['id_code', 'jv_no', 'active', 'date_trans', 'primary_code', 'secondary_code', 'acct_code', 'subsidiary_code', 'acct_title']),
    #         models.Index(fields=['jv_no']),
    #         models.Index(fields=['date_trans']),
    #         models.Index(fields=['id_code']),
    #         models.Index(fields=['sl_acct']),
    #         models.Index(fields=['guarantor_id']),
    #         models.Index(fields=['guarantor']),
    #         models.Index(fields=['primary_code']),
    #         models.Index(fields=['secondary_code']),
    #         models.Index(fields=['acct_code']),
    #         models.Index(fields=['subsidiary_code']),
    #         models.Index(fields=['acct_title']),
    #         models.Index(fields=['debit_amount']),
    #         models.Index(fields=['credit_amount']),
    #         models.Index(fields=['active']),
    #         models.Index(fields=['sl_type']),
    #     ]


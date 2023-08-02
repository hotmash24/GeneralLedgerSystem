from django.db import models
from myapp.disbursementmodels import *

# Create your models here.
class CvList(models.Model):
    autonum = models.BigIntegerField(primary_key=True)
    ul_code = models.SmallIntegerField(default=0)
    cv_no = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    date_trans = models.DateField(default='0000-00-00')
    due_date = models.DateField(default='0000-00-00')
    id_code = models.PositiveIntegerField(default=0)
    payee = models.CharField(max_length=150, default=' ')
    check_amt = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    drawee_bank = models.CharField(max_length=150, default=' ')
    date_check = models.DateField(default='0000-00-00')
    check_no = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    check_type = models.CharField(max_length=1, default='')
    remarks = models.CharField(max_length=999, default=' ')
    TransType = models.CharField(max_length=100, default=' ')
    active = models.CharField(max_length=2, default='')
    prepared_by = models.CharField(max_length=60, default=' ')
    reviewed_by = models.CharField(max_length=60, default=' ')
    reviewed_date = models.CharField(max_length=25, default='')
    approved_by = models.CharField(max_length=60, default=' ')
    approved_date = models.CharField(max_length=25, default='')
    cancel_by = models.CharField(max_length=60, default='')
    cancel_date = models.CharField(max_length=25, default='')
    sys_type = models.CharField(max_length=4, default='')
    doc_type = models.CharField(max_length=10, default='CV')
    terminal_no = models.CharField(max_length=21, default='0')
    tmp_payee = models.CharField(max_length=150, default='')
    ref_no = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    ref_type = models.CharField(max_length=10, default='0')

    class Meta:
        db_table = 'tbl_cv_list'
        permissions = [
            ("can_save_object", "Can Save Object"),
            # Add other custom permissions for this model if needed
        ]
class CFType(models.Model):
    line_number = models.IntegerField(default=0)
    header = models.CharField(max_length=1, default='')
    module_type = models.CharField(max_length=3, default='')
    cf_key = models.CharField(max_length=10, default='')
    cf_desc = models.CharField(max_length=100, default=' ')
    wtax = models.CharField(max_length=1, default='')
    status = models.CharField(max_length=1, default='Y')

    class Meta:
        db_table = 'tbl_cf_type'

class Payee(models.Model):
    id_code = models.IntegerField(default=0)
    payee_name = models.CharField(max_length=60, default=' ')
    address = models.CharField(max_length=150, default=' ')
    contact_no = models.CharField(max_length=20, default=' ')
    ul_code = models.IntegerField(default=0)
    active = models.CharField(max_length=1, default='Y')

    class Meta:
        db_table = 'tbl_payee'

class BankDrawee(models.Model):
    id_code = models.CharField(max_length=10, default='0')
    bank_description = models.CharField(max_length=150, default=' ')
    bank_abbreviation = models.CharField(max_length=150, default=' ')
    acct_title = models.CharField(max_length=150, default='')
    sl_code = models.IntegerField(default=0)
    sl_account = models.CharField(max_length=150, default='')
    status = models.CharField(max_length=1, default='Y')
    
    def __str__(self):
        return self.bank_description
    
    class Meta:
        db_table = 'tbl_bank_drawee'


class InvRefNo(models.Model):
    description = models.CharField(max_length=25, default=' ')
    next_no = models.DecimalField(max_digits=12, decimal_places=0, default=0)

    def __str__(self):
        return self.description
    
    class Meta:
        db_table = 'tbl_inv_ref_no'
    

class NumberGenerator(models.Model):
    description = models.CharField(max_length=25, default=' ')
    next_no = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    ul_code = models.PositiveSmallIntegerField(default=0)
    doc_type = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'tbl_number_generator'
        ordering = ['description']


class AcctList(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    code = models.CharField(max_length=15, default='')
    acct_title = models.CharField(max_length=100)
    primary_code = models.PositiveSmallIntegerField(default=0)
    secondary_code = models.PositiveSmallIntegerField(default=0)
    acct_code = models.PositiveSmallIntegerField(default=0)
    subsidiary_code = models.PositiveSmallIntegerField(default=0)
    under = models.CharField(max_length=150, default=' ')
    status = models.CharField(max_length=1, default='Y')
    def __str__(self):
        return self.acct_title
    class Meta:
        # Define the table name (optional)
        db_table = 'tbl_acct_list'
        # Define the unique constraint (optional)
        unique_together = ['code', 'acct_title']


class Setup(models.Model):
    autonum = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=150, default=' ')
    acct_title = models.TextField()
    sl_acct = models.CharField(max_length=100, default=' ')
    sl_id = models.IntegerField(default=0)
    sl_type = models.CharField(max_length=1, default='')
    acct_title2 = models.CharField(max_length=150, default=' ')
    module = models.CharField(max_length=100, default='')

    class Meta:
        db_table = 'tbl_setup'



class AcctSubsidiary(models.Model):
    autonum = models.AutoField(primary_key=True)
    primary_code = models.PositiveSmallIntegerField()
    secondary_code = models.PositiveSmallIntegerField()
    acct_code = models.PositiveSmallIntegerField()
    subsidiary_code = models.PositiveSmallIntegerField()
    subsidiary_acct_title = models.CharField(max_length=100)
    subsidiary_acct_desc = models.CharField(max_length=1000, blank=True, null=True)
    sl = models.CharField(db_column='SL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    calculation = models.PositiveSmallIntegerField()
    alter_code = models.CharField(max_length=50, blank=True, null=True)
    alter_name = models.CharField(max_length=100, blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_acct_subsidiary'
        unique_together = (('autonum', 'primary_code', 'secondary_code', 'acct_code', 'subsidiary_code', 'subsidiary_acct_title'),)
        
class CVTransType(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    cv_no = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    trans_type = models.CharField(max_length=100, default=' ')
    apv_no = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    date_trans = models.DateField(default='0000-00-00')
    amount_due = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    gross_amount = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    source_module_ap = models.CharField(max_length=3, default='')
    scheme_type = models.CharField(max_length=10, default='')
    sec_ref = models.CharField(max_length=10, default='')
    acct_title = models.CharField(max_length=150, default=' ')
    sys_type = models.CharField(max_length=4, default='')
    doc_type = models.CharField(max_length=10, default='CV')
    acct_code = models.CharField(max_length=11, default='')
    supplier_code = models.CharField(max_length=11, default='')
    sl_code = models.IntegerField(default=0)
    sl_name = models.CharField(max_length=100, default='')
    sl_type = models.CharField(max_length=1, default=None, null=True)
    ul_code_pmt = models.IntegerField(default=0)
    date_trans_pmt = models.DateField(default='0000-00-00')
    source_module_pmt = models.CharField(max_length=3, default='')

    class Meta:
        db_table = 'tbl_cv_transtype'
        
        
class APVPayScheme(models.Model):
    apv_no = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    installment_scheme = models.CharField(max_length=20, default=' ')
    no_installment = models.IntegerField(default=0)
    total_amount = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    due_date = models.DateField(default='0000-00-00')
    amortization = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    amount_paid = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    sys_type = models.CharField(max_length=4, default='')
    doc_type = models.CharField(max_length=10, default='APV')

    class Meta:
        db_table = 'tbl_apv_payscheme'
        unique_together = (('apv_no', 'installment_scheme', 'due_date'),)
        
class PropertyEquip(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.PositiveIntegerField(default=0)
    serial_no = models.CharField(max_length=50, default=' ')
    department = models.CharField(max_length=60, default=' ')
    personal_acctable = models.CharField(max_length=40, default=' ')
    prop_tag = models.CharField(max_length=40, default=' ')
    description = models.CharField(max_length=150, default=' ')
    category = models.CharField(max_length=150, default=' ')
    date_purch = models.DateField(default='1960-01-01')
    date_depr = models.DateField(null=True, default=None)
    cost_item = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    equip_condition = models.CharField(max_length=30, default=' ')
    responsibility_name = models.CharField(max_length=150, default='')
    service_life = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    salvage_value = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    fair_value = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    supplier = models.CharField(max_length=40, default='0')
    doc_ref_no = models.CharField(max_length=10, default='0')
    dismantling_cost = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    annual_dep = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    net_book_value = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    remarks = models.CharField(max_length=100, default=' ')
    beginning = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    provision = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    accu_dep = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    equip_image = models.BinaryField(null=True, default=None)
    image_yn = models.CharField(max_length=1, default='')
    ul_code = models.IntegerField(default=0)
    active = models.CharField(max_length=1, default='Y')
    profiling = models.CharField(max_length=1, default='N')

    class Meta:
        db_table = 'tbl_property_equip'
        unique_together = (('id_code', 'serial_no', 'department', 'personal_acctable', 'description', 'category', 'doc_ref_no'),)
        
class CVPPE(models.Model):
    cv_no = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    id_code = models.IntegerField(default=0)
    description = models.CharField(max_length=100, default=' ')
    category = models.CharField(max_length=150, default=' ')
    qty = models.PositiveIntegerField(default=0)
    date_acquired = models.DateField(default='0000-00-00')
    cost = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    service_life = models.PositiveIntegerField(default=0)
    code1 = models.IntegerField(default=0)
    code2 = models.IntegerField(default=0)
    code3 = models.IntegerField(default=0)
    code4 = models.IntegerField(default=0)
    sys_type = models.CharField(max_length=4, default='')
    doc_type = models.CharField(max_length=10, default='CV')

    class Meta:
        db_table = 'tbl_cv_ppe'
        unique_together = (('cv_no', 'id_code', 'description', 'category'),)
        
class CVParticular(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    cv_no = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    description = models.CharField(max_length=500, default=' ')
    amount = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    amount2 = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    sys_type = models.CharField(max_length=4, default='')
    doc_type = models.CharField(max_length=10, default='CV')

    class Meta:
        db_table = 'tbl_cv_particular'
        indexes = [
            models.Index(fields=['cv_no', 'description', 'amount', 'doc_type'], name='cdad'),
        ]
        
class CVPayScheme(models.Model):
    cv_no = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    installment_scheme = models.CharField(max_length=20, default=' ')
    no_installment = models.IntegerField(default=0)
    total_amount = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    sec_ref = models.CharField(max_length=100, default=' ')
    due_date = models.DateField(default='0000-00-00')
    amortization = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    amount_paid = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
    sys_type = models.CharField(max_length=4, default='')
    doc_type = models.CharField(max_length=10, default='CV')
    payment_status = models.CharField(max_length=10, default='')
    sl_code = models.IntegerField(default=0)
    sl_name = models.CharField(max_length=150, default=' ')

    class Meta:
        db_table = 'tbl_cv_payscheme'
        unique_together = (('cv_no', 'installment_scheme', 'due_date'),)
        
# class BackupListingCDB(models.Model):
#     autonum = models.BigAutoField(primary_key=True)
#     ul_code = models.SmallIntegerField(default=0, unsigned=True)
#     payee = models.CharField(max_length=150, default=' ')
#     cv_no = models.DecimalField(max_digits=12, decimal_places=0, default=0, unsigned=True)
#     date_trans = models.DateField(default='0000-00-00')
#     id_code = models.PositiveIntegerField(default=0, unsigned=True)
#     sl_acct = models.CharField(max_length=150, default=' ')
#     primary_code = models.PositiveIntegerField(default=0, unsigned=True)
#     secondary_code = models.PositiveIntegerField(default=0, unsigned=True)
#     acct_code = models.PositiveIntegerField(default=0, unsigned=True)
#     subsidiary_code = models.PositiveIntegerField(default=0, unsigned=True)
#     acct_title = models.CharField(max_length=150, default=' ')
#     debit_amount = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
#     credit_amount = models.DecimalField(max_digits=15, decimal_places=3, default='0.000')
#     active = models.CharField(max_length=2, default='')
#     sl_type = models.CharField(max_length=1, default='')
#     sys_type = models.CharField(max_length=4, default='')
#     doc_type = models.CharField(max_length=10, default='CV')

#     class Meta:
#         db_table = 'tbl_backup_listing_cdb'
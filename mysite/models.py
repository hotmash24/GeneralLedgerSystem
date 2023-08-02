# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Tbl13Thmonthpay(models.Model):
    auto_num = models.AutoField(db_column='Auto_num', primary_key=True)  # Field name made lowercase.
    company_code = models.IntegerField(db_column='Company_code', blank=True, null=True)  # Field name made lowercase.
    store_code = models.IntegerField(blank=True, null=True)
    emp_id = models.FloatField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(max_length=100, blank=True, null=True)
    year_release = models.FloatField(blank=True, null=True)
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    january = models.FloatField(db_column='January', blank=True, null=True)  # Field name made lowercase.
    february = models.FloatField(db_column='February', blank=True, null=True)  # Field name made lowercase.
    march = models.FloatField(db_column='March', blank=True, null=True)  # Field name made lowercase.
    april = models.FloatField(db_column='April', blank=True, null=True)  # Field name made lowercase.
    may = models.FloatField(db_column='May', blank=True, null=True)  # Field name made lowercase.
    june = models.FloatField(db_column='June', blank=True, null=True)  # Field name made lowercase.
    july = models.FloatField(db_column='July', blank=True, null=True)  # Field name made lowercase.
    august = models.FloatField(db_column='August', blank=True, null=True)  # Field name made lowercase.
    september = models.FloatField(db_column='September', blank=True, null=True)  # Field name made lowercase.
    october = models.FloatField(db_column='October', blank=True, null=True)  # Field name made lowercase.
    november = models.FloatField(db_column='November', blank=True, null=True)  # Field name made lowercase.
    december = models.FloatField(db_column='December', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_13thmonthpay'


class Tbl5Columnsded(models.Model):
    auto_num = models.AutoField(db_column='Auto_num', primary_key=True)  # Field name made lowercase.
    first_ded = models.CharField(db_column='First_Ded', max_length=100, blank=True, null=True)  # Field name made lowercase.
    second_ded = models.CharField(db_column='Second_ded', max_length=100, blank=True, null=True)  # Field name made lowercase.
    third_ded = models.CharField(db_column='Third_ded', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fourth_ded = models.CharField(db_column='Fourth_ded', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fifth_ded = models.CharField(db_column='Fifth_ded', max_length=100, blank=True, null=True)  # Field name made lowercase.
    other_deductions = models.TextField(db_column='Other_deductions', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_5columnsded'


class TblAccountTagging(models.Model):
    auto_num = models.AutoField(db_column='Auto_num', primary_key=True)  # Field name made lowercase.
    default_category = models.CharField(db_column='Default_Category', max_length=100, blank=True, null=True)  # Field name made lowercase.
    particular = models.CharField(db_column='Particular', max_length=100, blank=True, null=True)  # Field name made lowercase.
    account_title = models.CharField(db_column='Account_title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sl_type = models.CharField(db_column='SL_type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sl_name = models.CharField(db_column='SL_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    interface_no = models.IntegerField(db_column='Interface_no', blank=True, null=True)  # Field name made lowercase.
    account_code = models.CharField(max_length=30, blank=True, null=True)
    id_code = models.FloatField(blank=True, null=True)
    basic_category = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_account_tagging'


class TblAcctList(models.Model):
    code = models.CharField(max_length=15)
    acct_title = models.CharField(max_length=100)
    primary_code = models.PositiveSmallIntegerField(blank=True, null=True)
    secondary_code = models.PositiveSmallIntegerField(blank=True, null=True)
    acct_code = models.PositiveSmallIntegerField(blank=True, null=True)
    subsidiary_code = models.PositiveSmallIntegerField(blank=True, null=True)
    under = models.CharField(max_length=150)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_acct_list'


class TblAcctPrimary(models.Model):
    autonum = models.AutoField(primary_key=True)
    primary_code = models.PositiveSmallIntegerField()
    primary_acct_title = models.CharField(max_length=100)
    primary_acct_desc = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_acct_primary'
        unique_together = (('primary_code', 'primary_acct_title'),)


class TblAcctSecondary(models.Model):
    autonum = models.AutoField(primary_key=True)
    primary_code = models.PositiveSmallIntegerField()
    secondary_code = models.PositiveSmallIntegerField()
    secondary_acct_title = models.CharField(max_length=100)
    secondary_acct_desc = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_acct_secondary'
        unique_together = (('primary_code', 'secondary_code', 'secondary_acct_title'),)


class TblAcctSubsidiary(models.Model):
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


class TblAcctTitle(models.Model):
    autonum = models.AutoField(primary_key=True)
    primary_code = models.PositiveSmallIntegerField(blank=True, null=True)
    secondary_code = models.PositiveSmallIntegerField()
    acct_code = models.PositiveSmallIntegerField()
    acct_title = models.CharField(max_length=100)
    acct_desc = models.CharField(max_length=1000, blank=True, null=True)
    calculation = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_acct_title'
        unique_together = (('primary_code', 'secondary_code', 'acct_code', 'acct_title'),)


class TblAccttagging(models.Model):
    autonum = models.AutoField(db_column='AutoNUm', primary_key=True)  # Field name made lowercase.
    event_name = models.CharField(db_column='Event_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    acct_title = models.CharField(db_column='Acct_title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    departmet = models.TextField(db_column='Departmet', blank=True, null=True)  # Field name made lowercase.
    designation = models.TextField(db_column='Designation', blank=True, null=True)  # Field name made lowercase.
    sl_acctname = models.CharField(db_column='SL_acctName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_accttagging'


class TblAdjJournal(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    jv_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=999, blank=True, null=True)
    active = models.CharField(max_length=2, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    terminal_no = models.CharField(max_length=21, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_adj_journal'


class TblAffiliate(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.PositiveSmallIntegerField(blank=True, null=True)
    acct_title = models.CharField(max_length=100, blank=True, null=True)
    acronym = models.CharField(max_length=25, blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    date_as_of = models.DateField(blank=True, null=True)
    calculation = models.PositiveSmallIntegerField()
    ul_code = models.IntegerField(blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    sl_category = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_affiliate'
        unique_together = (('id_code', 'acct_title'),)


class TblAllowancelist(models.Model):
    auto_no = models.AutoField(primary_key=True)
    company_code = models.IntegerField(db_column='Company_code', blank=True, null=True)  # Field name made lowercase.
    store_code = models.IntegerField(blank=True, null=True)
    allow_code = models.FloatField(db_column='Allow_code', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    payout_period = models.CharField(db_column='Payout_period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    empye_share = models.FloatField(db_column='Empye_share', blank=True, null=True)  # Field name made lowercase.
    empr_share = models.FloatField(db_column='Empr_share', blank=True, null=True)  # Field name made lowercase.
    allow_name = models.CharField(db_column='Allow_name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    taxable = models.CharField(db_column='Taxable', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bir_tag = models.CharField(max_length=31, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_allowancelist'


class TblAllowemplist(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', primary_key=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    default_amnt = models.FloatField(db_column='Default_amnt', blank=True, null=True)  # Field name made lowercase.
    hourly_rate = models.CharField(max_length=30, blank=True, null=True)
    allow_code = models.CharField(db_column='Allow_Code', max_length=20, blank=True, null=True)  # Field name made lowercase.
    default_amnt2 = models.FloatField(db_column='Default_amnt2', blank=True, null=True)  # Field name made lowercase.
    effective_from = models.DateField(db_column='Effective_from', blank=True, null=True)  # Field name made lowercase.
    effective_to = models.DateField(db_column='Effective_to', blank=True, null=True)  # Field name made lowercase.
    specific_month = models.CharField(db_column='Specific_month', max_length=100, blank=True, null=True)  # Field name made lowercase.
    first_month_qtr = models.CharField(db_column='First_month_qtr', max_length=100, blank=True, null=True)  # Field name made lowercase.
    quarterly_month = models.CharField(db_column='Quarterly_month', max_length=100, blank=True, null=True)  # Field name made lowercase.
    allowance_sked = models.CharField(db_column='Allowance_sked', max_length=100, blank=True, null=True)  # Field name made lowercase.
    allowance_type = models.CharField(db_column='Allowance_type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    no_payments = models.IntegerField(db_column='No_payments', blank=True, null=True)  # Field name made lowercase.
    ref_no = models.CharField(db_column='Ref_no', max_length=11, blank=True, null=True)  # Field name made lowercase.
    bir_tag = models.CharField(max_length=31, blank=True, null=True)
    ded_sked = models.CharField(db_column='Ded_sked', max_length=30, blank=True, null=True)  # Field name made lowercase.
    deduction_type = models.CharField(db_column='Deduction_type', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_allowemplist'


class TblAlphadtl(models.Model):
    auto_num = models.AutoField(primary_key=True)
    form_type = models.CharField(max_length=25, blank=True, null=True)
    employer_tin = models.CharField(max_length=25, blank=True, null=True)
    employer_branch_code = models.CharField(max_length=25, blank=True, null=True)
    retrn_period = models.CharField(max_length=25, blank=True, null=True)
    schedule_num = models.CharField(max_length=25, blank=True, null=True)
    sequence_num = models.IntegerField()
    registered_name = models.CharField(max_length=250, blank=True, null=True)
    emp_id = models.IntegerField()
    full_name = models.CharField(max_length=999, blank=True, null=True)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    middle_name = models.CharField(max_length=250, blank=True, null=True)
    tin = models.CharField(max_length=25, blank=True, null=True)
    branch_code = models.CharField(max_length=250, blank=True, null=True)
    employment_from = models.CharField(max_length=25, blank=True, null=True)
    employment_to = models.CharField(max_length=25, blank=True, null=True)
    atc_code = models.CharField(max_length=25, blank=True, null=True)
    status_code = models.CharField(max_length=25, blank=True, null=True)
    region_num = models.CharField(max_length=25, blank=True, null=True)
    subs_filing = models.CharField(max_length=25, blank=True, null=True)
    exmpn_code = models.CharField(max_length=250, blank=True, null=True)
    factor_used = models.FloatField(blank=True, null=True)
    actual_amt_wthld = models.FloatField(blank=True, null=True)
    income_payment = models.FloatField(blank=True, null=True)
    pres_taxable_salaries = models.FloatField(blank=True, null=True)
    pres_taxable_13th_month = models.FloatField(blank=True, null=True)
    pres_tax_wthld = models.FloatField(blank=True, null=True)
    pres_nontax_salaries = models.FloatField(blank=True, null=True)
    pres_nontax_13th_month = models.FloatField(blank=True, null=True)
    prev_taxable_salaries = models.FloatField(blank=True, null=True)
    prev_taxable_13th_month = models.FloatField(blank=True, null=True)
    prev_tax_wthld = models.FloatField(blank=True, null=True)
    prev_nontax_salaries = models.FloatField(blank=True, null=True)
    prev_nontax_13th_month = models.FloatField(blank=True, null=True)
    pres_nontax_sss_gsis_oth_cont = models.FloatField(blank=True, null=True)
    prev_nontax_sss_gsis_oth_cont = models.FloatField(blank=True, null=True)
    tax_rate = models.FloatField(blank=True, null=True)
    over_wthld = models.FloatField(blank=True, null=True)
    amt_wthld_dec = models.FloatField(blank=True, null=True)
    exmpn_amt = models.FloatField(blank=True, null=True)
    tax_due = models.FloatField(blank=True, null=True)
    heath_premium = models.FloatField(blank=True, null=True)
    fringe_benefit = models.FloatField(blank=True, null=True)
    monetary_value = models.FloatField(blank=True, null=True)
    net_taxable_comp_income = models.FloatField(blank=True, null=True)
    gross_comp_income = models.FloatField(blank=True, null=True)
    prev_nontax_de_minimis = models.FloatField(blank=True, null=True)
    prev_total_nontax_comp_income = models.FloatField(blank=True, null=True)
    prev_taxable_basic_salary = models.FloatField(blank=True, null=True)
    pres_nontax_de_minimis = models.FloatField(blank=True, null=True)
    pres_taxable_basic_salary = models.FloatField(blank=True, null=True)
    pres_total_comp = models.FloatField(blank=True, null=True)
    prev_pres_total_taxable = models.FloatField(blank=True, null=True)
    pres_total_nontax_comp_income = models.FloatField(blank=True, null=True)
    prev_nontax_gross_comp_income = models.FloatField(blank=True, null=True)
    prev_nontax_basic_smw = models.FloatField(blank=True, null=True)
    prev_nontax_holiday_pay = models.FloatField(blank=True, null=True)
    prev_nontax_overtime_pay = models.FloatField(blank=True, null=True)
    prev_nontax_night_diff = models.FloatField(blank=True, null=True)
    prev_nontax_hazard_pay = models.FloatField(blank=True, null=True)
    pres_nontax_gross_comp_income = models.FloatField(blank=True, null=True)
    pres_nontax_basic_smw_day = models.FloatField(blank=True, null=True)
    pres_nontax_basic_smw_month = models.FloatField(blank=True, null=True)
    pres_nontax_basic_smw_year = models.FloatField(blank=True, null=True)
    pres_nontax_holiday_pay = models.FloatField(blank=True, null=True)
    pres_nontax_overtime_pay = models.FloatField(blank=True, null=True)
    pres_nontax_night_diff = models.FloatField(blank=True, null=True)
    prev_pres_total_comp_income = models.FloatField(blank=True, null=True)
    pres_nontax_hazard_pay = models.FloatField(blank=True, null=True)
    total_nontax_comp_income = models.FloatField(blank=True, null=True)
    total_taxable_comp_income = models.FloatField(blank=True, null=True)
    prev_total_taxable = models.FloatField(blank=True, null=True)
    nontax_basic_sal = models.FloatField(blank=True, null=True)
    tax_basic_sal = models.FloatField(blank=True, null=True)
    status_posted = models.CharField(max_length=2, blank=True, null=True)
    status_reviewed = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_alphadtl'


class TblAlphanumericTaxCode(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    short_desc = models.CharField(max_length=15, blank=True, null=True)
    tax_rate = models.FloatField(blank=True, null=True)
    atc_acronym = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_alphanumeric_tax_code'


class TblAlphanumericTaxCodeList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=25, blank=True, null=True)
    rr_date = models.CharField(max_length=25, blank=True, null=True)
    rec_code = models.IntegerField(blank=True, null=True)
    receiving_site = models.CharField(max_length=100, blank=True, null=True)
    period_from = models.DateField(blank=True, null=True)
    period_to = models.DateField(blank=True, null=True)
    supplier_code = models.IntegerField(blank=True, null=True)
    supplier = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    tin = models.CharField(db_column='TIN', max_length=25, blank=True, null=True)  # Field name made lowercase.
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    signatory = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_alphanumeric_tax_code_list'
        unique_together = (('ul_code', 'doc_no', 'rr_date', 'supplier'),)


class TblAlphanumericTaxCodeListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    rr_date = models.CharField(max_length=25, blank=True, null=True)
    rec_code = models.IntegerField(blank=True, null=True)
    receiving_site = models.CharField(max_length=100, blank=True, null=True)
    atc_acronym = models.CharField(max_length=15, blank=True, null=True)
    atc_id_code = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gross = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    vat_amount = models.FloatField(blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    tax_rate = models.CharField(max_length=10, blank=True, null=True)
    payment_amount = models.FloatField(blank=True, null=True)
    tax_withheld = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_alphanumeric_tax_code_listing'


class TblAlteracctList(models.Model):
    code = models.CharField(max_length=11)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    acct_title = models.CharField(max_length=75, blank=True, null=True)
    primary_code = models.PositiveSmallIntegerField(blank=True, null=True)
    secondary_code = models.PositiveSmallIntegerField(blank=True, null=True)
    acct_code = models.PositiveSmallIntegerField(blank=True, null=True)
    subsidiary_code = models.PositiveSmallIntegerField(blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_alteracct_list'


class TblApvList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    apv_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.PositiveIntegerField(blank=True, null=True)
    supplier = models.CharField(max_length=150, blank=True, null=True)
    terms_payment = models.PositiveSmallIntegerField(blank=True, null=True)
    payment_scheme = models.CharField(max_length=20, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=999, blank=True, null=True)
    transtype = models.CharField(db_column='TransType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(max_length=2, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    terminal_no = models.CharField(max_length=21, blank=True, null=True)
    payment_status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_apv_list'


class TblApvParticular(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    apv_no = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_apv_particular'


class TblApvPayscheme(models.Model):
    apv_no = models.FloatField(blank=True, null=True)
    installment_scheme = models.CharField(max_length=20, blank=True, null=True)
    no_installment = models.IntegerField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    amortization = models.FloatField(blank=True, null=True)
    amount_paid = models.FloatField(blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_apv_payscheme'
        unique_together = (('apv_no', 'installment_scheme', 'due_date'),)


class TblApvPpe(models.Model):
    apv_no = models.FloatField(blank=True, null=True)
    id_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=150, blank=True, null=True)
    qty = models.PositiveIntegerField(blank=True, null=True)
    date_acquired = models.DateField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    service_life = models.PositiveIntegerField(blank=True, null=True)
    code1 = models.IntegerField(blank=True, null=True)
    code2 = models.IntegerField(blank=True, null=True)
    code3 = models.IntegerField(blank=True, null=True)
    code4 = models.IntegerField(blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_apv_ppe'
        unique_together = (('apv_no', 'description'),)


class TblApvTranstype(models.Model):
    apv_no = models.FloatField(blank=True, null=True)
    trans_type = models.CharField(max_length=20, blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    rr_number = models.PositiveIntegerField(blank=True, null=True)
    dr_si_number = models.CharField(max_length=50, blank=True, null=True)
    si_no = models.CharField(max_length=50, blank=True, null=True)
    si_date = models.DateField(blank=True, null=True)
    gross_amount = models.FloatField(blank=True, null=True)
    amount_paid = models.FloatField(blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_apv_transtype'


class TblAuthorityToDeduct(models.Model):
    company_code = models.IntegerField(db_column='Company_code', blank=True, null=True)  # Field name made lowercase.
    store_code = models.IntegerField(db_column='Store_code', blank=True, null=True)  # Field name made lowercase.
    reference_no = models.CharField(db_column='Reference_no', max_length=20, blank=True, null=True)  # Field name made lowercase.
    deduction_name = models.CharField(db_column='Deduction_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deduction_type = models.CharField(db_column='Deduction_type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    deduction_code = models.CharField(db_column='Deduction_code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    amortization = models.TextField(db_column='AMORTIZATION', blank=True, null=True)  # Field name made lowercase.
    employee = models.TextField(db_column='Employee', blank=True, null=True)  # Field name made lowercase.
    company_name = models.CharField(db_column='Company_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    preparedby = models.CharField(db_column='PreparedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date_trans = models.DateField(db_column='Date_trans', blank=True, null=True)  # Field name made lowercase.
    pperiod = models.CharField(db_column='PPeriod', max_length=30, blank=True, null=True)  # Field name made lowercase.
    date_from = models.CharField(db_column='Date_from', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date_to = models.CharField(db_column='Date_to', max_length=20, blank=True, null=True)  # Field name made lowercase.
    payment_scheme = models.CharField(db_column='Payment_Scheme', max_length=20, blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status_ded = models.CharField(db_column='STATUS_DED', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dept_id = models.FloatField(db_column='Dept_ID', blank=True, null=True)  # Field name made lowercase.
    payout_type = models.CharField(db_column='PayOut_type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    firstmonth = models.CharField(db_column='FirstMonth', max_length=20, blank=True, null=True)  # Field name made lowercase.
    specified_month = models.CharField(db_column='Specified_Month', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    fix_amnt = models.CharField(db_column='Fix_amnt', max_length=5, blank=True, null=True)  # Field name made lowercase.
    designationid = models.FloatField(db_column='DesignationID', blank=True, null=True)  # Field name made lowercase.
    no_payment = models.FloatField(db_column='No_Payment', blank=True, null=True)  # Field name made lowercase.
    date_loan = models.DateField(db_column='Date_loan', blank=True, null=True)  # Field name made lowercase.
    first_due = models.DateField(db_column='First_Due', blank=True, null=True)  # Field name made lowercase.
    monthy_amort = models.FloatField(db_column='Monthy_Amort', blank=True, null=True)  # Field name made lowercase.
    first_month_amort = models.FloatField(db_column='First_month_Amort', blank=True, null=True)  # Field name made lowercase.
    same_amount = models.CharField(db_column='Same_amount', max_length=5, blank=True, null=True)  # Field name made lowercase.
    emp_stat = models.IntegerField(db_column='Emp_stat', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_authority_to_deduct'


class TblAuthorityToDeductWithEmployer(models.Model):
    company_code = models.IntegerField(db_column='Company_code', blank=True, null=True)  # Field name made lowercase.
    store_code = models.IntegerField(db_column='Store_code', blank=True, null=True)  # Field name made lowercase.
    reference_no = models.CharField(db_column='Reference_no', max_length=20, blank=True, null=True)  # Field name made lowercase.
    deduction_name = models.CharField(db_column='Deduction_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deduction_type = models.CharField(db_column='Deduction_type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    deduction_code = models.CharField(db_column='Deduction_code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    default_empe = models.FloatField(db_column='Default_empe', blank=True, null=True)  # Field name made lowercase.
    default_empr = models.FloatField(blank=True, null=True)
    amortization = models.TextField(db_column='AMORTIZATION', blank=True, null=True)  # Field name made lowercase.
    employee = models.TextField(db_column='Employee', blank=True, null=True)  # Field name made lowercase.
    company_name = models.CharField(db_column='Company_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    preparedby = models.CharField(db_column='PreparedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    date_trans = models.DateField(db_column='Date_trans', blank=True, null=True)  # Field name made lowercase.
    pperiod = models.CharField(db_column='PPeriod', max_length=30, blank=True, null=True)  # Field name made lowercase.
    date_from = models.CharField(db_column='Date_from', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date_to = models.CharField(db_column='Date_to', max_length=20, blank=True, null=True)  # Field name made lowercase.
    payment_scheme = models.CharField(db_column='Payment_Scheme', max_length=20, blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status_ded = models.CharField(db_column='Status_Ded', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dept_id = models.FloatField(db_column='Dept_ID', blank=True, null=True)  # Field name made lowercase.
    payout_type = models.CharField(db_column='PayOut_type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    firstmonth = models.CharField(db_column='FirstMonth', max_length=30, blank=True, null=True)  # Field name made lowercase.
    specified_month = models.CharField(db_column='Specified_Month', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    fix_amnt = models.CharField(db_column='Fix_amnt', max_length=5, blank=True, null=True)  # Field name made lowercase.
    designationid = models.FloatField(db_column='DesignationID', blank=True, null=True)  # Field name made lowercase.
    no_payment = models.FloatField(db_column='No_Payment', blank=True, null=True)  # Field name made lowercase.
    date_loan = models.DateField(db_column='Date_loan', blank=True, null=True)  # Field name made lowercase.
    first_due = models.DateField(db_column='First_Due', blank=True, null=True)  # Field name made lowercase.
    monthy_amort = models.FloatField(db_column='Monthy_Amort', blank=True, null=True)  # Field name made lowercase.
    first_month_amort = models.FloatField(db_column='First_month_Amort', blank=True, null=True)  # Field name made lowercase.
    same_amount = models.CharField(db_column='Same_amount', max_length=5, blank=True, null=True)  # Field name made lowercase.
    emp_stat = models.IntegerField(db_column='Emp_stat', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_authority_to_deduct_with_employer'


class TblBackupCvTranstype(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    cv_no = models.FloatField(blank=True, null=True)
    trans_type = models.CharField(max_length=150, blank=True, null=True)
    apv_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    amount_due = models.FloatField(blank=True, null=True)
    gross_amount = models.FloatField(blank=True, null=True)
    scheme_type = models.CharField(max_length=10, blank=True, null=True)
    sec_ref = models.CharField(max_length=10, blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    acct_code = models.CharField(max_length=11, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=100, blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_backup_cv_transtype'


class TblBackupJvAdjustment(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    jv_no = models.FloatField(blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=100, blank=True, null=True)
    reference_no = models.FloatField(blank=True, null=True)
    reference_type = models.CharField(max_length=3, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    transaction_type = models.CharField(max_length=100, blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    acct_code = models.CharField(max_length=11, blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doctype_ref = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_backup_jv_adjustment'


class TblBackupListingApv(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    supplier = models.CharField(max_length=150, blank=True, null=True)
    apv_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.PositiveIntegerField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    primary_code = models.PositiveSmallIntegerField(blank=True, null=True)
    secondary_code = models.PositiveSmallIntegerField(blank=True, null=True)
    acct_code = models.PositiveSmallIntegerField(blank=True, null=True)
    subsidiary_code = models.PositiveSmallIntegerField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    active = models.CharField(max_length=2, blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_backup_listing_apv'


class TblBackupListingAr(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    customer = models.CharField(max_length=150, blank=True, null=True)
    ci_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.PositiveIntegerField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    primary_code = models.PositiveIntegerField(blank=True, null=True)
    secondary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_code = models.PositiveIntegerField(blank=True, null=True)
    subsidiary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    active = models.CharField(max_length=2, blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_backup_listing_ar'


class TblBackupListingCdb(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    payee = models.CharField(max_length=150, blank=True, null=True)
    cv_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.PositiveIntegerField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    primary_code = models.PositiveIntegerField(blank=True, null=True)
    secondary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_code = models.PositiveIntegerField(blank=True, null=True)
    subsidiary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    active = models.CharField(max_length=2, blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_backup_listing_cdb'


class TblBackupListingCrb(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    payor = models.CharField(max_length=150, blank=True, null=True)
    ref_or_no = models.FloatField()
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.PositiveIntegerField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    primary_code = models.PositiveIntegerField(blank=True, null=True)
    secondary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_code = models.PositiveIntegerField(blank=True, null=True)
    subsidiary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    active = models.CharField(max_length=2, blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_backup_listing_crb'


class TblBackupListingGj(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    incharge = models.CharField(max_length=150, blank=True, null=True)
    jv_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.PositiveIntegerField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    primary_code = models.PositiveIntegerField(blank=True, null=True)
    secondary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_code = models.PositiveIntegerField(blank=True, null=True)
    subsidiary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    active = models.CharField(max_length=2, blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_backup_listing_gj'


class TblBackupPorTranstype(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    or_no = models.FloatField(blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=300, blank=True, null=True)
    ci_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    amount_due = models.FloatField(blank=True, null=True)
    gross_amount = models.FloatField(blank=True, null=True)
    scheme_type = models.CharField(max_length=10, blank=True, null=True)
    sec_ref = models.CharField(max_length=100, blank=True, null=True)
    sa_no = models.CharField(max_length=15, blank=True, null=True)
    sl_name = models.CharField(max_length=100, blank=True, null=True)
    acct_code = models.CharField(max_length=11, blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_backup_por_transtype'


class TblBankCard(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.CharField(max_length=10, blank=True, null=True)
    card_description = models.CharField(max_length=30, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_bank_card'


class TblBankCompany(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.CharField(max_length=10, blank=True, null=True)
    company_description = models.CharField(max_length=30, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_bank_company'


class TblBankDrawee(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.CharField(max_length=10, blank=True, null=True)
    bank_description = models.CharField(max_length=150, blank=True, null=True)
    bank_abbreviation = models.CharField(max_length=150, blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_account = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_bank_drawee'


class TblBiometricIpadd(models.Model):
    company_code = models.IntegerField(db_column='Company_code', blank=True, null=True)  # Field name made lowercase.
    store_code = models.IntegerField(db_column='Store_Code', blank=True, null=True)  # Field name made lowercase.
    ip_address_bio = models.CharField(db_column='IP_address_Bio', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bio_location = models.CharField(db_column='Bio_location', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_biometric_ipadd'


class TblBirTags(models.Model):
    auto_num = models.AutoField(db_column='Auto_num', primary_key=True)  # Field name made lowercase.
    bir_tag_id = models.CharField(max_length=250, blank=True, null=True)
    bir_tag_desc = models.CharField(max_length=250, blank=True, null=True)
    bir_tag_category = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_bir_tags'


class TblBooksHeader(models.Model):
    line_number = models.IntegerField(blank=True, null=True)
    module_type = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_books_header'


class TblBudget(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    center_type = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    desc_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    acct_code = models.FloatField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    budget_amt = models.FloatField(blank=True, null=True)
    budget_period = models.CharField(max_length=25, blank=True, null=True)
    budget_from = models.DateField(blank=True, null=True)
    budget_to = models.DateField(blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_budget'


class TblCategorytime(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    categ_desc = models.CharField(db_column='Categ_desc', max_length=40, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=1, blank=True, null=True)
    short_desc = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_categorytime'


class TblCcc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    code = models.SmallIntegerField(blank=True, null=True)
    category = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ccc'


class TblCccDetails(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=60, blank=True, null=True)
    desc_code = models.SmallIntegerField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    rc_cost_category = models.CharField(max_length=100, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    alter_code = models.CharField(max_length=50, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    mfg_date = models.CharField(max_length=25, blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.CharField(max_length=25, blank=True, null=True)
    mod_type = models.CharField(max_length=10, blank=True, null=True)
    mod_type_dup = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ccc_details'


class TblCccSubCategory(models.Model):
    desc_code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    sub_code = models.IntegerField(blank=True, null=True)
    sub_category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ccc_sub_category'


class TblCfType(models.Model):
    line_number = models.IntegerField(blank=True, null=True)
    header = models.CharField(max_length=1, blank=True, null=True)
    module_type = models.CharField(max_length=3, blank=True, null=True)
    cf_key = models.CharField(max_length=10, blank=True, null=True)
    cf_desc = models.CharField(max_length=100, blank=True, null=True)
    wtax = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_cf_type'


class TblChangeEquity(models.Model):
    description = models.CharField(max_length=40, blank=True, null=True)
    activate = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_change_equity'


class TblCheckSeries(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    bank_abbreviation = models.CharField(max_length=150, blank=True, null=True)
    current_check = models.BigIntegerField(blank=True, null=True)
    range1 = models.BigIntegerField(blank=True, null=True)
    range2 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_check_series'


class TblCiList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    ci_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.PositiveIntegerField(blank=True, null=True)
    customer = models.CharField(max_length=150, blank=True, null=True)
    sec_ref = models.CharField(max_length=100, blank=True, null=True)
    terms_payment = models.PositiveSmallIntegerField(blank=True, null=True)
    payment_scheme = models.CharField(max_length=20, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=999, blank=True, null=True)
    transtype = models.CharField(db_column='TransType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(max_length=2, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    payment_status = models.CharField(max_length=10, blank=True, null=True)
    terminal_no = models.CharField(max_length=21, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ci_list'


class TblCiPayscheme(models.Model):
    ci_no = models.FloatField(blank=True, null=True)
    installment_scheme = models.CharField(max_length=20, blank=True, null=True)
    no_installment = models.IntegerField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    amortization = models.FloatField(blank=True, null=True)
    amount_paid = models.FloatField(blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    payment_status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ci_payscheme'
        unique_together = (('ci_no', 'installment_scheme', 'due_date'),)


class TblCiTranstype(models.Model):
    ci_no = models.FloatField(blank=True, null=True)
    trans_type = models.CharField(max_length=900, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    gross_amount = models.FloatField(blank=True, null=True)
    amount_paid = models.FloatField(blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ci_transtype'


class TblCloseBook(models.Model):
    period_closed = models.CharField(max_length=6, blank=True, null=True)
    day_date = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_close_book'


class TblCodeRefNo(models.Model):
    autonum = models.AutoField(primary_key=True)
    description = models.CharField(max_length=25, blank=True, null=True)
    next_no = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_code_ref_no'


class TblCollector(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.SmallIntegerField(blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    home_phone_no = models.CharField(max_length=15, blank=True, null=True)
    mobile_no = models.CharField(max_length=15, blank=True, null=True)
    fax_no = models.CharField(max_length=15, blank=True, null=True)
    st_address = models.CharField(max_length=60, blank=True, null=True)
    city_address = models.CharField(max_length=30, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    date_entered = models.DateField(blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    with_salesagent = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_collector'


class TblCompanySetup(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    company_logo = models.CharField(max_length=1, blank=True, null=True)
    company_type = models.CharField(max_length=25, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_initials = models.CharField(max_length=1, blank=True, null=True)
    company_address = models.CharField(max_length=150, blank=True, null=True)
    begin_date = models.CharField(max_length=20)
    system_date_created = models.DateTimeField(blank=True, null=True)
    createinventory = models.CharField(db_column='createInventory', max_length=1, blank=True, null=True)  # Field name made lowercase.
    autocreate_bc = models.CharField(max_length=1)
    standpurch = models.CharField(db_column='standPurch', max_length=1)  # Field name made lowercase.
    company_tin = models.CharField(db_column='company_TIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    company_zipcode = models.CharField(max_length=4, blank=True, null=True)
    showallitem = models.CharField(max_length=1, blank=True, null=True)
    no_rs = models.CharField(max_length=1, blank=True, null=True)
    allowin = models.CharField(max_length=1, blank=True, null=True)
    autoin = models.CharField(max_length=1, blank=True, null=True)
    defaultfind = models.CharField(max_length=1, blank=True, null=True)
    method = models.CharField(max_length=2, blank=True, null=True)
    alter_code = models.CharField(max_length=1, blank=True, null=True)
    allow_dup = models.CharField(max_length=1, blank=True, null=True)
    allow_siprooflist = models.CharField(db_column='allow_SIproofList', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allow_multiar = models.CharField(db_column='allow_multiAR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allow_uomsum = models.CharField(db_column='allow_UOMSum', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allowcreatingcustomer = models.CharField(db_column='allowCreatingCustomer', max_length=1, blank=True, null=True)  # Field name made lowercase.
    with_salesagent = models.CharField(max_length=1, blank=True, null=True)
    tagging_per_product = models.CharField(max_length=1, blank=True, null=True)
    tagging_postprint = models.CharField(max_length=1, blank=True, null=True)
    allowinvoicecreation = models.CharField(db_column='allowInvoiceCreation', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allowstocktransfercreation = models.CharField(db_column='allowStockTransferCreation', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allowrrcreation = models.CharField(db_column='allowRRCreation', max_length=1, blank=True, null=True)  # Field name made lowercase.
    withvirtualset = models.CharField(db_column='withVirtualSet', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allow_custom_name = models.CharField(max_length=1, blank=True, null=True)
    withconcessionare = models.CharField(db_column='withConcessionare', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allowfixingvat = models.CharField(db_column='allowFixingVAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    collectionor = models.CharField(db_column='collectionOR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hide_prooflist = models.CharField(db_column='hide_ProofList', max_length=1, blank=True, null=True)  # Field name made lowercase.
    doc_type = models.CharField(max_length=1, blank=True, null=True)
    inv_type = models.CharField(max_length=25, blank=True, null=True)
    cat_sales = models.CharField(max_length=1, blank=True, null=True)
    comm_rep = models.CharField(max_length=1, blank=True, null=True)
    nopo = models.CharField(max_length=1, blank=True, null=True)
    rr_cost = models.CharField(max_length=1, blank=True, null=True)
    inv_dup = models.CharField(max_length=1, blank=True, null=True)
    edit_sell = models.CharField(max_length=1, blank=True, null=True)
    with_journal = models.CharField(max_length=1, blank=True, null=True)
    with_delivered = models.CharField(max_length=1, blank=True, null=True)
    with_pos_sales = models.CharField(db_column='with_POS_sales', max_length=1, blank=True, null=True)  # Field name made lowercase.
    banking = models.CharField(max_length=1, blank=True, null=True)
    supp_rel = models.CharField(max_length=1, blank=True, null=True)
    docpersite = models.CharField(max_length=1, blank=True, null=True)
    zero_qty = models.CharField(max_length=1, blank=True, null=True)
    blank_site = models.CharField(max_length=1, blank=True, null=True)
    cash_ref = models.CharField(max_length=1, blank=True, null=True)
    auto_pn = models.CharField(max_length=1, blank=True, null=True)
    sales_disc = models.CharField(max_length=1, blank=True, null=True)
    section = models.CharField(db_column='Section', max_length=1, blank=True, null=True)  # Field name made lowercase.
    multiplepricetype = models.CharField(db_column='Multiplepricetype', max_length=1, blank=True, null=True)  # Field name made lowercase.
    multiplediscounttype = models.CharField(db_column='MultipleDiscountType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    update_cost = models.CharField(max_length=1, blank=True, null=True)
    prodjoblot = models.CharField(db_column='prodJobLot', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prodinsite = models.CharField(db_column='ProdINSite', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pocurrency = models.CharField(db_column='POCurrency', max_length=1, blank=True, null=True)  # Field name made lowercase.
    unadj_sl = models.CharField(max_length=1, blank=True, null=True)
    per_ul = models.CharField(max_length=1, blank=True, null=True)
    business_unit = models.CharField(max_length=15, blank=True, null=True)
    per_logo = models.CharField(max_length=1, blank=True, null=True)
    multipletaxcustomer = models.CharField(db_column='multipleTaxCustomer', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allowdrsi = models.CharField(db_column='AllowDRSI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    auto_wht = models.CharField(max_length=1, blank=True, null=True)
    auto_tax = models.CharField(max_length=1, blank=True, null=True)
    sys_expire = models.CharField(max_length=1, blank=True, null=True)
    without_logo = models.TextField(blank=True, null=True)
    logo_img = models.TextField(blank=True, null=True)
    default_decimal = models.IntegerField(blank=True, null=True)
    default_po_validity = models.IntegerField(db_column='default_PO_Validity', blank=True, null=True)  # Field name made lowercase.
    doctypeno = models.IntegerField(blank=True, null=True)
    noofbook = models.IntegerField(blank=True, null=True)
    cv_app = models.CharField(max_length=1, blank=True, null=True)
    jv_app = models.CharField(max_length=1, blank=True, null=True)
    or_app = models.CharField(max_length=1, blank=True, null=True)
    apvrep = models.CharField(db_column='apvRep', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cvrep = models.CharField(db_column='cvRep', max_length=1, blank=True, null=True)  # Field name made lowercase.
    orrep = models.CharField(db_column='orRep', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cirep = models.CharField(db_column='ciRep', max_length=1, blank=True, null=True)  # Field name made lowercase.
    jvrep = models.CharField(db_column='jvRep', max_length=1, blank=True, null=True)  # Field name made lowercase.
    principal = models.CharField(max_length=1, blank=True, null=True)
    printbeforesave = models.CharField(db_column='PrintbeforeSave', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allowbackup = models.CharField(db_column='allowBackup', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allow_viewing_per_terminal = models.CharField(max_length=1, blank=True, null=True)
    allow_delete_module = models.CharField(max_length=1, blank=True, null=True)
    allow_custom_sl = models.CharField(max_length=1, blank=True, null=True)
    allow_block_aging = models.CharField(max_length=1, blank=True, null=True)
    posted_aging_only = models.CharField(max_length=1, blank=True, null=True)
    witholding_period = models.CharField(max_length=15, blank=True, null=True)
    customized_configuration = models.CharField(max_length=1, blank=True, null=True)
    bill_sequence = models.CharField(max_length=1, blank=True, null=True)
    req_drsi = models.CharField(db_column='req_DRSI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sl_change = models.CharField(max_length=1, blank=True, null=True)
    field_change = models.CharField(max_length=1, blank=True, null=True)
    item_trade = models.CharField(max_length=1, blank=True, null=True)
    po_specs = models.CharField(max_length=1, blank=True, null=True)
    so_specs = models.CharField(max_length=1, blank=True, null=True)
    po_trans_discount = models.CharField(max_length=1, blank=True, null=True)
    allow_post_cash = models.CharField(max_length=1, blank=True, null=True)
    show_issue_prod = models.CharField(max_length=1, blank=True, null=True)
    allow_issue_prod = models.CharField(max_length=1, blank=True, null=True)
    allow_transfer_price = models.CharField(max_length=1, blank=True, null=True)
    withhold_tax = models.CharField(max_length=1, blank=True, null=True)
    billing_display = models.CharField(max_length=1, blank=True, null=True)
    sortingavail = models.CharField(db_column='sortingAvail', max_length=1, blank=True, null=True)  # Field name made lowercase.
    activate_credit_limit = models.CharField(max_length=1, blank=True, null=True)
    allow_tagging_bank = models.CharField(max_length=1, blank=True, null=True)
    hide_overpayment = models.CharField(max_length=1, blank=True, null=True)
    manual_billing = models.CharField(max_length=1, blank=True, null=True)
    allow_payee_alter = models.CharField(max_length=1, blank=True, null=True)
    allow_rr_remarks_wtax = models.CharField(max_length=1, blank=True, null=True)
    allow_multiple_wtax = models.CharField(max_length=1, blank=True, null=True)
    customexport = models.CharField(db_column='CustomExport', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allow_breakdown = models.CharField(max_length=1, blank=True, null=True)
    allow_pcfslip = models.CharField(max_length=1, blank=True, null=True)
    allow_doctag = models.CharField(max_length=1, blank=True, null=True)
    allowbookaccount = models.CharField(db_column='allowBookAccount', max_length=1, blank=True, null=True)  # Field name made lowercase.
    customizeheader = models.CharField(db_column='CustomizeHeader', max_length=1, blank=True, null=True)  # Field name made lowercase.
    max_reference_no = models.IntegerField(blank=True, null=True)
    seriescheck = models.CharField(db_column='SeriesCheck', max_length=1, blank=True, null=True)  # Field name made lowercase.
    accessrestriction = models.CharField(db_column='accessRestriction', max_length=1, blank=True, null=True)  # Field name made lowercase.
    autofillcheckwithremarks = models.CharField(db_column='autoFillCheckWithRemarks', max_length=1, blank=True, null=True)  # Field name made lowercase.
    showcvamount = models.CharField(db_column='showCVAmount', max_length=1, blank=True, null=True)  # Field name made lowercase.
    backupenable = models.CharField(db_column='BackupEnable', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sortenabled = models.CharField(db_column='sortEnabled', max_length=1, blank=True, null=True)  # Field name made lowercase.
    enablebeginbalance = models.CharField(db_column='enableBeginBalance', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allowpostedtrans = models.CharField(db_column='AllowPostedTrans', max_length=1, blank=True, null=True)  # Field name made lowercase.
    enableothertrans = models.CharField(db_column='enableOtherTrans', max_length=1, blank=True, null=True)  # Field name made lowercase.
    showrequestpaymentind = models.CharField(db_column='showRequestPaymentInd', max_length=1, blank=True, null=True)  # Field name made lowercase.
    showrequestpaymentintegrated = models.CharField(db_column='showRequestPaymentIntegrated', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allowcashdaterangedeposit = models.CharField(db_column='AllowCashDateRangeDeposit', max_length=1, blank=True, null=True)  # Field name made lowercase.
    includeadjcollection = models.CharField(db_column='includeAdjCollection', max_length=1, blank=True, null=True)  # Field name made lowercase.
    by_sec_ref = models.CharField(max_length=1)
    by_delivery_date = models.CharField(max_length=1)
    by_terms = models.CharField(max_length=1)
    by_due_date = models.CharField(max_length=1)
    by_delivery_no = models.CharField(max_length=1)
    hide_trade = models.CharField(max_length=1)
    allowchangedocumentname = models.CharField(db_column='allowChangeDocumentName', max_length=1, blank=True, null=True)  # Field name made lowercase.
    payeecandeletenotadd = models.CharField(db_column='PayeeCanDeleteNotAdd', max_length=1, blank=True, null=True)  # Field name made lowercase.
    with_tardiness_escalation = models.CharField(max_length=1, blank=True, null=True)
    with_dtar = models.CharField(db_column='with_DTAR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    min_take_home_pay = models.CharField(max_length=30, blank=True, null=True)
    restrictulsite = models.CharField(db_column='restrictULSite', max_length=1, blank=True, null=True)  # Field name made lowercase.
    enablemembersl = models.CharField(db_column='EnableMemberSL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nologinul = models.CharField(db_column='NoLoginUL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    showslconso = models.CharField(db_column='showSLConso', max_length=1, blank=True, null=True)  # Field name made lowercase.
    show_period_no = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_company_setup'


class TblCondition(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.CharField(max_length=10, blank=True, null=True)
    condition_description = models.CharField(max_length=30, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_condition'


class TblConsultant(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.PositiveIntegerField()
    trade_name = models.CharField(max_length=40)
    consultant_class = models.CharField(max_length=15, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    business_phone_no = models.CharField(max_length=15, blank=True, null=True)
    mobile_no = models.CharField(max_length=15, blank=True, null=True)
    fax_no = models.CharField(max_length=15, blank=True, null=True)
    st_address = models.CharField(max_length=60, blank=True, null=True)
    city_address = models.CharField(max_length=30, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    trade = models.CharField(max_length=1, blank=True, null=True)
    vat = models.CharField(max_length=1, blank=True, null=True)
    bir_reg_no = models.CharField(max_length=20, blank=True, null=True)
    tax_id_no = models.IntegerField(blank=True, null=True)
    credit_terms = models.SmallIntegerField(blank=True, null=True)
    credit_limit = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    date_as_of = models.DateField(blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    consultant_image = models.TextField(blank=True, null=True)
    date_entered = models.DateField(blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_consultant'
        unique_together = (('id_code', 'trade_name', 'last_name', 'first_name', 'middle_name'),)


class TblCredentials(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    secret_word = models.CharField(max_length=150, blank=True, null=True)
    secret_phrase = models.CharField(max_length=150, blank=True, null=True)
    secret_role = models.CharField(max_length=150, blank=True, null=True)
    date_created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_credentials'


class TblCustomer(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.FloatField()
    trade_name = models.CharField(max_length=150, blank=True, null=True)
    customer_class = models.CharField(max_length=15, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=20)
    business_phone_no = models.CharField(max_length=15, blank=True, null=True)
    business_style = models.CharField(max_length=150, blank=True, null=True)
    mobile_no = models.CharField(max_length=15, blank=True, null=True)
    fax_no = models.CharField(max_length=15, blank=True, null=True)
    st_address = models.CharField(max_length=60, blank=True, null=True)
    city_address = models.CharField(max_length=30, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    vat = models.CharField(max_length=1, blank=True, null=True)
    bir_reg_no = models.CharField(max_length=25, blank=True, null=True)
    tax_id_no = models.CharField(max_length=25, blank=True, null=True)
    credit_terms = models.SmallIntegerField(blank=True, null=True)
    credit_limit = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    date_as_of = models.DateField(blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=150, blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)
    area_name = models.CharField(max_length=150, blank=True, null=True)
    office_name = models.CharField(max_length=150, blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    agent_name = models.CharField(max_length=150, blank=True, null=True)
    collector_id = models.IntegerField(blank=True, null=True)
    collector_name = models.CharField(max_length=150, blank=True, null=True)
    kob_id = models.IntegerField(blank=True, null=True)
    kob_name = models.CharField(max_length=150, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    customer_image = models.TextField(blank=True, null=True)
    date_entered = models.DateField(blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    concessionare = models.CharField(db_column='Concessionare', max_length=10, blank=True, null=True)  # Field name made lowercase.
    client_behavior = models.CharField(db_column='Client_behavior', max_length=5)  # Field name made lowercase.
    sl_category = models.CharField(max_length=50, blank=True, null=True)
    wtax_agent = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_customer'
        unique_together = (('id_code', 'trade_name', 'last_name', 'first_name', 'middle_name'),)


class TblCustomerArea(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    area_name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_customer_area'


class TblCustomerBillingInfo(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=150, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    st_address = models.CharField(max_length=60, blank=True, null=True)
    city_address = models.CharField(max_length=30, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_customer_billing_info'
        unique_together = (('id_code', 'full_name', 'designation'),)


class TblCustomerGroup(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_customer_group'


class TblCustomerKob(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    kob_name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_customer_kob'


class TblCustomerSOA(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveIntegerField()
    id_code = models.PositiveIntegerField()
    customer = models.CharField(max_length=100)
    cust_tin = models.CharField(max_length=150, blank=True, null=True)
    particulars = models.CharField(max_length=500, blank=True, null=True)
    customer_address = models.CharField(max_length=150, blank=True, null=True)
    soa_no = models.FloatField()
    date_trans = models.CharField(max_length=30)
    due_date = models.CharField(max_length=10, db_collation='latin1_bin')
    ref_no = models.CharField(max_length=20, blank=True, null=True)
    charges = models.FloatField()
    debit = models.FloatField(blank=True, null=True)
    credit = models.FloatField(blank=True, null=True)
    payments = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    date_covered = models.CharField(max_length=50, blank=True, null=True)
    date_generated = models.DateField(blank=True, null=True)
    so_no = models.CharField(max_length=10, blank=True, null=True)
    soa_no_char = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_customer_s_o_a'


class TblCustomerSoa(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveIntegerField()
    id_code = models.PositiveIntegerField()
    customer = models.CharField(max_length=100)
    soa_no = models.FloatField()
    ci_no = models.FloatField()
    due_date = models.DateField()
    amount = models.FloatField()
    date_covered = models.CharField(max_length=50, blank=True, null=True)
    date_generated = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_customer_soa'


class TblCvList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    cv_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    id_code = models.PositiveIntegerField(blank=True, null=True)
    payee = models.CharField(max_length=150, blank=True, null=True)
    check_amt = models.FloatField(blank=True, null=True)
    drawee_bank = models.CharField(max_length=150, blank=True, null=True)
    date_check = models.DateField(blank=True, null=True)
    check_no = models.FloatField(blank=True, null=True)
    check_type = models.CharField(max_length=1, blank=True, null=True)
    remarks = models.CharField(max_length=999, blank=True, null=True)
    transtype = models.CharField(db_column='TransType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(max_length=2, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    terminal_no = models.CharField(max_length=21, blank=True, null=True)
    tmp_payee = models.CharField(max_length=150, blank=True, null=True)
    ref_no = models.FloatField(blank=True, null=True)
    ref_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_cv_list'


class TblCvParticular(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    cv_no = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    amount2 = models.FloatField(blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_cv_particular'


class TblCvPaymentRequest(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    cv_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.PositiveIntegerField(blank=True, null=True)
    payee = models.CharField(max_length=150, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    transtype = models.CharField(db_column='TransType', max_length=150, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(max_length=2, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    disapproved_by = models.CharField(max_length=60, blank=True, null=True)
    disapproved_date = models.CharField(max_length=25, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_cv_payment_request'


class TblCvPayscheme(models.Model):
    cv_no = models.FloatField(blank=True, null=True)
    installment_scheme = models.CharField(max_length=20, blank=True, null=True)
    no_installment = models.IntegerField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    sec_ref = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    amortization = models.FloatField(blank=True, null=True)
    amount_paid = models.FloatField(blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    payment_status = models.CharField(max_length=10, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_cv_payscheme'
        unique_together = (('cv_no', 'installment_scheme', 'due_date'),)


class TblCvPpe(models.Model):
    cv_no = models.FloatField(blank=True, null=True)
    id_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=150, blank=True, null=True)
    qty = models.PositiveIntegerField(blank=True, null=True)
    date_acquired = models.DateField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    service_life = models.PositiveIntegerField(blank=True, null=True)
    code1 = models.IntegerField(blank=True, null=True)
    code2 = models.IntegerField(blank=True, null=True)
    code3 = models.IntegerField(blank=True, null=True)
    code4 = models.IntegerField(blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_cv_ppe'
        unique_together = (('cv_no', 'id_code', 'description', 'category'),)


class TblCvTranstype(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    cv_no = models.FloatField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    apv_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    amount_due = models.FloatField(blank=True, null=True)
    gross_amount = models.FloatField(blank=True, null=True)
    source_module_ap = models.CharField(max_length=3, blank=True, null=True)
    scheme_type = models.CharField(max_length=10, blank=True, null=True)
    sec_ref = models.CharField(max_length=10, blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    acct_code = models.CharField(max_length=11, blank=True, null=True)
    supplier_code = models.CharField(max_length=11, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=100, blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    ul_code_pmt = models.IntegerField(blank=True, null=True)
    date_trans_pmt = models.DateField(blank=True, null=True)
    source_module_pmt = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_cv_transtype'


class TblDedWithemplyerFinal(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', primary_key=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='COmpany_code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    store_code = models.IntegerField(db_column='Store_code', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    ded_code = models.FloatField(db_column='Ded_code', blank=True, null=True)  # Field name made lowercase.
    empyee_share = models.FloatField(db_column='Empyee_share', blank=True, null=True)  # Field name made lowercase.
    empyer_share = models.FloatField(db_column='Empyer_share', blank=True, null=True)  # Field name made lowercase.
    total_amnt = models.FloatField(db_column='Total_Amnt', blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ded_withemplyer_final'


class TblDedamortlist(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', primary_key=True)  # Field name made lowercase.
    ded_code = models.FloatField(db_column='Ded_code', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_ID', blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    amort = models.FloatField(db_column='Amort', blank=True, null=True)  # Field name made lowercase.
    series_no = models.IntegerField(db_column='Series_no', blank=True, null=True)  # Field name made lowercase.
    balance = models.FloatField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    date_update = models.DateField(db_column='Date_update', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ref_no = models.CharField(max_length=20, blank=True, null=True)
    bir_tag = models.CharField(max_length=31, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_dedamortlist'


class TblDedemplist(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', primary_key=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    default_amnt = models.FloatField(db_column='Default_amnt', blank=True, null=True)  # Field name made lowercase.
    ded_code = models.CharField(db_column='Ded_Code', max_length=20, blank=True, null=True)  # Field name made lowercase.
    default_amnt2 = models.FloatField(db_column='Default_amnt2', blank=True, null=True)  # Field name made lowercase.
    effective_from = models.DateField(db_column='Effective_from', blank=True, null=True)  # Field name made lowercase.
    effective_to = models.DateField(db_column='Effective_to', blank=True, null=True)  # Field name made lowercase.
    specific_month = models.CharField(db_column='Specific_month', max_length=100, blank=True, null=True)  # Field name made lowercase.
    first_month_qtr = models.CharField(db_column='First_month_qtr', max_length=100, blank=True, null=True)  # Field name made lowercase.
    quarterly_month = models.CharField(db_column='Quarterly_month', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ded_sked = models.CharField(db_column='Ded_sked', max_length=100, blank=True, null=True)  # Field name made lowercase.
    deduction_type = models.CharField(db_column='Deduction_type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    no_payments = models.IntegerField(db_column='No_payments', blank=True, null=True)  # Field name made lowercase.
    ref_no = models.CharField(db_column='Ref_no', max_length=11, blank=True, null=True)  # Field name made lowercase.
    bir_tag = models.CharField(max_length=31, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_dedemplist'


class TblDeductionlist(models.Model):
    auto_no = models.AutoField(primary_key=True)
    company_code = models.IntegerField(db_column='Company_code', blank=True, null=True)  # Field name made lowercase.
    store_code = models.IntegerField(blank=True, null=True)
    ded_code = models.FloatField(db_column='Ded_code', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    payout_period = models.CharField(db_column='Payout_period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    empye_share = models.FloatField(db_column='Empye_share', blank=True, null=True)  # Field name made lowercase.
    empr_share = models.FloatField(db_column='Empr_share', blank=True, null=True)  # Field name made lowercase.
    ded_name = models.CharField(db_column='Ded_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tax_deductible = models.CharField(db_column='Tax_deductible', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bir_tag = models.CharField(max_length=31, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_deductionlist'


class TblDeductionsPayrollFinal(models.Model):
    auto_no = models.FloatField(primary_key=True)
    company_code = models.FloatField(blank=True, null=True)
    branch_code = models.FloatField(db_column='Branch_code', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    dept_id = models.FloatField(db_column='Dept_ID', blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sss = models.FloatField(db_column='SSS', blank=True, null=True)  # Field name made lowercase.
    hdmf = models.FloatField(db_column='HDMF', blank=True, null=True)  # Field name made lowercase.
    phic = models.FloatField(db_column='PHIC', blank=True, null=True)  # Field name made lowercase.
    incometax = models.FloatField(db_column='IncomeTAX', blank=True, null=True)  # Field name made lowercase.
    other_deduction = models.CharField(db_column='Other_deduction', max_length=500, blank=True, null=True)  # Field name made lowercase.
    allowance = models.CharField(db_column='Allowance', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tot_odeductions = models.FloatField(db_column='Tot_Odeductions', blank=True, null=True)  # Field name made lowercase.
    total_deductions = models.FloatField(db_column='Total_deductions', blank=True, null=True)  # Field name made lowercase.
    total_allowance = models.FloatField(db_column='Total_allowance', blank=True, null=True)  # Field name made lowercase.
    sss_er = models.FloatField(db_column='SSS_er', blank=True, null=True)  # Field name made lowercase.
    sss_ec_er = models.FloatField(db_column='SSS_EC_er', blank=True, null=True)  # Field name made lowercase.
    hdmf_er = models.FloatField(db_column='HDMF_er', blank=True, null=True)  # Field name made lowercase.
    phic_er = models.FloatField(db_column='PHIC_er', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_deductions_payroll_final'


class TblDepartment(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    dept_description = models.CharField(max_length=60, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    oic_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_department'


class TblDesignation(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    designation_description = models.CharField(max_length=60, blank=True, null=True)
    short_description = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_designation'


class TblEdtrSettings(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    login_method = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_edtr_settings'


class TblEmpCategorySub1(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    primary_code = models.BigIntegerField(blank=True, null=True)
    secondary_code = models.BigIntegerField(blank=True, null=True)
    secondary_description = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_emp_category_sub_1'


class TblEmpCategorySub2(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    primary_code = models.BigIntegerField(blank=True, null=True)
    secondary_code = models.BigIntegerField(blank=True, null=True)
    subsidiary_code = models.BigIntegerField(blank=True, null=True)
    subsidiary_description = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_emp_category_sub_2'


class TblEmpCompany(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    company_type = models.CharField(max_length=30, blank=True, null=True)
    sub_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_emp_company'


class TblEmpCompanySubtype(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_emp_company_subtype'


class TblEmpCustomerSource(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    short_desc = models.CharField(max_length=6, blank=True, null=True)
    company_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_emp_customer_source'


class TblEmpStatus(models.Model):
    autonum = models.AutoField(db_column='Autonum', primary_key=True)  # Field name made lowercase.
    stat_id = models.IntegerField(db_column='Stat_ID', blank=True, null=True)  # Field name made lowercase.
    emp_status = models.CharField(db_column='Emp_Status', max_length=30, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=100, blank=True, null=True)  # Field name made lowercase.
    holiday_prem = models.CharField(db_column='Holiday_Prem', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_emp_status'


class TblEmpTime(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=250, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=30, blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=10, db_collation='latin1_bin', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    qwerty = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_emp_time'


class TblEmpTimePass(models.Model):
    auto_no = models.AutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    timeout = models.CharField(db_column='TimeOut', max_length=20, blank=True, null=True)  # Field name made lowercase.
    timein = models.CharField(db_column='TimeIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nohours = models.FloatField(db_column='NoHours', blank=True, null=True)  # Field name made lowercase.
    status_bp = models.CharField(db_column='Status_BP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_emp_time_pass'


class TblEmpallowances(models.Model):
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    emp_id = models.CharField(db_column='Emp_ID', max_length=15)  # Field name made lowercase.
    allowance_code = models.CharField(db_column='Allowance_Code', max_length=4)  # Field name made lowercase.
    default_amount = models.FloatField(db_column='Default_Amount', blank=True, null=True)  # Field name made lowercase.
    sked_type = models.CharField(db_column='Sked_Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.SmallIntegerField(db_column='Payroll_Period', blank=True, null=True)  # Field name made lowercase.
    fixed_yn = models.CharField(db_column='Fixed_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date_entered = models.DateField(db_column='Date_Entered', blank=True, null=True)  # Field name made lowercase.
    statustype = models.CharField(db_column='StatusType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    first_qtr_month = models.CharField(db_column='First_Qtr_Month', max_length=20, blank=True, null=True)  # Field name made lowercase.
    specific_monthfrom = models.TextField(db_column='Specific_MonthFrom', blank=True, null=True)  # Field name made lowercase.
    specific_monthto = models.CharField(db_column='Specific_MonthTo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    active_stat = models.CharField(db_column='Active_stat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    auto_no = models.AutoField(primary_key=True)
    ref_no = models.CharField(max_length=20, blank=True, null=True)
    dtr_base = models.CharField(db_column='DTR_base', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_empallowances'


class TblEmpcc(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', primary_key=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    cc_code = models.FloatField(db_column='CC_code', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ul_code = models.FloatField(blank=True, null=True)
    percentage = models.FloatField(db_column='Percentage', blank=True, null=True)  # Field name made lowercase.
    acct_title = models.CharField(db_column='Acct_title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    event_name = models.CharField(db_column='Event_name', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_empcc'


class TblEmpdeductions(models.Model):
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    emp_id = models.CharField(db_column='Emp_ID', max_length=15)  # Field name made lowercase.
    deduction_code = models.CharField(db_column='Deduction_Code', max_length=4)  # Field name made lowercase.
    default_amount = models.FloatField(db_column='Default_Amount', blank=True, null=True)  # Field name made lowercase.
    sked_type = models.CharField(db_column='Sked_Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    payroll_periodno = models.SmallIntegerField(db_column='Payroll_PeriodNo', blank=True, null=True)  # Field name made lowercase.
    fixed_yn = models.CharField(db_column='Fixed_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date_entered = models.DateField(db_column='Date_Entered', blank=True, null=True)  # Field name made lowercase.
    statustype = models.CharField(db_column='StatusType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    first_qtr_month = models.CharField(db_column='First_Qtr_Month', max_length=20, blank=True, null=True)  # Field name made lowercase.
    specific_monthfrom = models.TextField(db_column='Specific_MonthFrom', blank=True, null=True)  # Field name made lowercase.
    specific_monthto = models.CharField(db_column='Specific_MonthTo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    active_stat = models.CharField(db_column='Active_stat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    auto_no = models.AutoField(primary_key=True)
    ref_no = models.CharField(max_length=20, blank=True, null=True)
    effectivefrom = models.DateField(db_column='EffectiveFrom', blank=True, null=True)  # Field name made lowercase.
    effectiveto = models.DateField(db_column='EffectiveTo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_empdeductions'


class TblEmpdeductionsSetup(models.Model):
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    emp_id = models.CharField(db_column='Emp_ID', max_length=15)  # Field name made lowercase.
    deduction_code = models.CharField(db_column='Deduction_Code', max_length=4)  # Field name made lowercase.
    default_amount = models.FloatField(db_column='Default_Amount', blank=True, null=True)  # Field name made lowercase.
    sked_type = models.CharField(db_column='Sked_Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    payroll_periodno = models.SmallIntegerField(db_column='Payroll_PeriodNo', blank=True, null=True)  # Field name made lowercase.
    fixed_yn = models.CharField(db_column='Fixed_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date_entered = models.DateField(db_column='Date_Entered', blank=True, null=True)  # Field name made lowercase.
    statustype = models.CharField(db_column='StatusType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    first_qtr_month = models.CharField(db_column='First_Qtr_Month', max_length=20, blank=True, null=True)  # Field name made lowercase.
    specific_monthfrom = models.CharField(db_column='Specific_MonthFrom', max_length=20, blank=True, null=True)  # Field name made lowercase.
    specific_monthto = models.CharField(db_column='Specific_MonthTo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    employee_list = models.CharField(db_column='Employee_list', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_empdeductions_setup'


class TblEmpdedwidemprshare(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', primary_key=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_code', max_length=20, blank=True, null=True)  # Field name made lowercase.
    store_code = models.IntegerField(db_column='Store_code', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_Id', blank=True, null=True)  # Field name made lowercase.
    ded_code = models.FloatField(db_column='Ded_code', blank=True, null=True)  # Field name made lowercase.
    emp_share = models.FloatField(db_column='Emp_share', blank=True, null=True)  # Field name made lowercase.
    empr_share = models.FloatField(db_column='Empr_share', blank=True, null=True)  # Field name made lowercase.
    base_on = models.CharField(db_column='Base_on', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pay_period_no = models.FloatField(db_column='Pay_Period_no', blank=True, null=True)  # Field name made lowercase.
    pay_outsched = models.CharField(db_column='Pay_outSched', max_length=30, blank=True, null=True)  # Field name made lowercase.
    user_in = models.CharField(db_column='User_in', max_length=60, blank=True, null=True)  # Field name made lowercase.
    date_enter = models.DateField(db_column='Date_enter', blank=True, null=True)  # Field name made lowercase.
    active_stat = models.CharField(db_column='Active_stat', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fixed_yn = models.CharField(db_column='Fixed_YN', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_empdedwidemprshare'


class TblEmpdependents(models.Model):
    auto_no = models.AutoField(unique=True)
    emp_id = models.FloatField(db_column='Emp_ID', blank=True, null=True)  # Field name made lowercase.
    relationship = models.CharField(db_column='Relationship', max_length=50, blank=True, null=True)  # Field name made lowercase.
    full_name = models.CharField(db_column='Full_Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    date_birth = models.DateField(db_column='Date_birth', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_empdependents'


class TblEmpdtr(models.Model):
    auto_no = models.BigAutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    emp_id = models.CharField(db_column='Emp_ID', max_length=15)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    timein_1 = models.CharField(db_column='TIMEIN_1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mt1 = models.SmallIntegerField(db_column='MT1', blank=True, null=True)  # Field name made lowercase.
    tt1 = models.SmallIntegerField(db_column='TT1', blank=True, null=True)  # Field name made lowercase.
    timeout_1 = models.CharField(db_column='TIMEOUT_1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mt2 = models.SmallIntegerField(db_column='MT2', blank=True, null=True)  # Field name made lowercase.
    tt2 = models.SmallIntegerField(db_column='TT2', blank=True, null=True)  # Field name made lowercase.
    timein_2 = models.CharField(db_column='TIMEIN_2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mt3 = models.SmallIntegerField(db_column='MT3', blank=True, null=True)  # Field name made lowercase.
    tt3 = models.SmallIntegerField(db_column='TT3', blank=True, null=True)  # Field name made lowercase.
    timeout_2 = models.CharField(db_column='TIMEOUT_2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mt4 = models.SmallIntegerField(db_column='MT4', blank=True, null=True)  # Field name made lowercase.
    tt4 = models.SmallIntegerField(db_column='TT4', blank=True, null=True)  # Field name made lowercase.
    snackin = models.CharField(db_column='SnackIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    snackout = models.CharField(db_column='SnackOut', max_length=20, blank=True, null=True)  # Field name made lowercase.
    overtimein = models.CharField(db_column='OvertimeIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mt5 = models.SmallIntegerField(db_column='MT5', blank=True, null=True)  # Field name made lowercase.
    tt5 = models.SmallIntegerField(db_column='TT5', blank=True, null=True)  # Field name made lowercase.
    overtimeout = models.CharField(db_column='OvertimeOut', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mt6 = models.SmallIntegerField(db_column='MT6', blank=True, null=True)  # Field name made lowercase.
    tt6 = models.SmallIntegerField(db_column='TT6', blank=True, null=True)  # Field name made lowercase.
    manualtype = models.SmallIntegerField(db_column='ManualType', blank=True, null=True)  # Field name made lowercase.
    timein_type = models.SmallIntegerField(db_column='TimeIn_Type', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50, blank=True, null=True)  # Field name made lowercase.
    commit = models.SmallIntegerField(db_column='Commit', blank=True, null=True)  # Field name made lowercase.
    approved = models.CharField(db_column='Approved', max_length=10, blank=True, null=True)  # Field name made lowercase.
    shiftsched = models.FloatField(db_column='ShiftSched', blank=True, null=True)  # Field name made lowercase.
    cc1 = models.SmallIntegerField(db_column='CC1', blank=True, null=True)  # Field name made lowercase.
    cc2 = models.SmallIntegerField(db_column='CC2', blank=True, null=True)  # Field name made lowercase.
    cc3 = models.SmallIntegerField(db_column='CC3', blank=True, null=True)  # Field name made lowercase.
    cc4 = models.SmallIntegerField(db_column='CC4', blank=True, null=True)  # Field name made lowercase.
    cc5 = models.SmallIntegerField(db_column='CC5', blank=True, null=True)  # Field name made lowercase.
    cc6 = models.SmallIntegerField(db_column='CC6', blank=True, null=True)  # Field name made lowercase.
    cc7 = models.SmallIntegerField(db_column='CC7', blank=True, null=True)  # Field name made lowercase.
    cc8 = models.SmallIntegerField(db_column='CC8', blank=True, null=True)  # Field name made lowercase.
    flag_stat = models.CharField(max_length=30, blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)
    sync_status_server5 = models.CharField(max_length=4, blank=True, null=True)
    sync_status_server4 = models.CharField(max_length=4, blank=True, null=True)
    sync_status_server3 = models.CharField(max_length=4, blank=True, null=True)
    sync_status_server2 = models.CharField(max_length=4, blank=True, null=True)
    sync_status_server1 = models.CharField(max_length=4, blank=True, null=True)
    sync_created_server1 = models.CharField(max_length=50, blank=True, null=True)
    sync_created_server2 = models.CharField(max_length=50, blank=True, null=True)
    sync_created_server3 = models.CharField(max_length=50, blank=True, null=True)
    sync_created_server4 = models.CharField(max_length=50, blank=True, null=True)
    sync_created_server5 = models.CharField(max_length=50, blank=True, null=True)
    sync_created = models.CharField(max_length=50, blank=True, null=True)
    sync_status = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_empdtr'


class TblEmpfinger(models.Model):
    auto_no = models.BigAutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    emp_id = models.IntegerField(db_column='Emp_ID', unique=True, blank=True, null=True)  # Field name made lowercase.
    finger_primary = models.TextField(db_column='Finger_Primary', blank=True, null=True)  # Field name made lowercase.
    finger_secondary = models.TextField(db_column='Finger_Secondary', blank=True, null=True)  # Field name made lowercase.
    primary_hand = models.CharField(max_length=50, blank=True, null=True)
    secondary_hand = models.CharField(max_length=50, blank=True, null=True)
    primary_finger_index = models.CharField(max_length=50, blank=True, null=True)
    secondary_finger_index = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_empfinger'


class TblEmpleave(models.Model):
    auto_no = models.AutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2, blank=True, null=True)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.IntegerField(db_column='Emp_ID')  # Field name made lowercase.
    emp_name = models.CharField(db_column='Emp_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    period_from = models.DateField(db_column='Period_From')  # Field name made lowercase.
    period_to = models.DateField(db_column='Period_To')  # Field name made lowercase.
    date_added = models.DateField(db_column='Date_Added', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=2)  # Field name made lowercase.
    leaveearn = models.FloatField(db_column='LeaveEarn', blank=True, null=True)  # Field name made lowercase.
    leave_ava = models.FloatField(db_column='Leave_Ava', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_empleave'
        unique_together = (('emp_id', 'period_from', 'period_to', 'type'),)


class TblEmpleavetrans(models.Model):
    auto_no = models.AutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    leave_id = models.IntegerField(db_column='Leave_ID', blank=True, null=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.IntegerField(db_column='Emp_ID')  # Field name made lowercase.
    emp_name = models.CharField(db_column='Emp_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    date_from = models.DateField(db_column='Date_From')  # Field name made lowercase.
    date_to = models.DateField(db_column='Date_To')  # Field name made lowercase.
    no_days = models.FloatField(db_column='No_Days', blank=True, null=True)  # Field name made lowercase.
    available_leave = models.FloatField(db_column='Available_Leave', blank=True, null=True)  # Field name made lowercase.
    approve_creditleave = models.FloatField(db_column='Approve_CreditLeave', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=2)  # Field name made lowercase.
    date_trans = models.DateField(db_column='Date_Trans', blank=True, null=True)  # Field name made lowercase.
    date_updated = models.DateField(db_column='Date_Updated', blank=True, null=True)  # Field name made lowercase.
    approved_by = models.CharField(db_column='Approved_By', max_length=50, blank=True, null=True)  # Field name made lowercase.
    noted_by = models.CharField(db_column='Noted_By', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status_action = models.CharField(db_column='Status_Action', max_length=50, blank=True, null=True)  # Field name made lowercase.
    action_reason = models.CharField(db_column='Action_Reason', max_length=50, blank=True, null=True)  # Field name made lowercase.
    time_frm = models.CharField(max_length=30, blank=True, null=True)
    time_to = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_empleavetrans'


class TblEmploans(models.Model):
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    emp_id = models.CharField(db_column='Emp_ID', max_length=15)  # Field name made lowercase.
    date_loan = models.DateField(db_column='Date_Loan')  # Field name made lowercase.
    type_of_loan = models.CharField(db_column='Type_of_Loan', max_length=30)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gross_amount = models.FloatField(db_column='Gross_Amount', blank=True, null=True)  # Field name made lowercase.
    monthly_amort = models.FloatField(db_column='Monthly_Amort', blank=True, null=True)  # Field name made lowercase.
    no_of_months = models.SmallIntegerField(db_column='No_of_Months', blank=True, null=True)  # Field name made lowercase.
    first_due_date = models.DateField(db_column='First_Due_Date', blank=True, null=True)  # Field name made lowercase.
    last_due_date = models.DateField(db_column='Last_Due_Date', blank=True, null=True)  # Field name made lowercase.
    balance = models.FloatField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    payperiod = models.CharField(db_column='PayPeriod', max_length=20, blank=True, null=True)  # Field name made lowercase.
    active_stat = models.CharField(db_column='Active_stat', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_emploans'


class TblEmploansdue(models.Model):
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    emp_id = models.CharField(db_column='Emp_ID', max_length=15)  # Field name made lowercase.
    date_loan = models.DateField(db_column='Date_Loan')  # Field name made lowercase.
    type_of_loan = models.CharField(db_column='Type_of_Loan', max_length=30)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=15, blank=True, null=True)  # Field name made lowercase.
    due_date = models.DateField(db_column='Due_Date', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    date_paid = models.DateField(db_column='Date_Paid', blank=True, null=True)  # Field name made lowercase.
    amount_paid = models.FloatField(db_column='Amount_Paid', blank=True, null=True)  # Field name made lowercase.
    reference_or = models.CharField(db_column='Reference_OR', max_length=20, db_collation='latin1_bin', blank=True, null=True)  # Field name made lowercase.
    balance = models.FloatField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    auto_no = models.AutoField(db_column='Auto_no', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_emploansdue'


class TblEmployee(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.IntegerField()
    emp_id = models.IntegerField(db_column='Emp_ID', blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(max_length=55, blank=True, null=True)
    first_name = models.CharField(max_length=55, blank=True, null=True)
    middle_name = models.CharField(max_length=55, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=75, blank=True, null=True)
    home_phone_no = models.CharField(max_length=15, blank=True, null=True)
    mobile_no = models.CharField(max_length=25, blank=True, null=True)
    fax_no = models.CharField(max_length=15, blank=True, null=True)
    st_address = models.CharField(max_length=60, blank=True, null=True)
    city_address = models.CharField(max_length=30, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    date_as_of = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    active = models.CharField(max_length=5, blank=True, null=True)
    employee_image = models.TextField(blank=True, null=True)
    date_entered = models.DateField(blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    manual_yn = models.CharField(db_column='Manual_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    schedule = models.IntegerField(blank=True, null=True)
    civil_stat = models.CharField(db_column='Civil_stat', max_length=15, blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=5, blank=True, null=True)  # Field name made lowercase.
    finger_id = models.CharField(db_column='Finger_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    auto_filldtr = models.CharField(db_column='Auto_FillDTR', max_length=5, blank=True, null=True)  # Field name made lowercase.
    basic_comp = models.CharField(db_column='Basic_Comp', max_length=1, blank=True, null=True)  # Field name made lowercase.
    perjob_comp = models.CharField(db_column='PerJob_Comp', max_length=1, blank=True, null=True)  # Field name made lowercase.
    acct_no = models.CharField(db_column='Acct_no', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paid_lunch = models.CharField(db_column='Paid_Lunch', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sss_chk = models.CharField(db_column='SSS_chk', max_length=5, blank=True, null=True)  # Field name made lowercase.
    phic_chk = models.CharField(db_column='PHIC_chk', max_length=5, blank=True, null=True)  # Field name made lowercase.
    hdmf_chk = models.CharField(db_column='HDMF_chk', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tax_chk = models.CharField(db_column='Tax_chk', max_length=5, blank=True, null=True)  # Field name made lowercase.
    release_type = models.CharField(db_column='Release_type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    flexibreak = models.CharField(db_column='FlexiBreak', max_length=5, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, blank=True, null=True)  # Field name made lowercase.
    responsibility_center_code = models.CharField(max_length=11, blank=True, null=True)
    responsibility_center = models.CharField(max_length=250, blank=True, null=True)
    desc_department = models.CharField(max_length=999, blank=True, null=True)
    tax_exemption = models.CharField(max_length=50, blank=True, null=True)
    cola = models.CharField(max_length=1, blank=True, null=True)
    cola_taxable = models.CharField(max_length=1, blank=True, null=True)
    cola_based_on_dtr = models.CharField(max_length=1, blank=True, null=True)
    cola_amount = models.CharField(max_length=999, blank=True, null=True)
    fixed_schedule = models.CharField(max_length=2, blank=True, null=True)
    emp_status = models.CharField(max_length=50, blank=True, null=True)
    date_fired = models.CharField(max_length=50, blank=True, null=True)
    bir_schedule = models.CharField(max_length=10, blank=True, null=True)
    dtr_rotation_id = models.CharField(max_length=20, blank=True, null=True)
    am_only = models.CharField(max_length=2, blank=True, null=True)
    pm_only = models.CharField(max_length=2, blank=True, null=True)
    salary_type = models.CharField(max_length=25, blank=True, null=True)
    restday = models.CharField(db_column='RestDay', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flexitime = models.CharField(db_column='FlexiTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flexifirstin = models.CharField(db_column='FlexifirstIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flexifirstout = models.CharField(db_column='FlexifirstOUT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flexisecondin = models.CharField(db_column='FlexisecondIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flexisecondout = models.CharField(db_column='FlexisecondOUT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flexithirdin = models.CharField(db_column='FlexithirdIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    flexithirdout = models.CharField(db_column='FlexithirdOUT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sl_category = models.CharField(max_length=50, blank=True, null=True)
    edtr = models.CharField(db_column='EDTR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dtar = models.CharField(db_column='DTAR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mdtr = models.CharField(db_column='MDTR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mdtr_type = models.CharField(db_column='MDTR_TYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    unworkedholidaypay = models.CharField(db_column='UnworkedHolidayPay', max_length=2, blank=True, null=True)  # Field name made lowercase.
    unworkedholidayrestdaypay = models.CharField(db_column='UnworkedHolidayRestDayPay', max_length=2, blank=True, null=True)  # Field name made lowercase.
    locale = models.CharField(db_column='Locale', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nogrosspay = models.CharField(db_column='NoGrossPay', max_length=2, blank=True, null=True)  # Field name made lowercase.
    noholidaypay = models.CharField(db_column='NoHolidayPay', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nootpay = models.CharField(db_column='NoOTPay', max_length=2, blank=True, null=True)  # Field name made lowercase.
    otwopay = models.CharField(db_column='OTwOPay', max_length=4, blank=True, null=True)  # Field name made lowercase.
    min_take_home_pay = models.FloatField(blank=True, null=True)
    include_payroll = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_employee'
        unique_together = (('id_code', 'last_name', 'first_name', 'middle_name'),)


class TblEmployeeOtherInfo(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.IntegerField()
    last_name = models.CharField(max_length=55, blank=True, null=True)
    first_name = models.CharField(max_length=55, blank=True, null=True)
    middle_name = models.CharField(max_length=55, blank=True, null=True)
    sss_no = models.CharField(max_length=15, blank=True, null=True)
    phic_no = models.CharField(max_length=15, blank=True, null=True)
    hdmf_no = models.CharField(max_length=15, blank=True, null=True)
    tax_id_no = models.CharField(max_length=15, blank=True, null=True)
    blood_type = models.CharField(max_length=10, blank=True, null=True)
    salary_rate = models.FloatField(blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    emp_status = models.CharField(max_length=1, blank=True, null=True)
    date_hired = models.DateField(blank=True, null=True)
    date_fired = models.DateField(blank=True, null=True)
    case_contact_person = models.CharField(max_length=40, blank=True, null=True)
    relationship = models.CharField(max_length=15, blank=True, null=True)
    bir_schedule = models.CharField(max_length=10, blank=True, null=True)
    cola = models.FloatField(db_column='COLA', blank=True, null=True)  # Field name made lowercase.
    spouse_bday = models.CharField(max_length=20, blank=True, null=True)
    estatus = models.FloatField(db_column='Estatus', blank=True, null=True)  # Field name made lowercase.
    salary_type = models.CharField(db_column='Salary_type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    no_days = models.FloatField(db_column='No_days', blank=True, null=True)  # Field name made lowercase.
    daily_rate = models.FloatField(db_column='Daily_rate', blank=True, null=True)  # Field name made lowercase.
    e_phoneno = models.CharField(db_column='E_phoneNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    e_mobileno = models.CharField(db_column='E_mobileNo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    e_faxno = models.CharField(db_column='E_FaxNo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    e_street = models.CharField(db_column='E_street', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e_citymunicipal = models.CharField(db_column='E_CityMunicipal', max_length=30, blank=True, null=True)  # Field name made lowercase.
    e_zipcode = models.CharField(db_column='E_ZipCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    tax_exempt = models.CharField(max_length=20, blank=True, null=True)
    monthly_daily = models.FloatField(db_column='Monthly_Daily', blank=True, null=True)  # Field name made lowercase.
    payment_scheme = models.CharField(db_column='Payment_Scheme', max_length=20, blank=True, null=True)  # Field name made lowercase.
    provadd = models.CharField(db_column='ProvAdd', max_length=300, blank=True, null=True)  # Field name made lowercase.
    spouse_name = models.CharField(db_column='Spouse_name', max_length=80, blank=True, null=True)  # Field name made lowercase.
    spouse_addrss = models.CharField(db_column='Spouse_addrss', max_length=100, blank=True, null=True)  # Field name made lowercase.
    marriage_date = models.CharField(db_column='Marriage_date', max_length=20, blank=True, null=True)  # Field name made lowercase.
    spouse_occup = models.CharField(db_column='Spouse_occup', max_length=80, blank=True, null=True)  # Field name made lowercase.
    fathers_name = models.CharField(db_column='Fathers_name', max_length=80, blank=True, null=True)  # Field name made lowercase.
    mothers_name = models.CharField(db_column='Mothers_name', max_length=80, blank=True, null=True)  # Field name made lowercase.
    fathers_addrss = models.CharField(max_length=100, blank=True, null=True)
    mothers_addrss = models.CharField(max_length=100, blank=True, null=True)
    fathers_contact = models.CharField(max_length=30, blank=True, null=True)
    mothers_contact = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_employee_other_info'
        unique_together = (('id_code', 'last_name', 'first_name', 'middle_name'),)


class TblEmploymentrecord(models.Model):
    auto_no = models.FloatField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_code', max_length=3, blank=True, null=True)  # Field name made lowercase.
    store_code = models.FloatField(db_column='Store_code', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.CharField(db_column='Emp_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    employer_name = models.CharField(max_length=50, blank=True, null=True)
    position_assigned = models.CharField(db_column='Position_assigned', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emp_status = models.CharField(max_length=20, blank=True, null=True)
    date_from = models.CharField(db_column='Date_From', max_length=30, blank=True, null=True)  # Field name made lowercase.
    date_to = models.CharField(db_column='Date_To', max_length=30, blank=True, null=True)  # Field name made lowercase.
    manual_auto = models.CharField(db_column='Manual_auto', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_employmentrecord'


class TblEmppayrollDtrFinal(models.Model):
    company_code = models.IntegerField(blank=True, null=True)
    store_code = models.IntegerField(blank=True, null=True)
    emp_id = models.FloatField(primary_key=True)  # The composite primary key (emp_id, Payroll_period) found, that is not supported. The first column is selected.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=30)  # Field name made lowercase.
    daily_rate = models.FloatField(db_column='Daily_rate', blank=True, null=True)  # Field name made lowercase.
    per_hour = models.FloatField(db_column='Per_hour', blank=True, null=True)  # Field name made lowercase.
    reg_hrs = models.FloatField(db_column='Reg_hrs', blank=True, null=True)  # Field name made lowercase.
    ot_hrs = models.FloatField(db_column='OT_hrs', blank=True, null=True)  # Field name made lowercase.
    holiday_hrs = models.FloatField(blank=True, null=True)
    special_hrs = models.FloatField(blank=True, null=True)
    nsd_hrs = models.FloatField(db_column='NSD_hrs', blank=True, null=True)  # Field name made lowercase.
    absent_hrs = models.FloatField(db_column='Absent_hrs', blank=True, null=True)  # Field name made lowercase.
    reg_pay = models.FloatField(db_column='Reg_pay', blank=True, null=True)  # Field name made lowercase.
    ot_pay = models.FloatField(db_column='OT_pay', blank=True, null=True)  # Field name made lowercase.
    holiday_pay = models.FloatField(db_column='Holiday_pay', blank=True, null=True)  # Field name made lowercase.
    special_pay = models.FloatField(db_column='Special_pay', blank=True, null=True)  # Field name made lowercase.
    nsd_pay = models.FloatField(db_column='NSD_pay', blank=True, null=True)  # Field name made lowercase.
    deduct_absent = models.FloatField(db_column='Deduct_absent', blank=True, null=True)  # Field name made lowercase.
    gross_income = models.FloatField(db_column='Gross_income', blank=True, null=True)  # Field name made lowercase.
    salary_type = models.CharField(db_column='Salary_type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    monthly_salary = models.FloatField(db_column='Monthly_salary', blank=True, null=True)  # Field name made lowercase.
    payroll_details = models.CharField(db_column='Payroll_details', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    payroll_summary = models.CharField(db_column='Payroll_summary', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    dep_id = models.FloatField(db_column='Dep_id', blank=True, null=True)  # Field name made lowercase.
    other_income = models.FloatField(db_column='Other_income', blank=True, null=True)  # Field name made lowercase.
    t_cola = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_emppayroll_dtr_final'
        unique_together = (('emp_id', 'payroll_period'),)


class TblEmppayrollDtrbkup(models.Model):
    company_code = models.IntegerField(blank=True, null=True)
    store_code = models.IntegerField(blank=True, null=True)
    emp_id = models.FloatField(primary_key=True)  # The composite primary key (emp_id, Payroll_period) found, that is not supported. The first column is selected.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=30)  # Field name made lowercase.
    daily_rate = models.FloatField(blank=True, null=True)
    per_hour = models.FloatField(db_column='Per_hour', blank=True, null=True)  # Field name made lowercase.
    reg_hrs = models.FloatField(db_column='Reg_hrs', blank=True, null=True)  # Field name made lowercase.
    ot_hrs = models.FloatField(db_column='OT_hrs', blank=True, null=True)  # Field name made lowercase.
    holiday_hrs = models.FloatField(blank=True, null=True)
    special_hrs = models.FloatField(blank=True, null=True)
    nsd_hrs = models.FloatField(db_column='NSD_hrs', blank=True, null=True)  # Field name made lowercase.
    absent_hrs = models.FloatField(db_column='Absent_hrs', blank=True, null=True)  # Field name made lowercase.
    reg_pay = models.FloatField(db_column='Reg_pay', blank=True, null=True)  # Field name made lowercase.
    ot_pay = models.FloatField(db_column='OT_pay', blank=True, null=True)  # Field name made lowercase.
    holiday_pay = models.FloatField(db_column='Holiday_pay', blank=True, null=True)  # Field name made lowercase.
    special_pay = models.FloatField(db_column='Special_pay', blank=True, null=True)  # Field name made lowercase.
    nsd_pay = models.FloatField(db_column='NSD_pay', blank=True, null=True)  # Field name made lowercase.
    deduct_absent = models.FloatField(db_column='Deduct_absent', blank=True, null=True)  # Field name made lowercase.
    gross_income = models.FloatField(db_column='Gross_income', blank=True, null=True)  # Field name made lowercase.
    salary_type = models.CharField(db_column='Salary_type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    monthly_salary = models.FloatField(db_column='Monthly_salary', blank=True, null=True)  # Field name made lowercase.
    payroll_details = models.CharField(db_column='Payroll_details', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    payroll_summary = models.CharField(db_column='Payroll_summary', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    dep_id = models.FloatField(db_column='Dep_id', blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=5, blank=True, null=True)  # Field name made lowercase.
    other_income = models.FloatField(blank=True, null=True)
    paid_leave_hrs = models.FloatField(db_column='Paid_leave_hrs', blank=True, null=True)  # Field name made lowercase.
    absentlatewopay_hrs = models.FloatField(db_column='AbsentLateWOPay_hrs', blank=True, null=True)  # Field name made lowercase.
    total_regworking_hrs = models.FloatField(db_column='Total_RegWorking_hrs', blank=True, null=True)  # Field name made lowercase.
    ot_hrs_leg_hrs = models.FloatField(db_column='OT_hrs_Leg_hrs', blank=True, null=True)  # Field name made lowercase.
    ot_hrs_spec_hrs = models.FloatField(db_column='Ot_hrs_Spec_hrs', blank=True, null=True)  # Field name made lowercase.
    ot_dayoleg_hrs = models.FloatField(db_column='OT_DayOLeg_hrs', blank=True, null=True)  # Field name made lowercase.
    ot_dayospec_hrs = models.FloatField(db_column='OT_DayOSpec_hrs', blank=True, null=True)  # Field name made lowercase.
    ot_dayoff = models.FloatField(db_column='OT_dayOff', blank=True, null=True)  # Field name made lowercase.
    dayo_leg_hrs = models.FloatField(db_column='DayO_leg_hrs', blank=True, null=True)  # Field name made lowercase.
    dayo_spec_hrs = models.FloatField(db_column='DayO_spec_hrs', blank=True, null=True)  # Field name made lowercase.
    dayo_hrs = models.FloatField(db_column='DayO_hrs', blank=True, null=True)  # Field name made lowercase.
    nsd_leg_hrs = models.FloatField(db_column='NSD_leg_hrs', blank=True, null=True)  # Field name made lowercase.
    nsd_spec_hrs = models.FloatField(db_column='NSD_Spec_hrs', blank=True, null=True)  # Field name made lowercase.
    nsddayo_leg_hrs = models.FloatField(db_column='NSDDayO_leg_hrs', blank=True, null=True)  # Field name made lowercase.
    nsddayo_spec_hrs = models.FloatField(db_column='NSDDayO_spec_hrs', blank=True, null=True)  # Field name made lowercase.
    nsddayoff_hrs = models.FloatField(db_column='NSDDayOff_hrs', blank=True, null=True)  # Field name made lowercase.
    t_cola = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_emppayroll_dtrbkup'
        unique_together = (('emp_id', 'payroll_period'),)


class TblEmpshiftsked(models.Model):
    auto_no = models.BigAutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    emp_id = models.IntegerField(db_column='Emp_ID')  # Field name made lowercase.
    payroll_period = models.IntegerField(db_column='Payroll_Period')  # Field name made lowercase.
    date_trans = models.DateField(db_column='Date_Trans')  # Field name made lowercase.
    shift_code = models.IntegerField(db_column='Shift_Code')  # Field name made lowercase.
    shift_name = models.CharField(db_column='Shift_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    restday = models.IntegerField(db_column='Restday', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_empshiftsked'


class TblEmpshiftskedpresetup(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    payrollperiod = models.CharField(db_column='PayrollPeriod', max_length=30, blank=True, null=True)  # Field name made lowercase.
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    shift_code = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    rest_day = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_empshiftskedpresetup'


class TblEmptimecharges(models.Model):
    auto_no = models.BigAutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    emp_id = models.IntegerField(db_column='Emp_ID')  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=999, blank=True, null=True)  # Field name made lowercase.
    period = models.IntegerField(db_column='Period')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    charged_to = models.CharField(db_column='Charged_To', max_length=999, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=999, blank=True, null=True)  # Field name made lowercase.
    no_hours = models.FloatField(db_column='No_Hours', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=250)  # Field name made lowercase.
    date_entry = models.DateField(db_column='Date_Entry', blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='categoryID', blank=True, null=True)  # Field name made lowercase.
    cat_sub1_id = models.IntegerField(db_column='cat_sub1_ID', blank=True, null=True)  # Field name made lowercase.
    cat_sub2_id = models.IntegerField(db_column='cat_sub2_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_emptimecharges'


class TblExpire(models.Model):
    date_expire = models.CharField(max_length=20, blank=True, null=True)
    expire_yn = models.CharField(max_length=1, blank=True, null=True)
    sys_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_expire'


class TblGeneralLedger(models.Model):
    autonum = models.AutoField(primary_key=True)
    ul_code = models.SmallIntegerField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    reference_no = models.CharField(max_length=20, blank=True, null=True)
    doc_ref = models.FloatField(blank=True, null=True)
    acct_code = models.FloatField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    balance_as_of = models.FloatField(blank=True, null=True)
    beginning_bal = models.FloatField(blank=True, null=True)
    transtype = models.CharField(db_column='TransType', max_length=150, blank=True, null=True)  # Field name made lowercase.
    autonum_trans = models.BigIntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_general_ledger'
        unique_together = (('autonum', 'date_trans', 'reference_no', 'acct_title'),)


class TblGlClosingRoutine(models.Model):
    autonum = models.AutoField(primary_key=True)
    module = models.CharField(max_length=10, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    date_time = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_gl_closing_routine'


class TblGlDocType(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=15, blank=True, null=True)
    doc_name = models.CharField(max_length=50, blank=True, null=True)
    active = models.CharField(max_length=20, blank=True, null=True)
    restricted = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_gl_doc_type'


class TblGlDocTypeAcctTitle(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    doc_type = models.CharField(max_length=50, blank=True, null=True)
    doc_name = models.CharField(max_length=50, blank=True, null=True)
    acct_code = models.CharField(max_length=11, blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_gl_doc_type_acct_title'
        unique_together = (('doc_type', 'doc_name'),)


class TblGlReport(models.Model):
    autonum = models.AutoField(primary_key=True)
    terminal_no = models.PositiveIntegerField()
    date_trans = models.CharField(max_length=20)
    particulars = models.CharField(max_length=75)
    debit = models.FloatField(blank=True, null=True)
    credit = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    acct_code = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_gl_report'


class TblGrpallowances(models.Model):
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    employee = models.TextField(db_column='Employee', blank=True, null=True)  # Field name made lowercase.
    allowance_code = models.CharField(db_column='Allowance_Code', max_length=4)  # Field name made lowercase.
    default_amount = models.FloatField(db_column='Default_Amount', blank=True, null=True)  # Field name made lowercase.
    sked_type = models.CharField(db_column='Sked_Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.SmallIntegerField(db_column='Payroll_Period', blank=True, null=True)  # Field name made lowercase.
    fixed_yn = models.CharField(db_column='Fixed_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='User_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date_entered = models.DateField(db_column='Date_Entered', blank=True, null=True)  # Field name made lowercase.
    statustype = models.CharField(db_column='StatusType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    first_qtr_month = models.CharField(db_column='First_Qtr_Month', max_length=20, blank=True, null=True)  # Field name made lowercase.
    specific_monthfrom = models.CharField(db_column='Specific_MonthFrom', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    specific_monthto = models.CharField(db_column='Specific_MonthTo', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    deptid = models.FloatField(db_column='DeptID', blank=True, null=True)  # Field name made lowercase.
    positionid = models.FloatField(db_column='PositionID', blank=True, null=True)  # Field name made lowercase.
    payment_scheme = models.CharField(db_column='Payment_Scheme', max_length=20, blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reference_no = models.CharField(max_length=20, blank=True, null=True)
    same_amount = models.CharField(db_column='Same_amount', max_length=5, blank=True, null=True)  # Field name made lowercase.
    emp_stat = models.IntegerField(db_column='Emp_stat', blank=True, null=True)  # Field name made lowercase.
    effective_from = models.CharField(db_column='Effective_from', max_length=30, blank=True, null=True)  # Field name made lowercase.
    effective_to = models.CharField(db_column='Effective_to', max_length=30, blank=True, null=True)  # Field name made lowercase.
    auto_no = models.CharField(db_column='Auto_no', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_grpallowances'


class TblGuarantor(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.PositiveIntegerField()
    trade_name = models.CharField(max_length=150, blank=True, null=True)
    guarantor_class = models.CharField(max_length=15, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    business_phone_no = models.CharField(max_length=15, blank=True, null=True)
    mobile_no = models.CharField(max_length=15, blank=True, null=True)
    fax_no = models.CharField(max_length=15, blank=True, null=True)
    st_address = models.CharField(max_length=60, blank=True, null=True)
    city_address = models.CharField(max_length=30, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    bir_reg_no = models.CharField(max_length=25, blank=True, null=True)
    tax_id_no = models.IntegerField(blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    guarantor_image = models.TextField(blank=True, null=True)
    date_entered = models.DateField(blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_guarantor'
        unique_together = (('id_code', 'trade_name', 'last_name', 'first_name', 'middle_name'),)


class TblHdmfCont(models.Model):
    salary_bracket = models.IntegerField(blank=True, null=True)
    checked = models.CharField(max_length=1, blank=True, null=True)
    salary_from = models.FloatField(blank=True, null=True)
    salary_to = models.FloatField(blank=True, null=True)
    base_salary = models.FloatField(blank=True, null=True)
    total_mpremium = models.FloatField(blank=True, null=True)
    employee_share = models.FloatField(blank=True, null=True)
    employer_share = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_hdmf_cont'


class TblHrmisSystemSetting(models.Model):
    auto_no = models.AutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    id_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_hrmis_system_setting'


class TblImage(models.Model):
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_image'


class TblInvRefNo(models.Model):
    autonum = models.AutoField(primary_key=True)
    description = models.CharField(max_length=25, blank=True, null=True)
    next_no = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_inv_ref_no'


class TblIsClosingRoutine(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    module = models.CharField(max_length=100, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    date_time = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.CharField(max_length=150, blank=True, null=True)
    mod_desc = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_is_closing_routine'


class TblJoblist(models.Model):
    auto_num = models.AutoField(unique=True)
    job_code = models.IntegerField(db_column='Job_code', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=30, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    ul_code = models.IntegerField(db_column='Ul_code', blank=True, null=True)  # Field name made lowercase.
    taxable = models.CharField(db_column='Taxable', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_joblist'


class TblJvAdjustment(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    jv_no = models.FloatField(blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=100, blank=True, null=True)
    reference_no = models.FloatField(blank=True, null=True)
    reference_type = models.CharField(max_length=3, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    transaction_type = models.CharField(max_length=100, blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    acct_code = models.CharField(max_length=11, blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    ul_code_pmt = models.IntegerField(blank=True, null=True)
    date_trans_pmt = models.DateField(blank=True, null=True)
    source_module_pmt = models.CharField(max_length=3, blank=True, null=True)
    guarantor_id = models.PositiveIntegerField(blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doctype_ref = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_jv_adjustment'


class TblJvLiquidation(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    jv_no = models.FloatField(blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=100, blank=True, null=True)
    cv_no = models.FloatField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    reference_type = models.CharField(max_length=3, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_jv_liquidation'
        unique_together = (('jv_no', 'cv_no', 'reference_type'),)


class TblKob(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    kob_name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_kob'


class TblLocatorList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    trans_code = models.IntegerField(blank=True, null=True)
    date_trans = models.CharField(max_length=15, blank=True, null=True)
    payroll_period = models.CharField(max_length=50, blank=True, null=True)
    emp_id = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=60, blank=True, null=True)
    total_hours = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_locator_list'


class TblLocatorListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    trans_code = models.IntegerField(blank=True, null=True)
    locator_date = models.CharField(max_length=15, blank=True, null=True)
    emp_id = models.IntegerField(blank=True, null=True)
    type_of_transactions = models.CharField(max_length=20, blank=True, null=True)
    destination = models.CharField(max_length=50, blank=True, null=True)
    time_out = models.CharField(max_length=15, blank=True, null=True)
    time_in = models.CharField(max_length=15, blank=True, null=True)
    hours_out = models.FloatField(blank=True, null=True)
    purpose = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_locator_listing'


class TblLogs(models.Model):
    user_id = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    activity = models.CharField(max_length=150, blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    reference_no = models.CharField(max_length=100, blank=True, null=True)
    reference_type = models.CharField(max_length=50, blank=True, null=True)
    system_version = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_logs'


class TblMandatoryDeductionSettings(models.Model):
    auto_no = models.BigAutoField(primary_key=True)
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deduction_schedule = models.CharField(db_column='Deduction_Schedule', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gross_contract = models.CharField(db_column='Gross_Contract', max_length=5, blank=True, null=True)  # Field name made lowercase.
    basic_salary = models.CharField(db_column='Basic_Salary', max_length=5, blank=True, null=True)  # Field name made lowercase.
    absences = models.CharField(db_column='Absences', max_length=5, blank=True, null=True)  # Field name made lowercase.
    overtime = models.CharField(db_column='Overtime', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nsd_premiums_holiday = models.CharField(db_column='NSD_Premiums_Holiday', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cola = models.CharField(db_column='Cola', max_length=5, blank=True, null=True)  # Field name made lowercase.
    incentive_leave = models.CharField(db_column='Incentive_leave', max_length=5, blank=True, null=True)  # Field name made lowercase.
    qual_allowance = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_mandatory_deduction_settings'


class TblMandatoryDescription(models.Model):
    auto_no = models.AutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_mandatory_description'


class TblMember(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.PositiveIntegerField()
    trade_name = models.CharField(max_length=40)
    member_class = models.CharField(max_length=15, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    business_phone_no = models.CharField(max_length=15, blank=True, null=True)
    mobile_no = models.CharField(max_length=15, blank=True, null=True)
    fax_no = models.CharField(max_length=15, blank=True, null=True)
    st_address = models.CharField(max_length=60, blank=True, null=True)
    city_address = models.CharField(max_length=30, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    trade = models.CharField(max_length=1, blank=True, null=True)
    vat = models.CharField(max_length=1, blank=True, null=True)
    bir_reg_no = models.CharField(max_length=20, blank=True, null=True)
    tax_id_no = models.IntegerField(blank=True, null=True)
    credit_terms = models.SmallIntegerField(blank=True, null=True)
    credit_limit = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    date_as_of = models.DateField(blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    member_image = models.TextField(blank=True, null=True)
    date_entered = models.DateField(blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    sl_category = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_member'
        unique_together = (('id_code', 'trade_name', 'last_name', 'first_name', 'middle_name'),)


class TblModuleAccess(models.Model):
    line_number = models.PositiveBigIntegerField()
    header = models.CharField(max_length=1, blank=True, null=True)
    trans_module = models.CharField(max_length=100, blank=True, null=True)
    key_text = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_module_access'


class TblNegativeNet(models.Model):
    auto_num = models.AutoField(db_column='Auto_num', primary_key=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    payrollperiod = models.CharField(db_column='PayrollPeriod', max_length=30, blank=True, null=True)  # Field name made lowercase.
    negative_amount = models.FloatField(db_column='Negative_Amount', blank=True, null=True)  # Field name made lowercase.
    status_s = models.CharField(db_column='Status_S', max_length=10, blank=True, null=True)  # Field name made lowercase.
    applied_payperiod = models.CharField(db_column='Applied_payPeriod', max_length=30, blank=True, null=True)  # Field name made lowercase.
    date_create = models.DateField(db_column='Date_create', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_negative_net'


class TblNumberGenerator(models.Model):
    autonum = models.AutoField(primary_key=True)
    description = models.CharField(max_length=25, blank=True, null=True)
    next_no = models.FloatField(blank=True, null=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_number_generator'


class TblOffsettingTrans(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_acct = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    acct_code = models.CharField(max_length=15, blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    module_name = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_offsetting_trans'


class TblOtherAcct(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.PositiveSmallIntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=150, blank=True, null=True)
    trade_name = models.CharField(max_length=100, blank=True, null=True)
    abbr = models.CharField(max_length=10, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    code = models.CharField(max_length=75, blank=True, null=True)
    acct_title = models.CharField(max_length=100, blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    date_as_of = models.DateField(blank=True, null=True)
    calculation = models.PositiveSmallIntegerField()
    ul_code = models.IntegerField(blank=True, null=True)
    alter_code = models.CharField(max_length=50, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_other_acct'
        unique_together = (('id_code', 'acct_title'),)


class TblPatient(models.Model):
    autonum = models.AutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    id_code = models.PositiveIntegerField()
    case_no = models.CharField(max_length=10, blank=True, null=True)
    patient_code = models.CharField(max_length=10, blank=True, null=True)
    patient_type = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    father_name = models.CharField(max_length=60, blank=True, null=True)
    mother_name = models.CharField(max_length=60, blank=True, null=True)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    birth_place = models.CharField(max_length=150, blank=True, null=True)
    nationality = models.CharField(max_length=150, blank=True, null=True)
    religion = models.CharField(max_length=30, blank=True, null=True)
    st_address = models.CharField(max_length=60, blank=True, null=True)
    city_address = models.CharField(max_length=60, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    barangay = models.CharField(max_length=150, blank=True, null=True)
    province = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=150, blank=True, null=True)
    hmo = models.CharField(max_length=150, blank=True, null=True)
    phic = models.CharField(max_length=1, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    patient_image = models.TextField(blank=True, null=True)
    date_admitted = models.CharField(max_length=20, blank=True, null=True)
    date_discharge = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_patient'
        unique_together = (('id_code', 'last_name', 'first_name', 'middle_name'),)


class TblPatientHistory(models.Model):
    autonum = models.AutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    id_code = models.PositiveIntegerField()
    case_no = models.CharField(max_length=10, blank=True, null=True)
    patient_code = models.CharField(max_length=10, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    date_admitted = models.CharField(max_length=20, blank=True, null=True)
    date_discharge = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_patient_history'
        unique_together = (('id_code', 'case_no', 'patient_code', 'date_admitted', 'date_discharge'),)


class TblPayee(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    payee_name = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    contact_no = models.CharField(max_length=20, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_payee'


class TblPayor(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    payor_name = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    contact_no = models.CharField(max_length=20, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_payor'


class TblPayrollBatching(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    emp_id = models.IntegerField(blank=True, null=True)
    emp_name = models.CharField(max_length=150, blank=True, null=True)
    payrollperiod = models.CharField(max_length=50, blank=True, null=True)
    batch_no = models.IntegerField(blank=True, null=True)
    batch_status = models.CharField(max_length=5, blank=True, null=True)
    done_payroll = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_payroll_batching'


class TblPayrollCompact(models.Model):
    auto_num = models.AutoField(db_column='Auto_num', primary_key=True)  # Field name made lowercase.
    terminal_no = models.CharField(db_column='Terminal_no', max_length=30, blank=True, null=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    full_name = models.CharField(db_column='Full_Name', max_length=40, blank=True, null=True)  # Field name made lowercase.
    basic_salary = models.FloatField(db_column='Basic_Salary', blank=True, null=True)  # Field name made lowercase.
    adjustment = models.FloatField(db_column='Adjustment', blank=True, null=True)  # Field name made lowercase.
    gross_pay = models.FloatField(db_column='Gross_Pay', blank=True, null=True)  # Field name made lowercase.
    deductions = models.FloatField(db_column='Deductions', blank=True, null=True)  # Field name made lowercase.
    net_pay = models.FloatField(db_column='Net_pay', blank=True, null=True)  # Field name made lowercase.
    wtax = models.FloatField(db_column='wTax', blank=True, null=True)  # Field name made lowercase.
    sss = models.FloatField(db_column='SSS', blank=True, null=True)  # Field name made lowercase.
    phic = models.FloatField(db_column='PHIC', blank=True, null=True)  # Field name made lowercase.
    hdmf = models.FloatField(db_column='HDMF', blank=True, null=True)  # Field name made lowercase.
    details1 = models.FloatField(db_column='Details1', blank=True, null=True)  # Field name made lowercase.
    details2 = models.FloatField(db_column='Details2', blank=True, null=True)  # Field name made lowercase.
    details3 = models.FloatField(db_column='Details3', blank=True, null=True)  # Field name made lowercase.
    details4 = models.FloatField(db_column='Details4', blank=True, null=True)  # Field name made lowercase.
    details5 = models.FloatField(db_column='Details5', blank=True, null=True)  # Field name made lowercase.
    details6 = models.FloatField(db_column='Details6', blank=True, null=True)  # Field name made lowercase.
    details7 = models.FloatField(db_column='Details7', blank=True, null=True)  # Field name made lowercase.
    details8 = models.FloatField(db_column='Details8', blank=True, null=True)  # Field name made lowercase.
    details9 = models.FloatField(db_column='Details9', blank=True, null=True)  # Field name made lowercase.
    details10 = models.FloatField(db_column='Details10', blank=True, null=True)  # Field name made lowercase.
    details11 = models.FloatField(db_column='Details11', blank=True, null=True)  # Field name made lowercase.
    details12 = models.FloatField(db_column='Details12', blank=True, null=True)  # Field name made lowercase.
    details13 = models.FloatField(db_column='Details13', blank=True, null=True)  # Field name made lowercase.
    details14 = models.FloatField(db_column='Details14', blank=True, null=True)  # Field name made lowercase.
    details15 = models.FloatField(db_column='Details15', blank=True, null=True)  # Field name made lowercase.
    details16 = models.FloatField(db_column='Details16', blank=True, null=True)  # Field name made lowercase.
    details17 = models.FloatField(db_column='Details17', blank=True, null=True)  # Field name made lowercase.
    details18 = models.FloatField(db_column='Details18', blank=True, null=True)  # Field name made lowercase.
    details19 = models.FloatField(db_column='Details19', blank=True, null=True)  # Field name made lowercase.
    details20 = models.FloatField(db_column='Details20', blank=True, null=True)  # Field name made lowercase.
    details21 = models.FloatField(db_column='Details21', blank=True, null=True)  # Field name made lowercase.
    details22 = models.FloatField(db_column='Details22', blank=True, null=True)  # Field name made lowercase.
    details23 = models.FloatField(db_column='Details23', blank=True, null=True)  # Field name made lowercase.
    details24 = models.FloatField(db_column='Details24', blank=True, null=True)  # Field name made lowercase.
    details25 = models.FloatField(db_column='Details25', blank=True, null=True)  # Field name made lowercase.
    details26 = models.FloatField(db_column='Details26', blank=True, null=True)  # Field name made lowercase.
    details27 = models.FloatField(db_column='Details27', blank=True, null=True)  # Field name made lowercase.
    details28 = models.FloatField(db_column='Details28', blank=True, null=True)  # Field name made lowercase.
    details29 = models.FloatField(db_column='Details29', blank=True, null=True)  # Field name made lowercase.
    details30 = models.FloatField(db_column='Details30', blank=True, null=True)  # Field name made lowercase.
    details31 = models.FloatField(db_column='Details31', blank=True, null=True)  # Field name made lowercase.
    details32 = models.FloatField(db_column='Details32', blank=True, null=True)  # Field name made lowercase.
    details33 = models.FloatField(db_column='Details33', blank=True, null=True)  # Field name made lowercase.
    details34 = models.FloatField(db_column='Details34', blank=True, null=True)  # Field name made lowercase.
    details35 = models.FloatField(db_column='Details35', blank=True, null=True)  # Field name made lowercase.
    details36 = models.FloatField(db_column='Details36', blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_payroll_compact'


class TblPayrollFinal(models.Model):
    company_code = models.IntegerField(primary_key=True)  # The composite primary key (company_code, store_code, Emp_id, Payroll_period) found, that is not supported. The first column is selected.
    store_code = models.IntegerField()
    emp_id = models.FloatField(db_column='Emp_id')  # Field name made lowercase.
    emp_name = models.CharField(db_column='Emp_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emp_tax_status = models.CharField(db_column='Emp_Tax_status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    emp_basic_pay = models.FloatField(db_column='Emp_Basic_Pay', blank=True, null=True)  # Field name made lowercase.
    emp_additional_paywtax = models.FloatField(db_column='Emp_Additional_PaywTax', blank=True, null=True)  # Field name made lowercase.
    emp_nontax_allowance = models.FloatField(db_column='Emp_NonTax_allowance', blank=True, null=True)  # Field name made lowercase.
    sss_cont = models.FloatField(db_column='SSS_cont', blank=True, null=True)  # Field name made lowercase.
    phic_cont = models.FloatField(db_column='PHIC_cont', blank=True, null=True)  # Field name made lowercase.
    hdmf_cont = models.FloatField(db_column='HDMF_cont', blank=True, null=True)  # Field name made lowercase.
    salary_type = models.CharField(db_column='Salary_type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tax_deduction = models.FloatField(db_column='Tax_deduction', blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=30)  # Field name made lowercase.
    company_deductions = models.FloatField(db_column='Company_deductions', blank=True, null=True)  # Field name made lowercase.
    loans_benefits = models.FloatField(db_column='Loans_benefits', blank=True, null=True)  # Field name made lowercase.
    gross_income = models.FloatField(db_column='Gross_income', blank=True, null=True)  # Field name made lowercase.
    net_income = models.FloatField(db_column='Net_income', blank=True, null=True)  # Field name made lowercase.
    dept_id = models.FloatField(db_column='Dept_id', blank=True, null=True)  # Field name made lowercase.
    no_count = models.FloatField(db_column='No_count', blank=True, null=True)  # Field name made lowercase.
    payroll_details = models.CharField(db_column='Payroll_details', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    payroll_summary = models.CharField(db_column='Payroll_summary', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    absent_late = models.FloatField(db_column='Absent_late', blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='ConfiDential', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sss_er = models.FloatField(db_column='SSS_er', blank=True, null=True)  # Field name made lowercase.
    phic_er = models.FloatField(db_column='PHIC_er', blank=True, null=True)  # Field name made lowercase.
    hdmf_er = models.FloatField(db_column='HDMF_er', blank=True, null=True)  # Field name made lowercase.
    taxable_allowance = models.FloatField(blank=True, null=True)
    non_taxable_deduction = models.FloatField(db_column='Non_taxable_deduction', blank=True, null=True)  # Field name made lowercase.
    sss_ec_er = models.FloatField(db_column='sss_eC_er', blank=True, null=True)  # Field name made lowercase.
    cv_no = models.CharField(db_column='CV_no', max_length=30, blank=True, null=True)  # Field name made lowercase.
    jv_no = models.CharField(db_column='JV_no', max_length=11, blank=True, null=True)  # Field name made lowercase.
    other_income = models.FloatField(db_column='Other_Income', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_payroll_final'
        unique_together = (('company_code', 'store_code', 'emp_id', 'payroll_period'),)


class TblPayrollSettings(models.Model):
    company_code = models.IntegerField(blank=True, null=True)
    store_code = models.IntegerField(db_column='Store_code', blank=True, null=True)  # Field name made lowercase.
    sss_period = models.CharField(db_column='SSS_Period', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hdmf_period = models.CharField(db_column='HDMF_period', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phic_period = models.CharField(db_column='PHIC_period', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tax_period = models.CharField(db_column='Tax_period', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reg_holiday = models.FloatField(db_column='Reg_holiday', blank=True, null=True)  # Field name made lowercase.
    special_holiday = models.FloatField(db_column='Special_holiday', blank=True, null=True)  # Field name made lowercase.
    overtime = models.FloatField(db_column='Overtime', blank=True, null=True)  # Field name made lowercase.
    restday = models.FloatField(db_column='RestDay', blank=True, null=True)  # Field name made lowercase.
    nightshift = models.FloatField(db_column='NightShift', blank=True, null=True)  # Field name made lowercase.
    minimumdaily = models.FloatField(db_column='MinimumDaily', blank=True, null=True)  # Field name made lowercase.
    reg_rest = models.FloatField(db_column='Reg_Rest', blank=True, null=True)  # Field name made lowercase.
    spec_rest = models.FloatField(db_column='Spec_Rest', blank=True, null=True)  # Field name made lowercase.
    ot_on_holidayrestday = models.FloatField(db_column='OT_on_HolidayRestday', blank=True, null=True)  # Field name made lowercase.
    accounting = models.CharField(db_column='Accounting', max_length=5, blank=True, null=True)  # Field name made lowercase.
    client_type = models.IntegerField(db_column='Client_type', blank=True, null=True)  # Field name made lowercase.
    graceperiod = models.FloatField(db_column='GracePeriod', blank=True, null=True)  # Field name made lowercase.
    cola = models.FloatField(db_column='Cola', blank=True, null=True)  # Field name made lowercase.
    sss_period2 = models.CharField(db_column='SSS_Period2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hdmf_period2 = models.CharField(db_column='HDMF_period2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phic_period2 = models.CharField(db_column='PHIC_period2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sss_period3 = models.CharField(db_column='SSS_Period3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hdmf_period3 = models.CharField(db_column='HDMF_period3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phic_period3 = models.CharField(db_column='PHIC_period3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    other_deduction = models.CharField(db_column='Other_deduction', max_length=20, blank=True, null=True)  # Field name made lowercase.
    perjob = models.CharField(db_column='PerJob', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_payroll_settings'


class TblPayrollTemp(models.Model):
    company_code = models.IntegerField(primary_key=True)  # The composite primary key (company_code, store_code, Emp_id, Payroll_period) found, that is not supported. The first column is selected.
    store_code = models.IntegerField()
    emp_id = models.FloatField(db_column='Emp_id')  # Field name made lowercase.
    emp_name = models.CharField(db_column='Emp_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emp_tax_status = models.CharField(db_column='Emp_Tax_status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    emp_basic_pay = models.FloatField(db_column='Emp_Basic_Pay', blank=True, null=True)  # Field name made lowercase.
    emp_additional_paywtax = models.FloatField(db_column='Emp_Additional_PaywTax', blank=True, null=True)  # Field name made lowercase.
    emp_nontax_allowance = models.FloatField(db_column='Emp_NonTax_allowance', blank=True, null=True)  # Field name made lowercase.
    sss_cont = models.FloatField(db_column='SSS_cont', blank=True, null=True)  # Field name made lowercase.
    phic_cont = models.FloatField(db_column='PHIC_cont', blank=True, null=True)  # Field name made lowercase.
    hdmf_cont = models.FloatField(db_column='HDMF_cont', blank=True, null=True)  # Field name made lowercase.
    salary_type = models.CharField(db_column='Salary_type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tax_deduction = models.FloatField(db_column='Tax_deduction', blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=30)  # Field name made lowercase.
    company_deductions = models.FloatField(db_column='Company_deductions', blank=True, null=True)  # Field name made lowercase.
    loans_benefits = models.FloatField(db_column='Loans_benefits', blank=True, null=True)  # Field name made lowercase.
    gross_income = models.FloatField(db_column='Gross_income', blank=True, null=True)  # Field name made lowercase.
    net_income = models.FloatField(db_column='Net_income', blank=True, null=True)  # Field name made lowercase.
    dept_id = models.FloatField(db_column='Dept_id', blank=True, null=True)  # Field name made lowercase.
    no_count = models.FloatField(db_column='No_count', blank=True, null=True)  # Field name made lowercase.
    payroll_details = models.CharField(db_column='Payroll_details', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    payroll_summary = models.CharField(db_column='Payroll_summary', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    absent_late = models.FloatField(db_column='Absent_late', blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='ConfiDential', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sss_er = models.FloatField(db_column='SSS_er', blank=True, null=True)  # Field name made lowercase.
    phic_er = models.FloatField(db_column='PHIC_er', blank=True, null=True)  # Field name made lowercase.
    hdmf_er = models.FloatField(db_column='HDMF_er', blank=True, null=True)  # Field name made lowercase.
    taxable_allowance = models.FloatField(blank=True, null=True)
    non_taxable_deduction = models.FloatField(db_column='Non_taxable_deduction', blank=True, null=True)  # Field name made lowercase.
    sss_ec_er = models.FloatField(db_column='sss_eC_er', blank=True, null=True)  # Field name made lowercase.
    cv_no = models.CharField(db_column='CV_no', max_length=30, blank=True, null=True)  # Field name made lowercase.
    other_income = models.FloatField(db_column='Other_Income', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_payroll_temp'
        unique_together = (('company_code', 'store_code', 'emp_id', 'payroll_period'),)


class TblPayrollperiod(models.Model):
    auto_no = models.AutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    cod = models.IntegerField(db_column='COD', blank=True, null=True)  # Field name made lowercase.
    store_code = models.IntegerField(db_column='Store_Code', blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_Period', max_length=20, blank=True, null=True)  # Field name made lowercase.
    period_type = models.CharField(db_column='Period_Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datestart = models.DateField(db_column='DateStart', blank=True, null=True)  # Field name made lowercase.
    dateend = models.DateField(db_column='DateEnd', blank=True, null=True)  # Field name made lowercase.
    year = models.FloatField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    payroll_type = models.CharField(db_column='Payroll_type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    transaction_status = models.CharField(max_length=3, blank=True, null=True)
    year_month1 = models.CharField(db_column='Year_Month1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    period_no = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_payrollperiod'


class TblPerSalesList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    reference_no = models.FloatField(blank=True, null=True)
    terminal_no = models.BigIntegerField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=400, blank=True, null=True)
    active = models.CharField(db_column='Active', max_length=2, blank=True, null=True)  # Field name made lowercase.
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_per_sales_list'
        unique_together = (('reference_no', 'date_trans', 'trans_type'),)


class TblPerpiece(models.Model):
    auto_no = models.AutoField(unique=True)
    company_code = models.IntegerField(blank=True, null=True)
    store_code = models.IntegerField(db_column='Store_code', blank=True, null=True)  # Field name made lowercase.
    date_in = models.DateField(db_column='Date_in', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_ID', blank=True, null=True)  # Field name made lowercase.
    job_code = models.FloatField(db_column='Job_code', blank=True, null=True)  # Field name made lowercase.
    unit_qty = models.FloatField(db_column='Unit_Qty', blank=True, null=True)  # Field name made lowercase.
    job_cost = models.FloatField(db_column='Job_cost', blank=True, null=True)  # Field name made lowercase.
    total_cost = models.FloatField(db_column='Total_cost', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    unit_abbrev = models.CharField(db_column='Unit_Abbrev', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ul_code = models.SmallIntegerField(db_column='Ul_code', blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_Period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dept_id = models.FloatField(db_column='Dept_id', blank=True, null=True)  # Field name made lowercase.
    ref_no = models.CharField(max_length=15, blank=True, null=True)
    taxable_cost = models.FloatField(db_column='Taxable_Cost', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_perpiece'


class TblPerpiecelist(models.Model):
    auto_num = models.AutoField(unique=True)
    company_code = models.IntegerField(blank=True, null=True)
    store_code = models.IntegerField(blank=True, null=True)
    ref_no = models.CharField(db_column='Ref_no', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_in = models.DateField(db_column='Date_in', blank=True, null=True)  # Field name made lowercase.
    job_code = models.FloatField(db_column='Job_code', blank=True, null=True)  # Field name made lowercase.
    unit_qty = models.FloatField(db_column='Unit_qty', blank=True, null=True)  # Field name made lowercase.
    job_cost = models.FloatField(db_column='Job_cost', blank=True, null=True)  # Field name made lowercase.
    total_cost = models.FloatField(blank=True, null=True)
    ul_code = models.SmallIntegerField(db_column='Ul_code', blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dept_id = models.FloatField(blank=True, null=True)
    position_id = models.FloatField(db_column='Position_ID', blank=True, null=True)  # Field name made lowercase.
    emp_stat_id = models.FloatField(db_column='Emp_stat_ID', blank=True, null=True)  # Field name made lowercase.
    same_qty = models.CharField(max_length=5, blank=True, null=True)
    confi = models.CharField(db_column='Confi', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_perpiecelist'


class TblPhicContSched(models.Model):
    check = models.CharField(max_length=1, blank=True, null=True)
    sal_bracket = models.IntegerField(primary_key=True)
    frm_amnt = models.FloatField(blank=True, null=True)
    to_amount = models.FloatField(blank=True, null=True)
    r_premium = models.FloatField(blank=True, null=True)
    m_salary = models.FloatField(blank=True, null=True)
    total_mpremium = models.FloatField(blank=True, null=True)
    employee_share = models.FloatField(blank=True, null=True)
    employer_share = models.FloatField(blank=True, null=True)
    percent = models.CharField(db_column='Percent', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_phic_cont_sched'


class TblPorCheck(models.Model):
    or_no = models.FloatField(blank=True, null=True)
    date_check = models.DateField(blank=True, null=True)
    drawee_bank = models.CharField(max_length=10, blank=True, null=True)
    check_no = models.FloatField(blank=True, null=True)
    check_amt = models.FloatField(blank=True, null=True)
    cash_amt = models.FloatField(blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_por_check'
        unique_together = (('or_no', 'date_check', 'check_no', 'check_amt', 'cash_amt'),)


class TblPorCollection(models.Model):
    or_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    dept_code = models.CharField(max_length=10, blank=True, null=True)
    cardholder = models.CharField(max_length=60, blank=True, null=True)
    authorized_person = models.CharField(max_length=60, blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    amount_applied = models.FloatField(blank=True, null=True)
    check_type = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_por_collection'
        unique_together = (('or_no', 'date_trans', 'doc_no', 'dept_code'),)


class TblPorDevinc(models.Model):
    or_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    dev_location = models.CharField(max_length=100, blank=True, null=True)
    particulars = models.CharField(max_length=100, blank=True, null=True)
    dept_code = models.CharField(max_length=10, blank=True, null=True)
    amount_applied = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_por_devinc'
        unique_together = (('or_no', 'date_trans', 'dev_location', 'particulars'),)


class TblPorGiftCheck(models.Model):
    or_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    gift_check_no = models.FloatField(blank=True, null=True)
    dept_code = models.CharField(max_length=10, blank=True, null=True)
    validity_period = models.CharField(max_length=20, blank=True, null=True)
    amount_applied = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_por_gift_check'
        unique_together = (('or_no', 'date_trans', 'gift_check_no', 'dept_code'),)


class TblPorList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    or_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.PositiveIntegerField(blank=True, null=True)
    payor = models.CharField(max_length=150, blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    date_check = models.DateField(blank=True, null=True)
    check_no = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=400, blank=True, null=True)
    transtype = models.CharField(db_column='TransType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=2, blank=True, null=True)  # Field name made lowercase.
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    terminal_no = models.CharField(max_length=21, blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_por_list'


class TblPorRca(models.Model):
    or_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    dept_code = models.CharField(max_length=10, blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    amount_applied = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_por_rca'
        unique_together = (('or_no', 'date_trans', 'doc_no', 'dept_code'),)


class TblPorTranstype(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    or_no = models.FloatField(blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=300, blank=True, null=True)
    ci_no = models.FloatField(blank=True, null=True)
    source_module_ar = models.CharField(max_length=3, blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    amount_due = models.FloatField(blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    gross_amount = models.FloatField(blank=True, null=True)
    scheme_type = models.CharField(max_length=10, blank=True, null=True)
    sec_ref = models.CharField(max_length=100, blank=True, null=True)
    sa_no = models.CharField(max_length=15, blank=True, null=True)
    sl_name = models.CharField(max_length=100, blank=True, null=True)
    ul_code_pmt = models.IntegerField(blank=True, null=True)
    date_trans_pmt = models.DateField(blank=True, null=True)
    source_module_pmt = models.CharField(max_length=3, blank=True, null=True)
    acct_code = models.CharField(max_length=11, blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_por_transtype'


class TblProduct(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    pos_site_code = models.CharField(max_length=10, blank=True, null=True)
    pos_item = models.CharField(max_length=6, blank=True, null=True)
    item_type = models.CharField(max_length=20, blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=150, blank=True, null=True)
    principal_id = models.IntegerField(blank=True, null=True)
    principal = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    style = models.CharField(max_length=50, blank=True, null=True)
    p_size = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    qty_onhand = models.FloatField(blank=True, null=True)
    qty_avl = models.FloatField(blank=True, null=True)
    uom = models.CharField(max_length=50, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    long_desc = models.CharField(max_length=150, blank=True, null=True)
    short_desc = models.CharField(max_length=150, blank=True, null=True)
    reg_price = models.FloatField(blank=True, null=True)
    key_price = models.FloatField(blank=True, null=True)
    ws_price = models.FloatField(blank=True, null=True)
    ec_price = models.FloatField(blank=True, null=True)
    last_purch = models.FloatField(blank=True, null=True)
    po_qty_allowance = models.FloatField(blank=True, null=True)
    so_qty_allowance = models.FloatField(blank=True, null=True)
    standard_price = models.FloatField(blank=True, null=True)
    rm_cost = models.FloatField(blank=True, null=True)
    dl_cost = models.FloatField(blank=True, null=True)
    oh_cost = models.FloatField(blank=True, null=True)
    ave_cost = models.FloatField(blank=True, null=True)
    fifo_cost = models.FloatField(blank=True, null=True)
    tax_code = models.CharField(max_length=10, blank=True, null=True)
    prod_img = models.TextField(blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    with_serial = models.CharField(max_length=4, blank=True, null=True)
    batch_code = models.CharField(max_length=4, blank=True, null=True)
    rebates_amount = models.FloatField(blank=True, null=True)
    salesman_amount = models.FloatField(blank=True, null=True)
    trustor_name = models.CharField(max_length=250, blank=True, null=True)
    virtual_setup = models.CharField(max_length=10, blank=True, null=True)
    production_setup = models.CharField(max_length=1, blank=True, null=True)
    vat_category_code = models.CharField(max_length=10, blank=True, null=True)
    back_flush = models.CharField(max_length=1, blank=True, null=True)
    charcoal_item = models.CharField(max_length=1, blank=True, null=True)
    product_export = models.CharField(max_length=1, blank=True, null=True)
    cwt_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product'
        unique_together = (('item_type', 'brand', 'model', 'style', 'p_size', 'color', 'alternate_code', 'bar_code'),)


class TblProductAccountReceivableList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ci_date_from = models.DateField(blank=True, null=True)
    ci_date_to = models.DateField(blank=True, null=True)
    or_date_from = models.DateField(blank=True, null=True)
    or_date_to = models.DateField(blank=True, null=True)
    arc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    id_code = models.IntegerField(blank=True, null=True)
    sl_acct = models.CharField(max_length=100, blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    paymentsource = models.CharField(db_column='paymentSource', max_length=20, blank=True, null=True)  # Field name made lowercase.
    total_applied = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_account_receivable_list'


class TblProductAccountReceivableListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ci_date_from = models.DateField(blank=True, null=True)
    ci_date_to = models.DateField(blank=True, null=True)
    or_date_from = models.DateField(blank=True, null=True)
    or_date_to = models.DateField(blank=True, null=True)
    arc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    tmp1 = models.CharField(max_length=100, blank=True, null=True)
    tmp2 = models.CharField(max_length=100, blank=True, null=True)
    tmp3 = models.CharField(max_length=100, blank=True, null=True)
    tmp4 = models.CharField(max_length=100, blank=True, null=True)
    tmp5 = models.CharField(max_length=100, blank=True, null=True)
    tmp6 = models.CharField(max_length=100, blank=True, null=True)
    tmp7 = models.CharField(max_length=100, blank=True, null=True)
    tmp8 = models.CharField(max_length=100, blank=True, null=True)
    tmp9 = models.CharField(max_length=100, blank=True, null=True)
    tmp10 = models.CharField(max_length=100, blank=True, null=True)
    tmp11 = models.CharField(max_length=100, blank=True, null=True)
    tmp12 = models.CharField(max_length=100, blank=True, null=True)
    tmp13 = models.CharField(max_length=100, blank=True, null=True)
    tmp14 = models.CharField(max_length=100, blank=True, null=True)
    tmp15 = models.CharField(max_length=100, blank=True, null=True)
    tmp16 = models.CharField(max_length=100, blank=True, null=True)
    tmp17 = models.CharField(max_length=100, blank=True, null=True)
    tmp18 = models.CharField(max_length=100, blank=True, null=True)
    tmp19 = models.CharField(max_length=100, blank=True, null=True)
    tmp20 = models.CharField(max_length=100, blank=True, null=True)
    tmp21 = models.CharField(max_length=100, blank=True, null=True)
    tmp22 = models.CharField(max_length=100, blank=True, null=True)
    tmp23 = models.CharField(max_length=100, blank=True, null=True)
    tmp24 = models.CharField(max_length=100, blank=True, null=True)
    tmp25 = models.CharField(max_length=100, blank=True, null=True)
    tmp26 = models.CharField(max_length=100, blank=True, null=True)
    tmp27 = models.CharField(max_length=100, blank=True, null=True)
    tmp28 = models.CharField(max_length=100, blank=True, null=True)
    tmp29 = models.CharField(max_length=100, blank=True, null=True)
    tmp30 = models.CharField(max_length=100, blank=True, null=True)
    tmp31 = models.CharField(max_length=100, blank=True, null=True)
    tmp32 = models.CharField(max_length=100, blank=True, null=True)
    tmp33 = models.CharField(max_length=100, blank=True, null=True)
    tmp34 = models.CharField(max_length=100, blank=True, null=True)
    tmp35 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_account_receivable_listing'


class TblProductAccountReceivableOutstanding(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ci_date_from = models.DateField(blank=True, null=True)
    ci_date_to = models.DateField(blank=True, null=True)
    or_date_from = models.DateField(blank=True, null=True)
    or_date_to = models.DateField(blank=True, null=True)
    arc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    ci_or_date = models.CharField(max_length=25, blank=True, null=True)
    ci_or_reference = models.CharField(max_length=50, blank=True, null=True)
    ci_or_acct_title = models.CharField(max_length=150, blank=True, null=True)
    ci_or_total = models.CharField(max_length=50, blank=True, null=True)
    ci_or_outstanding = models.CharField(max_length=50, blank=True, null=True)
    ci_or_payment = models.CharField(max_length=50, blank=True, null=True)
    ci_check_status = models.CharField(max_length=25, blank=True, null=True)
    ci_ul_code = models.CharField(max_length=1, blank=True, null=True)
    ci_doc_no = models.CharField(max_length=50, blank=True, null=True)
    ci_date_trans = models.CharField(max_length=25, blank=True, null=True)
    ci_id_code = models.CharField(max_length=50, blank=True, null=True)
    ci_customer_name = models.CharField(max_length=100, blank=True, null=True)
    ci_terms = models.CharField(max_length=50, blank=True, null=True)
    ci_payment_scheme = models.CharField(max_length=20, blank=True, null=True)
    ci_due_date = models.CharField(max_length=25, blank=True, null=True)
    ci_total_amt = models.CharField(max_length=50, blank=True, null=True)
    ci_remarks = models.CharField(max_length=100, blank=True, null=True)
    ci_doc_type = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_account_receivable_outstanding'


class TblProductAccountReceivableUnapplied(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ci_date_from = models.DateField(blank=True, null=True)
    ci_date_to = models.DateField(blank=True, null=True)
    or_date_from = models.DateField(blank=True, null=True)
    or_date_to = models.DateField(blank=True, null=True)
    arc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    or_ci_date = models.CharField(max_length=25, blank=True, null=True)
    or_ci_reference = models.CharField(max_length=50, blank=True, null=True)
    or_acct_title = models.CharField(max_length=150, blank=True, null=True)
    or_ci_total = models.CharField(max_length=50, blank=True, null=True)
    or_ci_unapplied = models.CharField(max_length=50, blank=True, null=True)
    or_ci_payment = models.CharField(max_length=50, blank=True, null=True)
    or_check_status = models.CharField(max_length=25, blank=True, null=True)
    or_doc_no = models.CharField(max_length=50, blank=True, null=True)
    or_ul_code = models.CharField(max_length=2, blank=True, null=True)
    or_ci_no = models.CharField(max_length=50, blank=True, null=True)
    or_date_trans = models.CharField(max_length=25, blank=True, null=True)
    or_amount_due = models.CharField(max_length=50, blank=True, null=True)
    or_gross_amt = models.CharField(max_length=50, blank=True, null=True)
    or_scheme_type = models.CharField(max_length=1, blank=True, null=True)
    or_sec_ref = models.CharField(max_length=25, blank=True, null=True)
    or_doc_type = models.CharField(max_length=25, blank=True, null=True)
    or_last_row = models.CharField(max_length=25, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_account_receivable_unapplied'


class TblProductAddInfo(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    bar_code = models.CharField(unique=True, max_length=20, blank=True, null=True)
    min_qty = models.FloatField(blank=True, null=True)
    max_qty = models.FloatField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)
    inv_buildup = models.FloatField(blank=True, null=True)
    day_to_st = models.FloatField(db_column='day_to_ST', blank=True, null=True)  # Field name made lowercase.
    daily_ave = models.FloatField(blank=True, null=True)
    last_sales_date = models.DateField(blank=True, null=True)
    regular_or_phaseout = models.CharField(max_length=1, blank=True, null=True)
    active_or_inactive = models.CharField(max_length=1, blank=True, null=True)
    trade_or_nontrade = models.CharField(max_length=1, blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    serial_no = models.FloatField(blank=True, null=True)
    supervisordiscount_from = models.FloatField(blank=True, null=True)
    supervisordiscount_to = models.FloatField(blank=True, null=True)
    cashierdiscount_from = models.FloatField(blank=True, null=True)
    cashierdiscount_to = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_add_info'


class TblProductAdjInList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    in_no = models.FloatField(blank=True, null=True)
    doctype = models.CharField(max_length=10, blank=True, null=True)
    in_date = models.CharField(max_length=25, blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    adjsite_code = models.IntegerField(blank=True, null=True)
    adjsite_name = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=50, blank=True, null=True)
    doc_no = models.IntegerField(blank=True, null=True)
    doc_date = models.CharField(max_length=10, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, db_collation='latin1_general_ci', blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, db_collation='latin1_general_ci', blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, db_collation='latin1_general_ci', blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_adj_in_list'
        unique_together = (('ul_code', 'in_no', 'in_date', 'site_name', 'doc_no', 'doc_date'),)


class TblProductAdjInListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    in_no = models.FloatField(blank=True, null=True)
    doctype = models.CharField(max_length=10, blank=True, null=True)
    in_date = models.CharField(max_length=25, blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    ave_cost = models.FloatField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_adj_in_listing'


class TblProductAdjInSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    in_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    in_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_adj_in_sn_bc'


class TblProductAdjOffset(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    jv_no = models.FloatField(blank=True, null=True)
    offset_no = models.PositiveIntegerField(blank=True, null=True)
    offset_date = models.CharField(max_length=25, db_collation='latin1_bin', blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    site_name = models.CharField(max_length=100, db_collation='latin1_general_ci', blank=True, null=True)
    remarks = models.CharField(max_length=250, db_collation='latin1_general_ci', blank=True, null=True)
    adjsite_code = models.IntegerField(blank=True, null=True)
    adjsite_name = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=50, blank=True, null=True)
    doc_no = models.IntegerField(blank=True, null=True)
    doc_date = models.DateField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, db_collation='latin1_general_ci', blank=True, null=True)
    alternate_code = models.CharField(max_length=20, db_collation='latin1_general_ci', blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, db_collation='latin1_general_ci', blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, db_collation='latin1_general_ci', blank=True, null=True)
    description = models.CharField(max_length=100, db_collation='latin1_general_ci', blank=True, null=True)
    regular_price = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, db_collation='latin1_general_ci', blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, db_collation='latin1_general_ci', blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, db_collation='latin1_general_ci', blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_adj_offset'
        unique_together = (('ul_code', 'jv_no', 'offset_no', 'offset_date', 'site_name', 'doc_no', 'doc_date', 'bar_code', 'description', 'line_number'),)


class TblProductAdjOutList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doctype = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    site_code = models.PositiveIntegerField(blank=True, null=True)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    adjsite_code = models.PositiveIntegerField(blank=True, null=True)
    adjsite_name = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=50, blank=True, null=True)
    doc_no = models.PositiveIntegerField(blank=True, null=True)
    doc_date = models.CharField(max_length=10, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_adj_out_list'
        unique_together = (('ul_code', 'out_no', 'out_date', 'site_name', 'doc_no', 'doc_date'),)


class TblProductAdjOutListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doctype = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    ave_cost = models.FloatField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_adj_out_listing'
        unique_together = (('ul_code', 'out_no', 'out_date', 'bar_code', 'description', 'line_number'),)


class TblProductAdjOutSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_adj_out_sn_bc'


class TblProductBankCreditSetup(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    code = models.PositiveIntegerField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    acct_code = models.FloatField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    sl_code = models.FloatField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_bank_credit_setup'


class TblProductBankDebitSetup(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    code = models.PositiveIntegerField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    acct_code = models.FloatField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    sl_code = models.FloatField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_bank_debit_setup'


class TblProductBarcodeRequestList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    source_doc = models.CharField(max_length=25, blank=True, null=True)
    doc_range_from = models.CharField(max_length=25, blank=True, null=True)
    doc_range_to = models.CharField(max_length=25, blank=True, null=True)
    charge_to = models.CharField(max_length=250, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    barcode_count = models.FloatField(blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    include_barcode = models.CharField(max_length=1, blank=True, null=True)
    include_prod_desc = models.CharField(max_length=1, blank=True, null=True)
    include_price = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_barcode_request_list'
        unique_together = (('ul_code', 'doc_no', 'doc_date', 'trans_type'),)


class TblProductBarcodeRequestListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    barcode_count = models.FloatField(blank=True, null=True)
    sell_price = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_barcode_request_listing'
        unique_together = (('ul_code', 'doc_no', 'doc_date', 'bar_code', 'description', 'line_number'),)


class TblProductBillingSetupList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    customer_code = models.IntegerField(blank=True, null=True)
    customer = models.CharField(max_length=500, blank=True, null=True)
    billing_period_type = models.CharField(max_length=25, blank=True, null=True)
    billing_period_sub1 = models.CharField(max_length=100, blank=True, null=True)
    billing_period_sub2 = models.CharField(max_length=100, blank=True, null=True)
    billing_period_sub3 = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_billing_setup_list'


class TblProductBrandSetup(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    brand_code = models.PositiveIntegerField(blank=True, null=True)
    brand_desc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_brand_setup'


class TblProductCanvassList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    pc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    pc_date = models.CharField(max_length=25, blank=True, null=True)
    date_expected = models.DateField(blank=True, null=True)
    supplier_code1 = models.IntegerField(blank=True, null=True)
    supplier1 = models.CharField(max_length=100, blank=True, null=True)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    contact_no1 = models.CharField(max_length=25, blank=True, null=True)
    remarks1 = models.CharField(max_length=255, blank=True, null=True)
    supplier_type1 = models.CharField(max_length=1, blank=True, null=True)
    supplier_code2 = models.IntegerField(blank=True, null=True)
    supplier2 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    contact_no2 = models.CharField(max_length=25, blank=True, null=True)
    remarks2 = models.CharField(max_length=255, blank=True, null=True)
    supplier_type2 = models.CharField(max_length=1, blank=True, null=True)
    supplier_code3 = models.IntegerField(blank=True, null=True)
    supplier3 = models.CharField(max_length=100, blank=True, null=True)
    address3 = models.CharField(max_length=100, blank=True, null=True)
    contact_no3 = models.CharField(max_length=25, blank=True, null=True)
    remarks3 = models.CharField(max_length=255, blank=True, null=True)
    supplier_type3 = models.CharField(max_length=1, blank=True, null=True)
    supplier_code4 = models.IntegerField(blank=True, null=True)
    supplier4 = models.CharField(max_length=100, blank=True, null=True)
    address4 = models.CharField(max_length=100, blank=True, null=True)
    contact_no4 = models.CharField(max_length=25, blank=True, null=True)
    remarks4 = models.CharField(max_length=255, blank=True, null=True)
    supplier_type4 = models.CharField(max_length=1, blank=True, null=True)
    supplier_code5 = models.IntegerField(blank=True, null=True)
    supplier5 = models.CharField(max_length=100, blank=True, null=True)
    address5 = models.CharField(max_length=100, blank=True, null=True)
    contact_no5 = models.CharField(max_length=25, blank=True, null=True)
    remarks5 = models.CharField(max_length=255, blank=True, null=True)
    supplier_type5 = models.CharField(max_length=1, blank=True, null=True)
    deliver_to = models.CharField(max_length=150, blank=True, null=True)
    terms = models.CharField(max_length=10, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_canvass_list'
        unique_together = (('ul_code', 'pc_no', 'pc_date'),)


class TblProductCanvassListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    pc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    pc_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    specification = models.CharField(max_length=150, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    net_amount = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    vat_amt = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    indicator = models.CharField(max_length=1, blank=True, null=True)
    lowest_bid = models.CharField(max_length=1, blank=True, null=True)
    bid_byes = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_canvass_listing'
        unique_together = (('ul_code', 'pc_no', 'pc_date', 'bar_code', 'description', 'line_number', 'indicator'),)


class TblProductCanvassPo(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    pc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    po_doc_no = models.IntegerField(blank=True, null=True)
    po_doc_type = models.CharField(max_length=10)
    po_date = models.DateField(blank=True, null=True)
    pc_indicator = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_canvass_po'
        unique_together = (('pc_no', 'po_doc_no', 'po_date', 'pc_indicator'),)


class TblProductCategoryInfo(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    category_desc1 = models.CharField(max_length=150, blank=True, null=True)
    category_desc2 = models.CharField(max_length=150, blank=True, null=True)
    category_desc3 = models.CharField(max_length=150, blank=True, null=True)
    category_desc4 = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_category_info'


class TblProductCategorySales(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    mod_code = models.PositiveIntegerField(blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    category_desc = models.CharField(max_length=150, blank=True, null=True)
    vat_code = models.FloatField(blank=True, null=True)
    vat_title = models.CharField(max_length=150, blank=True, null=True)
    acct_code2 = models.FloatField(blank=True, null=True)
    acct_title2 = models.CharField(max_length=150, blank=True, null=True)
    nonvat_code = models.FloatField(blank=True, null=True)
    nonvat_title = models.CharField(max_length=150, blank=True, null=True)
    acct_code3 = models.FloatField(blank=True, null=True)
    acct_title3 = models.CharField(max_length=150, blank=True, null=True)
    zerorated_code = models.FloatField(blank=True, null=True)
    zerorated_title = models.CharField(max_length=150, blank=True, null=True)
    acct_code4 = models.FloatField(blank=True, null=True)
    acct_title4 = models.CharField(max_length=150)
    vatex_code = models.FloatField(blank=True, null=True)
    vatex_title = models.CharField(max_length=150, blank=True, null=True)
    acct_code5 = models.FloatField(blank=True, null=True)
    acct_title5 = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'tbl_product_category_sales'


class TblProductCategorySetup(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    category_code = models.PositiveIntegerField(blank=True, null=True)
    category_desc = models.CharField(max_length=150, blank=True, null=True)
    acct_code = models.FloatField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    acct_code2 = models.FloatField(blank=True, null=True)
    acct_title2 = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_category_setup'


class TblProductCategorySub1(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    category_code = models.PositiveIntegerField(blank=True, null=True)
    category_desc = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_category_sub1'


class TblProductCategorySub2(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    category_code = models.PositiveIntegerField(blank=True, null=True)
    category_desc = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_category_sub2'


class TblProductCategorySub3(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    category_code = models.PositiveIntegerField(blank=True, null=True)
    category_desc = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_category_sub3'


class TblProductCheckDisbursementMonitoring(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    date = models.CharField(max_length=25, blank=True, null=True)
    bank_description = models.CharField(max_length=150, blank=True, null=True)
    cv_no = models.CharField(max_length=30, blank=True, null=True)
    check_no = models.CharField(max_length=30, blank=True, null=True)
    debit = models.FloatField(blank=True, null=True)
    credit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_check_disbursement_monitoring'


class TblProductCmList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    customer = models.CharField(max_length=100, blank=True, null=True)
    customer_code = models.IntegerField(blank=True, null=True)
    customer_address = models.CharField(max_length=250, blank=True, null=True)
    contact_no = models.CharField(max_length=25, blank=True, null=True)
    cm_amount = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    remarks = models.CharField(max_length=900, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_cm_list'


class TblProductCmListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    reference_no = models.CharField(max_length=20, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    acct_name = models.CharField(max_length=150, blank=True, null=True)
    amount_due = models.FloatField(blank=True, null=True)
    pmt_amount = models.FloatField(blank=True, null=True)
    acct_name_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_cm_listing'


class TblProductCmOther(models.Model):
    doc_no = models.FloatField()
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    particular = models.CharField(max_length=150, blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    sl_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_cm_other'


class TblProductCommRate(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    comm_name = models.CharField(max_length=50, blank=True, null=True)
    comm_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_comm_rate'


class TblProductCsActivity(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    activity_type = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_cs_activity'
        unique_together = (('ul_code', 'doc_no', 'doc_date', 'site_name'),)


class TblProductCsCuttoff(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    activity_no = models.FloatField(blank=True, null=True)
    activity_date = models.CharField(max_length=25, blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=250, blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_cs_cuttoff'


class TblProductCsList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    reference_no = models.FloatField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    cs_no = models.FloatField(blank=True, null=True)
    cs_date = models.CharField(max_length=25, blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    locator = models.CharField(max_length=250, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    int_setup = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_cs_list'
        unique_together = (('ul_code', 'cs_no', 'cs_date', 'site_name', 'trans_type'),)


class TblProductCsListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    reference_no = models.FloatField(blank=True, null=True)
    cs_no = models.FloatField(blank=True, null=True)
    cs_date = models.CharField(max_length=25, blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    ave_cost = models.FloatField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_cs_listing'
        unique_together = (('ul_code', 'cs_no', 'cs_date', 'bar_code', 'description', 'line_number'),)


class TblProductCsSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    activity_no = models.FloatField(blank=True, null=True)
    cs_no = models.FloatField(blank=True, null=True)
    cs_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_cs_sn_bc'


class TblProductCsVariance(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    reference_no = models.FloatField(blank=True, null=True)
    var_date = models.CharField(max_length=25, blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    qty_count = models.FloatField(blank=True, null=True)
    system_qty = models.FloatField(blank=True, null=True)
    qty_variance = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    total_variance = models.FloatField(blank=True, null=True)
    in_no = models.FloatField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_cs_variance'


class TblProductDamageList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    shet_no = models.PositiveIntegerField(blank=True, null=True)
    shet_date = models.CharField(max_length=25, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_damage_list'
        unique_together = (('ul_code', 'out_no', 'out_date', 'site_name', 'shet_no', 'shet_date', 'trans_type'),)


class TblProductDamageListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    ave_cost = models.FloatField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_damage_listing'
        unique_together = (('ul_code', 'out_no', 'out_date', 'bar_code', 'description', 'line_number'),)


class TblProductDeliveryInfo(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    delivery_desc = models.CharField(max_length=100, blank=True, null=True)
    customer_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_delivery_info'


class TblProductDepositCashList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    date_deposited = models.DateField(blank=True, null=True)
    account_name = models.CharField(max_length=900, blank=True, null=True)
    sl_acct = models.CharField(max_length=100, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    total_bills = models.FloatField(blank=True, null=True)
    partial_deposit = models.FloatField(blank=True, null=True)
    total_deposit = models.FloatField(blank=True, null=True)
    total_count = models.FloatField(blank=True, null=True)
    deposit_count = models.FloatField(blank=True, null=True)
    undeposited_bills = models.FloatField(blank=True, null=True)
    bills_status = models.CharField(max_length=15, blank=True, null=True)
    remarks = models.CharField(max_length=900, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=50)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=50)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_deposit_cash_list'


class TblProductDepositCashListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.DateField(blank=True, null=True)
    acct_code = models.FloatField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    reference_type = models.CharField(max_length=25, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    payor_name = models.CharField(max_length=150, blank=True, null=True)
    collector_name = models.CharField(max_length=150, blank=True, null=True)
    total_bills = models.FloatField(blank=True, null=True)
    partial_payment = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_deposit_cash_listing'


class TblProductDepositCheckList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    id_code = models.IntegerField()
    bank_account = models.CharField(max_length=150, blank=True, null=True)
    record_month = models.CharField(max_length=20, blank=True, null=True)
    record_year = models.CharField(max_length=5, blank=True, null=True)
    default_date = models.DateField(blank=True, null=True)
    count_issued = models.FloatField(blank=True, null=True)
    count_cleared = models.FloatField(blank=True, null=True)
    count_ocs = models.FloatField(blank=True, null=True)
    count_pdc = models.FloatField(blank=True, null=True)
    count_stale = models.FloatField(blank=True, null=True)
    total_issued = models.FloatField(blank=True, null=True)
    total_cleared = models.FloatField(blank=True, null=True)
    total_ocs = models.FloatField(blank=True, null=True)
    total_pdc = models.FloatField(blank=True, null=True)
    total_stale = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=50)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=50)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_deposit_check_list'


class TblProductDepositCheckListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    check_dates = models.DateField(blank=True, null=True)
    check_number = models.CharField(max_length=20, blank=True, null=True)
    reference_type = models.CharField(max_length=20, blank=True, null=True)
    cv_dates = models.DateField(blank=True, null=True)
    payee = models.CharField(max_length=150, blank=True, null=True)
    cv_amount = models.FloatField(blank=True, null=True)
    cleared_amount = models.FloatField(blank=True, null=True)
    date_cleared = models.DateField(blank=True, null=True)
    stale_status = models.CharField(max_length=1, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    tab_status = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_deposit_check_listing'


class TblProductDepositEntries(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_acct = models.CharField(max_length=100, blank=True, null=True)
    total_deposit = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_deposit_entries'
        unique_together = (('doc_no', 'doc_type', 'sl_code'),)


class TblProductDepositList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    sl_acct = models.CharField(max_length=100, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    deposit_amount = models.FloatField(blank=True, null=True)
    no_of_chk = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=50, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=50, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_deposit_list'


class TblProductDepositListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    check_no = models.CharField(max_length=20, blank=True, null=True)
    check_date = models.DateField(blank=True, null=True)
    drawee_bank = models.CharField(max_length=150, blank=True, null=True)
    check_amt = models.FloatField(blank=True, null=True)
    customer_name = models.CharField(max_length=150, blank=True, null=True)
    si_no = models.CharField(max_length=20, blank=True, null=True)
    si_date = models.DateField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    sl_id = models.IntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=150, blank=True, null=True)
    check_type = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_deposit_listing'


class TblProductDmList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    customer = models.CharField(max_length=100, blank=True, null=True)
    customer_code = models.IntegerField(blank=True, null=True)
    customer_address = models.CharField(max_length=250, blank=True, null=True)
    contact_no = models.CharField(max_length=25, blank=True, null=True)
    cm_amount = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    remarks = models.CharField(max_length=900, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_dm_list'


class TblProductDmListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    reference_no = models.CharField(max_length=20, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    acct_name = models.CharField(max_length=150, blank=True, null=True)
    amount_due = models.FloatField(blank=True, null=True)
    pmt_amount = models.FloatField(blank=True, null=True)
    acct_name_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_dm_listing'


class TblProductDmOther(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    doc_no = models.FloatField()
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    particular = models.CharField(max_length=150, blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    sl_id = models.IntegerField(blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_dm_other'


class TblProductDocType(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    doc_type = models.CharField(max_length=15, blank=True, null=True)
    doc_name = models.CharField(max_length=50, blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    tax_type = models.CharField(max_length=10, blank=True, null=True)
    payment_type = models.CharField(max_length=25, blank=True, null=True)
    vat_item_type = models.CharField(max_length=10, blank=True, null=True)
    allow_no_po = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_doc_type'


class TblProductInventoryQtyLive(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    site_code = models.IntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=50, blank=True, null=True)
    item_code = models.CharField(max_length=50, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    prev_modify_by = models.CharField(max_length=100, blank=True, null=True)
    prev_modify_date = models.CharField(max_length=100, blank=True, null=True)
    prev_modify_form = models.CharField(max_length=100, blank=True, null=True)
    latest_modify_by = models.CharField(max_length=100, blank=True, null=True)
    latest_modify_date = models.CharField(max_length=100, blank=True, null=True)
    latest_modify_form = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_inventory_qty_live'


class TblProductJoblotDetails1(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_joblot_details1'


class TblProductJoblotDetails2(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_joblot_details2'


class TblProductJoblotDetails3(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_joblot_details3'


class TblProductJoblotDetails4(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_joblot_details4'


class TblProductJoblotDetails5(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_joblot_details5'


class TblProductJoblotProfile(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    desc_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    customer = models.CharField(max_length=250, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    mfg_date_from = models.DateField(blank=True, null=True)
    mfg_date_to = models.DateField(blank=True, null=True)
    charging_date_from = models.DateField(blank=True, null=True)
    charging_date_to = models.DateField(blank=True, null=True)
    date_completed = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=250, blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    pd_one = models.IntegerField(blank=True, null=True)
    pd_one_desc = models.CharField(max_length=250, blank=True, null=True)
    pd_two = models.IntegerField(blank=True, null=True)
    pd_two_desc = models.CharField(max_length=250, blank=True, null=True)
    pd_three = models.IntegerField(blank=True, null=True)
    pd_three_desc = models.CharField(max_length=250, blank=True, null=True)
    pd_four = models.IntegerField(blank=True, null=True)
    pd_four_desc = models.CharField(max_length=250, blank=True, null=True)
    pd_five = models.IntegerField(blank=True, null=True)
    pd_five_desc = models.CharField(max_length=250, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=60, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=60, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_joblot_profile'


class TblProductJoblotSummaryList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    required_field1 = models.CharField(max_length=1, blank=True, null=True)
    required_add1 = models.CharField(db_column='required_Add1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    required_increment1 = models.CharField(max_length=1, blank=True, null=True)
    required_change1 = models.CharField(db_column='required_Change1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    details_name1 = models.CharField(db_column='Details_Name1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    required_field2 = models.CharField(max_length=1, blank=True, null=True)
    required_add2 = models.CharField(db_column='required_Add2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    required_increment2 = models.CharField(max_length=1, blank=True, null=True)
    required_change2 = models.CharField(db_column='required_Change2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    details_name2 = models.CharField(db_column='Details_Name2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    required_field3 = models.CharField(max_length=1, blank=True, null=True)
    required_add3 = models.CharField(db_column='required_Add3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    required_increment3 = models.CharField(max_length=1, blank=True, null=True)
    required_change3 = models.CharField(db_column='required_Change3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    details_name3 = models.CharField(db_column='Details_Name3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    required_field4 = models.CharField(max_length=1, blank=True, null=True)
    required_add4 = models.CharField(db_column='required_Add4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    required_increment4 = models.CharField(max_length=1, blank=True, null=True)
    required_change4 = models.CharField(db_column='required_Change4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    details_name4 = models.CharField(db_column='Details_Name4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    required_field5 = models.CharField(max_length=1, blank=True, null=True)
    required_add5 = models.CharField(db_column='required_Add5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    required_increment5 = models.CharField(max_length=1, blank=True, null=True)
    required_change5 = models.CharField(db_column='required_Change5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    details_name5 = models.CharField(db_column='Details_Name5', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_product_joblot_summary_list'


class TblProductJplList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    doc_date = models.DateField(blank=True, null=True)
    jpl_no = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    jpl_date = models.DateField(blank=True, null=True)
    jpl_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_jpl_list'
        unique_together = (('doc_date', 'jpl_no', 'jpl_date', 'jpl_status'),)


class TblProductLogs(models.Model):
    user_id = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    activity = models.CharField(max_length=100, blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    reference_no = models.CharField(max_length=50, blank=True, null=True)
    system_version = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_logs'


class TblProductMovingInfo(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    moving_ave = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_moving_info'


class TblProductMultiplePrice(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    bar_code = models.CharField(max_length=20)
    site_code = models.IntegerField()
    price_type = models.CharField(db_column='Price_type', max_length=20)  # Field name made lowercase.
    price_name = models.CharField(max_length=100, blank=True, null=True)
    amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tbl_product_multiple_price'


class TblProductMultiplePriceLogs(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    activity = models.CharField(max_length=150, blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    reference_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_multiple_price_logs'


class TblProductOtherCreditSetup(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    cr_code = models.PositiveIntegerField(blank=True, null=True)
    cr_desc = models.CharField(max_length=150, blank=True, null=True)
    acct_code = models.FloatField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    pmt_type = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_other_credit_setup'


class TblProductOtherInfo(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    bar_code = models.CharField(unique=True, max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    min_qty = models.FloatField(blank=True, null=True)
    max_qty = models.FloatField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)
    req_inv_bld_up = models.FloatField(blank=True, null=True)
    days_trans_stock = models.FloatField(blank=True, null=True)
    daily_ave_sales = models.FloatField(blank=True, null=True)
    last_sales_date = models.DateField(blank=True, null=True)
    salesman = models.CharField(max_length=60, blank=True, null=True)
    vendor = models.CharField(max_length=60, blank=True, null=True)
    phase_out = models.CharField(max_length=1, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    trade = models.CharField(max_length=1, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    serial_no = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_other_info'


class TblProductOtherPmtSetup(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    pmt_code = models.PositiveIntegerField(blank=True, null=True)
    pmt_desc = models.CharField(max_length=150, blank=True, null=True)
    acct_code = models.FloatField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    pmt_type = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_other_pmt_setup'


class TblProductPmttypeSetup(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    pmt_code = models.PositiveIntegerField(blank=True, null=True)
    pmt_desc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_pmttype_setup'


class TblProductPoCurrency(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    acronym = models.CharField(max_length=5, blank=True, null=True)
    currency_name = models.CharField(max_length=50, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_po_currency'


class TblProductPoList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    po_terms = models.CharField(max_length=50, blank=True, null=True)
    po_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    po_date = models.CharField(max_length=25, blank=True, null=True)
    date_expected = models.DateField(blank=True, null=True)
    po_status = models.CharField(max_length=25, blank=True, null=True)
    rs_no = models.IntegerField(blank=True, null=True)
    shipto = models.CharField(max_length=150, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    supplier_code = models.IntegerField(blank=True, null=True)
    supplier = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    contact_no = models.CharField(max_length=25, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    po_currency = models.CharField(max_length=3, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)
    net_vat = models.FloatField(blank=True, null=True)
    net_discount = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    lvl_disc1 = models.FloatField(blank=True, null=True)
    lvl_disc2 = models.FloatField(blank=True, null=True)
    lvl_disc3 = models.FloatField(blank=True, null=True)
    lvl_disc4 = models.FloatField(blank=True, null=True)
    lvl_disc5 = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)
    auto_retransfer = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_po_list'
        unique_together = (('ul_code', 'po_no', 'po_date', 'supplier'),)


class TblProductPoListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    po_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    po_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    specification = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    disc_amt = models.FloatField(blank=True, null=True)
    vat_amt = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    qty_served = models.FloatField(blank=True, null=True)
    qty_cancel = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    pr_no = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_po_listing'
        unique_together = (('ul_code', 'po_no', 'po_date', 'bar_code', 'description', 'line_number'),)


class TblProductPoPr(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    po_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    pr_no = models.IntegerField(blank=True, null=True)
    pr_date = models.DateField(blank=True, null=True)
    pr_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_po_pr'
        unique_together = (('po_no', 'pr_no', 'pr_date', 'pr_status'),)


class TblProductPoTerms(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_po_terms'


class TblProductPrList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    pr_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=25, blank=True, null=True)
    pr_date = models.CharField(max_length=25, blank=True, null=True)
    date_expected = models.DateField(blank=True, null=True)
    pr_status = models.CharField(max_length=25, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=100, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_pr_list'
        unique_together = (('ul_code', 'pr_no', 'doc_type', 'pr_date', 'sl_name'),)


class TblProductPrListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    pr_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    pr_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    qty_served = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_pr_listing'
        unique_together = (('ul_code', 'pr_no', 'pr_date', 'bar_code', 'description', 'line_number'),)


class TblProductPriceChange(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    pci_no = models.FloatField(blank=True, null=True)
    reason = models.CharField(max_length=400, blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    date_apply = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=60, blank=True, null=True)
    apply_by = models.CharField(max_length=60, blank=True, null=True)
    line_number = models.IntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=60, blank=True, null=True)
    brand = models.CharField(max_length=60, blank=True, null=True)
    p_size = models.CharField(max_length=60, blank=True, null=True)
    curr_price = models.FloatField(blank=True, null=True)
    new_price = models.FloatField(blank=True, null=True)
    variance = models.FloatField(blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    received_by = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_price_change'
        unique_together = (('pci_no', 'date_trans', 'date_apply', 'line_number', 'bar_code', 'description', 'category', 'curr_price', 'new_price', 'variance'),)


class TblProductPriceInfo(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    actual_price = models.FloatField(blank=True, null=True)
    mark_up = models.FloatField(blank=True, null=True)
    qty_price1 = models.FloatField(blank=True, null=True)
    qty_markup1 = models.FloatField(blank=True, null=True)
    qty_perunit1 = models.FloatField(blank=True, null=True)
    qty_price2 = models.FloatField(blank=True, null=True)
    qty_markup2 = models.FloatField(blank=True, null=True)
    qty_perunit2 = models.FloatField(blank=True, null=True)
    qty_price3 = models.FloatField(blank=True, null=True)
    qty_markup3 = models.FloatField(blank=True, null=True)
    qty_perunit3 = models.FloatField(blank=True, null=True)
    promo_price = models.FloatField(blank=True, null=True)
    promo_markup = models.FloatField(blank=True, null=True)
    promo_datefrom = models.CharField(max_length=10, db_collation='latin1_bin', blank=True, null=True)
    promo_dateto = models.CharField(max_length=10, db_collation='latin1_bin', blank=True, null=True)
    apply_ws = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_price_info'
        unique_together = (('bar_code', 'actual_price', 'mark_up'),)


class TblProductPriceSetup(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=400, blank=True, null=True)
    line_number = models.IntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    mark_up = models.FloatField(blank=True, null=True)
    reg_price = models.FloatField(blank=True, null=True)
    qty1 = models.FloatField(blank=True, null=True)
    price1 = models.FloatField(blank=True, null=True)
    qty2 = models.FloatField(blank=True, null=True)
    price2 = models.FloatField(blank=True, null=True)
    qty3 = models.FloatField(blank=True, null=True)
    price3 = models.FloatField(blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    received_by = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_price_setup'
        unique_together = (('doc_no', 'date_trans', 'bar_code'),)


class TblProductPriceType(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    price_type = models.CharField(max_length=15, blank=True, null=True)
    price_name = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_price_type'


class TblProductPricechangeList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    effect_date = models.DateField(blank=True, null=True)
    executed_date = models.DateTimeField(blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    total_sku = models.FloatField(blank=True, null=True)
    price_status = models.CharField(max_length=15, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_pricechange_list'
        unique_together = (('ul_code', 'doc_no', 'doc_date'),)


class TblProductPricechangeListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    uom = models.CharField(max_length=30, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    old_price = models.FloatField(blank=True, null=True)
    new_price = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    mu_cost = models.FloatField(blank=True, null=True)
    mu_price = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_pricechange_listing'
        unique_together = (('ul_code', 'doc_no', 'doc_date', 'bar_code', 'description', 'line_number'),)


class TblProductPrincipalSetup(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    principal_id = models.PositiveIntegerField(blank=True, null=True)
    principal = models.CharField(max_length=100, blank=True, null=True)
    supplier_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_principal_setup'


class TblProductProdreceiveJpl(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    pr_no = models.PositiveIntegerField(blank=True, null=True)
    jpl_no = models.IntegerField(blank=True, null=True)
    jpl_description = models.CharField(max_length=100, blank=True, null=True)
    jpl_date = models.DateField(blank=True, null=True)
    jpl_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_prodreceive_jpl'
        unique_together = (('pr_no', 'jpl_no', 'jpl_date', 'jpl_status'),)


class TblProductProdreceiveList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    pr_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    pr_date = models.CharField(max_length=25, blank=True, null=True)
    production_code = models.IntegerField(blank=True, null=True)
    production_site = models.CharField(max_length=100, blank=True, null=True)
    jpl_code = models.IntegerField(blank=True, null=True)
    jpl_name = models.CharField(max_length=100, blank=True, null=True)
    pr_status = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_prodreceive_list'
        unique_together = (('ul_code', 'pr_no', 'pr_date'),)


class TblProductProdreceiveListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    pr_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    pr_date = models.CharField(max_length=25, db_collation='latin1_bin', blank=True, null=True)
    production_code = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    lot_no = models.IntegerField(blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    standard_cost = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    ave_cost = models.FloatField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    batch_no = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tbl_product_prodreceive_listing'
        unique_together = (('ul_code', 'pr_no', 'pr_date', 'bar_code', 'description', 'line_number'),)


class TblProductProdreceiveSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    pr_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    pr_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_prodreceive_sn_bc'


class TblProductProductionSetEntry(models.Model):
    autonum = models.BigAutoField(primary_key=True)  # The composite primary key (autonum, main_bar_code, uom) found, that is not supported. The first column is selected.
    main_bar_code = models.CharField(max_length=21)
    bar_code = models.CharField(max_length=21)
    description = models.CharField(max_length=150, blank=True, null=True)
    item_code = models.CharField(max_length=21, blank=True, null=True)
    qty_base_yield = models.FloatField(blank=True, null=True)
    uom = models.CharField(max_length=50)
    std_base_cost = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_production_set_entry'
        unique_together = (('autonum', 'main_bar_code', 'uom'),)


class TblProductProductionSetList(models.Model):
    autonum = models.BigAutoField(primary_key=True)  # The composite primary key (autonum, bar_code, uom) found, that is not supported. The first column is selected.
    bar_code = models.CharField(max_length=21)
    description = models.CharField(max_length=150, blank=True, null=True)
    item_code = models.CharField(max_length=21, blank=True, null=True)
    qty_base_yield = models.FloatField(blank=True, null=True)
    uom = models.CharField(max_length=50)
    std_base_cost = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_production_set_list'
        unique_together = (('autonum', 'bar_code', 'uom'),)


class TblProductProductionSetListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    main_bar_code = models.CharField(max_length=20, blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    pc_price = models.FloatField(blank=True, null=True)
    qtyperuom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    disc_amt = models.FloatField(blank=True, null=True)
    vat_amt = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    unit_cost = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    qty_served = models.FloatField(blank=True, null=True)
    qty_cancel = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    so_no = models.FloatField(blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_production_set_listing'


class TblProductPrsList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    sending_site = models.CharField(max_length=100, blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    prs_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    prs_date = models.CharField(max_length=25, blank=True, null=True)
    prs_status = models.CharField(max_length=25, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=150, blank=True, null=True)
    purpose = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=150, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_prs_list'
        unique_together = (('ul_code', 'prs_no', 'prs_date', 'sending_site'),)


class TblProductPrsListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    prs_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    prs_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    qty_served = models.FloatField(blank=True, null=True)
    qty_cancel = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_prs_listing'
        unique_together = (('ul_code', 'prs_no', 'prs_date', 'bar_code', 'description', 'line_number'),)


class TblProductPurchaseDetails(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    item_code = models.FloatField(blank=True, null=True)
    item_description = models.CharField(max_length=200, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_purchase_details'


class TblProductPurchaseDiscounts(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    particulars = models.CharField(max_length=150, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_purchase_discounts'


class TblProductReceiptAdvances(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    reference_no = models.CharField(max_length=20, blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    customer = models.CharField(max_length=150, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    payment = models.FloatField(blank=True, null=True)
    customer_code = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_receipt_advances'


class TblProductReceiptCard(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField()
    doc_date = models.DateField(blank=True, null=True)
    card_no = models.FloatField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    card_type = models.CharField(max_length=10, blank=True, null=True)
    drawee_bank = models.CharField(max_length=100, blank=True, null=True)
    bank_code = models.FloatField()
    payor = models.CharField(max_length=100, blank=True, null=True)
    appr_no = models.IntegerField(blank=True, null=True)
    card_amt = models.FloatField(blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_receipt_card'


class TblProductReceiptChk(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_no = models.FloatField()
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    check_no = models.FloatField(blank=True, null=True)
    check_date = models.DateField(blank=True, null=True)
    chk_type = models.CharField(max_length=1, blank=True, null=True)
    drawee_bank = models.CharField(max_length=100, blank=True, null=True)
    payor = models.CharField(max_length=100, blank=True, null=True)
    check_amt = models.FloatField(blank=True, null=True)
    cash_amt = models.FloatField(blank=True, null=True)
    check_status = models.CharField(max_length=10, blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_receipt_chk'


class TblProductReceiptColl(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    salesman_id = models.IntegerField(blank=True, null=True)
    salesman = models.CharField(max_length=100, blank=True, null=True)
    collector_id = models.IntegerField(blank=True, null=True)
    collector = models.CharField(max_length=100, blank=True, null=True)
    total_cash = models.FloatField(blank=True, null=True)
    total_check = models.FloatField(blank=True, null=True)
    total_pdc = models.FloatField(blank=True, null=True)
    total_others = models.FloatField(blank=True, null=True)
    total_online_payment = models.FloatField(blank=True, null=True)
    acct_type = models.CharField(max_length=10, blank=True, null=True)
    check_status = models.CharField(max_length=10, blank=True, null=True)
    deposit_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_receipt_coll'


class TblProductReceiptList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    payor = models.CharField(max_length=100, blank=True, null=True)
    payor_code = models.IntegerField(blank=True, null=True)
    payor_address = models.CharField(max_length=250, blank=True, null=True)
    contact_no = models.CharField(max_length=25, blank=True, null=True)
    acct_name = models.CharField(max_length=100, blank=True, null=True)
    collector = models.CharField(max_length=100, blank=True, null=True)
    online_id = models.IntegerField(blank=True, null=True)
    online_name = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    total_due = models.FloatField(blank=True, null=True)
    total_pmt = models.FloatField(blank=True, null=True)
    total_cash = models.FloatField(blank=True, null=True)
    total_check = models.FloatField(blank=True, null=True)
    total_pdc = models.FloatField(blank=True, null=True)
    total_cr = models.FloatField(blank=True, null=True)
    other_payment = models.FloatField(blank=True, null=True)
    other_credit = models.FloatField(blank=True, null=True)
    online_payment = models.FloatField(blank=True, null=True)
    total_adv = models.FloatField(blank=True, null=True)
    short_over = models.FloatField(blank=True, null=True)
    advoroverpayment = models.CharField(max_length=25, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_receipt_list'


class TblProductReceiptListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    reference_no = models.CharField(max_length=20, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    acct_name = models.CharField(max_length=150, blank=True, null=True)
    amount_due = models.FloatField(blank=True, null=True)
    pmt_amount = models.FloatField(blank=True, null=True)
    acct_name_id = models.IntegerField(blank=True, null=True)
    salesman = models.CharField(max_length=150, blank=True, null=True)
    doctype_ref = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_receipt_listing'


class TblProductReceiptOther(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_no = models.FloatField()
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    particular = models.CharField(max_length=150, blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    sl_id = models.IntegerField(blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_receipt_other'


class TblProductReceiptOtherCredit(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_no = models.FloatField()
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    particular = models.CharField(max_length=150, blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    sl_id = models.IntegerField(blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_receipt_other_credit'


class TblProductReceiveList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    rr_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    rr_date = models.CharField(max_length=25, blank=True, null=True)
    rec_code = models.IntegerField(blank=True, null=True)
    receiving_site = models.CharField(max_length=100, blank=True, null=True)
    supplier_code = models.IntegerField(blank=True, null=True)
    supplier = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    terms = models.IntegerField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)
    net_vat = models.FloatField(blank=True, null=True)
    net_discount = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    lvl_disc1 = models.FloatField(blank=True, null=True)
    lvl_disc2 = models.FloatField(blank=True, null=True)
    lvl_disc3 = models.FloatField(blank=True, null=True)
    lvl_disc4 = models.FloatField(blank=True, null=True)
    lvl_disc5 = models.FloatField(blank=True, null=True)
    per_type = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)
    po_auto_created = models.CharField(max_length=50, blank=True, null=True)
    auto_retransfer = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_receive_list'
        unique_together = (('ul_code', 'rr_no', 'rr_date', 'supplier'),)


class TblProductReceiveListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    rr_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    rr_date = models.CharField(max_length=25, blank=True, null=True)
    rec_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    disc_amt = models.FloatField(blank=True, null=True)
    vat_amt = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    po_no = models.FloatField(blank=True, null=True)
    si_no = models.CharField(max_length=50, blank=True, null=True)
    dr_no = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_receive_listing'
        unique_together = (('ul_code', 'rr_no', 'rr_date', 'bar_code', 'description', 'line_number'),)


class TblProductReceivePo(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    rr_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    po_no = models.IntegerField(blank=True, null=True)
    po_terms = models.CharField(max_length=10)
    po_doc_type = models.CharField(max_length=10)
    po_date = models.DateField(blank=True, null=True)
    po_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_receive_po'
        unique_together = (('rr_no', 'po_no', 'po_date', 'po_status'),)


class TblProductReceiveSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    rr_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    rr_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_receive_sn_bc'


class TblProductReceiveissList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    rrdi_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    rrdi_date = models.CharField(max_length=25, blank=True, null=True)
    rec_code = models.IntegerField(blank=True, null=True)
    receiving_site = models.CharField(max_length=100, blank=True, null=True)
    supplier_code = models.IntegerField(blank=True, null=True)
    supplier = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    payment_scheme = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    pmt_mode = models.CharField(max_length=150, blank=True, null=True)
    terms = models.IntegerField(blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)
    net_vat = models.FloatField(blank=True, null=True)
    net_discount = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    lvl_disc1 = models.FloatField(blank=True, null=True)
    lvl_disc2 = models.FloatField(blank=True, null=True)
    lvl_disc3 = models.FloatField(blank=True, null=True)
    lvl_disc4 = models.FloatField(blank=True, null=True)
    lvl_disc5 = models.FloatField(blank=True, null=True)
    per_type = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)
    direct_issue = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_receiveiss_list'
        unique_together = (('ul_code', 'rrdi_no', 'rrdi_date', 'supplier'),)


class TblProductReceiveissListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    rrdi_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    rrdi_date = models.CharField(max_length=25, blank=True, null=True)
    rec_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    disc_amt = models.FloatField(blank=True, null=True)
    vat_amt = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    po_no = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_receiveiss_listing'
        unique_together = (('ul_code', 'rrdi_no', 'rrdi_date', 'bar_code', 'description', 'line_number'),)


class TblProductReceiveissPo(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    rrdi_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    po_no = models.IntegerField(blank=True, null=True)
    po_terms = models.CharField(max_length=10)
    po_doc_type = models.CharField(max_length=10)
    po_date = models.DateField(blank=True, null=True)
    po_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_receiveiss_po'
        unique_together = (('rrdi_no', 'po_no', 'po_date', 'po_status'),)


class TblProductReceiveissSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    rrdi_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    rrdi_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_receiveiss_sn_bc'


class TblProductReturnList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    return_no = models.FloatField(blank=True, null=True)
    return_date = models.CharField(max_length=25, blank=True, null=True)
    rec_code = models.IntegerField(blank=True, null=True)
    receiving_site = models.CharField(max_length=100, blank=True, null=True)
    supplier_code = models.IntegerField(blank=True, null=True)
    supplier = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    rr_no = models.IntegerField(blank=True, null=True)
    rr_date = models.CharField(max_length=10, db_collation='latin1_bin', blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_net = models.FloatField(blank=True, null=True)
    per_type = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, db_collation='latin1_general_ci', blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, db_collation='latin1_general_ci', blank=True, null=True)
    approved_by = models.CharField(max_length=60, db_collation='latin1_general_ci', blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_return_list'
        unique_together = (('ul_code', 'return_no', 'return_date', 'supplier', 'rr_no', 'rr_date', 'trans_type'),)


class TblProductReturnListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    return_no = models.FloatField(blank=True, null=True)
    return_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    inv_price = models.FloatField(blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_return_listing'
        unique_together = (('ul_code', 'return_no', 'return_date', 'bar_code', 'description', 'line_number'),)


class TblProductReturnPo(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    return_no = models.FloatField(blank=True, null=True)
    po_no = models.IntegerField(blank=True, null=True)
    po_date = models.DateField(blank=True, null=True)
    po_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_return_po'
        unique_together = (('return_no', 'po_no', 'po_date', 'po_status'),)


class TblProductReturnSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    return_no = models.FloatField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_return_sn_bc'


class TblProductRrAdjList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    ref_no = models.IntegerField(blank=True, null=True)
    adj_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    adj_date = models.CharField(max_length=25, blank=True, null=True)
    rec_code = models.IntegerField(blank=True, null=True)
    receiving_site = models.CharField(max_length=100, blank=True, null=True)
    supplier_code = models.IntegerField(blank=True, null=True)
    supplier = models.CharField(max_length=100, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_rr_adj_list'
        unique_together = (('ul_code', 'adj_no', 'adj_date', 'supplier'),)


class TblProductRrAdjListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    adj_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    adj_date = models.CharField(max_length=25, blank=True, null=True)
    rec_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    disc_amt = models.FloatField(blank=True, null=True)
    vat_amt = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_rr_adj_listing'
        unique_together = (('ul_code', 'adj_no', 'adj_date', 'bar_code', 'description', 'line_number'),)


class TblProductRrAdjListing2(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    adj_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    adj_date = models.CharField(max_length=25, blank=True, null=True)
    rr_no = models.FloatField(blank=True, null=True)
    rr_doctype = models.CharField(max_length=10, blank=True, null=True)
    rr_date = models.DateField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    cost_adj = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_rr_adj_listing2'
        unique_together = (('ul_code', 'adj_no', 'adj_date', 'bar_code', 'description', 'line_number'),)


class TblProductRrReturnList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    prs_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    prs_date = models.CharField(max_length=25, blank=True, null=True)
    rec_code = models.IntegerField(blank=True, null=True)
    receiving_site = models.CharField(max_length=100, blank=True, null=True)
    supplier_code = models.IntegerField(blank=True, null=True)
    supplier = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)
    net_vat = models.FloatField(blank=True, null=True)
    net_discount = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    lvl_disc1 = models.FloatField(blank=True, null=True)
    lvl_disc2 = models.FloatField(blank=True, null=True)
    lvl_disc3 = models.FloatField(blank=True, null=True)
    lvl_disc4 = models.FloatField(blank=True, null=True)
    lvl_disc5 = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_rr_return_list'
        unique_together = (('ul_code', 'prs_no', 'prs_date', 'supplier'),)


class TblProductRrReturnListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    prs_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    prs_date = models.CharField(max_length=25, blank=True, null=True)
    rec_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    disc_amt = models.FloatField(blank=True, null=True)
    vat_amt = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_rr_return_listing'
        unique_together = (('ul_code', 'prs_no', 'prs_date', 'bar_code', 'description', 'line_number'),)


class TblProductRrReturnListing2(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    prs_no = models.FloatField(blank=True, null=True)
    prs_date = models.CharField(max_length=25, blank=True, null=True)
    reference_no = models.CharField(max_length=20, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    amount_due = models.FloatField(blank=True, null=True)
    amount_apply = models.FloatField(blank=True, null=True)
    acct_name_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_rr_return_listing2'


class TblProductRrReturnSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    prs_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    prs_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_rr_return_sn_bc'


class TblProductRsList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    rs_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    rs_date = models.CharField(max_length=25, blank=True, null=True)
    rs_status = models.CharField(max_length=25, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=150, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    sending_site = models.CharField(max_length=100, blank=True, null=True)
    purpose = models.CharField(max_length=250, blank=True, null=True)
    remarks = models.CharField(max_length=150, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_rs_list'
        unique_together = (('ul_code', 'rs_no', 'rs_date', 'sending_site'),)


class TblProductRsListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    rs_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    rs_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    qty_served = models.FloatField(blank=True, null=True)
    qty_cancel = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_rs_listing'
        unique_together = (('ul_code', 'rs_no', 'rs_date', 'bar_code', 'description', 'line_number'),)


class TblProductSales(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.PositiveIntegerField(blank=True, null=True)
    register_no = models.PositiveIntegerField(blank=True, null=True)
    receipt_no = models.PositiveIntegerField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    qty = models.PositiveIntegerField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    regular_price = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    customer = models.CharField(max_length=60, blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    cashier = models.CharField(max_length=60, blank=True, null=True)
    bagger = models.CharField(max_length=60, blank=True, null=True)
    cash_amt = models.FloatField(blank=True, null=True)
    credit_card = models.FloatField(blank=True, null=True)
    check_pmt = models.FloatField(blank=True, null=True)
    gift_check = models.FloatField(blank=True, null=True)
    other_pmt = models.FloatField(blank=True, null=True)
    pmt_type = models.CharField(max_length=3, blank=True, null=True)
    terminal_no = models.IntegerField(blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales'
        unique_together = (('ul_code', 'register_no', 'receipt_no', 'date_trans', 'bar_code', 'description', 'regular_price'),)


class TblProductSalesHistory(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.PositiveIntegerField(blank=True, null=True)
    register_no = models.PositiveIntegerField(blank=True, null=True)
    receipt_no = models.PositiveIntegerField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    regular_price = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    customer = models.CharField(max_length=60, blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    cashier = models.CharField(max_length=60, blank=True, null=True)
    bagger = models.CharField(max_length=60, blank=True, null=True)
    cash_amt = models.FloatField(blank=True, null=True)
    credit_card = models.FloatField(blank=True, null=True)
    gift_check = models.FloatField(blank=True, null=True)
    check_pmt = models.FloatField(blank=True, null=True)
    debit_card = models.FloatField(blank=True, null=True)
    po = models.FloatField(blank=True, null=True)
    multiple = models.FloatField(blank=True, null=True)
    credit_sales = models.FloatField(blank=True, null=True)
    other_pmt = models.FloatField(blank=True, null=True)
    pmt_type = models.CharField(max_length=3, blank=True, null=True)
    terminal_no = models.IntegerField(blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales_history'
        unique_together = (('ul_code', 'register_no', 'receipt_no', 'date_trans', 'bar_code', 'description', 'regular_price'),)


class TblProductSalesInvoiceAdvances(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    reference_no = models.CharField(max_length=20, blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    customer = models.CharField(max_length=150, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    payment = models.FloatField(blank=True, null=True)
    customer_code = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales_invoice_advances'


class TblProductSalesInvoiceCard(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField()
    doc_date = models.DateField(blank=True, null=True)
    card_no = models.FloatField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    card_type = models.CharField(max_length=10, blank=True, null=True)
    drawee_bank = models.CharField(max_length=100, blank=True, null=True)
    bank_code = models.FloatField()
    payor = models.CharField(max_length=100, blank=True, null=True)
    appr_no = models.IntegerField(blank=True, null=True)
    card_amt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales_invoice_card'


class TblProductSalesInvoiceChk(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField()
    check_no = models.FloatField(blank=True, null=True)
    check_date = models.DateField(blank=True, null=True)
    chk_type = models.CharField(max_length=1, blank=True, null=True)
    drawee_bank = models.CharField(max_length=100, blank=True, null=True)
    payor = models.CharField(max_length=100, blank=True, null=True)
    check_amt = models.FloatField(blank=True, null=True)
    check_status = models.CharField(max_length=10, blank=True, null=True)
    deposit_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales_invoice_chk'


class TblProductSalesInvoiceList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    so_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    dr_no = models.FloatField(blank=True, null=True)
    agent = models.CharField(max_length=100, blank=True, null=True)
    customer_code = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_address = models.CharField(max_length=250, blank=True, null=True)
    business_unit = models.CharField(max_length=100, blank=True, null=True)
    salesman_id = models.IntegerField(blank=True, null=True)
    salesman = models.CharField(max_length=100, blank=True, null=True)
    collector_id = models.IntegerField(blank=True, null=True)
    collector = models.CharField(max_length=100, blank=True, null=True)
    section_id = models.IntegerField(blank=True, null=True)
    section_name = models.CharField(max_length=100, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    terms = models.IntegerField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    total_cash = models.FloatField(blank=True, null=True)
    total_check = models.FloatField(blank=True, null=True)
    total_pdc = models.FloatField(blank=True, null=True)
    total_cr = models.FloatField(blank=True, null=True)
    total_credit_sales = models.FloatField(blank=True, null=True)
    total_online_payment = models.FloatField(db_column='total_Online_Payment', blank=True, null=True)  # Field name made lowercase.
    other_payment = models.FloatField(blank=True, null=True)
    total_adv = models.FloatField(blank=True, null=True)
    total_overpayment = models.FloatField(blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)
    net_vat = models.FloatField(blank=True, null=True)
    net_discount = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    lvl_disc1 = models.FloatField(blank=True, null=True)
    lvl_disc2 = models.FloatField(blank=True, null=True)
    lvl_disc3 = models.FloatField(blank=True, null=True)
    lvl_disc4 = models.FloatField(blank=True, null=True)
    lvl_disc5 = models.FloatField(blank=True, null=True)
    payment_status = models.CharField(max_length=10, blank=True, null=True)
    hmo = models.CharField(db_column='HMO', max_length=150, blank=True, null=True)  # Field name made lowercase.
    phic = models.CharField(db_column='PHIC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(max_length=400, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    joblot_id = models.IntegerField(db_column='jobLot_id', blank=True, null=True)  # Field name made lowercase.
    joblot_name = models.CharField(db_column='jobLot_name', max_length=250, blank=True, null=True)  # Field name made lowercase.
    billing_period_type = models.CharField(max_length=100)
    billing_year_month = models.CharField(max_length=100)
    billing_period_sub1 = models.CharField(max_length=100)
    billing_period_sub2 = models.CharField(max_length=100)
    billing_period_sub3 = models.CharField(max_length=100)
    trans_post = models.CharField(max_length=1, blank=True, null=True)
    delivery_id = models.IntegerField(blank=True, null=True)
    delivery = models.CharField(max_length=100, blank=True, null=True)
    so_auto_created = models.CharField(max_length=50, blank=True, null=True)
    auto_retransfer = models.CharField(max_length=1, blank=True, null=True)
    control_no = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales_invoice_list'


class TblProductSalesInvoiceListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    pc_price = models.FloatField(blank=True, null=True)
    qtyperuom = models.FloatField(blank=True, null=True)
    disc_amt = models.FloatField(blank=True, null=True)
    effective_rate = models.CharField(max_length=100, blank=True, null=True)
    lvl_disc1 = models.FloatField(blank=True, null=True)
    lvl_disc2 = models.FloatField(blank=True, null=True)
    lvl_disc3 = models.FloatField(blank=True, null=True)
    lvl_disc4 = models.FloatField(blank=True, null=True)
    lvl_disc5 = models.FloatField(blank=True, null=True)
    vat_amt = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    unit_cost = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    so_no = models.FloatField(blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales_invoice_listing'


class TblProductSalesInvoiceOther(models.Model):
    ul_code = models.IntegerField(blank=True, null=True)
    doc_no = models.FloatField()
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    particular = models.CharField(max_length=150, blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    sl_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales_invoice_other'


class TblProductSalesInvoiceSetListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=25, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    main_bar_code = models.CharField(max_length=20, blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    pc_price = models.FloatField(blank=True, null=True)
    qtyperuom = models.FloatField(blank=True, null=True)
    disc_amt = models.FloatField(blank=True, null=True)
    vat_amt = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    unit_cost = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    so_no = models.FloatField(blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)
    variable_percentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales_invoice_set_listing'


class TblProductSalesInvoiceSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales_invoice_sn_bc'


class TblProductSalesInvoiceSo(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    so_no = models.IntegerField(blank=True, null=True)
    so_doc_type = models.CharField(max_length=10, blank=True, null=True)
    so_date = models.DateField(blank=True, null=True)
    so_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales_invoice_so'
        unique_together = (('doc_no', 'doc_type', 'so_no', 'so_date', 'so_status'),)


class TblProductSalesOrderList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    so_no = models.PositiveIntegerField(blank=True, null=True)
    so_date = models.CharField(max_length=25, blank=True, null=True)
    customer_code = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_address = models.CharField(max_length=250, blank=True, null=True)
    customer_contact = models.CharField(max_length=25, blank=True, null=True)
    pmt_type = models.CharField(max_length=25, blank=True, null=True)
    terms = models.IntegerField(blank=True, null=True)
    pmt_scheme = models.CharField(max_length=20, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales_order_list'
        unique_together = (('ul_code', 'so_no', 'so_date', 'customer_name', 'customer_contact', 'pmt_type', 'bar_code', 'description', 'line_number'),)


class TblProductSalesOrderListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    so_no = models.PositiveIntegerField(blank=True, null=True)
    so_date = models.CharField(max_length=25, blank=True, null=True)
    customer_code = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_address = models.CharField(max_length=250, blank=True, null=True)
    customer_contact = models.CharField(max_length=25, blank=True, null=True)
    pmt_type = models.CharField(max_length=25, blank=True, null=True)
    terms = models.IntegerField(blank=True, null=True)
    pmt_scheme = models.CharField(max_length=20, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales_order_listing'
        unique_together = (('ul_code', 'so_no', 'so_date', 'customer_name', 'customer_contact', 'pmt_type', 'bar_code', 'description', 'line_number'),)


class TblProductSalesReturnList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    selling_site = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    si_ref = models.FloatField(blank=True, null=True)
    agent = models.CharField(max_length=100, blank=True, null=True)
    secondaryref = models.CharField(db_column='secondaryRef', max_length=500, blank=True, null=True)  # Field name made lowercase.
    customer_code = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_address = models.CharField(max_length=250, blank=True, null=True)
    business_unit = models.CharField(max_length=100, blank=True, null=True)
    salesman_id = models.IntegerField(blank=True, null=True)
    salesman = models.CharField(max_length=100, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    stdpricing = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)
    net_vat = models.FloatField(blank=True, null=True)
    net_discount = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    lvl_disc1 = models.FloatField(blank=True, null=True)
    lvl_disc2 = models.FloatField(blank=True, null=True)
    lvl_disc3 = models.FloatField(blank=True, null=True)
    lvl_disc4 = models.FloatField(blank=True, null=True)
    lvl_disc5 = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=400, blank=True, null=True)
    hmo = models.CharField(db_column='HMO', max_length=150, blank=True, null=True)  # Field name made lowercase.
    phic = models.CharField(db_column='PHIC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales_return_list'


class TblProductSalesReturnListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    si_no = models.FloatField(blank=True, null=True)
    si_type = models.CharField(max_length=10, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    pc_price = models.FloatField(blank=True, null=True)
    qtyperuom = models.FloatField(blank=True, null=True)
    disc_amt = models.FloatField(blank=True, null=True)
    vat_amt = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    unit_cost = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    ref_autonum = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales_return_listing'


class TblProductSalesReturnListing2(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    reference_no = models.CharField(max_length=20, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    amount_due = models.FloatField(blank=True, null=True)
    amount_apply = models.FloatField(blank=True, null=True)
    acct_name_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales_return_listing2'


class TblProductSalesReturnSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales_return_sn_bc'


class TblProductSalesTagging(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    mod_code = models.PositiveIntegerField(blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    product_desc = models.CharField(max_length=150, blank=True, null=True)
    vat_code = models.FloatField(blank=True, null=True)
    vat_title = models.CharField(max_length=150, blank=True, null=True)
    sl_code2 = models.FloatField(blank=True, null=True)
    sl_acct2 = models.CharField(max_length=150, blank=True, null=True)
    acct_code2 = models.FloatField(blank=True, null=True)
    acct_title2 = models.CharField(max_length=150, blank=True, null=True)
    discount_sl_code2 = models.FloatField(blank=True, null=True)
    discount_sl_acct2 = models.CharField(max_length=150, blank=True, null=True)
    nonvat_code = models.FloatField(blank=True, null=True)
    nonvat_title = models.CharField(max_length=150, blank=True, null=True)
    sl_code3 = models.FloatField(blank=True, null=True)
    sl_acct3 = models.CharField(max_length=150, blank=True, null=True)
    acct_code3 = models.FloatField(blank=True, null=True)
    acct_title3 = models.CharField(max_length=150, blank=True, null=True)
    discount_sl_code3 = models.FloatField(blank=True, null=True)
    discount_sl_acct3 = models.CharField(max_length=150, blank=True, null=True)
    zerorated_code = models.FloatField(blank=True, null=True)
    zerorated_title = models.CharField(max_length=150, blank=True, null=True)
    sl_code4 = models.FloatField(blank=True, null=True)
    sl_acct4 = models.CharField(max_length=150, blank=True, null=True)
    acct_code4 = models.FloatField(blank=True, null=True)
    acct_title4 = models.CharField(max_length=150)
    discount_sl_code4 = models.FloatField(blank=True, null=True)
    discount_sl_acct4 = models.CharField(max_length=150, blank=True, null=True)
    vatex_code = models.FloatField(blank=True, null=True)
    vatex_title = models.CharField(max_length=150, blank=True, null=True)
    sl_code5 = models.FloatField(blank=True, null=True)
    sl_acct5 = models.CharField(max_length=150, blank=True, null=True)
    acct_code5 = models.FloatField(blank=True, null=True)
    acct_title5 = models.CharField(max_length=150)
    discount_sl_code5 = models.FloatField(blank=True, null=True)
    discount_sl_acct5 = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_sales_tagging'


class TblProductSection(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    section_code = models.IntegerField(blank=True, null=True)
    section_desc = models.CharField(max_length=50, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_section'


class TblProductSiDraftList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    so_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    dr_no = models.FloatField(blank=True, null=True)
    agent = models.CharField(max_length=100, blank=True, null=True)
    customer_code = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_address = models.CharField(max_length=250, blank=True, null=True)
    business_unit = models.CharField(max_length=100, blank=True, null=True)
    salesman_id = models.IntegerField(blank=True, null=True)
    salesman = models.CharField(max_length=100, blank=True, null=True)
    collector_id = models.IntegerField(blank=True, null=True)
    collector = models.CharField(max_length=100, blank=True, null=True)
    section_id = models.IntegerField(blank=True, null=True)
    section_name = models.CharField(max_length=100, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    terms = models.IntegerField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    total_cash = models.FloatField(blank=True, null=True)
    total_check = models.FloatField(blank=True, null=True)
    total_pdc = models.FloatField(blank=True, null=True)
    total_cr = models.FloatField(blank=True, null=True)
    total_credit_sales = models.FloatField(blank=True, null=True)
    other_payment = models.FloatField(blank=True, null=True)
    total_adv = models.FloatField(blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)
    net_vat = models.FloatField(blank=True, null=True)
    net_discount = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    lvl_disc1 = models.FloatField(blank=True, null=True)
    lvl_disc2 = models.FloatField(blank=True, null=True)
    lvl_disc3 = models.FloatField(blank=True, null=True)
    lvl_disc4 = models.FloatField(blank=True, null=True)
    lvl_disc5 = models.FloatField(blank=True, null=True)
    payment_status = models.CharField(max_length=10, blank=True, null=True)
    hmo = models.CharField(db_column='HMO', max_length=150, blank=True, null=True)  # Field name made lowercase.
    phic = models.CharField(db_column='PHIC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(max_length=400, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_si_draft_list'


class TblProductSiDraftListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    pc_price = models.FloatField(blank=True, null=True)
    qtyperuom = models.FloatField(blank=True, null=True)
    disc_amt = models.FloatField(blank=True, null=True)
    vat_amt = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    unit_cost = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    so_no = models.FloatField(blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_si_draft_listing'


class TblProductSiDraftSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=50, blank=True, null=True)
    batch_code = models.CharField(max_length=50, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_si_draft_sn_bc'


class TblProductSiteSetup(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    site_code = models.PositiveIntegerField(blank=True, null=True)
    site_desc = models.CharField(max_length=100, blank=True, null=True)
    site_address = models.CharField(max_length=150, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_site_setup'


class TblProductSoList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    so_terms = models.CharField(max_length=50, blank=True, null=True)
    so_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    so_date = models.CharField(max_length=25, blank=True, null=True)
    date_expected = models.DateField(blank=True, null=True)
    so_status = models.CharField(max_length=25, blank=True, null=True)
    rs_no = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)
    shipto = models.CharField(max_length=150, blank=True, null=True)
    customer_code = models.IntegerField(blank=True, null=True)
    customer = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    contact_no = models.CharField(max_length=25, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)
    net_vat = models.FloatField(blank=True, null=True)
    net_discount = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    lvl_disc1 = models.FloatField(blank=True, null=True)
    lvl_disc2 = models.FloatField(blank=True, null=True)
    lvl_disc3 = models.FloatField(blank=True, null=True)
    lvl_disc4 = models.FloatField(blank=True, null=True)
    lvl_disc5 = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    collector_id = models.IntegerField(blank=True, null=True)
    collector = models.CharField(max_length=100, blank=True, null=True)
    salesman_id = models.IntegerField(blank=True, null=True)
    salesman = models.CharField(max_length=100, blank=True, null=True)
    auto_retransfer = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_so_list'
        unique_together = (('ul_code', 'so_no', 'so_date', 'customer'),)


class TblProductSoListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    so_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    so_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    specification = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    disc_amt = models.FloatField(blank=True, null=True)
    effective_rate = models.CharField(max_length=10, blank=True, null=True)
    lvl_disc1 = models.FloatField(blank=True, null=True)
    lvl_disc2 = models.FloatField(blank=True, null=True)
    lvl_disc3 = models.FloatField(blank=True, null=True)
    lvl_disc4 = models.FloatField(blank=True, null=True)
    lvl_disc5 = models.FloatField(blank=True, null=True)
    vat_amt = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    qty_served = models.FloatField(blank=True, null=True)
    qty_cancel = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_so_listing'
        unique_together = (('ul_code', 'so_no', 'so_date', 'bar_code', 'description', 'line_number'),)


class TblProductSoTerms(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_so_terms'


class TblProductStockBcDetails(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=20, blank=True, null=True)
    doc_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=50, blank=True, null=True)
    batch_qty = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    expiry_date = models.CharField(max_length=20, blank=True, null=True)
    ref_docno = models.FloatField(blank=True, null=True)
    ref_doctype = models.CharField(max_length=20, blank=True, null=True)
    ref_qty = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_bc_details'


class TblProductStockInList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    in_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    in_date = models.CharField(max_length=25, blank=True, null=True)
    rec_code = models.IntegerField(blank=True, null=True)
    receiving_site = models.CharField(max_length=100, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    sending_site = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    out_no = models.IntegerField(blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    req_no = models.IntegerField(blank=True, null=True)
    req_date = models.CharField(max_length=25, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=100, blank=True, null=True)
    reviewed_by = models.CharField(max_length=100, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=100, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)
    auto_retransfer = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_in_list'
        unique_together = (('ul_code', 'in_no', 'in_date', 'receiving_site', 'out_no', 'out_date'),)


class TblProductStockInListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    rec_code = models.IntegerField(blank=True, null=True)
    in_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    in_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    ave_cost = models.FloatField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_in_listing'


class TblProductStockInSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    in_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    in_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_in_sn_bc'


class TblProductStockIssList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    sending_site = models.CharField(max_length=100, blank=True, null=True)
    prod_code = models.IntegerField(blank=True, null=True)
    production_site = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    req_no = models.IntegerField(blank=True, null=True)
    req_date = models.CharField(max_length=10, db_collation='latin1_bin', blank=True, null=True)
    jpl_no = models.IntegerField(blank=True, null=True)
    jpl_date = models.CharField(max_length=10, db_collation='latin1_bin', blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_iss_list'
        unique_together = (('ul_code', 'out_no', 'out_date', 'sending_site', 'req_no', 'req_date', 'trans_type'),)


class TblProductStockIssList2(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    po_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    dr_no = models.FloatField(blank=True, null=True)
    terms = models.IntegerField(blank=True, null=True)
    customer_code = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    supplier_code = models.IntegerField(blank=True, null=True)
    supplier_name = models.CharField(max_length=100, blank=True, null=True)
    customer_address = models.CharField(max_length=250, blank=True, null=True)
    remarks = models.CharField(max_length=400, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)
    net_vat = models.FloatField(blank=True, null=True)
    net_discount = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    lvl_disc1 = models.FloatField(blank=True, null=True)
    lvl_disc2 = models.FloatField(blank=True, null=True)
    lvl_disc3 = models.FloatField(blank=True, null=True)
    lvl_disc4 = models.FloatField(blank=True, null=True)
    lvl_disc5 = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_iss_list2'


class TblProductStockIssListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    ave_cost = models.FloatField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_iss_listing'
        unique_together = (('ul_code', 'out_no', 'out_date', 'bar_code', 'description', 'line_number'),)


class TblProductStockIssListing2(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    pc_price = models.FloatField(blank=True, null=True)
    qtyperuom = models.FloatField(blank=True, null=True)
    disc_amt = models.FloatField(blank=True, null=True)
    vat_amt = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    unit_cost = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_iss_listing2'


class TblProductStockIssListing2SnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=50, blank=True, null=True)
    batch_code = models.CharField(max_length=50, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_iss_listing2_sn_bc'


class TblProductStockIssListingSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=50, blank=True, null=True)
    batch_code = models.CharField(max_length=50, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_iss_listing_sn_bc'


class TblProductStockIssPrs(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    prs_no = models.IntegerField(blank=True, null=True)
    prs_doc_type = models.CharField(max_length=10, blank=True, null=True)
    prs_date = models.DateField(blank=True, null=True)
    prs_status = models.CharField(max_length=20, blank=True, null=True)
    trans_type = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_iss_prs'
        unique_together = (('out_no', 'prs_no', 'prs_date', 'prs_status'),)


class TblProductStockIssRs(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    rs_no = models.IntegerField(blank=True, null=True)
    sir_doc_type = models.CharField(max_length=10, blank=True, null=True)
    rs_date = models.DateField(blank=True, null=True)
    rs_status = models.CharField(max_length=20, blank=True, null=True)
    trans_type = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_iss_rs'
        unique_together = (('out_no', 'rs_no', 'rs_date', 'rs_status'),)


class TblProductStockIssadjList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    ref_no = models.IntegerField(blank=True, null=True)
    adj_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    adj_date = models.CharField(max_length=25, blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    site_name = models.CharField(max_length=100, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issadj_list'
        unique_together = (('ul_code', 'adj_no', 'adj_date', 'sl_name'),)


class TblProductStockIssadjListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    adj_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    adj_date = models.CharField(max_length=25, blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    disc_amt = models.FloatField(blank=True, null=True)
    vat_amt = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issadj_listing'
        unique_together = (('ul_code', 'adj_no', 'adj_date', 'bar_code', 'description', 'line_number'),)


class TblProductStockIssadjListing2(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    adj_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    adj_date = models.CharField(max_length=25, blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    out_date = models.DateField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    cost_adj = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issadj_listing2'
        unique_together = (('ul_code', 'adj_no', 'adj_date', 'bar_code', 'description', 'line_number'),)


class TblProductStockIsscostList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    sending_site = models.CharField(max_length=100, blank=True, null=True)
    cost_code = models.IntegerField(blank=True, null=True)
    cost_center = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    req_no = models.IntegerField(blank=True, null=True)
    req_date = models.CharField(max_length=10, db_collation='latin1_bin', blank=True, null=True)
    req_status = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_isscost_list'
        unique_together = (('ul_code', 'out_no', 'out_date', 'sending_site', 'req_no', 'req_date', 'trans_type'),)


class TblProductStockIsscostListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    lot_no = models.IntegerField(blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    ave_cost = models.FloatField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    req_no = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)
    return_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_isscost_listing'
        unique_together = (('ul_code', 'out_no', 'out_date', 'bar_code', 'description', 'line_number'),)


class TblProductStockIsscostSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_isscost_sn_bc'


class TblProductStockIssempList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    sending_site = models.CharField(max_length=100, blank=True, null=True)
    emp_code = models.IntegerField(blank=True, null=True)
    employee = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    req_no = models.IntegerField(blank=True, null=True)
    req_date = models.CharField(max_length=10, db_collation='latin1_bin', blank=True, null=True)
    req_status = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issemp_list'
        unique_together = (('ul_code', 'out_no', 'out_date', 'sending_site', 'req_no', 'req_date', 'trans_type'),)


class TblProductStockIssempListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    lot_no = models.IntegerField(blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    ave_cost = models.FloatField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    req_no = models.IntegerField(blank=True, null=True)
    req_doc_type = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)
    return_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issemp_listing'
        unique_together = (('ul_code', 'out_no', 'out_date', 'bar_code', 'description', 'line_number'),)


class TblProductStockIssempSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issemp_sn_bc'


class TblProductStockIssheldList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    sending_site = models.CharField(max_length=100, blank=True, null=True)
    prod_code = models.IntegerField(blank=True, null=True)
    production_site = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    req_no = models.IntegerField(blank=True, null=True)
    req_date = models.CharField(max_length=10, db_collation='latin1_bin', blank=True, null=True)
    held_no = models.IntegerField(blank=True, null=True)
    trustor_name = models.CharField(max_length=100, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issheld_list'
        unique_together = (('ul_code', 'out_no', 'out_date', 'sending_site', 'req_no', 'req_date', 'trans_type'),)


class TblProductStockIssheldListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    lot_no = models.IntegerField(blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    ave_cost = models.FloatField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issheld_listing'
        unique_together = (('ul_code', 'out_no', 'out_date', 'bar_code', 'description', 'line_number'),)


class TblProductStockIssheldSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issheld_sn_bc'


class TblProductStockIssoaList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    sending_site = models.CharField(max_length=100, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    req_no = models.IntegerField(blank=True, null=True)
    req_date = models.CharField(max_length=10, db_collation='latin1_bin', blank=True, null=True)
    req_status = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issoa_list'
        unique_together = (('ul_code', 'out_no', 'out_date', 'sending_site', 'req_no', 'req_date', 'trans_type'),)


class TblProductStockIssoaListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    lot_no = models.IntegerField(blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    ave_cost = models.FloatField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    req_no = models.IntegerField(blank=True, null=True)
    req_doc_type = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)
    return_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issoa_listing'
        unique_together = (('ul_code', 'out_no', 'out_date', 'bar_code', 'description', 'line_number'),)


class TblProductStockIssoaSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issoa_sn_bc'


class TblProductStockIssprodJpl(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    out_no = models.PositiveIntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    jpl_no = models.IntegerField(blank=True, null=True)
    jpl_description = models.CharField(max_length=100, blank=True, null=True)
    jpl_date = models.DateField(blank=True, null=True)
    jpl_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issprod_jpl'
        unique_together = (('out_no', 'jpl_no', 'jpl_date', 'jpl_status'),)


class TblProductStockIssprodList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    sending_site = models.CharField(max_length=100, blank=True, null=True)
    prod_code = models.IntegerField(blank=True, null=True)
    production_site = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    req_no = models.IntegerField(blank=True, null=True)
    req_date = models.CharField(max_length=10, db_collation='latin1_bin', blank=True, null=True)
    jpl_no = models.IntegerField(blank=True, null=True)
    jpl_description = models.CharField(max_length=100, blank=True, null=True)
    jpl_date = models.CharField(max_length=10, db_collation='latin1_bin', blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)
    direct_issue = models.IntegerField(blank=True, null=True)
    ip_auto_created = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issprod_list'
        unique_together = (('ul_code', 'out_no', 'out_date', 'sending_site', 'req_no', 'req_date', 'trans_type'),)


class TblProductStockIssprodListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    lot_no = models.IntegerField(blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    ave_cost = models.FloatField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)
    req_no = models.FloatField(blank=True, null=True)
    req_doc_type = models.CharField(max_length=10, blank=True, null=True)
    return_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issprod_listing'
        unique_together = (('ul_code', 'out_no', 'out_date', 'bar_code', 'description', 'line_number'),)


class TblProductStockIssprodSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issprod_sn_bc'


class TblProductStockIssrespList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    sending_site = models.CharField(max_length=100, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    req_no = models.IntegerField(blank=True, null=True)
    req_date = models.CharField(max_length=10, db_collation='latin1_bin', blank=True, null=True)
    req_status = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issresp_list'
        unique_together = (('ul_code', 'out_no', 'out_date', 'sending_site', 'req_no', 'req_date', 'trans_type'),)


class TblProductStockIssrespListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    lot_no = models.IntegerField(blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    ave_cost = models.FloatField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    req_no = models.IntegerField(blank=True, null=True)
    req_doc_type = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)
    return_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issresp_listing'
        unique_together = (('ul_code', 'out_no', 'out_date', 'bar_code', 'description', 'line_number'),)


class TblProductStockIssrespSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issresp_sn_bc'


class TblProductStockIssreturnList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    in_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    in_date = models.CharField(max_length=25, blank=True, null=True)
    iss_no = models.CharField(max_length=250, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    sending_site = models.CharField(max_length=100, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issreturn_list'
        unique_together = (('ul_code', 'in_no', 'in_date', 'sending_site', 'trans_type'),)


class TblProductStockIssreturnListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    in_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    in_date = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    lot_no = models.IntegerField(blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    ave_cost = models.FloatField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    req_no = models.IntegerField(blank=True, null=True)
    req_doctype = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issreturn_listing'
        unique_together = (('ul_code', 'in_no', 'in_date', 'bar_code', 'description', 'line_number'),)


class TblProductStockIssreturnSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    in_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    in_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issreturn_sn_bc'


class TblProductStockIssrevList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    sending_site = models.CharField(max_length=100, blank=True, null=True)
    rev_code = models.IntegerField(blank=True, null=True)
    revenue_center = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    req_no = models.IntegerField(blank=True, null=True)
    req_date = models.CharField(max_length=10, db_collation='latin1_bin', blank=True, null=True)
    req_status = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issrev_list'
        unique_together = (('ul_code', 'out_no', 'out_date', 'sending_site', 'req_no', 'req_date', 'trans_type'),)


class TblProductStockIssrevListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    lot_no = models.IntegerField(blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    ave_cost = models.FloatField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    req_no = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)
    return_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issrev_listing'
        unique_together = (('ul_code', 'out_no', 'out_date', 'bar_code', 'description', 'line_number'),)


class TblProductStockIssrevSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_issrev_sn_bc'


class TblProductStockIsstransList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    po_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    dr_no = models.FloatField(blank=True, null=True)
    terms = models.IntegerField(blank=True, null=True)
    customer_code = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    supplier_code = models.IntegerField(blank=True, null=True)
    supplier_name = models.CharField(max_length=100, blank=True, null=True)
    customer_address = models.CharField(max_length=250, blank=True, null=True)
    principal_id = models.FloatField(blank=True, null=True)
    principal = models.CharField(max_length=250, blank=True, null=True)
    remarks = models.CharField(max_length=400, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)
    net_vat = models.FloatField(blank=True, null=True)
    net_discount = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    lvl_disc1 = models.FloatField(blank=True, null=True)
    lvl_disc2 = models.FloatField(blank=True, null=True)
    lvl_disc3 = models.FloatField(blank=True, null=True)
    lvl_disc4 = models.FloatField(blank=True, null=True)
    lvl_disc5 = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_isstrans_list'


class TblProductStockIsstransListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=40, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    pc_price = models.FloatField(blank=True, null=True)
    qtyperuom = models.FloatField(blank=True, null=True)
    disc_amt = models.FloatField(blank=True, null=True)
    vat_amt = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    unit_cost = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_isstrans_listing'


class TblProductStockIsstransListingSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=40, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=50, blank=True, null=True)
    batch_code = models.CharField(max_length=50, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_isstrans_listing_sn_bc'


class TblProductStockLedger(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    reference_no = models.FloatField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    moving_ave = models.FloatField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    running_qty = models.FloatField(blank=True, null=True)
    running_amt = models.FloatField(blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_ledger'


class TblProductStockLevelManagement(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    site_name = models.CharField(max_length=150, blank=True, null=True)
    bar_code = models.CharField(max_length=255, blank=True, null=True)
    short_desc = models.CharField(max_length=255, blank=True, null=True)
    item_code = models.CharField(max_length=255, blank=True, null=True)
    uom = models.CharField(max_length=255, blank=True, null=True)
    min_qty = models.FloatField(blank=True, null=True)
    max_qty = models.FloatField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)
    order_size = models.FloatField(blank=True, null=True)
    inv_buildup = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_level_management'
        unique_together = (('ul_code', 'site_code', 'site_name', 'bar_code', 'item_code'),)


class TblProductStockOutList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    sending_site = models.CharField(max_length=100, blank=True, null=True)
    rec_code = models.IntegerField(blank=True, null=True)
    receiving_site = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    in_no = models.IntegerField(blank=True, null=True)
    in_date = models.CharField(max_length=25, blank=True, null=True)
    req_no = models.IntegerField(blank=True, null=True)
    req_date = models.CharField(max_length=25, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)
    auto_retransfer = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_out_list'
        unique_together = (('ul_code', 'out_no', 'out_date', 'sending_site', 'req_no', 'req_date'),)


class TblProductStockOutListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.CharField(max_length=25, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    ave_cost = models.FloatField(blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)
    req_no = models.FloatField(blank=True, null=True)
    req_doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_out_listing'
        unique_together = (('ul_code', 'out_no', 'out_date', 'bar_code', 'description', 'line_number'),)


class TblProductStockOutSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_out_sn_bc'


class TblProductStockOutStr(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    out_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    out_date = models.DateField(blank=True, null=True)
    str_no = models.IntegerField(blank=True, null=True)
    str_doc_type = models.CharField(max_length=10, blank=True, null=True)
    str_date = models.DateField(blank=True, null=True)
    str_status = models.CharField(max_length=20, blank=True, null=True)
    trans_type = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_out_str'
        unique_together = (('out_no', 'str_no', 'str_date', 'str_status'),)


class TblProductStockSalesIssList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    dr_no = models.FloatField(blank=True, null=True)
    customer_code = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_address = models.CharField(max_length=250, blank=True, null=True)
    supplier_id = models.IntegerField(blank=True, null=True)
    supplier_name = models.CharField(max_length=100, blank=True, null=True)
    principal_id = models.IntegerField(blank=True, null=True)
    principal = models.CharField(max_length=100, blank=True, null=True)
    collector_id = models.IntegerField(blank=True, null=True)
    collector = models.CharField(max_length=100, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    saprice = models.CharField(db_column='SAPrice', max_length=25, blank=True, null=True)  # Field name made lowercase.
    terms = models.IntegerField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)
    net_vat = models.FloatField(blank=True, null=True)
    net_discount = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    lvl_disc1 = models.FloatField(blank=True, null=True)
    lvl_disc2 = models.FloatField(blank=True, null=True)
    lvl_disc3 = models.FloatField(blank=True, null=True)
    lvl_disc4 = models.FloatField(blank=True, null=True)
    lvl_disc5 = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=400, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_sales_iss_list'


class TblProductStockSalesIssListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    unit_price = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    pc_price = models.FloatField(blank=True, null=True)
    qtyperuom = models.FloatField(blank=True, null=True)
    disc_amt = models.FloatField(blank=True, null=True)
    vat_amt = models.FloatField(blank=True, null=True)
    net_total = models.FloatField(blank=True, null=True)
    unit_cost = models.FloatField(blank=True, null=True)
    vatable = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    so_no = models.FloatField(blank=True, null=True)
    batch_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_sales_iss_listing'


class TblProductStockSalesIssSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)
    serial_no = models.CharField(max_length=50, blank=True, null=True)
    batch_code = models.CharField(max_length=50, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    initial_source = models.CharField(max_length=150, blank=True, null=True)
    ref_autonum = models.BigIntegerField(blank=True, null=True)
    reorder_qty = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_sales_iss_sn_bc'


class TblProductStockSnBc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    origin_doc_no = models.FloatField(blank=True, null=True)
    origin_doc_type = models.CharField(max_length=10)
    initial_source = models.CharField(max_length=50, blank=True, null=True)
    doc_date = models.DateField(blank=True, null=True)
    bar_code = models.CharField(max_length=25, blank=True, null=True)
    item_code = models.CharField(max_length=25, blank=True, null=True)
    serial_no = models.CharField(max_length=25, blank=True, null=True)
    batch_code = models.CharField(max_length=25, blank=True, null=True)
    bc_qty = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    item_status = models.CharField(max_length=20, blank=True, null=True)
    item_docno = models.FloatField(blank=True, null=True)
    item_doctype = models.CharField(max_length=10, blank=True, null=True)
    item_served = models.FloatField(blank=True, null=True)
    sys_gen = models.CharField(max_length=1, blank=True, null=True)
    adj_docno = models.FloatField(blank=True, null=True)
    adj_doctype = models.CharField(max_length=10, blank=True, null=True)
    adj_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_stock_sn_bc'


class TblProductStrList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    str_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    str_date = models.CharField(max_length=25, blank=True, null=True)
    str_status = models.CharField(max_length=25, blank=True, null=True)
    rec_code = models.IntegerField(blank=True, null=True)
    receiving_site = models.CharField(max_length=150, blank=True, null=True)
    send_code = models.IntegerField(blank=True, null=True)
    sending_site = models.CharField(max_length=100, blank=True, null=True)
    date_need = models.CharField(max_length=20, blank=True, null=True)
    pricing = models.CharField(max_length=25, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    trans_post = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_str_list'
        unique_together = (('ul_code', 'str_no', 'str_date', 'sending_site'),)


class TblProductStrListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    str_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    str_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.PositiveIntegerField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    rec_qty = models.FloatField(blank=True, null=True)
    rec_uom = models.CharField(max_length=30, blank=True, null=True)
    qty_per_uom = models.FloatField(blank=True, null=True)
    sell_qty = models.FloatField(blank=True, null=True)
    sell_uom = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    net_cost = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField(blank=True, null=True)
    qty_served = models.FloatField(blank=True, null=True)
    qty_cancel = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_str_listing'
        unique_together = (('ul_code', 'str_no', 'str_date', 'bar_code', 'description', 'line_number'),)


class TblProductSupplier(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    supplier_code = models.IntegerField(blank=True, null=True)
    supplier_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_supplier'
        unique_together = (('bar_code', 'supplier_code', 'supplier_name', 'autonum'),)


class TblProductSystemSettings(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    reports_name = models.CharField(max_length=100, blank=True, null=True)
    view_reports = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_system_settings'


class TblProductTransType(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    type_of_trans = models.CharField(max_length=150, blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    doc_type = models.CharField(max_length=50, blank=True, null=True)
    balancing_figure = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_trans_type'


class TblProductType(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    item_code = models.PositiveIntegerField(blank=True, null=True)
    item_desc = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_type'


class TblProductUomInfo(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    reg_price = models.FloatField(blank=True, null=True)
    base_unit_uom = models.CharField(max_length=20, blank=True, null=True)
    rec_uom = models.CharField(max_length=20, blank=True, null=True)
    rec_uom_desc = models.CharField(max_length=40, blank=True, null=True)
    rec_uom_qty = models.FloatField(blank=True, null=True)
    rec_uom2 = models.CharField(max_length=20, blank=True, null=True)
    rec_uom_desc2 = models.CharField(max_length=40, blank=True, null=True)
    rec_uom_qty2 = models.FloatField(blank=True, null=True)
    rec_uom3 = models.CharField(max_length=20, blank=True, null=True)
    rec_uom_desc3 = models.CharField(max_length=40, blank=True, null=True)
    rec_uom_qty3 = models.FloatField(blank=True, null=True)
    stpurccost = models.FloatField(db_column='StPurcCost', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_product_uom_info'


class TblProductUomSetup(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    uom_code = models.PositiveIntegerField(blank=True, null=True)
    uom_desc = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_uom_setup'


class TblProductUpdate(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    last_update = models.CharField(max_length=25, blank=True, null=True)
    last_price = models.FloatField(blank=True, null=True)
    current_price = models.FloatField(blank=True, null=True)
    update_by = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_product_update'
        unique_together = (('bar_code', 'last_update', 'last_price', 'current_price', 'update_by'),)


class TblProductVirtualSetEntry(models.Model):
    autonum = models.BigAutoField(primary_key=True)  # The composite primary key (autonum, main_bar_code, price_type) found, that is not supported. The first column is selected.
    main_bar_code = models.CharField(max_length=21)
    bar_code = models.CharField(max_length=21)
    description = models.CharField(max_length=150, blank=True, null=True)
    item_code = models.CharField(max_length=21, blank=True, null=True)
    qty_per_component = models.FloatField(blank=True, null=True)
    unit_component_price = models.FloatField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    variable_percentage = models.FloatField(blank=True, null=True)
    price_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tbl_product_virtual_set_entry'
        unique_together = (('autonum', 'main_bar_code', 'price_type'),)


class TblProductVirtualSetList(models.Model):
    autonum = models.BigAutoField(primary_key=True)  # The composite primary key (autonum, bar_code, price_type) found, that is not supported. The first column is selected.
    bar_code = models.CharField(max_length=21)
    description = models.CharField(max_length=150, blank=True, null=True)
    item_code = models.CharField(max_length=21, blank=True, null=True)
    qty_per_set = models.FloatField(blank=True, null=True)
    unit_set_price = models.FloatField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    total_percentage = models.FloatField(blank=True, null=True)
    price_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tbl_product_virtual_set_list'
        unique_together = (('autonum', 'bar_code', 'price_type'),)


class TblPropertyEquip(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.PositiveIntegerField()
    serial_no = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=60, blank=True, null=True)
    personal_acctable = models.CharField(max_length=40, blank=True, null=True)
    prop_tag = models.CharField(max_length=40, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    category = models.CharField(max_length=150, blank=True, null=True)
    date_purch = models.DateField(blank=True, null=True)
    date_depr = models.DateField(blank=True, null=True)
    cost_item = models.FloatField(blank=True, null=True)
    equip_condition = models.CharField(max_length=30, blank=True, null=True)
    responsibility_name = models.CharField(max_length=150, blank=True, null=True)
    service_life = models.FloatField(blank=True, null=True)
    salvage_value = models.FloatField(blank=True, null=True)
    fair_value = models.FloatField(blank=True, null=True)
    supplier = models.CharField(max_length=40, blank=True, null=True)
    doc_ref_no = models.CharField(max_length=10, blank=True, null=True)
    dismantling_cost = models.FloatField(blank=True, null=True)
    annual_dep = models.FloatField(blank=True, null=True)
    net_book_value = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    beginning = models.FloatField(blank=True, null=True)
    provision = models.FloatField(blank=True, null=True)
    accu_dep = models.FloatField(blank=True, null=True)
    equip_image = models.TextField(blank=True, null=True)
    image_yn = models.CharField(max_length=1, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    profiling = models.CharField(db_column='Profiling', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_property_equip'
        unique_together = (('id_code', 'serial_no', 'department', 'personal_acctable', 'description', 'category', 'doc_ref_no'),)


class TblPropertyEquipSl(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.PositiveIntegerField()
    description = models.CharField(max_length=40, blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    beginning = models.FloatField(blank=True, null=True)
    provision = models.FloatField(blank=True, null=True)
    accu_dep = models.FloatField(blank=True, null=True)
    net_book_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_property_equip_sl'
        unique_together = (('autonum', 'id_code', 'description', 'date_trans', 'beginning', 'provision', 'accu_dep', 'net_book_value'),)


class TblPsAccountTagging(models.Model):
    autonum = models.AutoField(unique=True)
    ul_code = models.CharField(max_length=11, blank=True, null=True)
    rc_costcat_id = models.CharField(max_length=11, blank=True, null=True)
    rc_cost_category = models.CharField(max_length=250, blank=True, null=True)
    component_type = models.CharField(max_length=250, blank=True, null=True)
    payroll_component = models.CharField(max_length=250, blank=True, null=True)
    dr_cr = models.CharField(max_length=11, blank=True, null=True)
    acct_element = models.CharField(max_length=20, blank=True, null=True)
    account_code = models.CharField(max_length=100, blank=True, null=True)
    account_title = models.CharField(max_length=250, blank=True, null=True)
    sl_type = models.CharField(max_length=5, blank=True, null=True)
    sl_code = models.CharField(max_length=20, blank=True, null=True)
    sl_acct = models.CharField(max_length=350, blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.CharField(max_length=20, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    updated_timestamp = models.CharField(max_length=20, blank=True, null=True)
    approved_by = models.CharField(max_length=100, blank=True, null=True)
    approved_timestamp = models.CharField(max_length=20, blank=True, null=True)
    salary_type = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_account_tagging'


class TblPsAdjJournal(models.Model):
    auto_no = models.BigAutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    jv_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=400, blank=True, null=True)
    active = models.CharField(max_length=2, blank=True, null=True)
    prepared_by = models.CharField(max_length=150, blank=True, null=True)
    reviewed_by = models.CharField(max_length=150, blank=True, null=True)
    approved_by = models.CharField(max_length=150, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    payrollperiod = models.CharField(db_column='PayrollPeriod', max_length=999, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ps_adj_journal'


class TblPsApproveLeave(models.Model):
    auto_no = models.AutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    reference_code = models.IntegerField(blank=True, null=True)
    payrollperiod = models.CharField(db_column='PayrollPeriod', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_code = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    day = models.CharField(max_length=30, blank=True, null=True)
    leave_type = models.CharField(max_length=30, blank=True, null=True)
    shift_code = models.CharField(max_length=30, blank=True, null=True)
    time_from = models.CharField(max_length=30, blank=True, null=True)
    time_to = models.CharField(max_length=30, blank=True, null=True)
    hours = models.CharField(max_length=30, blank=True, null=True)
    set = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=999, blank=True, null=True)
    recommended_approved = models.CharField(max_length=50, blank=True, null=True)
    approved_by = models.CharField(max_length=50, blank=True, null=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    created_by = models.CharField(max_length=999, blank=True, null=True)
    updated_by = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=250, blank=True, null=True)
    approved_leave_with_pay = models.CharField(max_length=10, blank=True, null=True)
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    posted = models.CharField(max_length=30, blank=True, null=True)
    posted_by = models.CharField(max_length=30, blank=True, null=True)
    hours_worked_on_leave = models.CharField(max_length=30, blank=True, null=True)
    used_leave_hours = models.CharField(max_length=30, blank=True, null=True)
    cancelled_leave_hours = models.CharField(max_length=30, blank=True, null=True)
    sys_type = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_approve_leave'


class TblPsApproveLeaveList(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    doc_ref = models.CharField(max_length=11, blank=True, null=True)
    payroll_period = models.CharField(db_column='Payroll_Period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_code = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    day = models.CharField(max_length=30, blank=True, null=True)
    leave_type = models.CharField(max_length=30, blank=True, null=True)
    shift_code = models.CharField(max_length=30, blank=True, null=True)
    time_from = models.CharField(max_length=30, blank=True, null=True)
    time_to = models.CharField(max_length=30, blank=True, null=True)
    hours = models.CharField(max_length=30, blank=True, null=True)
    set = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=999, blank=True, null=True)
    recommended_approved = models.CharField(max_length=999, blank=True, null=True)
    approved_by = models.CharField(max_length=999, blank=True, null=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    created_by = models.CharField(max_length=999, blank=True, null=True)
    updated_by = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    approve_leave_with_pay = models.CharField(max_length=30, blank=True, null=True)
    posted = models.CharField(max_length=30, blank=True, null=True)
    posted_by = models.CharField(max_length=30, blank=True, null=True)
    sys_type = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_approve_leave_list'


class TblPsApproveLeaveListing(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    doc_ref = models.CharField(max_length=11, blank=True, null=True)
    payroll_period = models.CharField(db_column='Payroll_Period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_code = models.IntegerField(blank=True, null=True)
    employee = models.CharField(max_length=60, blank=True, null=True)
    employment_contract = models.CharField(max_length=30, blank=True, null=True)
    leave_date = models.CharField(max_length=30, blank=True, null=True)
    leave_type = models.CharField(max_length=30, blank=True, null=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    total_hours = models.CharField(max_length=30, blank=True, null=True)
    department = models.CharField(max_length=30, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=30, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    request_status = models.CharField(max_length=30, blank=True, null=True)
    approved_by = models.CharField(max_length=999, blank=True, null=True)
    reviewed_by = models.CharField(max_length=999, blank=True, null=True)
    created_by = models.CharField(max_length=999, blank=True, null=True)
    posted = models.CharField(max_length=30, blank=True, null=True)
    posted_by = models.CharField(max_length=30, blank=True, null=True)
    set = models.CharField(max_length=10, blank=True, null=True)
    sys_type = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_approve_leave_listing'


class TblPsApproveOt(models.Model):
    auto_no = models.AutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    reference_code = models.IntegerField(blank=True, null=True)
    payrollperiod = models.CharField(db_column='PayrollPeriod', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_code = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    day = models.CharField(max_length=30, blank=True, null=True)
    ot_type = models.CharField(max_length=30, blank=True, null=True)
    shift_code = models.CharField(max_length=30, blank=True, null=True)
    time_from = models.CharField(max_length=30, blank=True, null=True)
    time_to = models.CharField(max_length=30, blank=True, null=True)
    hours = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=999, blank=True, null=True)
    recommended_approved = models.CharField(max_length=50, blank=True, null=True)
    approved_by = models.CharField(max_length=50, blank=True, null=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    created_by = models.CharField(max_length=999, blank=True, null=True)
    updated_by = models.CharField(max_length=999, blank=True, null=True)
    od_no_nsd = models.CharField(max_length=30, blank=True, null=True)
    leg_no_nsd = models.CharField(max_length=30, blank=True, null=True)
    spl_no_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_no_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_leg_no_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_spl_no_nsd = models.CharField(max_length=30, blank=True, null=True)
    od_nsd = models.CharField(max_length=30, blank=True, null=True)
    leg_nsd = models.CharField(max_length=30, blank=True, null=True)
    spl_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_leg_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_spl_nsd = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=250, blank=True, null=True)
    doc_type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_approve_ot'


class TblPsApproveOtList(models.Model):
    auto_no = models.AutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    doc_ref = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    payrollperiod = models.CharField(db_column='PayrollPeriod', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_code = models.IntegerField(blank=True, null=True)
    employee = models.CharField(max_length=50, blank=True, null=True)
    employment_contract = models.CharField(max_length=30, blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    ot_type = models.CharField(max_length=30, blank=True, null=True)
    hours = models.CharField(max_length=30, blank=True, null=True)
    recommended_approved = models.CharField(max_length=50, blank=True, null=True)
    approved_by = models.CharField(max_length=50, blank=True, null=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    created_by = models.CharField(max_length=999, blank=True, null=True)
    updated_by = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_approve_ot_list'


class TblPsApproveOtListing(models.Model):
    auto_no = models.AutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    doc_ref = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    payrollperiod = models.CharField(db_column='PayrollPeriod', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_code = models.IntegerField(blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    day = models.CharField(max_length=30, blank=True, null=True)
    ot_type = models.CharField(max_length=30, blank=True, null=True)
    shift_code = models.CharField(max_length=30, blank=True, null=True)
    time_from = models.CharField(max_length=30, blank=True, null=True)
    time_to = models.CharField(max_length=30, blank=True, null=True)
    hours = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=999, blank=True, null=True)
    recommended_approved = models.CharField(max_length=50, blank=True, null=True)
    approved_by = models.CharField(max_length=50, blank=True, null=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    created_by = models.CharField(max_length=999, blank=True, null=True)
    updated_by = models.CharField(max_length=999, blank=True, null=True)
    od_no_nsd = models.CharField(max_length=30, blank=True, null=True)
    leg_no_nsd = models.CharField(max_length=30, blank=True, null=True)
    spl_no_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_no_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_leg_no_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_spl_no_nsd = models.CharField(max_length=30, blank=True, null=True)
    od_nsd = models.CharField(max_length=30, blank=True, null=True)
    leg_nsd = models.CharField(max_length=30, blank=True, null=True)
    spl_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_leg_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_spl_nsd = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_approve_ot_listing'


class TblPsApproveTravelOrder(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    doc_ref = models.CharField(max_length=11, blank=True, null=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    payroll_period = models.CharField(db_column='Payroll_Period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_code = models.IntegerField(blank=True, null=True)
    employee_name = models.CharField(max_length=999, blank=True, null=True)
    employment_contract = models.CharField(max_length=999, blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    day = models.CharField(max_length=30, blank=True, null=True)
    number_of_days = models.CharField(max_length=30, blank=True, null=True)
    hrs_equivalent = models.CharField(max_length=30, blank=True, null=True)
    travel_category = models.CharField(max_length=30, blank=True, null=True)
    destination = models.CharField(max_length=999, blank=True, null=True)
    funds_charged_to = models.CharField(max_length=999, blank=True, null=True)
    remarks = models.CharField(max_length=999, blank=True, null=True)
    recommended_approved = models.CharField(max_length=999, blank=True, null=True)
    approved_by = models.CharField(max_length=999, blank=True, null=True)
    updated_by = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    timeset = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_approve_travel_order'


class TblPsApproveTravelOrderList(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    doc_ref = models.CharField(max_length=11, blank=True, null=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    payroll_period = models.CharField(db_column='Payroll_Period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_code = models.IntegerField(blank=True, null=True)
    employee_name = models.CharField(max_length=999, blank=True, null=True)
    employment_contract = models.CharField(max_length=999, blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    travel_category = models.CharField(max_length=30, blank=True, null=True)
    destination = models.CharField(max_length=999, blank=True, null=True)
    total_number_of_days = models.CharField(max_length=30, blank=True, null=True)
    total_hrs_equivalent = models.CharField(max_length=30, blank=True, null=True)
    recommended_approved = models.CharField(max_length=999, blank=True, null=True)
    approved_by = models.CharField(max_length=999, blank=True, null=True)
    updated_by = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_approve_travel_order_list'


class TblPsApproveTravelOrderListing(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    doc_ref = models.CharField(max_length=11, blank=True, null=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    payroll_period = models.CharField(db_column='Payroll_Period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_code = models.IntegerField(blank=True, null=True)
    employee_name = models.CharField(max_length=999, blank=True, null=True)
    employment_contract = models.CharField(max_length=999, blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    day = models.CharField(max_length=30, blank=True, null=True)
    number_of_days = models.CharField(max_length=30, blank=True, null=True)
    hrs_equivalent = models.CharField(max_length=30, blank=True, null=True)
    travel_category = models.CharField(max_length=30, blank=True, null=True)
    destination = models.CharField(max_length=999, blank=True, null=True)
    funds_charged_to = models.CharField(max_length=999, blank=True, null=True)
    remarks = models.CharField(max_length=999, blank=True, null=True)
    recommended_approved = models.CharField(max_length=999, blank=True, null=True)
    approved_by = models.CharField(max_length=999, blank=True, null=True)
    updated_by = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    timeset = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_approve_travel_order_listing'


class TblPsApprovingOfficer(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    id_code = models.CharField(max_length=30, blank=True, null=True)
    rank = models.CharField(max_length=30, blank=True, null=True)
    employee_name = models.CharField(max_length=999, blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    system = models.CharField(max_length=999, blank=True, null=True)
    signatory_designation = models.CharField(max_length=9999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_approving_officer'


class TblPsAtu(models.Model):
    auto_no = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    department_desc = models.CharField(max_length=200, blank=True, null=True)
    responsibility_center = models.IntegerField(blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=200, blank=True, null=True)
    payroll_period = models.CharField(max_length=200, blank=True, null=True)
    hours_worked = models.FloatField(blank=True, null=True)
    absent = models.FloatField(blank=True, null=True)
    tardiness = models.FloatField(blank=True, null=True)
    undertime = models.FloatField(blank=True, null=True)
    working_days = models.FloatField(blank=True, null=True)
    sys_type = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_atu'


class TblPsAtuPerDay(models.Model):
    auto_no = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    department_desc = models.CharField(max_length=200, blank=True, null=True)
    responsibility_center = models.IntegerField(blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=200, blank=True, null=True)
    payroll_period = models.CharField(max_length=200, blank=True, null=True)
    date = models.CharField(max_length=20, blank=True, null=True)
    absent1 = models.FloatField(blank=True, null=True)
    tardiness1 = models.FloatField(blank=True, null=True)
    undertime1 = models.FloatField(blank=True, null=True)
    absent2 = models.FloatField(blank=True, null=True)
    tardiness2 = models.FloatField(blank=True, null=True)
    undertime2 = models.FloatField(blank=True, null=True)
    absent3 = models.FloatField(blank=True, null=True)
    tardiness3 = models.FloatField(blank=True, null=True)
    undertime3 = models.FloatField(blank=True, null=True)
    tardy_equivalent_in_minutes = models.FloatField(blank=True, null=True)
    tardy_equivalent_in_hours = models.FloatField(blank=True, null=True)
    undertime_equivalent_in_minutes = models.FloatField(blank=True, null=True)
    undertime_equivalent_in_hours = models.FloatField(blank=True, null=True)
    tardy_equivalent_in_minutes2 = models.FloatField(blank=True, null=True)
    tardy_equivalent_in_hours2 = models.FloatField(blank=True, null=True)
    undertime_equivalent_in_minutes2 = models.FloatField(blank=True, null=True)
    undertime_equivalent_in_hours2 = models.FloatField(blank=True, null=True)
    tardy_equivalent_in_minutes3 = models.FloatField(blank=True, null=True)
    tardy_equivalent_in_hours3 = models.FloatField(blank=True, null=True)
    undertime_equivalent_in_minutes3 = models.FloatField(blank=True, null=True)
    undertime_equivalent_in_hours3 = models.FloatField(blank=True, null=True)
    sys_type = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_atu_per_day'


class TblPsAtuPosted(models.Model):
    auto_no = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    department_desc = models.CharField(max_length=200, blank=True, null=True)
    responsibility_center = models.IntegerField(blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=200, blank=True, null=True)
    payroll_period = models.CharField(max_length=200, blank=True, null=True)
    hours_worked = models.FloatField(blank=True, null=True)
    absent = models.FloatField(blank=True, null=True)
    tardiness = models.FloatField(blank=True, null=True)
    undertime = models.FloatField(blank=True, null=True)
    working_days = models.FloatField(blank=True, null=True)
    tardy_equivalent_in_minutes = models.FloatField(blank=True, null=True)
    tardy_equivalent_in_hours = models.FloatField(blank=True, null=True)
    undertime_equivalent_in_minutes = models.FloatField(blank=True, null=True)
    undertime_equivalent_in_hours = models.FloatField(blank=True, null=True)
    batch_no = models.CharField(max_length=2, blank=True, null=True)
    sys_type = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_atu_posted'


class TblPsBrokenTime(models.Model):
    auto_no = models.AutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    id_code = models.IntegerField(blank=True, null=True)
    payrollperiod = models.CharField(db_column='PayrollPeriod', max_length=30, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=30, blank=True, null=True)
    day = models.CharField(max_length=30, blank=True, null=True)
    time_from = models.CharField(max_length=30, blank=True, null=True)
    time_to = models.CharField(max_length=30, blank=True, null=True)
    hours = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=999, blank=True, null=True)
    set = models.CharField(max_length=30, blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    created_by = models.CharField(max_length=999, blank=True, null=True)
    updated_by = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_broken_time'


class TblPsCodeRefNo(models.Model):
    autonum = models.AutoField(primary_key=True)
    description = models.CharField(max_length=25, blank=True, null=True)
    next_no = models.PositiveIntegerField(blank=True, null=True)
    long_desc = models.CharField(max_length=30, blank=True, null=True)
    updated_by = models.CharField(max_length=30, blank=True, null=True)
    created_by = models.CharField(max_length=30, blank=True, null=True)
    module = models.CharField(max_length=99, blank=True, null=True)
    terminal = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_code_ref_no'


class TblPsComputationHours(models.Model):
    auto_no = models.BigAutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2, blank=True, null=True)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code', blank=True, null=True)  # Field name made lowercase.
    factor_type = models.CharField(max_length=50, blank=True, null=True)
    od_reg = models.CharField(max_length=30, blank=True, null=True)
    od_ot = models.CharField(max_length=30, blank=True, null=True)
    od_nsd = models.CharField(max_length=30, blank=True, null=True)
    od_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    sh_reg = models.CharField(max_length=30, blank=True, null=True)
    sh_ot = models.CharField(max_length=30, blank=True, null=True)
    sh_nsd = models.CharField(max_length=30, blank=True, null=True)
    sh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    rh_reg = models.CharField(max_length=30, blank=True, null=True)
    rh_ot = models.CharField(max_length=30, blank=True, null=True)
    rh_nsd = models.CharField(max_length=30, blank=True, null=True)
    rh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    dh_reg = models.CharField(max_length=30, blank=True, null=True)
    dh_ot = models.CharField(max_length=30, blank=True, null=True)
    dh_nsd = models.CharField(max_length=30, blank=True, null=True)
    dh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_reg = models.CharField(max_length=30, blank=True, null=True)
    rd_ot = models.CharField(max_length=30, blank=True, null=True)
    rd_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_sh_reg = models.CharField(max_length=30, blank=True, null=True)
    rd_sh_ot = models.CharField(max_length=30, blank=True, null=True)
    rd_sh_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_sh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_rh_reg = models.CharField(max_length=30, blank=True, null=True)
    rd_rh_ot = models.CharField(max_length=30, blank=True, null=True)
    rd_rh_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_rh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_dh_reg = models.CharField(max_length=30, blank=True, null=True)
    rd_dh_ot = models.CharField(max_length=30, blank=True, null=True)
    rd_dh_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_dh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    date_from = models.CharField(max_length=50, blank=True, null=True)
    date_to = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_computation_hours'


class TblPsComputeBasicPay32Columns(models.Model):
    auto_no = models.BigAutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    id_code = models.IntegerField()
    employee_id = models.IntegerField()
    payroll_period = models.CharField(max_length=45, blank=True, null=True)
    department = models.CharField(max_length=11, blank=True, null=True)
    department_desc = models.CharField(max_length=500, blank=True, null=True)
    rc_costcat_id = models.CharField(max_length=10, blank=True, null=True)
    rc_cost_category = models.CharField(max_length=100, blank=True, null=True)
    responsibility_center = models.CharField(max_length=11, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=500, blank=True, null=True)
    salary_type = models.CharField(max_length=500, blank=True, null=True)
    option = models.CharField(max_length=3, blank=True, null=True)
    total_compensation = models.FloatField(blank=True, null=True)
    basic_pay = models.FloatField(blank=True, null=True)
    absences = models.FloatField(blank=True, null=True)
    undertime = models.FloatField(blank=True, null=True)
    late = models.FloatField(blank=True, null=True)
    regular_not_worked_holiday_pay = models.FloatField(blank=True, null=True)
    cola = models.FloatField(blank=True, null=True)
    leave_benefits = models.FloatField(blank=True, null=True)
    od_reg = models.FloatField(blank=True, null=True)
    od_ot = models.FloatField(blank=True, null=True)
    od_nsd = models.FloatField(blank=True, null=True)
    od_nsd_ot = models.FloatField(blank=True, null=True)
    sh_reg = models.FloatField(blank=True, null=True)
    sh_ot = models.FloatField(blank=True, null=True)
    sh_nsd = models.FloatField(blank=True, null=True)
    sh_nsd_ot = models.FloatField(blank=True, null=True)
    rh_reg = models.FloatField(blank=True, null=True)
    rh_ot = models.FloatField(blank=True, null=True)
    rh_nsd = models.FloatField(blank=True, null=True)
    rh_nsd_ot = models.FloatField(blank=True, null=True)
    dh_reg = models.FloatField(blank=True, null=True)
    dh_ot = models.FloatField(blank=True, null=True)
    dh_nsd = models.FloatField(blank=True, null=True)
    dh_nsd_ot = models.FloatField(blank=True, null=True)
    rd_reg = models.FloatField(blank=True, null=True)
    rd_ot = models.FloatField(blank=True, null=True)
    rd_nsd = models.FloatField(blank=True, null=True)
    rd_nsd_ot = models.FloatField(blank=True, null=True)
    rd_sh_reg = models.FloatField(blank=True, null=True)
    rd_sh_ot = models.FloatField(blank=True, null=True)
    rd_sh_nsd = models.FloatField(blank=True, null=True)
    rd_sh_nsd_ot = models.FloatField(blank=True, null=True)
    rd_rh_reg = models.FloatField(blank=True, null=True)
    rd_rh_ot = models.FloatField(blank=True, null=True)
    rd_rh_nsd = models.FloatField(blank=True, null=True)
    rd_rh_nsd_ot = models.FloatField(blank=True, null=True)
    rd_dh_reg = models.FloatField(blank=True, null=True)
    rd_dh_ot = models.FloatField(blank=True, null=True)
    rd_dh_nsd = models.FloatField(blank=True, null=True)
    rd_dh_nsd_ot = models.FloatField(blank=True, null=True)
    od_reg_h = models.FloatField(blank=True, null=True)
    od_nsd_h = models.FloatField(blank=True, null=True)
    sh_reg_h = models.FloatField(blank=True, null=True)
    sh_nsd_h = models.FloatField(blank=True, null=True)
    rh_reg_h = models.FloatField(blank=True, null=True)
    rh_nsd_h = models.FloatField(blank=True, null=True)
    dh_reg_h = models.FloatField(blank=True, null=True)
    dh_nsd_h = models.FloatField(blank=True, null=True)
    number_13_month = models.FloatField(db_column='13_month', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    od_nsd_p = models.FloatField(blank=True, null=True)
    sh_reg_p = models.FloatField(blank=True, null=True)
    sh_nsd_p = models.FloatField(blank=True, null=True)
    rh_reg_p = models.FloatField(blank=True, null=True)
    rh_nsd_p = models.FloatField(blank=True, null=True)
    dh_reg_p = models.FloatField(blank=True, null=True)
    dh_nsd_p = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    batch_no = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_compute_basic_pay_32_columns'


class TblPsDayCategory(models.Model):
    auto_num = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_day_category'


class TblPsDeductionPriority(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    deduction_type = models.CharField(max_length=25, blank=True, null=True)
    ded_code = models.IntegerField(blank=True, null=True)
    deduction_name = models.CharField(max_length=50, blank=True, null=True)
    seq_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_deduction_priority'


class TblPsDiscardedEntry(models.Model):
    auto_no = models.BigAutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    payrollperiod = models.CharField(db_column='PayrollPeriod', max_length=25, blank=True, null=True)  # Field name made lowercase.
    date_from = models.CharField(max_length=25, blank=True, null=True)
    date_to = models.CharField(max_length=25, blank=True, null=True)
    employee_id_code = models.CharField(max_length=20, blank=True, null=True)
    entry_id_code = models.CharField(max_length=20, blank=True, null=True)
    entry_name = models.CharField(max_length=300, blank=True, null=True)
    entry_type = models.CharField(max_length=20, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    payrollperiod_from = models.CharField(max_length=25, blank=True, null=True)
    status = models.CharField(max_length=25, blank=True, null=True)
    date_created = models.CharField(max_length=25, blank=True, null=True)
    date_regenerated = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_discarded_entry'


class TblPsDisposition(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    disposition = models.CharField(max_length=999, blank=True, null=True)
    disposition_type = models.CharField(max_length=999, blank=True, null=True)
    hours = models.CharField(max_length=999, blank=True, null=True)
    remarks = models.CharField(max_length=9999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_disposition'


class TblPsDtrPostedLogs(models.Model):
    autonum = models.AutoField(primary_key=True)
    emp_id = models.IntegerField(db_column='Emp_ID', blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(max_length=30)
    date = models.CharField(max_length=55, blank=True, null=True)
    day = models.CharField(max_length=50, blank=True, null=True)
    time_in = models.CharField(max_length=55, blank=True, null=True)
    time_out = models.CharField(max_length=55, blank=True, null=True)
    time_in2 = models.CharField(max_length=55, blank=True, null=True)
    time_out2 = models.CharField(max_length=55, blank=True, null=True)
    ot_in = models.CharField(max_length=55, blank=True, null=True)
    ot_out = models.CharField(max_length=55, blank=True, null=True)
    reg_hrs = models.CharField(max_length=11, blank=True, null=True)
    ot_hrs = models.CharField(max_length=11, blank=True, null=True)
    leave_hrs = models.CharField(max_length=15, blank=True, null=True)
    shift_sched = models.CharField(max_length=25, blank=True, null=True)
    resp_center = models.CharField(max_length=25, blank=True, null=True)
    period_status = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=60, blank=True, null=True)
    batch_no = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_dtr_posted_logs'


class TblPsDtrRectificationList(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    doc_ref = models.CharField(max_length=11, blank=True, null=True)
    payroll_period = models.CharField(db_column='Payroll_Period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    recommended_approved = models.CharField(max_length=999, blank=True, null=True)
    approved_by = models.CharField(max_length=999, blank=True, null=True)
    updated_by = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_dtr_rectification_list'


class TblPsDtrRectificationListing(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    doc_ref = models.CharField(max_length=11, blank=True, null=True)
    payroll_period = models.CharField(db_column='Payroll_Period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_code = models.IntegerField(blank=True, null=True)
    employee_name = models.CharField(max_length=999, blank=True, null=True)
    employment_contract = models.CharField(max_length=999, blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    time_set = models.CharField(max_length=10, blank=True, null=True)
    req_log_in = models.CharField(max_length=30, blank=True, null=True)
    req_log_out = models.CharField(max_length=30, blank=True, null=True)
    actual_log_in = models.CharField(max_length=30, blank=True, null=True)
    actual_log_out = models.CharField(max_length=30, blank=True, null=True)
    hours_worked = models.CharField(max_length=30, blank=True, null=True)
    tardy = models.CharField(max_length=30, blank=True, null=True)
    undertime = models.CharField(max_length=30, blank=True, null=True)
    awol = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=999, blank=True, null=True)
    rectified_data = models.CharField(max_length=30, blank=True, null=True)
    recommended_approved = models.CharField(max_length=999, blank=True, null=True)
    approved_by = models.CharField(max_length=999, blank=True, null=True)
    updated_by = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_dtr_rectification_listing'


class TblPsEmpdtr(models.Model):
    auto_no = models.BigAutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    emp_id = models.CharField(db_column='Emp_ID', max_length=15)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    timein_1 = models.CharField(db_column='TIMEIN_1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    timeout_1 = models.CharField(db_column='TIMEOUT_1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    timein_2 = models.CharField(db_column='TIMEIN_2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    timeout_2 = models.CharField(db_column='TIMEOUT_2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    timein_3 = models.CharField(db_column='TIMEIN_3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    timeout_3 = models.CharField(db_column='TIMEOUT_3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ot_timein = models.CharField(db_column='OT_TIMEIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ot_timeout = models.CharField(db_column='OT_TIMEOUT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    shiftsched = models.FloatField(db_column='ShiftSched', blank=True, null=True)  # Field name made lowercase.
    doc_type = models.CharField(max_length=50, blank=True, null=True)
    doc_ref = models.CharField(max_length=50, blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)
    sync_status_server5 = models.CharField(max_length=4, blank=True, null=True)
    sync_status_server4 = models.CharField(max_length=4, blank=True, null=True)
    sync_status_server3 = models.CharField(max_length=4, blank=True, null=True)
    sync_status_server2 = models.CharField(max_length=4, blank=True, null=True)
    sync_status_server1 = models.CharField(max_length=4, blank=True, null=True)
    sync_created_server1 = models.CharField(max_length=50, blank=True, null=True)
    sync_created_server2 = models.CharField(max_length=50, blank=True, null=True)
    sync_created_server3 = models.CharField(max_length=50, blank=True, null=True)
    sync_created_server4 = models.CharField(max_length=50, blank=True, null=True)
    sync_created_server5 = models.CharField(max_length=50, blank=True, null=True)
    sync_created = models.CharField(max_length=50, blank=True, null=True)
    sync_status = models.CharField(max_length=4, blank=True, null=True)
    log_status = models.CharField(max_length=50, blank=True, null=True)
    nologsonbreak = models.CharField(db_column='NoLogsOnBreak', max_length=5, blank=True, null=True)  # Field name made lowercase.
    rectify3 = models.CharField(max_length=500, blank=True, null=True)
    rectifyot = models.CharField(max_length=500, blank=True, null=True)
    rectify2 = models.CharField(max_length=500, blank=True, null=True)
    rectify = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_empdtr'


class TblPsEmpleaveList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    leave_id = models.IntegerField(blank=True, null=True)
    leave_acronym = models.CharField(max_length=10, blank=True, null=True)
    leave_desc = models.CharField(max_length=150, blank=True, null=True)
    emp_id = models.IntegerField(db_column='Emp_ID', blank=True, null=True)  # Field name made lowercase.
    emp_name = models.CharField(db_column='Emp_Name', max_length=150, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(max_length=150, blank=True, null=True)
    designation = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_empleave_list'


class TblPsEmployeeGroupShift(models.Model):
    emp_group_id_code = models.AutoField(unique=True)
    emp_group_desc = models.CharField(max_length=30, blank=True, null=True)
    emp_group_short_code = models.CharField(max_length=30, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=99, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_employee_group_shift'


class TblPsEmployeeGroupShiftList(models.Model):
    auto_no = models.AutoField(unique=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    doc_ref = models.CharField(max_length=11, blank=True, null=True)
    payroll_period = models.CharField(max_length=30, blank=True, null=True)
    group_id_code = models.CharField(max_length=30, blank=True, null=True)
    group_shift_desc = models.CharField(max_length=30, blank=True, null=True)
    emp_group_id_code = models.CharField(max_length=11, blank=True, null=True)
    emp_group_desc = models.CharField(max_length=30, blank=True, null=True)
    shift_code = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=99, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    recommended_approved = models.CharField(max_length=40, blank=True, null=True)
    approved_by = models.CharField(max_length=999, blank=True, null=True)
    reviewed_by = models.CharField(max_length=999, blank=True, null=True)
    created_by = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_employee_group_shift_list'


class TblPsEmployeeGroupShiftListing(models.Model):
    auto_no = models.AutoField(unique=True)
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    doc_ref = models.CharField(max_length=11, blank=True, null=True)
    payroll_period = models.CharField(max_length=30, blank=True, null=True)
    group_id_code = models.CharField(max_length=30, blank=True, null=True)
    group_shift_desc = models.CharField(max_length=30, blank=True, null=True)
    shift_code = models.CharField(max_length=30, blank=True, null=True)
    shift_name = models.CharField(max_length=30, blank=True, null=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    emp_group_id_code = models.CharField(max_length=11, blank=True, null=True)
    emp_group_desc = models.CharField(max_length=30, blank=True, null=True)
    emp_id_code = models.CharField(max_length=11, blank=True, null=True)
    emp_name = models.CharField(max_length=30, blank=True, null=True)
    emp_contract = models.CharField(max_length=30, blank=True, null=True)
    emp_dept = models.CharField(max_length=30, blank=True, null=True)
    emp_dept_code = models.CharField(max_length=30, blank=True, null=True)
    emp_resp_center = models.CharField(max_length=30, blank=True, null=True)
    emp_resp_center_code = models.CharField(max_length=30, blank=True, null=True)
    rest_day = models.CharField(max_length=30, blank=True, null=True)
    irregular_day_off = models.CharField(max_length=10, blank=True, null=True)
    remarks = models.CharField(max_length=99, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    recommended_approved = models.CharField(max_length=40, blank=True, null=True)
    approved_by = models.CharField(max_length=999, blank=True, null=True)
    reviewed_by = models.CharField(max_length=999, blank=True, null=True)
    created_by = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_employee_group_shift_listing'


class TblPsEmployeeOtherInformation(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    id_code = models.CharField(max_length=11, blank=True, null=True)
    full_name = models.CharField(max_length=999, blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    sss_no = models.CharField(max_length=999, blank=True, null=True)
    phic_no = models.CharField(max_length=999, blank=True, null=True)
    hdmf_no = models.CharField(max_length=999, blank=True, null=True)
    tin_id_no = models.CharField(max_length=999, blank=True, null=True)
    tax_schedule = models.CharField(max_length=999, blank=True, null=True)
    tax_exemption = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_employee_other_information'


class TblPsEmployeeRecordHistory(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    id_code = models.CharField(max_length=11, blank=True, null=True)
    full_name = models.CharField(max_length=999, blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    employer = models.CharField(max_length=999, blank=True, null=True)
    position = models.CharField(max_length=999, blank=True, null=True)
    working_days = models.CharField(max_length=999, blank=True, null=True)
    salary = models.CharField(max_length=999, blank=True, null=True)
    salary_type = models.CharField(max_length=999, blank=True, null=True)
    salary_release_frequency = models.CharField(max_length=999, blank=True, null=True)
    time_from = models.DateField(blank=True, null=True)
    time_to = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=999, blank=True, null=True)
    daily_rate = models.CharField(db_column='Daily_rate', max_length=999, blank=True, null=True)  # Field name made lowercase.
    hourly_rate = models.CharField(db_column='Hourly_rate', max_length=999, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ps_employee_record_history'


class TblPsEmployeeShiftSchedule(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    payrollperiod = models.CharField(db_column='PayrollPeriod', max_length=999, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    shift_code = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    rest_day = models.CharField(max_length=20, blank=True, null=True)
    broken_time = models.CharField(max_length=999, blank=True, null=True)
    approved_ot = models.CharField(max_length=999, blank=True, null=True)
    approved_leave = models.CharField(max_length=999, blank=True, null=True)
    holiday = models.CharField(max_length=999, blank=True, null=True)
    created_by = models.CharField(max_length=999, blank=True, null=True)
    updated_by = models.CharField(max_length=999, blank=True, null=True)
    reviewed = models.CharField(max_length=250, blank=True, null=True)
    reviewed_by = models.CharField(max_length=250, blank=True, null=True)
    approved_by = models.CharField(max_length=250, blank=True, null=True)
    approved = models.CharField(max_length=250, blank=True, null=True)
    doc_type = models.CharField(max_length=20, blank=True, null=True)
    doc_ref = models.CharField(max_length=20, blank=True, null=True)
    drd = models.CharField(db_column='DRD', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ps_employee_shift_schedule'


class TblPsEmploymentRecord(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    id_code = models.IntegerField()
    full_name = models.CharField(max_length=999, blank=True, null=True)
    department = models.IntegerField()
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.IntegerField()
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    employer = models.CharField(max_length=999, blank=True, null=True)
    position = models.CharField(max_length=999, blank=True, null=True)
    working_days = models.CharField(max_length=999, blank=True, null=True)
    salary = models.CharField(max_length=999, blank=True, null=True)
    salary_type = models.CharField(max_length=999, blank=True, null=True)
    salary_release_frequency = models.CharField(max_length=999, blank=True, null=True)
    time_from = models.DateField(blank=True, null=True)
    time_to = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=999, blank=True, null=True)
    daily_rate = models.CharField(db_column='Daily_rate', max_length=21, blank=True, null=True)  # Field name made lowercase.
    hourly_rate = models.CharField(db_column='Hourly_rate', max_length=21, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ps_employment_record'


class TblPsEntryLogs(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    username = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    employee_name = models.CharField(max_length=999, blank=True, null=True)
    employee_rank = models.CharField(max_length=200, blank=True, null=True)
    entry_description = models.CharField(max_length=999, blank=True, null=True)
    reference_no = models.CharField(max_length=999, blank=True, null=True)
    date_transact = models.CharField(max_length=50, blank=True, null=True)
    system = models.CharField(max_length=999, blank=True, null=True)
    form_module = models.CharField(max_length=999, blank=True, null=True)
    system_version = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_entry_logs'


class TblPsFiltersUsed(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    dept = models.CharField(max_length=30, blank=True, null=True)
    resp_center = models.CharField(max_length=30, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_filters_used'


class TblPsFlexiPerEmployee(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    employee_id = models.IntegerField(blank=True, null=True)
    employee_name = models.CharField(max_length=150, blank=True, null=True)
    day_of_week = models.CharField(max_length=10, blank=True, null=True)
    am_time_in = models.CharField(max_length=8, blank=True, null=True)
    am_time_out = models.CharField(max_length=8, blank=True, null=True)
    pm_time_in = models.CharField(max_length=8, blank=True, null=True)
    pm_time_out = models.CharField(max_length=8, blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_flexi_per_employee'


class TblPsGroupShiftList(models.Model):
    group_id_code = models.AutoField(unique=True)
    group_shift_desc = models.CharField(max_length=30, blank=True, null=True)
    shift_code = models.CharField(max_length=11, blank=True, null=True)
    shift_name = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=99, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    fixed_sched = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_group_shift_list'


class TblPsGroupShiftScheduleNotFixed(models.Model):
    autonum = models.AutoField(primary_key=True)
    group_id = models.IntegerField(blank=True, null=True)
    group_desc = models.CharField(max_length=100, blank=True, null=True)
    payroll_period = models.CharField(max_length=100, blank=True, null=True)
    from_date = models.CharField(max_length=25, blank=True, null=True)
    to_date = models.CharField(max_length=25, blank=True, null=True)
    shift_code = models.IntegerField(blank=True, null=True)
    rest_day = models.CharField(max_length=20, blank=True, null=True)
    date_trans = models.CharField(max_length=25, blank=True, null=True)
    broken_time = models.CharField(max_length=100, blank=True, null=True)
    approved_ot = models.CharField(max_length=100, blank=True, null=True)
    approved_leave = models.CharField(max_length=150, blank=True, null=True)
    holiday = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)
    reviewed = models.CharField(max_length=100, blank=True, null=True)
    reviewed_by = models.CharField(max_length=100, blank=True, null=True)
    approved_by = models.CharField(max_length=150, blank=True, null=True)
    approved = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_group_shift_schedule_not_fixed'


class TblPsJournalOrderSetupList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    main_code = models.FloatField(blank=True, null=True)
    main_desc = models.CharField(max_length=50, blank=True, null=True)
    seq_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_journal_order_setup_list'


class TblPsJournalOrderSetupListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    main_code = models.FloatField(blank=True, null=True)
    sub_code = models.CharField(max_length=5, blank=True, null=True)
    sub_desc = models.CharField(max_length=50, blank=True, null=True)
    seq_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_journal_order_setup_listing'


class TblPsLeaveGrantReduction(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    id_code = models.CharField(max_length=11, blank=True, null=True)
    employee_name = models.CharField(db_column='Employee_name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    employment_contract = models.CharField(db_column='Employment_contract', max_length=30, blank=True, null=True)  # Field name made lowercase.
    resp_center = models.CharField(db_column='Resp_Center', max_length=30, blank=True, null=True)  # Field name made lowercase.
    leave_type = models.CharField(max_length=30, blank=True, null=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    days_credit = models.FloatField(blank=True, null=True)
    hours_equivalent = models.FloatField(blank=True, null=True)
    effectivity_date = models.CharField(max_length=30, blank=True, null=True)
    doc_ref = models.CharField(max_length=30, blank=True, null=True)
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    transaction_type = models.CharField(max_length=30, blank=True, null=True)
    recommended_approved = models.CharField(max_length=40, blank=True, null=True)
    approved_by = models.CharField(max_length=40, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_leave_grant_reduction'


class TblPsLeaveGrantReductionList(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    doc_ref = models.CharField(max_length=30, blank=True, null=True)
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    leave_type = models.CharField(max_length=30, blank=True, null=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    effectivity_date = models.CharField(max_length=30, blank=True, null=True)
    transaction_type = models.CharField(max_length=30, blank=True, null=True)
    recommended_approved = models.CharField(max_length=40, blank=True, null=True)
    approved_by = models.CharField(max_length=40, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_leave_grant_reduction_list'


class TblPsLeaveGrantReductionListing(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    doc_ref = models.CharField(max_length=30, blank=True, null=True)
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    id_code = models.CharField(max_length=11, blank=True, null=True)
    employee_name = models.CharField(db_column='Employee_name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    employment_contract = models.CharField(db_column='Employment_contract', max_length=30, blank=True, null=True)  # Field name made lowercase.
    resp_center = models.CharField(db_column='Resp_Center', max_length=30, blank=True, null=True)  # Field name made lowercase.
    leave_type = models.CharField(max_length=30, blank=True, null=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    days_credit = models.FloatField(blank=True, null=True)
    hours_equivalent = models.FloatField(blank=True, null=True)
    effectivity_date = models.CharField(max_length=30, blank=True, null=True)
    transaction_type = models.CharField(max_length=30, blank=True, null=True)
    recommended_approved = models.CharField(max_length=40, blank=True, null=True)
    approved_by = models.CharField(max_length=40, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_leave_grant_reduction_listing'


class TblPsLeaveRequestUsedPosted(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    id_code = models.CharField(max_length=11, blank=True, null=True)
    leave_reference = models.CharField(max_length=11, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=199, blank=True, null=True)
    department_desc = models.CharField(max_length=199, blank=True, null=True)
    responsibility_center = models.CharField(max_length=199, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=199, blank=True, null=True)
    payroll_period = models.CharField(max_length=199, blank=True, null=True)
    leave_type = models.CharField(max_length=199, blank=True, null=True)
    used_leave = models.CharField(max_length=199, blank=True, null=True)
    leave_days = models.CharField(max_length=199, blank=True, null=True)
    date_posted = models.CharField(max_length=199, blank=True, null=True)
    posted_by = models.CharField(max_length=199, blank=True, null=True)
    leave_code_type = models.CharField(max_length=199, blank=True, null=True)
    batch_no = models.CharField(max_length=2, blank=True, null=True)
    sys_type = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_leave_request_used_posted'


class TblPsLeaveRequestUsedTemp(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    id_code = models.CharField(max_length=11, blank=True, null=True)
    leave_reference = models.CharField(max_length=11, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=30, blank=True, null=True)
    department_desc = models.CharField(max_length=30, blank=True, null=True)
    responsibility_center = models.CharField(max_length=30, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=30, blank=True, null=True)
    payroll_period = models.CharField(max_length=30, blank=True, null=True)
    leave_type = models.CharField(max_length=30, blank=True, null=True)
    used_leave = models.CharField(max_length=30, blank=True, null=True)
    leave_days = models.CharField(max_length=30, blank=True, null=True)
    date_posted = models.CharField(max_length=30, blank=True, null=True)
    posted_by = models.CharField(max_length=50, blank=True, null=True)
    leave_code_type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_leave_request_used_temp'


class TblPsLeaveType(models.Model):
    auto_no = models.AutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    leave_type_abbre = models.CharField(max_length=11, blank=True, null=True)
    leave_type = models.CharField(max_length=30, blank=True, null=True)
    leave_description = models.CharField(max_length=250, blank=True, null=True)
    remarks = models.CharField(max_length=999, blank=True, null=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    created_by = models.CharField(max_length=999, blank=True, null=True)
    updated_by = models.CharField(max_length=999, blank=True, null=True)
    with_pay = models.CharField(max_length=30, blank=True, null=True)
    max_days_leave = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_leave_type'


class TblPsListEmployeeGroup(models.Model):
    auto_no = models.AutoField(unique=True)
    emp_group_id_code = models.CharField(max_length=11, blank=True, null=True)
    emp_group_desc = models.CharField(max_length=30, blank=True, null=True)
    emp_id_code = models.CharField(max_length=11, blank=True, null=True)
    emp_name = models.CharField(max_length=30, blank=True, null=True)
    emp_contract = models.CharField(max_length=30, blank=True, null=True)
    emp_dept = models.CharField(max_length=30, blank=True, null=True)
    emp_resp_center = models.CharField(max_length=30, blank=True, null=True)
    day_1_off = models.CharField(max_length=30, blank=True, null=True)
    day_2_off = models.CharField(max_length=30, blank=True, null=True)
    day_3_off = models.CharField(max_length=30, blank=True, null=True)
    irregular_day_off = models.CharField(max_length=10, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=99, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_list_employee_group'


class TblPsLocale(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    id_code = models.IntegerField(blank=True, null=True)
    locale = models.CharField(max_length=99, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_locale'


class TblPsMainPayrollTransactionListing(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    id_code = models.CharField(max_length=11, blank=True, null=True)
    full_name = models.CharField(max_length=999, blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    payrollperiod = models.CharField(db_column='PayrollPeriod', max_length=999, blank=True, null=True)  # Field name made lowercase.
    date_from = models.CharField(max_length=999, blank=True, null=True)
    date_to = models.CharField(max_length=999, blank=True, null=True)
    factor_computation_id = models.CharField(max_length=999, blank=True, null=True)
    payroll_type = models.CharField(max_length=999, blank=True, null=True)
    payroll_pay_scheme = models.CharField(max_length=999, blank=True, null=True)
    payroll_pay_frequency = models.CharField(max_length=999, blank=True, null=True)
    transaction_type = models.CharField(max_length=999, blank=True, null=True)
    transaction_desc = models.CharField(max_length=999, blank=True, null=True)
    transaction_account_name = models.CharField(max_length=999, blank=True, null=True)
    transaction_account_tag = models.CharField(max_length=999, blank=True, null=True)
    transaction_item_id_code = models.CharField(max_length=999, blank=True, null=True)
    debit = models.CharField(max_length=9999, blank=True, null=True)
    credit = models.CharField(max_length=9999, blank=True, null=True)
    reviewed = models.CharField(max_length=999, blank=True, null=True)
    reviewed_by = models.CharField(max_length=999, blank=True, null=True)
    reviewed_date = models.CharField(max_length=999, blank=True, null=True)
    approved = models.CharField(max_length=999, blank=True, null=True)
    approved_by = models.CharField(max_length=999, blank=True, null=True)
    approved_date = models.CharField(max_length=999, blank=True, null=True)
    posted = models.CharField(max_length=999, blank=True, null=True)
    posted_by = models.CharField(max_length=999, blank=True, null=True)
    posted_date = models.CharField(max_length=999, blank=True, null=True)
    discarded = models.CharField(max_length=1, blank=True, null=True)
    discarded_by = models.CharField(max_length=999, blank=True, null=True)
    discarded_date = models.CharField(max_length=999, blank=True, null=True)
    amount_adjustment = models.FloatField(blank=True, null=True)
    amount_adjustment_deducted = models.FloatField(blank=True, null=True)
    payslip_set = models.IntegerField(blank=True, null=True)
    payslip_order = models.IntegerField(blank=True, null=True)
    counted_hours = models.FloatField(blank=True, null=True)
    batch_no = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_main_payroll_transaction_listing'


class TblPsManualDtrList(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    doc_ref = models.CharField(max_length=11, blank=True, null=True)
    payroll_period = models.CharField(db_column='Payroll_Period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_code = models.IntegerField(blank=True, null=True)
    employee_name = models.CharField(max_length=999, blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    total_hours = models.CharField(max_length=30, blank=True, null=True)
    recommended_approved = models.CharField(max_length=999, blank=True, null=True)
    approved_by = models.CharField(max_length=999, blank=True, null=True)
    created_by = models.CharField(max_length=999, blank=True, null=True)
    updated_by = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    module = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_manual_dtr_list'


class TblPsManualDtrListing(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    doc_ref = models.CharField(max_length=11, blank=True, null=True)
    payroll_period = models.CharField(db_column='Payroll_Period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_code = models.IntegerField(blank=True, null=True)
    employee_name = models.CharField(max_length=999, blank=True, null=True)
    employment_contract = models.CharField(max_length=999, blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    date_filed = models.CharField(max_length=30, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    day_category = models.CharField(max_length=30, blank=True, null=True)
    no_nsd_reg_hrs = models.CharField(max_length=10, blank=True, null=True)
    no_nsd_ot_hrs = models.CharField(max_length=10, blank=True, null=True)
    with_nsd_reg_hrs = models.CharField(max_length=10, blank=True, null=True)
    with_nsd_ot_hrs = models.CharField(max_length=10, blank=True, null=True)
    hours_worked = models.CharField(max_length=10, blank=True, null=True)
    leave_code = models.CharField(max_length=10, blank=True, null=True)
    leave_type = models.CharField(max_length=30, blank=True, null=True)
    leave_hrs = models.CharField(max_length=10, blank=True, null=True)
    absent_code = models.CharField(max_length=10, blank=True, null=True)
    absent_type = models.CharField(max_length=30, blank=True, null=True)
    absent_hrs = models.CharField(max_length=10, blank=True, null=True)
    tardy = models.CharField(max_length=30, blank=True, null=True)
    undertime = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=999, blank=True, null=True)
    recommended_approved = models.CharField(max_length=999, blank=True, null=True)
    approved_by = models.CharField(max_length=999, blank=True, null=True)
    created_by = models.CharField(max_length=999, blank=True, null=True)
    updated_by = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_manual_dtr_listing'


class TblPsModuleAccess(models.Model):
    line_number = models.PositiveBigIntegerField()
    header = models.CharField(max_length=1, blank=True, null=True)
    trans_module = models.CharField(max_length=100, blank=True, null=True)
    key_text = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_module_access'


class TblPsMultipleSalaryRate(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    department = models.CharField(max_length=20)
    department_desc = models.CharField(max_length=250)
    responsibility_center = models.CharField(max_length=20, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=250, blank=True, null=True)
    designation = models.CharField(max_length=250, blank=True, null=True)
    no_of_days_worked = models.CharField(max_length=20, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    date_start = models.CharField(max_length=30, blank=True, null=True)
    date_end = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_multiple_salary_rate'


class TblPsNoLogBreakList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    trans_date = models.CharField(max_length=30, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.IntegerField(blank=True, null=True)
    payroll_period = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=50, blank=True, null=True)
    reviewed_by = models.CharField(max_length=50, blank=True, null=True)
    approved_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_no_log_break_list'


class TblPsNoLogBreakListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    chk = models.CharField(max_length=1, blank=True, null=True)
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    doc_no = models.IntegerField(blank=True, null=True)
    emp_id = models.IntegerField(blank=True, null=True)
    employee = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    shift_code = models.IntegerField(blank=True, null=True)
    shift_name = models.CharField(max_length=50, blank=True, null=True)
    out = models.CharField(max_length=30, blank=True, null=True)
    in_field = models.CharField(db_column='in', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    posted = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_no_log_break_listing'


class TblPsNoLogOnOtList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    trans_date = models.CharField(max_length=30, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.IntegerField(blank=True, null=True)
    payroll_period = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=50, blank=True, null=True)
    reviewed_by = models.CharField(max_length=50, blank=True, null=True)
    approved_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_no_log_on_ot_list'


class TblPsNoLogOnOtListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    chk = models.CharField(max_length=1, blank=True, null=True)
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    doc_no = models.IntegerField(blank=True, null=True)
    emp_id = models.IntegerField(blank=True, null=True)
    employee = models.CharField(max_length=50, blank=True, null=True)
    date = models.CharField(max_length=30, blank=True, null=True)
    shift_code = models.IntegerField(blank=True, null=True)
    shift_name = models.CharField(max_length=50, blank=True, null=True)
    out = models.CharField(max_length=30, blank=True, null=True)
    in_field = models.CharField(db_column='in', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    posted = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_no_log_on_ot_listing'


class TblPsNsdConfig(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    night_shift_diff = models.CharField(max_length=10, blank=True, null=True)
    time_starts = models.CharField(max_length=30, blank=True, null=True)
    time_ends = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_nsd_config'


class TblPsOtType(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    id_code = models.CharField(max_length=11, blank=True, null=True)
    ot_description = models.CharField(max_length=30, blank=True, null=True)
    ot_abbreviation = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_ot_type'


class TblPsPayrollJournalEntry(models.Model):
    autonum = models.AutoField(unique=True)
    ul_code = models.CharField(max_length=11, blank=True, null=True)
    employee_id = models.IntegerField(db_column='Employee_id')  # Field name made lowercase.
    employee_name = models.CharField(db_column='Employee_name', max_length=250, blank=True, null=True)  # Field name made lowercase.
    rc_costcat_id = models.CharField(max_length=11, blank=True, null=True)
    rc_cost_category = models.CharField(max_length=250, blank=True, null=True)
    payroll_period = models.CharField(max_length=250, blank=True, null=True)
    responsibility_center_code = models.IntegerField()
    responsibility_center_desc = models.CharField(max_length=250, blank=True, null=True)
    payroll_component_id = models.IntegerField()
    component_type = models.CharField(max_length=250, blank=True, null=True)
    payroll_component = models.CharField(max_length=250, blank=True, null=True)
    date_trans = models.CharField(max_length=20, blank=True, null=True)
    account_code = models.CharField(max_length=20, blank=True, null=True)
    account_title = models.CharField(max_length=250, blank=True, null=True)
    sl_type = models.CharField(max_length=10, blank=True, null=True)
    sl_code = models.CharField(max_length=20, blank=True, null=True)
    sl_acct = models.CharField(max_length=350, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    batch_no = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_payroll_journal_entry'


class TblPsPayrollJournalList(models.Model):
    auto_num = models.BigAutoField(primary_key=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_date = models.DateField(blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_type = models.CharField(max_length=15, blank=True, null=True)
    payroll_period = models.CharField(db_column='Payroll_Period', max_length=20, blank=True, null=True)  # Field name made lowercase.
    transaction_type = models.CharField(max_length=150, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    batch_no = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_payroll_journal_list'


class TblPsPayrollSettings(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    accounting = models.CharField(max_length=1, blank=True, null=True)
    client_type = models.CharField(max_length=1, blank=True, null=True)
    deduction_settings = models.CharField(max_length=1, blank=True, null=True)
    tardy_computation_option = models.CharField(max_length=1, blank=True, null=True)
    monthly_sss = models.CharField(max_length=999, blank=True, null=True)
    semi_monthly_sss = models.CharField(max_length=999, blank=True, null=True)
    weekly_sss = models.CharField(max_length=999, blank=True, null=True)
    daily_sss = models.CharField(max_length=999, blank=True, null=True)
    monthly_hdmf = models.CharField(max_length=999, blank=True, null=True)
    semi_monthly_hdmf = models.CharField(max_length=999, blank=True, null=True)
    weekly_hdmf = models.CharField(max_length=999, blank=True, null=True)
    daily_hdmf = models.CharField(max_length=999, blank=True, null=True)
    monthly_phic = models.CharField(max_length=999, blank=True, null=True)
    semi_monthly_phic = models.CharField(max_length=999, blank=True, null=True)
    weekly_phic = models.CharField(max_length=999, blank=True, null=True)
    daily_phic = models.CharField(max_length=999, blank=True, null=True)
    monthly_tax = models.CharField(max_length=999, blank=True, null=True)
    semi_monthly_tax = models.CharField(max_length=999, blank=True, null=True)
    weekly_tax = models.CharField(max_length=999, blank=True, null=True)
    daily_tax = models.CharField(max_length=999, blank=True, null=True)
    grace_period = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_payroll_settings'


class TblPsPayrollSettingsTardiness(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    id_code = models.CharField(max_length=11, blank=True, null=True)
    employee_name = models.CharField(max_length=999, blank=True, null=True)
    option_field = models.CharField(db_column='option_', max_length=1, blank=True, null=True)  # Field renamed because it ended with '_'.
    option_2_time_from = models.CharField(max_length=999, blank=True, null=True)
    option_2_time_to = models.CharField(max_length=999, blank=True, null=True)
    option_2_time_deduction = models.CharField(max_length=999, blank=True, null=True)
    option_3_time_from = models.CharField(max_length=999, blank=True, null=True)
    option_3_time_to = models.CharField(max_length=999, blank=True, null=True)
    option_3_time_deduction = models.CharField(max_length=999, blank=True, null=True)
    option_4_time_from = models.CharField(max_length=999, blank=True, null=True)
    option_4_time_to = models.CharField(max_length=999, blank=True, null=True)
    option_4_time_deduction = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_payroll_settings_tardiness'


class TblPsPayrollSettingsTardinessEscalation(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    start_time = models.FloatField(blank=True, null=True)
    end_time = models.FloatField(blank=True, null=True)
    escalation = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_payroll_settings_tardiness_escalation'


class TblPsPieceWorkSetup(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    work_desc = models.CharField(max_length=60, blank=True, null=True)
    uom = models.CharField(max_length=60, blank=True, null=True)
    piece_rate = models.CharField(max_length=60, blank=True, null=True)
    acct_code = models.FloatField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    acct_code1 = models.FloatField(blank=True, null=True)
    acct_title1 = models.CharField(max_length=150, blank=True, null=True)
    acct_code2 = models.FloatField(blank=True, null=True)
    acct_title2 = models.CharField(max_length=150, blank=True, null=True)
    acct_code3 = models.FloatField(blank=True, null=True)
    acct_title3 = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_piece_work_setup'


class TblPsRccCategory(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=60, blank=True, null=True)
    category = models.CharField(max_length=60, blank=True, null=True)
    active = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_rcc_category'


class TblPsRectificationCauses(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    short_code = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    updated_by = models.CharField(max_length=30, blank=True, null=True)
    created_by = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_rectification_causes'


class TblPsReportsFieldsHolder(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    field1 = models.CharField(max_length=999, blank=True, null=True)
    field2 = models.CharField(max_length=999, blank=True, null=True)
    field3 = models.CharField(max_length=999, blank=True, null=True)
    field4 = models.CharField(max_length=999, blank=True, null=True)
    field5 = models.CharField(max_length=999, blank=True, null=True)
    field6 = models.CharField(max_length=999, blank=True, null=True)
    field7 = models.CharField(max_length=999, blank=True, null=True)
    field8 = models.CharField(max_length=999, blank=True, null=True)
    field9 = models.CharField(max_length=999, blank=True, null=True)
    field10 = models.CharField(max_length=999, blank=True, null=True)
    field11 = models.CharField(max_length=999, blank=True, null=True)
    field12 = models.CharField(max_length=999, blank=True, null=True)
    field13 = models.CharField(max_length=999, blank=True, null=True)
    field14 = models.CharField(max_length=999, blank=True, null=True)
    field15 = models.CharField(max_length=999, blank=True, null=True)
    username = models.CharField(max_length=999, blank=True, null=True)
    user_fullname = models.CharField(max_length=999, blank=True, null=True)
    field16 = models.CharField(max_length=30, blank=True, null=True)
    field17 = models.CharField(max_length=30, blank=True, null=True)
    field18 = models.CharField(max_length=30, blank=True, null=True)
    hourly_rate = models.FloatField(db_column='Hourly_rate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ps_reports_fields_holder'


class TblPsReportsHolderPayrollJournal(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    field1 = models.CharField(max_length=999, blank=True, null=True)
    field2 = models.CharField(max_length=999, blank=True, null=True)
    field3 = models.CharField(max_length=999, blank=True, null=True)
    field4 = models.CharField(max_length=999, blank=True, null=True)
    field5 = models.CharField(max_length=999, blank=True, null=True)
    field6 = models.CharField(max_length=999, blank=True, null=True)
    field7 = models.CharField(max_length=999, blank=True, null=True)
    field8 = models.CharField(max_length=999, blank=True, null=True)
    field9 = models.CharField(max_length=999, blank=True, null=True)
    field10 = models.CharField(max_length=999, blank=True, null=True)
    field11 = models.CharField(max_length=999, blank=True, null=True)
    field12 = models.CharField(max_length=999, blank=True, null=True)
    field13 = models.CharField(max_length=999, blank=True, null=True)
    field14 = models.CharField(max_length=999, blank=True, null=True)
    field15 = models.CharField(max_length=999, blank=True, null=True)
    field16 = models.CharField(max_length=999, blank=True, null=True)
    field17 = models.CharField(max_length=999, blank=True, null=True)
    field18 = models.CharField(max_length=999, blank=True, null=True)
    field19 = models.CharField(max_length=999, blank=True, null=True)
    field20 = models.CharField(max_length=999, blank=True, null=True)
    field21 = models.CharField(max_length=999, blank=True, null=True)
    field22 = models.CharField(max_length=999, blank=True, null=True)
    field23 = models.CharField(max_length=999, blank=True, null=True)
    field24 = models.CharField(max_length=999, blank=True, null=True)
    field25 = models.CharField(max_length=999, blank=True, null=True)
    field26 = models.CharField(max_length=999, blank=True, null=True)
    field27 = models.CharField(max_length=999, blank=True, null=True)
    field28 = models.CharField(max_length=999, blank=True, null=True)
    field29 = models.CharField(max_length=999, blank=True, null=True)
    field30 = models.CharField(max_length=999, blank=True, null=True)
    field31 = models.CharField(max_length=999, blank=True, null=True)
    field32 = models.CharField(max_length=999, blank=True, null=True)
    field33 = models.CharField(max_length=999, blank=True, null=True)
    field34 = models.CharField(max_length=999, blank=True, null=True)
    field35 = models.CharField(max_length=999, blank=True, null=True)
    field36 = models.CharField(max_length=999, blank=True, null=True)
    field37 = models.CharField(max_length=999, blank=True, null=True)
    field38 = models.CharField(max_length=999, blank=True, null=True)
    field39 = models.CharField(max_length=999, blank=True, null=True)
    field40 = models.CharField(max_length=999, blank=True, null=True)
    field41 = models.CharField(max_length=999, blank=True, null=True)
    field42 = models.CharField(max_length=999, blank=True, null=True)
    username = models.CharField(max_length=999, blank=True, null=True)
    user_fullname = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_reports_holder_payroll_journal'


class TblPsRequestOtList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    id_code = models.IntegerField(blank=True, null=True)
    employee_name = models.CharField(max_length=150, blank=True, null=True)
    total_hours = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    sync_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_request_ot_list'


class TblPsRequestOtListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    line_number = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time_from = models.TimeField(blank=True, null=True)
    time_to = models.TimeField(blank=True, null=True)
    hours = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=999, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    sync_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_request_ot_listing'


class TblPsScheduleRotationRestdaySetup(models.Model):
    auto_no = models.BigAutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    rotation_id = models.IntegerField()
    rotation_rest_day_id = models.IntegerField()
    restday_date = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_schedule_rotation_restday_setup'


class TblPsScheduleRotationSetup(models.Model):
    auto_no = models.BigAutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    id_code = models.IntegerField()
    emp_id = models.IntegerField()
    date_start = models.CharField(max_length=30)
    active = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_schedule_rotation_setup'


class TblPsScheduleRotationSetupDetails(models.Model):
    auto_no = models.BigAutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    rotation_id = models.IntegerField()
    shift_schedule = models.IntegerField()
    department = models.IntegerField()
    department_desc = models.CharField(max_length=250, blank=True, null=True)
    responsibility_center = models.IntegerField()
    responsibility_center_desc = models.CharField(max_length=250, blank=True, null=True)
    interval = models.IntegerField()
    rotation_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_ps_schedule_rotation_setup_details'


class TblPsShiftScheduleTagging(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    department = models.CharField(max_length=30, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    shift_code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_shift_schedule_tagging'


class TblPsShiftScheduleTagging2(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    department = models.CharField(max_length=30, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=30, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    shift_code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_shift_schedule_tagging_2'


class TblPsShiftScheduleTimeAllowance(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    time = models.CharField(max_length=30, blank=True, null=True)
    time_from = models.CharField(max_length=30, blank=True, null=True)
    time_to = models.CharField(max_length=30, blank=True, null=True)
    shift_code = models.CharField(max_length=30, blank=True, null=True)
    shift_type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_shift_schedule_time_allowance'


class TblPsSysshiftsked(models.Model):
    shifting_code = models.AutoField(db_column='Shifting_Code', primary_key=True)  # Field name made lowercase.
    shift_name = models.CharField(db_column='Shift_Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    shift_name_initials = models.CharField(db_column='Shift_Name_Initials', max_length=50, blank=True, null=True)  # Field name made lowercase.
    time_in1 = models.CharField(db_column='TIME_IN1', max_length=8)  # Field name made lowercase.
    time_out1 = models.CharField(db_column='TIME_OUT1', max_length=8)  # Field name made lowercase.
    time_in2 = models.CharField(db_column='TIME_IN2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    time_out2 = models.CharField(db_column='TIME_OUT2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    time_in3 = models.CharField(db_column='TIME_IN3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    time_out3 = models.CharField(db_column='TIME_OUT3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ot_time_in = models.CharField(db_column='OT_TIME_IN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ot_time_out = models.CharField(db_column='OT_TIME_OUT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    restday = models.CharField(db_column='RestDay', max_length=20, blank=True, null=True)  # Field name made lowercase.
    additional_time = models.FloatField(blank=True, null=True)
    validation_timein = models.CharField(db_column='validation_timeIn', max_length=8, blank=True, null=True)  # Field name made lowercase.
    validation_timeout = models.CharField(db_column='validation_timeOut', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimein1_from = models.CharField(db_column='AllowedTimeIn1_from', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimein1_to = models.CharField(db_column='AllowedTimeIn1_to', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimeout1_from = models.CharField(db_column='AllowedTimeOut1_from', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimeout1_to = models.CharField(db_column='AllowedTimeOut1_to', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimein2_from = models.CharField(db_column='AllowedTimeIn2_from', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimein2_to = models.CharField(db_column='AllowedTimeIn2_to', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimeout2_from = models.CharField(db_column='AllowedTimeOut2_from', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimeout2_to = models.CharField(db_column='AllowedTimeOut2_to', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimein3_from = models.CharField(db_column='AllowedTimeIn3_from', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimein3_to = models.CharField(db_column='AllowedTimeIn3_to', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimeout3_from = models.CharField(db_column='AllowedTimeOut3_from', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimeout3_to = models.CharField(db_column='AllowedTimeOut3_to', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedottimein_from = models.CharField(db_column='AllowedOTTimeIn_from', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedottimein_to = models.CharField(db_column='AllowedOTTimeIn_to', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedottimeout_from = models.CharField(db_column='AllowedOTTimeOut_from', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedottimeout_to = models.CharField(db_column='AllowedOTTimeOut_to', max_length=8, blank=True, null=True)  # Field name made lowercase.
    shift_type = models.IntegerField(db_column='Shift_type', blank=True, null=True)  # Field name made lowercase.
    shift_rotation_name = models.CharField(max_length=250, blank=True, null=True)
    hourslimit = models.IntegerField(db_column='HoursLimit', blank=True, null=True)  # Field name made lowercase.
    hourlimit = models.IntegerField(db_column='HourLimit', blank=True, null=True)  # Field name made lowercase.
    nologsrequired = models.CharField(db_column='NoLogsRequired', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nologsrequiredonot = models.CharField(db_column='NoLogsRequiredOnOT', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ps_sysshiftsked'


class TblPsSystemSetting(models.Model):
    auto_no = models.AutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    id_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ps_system_setting'


class TblPsTimeAllowance(models.Model):
    allowance_code = models.IntegerField(db_column='Allowance_Code', primary_key=True)  # Field name made lowercase.
    allowance_name = models.CharField(db_column='Allowance_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    time_allowance = models.CharField(db_column='Time_Allowance', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ps_time_allowance'


class TblPsTimeLogs(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', primary_key=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    id_code = models.CharField(max_length=30, blank=True, null=True)
    employee_name = models.CharField(max_length=999, blank=True, null=True)
    date_log = models.CharField(max_length=30, blank=True, null=True)
    time_log = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_time_logs'


class TblPsTimeLogsForParallelRun(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    id_code = models.CharField(max_length=30, blank=True, null=True)
    employee_name = models.CharField(max_length=999, blank=True, null=True)
    date_log = models.CharField(max_length=30, blank=True, null=True)
    time_log = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_time_logs_for_parallel_run'


class TblPsTimekeepingDtr(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    emp_id = models.CharField(db_column='Emp_ID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_Period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    date_trans = models.CharField(max_length=50, blank=True, null=True)
    days = models.CharField(max_length=30, blank=True, null=True)
    time_in_morning = models.CharField(max_length=50, blank=True, null=True)
    time_out_moring = models.CharField(max_length=50, blank=True, null=True)
    time_in_afternoon = models.CharField(max_length=50, blank=True, null=True)
    time_out_afternoon = models.CharField(max_length=50, blank=True, null=True)
    time_in_ot = models.CharField(max_length=50, blank=True, null=True)
    time_out_out = models.CharField(max_length=50, blank=True, null=True)
    reg_hours = models.CharField(max_length=50, blank=True, null=True)
    ot_hours = models.CharField(max_length=50, blank=True, null=True)
    leave_with_pay = models.CharField(max_length=50, blank=True, null=True)
    absent = models.CharField(max_length=50, blank=True, null=True)
    tardy = models.CharField(max_length=50, blank=True, null=True)
    undertime = models.CharField(max_length=50, blank=True, null=True)
    manual_hours_reg = models.CharField(max_length=50, blank=True, null=True)
    manual_hours_ot = models.CharField(max_length=50, blank=True, null=True)
    doc_ref = models.CharField(max_length=50, blank=True, null=True)
    shift_sched = models.CharField(max_length=150, blank=True, null=True)
    res_desc = models.CharField(max_length=150, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_timekeeping_dtr'


class TblPsTransactionAllowance(models.Model):
    auto_num = models.AutoField(primary_key=True)
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    doc_num = models.BigIntegerField(db_column='Doc_num', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.IntegerField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    employee_name = models.CharField(db_column='Employee_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    allow_code = models.IntegerField(blank=True, null=True)
    allowance_name = models.CharField(db_column='Allowance_name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=20, blank=True, null=True)  # Field name made lowercase.
    trans_type = models.CharField(max_length=20, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    amnt_applied = models.FloatField(blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    prepared_by = models.CharField(max_length=50, blank=True, null=True)
    doc_type = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    reviewed_date = models.DateField(blank=True, null=True)
    reviewed_by = models.CharField(max_length=50, blank=True, null=True)
    approved_date = models.DateField(blank=True, null=True)
    approved_by = models.CharField(max_length=50, blank=True, null=True)
    cancelled_date = models.DateField(blank=True, null=True)
    cancelled_by = models.CharField(max_length=50, blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    rc_costcat_id = models.IntegerField(blank=True, null=True)
    rc_cost_category = models.CharField(max_length=100, blank=True, null=True)
    responsibility_center = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(db_column='Remarks', max_length=225, blank=True, null=True)  # Field name made lowercase.
    batch_no = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_transaction_allowance'


class TblPsTransactionDeduction(models.Model):
    auto_num = models.AutoField(primary_key=True)
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    doc_num = models.BigIntegerField(db_column='Doc_num', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.IntegerField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    employee_name = models.CharField(db_column='Employee_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ded_code = models.IntegerField(db_column='Ded_code', blank=True, null=True)  # Field name made lowercase.
    deduction_name = models.CharField(db_column='Deduction_name', max_length=150, blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_Period', max_length=20, blank=True, null=True)  # Field name made lowercase.
    trans_type = models.CharField(max_length=50, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    deferral = models.FloatField(blank=True, null=True)
    amnt_applied = models.FloatField(blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    prepared_by = models.CharField(max_length=50, blank=True, null=True)
    doc_type = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    deferral_status = models.CharField(max_length=15, blank=True, null=True)
    reviewed_date = models.DateField(blank=True, null=True)
    reviewed_by = models.CharField(max_length=50, blank=True, null=True)
    approved_date = models.DateField(blank=True, null=True)
    approved_by = models.CharField(max_length=50, blank=True, null=True)
    cancelled_date = models.DateField(blank=True, null=True)
    cancelled_by = models.CharField(max_length=50, blank=True, null=True)
    department = models.IntegerField(db_column='Department', blank=True, null=True)  # Field name made lowercase.
    rc_costcat_id = models.IntegerField(blank=True, null=True)
    rc_cost_category = models.CharField(max_length=100, blank=True, null=True)
    responsibility_center = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(db_column='Remarks', max_length=225, blank=True, null=True)  # Field name made lowercase.
    batch_no = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_transaction_deduction'


class TblPsTransactionListingGj(models.Model):
    auto_no = models.BigAutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    jv_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.PositiveIntegerField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    guarantor_id = models.PositiveIntegerField(blank=True, null=True)
    guarantor = models.CharField(max_length=150, blank=True, null=True)
    primary_code = models.PositiveSmallIntegerField(blank=True, null=True)
    secondary_code = models.PositiveSmallIntegerField(blank=True, null=True)
    acct_code = models.PositiveSmallIntegerField(blank=True, null=True)
    subsidiary_code = models.PositiveSmallIntegerField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    active = models.CharField(max_length=2, blank=True, null=True)
    posted_by = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.DateField(blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    payment_status = models.CharField(max_length=10, blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    payrollperiod = models.CharField(db_column='PayrollPeriod', max_length=999, blank=True, null=True)  # Field name made lowercase.
    entry_type = models.CharField(max_length=999, blank=True, null=True)
    entry_id_code = models.CharField(max_length=999, blank=True, null=True)
    filter = models.CharField(max_length=999, blank=True, null=True)
    filter_id = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_transaction_listing_gj'


class TblPsTransactionMandatory(models.Model):
    auto_no = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    doc_num = models.IntegerField(blank=True, null=True)
    emp_id = models.IntegerField(blank=True, null=True)
    employee_name = models.CharField(max_length=60, blank=True, null=True)
    ded_code = models.IntegerField(blank=True, null=True)
    deduction_name = models.CharField(max_length=50, blank=True, null=True)
    payroll_period = models.CharField(max_length=50, blank=True, null=True)
    trans_type = models.CharField(max_length=50, blank=True, null=True)
    employee_share = models.FloatField(blank=True, null=True)
    employer_share = models.FloatField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    deferral_ee = models.FloatField(blank=True, null=True)
    deferral_er = models.FloatField(blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    doc_type = models.CharField(max_length=5, blank=True, null=True)
    department = models.CharField(max_length=5, blank=True, null=True)
    rc_costcat_id = models.IntegerField(blank=True, null=True)
    rc_cost_category = models.CharField(max_length=100, blank=True, null=True)
    responsibility_center = models.CharField(max_length=5, blank=True, null=True)
    remarks = models.CharField(max_length=225, blank=True, null=True)
    deferral_status = models.CharField(max_length=15, blank=True, null=True)
    batch_no = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_transaction_mandatory'


class TblPsTransactionPieceWork(models.Model):
    autonum = models.AutoField(primary_key=True)
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    doc_num = models.BigIntegerField(db_column='Doc_num', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.IntegerField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    employee_name = models.CharField(db_column='Employee_name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    work_code = models.IntegerField(blank=True, null=True)
    work_description = models.CharField(max_length=150, blank=True, null=True)
    payroll_period = models.CharField(db_column='Payroll_period', max_length=20, blank=True, null=True)  # Field name made lowercase.
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    uom = models.CharField(max_length=60, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    resp_center = models.CharField(max_length=5, blank=True, null=True)
    customer = models.CharField(max_length=150, blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    prepared_by = models.CharField(max_length=50, blank=True, null=True)
    doc_type = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    reviewed_date = models.DateField(blank=True, null=True)
    reviewed_by = models.CharField(max_length=50, blank=True, null=True)
    approved_date = models.DateField(blank=True, null=True)
    approved_by = models.CharField(max_length=50, blank=True, null=True)
    cancelled_date = models.DateField(blank=True, null=True)
    cancelled_by = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(db_column='Remarks', max_length=225, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ps_transaction_piece_work'


class TblPsTranstype(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    id_code = models.CharField(max_length=11, blank=True, null=True)
    type_of_trans = models.CharField(max_length=150, blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)
    module_abbre = models.CharField(max_length=50, blank=True, null=True)
    doc_type = models.CharField(max_length=30, blank=True, null=True)
    sys_type = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_transtype'


class TblPsTravelCategory(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    short_code = models.CharField(max_length=10, blank=True, null=True)
    updated_by = models.CharField(max_length=30, blank=True, null=True)
    created_by = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_travel_category'


class TblPsUomSetup(models.Model):
    autonum = models.AutoField(primary_key=True)
    uom_code = models.IntegerField(blank=True, null=True)
    uom_desc = models.CharField(max_length=60, blank=True, null=True)
    uom = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_uom_setup'


class TblPsUser(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.CharField(max_length=5, blank=True, null=True)
    full_name = models.CharField(max_length=40, blank=True, null=True)
    user_name = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    user_rank = models.CharField(max_length=20, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_user'


class TblPsUserModuleAccess(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    user_name = models.CharField(max_length=250, blank=True, null=True)
    password = models.CharField(max_length=999, blank=True, null=True)
    module_access = models.CharField(max_length=250, blank=True, null=True)
    sys_type = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_user_module_access'


class TblPsWorkCategorization(models.Model):
    auto_no = models.BigAutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    emp_id = models.CharField(db_column='Emp_ID', max_length=15)  # Field name made lowercase.
    date = models.CharField(max_length=30, blank=True, null=True)
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    payroll_period = models.CharField(max_length=999, blank=True, null=True)
    hours_worked = models.CharField(max_length=30, blank=True, null=True)
    od_reg = models.CharField(max_length=30, blank=True, null=True)
    od_ot = models.CharField(max_length=30, blank=True, null=True)
    od_nsd = models.CharField(max_length=30, blank=True, null=True)
    od_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    sh_reg = models.CharField(max_length=30, blank=True, null=True)
    sh_ot = models.CharField(max_length=30, blank=True, null=True)
    sh_nsd = models.CharField(max_length=30, blank=True, null=True)
    sh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    rh_reg = models.CharField(max_length=30, blank=True, null=True)
    rh_ot = models.CharField(max_length=30, blank=True, null=True)
    rh_nsd = models.CharField(max_length=30, blank=True, null=True)
    rh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    dh_reg = models.CharField(max_length=30, blank=True, null=True)
    dh_ot = models.CharField(max_length=30, blank=True, null=True)
    dh_nsd = models.CharField(max_length=30, blank=True, null=True)
    dh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_reg = models.CharField(max_length=30, blank=True, null=True)
    rd_ot = models.CharField(max_length=30, blank=True, null=True)
    rd_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_sh_reg = models.CharField(max_length=30, blank=True, null=True)
    rd_sh_ot = models.CharField(max_length=30, blank=True, null=True)
    rd_sh_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_sh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_rh_reg = models.CharField(max_length=30, blank=True, null=True)
    rd_rh_ot = models.CharField(max_length=30, blank=True, null=True)
    rd_rh_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_rh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_dh_reg = models.CharField(max_length=30, blank=True, null=True)
    rd_dh_ot = models.CharField(max_length=30, blank=True, null=True)
    rd_dh_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_dh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    tardy = models.CharField(max_length=30, blank=True, null=True)
    undertime = models.CharField(max_length=30, blank=True, null=True)
    absent = models.CharField(max_length=30, blank=True, null=True)
    tardy_times = models.CharField(max_length=30, blank=True, null=True)
    undertime_times = models.CharField(max_length=30, blank=True, null=True)
    absent_times = models.CharField(max_length=30, blank=True, null=True)
    entry_type = models.CharField(max_length=30, blank=True, null=True)
    hours_worked_on_leave = models.CharField(max_length=30, blank=True, null=True)
    uh_rd = models.CharField(max_length=30, blank=True, null=True)
    dtrexmpt = models.CharField(db_column='DTRExmpt', max_length=30, blank=True, null=True)  # Field name made lowercase.
    uh_rh = models.CharField(max_length=60, blank=True, null=True)
    uh_sh = models.CharField(max_length=60, blank=True, null=True)
    sys_type = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_work_categorization'


class TblPsWorkCategorizationPosted(models.Model):
    auto_no = models.BigAutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    company_code = models.CharField(db_column='Company_Code', max_length=2)  # Field name made lowercase.
    branch_code = models.SmallIntegerField(db_column='Branch_Code')  # Field name made lowercase.
    emp_id = models.CharField(db_column='Emp_ID', max_length=11, blank=True, null=True)  # Field name made lowercase.
    emp_name = models.CharField(db_column='Emp_name', max_length=999, blank=True, null=True)  # Field name made lowercase.
    payrollperiod = models.CharField(db_column='PayrollPeriod', max_length=999)  # Field name made lowercase.
    department = models.CharField(max_length=999, blank=True, null=True)
    department_desc = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center = models.CharField(max_length=999, blank=True, null=True)
    responsibility_center_desc = models.CharField(max_length=999, blank=True, null=True)
    hours_worked = models.CharField(max_length=30, blank=True, null=True)
    od_reg = models.CharField(max_length=30, blank=True, null=True)
    od_ot = models.CharField(max_length=30, blank=True, null=True)
    od_nsd = models.CharField(max_length=30, blank=True, null=True)
    od_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    sh_reg = models.CharField(max_length=30, blank=True, null=True)
    sh_ot = models.CharField(max_length=30, blank=True, null=True)
    sh_nsd = models.CharField(max_length=30, blank=True, null=True)
    sh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    rh_reg = models.CharField(max_length=30, blank=True, null=True)
    rh_ot = models.CharField(max_length=30, blank=True, null=True)
    rh_nsd = models.CharField(max_length=30, blank=True, null=True)
    rh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    dh_reg = models.CharField(max_length=30, blank=True, null=True)
    dh_ot = models.CharField(max_length=30, blank=True, null=True)
    dh_nsd = models.CharField(max_length=30, blank=True, null=True)
    dh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_reg = models.CharField(max_length=30, blank=True, null=True)
    rd_ot = models.CharField(max_length=30, blank=True, null=True)
    rd_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_sh_reg = models.CharField(max_length=30, blank=True, null=True)
    rd_sh_ot = models.CharField(max_length=30, blank=True, null=True)
    rd_sh_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_sh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_rh_reg = models.CharField(max_length=30, blank=True, null=True)
    rd_rh_ot = models.CharField(max_length=30, blank=True, null=True)
    rd_rh_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_rh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_dh_reg = models.CharField(max_length=30, blank=True, null=True)
    rd_dh_ot = models.CharField(max_length=30, blank=True, null=True)
    rd_dh_nsd = models.CharField(max_length=30, blank=True, null=True)
    rd_dh_ot_nsd = models.CharField(max_length=30, blank=True, null=True)
    date_posted = models.CharField(max_length=30, blank=True, null=True)
    posted_by = models.CharField(max_length=999)
    tardy = models.CharField(max_length=30, blank=True, null=True)
    undertime = models.CharField(max_length=30, blank=True, null=True)
    absent = models.CharField(max_length=30, blank=True, null=True)
    tardy_times = models.CharField(max_length=30, blank=True, null=True)
    undertime_times = models.CharField(max_length=30, blank=True, null=True)
    absent_times = models.CharField(max_length=30, blank=True, null=True)
    dtrexmpt = models.CharField(db_column='DTRExmpt', max_length=30, blank=True, null=True)  # Field name made lowercase.
    uh_rd = models.CharField(max_length=30, blank=True, null=True)
    uh_rh = models.CharField(max_length=60, blank=True, null=True)
    uh_sh = models.CharField(max_length=60, blank=True, null=True)
    batch_no = models.CharField(max_length=2, blank=True, null=True)
    sys_type = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_work_categorization_posted'


class TblPsZktecoEmpid(models.Model):
    autonum = models.AutoField(primary_key=True)
    emp_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    ac_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_ps_zkteco_empid'


class TblRcc(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    code = models.SmallIntegerField(blank=True, null=True)
    category = models.CharField(max_length=60, blank=True, null=True)
    budget_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_rcc'


class TblRccDetails(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=60, blank=True, null=True)
    desc_code = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    rc_cost_category = models.CharField(max_length=100, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    alter_code = models.CharField(max_length=50, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    mfg_date = models.CharField(max_length=25, blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.CharField(max_length=25, blank=True, null=True)
    mod_type = models.CharField(max_length=10)
    mod_type_dup = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'tbl_rcc_details'


class TblRccSubCategory(models.Model):
    desc_code = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    sub_code = models.IntegerField(blank=True, null=True)
    sub_category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_rcc_sub_category'


class TblReportResponsibilities(models.Model):
    auto_no = models.IntegerField(db_column='Auto_No', blank=True, null=True)  # Field name made lowercase.
    report_name = models.CharField(db_column='Report_Name', max_length=150, blank=True, null=True)  # Field name made lowercase.
    responsibility = models.CharField(db_column='Responsibility', max_length=150, blank=True, null=True)  # Field name made lowercase.
    emp_id = models.CharField(max_length=33, blank=True, null=True)
    personnel = models.CharField(db_column='Personnel', max_length=150, blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=450, blank=True, null=True)  # Field name made lowercase.
    created_by = models.CharField(db_column='Created_by', max_length=150, blank=True, null=True)  # Field name made lowercase.
    date_time_created = models.CharField(max_length=150, blank=True, null=True)
    modified_by = models.CharField(max_length=150, blank=True, null=True)
    date_time_modified = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_report_responsibilities'


class TblResolutionno(models.Model):
    company_code = models.IntegerField(db_column='Company_code', blank=True, null=True)  # Field name made lowercase.
    store_code = models.IntegerField(db_column='Store_code', blank=True, null=True)  # Field name made lowercase.
    sss_repact = models.CharField(db_column='SSS_repAct', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phic_repact = models.CharField(db_column='PHIC_repAct', max_length=100, blank=True, null=True)  # Field name made lowercase.
    hdmf_repact = models.CharField(db_column='HDMF_repAct', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tax_repact = models.CharField(db_column='Tax_repAct', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_resolutionno'


class TblRpnPaymentRequestList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    rpn_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.PositiveIntegerField(blank=True, null=True)
    payee = models.CharField(max_length=150, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    drawee_bank = models.CharField(max_length=150, blank=True, null=True)
    date_check = models.DateField(blank=True, null=True)
    check_no = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=999, blank=True, null=True)
    transtype = models.CharField(db_column='TransType', max_length=150, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(max_length=2, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancel_by = models.CharField(max_length=60, blank=True, null=True)
    cancel_date = models.CharField(max_length=25, blank=True, null=True)
    disapproved_by = models.CharField(max_length=60, blank=True, null=True)
    disapproved_date = models.CharField(max_length=25, blank=True, null=True)
    cv_ref_no = models.FloatField(blank=True, null=True)
    cv_ref_type = models.CharField(max_length=10, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_rpn_payment_request_list'


class TblRpnPaymentRequestListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    rpn_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    amount_due = models.FloatField(blank=True, null=True)
    amount_paid = models.FloatField(blank=True, null=True)
    active = models.CharField(max_length=2, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_rpn_payment_request_listing'


class TblSalesAgent(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.SmallIntegerField(blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    home_phone_no = models.CharField(max_length=15, blank=True, null=True)
    mobile_no = models.CharField(max_length=15, blank=True, null=True)
    fax_no = models.CharField(max_length=15, blank=True, null=True)
    st_address = models.CharField(max_length=60, blank=True, null=True)
    city_address = models.CharField(max_length=30, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    date_entered = models.DateField(blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    with_collector = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_sales_agent'


class TblSetup(models.Model):
    autonum = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=150, blank=True, null=True)
    acct_title = models.TextField(blank=True, null=True)
    sl_acct = models.CharField(max_length=100, blank=True, null=True)
    sl_id = models.IntegerField(blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    acct_title2 = models.CharField(max_length=150, blank=True, null=True)
    module = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_setup'


class TblSetupConfiguration(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    reports_name = models.CharField(max_length=100, blank=True, null=True)
    view_reports = models.CharField(max_length=10, blank=True, null=True)
    module = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_setup_configuration'


class TblSetupTranstype(models.Model):
    autonum = models.AutoField(primary_key=True)
    adj_type = models.CharField(max_length=50, blank=True, null=True)
    transaction_type = models.CharField(max_length=150, blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    setup_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_setup_transtype'


class TblSetupWht(models.Model):
    autonum = models.AutoField(primary_key=True)
    tax = models.FloatField(blank=True, null=True)
    event_name = models.CharField(max_length=150, blank=True, null=True)
    acct_title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_setup_wht'


class TblShiftHistory(models.Model):
    company_code = models.IntegerField(db_column='Company_code', blank=True, null=True)  # Field name made lowercase.
    store_code = models.IntegerField(db_column='Store_code', blank=True, null=True)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date_change = models.DateField(db_column='Date_Change', blank=True, null=True)  # Field name made lowercase.
    dept_id = models.FloatField(db_column='Dept_ID', blank=True, null=True)  # Field name made lowercase.
    empposition = models.FloatField(db_column='EmpPosition', blank=True, null=True)  # Field name made lowercase.
    shift_sched = models.FloatField(db_column='Shift_Sched', blank=True, null=True)  # Field name made lowercase.
    usern = models.CharField(db_column='UserN', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_shift_history'


class TblShiftHistoryEmp(models.Model):
    reference = models.CharField(db_column='Reference', max_length=20, blank=True, null=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_ID', blank=True, null=True)  # Field name made lowercase.
    current_shift = models.FloatField(db_column='Current_shift', blank=True, null=True)  # Field name made lowercase.
    date_change = models.DateField(db_column='Date_change', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_shift_history_emp'


class TblSlCategory(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    code = models.SmallIntegerField(blank=True, null=True)
    category = models.CharField(max_length=60, blank=True, null=True)
    module = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_sl_category'


class TblSssCon(models.Model):
    sched_id = models.AutoField(primary_key=True)
    from_amount = models.FloatField(blank=True, null=True)
    to_amount = models.FloatField(blank=True, null=True)
    m_salary = models.FloatField(blank=True, null=True)
    wisp = models.FloatField(blank=True, null=True)
    ss_er = models.FloatField(blank=True, null=True)
    ss_ee = models.FloatField(blank=True, null=True)
    ec_er = models.FloatField(blank=True, null=True)
    wisp_er = models.FloatField(blank=True, null=True)
    wisp_ee = models.FloatField(blank=True, null=True)
    tc_er = models.FloatField(blank=True, null=True)
    tc_ee = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_sss_con'


class TblStudent(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.PositiveIntegerField()
    student_class = models.CharField(max_length=1, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    address = models.CharField(max_length=150, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    birth_place = models.CharField(max_length=150, blank=True, null=True)
    father_name = models.CharField(max_length=60, blank=True, null=True)
    mother_name = models.CharField(max_length=60, blank=True, null=True)
    parents_adds = models.CharField(max_length=150, blank=True, null=True)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    baptized = models.CharField(max_length=150, blank=True, null=True)
    confirmed = models.CharField(max_length=150, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    religion = models.CharField(max_length=30, blank=True, null=True)
    level = models.CharField(max_length=1, blank=True, null=True)
    year_grade = models.CharField(max_length=30, blank=True, null=True)
    school_year = models.CharField(max_length=20, db_collation='latin1_bin', blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    student_image = models.TextField(blank=True, null=True)
    date_entered = models.DateField(blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_student'
        unique_together = (('id_code', 'last_name', 'first_name', 'middle_name'),)


class TblSubLedger(models.Model):
    autonum = models.AutoField(primary_key=True)
    ul_code = models.SmallIntegerField(blank=True, null=True)
    id_code = models.PositiveBigIntegerField(blank=True, null=True)
    sl_acct = models.CharField(max_length=100, blank=True, null=True)
    guarantor_id = models.PositiveIntegerField(blank=True, null=True)
    guarantor = models.CharField(max_length=150, blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    reference_no = models.CharField(max_length=25, blank=True, null=True)
    doc_ref = models.FloatField(blank=True, null=True)
    particulars = models.CharField(max_length=800, blank=True, null=True)
    acct_code = models.FloatField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    balance_as_of = models.FloatField(blank=True, null=True)
    beginning_bal = models.FloatField(blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    autonum_trans = models.BigIntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_sub_ledger'
        unique_together = (('autonum', 'id_code', 'sl_acct', 'date_trans', 'reference_no', 'particulars', 'sl_type'),)


class TblSubLedgerCutoffList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=11, blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    cut_off_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_sub_ledger_cutoff_list'


class TblSubLedgerCutoffListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.SmallIntegerField(blank=True, null=True)
    code = models.CharField(max_length=11, blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    id_code = models.IntegerField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    cut_off_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_sub_ledger_cutoff_listing'


class TblSupplier(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.PositiveIntegerField()
    trade_name = models.CharField(max_length=150, blank=True, null=True)
    supplier_class = models.CharField(max_length=15, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=20)
    business_phone_no = models.CharField(max_length=15, blank=True, null=True)
    mobile_no = models.CharField(max_length=15, blank=True, null=True)
    fax_no = models.CharField(max_length=15, blank=True, null=True)
    st_address = models.CharField(max_length=60, blank=True, null=True)
    city_address = models.CharField(max_length=30, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    trade = models.CharField(max_length=1, blank=True, null=True)
    vat = models.CharField(max_length=1, blank=True, null=True)
    bir_reg_no = models.CharField(max_length=20, blank=True, null=True)
    tax_id_no = models.CharField(max_length=25, blank=True, null=True)
    credit_terms = models.SmallIntegerField(blank=True, null=True)
    credit_limit = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    date_as_of = models.DateField(blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=150, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    supplier_image = models.TextField(blank=True, null=True)
    date_entered = models.DateField(blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    sl_category = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_supplier'
        unique_together = (('id_code', 'trade_name', 'last_name', 'first_name', 'middle_name'),)


class TblSupplierAtcSetup(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    supplier_id = models.IntegerField(blank=True, null=True)
    atc_id = models.IntegerField(blank=True, null=True)
    atc_acronym = models.CharField(max_length=50, blank=True, null=True)
    short_desc = models.CharField(max_length=15, blank=True, null=True)
    tax_rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_supplier_atc_setup'


class TblSupplierGroup(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_supplier_group'


class TblSysallowances(models.Model):
    allowance_code = models.IntegerField(db_column='Allowance_Code', blank=True, null=True)  # Field name made lowercase.
    allowance_long_description = models.CharField(db_column='Allowance_long_description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    allowance_name = models.CharField(db_column='Allowance_Name', max_length=20)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=20, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apply_payrollperiod = models.IntegerField(db_column='Apply_PayrollPeriod', blank=True, null=True)  # Field name made lowercase.
    taxable_yn = models.CharField(db_column='Taxable_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sss_yn = models.CharField(db_column='SSS_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    number_13month_yn = models.CharField(db_column='13month_YN', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    fixed = models.CharField(db_column='Fixed', max_length=10, blank=True, null=True)  # Field name made lowercase.
    payout_scheme = models.CharField(db_column='Payout_scheme', max_length=30, blank=True, null=True)  # Field name made lowercase.
    allowance_type = models.CharField(db_column='Allowance_type', max_length=30, blank=True, null=True)  # Field name made lowercase.
    effective_from = models.DateField(blank=True, null=True)
    effective_to = models.DateField(blank=True, null=True)
    default_amnt = models.FloatField(db_column='Default_amnt', blank=True, null=True)  # Field name made lowercase.
    allow_sked = models.CharField(max_length=50, blank=True, null=True)
    specific_month = models.TextField(db_column='Specific_month', blank=True, null=True)  # Field name made lowercase.
    first_month_qtr = models.CharField(db_column='First_month_qtr', max_length=40, blank=True, null=True)  # Field name made lowercase.
    based_dtr = models.CharField(db_column='Based_dtr', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cola = models.CharField(db_column='Cola', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bir_tag = models.CharField(max_length=31, blank=True, null=True)
    active = models.CharField(db_column='Active', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_sysallowances'


class TblSysdedWemployershare(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', primary_key=True)  # Field name made lowercase.
    ded_code = models.FloatField(blank=True, null=True)
    ded_name = models.CharField(db_column='Ded_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    base_on = models.CharField(db_column='Base_on', max_length=20, blank=True, null=True)  # Field name made lowercase.
    employee_shr = models.FloatField(blank=True, null=True)
    employer_shr = models.FloatField(blank=True, null=True)
    taxable = models.CharField(db_column='Taxable', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_sysded_wemployershare'


class TblSysdeductions(models.Model):
    deduction_code = models.IntegerField(db_column='Deduction_Code', blank=True, null=True)  # Field name made lowercase.
    deduction_long_description = models.CharField(db_column='Deduction_long_description', max_length=100, blank=True, null=True)  # Field name made lowercase.
    deduction_name = models.CharField(db_column='Deduction_Name', max_length=31, blank=True, null=True)  # Field name made lowercase.
    style = models.CharField(db_column='Style', max_length=20, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deduct_payrollperiod = models.IntegerField(db_column='Deduct_PayrollPeriod', blank=True, null=True)  # Field name made lowercase.
    taxable_yn = models.CharField(db_column='Taxable_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sss_yn = models.CharField(db_column='SSS_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fixed = models.CharField(max_length=10, blank=True, null=True)
    effective_from = models.DateField(blank=True, null=True)
    effective_to = models.DateField(blank=True, null=True)
    deduction_type = models.CharField(db_column='Deduction_type', max_length=30, blank=True, null=True)  # Field name made lowercase.
    default_amnt = models.FloatField(db_column='Default_amnt', blank=True, null=True)  # Field name made lowercase.
    payout_scheme = models.CharField(db_column='Payout_scheme', max_length=30, blank=True, null=True)  # Field name made lowercase.
    d_category = models.CharField(db_column='D_Category', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ded_sked = models.CharField(db_column='Ded_sked', max_length=50, blank=True, null=True)  # Field name made lowercase.
    specific_month = models.TextField(db_column='Specific_month', blank=True, null=True)  # Field name made lowercase.
    first_month_qtr = models.CharField(db_column='First_month_qtr', max_length=40, blank=True, null=True)  # Field name made lowercase.
    quarterly_month = models.CharField(db_column='Quarterly_month', max_length=100, blank=True, null=True)  # Field name made lowercase.
    with_empr_share = models.CharField(db_column='With_empr_share', max_length=5, blank=True, null=True)  # Field name made lowercase.
    base_on = models.CharField(db_column='Base_on', max_length=20, blank=True, null=True)  # Field name made lowercase.
    empr_share = models.FloatField(db_column='Empr_share', blank=True, null=True)  # Field name made lowercase.
    empye_share = models.FloatField(blank=True, null=True)
    bir_tag = models.CharField(max_length=31, blank=True, null=True)
    active = models.CharField(db_column='Active', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_sysdeductions'


class TblSysholidays(models.Model):
    auto_no = models.AutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    holiday_type = models.CharField(db_column='Holiday_Type', max_length=1)  # Field name made lowercase.
    holiday_description = models.CharField(db_column='Holiday_Description', max_length=50)  # Field name made lowercase.
    holiday_date = models.CharField(db_column='Holiday_Date', max_length=30)  # Field name made lowercase.
    yearly_yn = models.CharField(db_column='Yearly_YN', max_length=1)  # Field name made lowercase.
    additional_percent = models.FloatField(db_column='Additional_Percent', blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=30, blank=True, null=True)  # Field name made lowercase.
    date_edited = models.CharField(db_column='Date_Edited', max_length=30, blank=True, null=True)  # Field name made lowercase.
    field_coverage = models.CharField(db_column='Field_Coverage', max_length=30, blank=True, null=True)  # Field name made lowercase.
    locale = models.CharField(db_column='Locale', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_sysholidays'


class TblSysloans(models.Model):
    loan_code = models.CharField(db_column='Loan_Code', primary_key=True, max_length=4)  # Field name made lowercase.
    loan_name = models.CharField(db_column='Loan_Name', max_length=30)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_sysloans'


class TblSysnsdRange(models.Model):
    company_code = models.IntegerField(blank=True, null=True)
    store_code = models.IntegerField(blank=True, null=True)
    nsd_time_from = models.CharField(db_column='NSD_time_from', max_length=30, db_collation='latin1_general_ci', blank=True, null=True)  # Field name made lowercase.
    nsd_time_to = models.CharField(db_column='NSD_time_to', max_length=30, db_collation='latin1_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_sysnsd_range'


class TblSysshiftsked(models.Model):
    shifting_code = models.AutoField(db_column='Shifting_Code', primary_key=True)  # Field name made lowercase.
    shift_name = models.CharField(db_column='Shift_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    time_in1 = models.CharField(db_column='TIME_IN1', max_length=8)  # Field name made lowercase.
    time_out1 = models.CharField(db_column='TIME_OUT1', max_length=8)  # Field name made lowercase.
    time_in2 = models.CharField(db_column='TIME_IN2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    time_out2 = models.CharField(db_column='TIME_OUT2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    snack_in = models.CharField(db_column='SNACK_IN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    snack_out = models.CharField(db_column='SNACK_OUT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    shift_sameday_yn = models.CharField(db_column='Shift_SameDay_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    active_yn = models.CharField(db_column='Active_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ot_break = models.SmallIntegerField(db_column='OT_Break', blank=True, null=True)  # Field name made lowercase.
    restday = models.CharField(db_column='RestDay', max_length=20, blank=True, null=True)  # Field name made lowercase.
    time_cutoff = models.CharField(db_column='TIME_CUTOFF', max_length=8, blank=True, null=True)  # Field name made lowercase.
    additional_time = models.FloatField(blank=True, null=True)
    allowedtimein1 = models.CharField(db_column='AllowedTimeIn1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimein2 = models.CharField(db_column='AllowedTimeIn2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimeout1 = models.CharField(db_column='AllowedTimeOut1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimeout2 = models.CharField(db_column='AllowedTimeOut2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimein3 = models.CharField(db_column='AllowedTimeIn3', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimein4 = models.CharField(db_column='AllowedTimeIn4', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimeout3 = models.CharField(db_column='AllowedTimeOut3', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimeout4 = models.CharField(db_column='AllowedTimeOut4', max_length=8, blank=True, null=True)  # Field name made lowercase.
    shift_type = models.IntegerField(db_column='Shift_type', blank=True, null=True)  # Field name made lowercase.
    hourslimit = models.IntegerField(db_column='HoursLimit', blank=True, null=True)  # Field name made lowercase.
    hourlimit = models.IntegerField(db_column='HourLimit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_sysshiftsked'


class TblSystemconfig(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.IntegerField(db_column='Company_code', blank=True, null=True)  # Field name made lowercase.
    store_code = models.IntegerField(db_column='Store_code', blank=True, null=True)  # Field name made lowercase.
    company_name = models.CharField(db_column='Company_name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    company_name1 = models.CharField(db_column='Company_name1', max_length=60, blank=True, null=True)  # Field name made lowercase.
    company_address = models.CharField(db_column='Company_address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    contact_info = models.CharField(max_length=25, blank=True, null=True)
    site_location = models.CharField(max_length=25, blank=True, null=True)
    logo = models.TextField(db_column='Logo', blank=True, null=True)  # Field name made lowercase.
    logo1 = models.TextField(db_column='Logo1', blank=True, null=True)  # Field name made lowercase.
    machine_ip = models.CharField(db_column='Machine_IP', max_length=70, blank=True, null=True)  # Field name made lowercase.
    empr_taxidno = models.CharField(db_column='empr_taxIDno', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rdo_code = models.CharField(db_column='RDO_code', max_length=10, blank=True, null=True)  # Field name made lowercase.
    empr_name = models.CharField(db_column='Empr_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reg_addrss = models.CharField(db_column='Reg_addrss', max_length=100, blank=True, null=True)  # Field name made lowercase.
    zip_code = models.CharField(db_column='Zip_code', max_length=6, blank=True, null=True)  # Field name made lowercase.
    authorized_rep = models.CharField(db_column='Authorized_rep', max_length=80, blank=True, null=True)  # Field name made lowercase.
    noholiday_pay = models.CharField(db_column='NoHoliday_pay', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cola_proportion_hrs = models.CharField(db_column='Cola_proportion_hrs', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allow_manual_dtr = models.CharField(db_column='Allow_Manual_DTR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fullpayprevday = models.CharField(db_column='FullPayPrevDay', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allow_loadbreaktimelogs = models.CharField(db_column='Allow_LoadBreakTimeLogs', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allow_atuentries = models.CharField(db_column='Allow_ATUEntries', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allow_payrollbatching = models.CharField(db_column='Allow_PayrollBatching', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allow_negative_leaveledger = models.CharField(db_column='Allow_Negative_LeaveLedger', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_systemconfig'


class TblTagcompensation(models.Model):
    autonum = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=150, blank=True, null=True)
    acct_title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tagcompensation'


class TblTax(models.Model):
    auto_no = models.AutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    salary_type = models.CharField(db_column='Salary_type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tax_name = models.CharField(db_column='Tax_Name', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ooop = models.FloatField(db_column='OOOP', blank=True, null=True)  # Field name made lowercase.
    num1 = models.FloatField(db_column='Num1', blank=True, null=True)  # Field name made lowercase.
    num2 = models.FloatField(db_column='Num2', blank=True, null=True)  # Field name made lowercase.
    num3 = models.FloatField(db_column='Num3', blank=True, null=True)  # Field name made lowercase.
    num4 = models.FloatField(db_column='Num4', blank=True, null=True)  # Field name made lowercase.
    num5 = models.FloatField(db_column='Num5', blank=True, null=True)  # Field name made lowercase.
    num6 = models.FloatField(db_column='Num6', blank=True, null=True)  # Field name made lowercase.
    num7 = models.FloatField(db_column='Num7', blank=True, null=True)  # Field name made lowercase.
    num8 = models.FloatField(db_column='Num8', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_tax'


class TblTaxAnnual(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    over_annual = models.FloatField(db_column='Over_annual', blank=True, null=True)  # Field name made lowercase.
    not_over_annual = models.FloatField(db_column='Not_over_annual', blank=True, null=True)  # Field name made lowercase.
    amount_annual = models.FloatField(db_column='Amount_annual', blank=True, null=True)  # Field name made lowercase.
    rate_percent_annual = models.FloatField(db_column='Rate_Percent_annual', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_tax_annual'


class TblTaxExemptionList(models.Model):
    auto_num = models.AutoField(db_column='Auto_num', primary_key=True)  # Field name made lowercase.
    tax_name = models.CharField(max_length=250, blank=True, null=True)
    tax_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tax_exemption_list'


class TblTaxNew(models.Model):
    auto_no = models.AutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    salary_type = models.CharField(db_column='Salary_type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tax_name = models.CharField(db_column='Tax_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num1 = models.FloatField(db_column='Num1', blank=True, null=True)  # Field name made lowercase.
    num2 = models.FloatField(db_column='Num2', blank=True, null=True)  # Field name made lowercase.
    num3 = models.FloatField(db_column='Num3', blank=True, null=True)  # Field name made lowercase.
    num4 = models.FloatField(db_column='Num4', blank=True, null=True)  # Field name made lowercase.
    num5 = models.FloatField(db_column='Num5', blank=True, null=True)  # Field name made lowercase.
    num6 = models.FloatField(db_column='Num6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_tax_new'


class TblTmsBalanceConfirmationList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    date_cut_off = models.CharField(max_length=225, blank=True, null=True)
    bank_id = models.FloatField(blank=True, null=True)
    bank_account = models.CharField(db_column='Bank_account', max_length=225, blank=True, null=True)  # Field name made lowercase.
    doc_type = models.CharField(max_length=225, blank=True, null=True)
    doc_no = models.CharField(max_length=225, blank=True, null=True)
    total_balance = models.FloatField(blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allow_multiple_date = models.CharField(db_column='Allow_multiple_date', max_length=1, blank=True, null=True)  # Field name made lowercase.
    allow_multiple_account = models.CharField(db_column='Allow_multiple_account', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=100, blank=True, null=True)
    approved_date = models.CharField(max_length=100, blank=True, null=True)
    cancelled_by = models.CharField(max_length=60, blank=True, null=True)
    cancelled_date = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tms_balance_confirmation_list'


class TblTmsBalanceConfirmationListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    day = models.CharField(db_column='Day', max_length=225, blank=True, null=True)  # Field name made lowercase.
    drawee_id = models.CharField(max_length=10, blank=True, null=True)
    drawee_bank = models.CharField(max_length=225, blank=True, null=True)
    doc_type = models.CharField(max_length=225, blank=True, null=True)
    doc_no = models.CharField(max_length=225, blank=True, null=True)
    balance_amount = models.FloatField(db_column='Balance_amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_tms_balance_confirmation_listing'


class TblTmsBankCreditMemoList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    bank_date = models.CharField(max_length=25, blank=True, null=True)
    bank_id = models.FloatField(blank=True, null=True)
    bank_account = models.CharField(max_length=100, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancelled_by = models.CharField(max_length=60, blank=True, null=True)
    cancelled_date = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tms_bank_credit_memo_list'


class TblTmsBankCreditMemoListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    line_number = models.IntegerField(blank=True, null=True)
    bank_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tms_bank_credit_memo_listing'


class TblTmsBankDebitMemoList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    bank_date = models.CharField(max_length=25, blank=True, null=True)
    bank_id = models.FloatField(blank=True, null=True)
    bank_account = models.CharField(max_length=100, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=25, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancelled_by = models.CharField(max_length=60, blank=True, null=True)
    cancelled_date = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tms_bank_debit_memo_list'


class TblTmsBankDebitMemoListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    line_number = models.IntegerField(blank=True, null=True)
    bank_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tms_bank_debit_memo_listing'


class TblTmsOutstandingChecksIssuedList(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.BigIntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=5, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    record_month = models.CharField(max_length=50, blank=True, null=True)
    record_year = models.CharField(max_length=4, blank=True, null=True)
    doc_date = models.CharField(max_length=25, blank=True, null=True)
    bank_code = models.BigIntegerField(blank=True, null=True)
    bank_account = models.CharField(max_length=50, blank=True, null=True)
    date_adjust = models.CharField(max_length=25, blank=True, null=True)
    doc_no_adjust = models.FloatField(blank=True, null=True)
    bank_code_rev = models.BigIntegerField(blank=True, null=True)
    bank_account_rev = models.CharField(max_length=50, blank=True, null=True)
    date_rev = models.CharField(max_length=25, blank=True, null=True)
    doc_no_rev = models.FloatField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=225, blank=True, null=True)
    trans_type = models.CharField(max_length=225, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=100, blank=True, null=True)
    reviewed_by = models.CharField(max_length=100, blank=True, null=True)
    approved_by = models.CharField(max_length=100, blank=True, null=True)
    cancel_by = models.CharField(max_length=100, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancelled_date = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tms_outstanding_checks_issued_list'


class TblTmsOutstandingChecksIssuedListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    doc_date = models.DateField(blank=True, null=True)
    jv_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.PositiveIntegerField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    guarantor_id = models.PositiveIntegerField(blank=True, null=True)
    guarantor = models.CharField(max_length=150, blank=True, null=True)
    account_code = models.FloatField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    active = models.CharField(max_length=2, blank=True, null=True)
    posted_by = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.DateField(blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    payment_status = models.CharField(max_length=10, blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tms_outstanding_checks_issued_listing'


class TblTmsProductReceiptOnlinePaymentSetup(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    date_credited = models.CharField(max_length=25, blank=True, null=True)
    date_trans = models.CharField(max_length=25, blank=True, null=True)
    code = models.FloatField(blank=True, null=True)
    bank_account = models.CharField(max_length=60, blank=True, null=True)
    sl_code = models.FloatField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=25, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancelled_by = models.CharField(max_length=60, blank=True, null=True)
    cancelled_date = models.CharField(max_length=25, blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tms_product_receipt_online_payment_setup'


class TblTmsProductSalesInvoiceOnlinePaymentSetup(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    company_code = models.CharField(max_length=10, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    date_credited = models.CharField(max_length=25, blank=True, null=True)
    date_trans = models.CharField(max_length=25, blank=True, null=True)
    code = models.FloatField(blank=True, null=True)
    bank_account = models.CharField(max_length=60, blank=True, null=True)
    sl_code = models.FloatField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=25, blank=True, null=True)
    reviewed_date = models.CharField(max_length=25, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    approved_date = models.CharField(max_length=25, blank=True, null=True)
    cancelled_by = models.CharField(max_length=60, blank=True, null=True)
    cancelled_date = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_tms_product_sales_invoice_online_payment_setup'


class TblTransactionListingApv(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    supplier = models.CharField(max_length=150, blank=True, null=True)
    apv_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.FloatField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    primary_code = models.PositiveSmallIntegerField(blank=True, null=True)
    secondary_code = models.PositiveSmallIntegerField(blank=True, null=True)
    acct_code = models.PositiveSmallIntegerField(blank=True, null=True)
    subsidiary_code = models.PositiveSmallIntegerField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    terms_payment = models.PositiveSmallIntegerField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    active = models.CharField(max_length=2, blank=True, null=True)
    posted_by = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.DateField(blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    payment_status = models.CharField(max_length=10, blank=True, null=True)
    transtype_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_transaction_listing_apv'


class TblTransactionListingAr(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    customer = models.CharField(max_length=150, blank=True, null=True)
    ci_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.FloatField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    guarantor_id = models.PositiveIntegerField(blank=True, null=True)
    guarantor = models.CharField(max_length=150, blank=True, null=True)
    primary_code = models.PositiveIntegerField(blank=True, null=True)
    secondary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_code = models.PositiveIntegerField(blank=True, null=True)
    subsidiary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    terms_payment = models.PositiveSmallIntegerField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    active = models.CharField(max_length=2, blank=True, null=True)
    posted_by = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.DateField(blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    terminal_no = models.CharField(max_length=21, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    payment_status = models.CharField(max_length=10, blank=True, null=True)
    transtype_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_transaction_listing_ar'


class TblTransactionListingCdb(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    payee = models.CharField(max_length=150, blank=True, null=True)
    cv_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.FloatField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    guarantor_id = models.PositiveIntegerField(blank=True, null=True)
    guarantor = models.CharField(max_length=150, blank=True, null=True)
    primary_code = models.PositiveIntegerField(blank=True, null=True)
    secondary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_code = models.PositiveIntegerField(blank=True, null=True)
    subsidiary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    active = models.CharField(max_length=2, blank=True, null=True)
    posted_by = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.DateField(blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    check_no = models.CharField(max_length=50, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    payment_status = models.CharField(max_length=10, blank=True, null=True)
    transtype_status = models.CharField(max_length=20, blank=True, null=True)
    cleared_amount = models.FloatField(blank=True, null=True)
    cleared_date = models.CharField(max_length=25, blank=True, null=True)
    expiry_date = models.CharField(max_length=25, blank=True, null=True)
    status_stale = models.CharField(max_length=1, blank=True, null=True)
    check_status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_transaction_listing_cdb'


class TblTransactionListingCrb(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    payor = models.CharField(max_length=150, blank=True, null=True)
    ref_or_no = models.FloatField()
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.FloatField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    guarantor_id = models.PositiveIntegerField(blank=True, null=True)
    guarantor = models.CharField(max_length=150, blank=True, null=True)
    primary_code = models.PositiveIntegerField(blank=True, null=True)
    secondary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_code = models.PositiveIntegerField(blank=True, null=True)
    subsidiary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    terms_payment = models.SmallIntegerField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    active = models.CharField(max_length=2, blank=True, null=True)
    posted_by = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.DateField(blank=True, null=True)
    trans_type = models.CharField(max_length=2, blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    payment_status = models.CharField(max_length=10, blank=True, null=True)
    transtype_status = models.CharField(max_length=20, blank=True, null=True)
    terminal_no = models.CharField(max_length=21, blank=True, null=True)
    collected_amount = models.FloatField(blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_transaction_listing_crb'


class TblTransactionListingGj(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    jv_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.FloatField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    guarantor_id = models.PositiveIntegerField(blank=True, null=True)
    guarantor = models.CharField(max_length=150, blank=True, null=True)
    primary_code = models.PositiveIntegerField(blank=True, null=True)
    secondary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_code = models.PositiveIntegerField(blank=True, null=True)
    subsidiary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    active = models.CharField(max_length=2, blank=True, null=True)
    posted_by = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.DateField(blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)
    sys_type = models.CharField(max_length=4, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    payment_status = models.CharField(max_length=10, blank=True, null=True)
    transtype_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_transaction_listing_gj'


class TblTypeTrans(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.CharField(max_length=10, blank=True, null=True)
    type_of_trans = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_type_trans'


class TblUnitLocation(models.Model):
    autonum = models.AutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    unit_description = models.CharField(max_length=30, blank=True, null=True)
    location_description = models.CharField(max_length=40, blank=True, null=True)
    alpha_code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_unit_location'


class TblUnpostLogs(models.Model):
    user_id = models.CharField(max_length=100, blank=True, null=True)
    datetime = models.DateTimeField(db_column='dateTime', blank=True, null=True)  # Field name made lowercase.
    module = models.CharField(max_length=50, blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    reference_no = models.CharField(max_length=20, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    sys_type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_unpost_logs'


class TblUser(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.CharField(max_length=5, blank=True, null=True)
    fullname = models.CharField(max_length=40, blank=True, null=True)
    department = models.CharField(max_length=30, blank=True, null=True)
    responsibility_center = models.CharField(max_length=60, blank=True, null=True)
    user_name = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    user_rank = models.CharField(max_length=20, blank=True, null=True)
    sys_type = models.CharField(max_length=2, blank=True, null=True)
    mod_access = models.TextField(blank=True, null=True)
    acct_title = models.TextField(blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user'


class TblUserConnect(models.Model):
    autonum = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=40, blank=True, null=True)
    sys_type = models.CharField(max_length=2, blank=True, null=True)
    login_date = models.DateField(blank=True, null=True)
    login_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user_connect'


class TblUserRankAccess(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    user_rank = models.CharField(max_length=35, blank=True, null=True)
    mod_access = models.CharField(max_length=5000, blank=True, null=True)
    sys_type = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user_rank_access'


class TblVat(models.Model):
    autonum = models.AutoField(primary_key=True)
    vat_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_vat'


class TblZTempEmpTime(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=250, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=350, blank=True, null=True)  # Field name made lowercase.
    date_log = models.DateField(db_column='Date_log', blank=True, null=True)  # Field name made lowercase.
    timein_1 = models.CharField(db_column='TIMEIN_1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    timeout_1 = models.CharField(db_column='TIMEOUT_1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    timein_2 = models.CharField(db_column='TIMEIN_2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    timeout_2 = models.CharField(db_column='TIMEOUT_2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    timein_3 = models.CharField(db_column='TIMEIN_3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    timeout_3 = models.CharField(db_column='TIMEOUT_3', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_z_temp_emp_time'


class TblZkteco(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    bio_code = models.CharField(max_length=11, blank=True, null=True)
    full_name = models.CharField(max_length=999, blank=True, null=True)
    date = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    doc_no = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=50, blank=True, null=True)
    trans_date = models.CharField(max_length=100, blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    port_no = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_zkteco'


class TblZktecoDisallowedMultipleLogs(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    bio_code = models.CharField(max_length=11, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=25, blank=True, null=True)
    time = models.CharField(max_length=25, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)
    doc_no = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    trans_date = models.CharField(max_length=50, blank=True, null=True)
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    disallowed_timeset = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_zkteco_disallowed_multiple_logs'


class TblZktecoDuplicateLogs(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    bio_code = models.CharField(max_length=11, blank=True, null=True)
    full_name = models.CharField(max_length=999, blank=True, null=True)
    date = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    reload_date = models.CharField(max_length=100, blank=True, null=True)
    doc_no = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=50, blank=True, null=True)
    trans_date = models.CharField(max_length=100, blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    port_no = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_zkteco_duplicate_logs'


class TblZktecoList(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=999, blank=True, null=True)  # Field name made lowercase.
    doc_no = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=50, blank=True, null=True)
    trans_date = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    port_no = models.CharField(max_length=10, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_zkteco_list'


class TblZktecoListing(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    bio_code = models.CharField(max_length=11, blank=True, null=True)
    full_name = models.CharField(max_length=999, blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    doc_no = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=50, blank=True, null=True)
    trans_date = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_zkteco_listing'


class TblZktecoUnofficialLogs(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    bio_code = models.CharField(max_length=11, blank=True, null=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=25, blank=True, null=True)
    time = models.CharField(max_length=25, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)
    doc_no = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    trans_date = models.CharField(max_length=50, blank=True, null=True)
    ip_address = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_zkteco_unofficial_logs'


class TblZktecoUnrecognizeLogs(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    bio_code = models.CharField(max_length=11, blank=True, null=True)
    full_name = models.CharField(max_length=999, blank=True, null=True)
    date = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    doc_no = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=50, blank=True, null=True)
    trans_date = models.CharField(max_length=100, blank=True, null=True)
    ip_address = models.CharField(max_length=50, blank=True, null=True)
    port_no = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_zkteco_unrecognize_logs'


class TempDtrTblBiokey(models.Model):
    auto_no = models.AutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    finger_id = models.IntegerField(db_column='Finger_ID', blank=True, null=True)  # Field name made lowercase.
    field_date = models.DateField(db_column='_Date', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_time = models.CharField(db_column='_Time', max_length=21, blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    field_status = models.IntegerField(db_column='_Status', blank=True, null=True)  # Field name made lowercase. Field renamed because it started with '_'.
    terminal_no = models.CharField(db_column='Terminal_no', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'temp_dtr_tbl_biokey'


class TempTblDepartment(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.IntegerField(blank=True, null=True)
    dept_description = models.CharField(max_length=60, blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    oic_id = models.IntegerField(blank=True, null=True)
    date_created = models.CharField(max_length=45, blank=True, null=True)
    date_updated = models.CharField(max_length=45, blank=True, null=True)
    date_uploaded = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_tbl_department'


class TempTblEmpTime(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=30, blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=10, db_collation='latin1_bin', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'temp_tbl_emp_time'


class TempTblEmpTimePass(models.Model):
    auto_no = models.AutoField(db_column='Auto_No', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    timeout = models.CharField(db_column='TimeOut', max_length=20, blank=True, null=True)  # Field name made lowercase.
    timein = models.CharField(db_column='TimeIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nohours = models.FloatField(db_column='NoHours', blank=True, null=True)  # Field name made lowercase.
    status_bp = models.CharField(db_column='Status_BP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'temp_tbl_emp_time_pass'


class TempTblEmployee(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.CharField(max_length=11)
    emp_id = models.IntegerField(db_column='Emp_ID', blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(max_length=55, blank=True, null=True)
    first_name = models.CharField(max_length=55, blank=True, null=True)
    middle_name = models.CharField(max_length=55, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    desc_department = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=75, blank=True, null=True)
    home_phone_no = models.CharField(max_length=15, blank=True, null=True)
    mobile_no = models.CharField(max_length=25, blank=True, null=True)
    fax_no = models.CharField(max_length=15, blank=True, null=True)
    st_address = models.CharField(max_length=60, blank=True, null=True)
    city_address = models.CharField(max_length=30, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    date_as_of = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)
    employee_image = models.TextField(blank=True, null=True)
    date_entered = models.DateField(blank=True, null=True)
    ul_code = models.IntegerField(blank=True, null=True)
    manual_yn = models.CharField(db_column='Manual_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    release_type = models.CharField(db_column='Release_type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    flexibreak = models.CharField(db_column='FlexiBreak', max_length=5, blank=True, null=True)  # Field name made lowercase.
    responsibility_center_code = models.CharField(max_length=11, blank=True, null=True)
    responsibility_center = models.CharField(max_length=250, blank=True, null=True)
    fixed_schedule = models.CharField(max_length=2, blank=True, null=True)
    schedule = models.IntegerField(db_column='SCHEDULE', blank=True, null=True)  # Field name made lowercase.
    civil_stat = models.CharField(db_column='Civil_stat', max_length=15, blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=5, blank=True, null=True)  # Field name made lowercase.
    finger_id = models.CharField(db_column='Finger_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    auto_filldtr = models.CharField(db_column='Auto_FillDTR', max_length=5, blank=True, null=True)  # Field name made lowercase.
    basic_comp = models.CharField(db_column='Basic_Comp', max_length=1, blank=True, null=True)  # Field name made lowercase.
    perjob_comp = models.CharField(db_column='PerJob_Comp', max_length=1, blank=True, null=True)  # Field name made lowercase.
    acct_no = models.CharField(db_column='Acct_no', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paid_lunch = models.CharField(db_column='Paid_Lunch', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sss_chk = models.CharField(db_column='SSS_chk', max_length=5, blank=True, null=True)  # Field name made lowercase.
    phic_chk = models.CharField(db_column='PHIC_chk', max_length=5, blank=True, null=True)  # Field name made lowercase.
    hdmf_chk = models.CharField(db_column='HDMF_chk', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tax_chk = models.CharField(db_column='Tax_chk', max_length=5, blank=True, null=True)  # Field name made lowercase.
    emp_status = models.CharField(max_length=50, blank=True, null=True)
    date_fired = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(db_column='Gender', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tax_exemption = models.CharField(max_length=50, blank=True, null=True)
    cola = models.CharField(max_length=1, blank=True, null=True)
    cola_taxable = models.CharField(max_length=1, blank=True, null=True)
    cola_based_on_dtr = models.CharField(max_length=1, blank=True, null=True)
    cola_amount = models.CharField(max_length=999, blank=True, null=True)
    bir_schedule = models.CharField(max_length=10, blank=True, null=True)
    dtr_rotation_id = models.CharField(max_length=20, blank=True, null=True)
    am_only = models.CharField(max_length=2, blank=True, null=True)
    pm_only = models.CharField(max_length=2, blank=True, null=True)
    salary_type = models.CharField(max_length=25, blank=True, null=True)
    date_created = models.CharField(max_length=45, blank=True, null=True)
    date_updated = models.CharField(max_length=45, blank=True, null=True)
    date_uploaded = models.CharField(max_length=45, blank=True, null=True)
    status_field = models.IntegerField(db_column='status_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'temp_tbl_employee'
        unique_together = (('id_code', 'last_name', 'first_name', 'middle_name'),)


class TempTblSysshiftsked(models.Model):
    shifting_code = models.AutoField(db_column='Shifting_Code')  # Field name made lowercase.
    shift_name = models.CharField(db_column='Shift_Name', max_length=20)  # Field name made lowercase.
    time_in1 = models.CharField(db_column='TIME_IN1', max_length=8)  # Field name made lowercase.
    time_out1 = models.CharField(db_column='TIME_OUT1', max_length=8)  # Field name made lowercase.
    time_in2 = models.CharField(db_column='TIME_IN2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    time_out2 = models.CharField(db_column='TIME_OUT2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    snack_in = models.CharField(db_column='SNACK_IN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    snack_out = models.CharField(db_column='SNACK_OUT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    shift_sameday_yn = models.CharField(db_column='Shift_SameDay_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    active_yn = models.CharField(db_column='Active_YN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ot_break = models.SmallIntegerField(db_column='OT_Break', blank=True, null=True)  # Field name made lowercase.
    restday = models.CharField(db_column='RestDay', max_length=20, blank=True, null=True)  # Field name made lowercase.
    time_cutoff = models.CharField(db_column='TIME_CUTOFF', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimein1 = models.CharField(db_column='AllowedTimeIn1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimein2 = models.CharField(db_column='AllowedTimeIn2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimeout1 = models.CharField(db_column='AllowedTimeOut1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    allowedtimeout2 = models.CharField(db_column='AllowedTimeOut2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    shift_type = models.IntegerField(db_column='Shift_type', blank=True, null=True)  # Field name made lowercase.
    date_created = models.CharField(max_length=45, blank=True, null=True)
    date_updated = models.CharField(max_length=45, blank=True, null=True)
    date_uploaded = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_tbl_sysshiftsked'


class TmpAdjJournal(models.Model):
    ul_code = models.IntegerField(blank=True, null=True)
    jv_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    remarks = models.CharField(max_length=400, blank=True, null=True)
    active = models.CharField(max_length=2, blank=True, null=True)
    prepared_by = models.CharField(max_length=60, blank=True, null=True)
    reviewed_by = models.CharField(max_length=60, blank=True, null=True)
    approved_by = models.CharField(max_length=60, blank=True, null=True)
    autonum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_adj_journal'


class TmpAllowanceDetails(models.Model):
    terminal = models.CharField(db_column='Terminal', max_length=30, blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    allowance_name = models.CharField(db_column='Allowance_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    taxable = models.CharField(db_column='Taxable', max_length=1, blank=True, null=True)  # Field name made lowercase.
    type_of_details = models.CharField(db_column='Type_Of_Details', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_allowance_details'


class TmpAllowanceReport(models.Model):
    auto_num = models.AutoField(db_column='Auto_num', unique=True)  # Field name made lowercase.
    terminal_no = models.CharField(max_length=20, blank=True, null=True)
    emp_id = models.CharField(max_length=20, blank=True, null=True)
    emp_name = models.CharField(max_length=60, blank=True, null=True)
    allowance_name = models.CharField(max_length=60, blank=True, null=True)
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    allowance_type = models.CharField(max_length=20, blank=True, null=True)
    first_half = models.FloatField(blank=True, null=True)
    second_half = models.FloatField(blank=True, null=True)
    date_range = models.CharField(db_column='Date_range', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_allowance_report'


class TmpAuthorityToDeduct(models.Model):
    terminal_no = models.CharField(max_length=30, blank=True, null=True)
    employee_name = models.CharField(db_column='Employee_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emp_id = models.CharField(db_column='Emp_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_authority_to_deduct'


class TmpDeductionsPayroll(models.Model):
    auto_no = models.FloatField(primary_key=True)
    company_code = models.FloatField(blank=True, null=True)
    branch_code = models.FloatField(db_column='Branch_code', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    dept_id = models.FloatField(db_column='Dept_ID', blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sss = models.FloatField(db_column='SSS', blank=True, null=True)  # Field name made lowercase.
    hdmf = models.FloatField(db_column='HDMF', blank=True, null=True)  # Field name made lowercase.
    phic = models.FloatField(db_column='PHIC', blank=True, null=True)  # Field name made lowercase.
    incometax = models.FloatField(db_column='IncomeTAX', blank=True, null=True)  # Field name made lowercase.
    other_deduction = models.TextField(db_column='Other_deduction', blank=True, null=True)  # Field name made lowercase.
    allowance = models.TextField(db_column='Allowance', blank=True, null=True)  # Field name made lowercase.
    tot_odeductions = models.FloatField(db_column='Tot_Odeductions', blank=True, null=True)  # Field name made lowercase.
    total_deductions = models.FloatField(db_column='Total_deductions', blank=True, null=True)  # Field name made lowercase.
    total_allowance = models.FloatField(db_column='Total_allowance', blank=True, null=True)  # Field name made lowercase.
    sss_er = models.FloatField(db_column='SSS_er', blank=True, null=True)  # Field name made lowercase.
    sss_ec_er = models.FloatField(db_column='SSS_EC_er', blank=True, null=True)  # Field name made lowercase.
    hdmf_er = models.FloatField(db_column='HDMF_er', blank=True, null=True)  # Field name made lowercase.
    phic_er = models.FloatField(db_column='PHIC_er', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_deductions_payroll'


class TmpDtr(models.Model):
    autonum = models.FloatField(primary_key=True)
    date = models.CharField(db_column='Date', max_length=25, blank=True, null=True)  # Field name made lowercase.
    timein1 = models.CharField(db_column='TimeIn1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    timeout1 = models.CharField(db_column='TimeOut1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    timein2 = models.CharField(db_column='TimeIn2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    timeout2 = models.CharField(db_column='TimeOut2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    otin = models.CharField(db_column='OTIn', max_length=15, blank=True, null=True)  # Field name made lowercase.
    otout = models.CharField(db_column='OTOut', max_length=15, blank=True, null=True)  # Field name made lowercase.
    shift = models.CharField(db_column='Shift', max_length=20, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=50, blank=True, null=True)  # Field name made lowercase.
    terminal = models.CharField(db_column='Terminal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    trhrs = models.FloatField(db_column='TrHrs', blank=True, null=True)  # Field name made lowercase.
    tothrs = models.FloatField(db_column='TOTHrs', blank=True, null=True)  # Field name made lowercase.
    timein3 = models.CharField(db_column='TimeIn3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    timeout3 = models.CharField(db_column='TimeOut3', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_dtr'


class TmpEmpdtr(models.Model):
    autonum = models.AutoField(primary_key=True)  # The composite primary key (autonum, terminalNo) found, that is not supported. The first column is selected.
    terminalno = models.IntegerField(db_column='terminalNo')  # Field name made lowercase.
    employee = models.CharField(db_column='Employee', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dates = models.DateField(db_column='Dates', blank=True, null=True)  # Field name made lowercase.
    nohrs = models.FloatField(db_column='NoHrs', blank=True, null=True)  # Field name made lowercase.
    timechargeshours = models.FloatField(db_column='TimeChargesHours', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_empdtr'
        unique_together = (('autonum', 'terminalno'),)


class TmpEmpotherinforef(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', unique=True)  # Field name made lowercase.
    terminal_no = models.CharField(db_column='Terminal_no', max_length=20, blank=True, null=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_ID', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='Fullname', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sss_id = models.CharField(db_column='SSS_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    phic_id = models.CharField(db_column='PHIC_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    hdmf_id = models.CharField(db_column='HDMF_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tin_no = models.CharField(db_column='TIN_no', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_empotherinforef'


class TmpEmppayrollDtr(models.Model):
    company_code = models.IntegerField(blank=True, null=True)
    store_code = models.IntegerField(blank=True, null=True)
    emp_id = models.FloatField(primary_key=True)  # The composite primary key (emp_id, Payroll_period) found, that is not supported. The first column is selected.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=30)  # Field name made lowercase.
    daily_rate = models.FloatField(blank=True, null=True)
    per_hour = models.FloatField(db_column='Per_hour', blank=True, null=True)  # Field name made lowercase.
    reg_hrs = models.FloatField(db_column='Reg_hrs', blank=True, null=True)  # Field name made lowercase.
    ot_hrs = models.FloatField(db_column='OT_hrs', blank=True, null=True)  # Field name made lowercase.
    holiday_hrs = models.FloatField(blank=True, null=True)
    special_hrs = models.FloatField(blank=True, null=True)
    nsd_hrs = models.FloatField(db_column='NSD_hrs', blank=True, null=True)  # Field name made lowercase.
    absent_hrs = models.FloatField(db_column='Absent_hrs', blank=True, null=True)  # Field name made lowercase.
    reg_pay = models.FloatField(db_column='Reg_pay', blank=True, null=True)  # Field name made lowercase.
    ot_pay = models.FloatField(db_column='OT_pay', blank=True, null=True)  # Field name made lowercase.
    holiday_pay = models.FloatField(db_column='Holiday_pay', blank=True, null=True)  # Field name made lowercase.
    special_pay = models.FloatField(db_column='Special_pay', blank=True, null=True)  # Field name made lowercase.
    nsd_pay = models.FloatField(db_column='NSD_pay', blank=True, null=True)  # Field name made lowercase.
    deduct_absent = models.FloatField(db_column='Deduct_absent', blank=True, null=True)  # Field name made lowercase.
    gross_income = models.FloatField(db_column='Gross_income', blank=True, null=True)  # Field name made lowercase.
    salary_type = models.CharField(db_column='Salary_type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    monthly_salary = models.FloatField(db_column='Monthly_salary', blank=True, null=True)  # Field name made lowercase.
    payroll_details = models.CharField(db_column='Payroll_details', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    payroll_summary = models.CharField(db_column='Payroll_summary', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    dep_id = models.FloatField(db_column='Dep_id', blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='Confidential', max_length=5, blank=True, null=True)  # Field name made lowercase.
    other_income = models.FloatField(blank=True, null=True)
    paid_leave_hrs = models.FloatField(db_column='Paid_leave_hrs', blank=True, null=True)  # Field name made lowercase.
    absentlatewopay_hrs = models.FloatField(db_column='AbsentLateWOPay_hrs', blank=True, null=True)  # Field name made lowercase.
    total_regworking_hrs = models.FloatField(db_column='Total_RegWorking_hrs', blank=True, null=True)  # Field name made lowercase.
    ot_hrs_leg_hrs = models.FloatField(db_column='OT_hrs_Leg_hrs', blank=True, null=True)  # Field name made lowercase.
    ot_hrs_spec_hrs = models.FloatField(db_column='Ot_hrs_Spec_hrs', blank=True, null=True)  # Field name made lowercase.
    ot_dayoleg_hrs = models.FloatField(db_column='OT_DayOLeg_hrs', blank=True, null=True)  # Field name made lowercase.
    ot_dayospec_hrs = models.FloatField(db_column='OT_DayOSpec_hrs', blank=True, null=True)  # Field name made lowercase.
    ot_dayoff = models.FloatField(db_column='OT_dayOff', blank=True, null=True)  # Field name made lowercase.
    dayo_leg_hrs = models.FloatField(db_column='DayO_leg_hrs', blank=True, null=True)  # Field name made lowercase.
    dayo_spec_hrs = models.FloatField(db_column='DayO_spec_hrs', blank=True, null=True)  # Field name made lowercase.
    dayo_hrs = models.FloatField(db_column='DayO_hrs', blank=True, null=True)  # Field name made lowercase.
    nsd_leg_hrs = models.FloatField(db_column='NSD_leg_hrs', blank=True, null=True)  # Field name made lowercase.
    nsd_spec_hrs = models.FloatField(db_column='NSD_Spec_hrs', blank=True, null=True)  # Field name made lowercase.
    nsddayo_leg_hrs = models.FloatField(db_column='NSDDayO_leg_hrs', blank=True, null=True)  # Field name made lowercase.
    nsddayo_spec_hrs = models.FloatField(db_column='NSDDayO_spec_hrs', blank=True, null=True)  # Field name made lowercase.
    nsddayoff_hrs = models.FloatField(db_column='NSDDayOff_hrs', blank=True, null=True)  # Field name made lowercase.
    t_cola = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_emppayroll_dtr'
        unique_together = (('emp_id', 'payroll_period'),)


class TmpGlentry(models.Model):
    autonum = models.FloatField(db_column='autoNum', primary_key=True)  # Field name made lowercase.
    sl_name = models.CharField(db_column='SL_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id_code = models.CharField(max_length=20, blank=True, null=True)
    accnt_title = models.CharField(db_column='Accnt_title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    debit_amnt = models.FloatField(db_column='Debit_amnt', blank=True, null=True)  # Field name made lowercase.
    cerit_amnt = models.FloatField(db_column='Cerit_amnt', blank=True, null=True)  # Field name made lowercase.
    terminalno = models.CharField(db_column='TerminalNo', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_glentry'


class TmpIncomeStatement(models.Model):
    auto_num = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=999, blank=True, null=True)
    account_code = models.CharField(db_column='Account_Code', max_length=999, blank=True, null=True)  # Field name made lowercase.
    accounttitle = models.CharField(db_column='AccountTitle', max_length=999, blank=True, null=True)  # Field name made lowercase.
    number_1stmonth = models.FloatField(db_column='1stMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndmonth = models.FloatField(db_column='2ndMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rdmonth = models.FloatField(db_column='3rdMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_4thmonth = models.FloatField(db_column='4thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5thmonth = models.FloatField(db_column='5thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_6thmonth = models.FloatField(db_column='6thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_7thmonth = models.FloatField(db_column='7thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_8thmonth = models.FloatField(db_column='8thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_9thmonth = models.FloatField(db_column='9thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_10thmonth = models.FloatField(db_column='10thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_11thmonth = models.FloatField(db_column='11thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_12thmonth = models.FloatField(db_column='12thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndyear1stmonth = models.FloatField(db_column='2ndYear1stMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndyear2ndmonth = models.FloatField(db_column='2ndYear2ndMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndyear3rdmonth = models.FloatField(db_column='2ndYear3rdMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndyear4thmonth = models.FloatField(db_column='2ndYear4thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndyear5thmonth = models.FloatField(db_column='2ndYear5thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndyear6thmonth = models.FloatField(db_column='2ndYear6thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndyear7thmonth = models.FloatField(db_column='2ndYear7thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndyear8thmonth = models.FloatField(db_column='2ndYear8thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndyear9thmonth = models.FloatField(db_column='2ndYear9thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndyear10thmonth = models.FloatField(db_column='2ndYear10thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndyear11thmonth = models.FloatField(db_column='2ndYear11thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndyear12thmonth = models.FloatField(db_column='2ndYear12thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rdyear1stmonth = models.FloatField(db_column='3rdYear1stMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rdyear2ndmonth = models.FloatField(db_column='3rdYear2ndMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rdyear3rdmonth = models.FloatField(db_column='3rdYear3rdMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rdyear4thmonth = models.FloatField(db_column='3rdYear4thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rdyear5thmonth = models.FloatField(db_column='3rdYear5thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rdyear6thmonth = models.FloatField(db_column='3rdYear6thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rdyear7thmonth = models.FloatField(db_column='3rdYear7thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rdyear8thmonth = models.FloatField(db_column='3rdYear8thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rdyear9thmonth = models.FloatField(db_column='3rdYear9thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rdyear10thmonth = models.FloatField(db_column='3rdYear10thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rdyear11thmonth = models.FloatField(db_column='3rdYear11thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rdyear12thmonth = models.FloatField(db_column='3rdYear12thMonth', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    fouryear1stmonth = models.FloatField(db_column='fourYear1stMonth', blank=True, null=True)  # Field name made lowercase.
    fouryear2ndmonth = models.FloatField(db_column='fourYear2ndMonth', blank=True, null=True)  # Field name made lowercase.
    fouryear3rdmonth = models.FloatField(db_column='fourYear3rdMonth', blank=True, null=True)  # Field name made lowercase.
    fouryear4thmonth = models.FloatField(db_column='fourYear4thMonth', blank=True, null=True)  # Field name made lowercase.
    fouryear5thmonth = models.FloatField(db_column='fourYear5thMonth', blank=True, null=True)  # Field name made lowercase.
    fouryear6thmonth = models.FloatField(db_column='fourYear6thMonth', blank=True, null=True)  # Field name made lowercase.
    fouryear7thmonth = models.FloatField(db_column='fourYear7thMonth', blank=True, null=True)  # Field name made lowercase.
    fouryear8thmonth = models.FloatField(db_column='fourYear8thMonth', blank=True, null=True)  # Field name made lowercase.
    fouryear9thmonth = models.FloatField(db_column='fourYear9thMonth', blank=True, null=True)  # Field name made lowercase.
    fouryear10thmonth = models.FloatField(db_column='fourYear10thMonth', blank=True, null=True)  # Field name made lowercase.
    fouryear11thmonth = models.FloatField(db_column='fourYear11thMonth', blank=True, null=True)  # Field name made lowercase.
    fouryear12thmonth = models.FloatField(db_column='fourYear12thMonth', blank=True, null=True)  # Field name made lowercase.
    number_1styear = models.FloatField(db_column='1stYear', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ndyear = models.FloatField(db_column='2ndYear', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3rdyear = models.FloatField(db_column='3rdYear', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_4rthyear = models.FloatField(db_column='4rthYear', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    terminalno = models.CharField(db_column='TerminalNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_income_statement'


class TmpJournalEntry(models.Model):
    auto_num = models.AutoField(unique=True)
    default_category = models.CharField(max_length=100, blank=True, null=True)
    particular = models.CharField(db_column='Particular', max_length=50, blank=True, null=True)  # Field name made lowercase.
    account_code = models.CharField(db_column='Account_code', max_length=30, blank=True, null=True)  # Field name made lowercase.
    account_title = models.CharField(db_column='Account_title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sl_type = models.CharField(db_column='SL_type', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sl_name = models.CharField(db_column='SL_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    debit = models.FloatField(db_column='Debit', blank=True, null=True)  # Field name made lowercase.
    credit = models.FloatField(db_column='Credit', blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_journal_entry'


class TmpModuleAccess(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    mod_access_table = models.CharField(max_length=10, blank=True, null=True)
    mod_access_desc = models.CharField(max_length=50, blank=True, null=True)
    mod_access_status = models.CharField(max_length=1, blank=True, null=True)
    mod_access_used = models.CharField(max_length=1, blank=True, null=True)
    mod_access_user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_module_access'


class TmpOtherdedreport(models.Model):
    auto_num = models.AutoField(db_column='Auto_num', unique=True)  # Field name made lowercase.
    terminal_no = models.CharField(max_length=20, blank=True, null=True)
    emp_id = models.CharField(max_length=20, blank=True, null=True)
    emp_name = models.CharField(max_length=60, blank=True, null=True)
    deduction_name = models.CharField(db_column='Deduction_name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    deduction_type = models.CharField(db_column='Deduction_type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    first_half = models.FloatField(blank=True, null=True)
    second_half = models.FloatField(blank=True, null=True)
    date_range = models.CharField(db_column='Date_range', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_otherdedreport'


class TmpPayrollDetailsPrint(models.Model):
    auto_num = models.AutoField(db_column='Auto_num', primary_key=True)  # Field name made lowercase.
    terminal = models.CharField(db_column='Terminal', max_length=30, blank=True, null=True)  # Field name made lowercase.
    company_code = models.IntegerField(db_column='Company_code', blank=True, null=True)  # Field name made lowercase.
    store_code = models.IntegerField(db_column='Store_code', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, blank=True, null=True)  # Field name made lowercase.
    hourss = models.FloatField(db_column='Hourss', blank=True, null=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_payroll_details_print'


class TmpPayrollGen(models.Model):
    company_code = models.IntegerField(primary_key=True)  # The composite primary key (company_code, store_code, Emp_id, Payroll_period) found, that is not supported. The first column is selected.
    store_code = models.IntegerField()
    emp_id = models.FloatField(db_column='Emp_id')  # Field name made lowercase.
    emp_name = models.CharField(db_column='Emp_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emp_tax_status = models.CharField(db_column='Emp_Tax_status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    emp_basic_pay = models.FloatField(db_column='Emp_Basic_Pay', blank=True, null=True)  # Field name made lowercase.
    emp_additional_paywtax = models.FloatField(db_column='Emp_Additional_PaywTax', blank=True, null=True)  # Field name made lowercase.
    emp_nontax_allowance = models.FloatField(db_column='Emp_NonTax_allowance', blank=True, null=True)  # Field name made lowercase.
    sss_cont = models.FloatField(db_column='SSS_cont', blank=True, null=True)  # Field name made lowercase.
    phic_cont = models.FloatField(db_column='PHIC_cont', blank=True, null=True)  # Field name made lowercase.
    hdmf_cont = models.FloatField(db_column='HDMF_cont', blank=True, null=True)  # Field name made lowercase.
    salary_type = models.CharField(db_column='Salary_type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tax_deduction = models.FloatField(db_column='Tax_deduction', blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=30)  # Field name made lowercase.
    company_deductions = models.FloatField(db_column='Company_deductions', blank=True, null=True)  # Field name made lowercase.
    loans_benefits = models.FloatField(db_column='Loans_benefits', blank=True, null=True)  # Field name made lowercase.
    gross_income = models.FloatField(db_column='Gross_income', blank=True, null=True)  # Field name made lowercase.
    net_income = models.FloatField(db_column='Net_income', blank=True, null=True)  # Field name made lowercase.
    dept_id = models.FloatField(db_column='Dept_id', blank=True, null=True)  # Field name made lowercase.
    no_count = models.FloatField(db_column='No_count', blank=True, null=True)  # Field name made lowercase.
    payroll_details = models.CharField(db_column='Payroll_details', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    payroll_summary = models.CharField(db_column='Payroll_summary', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    absent_late = models.FloatField(db_column='Absent_late', blank=True, null=True)  # Field name made lowercase.
    confidential = models.CharField(db_column='ConfiDential', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sss_er = models.FloatField(db_column='SSS_er', blank=True, null=True)  # Field name made lowercase.
    phic_er = models.FloatField(db_column='PHIC_er', blank=True, null=True)  # Field name made lowercase.
    hdmf_er = models.FloatField(db_column='HDMF_er', blank=True, null=True)  # Field name made lowercase.
    taxable_allowance = models.FloatField(blank=True, null=True)
    non_taxable_deduction = models.FloatField(db_column='Non_taxable_deduction', blank=True, null=True)  # Field name made lowercase.
    other_income = models.FloatField(db_column='Other_Income', blank=True, null=True)  # Field name made lowercase.
    sss_ec_er = models.FloatField(db_column='sss_eC_er', blank=True, null=True)  # Field name made lowercase.
    cv_no = models.CharField(db_column='CV_no', max_length=30, blank=True, null=True)  # Field name made lowercase.
    terminal_no = models.CharField(db_column='Terminal_no', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_payroll_gen'
        unique_together = (('company_code', 'store_code', 'emp_id', 'payroll_period'),)


class TmpPayrollJournal2(models.Model):
    terminal_no = models.IntegerField(db_column='Terminal_no', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_ID', blank=True, null=True)  # Field name made lowercase.
    employee_name = models.CharField(db_column='Employee_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    no_of_days = models.FloatField(db_column='No_of_days', blank=True, null=True)  # Field name made lowercase.
    basic_salary = models.FloatField(db_column='Basic_Salary', blank=True, null=True)  # Field name made lowercase.
    allowances_adj = models.FloatField(db_column='Allowances_Adj', blank=True, null=True)  # Field name made lowercase.
    total_wage = models.FloatField(db_column='Total_wage', blank=True, null=True)  # Field name made lowercase.
    late_absent = models.FloatField(db_column='Late_absent', blank=True, null=True)  # Field name made lowercase.
    gross_pay = models.FloatField(db_column='Gross_pay', blank=True, null=True)  # Field name made lowercase.
    sss = models.FloatField(db_column='SSS', blank=True, null=True)  # Field name made lowercase.
    phic = models.FloatField(db_column='PHIC', blank=True, null=True)  # Field name made lowercase.
    hdmf = models.FloatField(db_column='HDMF', blank=True, null=True)  # Field name made lowercase.
    wtax = models.FloatField(db_column='WTax', blank=True, null=True)  # Field name made lowercase.
    deduction1 = models.FloatField(db_column='Deduction1', blank=True, null=True)  # Field name made lowercase.
    deduction2 = models.FloatField(db_column='Deduction2', blank=True, null=True)  # Field name made lowercase.
    dedection3 = models.FloatField(db_column='Dedection3', blank=True, null=True)  # Field name made lowercase.
    deduction4 = models.FloatField(db_column='Deduction4', blank=True, null=True)  # Field name made lowercase.
    deduction5 = models.FloatField(db_column='Deduction5', blank=True, null=True)  # Field name made lowercase.
    other_deduction = models.FloatField(db_column='Other_deduction', blank=True, null=True)  # Field name made lowercase.
    net_pay = models.FloatField(db_column='Net_pay', blank=True, null=True)  # Field name made lowercase.
    payroll_period = models.CharField(db_column='Payroll_period', max_length=30, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_payroll_journal_2'


class TmpPsModuleAccess(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    mod_access_table = models.CharField(max_length=50, blank=True, null=True)
    mod_access_table_child = models.CharField(max_length=50, blank=True, null=True)
    mod_access_table_child_child = models.CharField(max_length=50, blank=True, null=True)
    mod_access_table_child_child_child = models.CharField(max_length=50, blank=True, null=True)
    mod_access_table_child_child_child_child = models.CharField(max_length=50, blank=True, null=True)
    mod_access_status = models.CharField(max_length=1, blank=True, null=True)
    mod_access_used = models.CharField(max_length=1, blank=True, null=True)
    mod_access_user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_ps_module_access'


class TmpReportAnnualTax(models.Model):
    auto_num = models.AutoField(db_column='Auto_num', primary_key=True)  # Field name made lowercase.
    emp_id = models.CharField(db_column='Emp_id', max_length=250, blank=True, null=True)  # Field name made lowercase.
    emp_name = models.CharField(db_column='Emp_name', max_length=250, blank=True, null=True)  # Field name made lowercase.
    actual_taxable_income = models.FloatField(db_column='Actual_taxable_income', blank=True, null=True)  # Field name made lowercase.
    actual_tax_withheld = models.FloatField(db_column='Actual_tax_withheld', blank=True, null=True)  # Field name made lowercase.
    annual_taxable_income = models.FloatField(db_column='Annual_taxable_income', blank=True, null=True)  # Field name made lowercase.
    annual_tax_withheld = models.FloatField(db_column='Annual_tax_withheld', blank=True, null=True)  # Field name made lowercase.
    tax_difference = models.FloatField(db_column='Tax_difference', blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_report_annual_tax'


class TmpSaveNetIncome(models.Model):
    autonum = models.AutoField(primary_key=True)
    category = models.CharField(max_length=999, blank=True, null=True)
    account_title = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_save_net_income'


class TmpSorting(models.Model):
    auto_no = models.AutoField(db_column='Auto_no', primary_key=True)  # Field name made lowercase.
    emp_id = models.FloatField(db_column='Emp_id', blank=True, null=True)  # Field name made lowercase.
    net_pay = models.FloatField(db_column='Net_pay', blank=True, null=True)  # Field name made lowercase.
    terminal_no = models.CharField(db_column='Terminal_no', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_sorting'


class TmpSyncdata(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveIntegerField(blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    doc_no = models.FloatField(blank=True, null=True)
    reference_no = models.CharField(max_length=50, blank=True, null=True)
    ref_doc_type = models.CharField(max_length=10, blank=True, null=True)
    ref_doc_no = models.FloatField(blank=True, null=True)
    ref_autonum = models.CharField(max_length=50, blank=True, null=True)
    parent_autonum_ref = models.CharField(max_length=50, blank=True, null=True)
    module = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_syncdata'


class TmpTableReservoirCost(models.Model):
    autonum = models.AutoField(primary_key=True)
    category = models.CharField(max_length=999, blank=True, null=True)
    account_title = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_table_reservoir_cost'


class TmpTableReservoirOperating(models.Model):
    autonum = models.AutoField(primary_key=True)
    category = models.CharField(max_length=999, blank=True, null=True)
    account_title = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_table_reservoir_operating'


class TmpTableReservoirRevenue(models.Model):
    autonum = models.AutoField(primary_key=True)
    category = models.CharField(max_length=999, blank=True, null=True)
    account_title = models.CharField(max_length=999, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_table_reservoir_revenue'


class TmpTimechargess(models.Model):
    autonum = models.AutoField(db_column='AutoNUm', primary_key=True)  # Field name made lowercase.
    terminalno = models.FloatField(db_column='terminalNo', blank=True, null=True)  # Field name made lowercase.
    usern = models.CharField(db_column='userN', max_length=999, blank=True, null=True)  # Field name made lowercase.
    chargeto = models.CharField(db_column='ChargeTo', max_length=999, blank=True, null=True)  # Field name made lowercase.
    departnmet = models.CharField(db_column='Departnmet', max_length=999, blank=True, null=True)  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=999, blank=True, null=True)  # Field name made lowercase.
    categ_desc = models.CharField(max_length=40, blank=True, null=True)
    d1 = models.FloatField(blank=True, null=True)
    d2 = models.FloatField(blank=True, null=True)
    d3 = models.FloatField(blank=True, null=True)
    d4 = models.FloatField(blank=True, null=True)
    d5 = models.FloatField(blank=True, null=True)
    d6 = models.FloatField(blank=True, null=True)
    d7 = models.FloatField(blank=True, null=True)
    d8 = models.FloatField(blank=True, null=True)
    d9 = models.FloatField(blank=True, null=True)
    d10 = models.FloatField(blank=True, null=True)
    d11 = models.FloatField(blank=True, null=True)
    d12 = models.FloatField(blank=True, null=True)
    d13 = models.FloatField(blank=True, null=True)
    d14 = models.FloatField(blank=True, null=True)
    d15 = models.FloatField(blank=True, null=True)
    d16 = models.FloatField(blank=True, null=True)
    dateprinted = models.DateField(db_column='DatePrinted', blank=True, null=True)  # Field name made lowercase.
    date1 = models.IntegerField(blank=True, null=True)
    date2 = models.IntegerField(blank=True, null=True)
    day1 = models.CharField(max_length=10, blank=True, null=True)
    stndrdhrs = models.FloatField(db_column='StndrdHrs', blank=True, null=True)  # Field name made lowercase.
    nodays = models.FloatField(blank=True, null=True)
    restday = models.CharField(db_column='restDay', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rtotal = models.FloatField(blank=True, null=True)
    empid = models.IntegerField(db_column='empID', blank=True, null=True)  # Field name made lowercase.
    cat_sub1_desc = models.CharField(max_length=100, blank=True, null=True)
    cat_sub2_desc = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_timechargess'


class TmpTransactionListingGj(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(blank=True, null=True)
    jv_no = models.FloatField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    id_code = models.PositiveIntegerField(blank=True, null=True)
    sl_acct = models.CharField(max_length=150, blank=True, null=True)
    guarantor = models.CharField(max_length=150, blank=True, null=True)
    primary_code = models.PositiveIntegerField(blank=True, null=True)
    secondary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_code = models.PositiveIntegerField(blank=True, null=True)
    subsidiary_code = models.PositiveIntegerField(blank=True, null=True)
    acct_title = models.CharField(max_length=150, blank=True, null=True)
    debit_amount = models.FloatField(blank=True, null=True)
    credit_amount = models.FloatField(blank=True, null=True)
    active = models.CharField(max_length=2, blank=True, null=True)
    posted_by = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.DateField(blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tmp_transaction_listing_gj'


class TmpTransactionhistory(models.Model):
    auto_num = models.BigAutoField(primary_key=True)
    terminalno = models.FloatField(db_column='terminalNo', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.IntegerField(db_column='Emp_ID', blank=True, null=True)  # Field name made lowercase.
    usern = models.CharField(db_column='userN', max_length=999, blank=True, null=True)  # Field name made lowercase.
    chargeto = models.CharField(db_column='chargeTo', max_length=999, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(max_length=999, blank=True, null=True)
    dateprinted = models.DateField(db_column='DatePrinted', blank=True, null=True)  # Field name made lowercase.
    rtotal = models.FloatField(db_column='rTotal', blank=True, null=True)  # Field name made lowercase.
    categ_desc = models.CharField(db_column='Categ_desc', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cat_sub1_desc = models.CharField(max_length=100, blank=True, null=True)
    cat_sub2_desc = models.CharField(max_length=100, blank=True, null=True)
    emp_name = models.CharField(db_column='Emp_Name', max_length=60, blank=True, null=True)  # Field name made lowercase.
    percentage = models.FloatField(blank=True, null=True)
    totalhoursperchargeto = models.FloatField(db_column='totalHoursPerChargeTo', blank=True, null=True)  # Field name made lowercase.
    percentageperclient = models.FloatField(db_column='percentagePerClient', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_transactionhistory'


class TmpTransactionhistory1(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    terminalno = models.FloatField(db_column='terminalNo', blank=True, null=True)  # Field name made lowercase.
    emp_id = models.IntegerField(db_column='Emp_ID', blank=True, null=True)  # Field name made lowercase.
    usern = models.CharField(db_column='userN', max_length=999, blank=True, null=True)  # Field name made lowercase.
    dateprinted = models.DateField(db_column='DatePrinted', blank=True, null=True)  # Field name made lowercase.
    firm = models.FloatField(db_column='Firm', blank=True, null=True)  # Field name made lowercase.
    client = models.FloatField(db_column='Client', blank=True, null=True)  # Field name made lowercase.
    others = models.FloatField(db_column='Others', blank=True, null=True)  # Field name made lowercase.
    fpercentage = models.FloatField(db_column='FPercentage', blank=True, null=True)  # Field name made lowercase.
    cpercentage = models.FloatField(db_column='CPercentage', blank=True, null=True)  # Field name made lowercase.
    opercentage = models.FloatField(db_column='OPercentage', blank=True, null=True)  # Field name made lowercase.
    total_percentage = models.FloatField(db_column='Total_Percentage', blank=True, null=True)  # Field name made lowercase.
    emp_name = models.CharField(db_column='Emp_Name', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmp_transactionhistory1'


class ZBillPrintoutRef(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    customer_code = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=250, blank=True, null=True)
    bill_reference = models.CharField(max_length=200, blank=True, null=True)
    bill_date = models.DateField(blank=True, null=True)
    bill_printout = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'z_bill_printout_ref'


class ZLoginFirst(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    fieldname = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'z_login_first'


class ZModuleAccess(models.Model):
    trans_mod = models.CharField(max_length=100, blank=True, null=True)
    maintenance_mod = models.CharField(max_length=100, blank=True, null=True)
    admin_mod = models.CharField(max_length=100, blank=True, null=True)
    report_mod = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'z_module_access'


class ZSettingsExport(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    font_name = models.CharField(max_length=50, blank=True, null=True)
    font_style = models.CharField(max_length=50, blank=True, null=True)
    font_size = models.IntegerField(blank=True, null=True)
    with_cname = models.CharField(db_column='with_cName', max_length=1, blank=True, null=True)  # Field name made lowercase.
    with_caddress = models.CharField(db_column='with_CAddress', max_length=1, blank=True, null=True)  # Field name made lowercase.
    with_clogo = models.CharField(db_column='with_CLogo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    header_color = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'z_settings_export'


class ZShortcutkey(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    module_name = models.CharField(max_length=100, blank=True, null=True)
    key_control = models.CharField(max_length=1, blank=True, null=True)
    key_shift = models.CharField(max_length=1, blank=True, null=True)
    key_alt = models.CharField(max_length=1, blank=True, null=True)
    key_character = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'z_shortcutkey'


class ZSlReports(models.Model):
    autonum = models.AutoField(primary_key=True)
    terminal_no = models.IntegerField(blank=True, null=True)
    ul_code = models.SmallIntegerField(blank=True, null=True)
    id_code = models.IntegerField(blank=True, null=True)
    sl_acct = models.CharField(max_length=40, blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    reference_no = models.CharField(max_length=25, blank=True, null=True)
    particulars = models.CharField(max_length=40, blank=True, null=True)
    sales = models.FloatField(blank=True, null=True)
    adjustment1 = models.FloatField(blank=True, null=True)
    collection = models.FloatField(blank=True, null=True)
    disc_return = models.FloatField(blank=True, null=True)
    adjustment2 = models.FloatField(blank=True, null=True)
    balances = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'z_sl_reports'
        unique_together = (('autonum', 'id_code', 'sl_acct', 'date_trans', 'reference_no', 'particulars', 'adjustment2'),)


class ZSlnameReports(models.Model):
    autonum = models.AutoField(primary_key=True)
    terminal_no = models.IntegerField(blank=True, null=True)
    id_code = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    contact_no = models.CharField(max_length=40, blank=True, null=True)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    bir_no = models.CharField(max_length=30, blank=True, null=True)
    tax_no = models.CharField(max_length=30, blank=True, null=True)
    credit_limit = models.FloatField(blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    date_hired = models.CharField(max_length=10, db_collation='latin1_bin', blank=True, null=True)
    date_separated = models.CharField(max_length=10, db_collation='latin1_bin', blank=True, null=True)
    sss_no = models.CharField(max_length=50, blank=True, null=True)
    phic_no = models.CharField(max_length=50, blank=True, null=True)
    hdmf_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'z_slname_reports'


class ZSystemCustomFields(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    module_name = models.CharField(max_length=100, blank=True, null=True)
    field_name = models.CharField(db_column='Field_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'z_system_custom_fields'


class ZSystemSettings(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    reports_name = models.CharField(max_length=100, blank=True, null=True)
    view_reports = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'z_system_settings'


class ZTblAgingList(models.Model):
    autonum = models.BigAutoField(primary_key=True)  # The composite primary key (autonum, ul_code, cutoff_date, date_trans) found, that is not supported. The first column is selected.
    ul_code = models.IntegerField()
    cutoff_date = models.DateField()
    date_trans = models.DateField()
    time_trans = models.TimeField(blank=True, null=True)
    acct_title = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'z_tbl_aging_list'
        unique_together = (('autonum', 'ul_code', 'cutoff_date', 'date_trans'),)


class ZTblAgingListing(models.Model):
    autonum = models.BigAutoField(primary_key=True)  # The composite primary key (autonum, ul_code, cutoff_date, date_trans) found, that is not supported. The first column is selected.
    ul_code = models.IntegerField()
    cutoff_date = models.DateField()
    date_trans = models.DateField()
    time_trans = models.TimeField(blank=True, null=True)
    acct_title = models.CharField(max_length=500, blank=True, null=True)
    sl_code = models.IntegerField(blank=True, null=True)
    sl_name = models.CharField(max_length=250, blank=True, null=True)
    total_ob = models.FloatField(blank=True, null=True)
    current = models.FloatField(blank=True, null=True)
    one_to_thirty = models.FloatField(blank=True, null=True)
    thirtyone_to_sixty = models.FloatField(blank=True, null=True)
    sixtyone_to_ninety = models.FloatField(blank=True, null=True)
    ninetyone_to_onetwenty = models.FloatField(blank=True, null=True)
    onetwenty_up = models.FloatField(blank=True, null=True)
    sl_type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'z_tbl_aging_listing'
        unique_together = (('autonum', 'ul_code', 'cutoff_date', 'date_trans'),)


class ZTblAutofixLogs(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    tmp1 = models.CharField(max_length=150, blank=True, null=True)
    tmp2 = models.CharField(max_length=150, blank=True, null=True)
    tmp3 = models.CharField(max_length=150, blank=True, null=True)
    tmp4 = models.CharField(max_length=150, blank=True, null=True)
    tmp5 = models.CharField(max_length=150, blank=True, null=True)
    tmp6 = models.CharField(max_length=150, blank=True, null=True)
    tmp7 = models.CharField(max_length=150, blank=True, null=True)
    tmp8 = models.CharField(max_length=150, blank=True, null=True)
    tmp9 = models.CharField(max_length=150, blank=True, null=True)
    tmp10 = models.CharField(max_length=150, blank=True, null=True)
    tmp11 = models.CharField(max_length=150, blank=True, null=True)
    tmp12 = models.CharField(max_length=150, blank=True, null=True)
    tmp13 = models.CharField(max_length=150, blank=True, null=True)
    tmp14 = models.CharField(max_length=150, blank=True, null=True)
    tmp15 = models.CharField(max_length=150, blank=True, null=True)
    tmp16 = models.CharField(max_length=150, blank=True, null=True)
    tmp17 = models.CharField(max_length=150, blank=True, null=True)
    tmp18 = models.CharField(max_length=150, blank=True, null=True)
    tmp19 = models.CharField(max_length=150, blank=True, null=True)
    tmp20 = models.CharField(max_length=150, blank=True, null=True)
    tmp21 = models.CharField(max_length=150, blank=True, null=True)
    tmp22 = models.CharField(max_length=150, blank=True, null=True)
    tmp23 = models.CharField(max_length=150, blank=True, null=True)
    tmp24 = models.CharField(max_length=150, blank=True, null=True)
    tmp25 = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'z_tbl_autofix_logs'


class ZTblProductStockLedger(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    datetime = models.DateTimeField(db_column='DateTime', blank=True, null=True)  # Field name made lowercase.
    ul_code = models.IntegerField(blank=True, null=True)
    site_code = models.IntegerField(blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    trans_type = models.CharField(max_length=100, blank=True, null=True)
    doc_type = models.CharField(max_length=10, blank=True, null=True)
    reference_no = models.FloatField(blank=True, null=True)
    bar_code = models.CharField(max_length=20, blank=True, null=True)
    alternate_code = models.CharField(max_length=20, blank=True, null=True)
    item_code = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    total_qty = models.FloatField(blank=True, null=True)
    moving_ave = models.FloatField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    running_qty = models.FloatField(blank=True, null=True)
    running_amt = models.FloatField(blank=True, null=True)
    sn_bc = models.CharField(max_length=10, blank=True, null=True)
    old_auto_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'z_tbl_product_stock_ledger'


class ZTempDetailedReport(models.Model):
    auto_no = models.AutoField(primary_key=True)
    number_32_col_indicator = models.CharField(db_column='32_col_indicator', max_length=45, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    day_1 = models.CharField(max_length=45, blank=True, null=True)
    day_2 = models.CharField(max_length=45, blank=True, null=True)
    day_3 = models.CharField(max_length=45, blank=True, null=True)
    day_4 = models.CharField(max_length=45, blank=True, null=True)
    day_5 = models.CharField(max_length=45, blank=True, null=True)
    day_6 = models.CharField(max_length=45, blank=True, null=True)
    day_7 = models.CharField(max_length=45, blank=True, null=True)
    day_8 = models.CharField(max_length=45, blank=True, null=True)
    day_9 = models.CharField(max_length=45, blank=True, null=True)
    day_10 = models.CharField(max_length=45, blank=True, null=True)
    day_11 = models.CharField(max_length=45, blank=True, null=True)
    day_12 = models.CharField(max_length=45, blank=True, null=True)
    day_13 = models.CharField(max_length=45, blank=True, null=True)
    day_14 = models.CharField(max_length=45, blank=True, null=True)
    day_15 = models.CharField(max_length=45, blank=True, null=True)
    day_16 = models.CharField(max_length=45, blank=True, null=True)
    total_hours = models.CharField(max_length=45, blank=True, null=True)
    premiunm_factors = models.CharField(max_length=45, blank=True, null=True)
    rate_per_hour = models.CharField(max_length=45, blank=True, null=True)
    total_amount = models.CharField(max_length=45, blank=True, null=True)
    total_amount2 = models.CharField(max_length=45, blank=True, null=True)
    tardy = models.CharField(max_length=45, blank=True, null=True)
    absent = models.CharField(max_length=45, blank=True, null=True)
    undertime = models.CharField(max_length=45, blank=True, null=True)
    cola = models.CharField(max_length=45, blank=True, null=True)
    gross_pay = models.CharField(max_length=100, blank=True, null=True)
    emp_code = models.CharField(max_length=45, blank=True, null=True)
    full_name = models.CharField(max_length=45, blank=True, null=True)
    payroll_period = models.CharField(max_length=45, blank=True, null=True)
    field22 = models.CharField(max_length=45, blank=True, null=True)
    field23 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'z_temp_detailed_report'

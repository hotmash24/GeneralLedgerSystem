from django.db import models

class OtherAccount(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.SmallIntegerField(default=0)
    sl_name = models.CharField(max_length=150, default=' ')
    trade_name = models.CharField(max_length=100, default=' ')
    abbr = models.CharField(max_length=10, default=' ')
    last_name = models.CharField(max_length=30, default=' ')
    first_name = models.CharField(max_length=30, default=' ')
    middle_name = models.CharField(max_length=30, default=' ')
    code = models.CharField(max_length=75, default='')
    acct_title = models.CharField(max_length=100, default=' ')
    balance = models.DecimalField(max_digits=15, decimal_places=3, default=0.000)
    date_as_of = models.DateField(default='0000-00-00')
    calculation = models.SmallIntegerField(default=0)
    ul_code = models.IntegerField(default=0)
    alter_code = models.CharField(max_length=50, default=' ')
    active = models.CharField(max_length=1, default='Y')

    class Meta:
        db_table = 'tbl_other_acct'

class Employee(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.IntegerField(default=0)
    Emp_ID = models.IntegerField(default=0)
    last_name = models.CharField(max_length=55, default=' ')
    first_name = models.CharField(max_length=55, default=' ')
    middle_name = models.CharField(max_length=55, default=' ')
    department = models.CharField(max_length=50, default=' ')
    designation = models.CharField(max_length=75, default=' ')
    home_phone_no = models.CharField(max_length=15, default=' ')
    mobile_no = models.CharField(max_length=25, default=' ')
    fax_no = models.CharField(max_length=15, default=' ')
    st_address = models.CharField(max_length=60, default=' ')
    city_address = models.CharField(max_length=30, default=' ')
    zip_code = models.IntegerField(default=0)
    date_of_birth = models.DateField(default='0000-00-00')
    place_of_birth = models.CharField(max_length=100, default='0.000')
    balance = models.DecimalField(max_digits=15, decimal_places=3, default=0.000)
    date_as_of = models.DateField(default='0000-00-00')
    remarks = models.CharField(max_length=100, default=' ')
    active = models.CharField(max_length=5, default='Y')
    employee_image = models.BinaryField(blank=True, null=True)
    date_entered = models.DateField(default='0000-00-00')
    ul_code = models.IntegerField(default=0)
    Manual_YN = models.CharField(max_length=1, default='')
    schedule = models.IntegerField(default=0)
    Civil_stat = models.CharField(max_length=15, default='Single')
    Confidential = models.CharField(max_length=5, default='N')
    Finger_ID = models.CharField(max_length=20, default=' ')
    Auto_FillDTR = models.CharField(max_length=5, default=' ')
    Basic_Comp = models.CharField(max_length=1, default='Y')
    PerJob_Comp = models.CharField(max_length=1, default='N')
    Acct_no = models.CharField(max_length=20, default=' ')
    Paid_Lunch = models.CharField(max_length=5, default='N')
    SSS_chk = models.CharField(max_length=5, default='Y')
    PHIC_chk = models.CharField(max_length=5, default='Y')
    HDMF_chk = models.CharField(max_length=5, default='Y')
    Tax_chk = models.CharField(max_length=5, default='Y')
    Release_type = models.CharField(max_length=10, default='CASH')
    FlexiBreak = models.CharField(max_length=5, default='N')
    Gender = models.CharField(max_length=1, default='')
    responsibility_center_code = models.CharField(max_length=11, default='')
    responsibility_center = models.CharField(max_length=250, default='')
    desc_department = models.CharField(max_length=999, default='')
    tax_exemption = models.CharField(max_length=50, default='')
    cola = models.CharField(max_length=1, default='N')
    cola_taxable = models.CharField(max_length=1, default='N')
    cola_based_on_dtr = models.CharField(max_length=1, default='N')
    cola_amount = models.CharField(max_length=999, default='0')
    fixed_schedule = models.CharField(max_length=2, default='N')
    emp_status = models.CharField(max_length=50, default='')
    date_fired = models.CharField(max_length=50, default='')
    bir_schedule = models.CharField(max_length=10, default='0')
    dtr_rotation_id = models.CharField(max_length=20, default='0')
    am_only = models.CharField(max_length=2, default='Y')
    pm_only = models.CharField(max_length=2, default='Y')
    salary_type = models.CharField(max_length=25, default='')
    RestDay = models.CharField(max_length=20, null=True)
    FlexiTime = models.CharField(max_length=20, null=True)
    FlexifirstIN = models.CharField(max_length=20, null=True)
    FlexifirstOUT = models.CharField(max_length=20, null=True)
    FlexisecondIN = models.CharField(max_length=20, null=True)
    FlexisecondOUT = models.CharField(max_length=20, null=True)
    FlexithirdIN = models.CharField(max_length=20, null=True)
    FlexithirdOUT = models.CharField(max_length=20, null=True)
    sl_category = models.CharField(max_length=50, default='')
    EDTR = models.CharField(max_length=30, default='')
    DTAR = models.CharField(max_length=1, default='N')
    MDTR = models.CharField(max_length=30, default='')
    MDTR_TYPE = models.CharField(max_length=30, default='')
    UnworkedHolidayPay = models.CharField(max_length=2, default='N')
    UnworkedHolidayRestDayPay = models.CharField(max_length=2, default='N')
    Locale = models.CharField(max_length=50, default='')
    NoGrossPay = models.CharField(max_length=2, default='N')
    NoHolidayPay = models.CharField(max_length=2, default='N')
    NoOTPay = models.CharField(max_length=2, default='N')
    OTwOPay = models.CharField(max_length=4, default='N')
    min_take_home_pay = models.DecimalField(max_digits=15, decimal_places=3, default=0.000)
    include_payroll = models.CharField(max_length=1, default='Y')

    class Meta:
        db_table = 'tbl_employee'

class Customer(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.DecimalField(max_digits=15, decimal_places=0, default=0)
    trade_name = models.CharField(max_length=150, default=' ')
    customer_class = models.CharField(max_length=15, default=' ')
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=20)
    business_phone_no = models.CharField(max_length=15, default=' ')
    business_style = models.CharField(max_length=150, default='')
    mobile_no = models.CharField(max_length=15, default=' ')
    fax_no = models.CharField(max_length=15, default=' ')
    st_address = models.CharField(max_length=60, default=' ')
    city_address = models.CharField(max_length=30, default=' ')
    zip_code = models.IntegerField(default=0)
    vat = models.CharField(max_length=1, default='')
    bir_reg_no = models.CharField(max_length=25, default=' ')
    tax_id_no = models.CharField(max_length=25, default=' ')
    credit_terms = models.SmallIntegerField(default=0)
    credit_limit = models.DecimalField(max_digits=15, decimal_places=3, default=0.000)
    balance = models.DecimalField(max_digits=15, decimal_places=3, default=0.000)
    date_as_of = models.DateField(default='0000-00-00')
    active = models.CharField(max_length=1, default='Y')
    group_id = models.IntegerField(default=0)
    group_name = models.CharField(max_length=150, default=' ')
    area_id = models.IntegerField(default=0)
    area_name = models.CharField(max_length=150, default=' ')
    office_name = models.CharField(max_length=150, default=' ')
    agent_id = models.IntegerField(default=0)
    agent_name = models.CharField(max_length=150, default=' ')
    collector_id = models.IntegerField(default=0)
    collector_name = models.CharField(max_length=150, default=' ')
    kob_id = models.IntegerField(default=0)
    kob_name = models.CharField(max_length=150, default=' ')
    remarks = models.CharField(max_length=100, default=' ')
    customer_image = models.BinaryField(blank=True, null=True)
    date_entered = models.DateField(default='0000-00-00')
    ul_code = models.IntegerField(default=0)
    Concessionare = models.CharField(max_length=10, default='')
    Client_behavior = models.CharField(max_length=5, default='LSCI')
    sl_category = models.CharField(max_length=50, default='')
    wtax_agent = models.CharField(max_length=1, default='')

    class Meta:
        db_table = 'tbl_customer'


class RCCDetails(models.Model):
    autonum = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=60, default=' ')
    desc_code = models.IntegerField(default=0)
    description = models.CharField(max_length=150, default=' ')
    rc_cost_category = models.CharField(max_length=100, default='')
    active = models.CharField(max_length=1, default='Y')
    alter_code = models.CharField(max_length=50, default=' ')
    ul_code = models.IntegerField(default=0)
    mfg_date = models.CharField(max_length=25, default='')
    created_by = models.CharField(max_length=100, default='')
    date_created = models.CharField(max_length=25, default='')
    mod_type = models.CharField(max_length=10, default='')
    mod_type_dup = models.CharField(max_length=10, default='')

    class Meta:
        db_table = 'tbl_rcc_details'


class Affiliate(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.SmallIntegerField(default=0)
    acct_title = models.CharField(max_length=100, default=' ')
    acronym = models.CharField(max_length=25, default='')
    balance = models.DecimalField(max_digits=15, decimal_places=3, default=0.000)
    date_as_of = models.DateField(default='0000-00-00')
    calculation = models.SmallIntegerField(default=0)
    ul_code = models.IntegerField(default=0)
    active = models.CharField(max_length=1, default='Y')
    sl_category = models.CharField(max_length=50, default='')

    class Meta:
        db_table = 'tbl_affiliate'


class Supplier(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.IntegerField(default=0)
    trade_name = models.CharField(max_length=150, default=' ')
    supplier_class = models.CharField(max_length=15, default=' ')
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=20)
    business_phone_no = models.CharField(max_length=15, default=' ')
    mobile_no = models.CharField(max_length=15, default=' ')
    fax_no = models.CharField(max_length=15, default=' ')
    st_address = models.CharField(max_length=60, default=' ')
    city_address = models.CharField(max_length=30, default=' ')
    zip_code = models.IntegerField(default=0)
    trade = models.CharField(max_length=1, default='')
    vat = models.CharField(max_length=1, default='')
    bir_reg_no = models.CharField(max_length=20, default=' ')
    tax_id_no = models.CharField(max_length=25, default=' ')
    credit_terms = models.SmallIntegerField(default=0)
    credit_limit = models.DecimalField(max_digits=15, decimal_places=3, default=0.000)
    balance = models.DecimalField(max_digits=15, decimal_places=3, default=0.000)
    date_as_of = models.DateField(default='1960-01-01')
    active = models.CharField(max_length=1, default='Y')
    group_id = models.IntegerField(default=0)
    group_name = models.CharField(max_length=150, default=' ')
    remarks = models.CharField(max_length=100, default=' ')
    supplier_image = models.BinaryField(blank=True, null=True)
    date_entered = models.DateField(default='1960-01-01')
    ul_code = models.IntegerField(default=0)
    sl_category = models.CharField(max_length=50, default='')

    class Meta:
        db_table = 'tbl_supplier'
        
        
class Consultant(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.PositiveIntegerField(default=0)
    trade_name = models.CharField(max_length=40)
    consultant_class = models.CharField(max_length=15, default=' ')
    last_name = models.CharField(max_length=30, default=' ')
    first_name = models.CharField(max_length=30, default=' ')
    middle_name = models.CharField(max_length=20, default=' ')
    business_phone_no = models.CharField(max_length=15, default=' ')
    mobile_no = models.CharField(max_length=15, default=' ')
    fax_no = models.CharField(max_length=15, default=' ')
    st_address = models.CharField(max_length=60, default=' ')
    city_address = models.CharField(max_length=30, default=' ')
    zip_code = models.PositiveIntegerField(default=0)
    trade = models.CharField(max_length=1, default='')
    vat = models.CharField(max_length=1, default='')
    bir_reg_no = models.CharField(max_length=20, default=' ')
    tax_id_no = models.PositiveIntegerField(default=0)
    credit_terms = models.SmallIntegerField(default=0)
    credit_limit = models.DecimalField(max_digits=15, decimal_places=3, default=0.000)
    balance = models.DecimalField(max_digits=15, decimal_places=3, default=0.000)
    date_as_of = models.DateField(default='0000-00-00')
    active = models.CharField(max_length=1, default='Y')
    remarks = models.CharField(max_length=100, default=' ')
    consultant_image = models.BinaryField(null=True, blank=True)
    date_entered = models.DateField(default='0000-00-00')
    ul_code = models.PositiveIntegerField(default=0)

    class Meta:
        # Define the table name explicitly (optional)
        db_table = 'tbl_consultant'

    def __str__(self):
        return self.trade_name        
        
class Member(models.Model):
    autonum = models.AutoField(primary_key=True)
    id_code = models.PositiveIntegerField(default=0)
    trade_name = models.CharField(max_length=40)
    member_class = models.CharField(max_length=15, default=' ')
    last_name = models.CharField(max_length=30, default=' ')
    first_name = models.CharField(max_length=30, default=' ')
    middle_name = models.CharField(max_length=20, default=' ')
    business_phone_no = models.CharField(max_length=15, default=' ')
    mobile_no = models.CharField(max_length=15, default=' ')
    fax_no = models.CharField(max_length=15, default=' ')
    st_address = models.CharField(max_length=60, default=' ')
    city_address = models.CharField(max_length=30, default=' ')
    zip_code = models.PositiveIntegerField(default=0)
    trade = models.CharField(max_length=1, default='')
    vat = models.CharField(max_length=1, default='')
    bir_reg_no = models.CharField(max_length=20, default=' ')
    tax_id_no = models.PositiveIntegerField(default=0)
    credit_terms = models.SmallIntegerField(default=0)
    credit_limit = models.DecimalField(max_digits=15, decimal_places=3, default=0.000)
    balance = models.DecimalField(max_digits=15, decimal_places=3, default=0.000)
    date_as_of = models.DateField(default='0000-00-00')
    active = models.CharField(max_length=1, default='Y')
    remarks = models.CharField(max_length=100, default=' ')
    member_image = models.BinaryField(null=True, blank=True)
    date_entered = models.DateField(default='0000-00-00')
    ul_code = models.PositiveIntegerField(default=0)
    sl_category = models.CharField(max_length=50, default='')

    class Meta:
        # Define the table name explicitly (optional)
        db_table = 'tbl_member'

    def __str__(self):
        return self.trade_name
    
    
class UnitLocation(models.Model):
    autonum = models.AutoField(primary_key=True)
    ul_code = models.PositiveSmallIntegerField(default=0)
    unit_description = models.CharField(max_length=30, default=' ')
    location_description = models.CharField(max_length=40, default=' ')
    alpha_code = models.CharField(max_length=10, default='')

    class Meta:
        db_table = 'tbl_unit_location'
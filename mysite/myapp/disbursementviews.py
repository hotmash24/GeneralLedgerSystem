
from datetime import  date
from calendar import monthrange
from django.db import transaction
from django.forms import CharField, ValidationError
from django.shortcuts import get_object_or_404, render,redirect
from django.shortcuts import render
from django.db import connection,models
# from models import (TblEmployee)


from django.templatetags.static import static
from myapp.disbursementmodels import (CvList,CFType,Payee,BankDrawee,NumberGenerator,AcctList,
                          Setup,AcctSubsidiary)
from myapp.subsidiarymodels import (OtherAccount,RCCDetails,Employee,Supplier,Affiliate,Customer,Member,Consultant,UnitLocation)

from myapp.transactionlistingmodels import (TransactionListingCDB,TransactionListingGeneralJournal,TransactionListingAPV,TransactionListingAR,TransactionListingCRB)
from myapp.reportviews import CV_list_report
from datetime import datetime

from django.http import HttpResponse
from django.http import JsonResponse
from .forms import SearchForm
from django.db.models import Q,Subquery, Sum
from django.db.models import F, Func
from django.db.models import Value
from django.db.models.functions import Concat, Substr, Cast, LPad
import datetime
from django.utils import timezone
import json
from django.core import serializers
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required, permission_required
from itertools import chain

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Image
from io import BytesIO
from docx import Document
from docx.shared import Inches

@login_required
def home(request):
    return render(request, 'home.html')


def xxx(request):
      return render(request, 'time.html')

def index(request):
    ul_code_login = request.session.get('UL_CODE')
    return render(request, 'disbursement.html',{'ul_code_login': ul_code_login})

def cashreceipts(request):
    ul_code_login = request.session.get('UL_CODE')
    return render(request, 'cashreceipts.html',{'ul_code_login': ul_code_login})
#---------- RETURN ALL LIST IN DISBURSEMENT FILTER------------

def cv_list_view(request):
    search_string = request.GET.get('SearchString')
    start_date = request.GET.get('from')
    end_date = request.GET.get('to')
    ul_code_login = request.session.get('UL_CODE')

    cv_list_records = CvList.objects.filter(ul_code=ul_code_login)

    # Apply filters based on the provided search_string and date range
    if search_string:
        cv_list_records = cv_list_records.filter(cv_no__icontains=search_string).order_by('-date_trans')
    if start_date and end_date:
        cv_list_records = cv_list_records.filter(date_trans__range=(start_date, end_date)).order_by('-date_trans')

    # Pagination
    paginator = Paginator(cv_list_records, 15)  # Show 10 records per page
    page_number = request.GET.get('page')
    try:
        cv_list_records_page = paginator.get_page(page_number)
    except PageNotAnInteger:
        # If the page parameter is not an integer, deliver the first page.
        cv_list_records_page = paginator.get_page(1)
    except EmptyPage:
        # If the page is out of range (e.g. 9999), deliver the last page of results.
        cv_list_records_page = paginator.get_page(paginator.num_pages)

    return render(request, 'disbursement.html', {'cv_list_records_page': cv_list_records_page})

# def cv_list_view(request):
#     search_string = request.GET.get('SearchString')
#     start_date = request.GET.get('from')
#     end_date = request.GET.get('to')
#     ul_code_login = request.session.get('UL_CODE')

#     # bank_drawee_list = BankDrawee.objects.all()
 
#     cv_list_records = CvList.objects.all()
#     if not start_date and not end_date and search_string:
#         # Filter records by search string only
#         cv_list_records = cv_list_records.filter(cv_no__icontains=search_string,ul_code=ul_code_login)
#     elif start_date and end_date and not search_string:
#         # Convert date strings to datetime objects
#         # start_date = datetime.strftime(start_date, '%Y-%m-%d').date()
#         # end_date = datetime.strftime(end_date, '%Y-%m-%d').date()

#         cv_list_records = cv_list_records.filter(date_trans__range=(start_date, end_date),ul_code=ul_code_login)
#     elif start_date and end_date and search_string:
#         # start_date = datetime.strftime(start_date, '%Y-%m-%d').date()
#         # end_date = datetime.strftime(end_date, '%Y-%m-%d').date()

#         cv_list_records = cv_list_records.filter(date_trans__range=(start_date, end_date), cv_no__icontains=search_string,ul_code=ul_code_login)
#     else:
#         # Retrieve all records if no filters provided
#         cv_list_records = CvList.objects.filter(ul_code=ul_code_login)
#     print(ul_code_login)
#     return render(request, 'disbursement.html', {'cv_list_records': cv_list_records})

# -----------------FILTER FOR SELECT TRANSTYPE------------------
def get_trans_type(request):
    module_type = 'CDB'
    status = 'Y'
    selected_option = request.GET.get('selectedOption')

    if selected_option == 'COFO':
        cf_key = 'COFO'
    elif selected_option == 'COFIA':
        cf_key = 'COFIA'
    else:
        cf_key = 'COFFA'
        
    trans_type_list = CFType.objects.filter(module_type=module_type, status=status, cf_key=cf_key).values('line_number', 'cf_desc')
    return JsonResponse(list(trans_type_list), safe=False)


# -----------------FILTER FOR SELECT PAYEE------------------
def payee(request):
    transactionTypeID = request.GET.get('transactionTypeID')
    payee_name = request.GET.get('payeeInput')
    sl_type = []
    if (transactionTypeID == 'Release of cash of advances to suppliers and contractors' or transactionTypeID == 'Payment of payables to suppliers' 
    or transactionTypeID == 'Cash aquisition of property' or transactionTypeID == 'Payment of payables to group accounts'):
        payee_list = Supplier.objects.filter(Q(trade_name__icontains=payee_name)).values('id_code', payee_name=F('trade_name'),address=F('st_address'))
        sl_type = 'Supplier'
    elif (transactionTypeID == 'Release of cash of advances to employees' or transactionTypeID == 'Replenishment of petty cash fund' 
   or transactionTypeID == 'Replenishment of revolving fund' or transactionTypeID == 'Payment of payables to employees'):
        # payee_list = Employee.objects.filter(Q(last_name__icontains=payee_name).annotate(payee_name=Concat('last_name', Value(' '), 'first_name', Value(' '), 'middle_name'))).values('id_code','payee_name')
        payee_list = Employee.objects.filter(last_name__icontains=payee_name).values(
        'id_code', payee_name=Concat('last_name', Value(' '), 'first_name', Value(' '), 'middle_name'),address=F('st_address'))
        sl_type = 'Employee'
    elif (transactionTypeID == 'Payment of payables to customers'):
        payee_list = Customer.objects.filter(Q(trade_name__icontains=payee_name)).values('id_code', payee_name=F('trade_name'),address=F('st_address'))
        sl_type = 'Customer'
    elif (transactionTypeID == 'Payment of payables to affiliates'):
        payee_list = Affiliate.objects.filter(Q(acct_title__icontains=payee_name)).values('id_code',payee_name=F('acct_title'),address=F('acronym'))
        sl_type = 'Affiliate'
    elif (transactionTypeID == 'Payment of other payables'):
        payee_list = OtherAccount.objects.filter(Q(sl_name__icontains=payee_name)).values('id_code',payee_name=F('sl_name'),address=F('acct_title'))
        sl_type = 'OtherAccount'
    elif (transactionTypeID == 'Payment of payables to consultant'):
        payee_list = Consultant.objects.filter(Q(trade_name__icontains=payee_name)).values('id_code', payee_name=F('trade_name'),address=F('st_address'))
        sl_type = 'Consultant'
    elif (transactionTypeID == 'Return of Owners Investment'):
        payee_list = Member.objects.filter(Q(trade_name__icontains=payee_name)).values('id_code', payee_name=F('trade_name'),address=F('st_address'))
        sl_type = 'Member'
    elif (transactionTypeID == 'Payment of payables to outsourcesd services'):
        payee_list = RCCDetails.objects.filter(Q(description__icontains=payee_name)).values(id_code=F('desc_code'), payee_name=F('description'),address=F('category'))
        sl_type = 'RCCDetails'
    else :
        payee_list = Payee.objects.filter(Q(payee_name__icontains=payee_name)).values('id_code','payee_name','address')
        sl_type = 'Payee'
    return JsonResponse(list(payee_list), safe=False)


# -----------------DISPLAY DRAWEE BANK-----------------
def bank_drawee(requets):
    drawee = requets.GET.get('draweeInput')

    if (drawee != ''):
         bank_drawee_list = BankDrawee.objects.filter(Q(bank_abbreviation__icontains=drawee)).values('id_code','bank_abbreviation')
    else:
         bank_drawee_list = BankDrawee.objects.all()
    return JsonResponse(list(bank_drawee_list), safe=False)


def modal(request):
    return render(request, 'modal.html')


def search_view(request):
    if request.method == 'POST' and request.is_ajax():
        form = SearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            results = Payee.objects.filter(Q(payee_name__icontains=search_query))
            payee_list = [payee.payee_name for payee in results]
            return JsonResponse({'results': payee_list})
    else:
        form = SearchForm()
    
    return render(request, 'disbursement.html', {'form': form})

# ------------------------------GET DOCUMENT NUMBER OF CV---------------------------
def CvNumber(request):
    cv_doctype = request.GET.get('doctype')
    with connection.cursor() as cursor:
        cursor.execute("SELECT next_no FROM tbl_number_generator WHERE doc_type = %s", [cv_doctype])
        row = cursor.fetchone()
        if row:
            next_no = row[0] + 1
        else:
            next_no = None
    response = JsonResponse({'cv_number': next_no})
    return HttpResponse(response, content_type='application/json')

def acct_title(requets):
    acct_code = requets.GET.get('accCode')
    acctTitle = requets.GET.get('acctTitle')
    # print('45454',acct_code)
    if acct_code is not None:
        acct_title_list = AcctList.objects.filter(
        Q(acct_title__icontains=acct_code) | Q(code__icontains=acct_code)
            ).values('code', 'acct_title')
    elif (acctTitle != ''):
         acct_title_list = AcctList.objects.filter(acct_title=acctTitle).values('code','acct_title')
        #  print(acct_title_list)
    else:
         acct_title_list = AcctList.objects.all()
    return JsonResponse(list(acct_title_list), safe=False)

def reviewed(requets):
    reviewed = requets.GET.get('reviewed')

    if reviewed != '':
        reviewed_list = Setup.objects.filter(Q(event_name__icontains=reviewed)).values('acct_title')
    else:
         reviewed_list = Setup.objects.all()
    return JsonResponse(list(reviewed_list), safe=False)

def approved(requets):
    approved = requets.GET.get('approved')

    if approved != '':
        approved_list = Setup.objects.filter(Q(event_name__icontains=approved)).values('acct_title')
    else:
        approved_list = Setup.objects.all()
    return JsonResponse(list(approved_list), safe=False)

def lsType(acct_title):
    sl_type_qs = AcctSubsidiary.objects.filter(subsidiary_acct_title=acct_title).values('sl_type')

    if sl_type_qs.exists():
        sl_type = sl_type_qs[0]['sl_type']
        return sl_type

    return None

def slAccount(request):

    acct_title = request.GET.get('slAcc')
    sl_type = lsType(acct_title)
    sl_list =[]
    print('SL_TYPE',sl_type)
    if sl_type == 'O':
        sl_list = list(OtherAccount.objects.filter(acct_title=acct_title).values('id_code', 'sl_name'))
    elif sl_type == 'R':
        sl_list = list(RCCDetails.objects.all().values(id_code=F('desc_code'), sl_name=F('description')))
    elif sl_type == 'E':
        sl_list = list(Employee.objects.annotate(sl_name=Concat('last_name', Value(' '), 'first_name', Value(' '), 'middle_name')).values('id_code', 'sl_name'))
    elif sl_type == 'S':
        sl_list = list(Supplier.objects.all().values('id_code', sl_name=F('trade_name')))
    elif sl_type == 'C':
        sl_list = list(Customer.objects.all().values('id_code', sl_name=F('trade_name')))
        # print(sl_list)
    return JsonResponse(list(sl_list), safe=False)

     
def GetPayeeID(payee):
    PayeeID = Payee.objects.filter(payee_name=payee).values('id_code')

    if PayeeID.exists():
        PayeeID = PayeeID[0]['id_code']
        return PayeeID

    return None

#-------------------- APPLICATION OF PAYMENT LIST-------------------
def ApplicationOfPayment(request):
    ul_code_login = request.session.get('UL_CODE')
    payee = request.GET.get('payee')
    Datefrom = request.GET.get('Datefrom')
    DateTo = request.GET.get('DateTo')
    Acct_title = request.GET.get('Acct_title')
    payeeID =request.GET.get('payeeId')
    sl_type = lsType(Acct_title)
    application_list = []
    application_list2 = []
    application_list3 = []
    combined_list = []

    if (Acct_title != 'ALL'):
                application_list = (
                TransactionListingCDB.objects
                .filter(date_trans__range=(Datefrom, DateTo), id_code=payeeID,acct_title=Acct_title,ul_code=ul_code_login,sl_type=sl_type)
                .exclude(credit_amount=0)
                .exclude(payment_status='PAID')
                .values(
                    'cv_no',
                    'date_trans',
                    'credit_amount',
                    'doc_type',
                    'id_code',
                    'acct_title',
                    'sl_acct',
                    'ul_code',
                    'primary_code',
                    'secondary_code',
                    'acct_code',
                    'subsidiary_code',
                        acct_codef=Concat(
                            LPad(Cast('primary_code', output_field=models.CharField(max_length=2)), 2, Value('0')),
                            LPad(Cast('secondary_code', output_field=models.CharField(max_length=2)), 2, Value('0')),
                            LPad(Cast('acct_code', output_field=models.CharField(max_length=3)), 3, Value('0')),
                            LPad(Cast('subsidiary_code', output_field=models.CharField(max_length=4)), 4, Value('0')),
                            output_field=models.CharField()
                        ) 
                    )
                )
        
                
                application_list3 = (
                    TransactionListingGeneralJournal.objects
                    .filter(date_trans__range=(Datefrom, DateTo), id_code=payeeID, acct_title=Acct_title, ul_code=ul_code_login, sl_type=sl_type)
                    .exclude(credit_amount=0)
                    .exclude(payment_status='PAID')
                    .values(
                        'date_trans',
                        'credit_amount',
                        'doc_type',
                        'id_code',
                        'acct_title',
                        'sl_acct',
                        'ul_code',
                        'primary_code',
                        'secondary_code',
                        'acct_code',
                        'subsidiary_code',
                        cv_no=F('jv_no'),
                        acct_codef=Concat(
                            LPad(Cast('primary_code', output_field=models.CharField(max_length=2)), 2, Value('0')),
                            LPad(Cast('secondary_code', output_field=models.CharField(max_length=2)), 2, Value('0')),
                            LPad(Cast('acct_code', output_field=models.CharField(max_length=3)), 3, Value('0')),
                            LPad(Cast('subsidiary_code', output_field=models.CharField(max_length=4)), 4, Value('0')),
                            output_field=models.CharField(),
                        ),
                    )
                    .annotate(credit_amoun=Sum('credit_amount'))
                )
                # print('search in GJ:',application_list3)
                        
                
                                                    
    else:
        acct_title =''
        print(acct_title)
        acct_title = getAcctiltleSetupforAplication2()
        for item in acct_title.split(','):
            cdb = TransactionListingCDB.objects.filter(
                date_trans__range=(Datefrom, DateTo),
                id_code=payeeID).exclude(credit_amount=0).exclude(payment_status='PAID').values(
                    'cv_no','date_trans','credit_amount','doc_type','id_code','sl_acct','ul_code','primary_code','secondary_code','acct_code','subsidiary_code').filter(acct_title__in=acct_title)
            application_list = list(cdb)
            combined_list.extend(application_list) 
            apv = (
                        TransactionListingAPV.objects
                        .filter(acct_title=item)
                        .exclude(credit_amount=0)
                        .exclude(payment_status='PAID')
                        .values(
                            'date_trans',
                            'credit_amount',
                            'doc_type',
                            'id_code',
                            'acct_title',
                            'sl_acct',
                            'ul_code',
                            'primary_code',
                            'secondary_code',
                            'acct_code',
                            'subsidiary_code',
                            cv_no=F('apv_no'),
                            acct_codef=Concat(
                                LPad(Cast('primary_code', output_field=models.CharField(max_length=2)), 2, Value('0')),
                                LPad(Cast('secondary_code', output_field=models.CharField(max_length=2)), 2, Value('0')),
                                LPad(Cast('acct_code', output_field=models.CharField(max_length=3)), 3, Value('0')),
                                LPad(Cast('subsidiary_code', output_field=models.CharField(max_length=4)), 4, Value('0')),
                                output_field=models.CharField(),
                            ),
                        )
                        .annotate(credit_amoun=Sum('credit_amount'))
                    )
            application_list2 = list(apv)
            combined_list.extend(application_list2)  
            
            gj = (
                        TransactionListingGeneralJournal.objects
                        .filter(date_trans__range=(Datefrom, DateTo), id_code=payeeID, acct_title=item, ul_code=ul_code_login)
                        .exclude(credit_amount=0)
                        .exclude(payment_status='PAID')
                        .values(
                            'date_trans',
                            'credit_amount',
                            'doc_type',
                            'id_code',
                            'acct_title',
                            'sl_acct',
                            'ul_code',
                            'primary_code',
                            'secondary_code',
                            'acct_code',
                            'subsidiary_code',
                            cv_no=F('jv_no'),
                            acct_codef=Concat(
                                LPad(Cast('primary_code', output_field=models.CharField(max_length=2)), 2, Value('0')),
                                LPad(Cast('secondary_code', output_field=models.CharField(max_length=2)), 2, Value('0')),
                                LPad(Cast('acct_code', output_field=models.CharField(max_length=3)), 3, Value('0')),
                                LPad(Cast('subsidiary_code', output_field=models.CharField(max_length=4)), 4, Value('0')),
                                output_field=models.CharField(),
                            ),
                        )
                        .annotate(credit_amoun=Sum('credit_amount'))
                    )
            application_list3 = list(gj)   
            combined_list.extend(application_list3)       
    return JsonResponse((combined_list), safe=False) 


def getAcctiltleSetupforAplication2():
    event_name = 'AP Voucher - Purchases'
    acct_title = Setup.objects.filter(event_name=event_name).values('acct_title')
    if acct_title.exists():
        acct_title = acct_title[0]['acct_title']
       
        return acct_title

    return None

def getAcctiltleSetupforAplication(request):
    event_name = 'AP Voucher - Purchases'
    act = request.GET.get('acct_title')
    acct_title_list=[]
    acct_title1 = Setup.objects.filter(event_name=event_name).values('acct_title')

    
    acct_titles = acct_title1[0]['acct_title'].split(',')
    for acct_title in acct_titles:
        queryset = AcctList.objects.filter(acct_title=acct_title).values('code','acct_title')
        # Append the queryset to the results list
        acct_title_list.extend(queryset)
        # print('SSS',queryset)
        # serialized_data = serializers.serialize('json', queryset)
        # acct_title_list.append(serialized_data)
    # print('SSS',acct_title_list)
    return JsonResponse(list(acct_title_list), safe=False) 
    # return JsonResponse(acct_title_list, safe=False)

@transaction.atomic
def SaveCashDisbursement(request):
    if request.user.has_perm('myapp.add_acctlist'):
        if request.method == 'POST':
            payeeId = request.POST.get('payeeId', '')
            payee = request.POST.get('payee', '')
            bank = request.POST.get('bank', '')
            doc_type = request.POST.get('doc_type', '')
            docref = request.POST.get('docref', '')
            Voucherdate = request.POST.get('Voucherdate', '')
            Checkdate = request.POST.get('Checkdate', '')
            checkNo = request.POST.get('checkNo', '')
            remarks = request.POST.get('remarks', '')
            approved = request.POST.get('approved', '')
            reviewed = request.POST.get('reviewed', '')
            prepared = request.POST.get('prepared', '')
            debit = request.POST.get('totaldebit', '')
            ul = request.session.get('UL_CODE'),
            # print('check no:',checkNo)
            credit = request.POST.get('totalcredit', '')
            transactionTypeID = request.POST.get('transactionTypeID', '').upper()
            table_list = request.POST.getlist('table_list')
            
            current_datetime = timezone.now()
            formatted_datetime = current_datetime.strftime('%Y-%m-%d')
            Save_to_CvList = CvList(
                ul_code = request.session.get('UL_CODE'),
                cv_no=docref,
                date_trans=formatted_datetime,
                due_date=Voucherdate,
                id_code = payeeId,
                payee=payee,
                check_amt = credit,
                drawee_bank = bank,
                date_check = Checkdate,
                check_no = checkNo,
                check_type = 'C',
                remarks = remarks,
                TransType = transactionTypeID,
                active = 'YS',
                prepared_by = prepared,
                doc_type = doc_type,
                )
            Save_to_CvList.save()
            
            SaveTransactionlistingCDB(table_list,payee,docref,doc_type,prepared,formatted_datetime,checkNo,ul)

            with connection.cursor() as cursor:
                cursor.execute("update tbl_number_generator set next_no = %s WHERE doc_type = %s", (docref,doc_type))
                # connection.commit()

            response_data = {
                'message': 'Data processed and saved successfully!',
            }
            print('success')
            # return redirect('cv_list_transaction')
            return JsonResponse(response_data)
        response_data = {
            'error': 'Invalid request',
        }
        # return redirect('cv_list_transaction')
        return JsonResponse(response_data, status=400)
    else:
        response_data = {'message': 'You do not have permission to perform this action.'}
        return JsonResponse(response_data)
        
@transaction.atomic
def SaveTransactionlistingCDB(table_list_json,payee,docref,doc_type,prepared,date,checkNo,ul):
    # Get the JSON string from the list and convert it to a list of dictionaries
    table_list = json.loads(table_list_json[0])
    # print('table_list:',table_list)
    for item in table_list:
        name_to_search = item['acct_title']
        # print(name_to_search)
        
        
        debit_amount_str = item['debit_amount']
        credit_amount_str = item['credit_amount']

        # Remove commas from the strings
        debit_amount_str = debit_amount_str.replace(',', '')
        credit_amount_str = credit_amount_str.replace(',', '')
        # print('name_to_search')
        debit_amount = float(debit_amount_str)
        credit_amount = float(credit_amount_str)
        # Convert the strings to floats
       
        Save_to_CDB = TransactionListingCDB(
            ul_code = int(ul[0]),
            payee = payee,
            cv_no = docref,
            date_trans = date,
            id_code = item['id_code'],
            sl_acct = item['sl_acct'],
            primary_code = item['primary_code'],
            secondary_code = item['secondary_code'],
            acct_code = item['acct_code2'],
            subsidiary_code = item['subsidiary_code'],
            acct_title = item['acct_title'],
            debit_amount = float(debit_amount),
            credit_amount = float(credit_amount),
            active = 'YS',
            posted_by = prepared,
            date_posted = date,
            sl_type = lsType(item['acct_title']),
            check_no = str(checkNo).zfill(10),
            doc_type = doc_type, 
             )
        
        Save_to_CDB.save()
    return
        
def GetAccountCodeIndividually(request):
    acct_title = request.GET.get('ACCOUNTTILTE')
    print('ACCOUNTTILTE', acct_title)
    sl_type_qs = AcctSubsidiary.objects.filter(subsidiary_acct_title=acct_title).values('primary_code', 'secondary_code', 'acct_code', 'subsidiary_code', 'sl_type')

    # Convert QuerySet to a list of dictionaries
    sl_type_list = list(sl_type_qs)
    return JsonResponse(sl_type_list, safe=False)

def GetSLCODE(request):

    sl_type = request.GET.get('sl_type_per_acct_Title')
    slentry = request.GET.get('slentry')
    sl_list =''
    # print('SL_TYPE',sl_type)
    if sl_type == 'O':
        sl_list = OtherAccount.objects.filter(sl_name=slentry).values('id_code')
    elif sl_type == 'R':
        sl_list = RCCDetails.objects.filter(description=slentry).values(id_code=F('desc_code'))
    elif sl_type == 'E':
        sl_list = Employee.objects.filter(sl_name=slentry).annotate(sl_name=Concat('last_name', Value(' '), 'first_name', Value(' '), 'middle_name')).values('id_code', 'sl_name')
    elif sl_type == 'S':
        sl_list = Supplier.objects.filter(trade_name=slentry).values('id_code')
    elif sl_type == 'C':
        sl_list = Customer.objects.filter(trade_name=slentry).values('id_code')
    if sl_list.exists():
        sl_type = sl_list[0]['id_code']
    return HttpResponse(sl_type)


# @login_required(login_url="/accounts/login/")

def cv_list_transaction(request):
    cv_list_records_page = 0
    if request.user.has_perm('myapp.CashReceiptsView'):
        today = date.today()

        # Get the first day of the current month
        first_day_of_month = today.replace(day=1)

        # Get the last day of the current month
        last_day_of_month = today.replace(day=monthrange(today.year, today.month)[1])
        ul_code_login = request.session.get('UL_CODE')
        
        cv_list_records = CvList.objects.filter(ul_code=ul_code_login)
        
        cv_list_records = cv_list_records.filter(date_trans__range=(first_day_of_month, last_day_of_month)).order_by('-date_trans','-cv_no')
        print('records:',cv_list_records)
        paginator = Paginator(cv_list_records, 15)  
        page_number = request.GET.get('page')
        try:
            cv_list_records_page = paginator.get_page(page_number)
        except PageNotAnInteger:
            cv_list_records_page = paginator.get_page(1)
        except EmptyPage:
            cv_list_records_page = paginator.get_page(paginator.num_pages)

        return render(request, 'disbursement.html', {'cv_list_records_page': cv_list_records_page,'ul_code_login': ul_code_login})
    message = "Sorry, you don't have permission to access this page."
    return render(request, 'home.html', {'message': message})

def SetDaTaFields(request):
    cv_no = request.GET.get('cv_no')
    checkNo = request.GET.get('checkNo')
    checkNo = str(checkNo).zfill(10)
    ul_code_login = request.session.get('UL_CODE')
    
    today = date.today()
    first_day_of_month = today.replace(day=1)
    last_day_of_month = today.replace(day=monthrange(today.year, today.month)[1])

    if cv_no == '':
        latest_records = CvList.objects.filter(date_trans__range=(first_day_of_month, last_day_of_month),ul_code=ul_code_login).order_by('-cv_no')[:1]
    else:
         latest_records = CvList.objects.filter(date_trans__range=(first_day_of_month, last_day_of_month),ul_code=ul_code_login,cv_no=cv_no,check_no=checkNo).order_by('-cv_no')[:1]
   
    latest_record = latest_records.first()  # Get the first record or None if no records are found
    if latest_record:
        latest_record_data = [
            latest_record.cv_no,
            latest_record.date_trans,
            latest_record.due_date,
            latest_record.doc_type,
            latest_record.id_code,
            latest_record.payee,
            latest_record.check_amt,
            latest_record.drawee_bank,
            latest_record.date_check,
            latest_record.check_no,
            latest_record.remarks,
            latest_record.TransType,
            latest_record.prepared_by,
            latest_record.reviewed_by,
            latest_record.approved_by,
            
        ]
        return JsonResponse(latest_record_data, safe=False)
    else:
        return JsonResponse({'message': 'No records found.'})
    
def DisplayEntry(request):
    ul_code_login = request.session.get('UL_CODE')
    cv_no = request.GET.get('cv_no')
    checkNo = request.GET.get('checkNo')
    checkNo = str(checkNo).zfill(10)
    # print('check number :' ,checkNo)
    results_list = []
    try:
        # print('eqweqweqweqw0.1', cv_no)
        transaction_records = TransactionListingCDB.objects.filter(cv_no=cv_no,check_no=checkNo).order_by('-cv_no')
        print('xxxfffffx.1',transaction_records)
        
        # Loop through each record
        for latest_transaction_record in transaction_records:
            print('acct_list_record:', latest_transaction_record.id_code)
            acct_list_record = AcctList.objects.filter(acct_title=latest_transaction_record.acct_title).values('code', 'primary_code', 'secondary_code', 'acct_code', 'subsidiary_code')
            
   
            # Initialize the results dictionary for each iteration
            results = {}

            ul_code = latest_transaction_record.ul_code
            id_code = latest_transaction_record.id_code
            sl_name = latest_transaction_record.sl_acct
            acct_title = latest_transaction_record.acct_title
            debit_amount = latest_transaction_record.debit_amount
            credit_amount = latest_transaction_record.credit_amount
            print('id_code',id_code)
            for record in acct_list_record:
                acct_code = record['code']
                primary_code = record['primary_code']
                secondary_code = record['secondary_code']
                acct_code2 = record['acct_code']
                subsidiary_code = record['subsidiary_code']

            # Add the values to the dictionary using cv_no as the key
            results = {
            'ul_code': ul_code,
            'acct_code': acct_code,
            'acct_title': acct_title,
            'sl_name': sl_name,
            'debit_amount': debit_amount,
            'credit_amount': credit_amount,
            'id_code': id_code,
            'primary_code': primary_code,
            'secondary_code': secondary_code,
            'acct_code2': acct_code2,
            'subsidiary_code': subsidiary_code,

                # Add other columns from both models if needed
            }

            results_list.append(results)

        # print('results:', results_list)
        results_json = JsonResponse(list(results_list),safe=False)
        return results_json
    except ValidationError as ve:
        # Log the error or handle it as needed
        print("ValidationError:", ve)

        # Return an error response to the client if desired
        return JsonResponse({'error': 'An error occurred while fetching data.'}, status=500)
    
def LocationSelect(request):
    ul = request.GET.get('ul')
    location_list = []
    location_list = list(UnitLocation.objects.all().values('ul_code','unit_description'))
    
    return JsonResponse(list(location_list),safe=False)

@transaction.atomic
@permission_required
def UpdateCashDisbursement(request):
    if request.method == 'POST':
        payeeId = request.POST.get('payeeId', '')
        payee = request.POST.get('payee', '')
        bank = request.POST.get('bank', '')
        doc_type = request.POST.get('doc_type', '')
        docref = request.POST.get('docref', '')
        Voucherdate = request.POST.get('Voucherdate', '')
        Checkdate = request.POST.get('Checkdate', '')
        checkNo = request.POST.get('checkNo', '')
        remarks = request.POST.get('remarks', '')
        approved = request.POST.get('approved', '')
        reviewed = request.POST.get('reviewed', '')
        prepared = request.POST.get('prepared', '')
        debit = request.POST.get('total_debit', '')
        ul = request.session.get('UL_CODE'),
       
       
        print( 'payeeeeeee',payeeId)

        CvList.objects.filter(cv_no=docref).delete()
        TransactionListingCDB.objects.filter(cv_no=docref).delete()
        credit = request.POST.get('total_credit', '')
        transactionTypeID = request.POST.get('transactionTypeID', '').upper()
        table_list = request.POST.getlist('table_list')
        
        
   
        
        credit = credit.replace(',', '')
        print('credit',credit)
        current_datetime = timezone.now()
        formatted_datetime = current_datetime.strftime('%Y-%m-%d')
        Save_to_CvList = CvList(
            ul_code = request.session.get('UL_CODE'),
            cv_no=docref,
            date_trans=formatted_datetime,
            due_date=Voucherdate,
            id_code = payeeId,
            payee=payee,
            check_amt = credit,
            drawee_bank = bank,
            date_check = Checkdate,
            check_no = checkNo,
            check_type = 'C',
            remarks = remarks,
            TransType = transactionTypeID,
            active = 'YS',
            prepared_by = prepared,
            doc_type = doc_type,
            )
        Save_to_CvList.save()
        
        UpdateTransactionlistingCDB(table_list,payee,docref,doc_type,prepared,formatted_datetime,checkNo,ul)

        with connection.cursor() as cursor:
            cursor.execute("update tbl_number_generator set next_no = %s WHERE doc_type = %s", (docref,doc_type))
            # connection.commit()

        response_data = {'message': 'Data processed and saved successfully!'}
        # return redirect('cv_list_transaction')
        return JsonResponse(response_data)
    # return redirect('cv_list_transaction')
    return JsonResponse(response_data, status=400)
@transaction.atomic
def UpdateTransactionlistingCDB(table_list_json,payee,docref,doc_type,prepared,date,checkNo,ul):
    # Get the JSON string from the list and convert it to a list of dictionaries
    table_list = json.loads(table_list_json[0])
    for item in table_list:
        name_to_search = item['acct_title']
        
        
        debit_amount_str = item['debit_amount']
        credit_amount_str = item['credit_amount']

        # Remove commas from the strings
        debit_amount_str = debit_amount_str.replace(',', '')
        credit_amount_str = credit_amount_str.replace(',', '')
        debit_amount = float(debit_amount_str)
        credit_amount = float(credit_amount_str)
        # Convert the strings to floats
       
        Save_to_CDB = TransactionListingCDB(
            ul_code = int(ul[0]),
            payee = payee,
            cv_no = docref,
            date_trans = date,
            id_code = item['id_code'],
            sl_acct = item['sl_acct'],
            primary_code = item['primary_code'],
            secondary_code = item['secondary_code'],
            acct_code = item['acct_code2'],
            subsidiary_code = item['subsidiary_code'],
            acct_title = item['acct_title'],
            debit_amount = float(debit_amount),
            credit_amount = float(credit_amount),
            active = 'YS',
            posted_by = prepared,
            date_posted = date,
            sl_type = lsType(item['acct_title']),
            check_no = str(checkNo).zfill(10),
            doc_type = doc_type, 
             )
        
        Save_to_CDB.save()
    return

def StatusOfTransaction(request):
    if request.user.has_perm('myapp.change_acctlist'):
        if request.method == 'POST':
            cv_no = request.POST.get('cv_no')
            click = request.POST.get('click')
            current_datetime = timezone.now()
            prepared_by = request.POST.get('prepared')
            approved_by = request.POST.get('approved')
            formatted_datetime = current_datetime.strftime('%Y-%m-%d')
            
            try:
                if click == 'Approve':
                    status = CvList.objects.get(cv_no=cv_no)
                    status.approved_by = approved_by
                    status.approved_date = formatted_datetime
                    status.active = 'YS'
                    status.save()
                elif click == 'Review':
                    status = CvList.objects.get(cv_no=cv_no)
                    status.reviewed_by = request.POST.get('reviewed')
                    status.reviewed_date = formatted_datetime
                    status.save()
                elif click == 'Cancel':
                    status = CvList.objects.get(cv_no=cv_no)
                    status.cancel_by = prepared_by
                    status.cancel_date = formatted_datetime
                    status.active = 'NS'
                    status.save()
                elif click == 'Uncancel':
                    status = CvList.objects.get(cv_no=cv_no)
                    status.active = 'YS'
                    status.save()
                else:
                    response_data = {'error': 'Invalid request'}
                    return JsonResponse(response_data, status=400)
                
                response_data = {'message': 'Data processed and saved successfully!'}
                return JsonResponse(response_data)
            except CvList.DoesNotExist:
                response_data = {'error': 'CV with the specified cv_no does not exist.'}
                return JsonResponse(response_data, status=404)
            except Exception as e:
                response_data = {'error': f'Something went wrong: {str(e)}'}
                return JsonResponse(response_data, status=500)

        response_data = {'error': 'Invalid request'}
        return JsonResponse(response_data, status=400)
    
    else:
        response_data = {'message': 'You do not have permission to perform this action.'}
        return JsonResponse(response_data)
    
    


from django.urls import path
from .disbursementviews import (index,cv_list_view,modal,get_trans_type,payee,search_view,bank_drawee,CvNumber,reviewed,
acct_title,approved,slAccount,ApplicationOfPayment,getAcctiltleSetupforAplication,home,cashreceipts,xxx,SaveCashDisbursement,
GetAccountCodeIndividually,GetSLCODE,cv_list_transaction,SetDaTaFields,DisplayEntry,LocationSelect,UpdateCashDisbursement,StatusOfTransaction)
from .loginviews import login_view,logout_view,get_client_ip
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('', login_view, name='login'),
    # path('', login_view, name='login'),
    path('home/', home , name='home'),
    path('disbursement/', index , name='index'),
    path('cash-list/', cv_list_transaction , name='cv_list_transaction'),
    path('cash-receipts>/', cashreceipts , name='cashreceipts'),
    path('xxx/', xxx , name='xxx'),
    #-------------- CASH DISBURSEMENT PATH----------------------
    path('disburement/', cv_list_view, name='search_view'),
    #  path('api/trans-type/', views.trans_type, name='trans_type'),
    path('api/trans-type/', get_trans_type, name='get_trans_type'),
    path('api/payee-list/', payee, name='payee'),
    path('search/', search_view, name='search'),
    path('api/drawee-list/', bank_drawee, name='bankdrawee'),
    path('api/cv-number/',CvNumber ,name='cvNumber' ),
    path('api/acct-title/',acct_title ,name='acct_title'),
    path('api/reviewed/',reviewed ,name='reviewed'),
    path('api/approved/',approved ,name='approved'),
    path('api/slAccount/',slAccount ,name='slAccount'),
    path('api/ApplicationOfPayment/',ApplicationOfPayment ,name='ApplicationOfPayment'),
    path('api/acct-title-list/',getAcctiltleSetupforAplication ,name='getAcctiltleSetupforAplication'),
    path('logout/',logout_view ,name='logout'),
    path('login/', login_view, name='login'),
    path('modal/',modal, name='modal'),
    path('api/set-data-fields/',SetDaTaFields, name='SetDaTaFields'),
    path('api/set-display-entry/',DisplayEntry, name='DisplayEntry'),
    path('api/Save-Cash-Disbursement/',SaveCashDisbursement, name='SaveCashDisbursement'),
    path('api/get-sl-code/',GetSLCODE, name='GetSLCODE'),
    path('api/AccoutCodeIndividual/',GetAccountCodeIndividually, name='GetAccountCodeIndividually'),
    path('api/location-select/', LocationSelect, name='LocationSelect'),
    path('api/update-Cash-Disbursement/',UpdateCashDisbursement, name='UpdateCashDisbursement'),
    path('api/status-of-transaction/',StatusOfTransaction, name='StatusOfTransaction'),
    # path('pdf-report/', pdf_report_view, name='pdf_report_view'),
    # path('word-report/', word_report_view, name='word_report_view'),
]
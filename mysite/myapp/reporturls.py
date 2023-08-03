from django.urls import path
from .disbursementviews import (index,cv_list_view,modal,get_trans_type,payee,search_view,bank_drawee,CvNumber,reviewed,
acct_title,approved,slAccount,ApplicationOfPayment,getAcctiltleSetupforAplication,home,cashreceipts,xxx,SaveCashDisbursement,
GetAccountCodeIndividually,GetSLCODE,cv_list_transaction,SetDaTaFields,DisplayEntry,LocationSelect,UpdateCashDisbursement,StatusOfTransaction)
from .loginviews import login_view,logout_view
from .reportviews import CV_list_report,CVPR_report_view,CVPR_report_view1,CVPR_reportView
from django.contrib.auth import views as auth_views
from .reportviews import generate_pdf



urlpatterns = [
    path('sub/', index, name='index'),
    path('pdf-report/', CV_list_report, name='pdf_report_view'),
    path('cvpr-report/', CVPR_report_view, name='CVPR_report_view'),
    path('cvpr-report1/', CVPR_report_view1, name='CVPR_report_view1'),
    # path('cvpr-doc-report/', generate_word_report, name='generate_word_report'),
    path('cvpr-html/', CVPR_reportView, name='CVPR_reportView'),
    path('api/generate_pdf/', generate_pdf, name='generate_pdf'),
    # # path('pdf/', GeneratePdf.as_view(),name="GeneratePdf"), 
    # path('resume-pdf/', resume_pdf, name="resume-pdf"),
    # Add more URLs for this subsection or functionality
]
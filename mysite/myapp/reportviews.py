

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
# from docx import Document
# from docx.shared import Pt
# from docx.enum.text import WD_ALIGN_PARAGRAPH
# from docx.shared import Inches
import locale
from .templatetags.AmountToWords import amount_to_words_with_cents
locale.setlocale(locale.LC_ALL, 'en_US')

from num2words import num2words


import pdfkit
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
import os
from django.template.loader import get_template
from django.views.generic import View
# from .process import html_to_pdf 

from django.template import Context
import datetime
# from xhtml2pdf import pisa 
import os
os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
from weasyprint import HTML ,CSS
def CV_list_report(request):
    if request.method == 'POST':
    # data = CvList.objects.all()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="specific_report.pdf"'
        data = json.loads(request.body)
        print(data)
        # Create the PDF
        left_margin = 10
        right_margin = 10
        top_margin = 10
        bottom_margin = 10
        # Create the PDF with custom margins
        doc = SimpleDocTemplate(response, pagesize=letter,
                                leftMargin=left_margin,
                                rightMargin=right_margin,
                                topMargin=top_margin,
                                bottomMargin=bottom_margin)
            # Create the container for elements
        elements = []
        font_size = 8
        styles = getSampleStyleSheet()
    
    
    
            # Adding an image to the PDF
        # image = YourModel.objects.get(pk=your_model_instance_id)  # Replace with the actual object ID
        # image_path = your_model_instance.image_field.path

        # # Adding an image to the PDF (using the image retrieved from the database)
        # img = Image(image_path, width=200, height=100)  # Adjust width and height as needed
        # elements.append(img)
    
        # Set up custom styles for table
        paragraph_text  = 'Cash Disbursement List'
        # Report_name = Paragraph(paragraph_text, styles['Normal'])
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), font_size), 
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])

        # Create the table data with custom formatting
        table_data = [['CV No', 'Date', 'Payee', 'Check No', 'Amount']]
        x = 0
        for item in data:
            x+=float(item['Amount'].replace(',',''))
            # amount = locale.format_string("%.2f", item.check_amt, grouping=True)
            table_data.append([
                item['DocRef'],          
                item['Date'], 
                item['Payee'], 
                item['CheckNO'], 
                item['Amount'],   
            ])

        total_style = ParagraphStyle(
            'TotalStyle',
            parent=styles['Normal'],
            fontName='Helvetica-Bold',
            fontSize=10,  # Change the font size here
            textColor=colors.black,  # Change the font color if needed
            spaceBefore=10,  # Adjust spacing before the paragraph
            alignment=2,
        )
        
        name_style = ParagraphStyle(
            'TotalStyle',
            parent=styles['Normal'],
            fontName='Helvetica-Bold',
            fontSize=20,  # Change the font size here
            textColor=colors.black,  # Change the font color if needed
            spaceAfter=40,  # Adjust spacing before the paragraph
            leftIndent=10,   # Adjust the left margin position in points (1 inch = 72 points)
            # rightIndent=80,
        )

        table = Table(table_data, colWidths=[100, 80, 280, 60, 60])
        table.setStyle(table_style)
        amount = locale.format_string("%.2f", x, grouping=True)
        total_string = 'TOTAL: ' + str(amount)
        
        TOTAL = Paragraph(total_string,total_style)
        NAME = Paragraph(paragraph_text,name_style)
        
        # Add the table to the PDF
        elements.append(NAME)
        elements.append(table)
        elements.append(TOTAL)
        # Build the PDF document
        
        doc.build(elements)

    return response


def CVPR_report_view1(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data sent in the request body
            data = json.loads(request.body)

            # Access the form data and table_list from the data dictionary
            form_data = data.get('formData', {})
            table_list = data.get('tableData', [])
            print('Table:',table_list)
            payee = form_data.get('payee')
            doc_typeank = form_data.get('doc_type')
            docref = form_data.get('docref')
            Voucherdate = form_data.get('Voucherdate')
            checkNo = form_data.get('checkNo')
            totalcredit = form_data.get('totalcredit')
            bantotaldebit = form_data.get('totaldebit')
            remark = form_data.get('remark')
            approved = form_data.get('approved')
            reviewed = form_data.get('reviewed')
            prepared = form_data.get('prepared')

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="specific_report.pdf"'
            data = json.loads(request.body)
            print(data)
            # Create the PDF
            left_margin = 10
            right_margin = 10
            top_margin = 10
            bottom_margin = 10
            doc = SimpleDocTemplate(response, pagesize=letter,
                                    leftMargin=left_margin,
                                    rightMargin=right_margin,
                                    topMargin=top_margin,
                                    bottomMargin=bottom_margin)
        
            
            elements = []
            font_size = 8
            styles = getSampleStyleSheet()
            
            row_heights = [100]
            PayeeData = [['PAYEE','CHECK VOUCHER']]
            PayeeData_style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.white),    # Header row background color
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),# Header text color
                ('ALIGN', (0, 0), (-1, 0), 'LEFT'),
                ('LINEBELOW', (0, 0), (-1, 0),1, colors.black),
                ('ALIGN', (0, 1), (-1, -1), 'LEFT'),           # Center align the content
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), # Header font
                ('BOTTOMPADDING', (0, 0), (-1, 0), 1),          # Header padding
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Non-header row background color
                ('GRID',(0, 0), (-1, -1), 1, colors.black),
                ])
            payeeTable = Table(PayeeData,colWidths=[475,130],rowHeights=row_heights)
            payeeTable.setStyle(PayeeData_style)
            elements.append(payeeTable)
            
            data = [['ACCOUNT ENTRY DETAILS','DEBIT','CREDIT']]
            table_style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.white),    # Header row background color
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),# Header text color
                ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                ('LINEBELOW', (0, 0), (-1, 0),1, colors.black),
                ('ALIGN', (0, 1), (-1, -1), 'LEFT'),           # Center align the content
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), # Header font
                ('BOTTOMPADDING', (0, 0), (-1, 0), 5),          # Header padding
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Non-header row background color
                ('ALIGN', (-2, 1), (-1, -1), 'RIGHT'),
                ('BOX',(0, 0), (-1, -1), 1, colors.black),
                ])




            for item in table_list:
                    data.append([
                    item['ul'] + ' ' + item['acct_title'] + ' - ' + item['sl_name'], 
                    item['debit_amount'], 
                    item['credit_amount'],   
                ])
            col_widths = [475,65,65]
            table = Table(data, colWidths=col_widths)
            table.setStyle(table_style)
            elements.append(table)
        
            doc.build(elements)
            return response
            # return JsonResponse({'success': True, 'message': 'Data retrieved successfully.'})

        except json.JSONDecodeError as e:
            # Handle the case when the JSON data is not valid
            return JsonResponse({'success': False, 'error': str(e)})

    else:
        # Handle the case when the request method is not POST
        return JsonResponse({'success': False, 'error': 'Invalid request method.'})


# def generate_word_report(request):
#     if request.method == 'POST':
#         doc = Document()
#         data = json.loads(request.body)
#         form_data = data.get('formData', {})
#         table_list = data.get('tableData', [])
#         # print('Table:', table_list)
#         # payee = form_data.get('payee')
#         # doc_typeank = form_data.get('doc_type')
#         # docref = form_data.get('docref')
#         # Voucherdate = form_data.get('Voucherdate')
#         # checkNo = form_data.get('checkNo')
#         # totalcredit = form_data.get('totalcredit')
#         # bantotaldebit = form_data.get('totaldebit')
#         # remark = form_data.get('remark')
#         # approved = form_data.get('approved')
#         # reviewed = form_data.get('reviewed')
#         # prepared = form_data.get('prepared')
       

#         title = doc.add_heading('Sample Word Report', level=1)
#         title.alignment = WD_ALIGN_PARAGRAPH.CENTER
#         doc.add_paragraph("This is a sample Word report generated using Django and python-docx.")
#         doc.add_paragraph("You can add more paragraphs and formatting as needed.")
#         response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#         response['Content-Disposition'] = 'attachment; filename="sample_report.docx"'
#         doc.save(response)

#         return response

        

def CVPR_report_view(request):
    if request.method == 'POST':
    
            # Parse the JSON data sent in the request body
            data = json.loads(request.body)

            # Access the form data and table_list from the data dictionary
            form_data = data.get('formData', {})
            table_list = data.get('tableData', [])
            payee = form_data.get('payee')
            doc_type = form_data.get('doc_type')
            docref = form_data.get('docref')
            bank = form_data.get('bank')
            Voucherdate = form_data.get('Voucherdate')
            checkNo = form_data.get('checkNo')
            totalcredit = form_data.get('totalcredit')
            totaldebit = form_data.get('totaldebit')
            remark = form_data.get('remarks')
            approved = form_data.get('approved')
            reviewed = form_data.get('reviewed')
            prepared = form_data.get('prepared')
            
            
            t1 = locale.format_string("%.2f", totalcredit, grouping=True)
            t2 = locale.format_string("%.2f", totaldebit, grouping=True)
            amount_in_words = amount_to_words_with_cents(totalcredit)
            print('amount to words:',amount_in_words)
            context = {
                'EntryDetails': table_list,
                'Payee': payee,
                'Doctype': doc_type,
                'DocRef': docref,
                'VoucherDate': Voucherdate,
                'Bank': bank,
                'AmountWords': amount_in_words,
                'CheckNo': checkNo,
                'Credit': t1,
                'Debit': t2,
                'Remarks': remark,
                'Approved': approved,
                'reviewed': reviewed,
                'prepared': prepared,
            }
            request.session['cvpr_data'] = context
            print(context)
        # Redirect to CVPR.html, which will open in a new tab
            return redirect('CVPR_reportView')
    
    # For GET request or any other request method, redirect to CVPR.html without data
    return redirect('CVPR_reportView')
        # return:
    #     except json.JSONDecodeError as e:
    #         # Handle the case when the JSON data is not valid
    #         return JsonResponse({'success': False, 'error': str(e)})

    # else:
    #     # Handle the case when the request method is not POST
    #     return JsonResponse({'success': False, 'error': 'Invalid request method.'})

def CVPR_reportView(request):
    context = request.session.get('cvpr_data', {})
    return render(request, 'CVPR.html', context)

# def html_to_pdf(request):
#     # Replace 'your_template.html' with the name of your HTML template
#     template_name = 'CVPR.html'

#     # Replace 'your_pdf_filename.pdf' with the desired name for the generated PDF file
#     pdf_filename = 'CVPR.pdf'

#     # Generate the absolute paths for the template and PDF file
#     template_path = os.path.join(settings.BASE_DIR, 'myapp', 'templates', template_name)
#     pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_filename)

#     # Render the HTML template to a string
#     html_string = render_to_string(template_name)

#     # Use pdfkit to convert the HTML string to a PDF file
#     pdfkit.from_string(html_string, pdf_path)

#     # Open the generated PDF file and serve it as an attachment for the user to print
#     with open(pdf_path, 'rb') as pdf_file:
#         response = HttpResponse(pdf_file.read(), content_type='application/pdf')
#         response['Content-Disposition'] = f'attachment; filename="{pdf_filename}"'
#         return response
    
# importing the necessary libraries

import weasyprint

def generate_pdf(request):
    # Get the HTML template
    template = get_template('CVPR.html')
    context = request.session.get('cvpr_data', {})
    html = template.render(context)

    # Generate PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filen1ame="CVPR.pdf"'
    weasyprint.HTML(string=html).write_pdf(response)

    return response
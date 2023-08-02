# from django.apps import AppConfig
from django.apps import AppConfig
from django.db import connection
from django.conf import settings
from django.http import HttpResponse
locationUnit = []
sORCash =[]
sORReceivables =[]
sORGC =[]
sOROthers = []
sCVCash = []
sCVPayables = []
sCVCAdvance=[]
sCVPPE=[]
class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
    
    def ready(self):
        # from . import signal
        with connection.cursor() as cursor:
            # cursor.execute("SELECT acct_title FROM tbl_setup  WHERE event_name = %s", ['AP Voucher - Purchases'])
            cursor.execute("SELECT event_name,acct_title FROM tbl_setup")
            row = cursor.fetchall()
            
            for rows in row:
                if rows[0] == 'AP Voucher - Purchases':
                    settings.APPurchases = rows[1]
                elif rows[0] == 'Official Receipts - Cash in Bank':
                    sORCash = rows[1]
                elif rows[0] == 'Official Receipts - Receivables':
                    sORReceivables = rows[1]
                elif rows[0] == 'Official Receipts - Cash Advance':
                    sORCA = rows[1]
                elif rows[0] == 'Official Receipts - Gift Check':
                    sORGC = rows[1]
                elif rows[0] == 'Official Receipts - Others':
                    sOROthers = rows[1]
                elif rows[0] == 'Check Voucher - Cash':
                    sCVCash = rows[1]
                elif rows[0] == 'Check Voucher - Payables':
                    sCVPayables = rows[1]
                elif rows[0] == 'Check Voucher - Cash Advance':
                    sCVCAdvance = rows[1]
                elif rows[0] == 'Check Voucher - PPE Title':
                    sCVPPE = rows[1]
                elif rows[0] == 'Check Voucher - Others':
                    sCVOthers = rows[1]
                elif rows[0] == 'Charge Invoice - Cash in Bank':
                    sCICash = rows[1]
                elif rows[0] == 'Charge Invoice - Receivables':
                    sCIRecievables = rows[1]
                elif rows[0] == 'AP Voucher  - Expenses':
                    sAPExoenses = rows[1]
                elif rows[0] == 'AP Voucher  - PPE Title':
                    sAPPPE = rows[1]
                elif rows[0] == 'AP Voucher  - Others':
                    sAPOthers = rows[1]
                elif rows[0] == 'Net income or loss forwarding':
                    sAPNet = rows[1]
                    
            # print('Global',sORCash)
            cursor.close
        with connection.cursor() as cursor:
            cursor.execute("SELECT ul_code,unit_description FROM tbl_unit_location")
            row = cursor.fetchall()
            columns = [col[0] for col in cursor.description]

# Loop through the rows and create a dictionary for each row
            for rows in row:
                row_dict = dict(zip(columns, rows))
                locationUnit.append(row_dict)
            print(locationUnit)
            # for rows in row:
            #     locationUnit.append((rows))
        # def get_client_ip(request):
        # # Get the client's IP address from the request's META attribute
        # # 'HTTP_X_FORWARDED_FOR' is used to handle cases when the app is behind a proxy or load balancer.
        # # 'REMOTE_ADDR' contains the client's IP when not behind a proxy.
        #     client_ip = request.META.get('HTTP_X_FORWARDED_FOR', '') or request.META.get('REMOTE_ADDR', '')
        #     print('IP Address:',client_ip)
        #     return HttpResponse(f"Your IP address is: {client_ip}")         
            
            
            

        
          
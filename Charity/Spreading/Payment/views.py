from django.shortcuts import render
import logging
import requests

from Payment import mpesa

# Create your views here.

logger = logging.getLogger(__name__)


# @login_required
# initiating donation
def Donation(request):
    if request.method =="POST":
        phone=request.POST["phone"]
        amount = request.POST["amount"]
        logger.info(f'{phone} {amount}')
        
        data = {    
                "BusinessShortCode": mpesa.get_business_shortcode(),
                "Password": mpesa.generate_password,    
                "Timestamp":mpesa.get_current_timestamp,    
                "TransactionType": "CustomerPayBillOnline",    
                "Amount": amount,    
                "PartyA":mpesa.get_business_shortcode,    
                "PartyB":phone,    
                "PhoneNumber":phone,    
                "CallBackURL": mpesa.get_callback_url,    
                "AccountReference":"656404",    
                "TransactionDesc":"Donation"
            }
        headers = mpesa.generate_request_headers
        resp = requests.post(mpesa.get_payment_url, json=data, headers=headers)    
        logger.info(resp.json())
    return render(request, "Donate.html")

def callback(request):
    pass
    return None
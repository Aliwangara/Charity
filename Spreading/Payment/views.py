import json

from django.http import HttpResponse
from django.shortcuts import render
import logging
import requests

from Payment import mpesa
from django.views.decorators.csrf import csrf_exempt

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
                "Password": mpesa.generate_password(),    
                "Timestamp":mpesa.get_current_timestamp(),    
                "TransactionType": "CustomerPayBillOnline",    
                "Amount": amount,    
                "PartyA":phone,    
                "PartyB":mpesa.get_business_shortcode(),    
                "PhoneNumber":phone,    
                "CallBackURL": mpesa.get_callback_url(),    
                "AccountReference":"656404",    
                "TransactionDesc":"Donation"
            }
        headers = mpesa.generate_request_headers()
        resp = requests.post(mpesa.get_payment_url(), json=data, headers=headers)  
          
        logger.info(resp.json())
        json_resp = resp.json()
        if "ResponseCode" in json_resp:
                code =json_resp["ResponseCode"]
                if code =="0":
                    mid = json_resp["MerchantRequestID"]
                    cid = json_resp["CheckoutRequestID"]
                    logger.info(f"{mid} {cid}")
                else:
                    logger.error(f"Error while Initiating STK push {code}")
        elif "errorCode" in json_resp:
            errorCode = json_resp["errorCode"]
            logger.error(f"Error with errorCode: {errorCode}")
        
    return render(request, "Donate.html")





def callback(request):
    result=json.loads(request.body)
    logger.info(result)
    mid = result["Body"] ["stkCallback"] ["MerchantRequestID"]
    cid = result["Body"] ["stkCallback"] ["CheckoutRequestID"]
    code = result["Body"] ["stkCallback"] ["ResultCode"]
    
    logger.info(f"from call back result {mid} {cid} {code}")
    return HttpResponse({"message": "successfully received"})



def card(request):
    pass
    return render(request, "CreditCard.html",  )


# ngrok http 8000
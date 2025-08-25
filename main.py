import requests
from getshipping_label import getlabel
from all_emails import sendtracking, send_update, sendlabel
from dotenv import load_dotenv
import os
load_dotenv()
from upload_tracking import upload_tracking
from get_tracking_update import tracking_update
from tracking_script import check_status_changes
#import uploadtracking_excel


# Pseudo Code for Main Function -> bringing all the code together
def get_order_details():
    order = "GS-XXXXX"
    order_num = "12345678" #make sure to get this from webhooks
    shipper_number = "508339"
    shipper_name = "Your Company Name"
    shipper_address1 = "123 Front Street West"
    shipper_city = "Toronto"
    shipper_state = "ON"
    shipper_zip = "M5J2N1"
    shipper_country = "CA"
    shipper_phone = "4165551234"
    recipient_name = "John Doe"
    recipient_address1 = "456 Burrard Street"
    recipient_city = "Vancouver"
    recipient_state = "BC"
    recipient_zip = "V6C3A8"
    recipient_country = "CA"
    recipient_phone = "4165551234"
    package_weight = "5"
    customer_email = "lowenberg1001@gmail.com"
    company_representative_email = "jrlowenberg@icloud.com"
    company_rep = "Jacob"
    return (shipper_number, shipper_name, shipper_address1, shipper_city, shipper_state, shipper_zip, 
        shipper_country, shipper_phone, recipient_name, recipient_address1, recipient_city, recipient_state, 
        recipient_zip, recipient_country, recipient_phone, package_weight, customer_email, company_representative_email, order, order_num, company_rep)

url = os.getenv("url")
priv_key = os.getenv("priv_key")

# UPS OAuth Token
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")

# My Email Password
sender_email = os.getenv("sender_email")
shipper_email = os.getenv("shipper_email")
password = os.getenv("password")

info = get_order_details()
data = getlabel(info, client_id, client_secret)



sendtracking(info[18], info[16], data[2], info[17], sender_email, password)
sendlabel(info[18], data[1], info[19], shipper_email, sender_email, password)
upload_tracking(info[19], info[18], info[17], info[20], info[16], data[2], tracking_update(data[2], client_id, client_secret), url, priv_key)


















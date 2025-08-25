from supabase import create_client
from get_tracking_update import tracking_update
from all_emails import send_update
from dotenv import load_dotenv
import os
load_dotenv()
sender_email = os.getenv("sender_email")
password = os.getenv("password")
priv_key = os.getenv("priv_key")
def check_status_changes(url, priv_key):
    supabase = create_client(url, priv_key)
    response = supabase.table("orders").select("*").execute()
    orders = response.data

    for order in orders:
        new_status = tracking_update(order["tracking_num"])
        order_number = order["order_number"]
        if (new_status != order["status"]):
            supabase.table("orders").update({"status": new_status}).eq("order_number", order_number).execute()
            send_update(order["order_name"], order["customer_email"], order["tracking_num"], new_status, sender_email, password)







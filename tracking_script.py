from supabase import create_client
from get_tracking_update import tracking_update
from all_emails import send_update


# Supabase info
url = "https://esycmlxppdctmvqaxqzu.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVzeWNtbHhwcGRjdG12cWF4cXp1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTU3ODI3MzIsImV4cCI6MjA3MTM1ODczMn0.LEKReBlNkgFQWOUmDh6raRurNxaN9-KkScTP526QlpE"
supabase = create_client(url, key)

# Keep track of previous statuses in a dict
previous_status = {}

def check_status_changes():
    # Fetch all orders (or filter for ones you care about)
    response = supabase.table("orders").select("*").execute()
    orders = response.data

    for order in orders:
        new_status = tracking_update(order["tracking_num"])
        order_number = order["order_number"]
        if (new_status != order["status"]):
            supabase.table("orders").update({"status": new_status}).eq("order_number", order_number).execute()
            send_update(order["order_name"], order["customer_email"], order["tracking_num"], new_status)
            
            
check_status_changes()





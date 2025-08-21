from supabase import create_client
from datetime import datetime, timezone

# Supabase info
url = "https://esycmlxppdctmvqaxqzu.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVzeWNtbHhwcGRjdG12cWF4cXp1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTU3ODI3MzIsImV4cCI6MjA3MTM1ODczMn0.LEKReBlNkgFQWOUmDh6raRurNxaN9-KkScTP526QlpE"
supabase = create_client(url, key)

def upload_tracking(order_number, order_name, customer_email, rep_name, rep_email, tracking, status):
    data = {
        "order_number": order_number,
        "order_name": order_name,
        "customer_email": customer_email,
        "rep_name": rep_name,
        "rep_email": rep_email,
        "tracking_num": tracking,
        "status": status,
        "order_date": datetime.now(timezone.utc).isoformat()  # UTC timestamp string
    }
    response = supabase.table("orders").upsert(data, on_conflict="order_number").execute()
    print(response)


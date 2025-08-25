from supabase import create_client
from datetime import datetime, timezone



def upload_tracking(order_number, order_name, customer_email, rep_name, rep_email, tracking, status, url, priv_key):
    supabase = create_client(url, priv_key)
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



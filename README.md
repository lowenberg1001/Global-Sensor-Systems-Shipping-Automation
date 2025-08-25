# Global Sensor Systems - Shipping Automation & Tracking

This repository contains the **shipping and tracking automation system** for Global Sensor Systems. It manages order processing, label generation, shipment tracking, and email notifications.

## Overview

The system workflow:

1. **Order Retrieval**: Receives order details from webhooks or internal systems.
2. **Shipping Label Creation**: Generates shipping labels via UPS authentication.
3. **Notifications**: Sends shipping label and tracking number to the shipper and customer/representative.
4. **Database Integration**: Stores orders and tracking info in Supabase. Monitors status changes and sends email updates.

## Modules and Files

**1. Authentication and API Integration**

* `get_token.py`: Handles UPS API token retrieval and refresh.

**2. Shipping Label Management**

* `getshipping_label.py`: Creates shipping labels and returns tracking info and shipment metadata.

**3. Email Notifications**

* `all_emails.py`: Sends updates to customers, representatives, and internal shipping staff.

**4. Automatic Tracking Updates**

* `tracking_update.py`: Retrieves shipment status from UPS.
* `tracking_script.py`: Periodically polls tracking data and triggers updates.

**5. Database and Order Updates**

* `upload_tracking.py`: Updates order and shipment info in the database.

**6. Central Orchestration**

* `main.py`: Receives orders, triggers label creation, and sends emails.

## Database (Supabase / Postgres)


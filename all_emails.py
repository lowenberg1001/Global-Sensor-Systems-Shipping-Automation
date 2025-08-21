#send automatic emails through a thrid party that connects to azure - SendGrid
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import base64
import io

def sendtracking(order, customer_email, trackingnum, customer_rep_email):
    sender_email = "lowenberg1001@gmail.com"
    password = "zbgf afea atxt mhwg" 

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = customer_email
    msg["Subject"] = f"Global Sensor Systems Shipping Confirmation, Tracking Number - {trackingnum}"
    msg["Cc"] = customer_rep_email

    # Add HTML body
    body = f"""
    <html>
        <body>
            <p>Hello,</p>
            <p>Your order <b>{order}</b> is about to be shipped.</p>
            <p>
                To track your order, please refer to the tracking number provided: {trackingnum}.
            </p>
            <p>
                You can also track it directly online: 
                <a href="https://www.ups.com/track?tracknum={order}" target="_blank">
                    Track Your Package
                </a>
            </p>
            <p>
                If you have any questions, please call our customer support at XXX-XXX-XXXX.
            </p>
            <p><i>Do not reply to this email.</i></p>
        </body>
    </html>
    """
    msg.attach(MIMEText(body, "html"))
    # Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

def sendlabel(order, label, order_num): #don's email or vennite
    sender_email = "lowenberg1001@gmail.com" # prob not my email
    password = "zbgf afea atxt mhwg" 
    rep_email = "lowenberg1001@gmail.com"
    # Create email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = rep_email
    msg["Subject"] = f"Global Sensor Systems Shipping Label For {order_num}"
    ## maybe add in a bcc for customer reprasentative / someone else
    body = f"""
    <html>
        <body>
            <p>Hello,</p>
            <p>The label for the <b>{order}</b> has been created and provided.</p>
            <p><i>Do not reply to this email.</i></p>
        </body>
    </html>
    """

    msg.attach(MIMEText(body, "html"))
    label_data = base64.b64decode(label)
    part = MIMEBase("application", "gif")  # use "pdf" if label is PDF
    part.set_payload(label_data)
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename=shipping_label.gif")
    msg.attach(part)
    # Connect to Gmail SMTP server and send
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Upgrade to secure connection
        server.login(sender_email, password)
        server.sendmail(sender_email, rep_email, msg.as_string())


def send_update(order, customer_email, tracking_num, status):
    sender_email = "lowenberg1001@gmail.com" # prob not my email
    password = "zbgf afea atxt mhwg" 

    # Create email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = customer_email
    msg["Subject"] = f"Global Sensor Systems Status Update - {status}"
    body = f"""
    <html>
    <body>
        <p>Hello,</p>
        <p>We wanted to let you know that there has been a <strong>status change</strong> in the delivery of your order.</p>
        <ul>
            <li><strong>Order:</strong> [{order}]</li>
            <li><strong>Tracking Number:</strong> [{tracking_num}]</li>
            <li><strong>Current Status:</strong> [{status}]</li>
        </ul>
        <p>Please do not reply to this email. For any questions, contact your representative.</p>
        <p>Thank you,<br>Global Sensor Systems</p>
    </body>
    </html>
    """

    msg.attach(MIMEText(body, "html"))

    # Connect to Gmail SMTP server and send
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Upgrade to secure connection
        server.login(sender_email, password)
        server.sendmail(sender_email, customer_email, msg.as_string())
from gettoken import get_oauth_token
import requests
import base64
import json

def getlabel(info, client_id, client_secret):
    email = info[14]
    shipper = {
        "name": info[1],
        "address1": info[2],
        "city": info[3],
        "state": info[4],
        "postal": info[5],
        "country": info[6],
        "phone": info[7]
    }

    recipient = {
        "name": info[8],
        "attention": "Attn",
        "phone": info[14],
        "address1": info[9],
        "city": info[10],
        "state": info[11],
        "postal": info[12],
        "country": info[13]
    }

    package_weight = info[15]
    shipper_number = info[0]


    oauth_token = get_oauth_token(client_id, client_secret)
    if not oauth_token:
        raise SystemExit("Failed to get OAuth token. Check get_oauth_token()")

    version = "v2403"
    url = f"https://wwwcie.ups.com/api/shipments/{version}/ship" # make sure to use real api endpoint (not sandbox)

    payload = {
        "ShipmentRequest": {
            "Request": {
                "RequestOption": "nonvalidate",
                "TransactionReference": {
                    "CustomerContext": "Test Label Creation"
                },
                "SubVersion": "1801"
            },
            "Shipment": {
                "Description": "Ship WS test",
                "Shipper": {
                    "Name": shipper["name"],
                    "AttentionName": "Shipping Dept",
                    "Phone": {"Number": shipper["phone"]},
                    "ShipperNumber": shipper_number,
                    "Address": {
                        "AddressLine": shipper["address1"],
                        "City": shipper["city"],
                        "StateProvinceCode": shipper["state"],
                        "PostalCode": shipper["postal"],
                        "CountryCode": shipper["country"]
                    }
                },
                "ShipTo": {
                    "Name": recipient["name"],
                    "AttentionName": recipient["attention"],
                    "Phone": {"Number": recipient["phone"]},
                    "Address": {
                        "AddressLine": recipient["address1"],
                        "City": recipient["city"],
                        "StateProvinceCode": recipient["state"],
                        "PostalCode": recipient["postal"],
                        "CountryCode": recipient["country"]
                    }
                },
                "ShipFrom": {
                    "Name": shipper["name"],
                    "Address": {
                        "AddressLine": shipper["address1"],
                        "City": shipper["city"],
                        "StateProvinceCode": shipper["state"],
                        "PostalCode": shipper["postal"],
                        "CountryCode": shipper["country"]
                    }
                },
                "PaymentInformation": {
                    "ShipmentCharge": {
                        "Type": "01",
                        "BillShipper": {
                            "AccountNumber": shipper_number
                        }
                    }
                },
                "Service": {
                    "Code": "14"
                },
                "Package": {
                    "Description": "Package Description",
                    "Packaging": {
                        "Code": "02",
                        "Description": "Customer Supplied Package"
                    },
                    "PackageWeight": {
                        "UnitOfMeasurement": {"Code": "KGS"},
                        "Weight": str(package_weight)
                    }
                }
            },
            "LabelSpecification": {
                "LabelImageFormat": {"Code": "GIF"},
                "HTTPUserAgent": "Mozilla/4.5"
            }
        }
    }

    headers = {
        "Authorization": f"Bearer {oauth_token}",
        "Content-Type": "application/json",
        "transId": "label_test",
        "transactionSrc": "label_script"
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        print(f"⚠️ UPS API error {response.status_code}: {response.text}")
        # Return payload so you can inspect indexing
        return payload, None, None,

    data = response.json()

    # Direct extraction — will raise if structure unexpected
    label_b64 = data["ShipmentResponse"]["ShipmentResults"]["PackageResults"][0]["ShippingLabel"]["GraphicImage"]
    tracking_number = data["ShipmentResponse"]["ShipmentResults"]["PackageResults"][0]["TrackingNumber"]


    return data, label_b64, tracking_number

#upload tracking number to database

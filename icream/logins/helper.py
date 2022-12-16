import requests,random




# form values

username = str()
password = str()
phone = str()
otp_number = str()


# otp

def otp():
    otp_number = random.randint(1001,9999)
    print(otp_number)
    url = "https://www.fast2sms.com/dev/bulkV2"

    payload = f"variables_values={otp_number}&route=otp&numbers={phone}"
    headers = {
        'authorization': "jGMpbHuHOq35AFV26oha2gX3IoLfW2WaS8urwhDQkr1ihpkhKOsMrwAYDzES",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }

    response = requests.request("POST", url, data=payload, headers=headers)


    import http.client

    conn = http.client.HTTPSConnection("d7sms.p.rapidapi.com")

    headers = {
        'Token': "undefined",
        'X-RapidAPI-Key': "151ad70285msh597648138d24f0ep187c02jsn57c0c507846e",
        'X-RapidAPI-Host': "d7sms.p.rapidapi.com"
        }

    conn.request("POST", "/messages/v1/balance", headers=headers)
    
    def otpsend():
        return otp_number
        
    return otpsend




# order details 

email = str()
state = str()
pincode = str()
address = str()
phone = str()
radio = str()

payment_type = str()
address_id = str()


order_id = list()

total = int()
coupontotal = int()
couponid = int()

orderpack_id = int()
from flask import Flask, request, make_response
import time
from Database import Database

app = Flask(__name__)


@app.route('/qoala/api', methods=['GET', 'POST'])
def qoala_api_post_request():
    start_time = time.time()
    db_obj = Database()
    end_time = time.time()
    print("Connected to DB : ", end_time - start_time)
    auth = request.authorization
    if auth and auth.username == 'qoala_admin' and auth.password == 'admin_password':
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            json = request.json
            json_length = len(json["data"])
            order_id = json["order_id"]
            print(json_length, order_id)
            if json_length >= 1:
                status = "Success"
            else:
                status = "Failed"
            for json in json["data"]:
                id = json['id']
                identity_number = json['identity_number']
                postal_code = json['postal_code']
                registration_number = json['registration_number']
                sum_coverage = json['sum_coverage']
                db_obj.insert_order_details(order_id, id, identity_number, registration_number, postal_code,
                                            sum_coverage)
            db_obj.insert_quotation_orders(order_id, json_length)
            return {"Status: ": status,
                    "Count success: ": json_length
                    }

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


if __name__ == '__main__':
    app.run(debug=True)

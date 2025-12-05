#!/usr/bin/env python3

from flask import Flask

# Sample contract data
contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]

# Sample customer data
customers = ["bob", "bill", "john", "sarah"]

app = Flask(__name__)

# -----------------------------------------------------
# /contract/<id>  → return contract info as string
# -----------------------------------------------------


@app.route("/contract/<int:id>")
def get_contract(id):
    """
    Returns contract information string if the ID matches.
    If not found → 404 response with plain text.
    """
    for contract in contracts:
        if contract["id"] == id:
            return contract["contract_information"], 200

    return "Contract not found", 404


# -----------------------------------------------------
# /customer/<customer_name>  → return 204 or 404
# -----------------------------------------------------
@app.route("/customer/<customer_name>")
def get_customer(customer_name):
    """
    Confirms a customer exists without returning sensitive data.
    If found → return 204 (No Content)
    If not found → 404
    """
    if customer_name.lower() in customers:
        return "", 204

    return "Customer not found", 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)

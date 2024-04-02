# Simple Bank Flask API README

This Flask API was developed as part of a homework assignment for [PUCPR (Pontifical Catholic University of Paraná)](https://pucpr.br). It serves as a simple bank account management system.

## Requirements

- Python 3

## How to run

> `$ py -3 -m venv .venv` \
> `$ .venv\Scripts\activate`\
> `$ pip install Flask` \
> `$ flask --app api run` 


## Endpoints

### 1. `GET /<account_id>`

- **Description:** Fetches the balance of the specified account.
- **Parameters:**
  - `account_id` (str): The ID of the account to fetch balance for.
- **Response:** 
  - Status Code: 200 OK
  - Content: JSON object containing the balance of the account.
  - Status Code: 404 Not Found (if the account does not exist)

### 2. `PUT /<account_id>/<deposit_value>`

- **Description:** Deposits funds into the specified account.
- **Parameters:**
  - `account_id` (str): The ID of the account to deposit funds into.
  - `deposit_value` (int): The amount of funds to deposit.
- **Response:** 
  - Status Code: 200 OK
  - Content: JSON object containing the new balance of the account after deposit.
  - Status Code: 404 Not Found (if the account does not exist)

### 3. `PATCH /<account_id>/<withdraw_value>`

- **Description:** Withdraws funds from the specified account.
- **Parameters:**
  - `account_id` (str): The ID of the account to withdraw funds from.
  - `withdraw_value` (int): The amount of funds to withdraw.
- **Response:** 
  - Status Code: 200 OK
  - Content: JSON object containing the new balance of the account after withdrawal.
  - Status Code: 400 Bad Request (if there are insufficient funds)
  - Status Code: 404 Not Found (if the account does not exist)

### 4. `POST /<account_id>`

- **Description:** Creates a new account with the specified ID.
- **Parameters:**
  - `account_id` (str): The ID of the account to create.
- **Response:** 
  - Status Code: 201 Created
  - Content: Confirmation message for account creation.
  - Status Code: 400 Bad Request (if the account already exists)

## College Information

This API was developed as part of a homework assignment for [PUCPR (Pontifical Catholic University of Paraná)](https://pucpr.br), a prestigious higher education institution located in Curitiba, Brazil.

## Disclaimer

This API is intended for educational purposes only. It may not be suitable for production use without further development and testing.

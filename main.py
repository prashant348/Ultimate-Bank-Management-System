from random import randint
import json
from datetime import datetime
import os

# Define dynamic paths for JSON files
USERS_JSON_PATH = os.path.join(os.path.dirname(__file__), "users.json")
USERS_HIST_JSON_PATH = os.path.join(os.path.dirname(__file__), "users_hist.json")


class Account():


    def __init__(self, name: str, phone: int, email: str):
        
        self.__user_name = name
        self.__user_phone = phone
        self.__user_email = email 


        try:
            with open(USERS_JSON_PATH, "r") as f:
                data = json.load(f)
                if self.__user_email in data.keys():
                    o = data[self.__user_email]
                    self.__user_acc_num = o["acc_num"]
                    self.__user_acc_pin = o["acc_pin"]
                    self.__balance = o["balance"]
                    
                else:
                    self.__user_acc_num = None
                    self.__user_acc_pin = None
                    self.__balance = None
        except:
            with open(USERS_JSON_PATH, "x") as f:
                json.dump({}, f, indent=4)
            print("users.json created")

        try:
            with open(USERS_HIST_JSON_PATH, "r") as f:
                pass
        except:
            with open(USERS_HIST_JSON_PATH, "x") as f:
                json.dump({}, f, indent=4)
            print("users_hist.json created")


    @property
    def user_name(self):
        return self.__user_name

    @property
    def user_email(self):
        return self.__user_email
    
    @property
    def user_phone(self):
        return self.__user_phone

    @property
    def balance(self):
        return self.__balance

    @property
    def user_acc_num(self):
        return self.__user_acc_num
    
    @property
    def user_acc_pin(self):
        return self.__user_acc_pin

    def create_acc(self, initial_balance=0):
        if self.__user_email.endswith("@gmail.com") or self.__user_email.endswith("@email.com") and len(str(self.__user_phone)) == 10:
            try:
                # try to load/open users.json if it exists
                with open(USERS_JSON_PATH, "r") as f:
                    data = json.load(f)
                # checking if users.json is empty
                if data == {}:
                    self.__user_acc_num = randint(100000, 999999)
                    self.__user_acc_pin = randint(1000, 9999)
                    self.__balance = initial_balance
                    if initial_balance>=0:
                        user_detail = {
                        "name": self.__user_name,
                        "phone": self.__user_phone,
                        "acc_num": self.__user_acc_num,
                        "acc_pin": self.__user_acc_pin,
                        "balance": self.__balance
                                    }
                        
                        data[self.__user_email] = user_detail
                        with open(USERS_JSON_PATH,"w") as f:
                            json.dump(data, f, indent=4)
                        print("Account created successfully!")
                    else:
                        print("Invalid initial balance!")
                #  if users.json is not empty
                else:
                    # checking if account already exists via user_email
                    if self.__user_email in data.keys():
                        print("Account already exists!")
                    
                    else:
                        # generating account number and pin
                        self.__user_acc_num = randint(100000, 999999)
                        self.__user_acc_pin = randint(1000, 9999)
                        self.__balance = initial_balance
                        if initial_balance>=0:
                            # checking if generated pin or account number is already in use 
                            found = False
                            for v in data.values():
                                if v["acc_pin"] == self.__user_acc_pin or v["acc_num"] == self.__user_acc_num:
                                    found = True
                                    print("System Faliure: Account could not be created due to some internal interuption")
                                    break

                            if not found:
                                # now checking if phone number is already linked to an account
                                found_p = False 
                                for v1 in data.values():
                                    if v1["phone"] == self.__user_phone:
                                        found_p = True
                                        print(f"Phone number {self.__user_phone} already linked to an account")

                                if not found_p:
                                    user_detail = {
                                        "name": self.__user_name,
                                        "phone": self.__user_phone,
                                        "acc_num": self.__user_acc_num,
                                        "acc_pin": self.__user_acc_pin,
                                        "balance": self.__balance
                                    }
                                        
                                    data[self.__user_email] = user_detail
                                    with open(USERS_JSON_PATH, "w") as f:
                                        json.dump(data, f, indent=4)
                                    print("Account created successfully")
                        else:
                            print("Invalid initial balance!")
            # printing exception if users.json does not exist
            except FileNotFoundError as e:
                print(e)

        else:
            print("Invalid mail address or may be the phone number is of not 10 characters")


    def delete_acc(self, pin: int):
        try:
            with open(USERS_JSON_PATH, "r") as f:
                data = json.load(f)
            found = False
            for k, v in data.items():
                if k == self.__user_email:
                    found = True
                    if pin == v["acc_pin"]:

                        with open(USERS_JSON_PATH, "r") as f1:
                            data1 = json.load(f1)

                            acc_to_del = [k1 for k1, v1 in data1.items() if v1["acc_num"] == v["acc_num"]]
                            for i in acc_to_del:
                                del data1[i]

                        with open(USERS_JSON_PATH, "w") as f:
                            json.dump(data1, f, indent=4)

                        # deleting history of the user from users_hist.json file
                        with open(USERS_HIST_JSON_PATH, "r") as f2:
                            data2 = json.load(f2)

                            acc_hist_to_del = [k2 for k2, v2 in data2.items() if k2.startswith(self.__user_email)]
                            for i in acc_hist_to_del:
                                del data2[i]

                        with open(USERS_HIST_JSON_PATH,"w") as f3:
                            json.dump(data2, f3, indent=4)
                    
                        print("Account deleted successfully")
                    else:
                        print("Invalid pin")
                    break # stop after finding the user

            if not found:
                print("Account not found")
                
        except FileNotFoundError as e:
            print(e)

        

    def deposite(self, amount: int|float, pin: int):

        try:
            with open(USERS_JSON_PATH, "r") as f:
                data = json.load(f)
            found = False
            for k, v in data.items():
                if k == self.__user_email:
                    found = True
                    if pin == v["acc_pin"]:

                        with open(USERS_JSON_PATH, "r") as f1:
                            data1 = json.load(f1)
                            
                            for k1, v1 in data1.items(): 
                                if k1 == self.__user_email:
                                    try:
                                        if amount < 0:
                                            print(f"Invalid amount!")
                                        else:
                                            updated_balance = v1["balance"] + amount

                                            data1[self.__user_email] = {
                                                "name": v1["name"], 
                                                "phone": v1["phone"], 
                                                "acc_num": v1["acc_num"], 
                                                "acc_pin": v1["acc_pin"], 
                                                "balance": updated_balance
                                                }
                                            
                                            with open(USERS_JSON_PATH, 'w') as f:
                                                json.dump(data1, f, indent=4)
                                            self.__balance = updated_balance

                                            # creating action details and saving it as history in users_hist.json file
                                            now = datetime.now()
                                            current_time = now.strftime("%H:%M:%S %p") # type of current_time is string
                                            current_date = now.strftime("%d-%m-%Y") # type of current_date is string
                                            hist = {
                                                "User_name": v1["name"],
                                                "User_acc_num": v1["acc_num"],
                                                "Action_Type": "Deposite",
                                                "Amount_Deposited": amount,
                                                "Date": current_date,
                                                "Time": current_time
                                            }
                                            with open(USERS_HIST_JSON_PATH, "r") as f2:
                                                data2 = json.load(f2)
                                            i = 1
                                            while i>= 1:
                                                key = self.__user_email + f" -Deposite action: {i}"
                                                if key in data2.keys():
                                                    pass
                                                else:
                                                    data2[key] = hist
                                                    with open(USERS_HIST_JSON_PATH, "w") as f3:
                                                        json.dump(data2, f3, indent=4)
                                                    print(f"\nbalance updated successfully!\nAmount deposited: {amount}\nYour current balance: {updated_balance}")
                                                    break
                                                i += 1
                                    except:
                                        print(f"Balance amount should must be a number, not like '{amount}'")
                    
                    else:
                        print("Please enter the valid pin!")
                    break # stop after finding the user

            if not found:
                print("Account not found")
        except FileNotFoundError as e:
            print(e)
            
                                                
    def withdraw(self, amount: int|float, pin: int):

        try: 
            with open(USERS_JSON_PATH) as f:
                data = json.load(f)
            found = False
            for k, v in data.items():
                if k == self.__user_email:
                    found = True
                    if pin == v["acc_pin"]:
                        with open(USERS_JSON_PATH, "r") as f1:
                            data1 = json.load(f1)

                            for k1, v1 in data1.items():
                                if k1 == self.__user_email:
                                    try:
                                        if amount < 0:
                                            print(f"Invalid amount!")
                                        else:
                                            if amount > v1["balance"]:
                                                print("Can't withdraw, withdrawel amount exceeded!")
                                                print(f"The maximum amount you can withdraw: {v1['balance']}")
                                            else:
                                                updated_balance = v1["balance"] - amount

                                                data1[self.__user_email] = {
                                                    "name": v1["name"], 
                                                    "phone": v1["phone"], 
                                                    "acc_num": v1["acc_num"], 
                                                    "acc_pin": v1["acc_pin"], 
                                                    "balance": updated_balance
                                                }
                                                 

                                                with open(USERS_JSON_PATH, "w") as f:
                                                    json.dump(data1, f, indent=4)
                                                self.__balance = updated_balance

                                                now = datetime.now()
                                                current_time = now.strftime("%H:%M:%S %p") # type of current_time is string
                                                current_date = now.strftime("%d-%m-%Y") # type of current_date is string
                                                
                                                hist = {
                                                    "User_name": v1["name"],
                                                    "User_acc_num": v1["acc_num"],
                                                    "Action_Type": "Withdraw",
                                                    "Amount_Withdraw": amount,
                                                    "Date": current_date,
                                                    "Time": current_time
                                                }
                                                with open(USERS_HIST_JSON_PATH, "r") as f2:
                                                    data2 = json.load(f2)
                                                i = 1
                                                while i>= 1:
                                                    key = self.__user_email + f" -Withdaw action: {i}"
                                                    if key in data2.keys():
                                                        pass
                                                    else:
                                                        data2[key] = hist
                                                        with open(USERS_HIST_JSON_PATH, "w") as f3:
                                                            json.dump(data2, f3, indent=4)
                                                        print(f"\nbalance updated successfully!\nAmount Withdrawed: {amount}\nYour current balance: {updated_balance}")
                                                        break
                                                    i += 1
                                    except:
                                        print(f"Balance amount should must be a number, not like {amount}")
                    else:
                        print("Please enter the valid pin!")
                    break
            if not found:
                print("Account not found")
        except FileNotFoundError as e:
            print(e)
    

    def load_user_details(self, pin: int):
        try:
            with open(USERS_JSON_PATH, "r") as f:
                data = json.load(f)
            found = False
            for k, v in data.items():
                if k == self.__user_email:
                    found = True
                    if pin == v["acc_pin"]:

                        print("\nAccount details:")   
                        print(f"name: {v["name"]}")
                        print(f"phone number: {v['phone']}")
                        print(f"account number: {v['acc_num']}")
                        print(f"account pin: {v['acc_pin']}")
                        print(f"balance: {v['balance']}")

                    else:
                        print("Invalid pin")
            if not found:
                print("Account not found")
        except FileNotFoundError as e:
            print(e)



    def send_to(self, amount: int, your_pin: int, receiver_object):
        try:
            with open(USERS_JSON_PATH, "r") as f:
                data = json.load(f)
            if self.__user_email in data.keys():
                if your_pin == self.__user_acc_pin:
                    if 0 < amount <= self.__balance:
                        updated_sender_balance = self.__balance - amount
                        data[self.__user_email] = {
                            "name": self.__user_name,
                            "phone": self.__user_phone,
                            "acc_num": self.__user_acc_num,
                            "acc_pin": self.__user_acc_pin,
                            "balance": updated_sender_balance
                        }

                        updated_receiver_balance =  receiver_object.__balance + amount

                        data[receiver_object.__user_email] = {
                            "name": receiver_object.__user_name,
                            "phone": receiver_object.__user_phone,
                            "acc_num": receiver_object.__user_acc_num,
                            "acc_pin": receiver_object.__user_acc_pin,
                            "balance": updated_receiver_balance
                        }
                        
                        #updating balance attributes in memory
                        self.__balance = updated_sender_balance
                        receiver_object.__balance = updated_receiver_balance

                        with open(USERS_JSON_PATH, "w") as f:
                            json.dump(data, f, indent=4)

                        # saving as history in users_hist.json file
                        with open(USERS_HIST_JSON_PATH, "r") as f1:
                            data1 = json.load(f1)

                        now = datetime.now()
                        current_time = now.strftime("%H:%M:%S %p")
                        current_date = now.strftime("%d-%m-%Y")

                        hist = {
                            "Sender_User_name": self.__user_name,
                            "Receiver_User_name": receiver_object.__user_name,
                            "Action_Type": "Send",
                            "Amount_sent": amount,
                            "Date": current_date,
                            "Time": current_time
                        }

                        i = 1
                        while 1>=1:
                            key = self.__user_email + f" -Send action: {i}"
                            if key in data1.keys():
                                pass
                            else:
                                data1[key] = hist
                                with open(USERS_HIST_JSON_PATH, "w") as f1:
                                    json.dump(data1, f1, indent=4)
                                break
                            i += 1
                        
                        print(f"Amount sent successfully!\nAmount sent: {amount}\nYour current balance: {self.__balance}")
                    elif amount < 0:
                        print("Invalid amount!")
                    else:
                        print("You don't have enough balance to sent!")
                else:
                    print("Please enter the valid pin!")
            else:
                print("Sender's account does not exist")
        except Exception as e:
            print(e)
            
                    

u1 = Account("prashant", 1234567890, "prashant999@gmail.com")
u2 = Account("krishna", 9876543210, "krishna111@gmail.com")
u3 = Account("shivam", 1234598760, "shivam228@gmail.com")

u1.create_acc()
u2.create_acc(200)
u3.create_acc()

# u2.send_to(100, 2781, u1)

# u1.deposite(100, 6503)
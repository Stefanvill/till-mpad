import requests
import os
import time
import json
import tkinter as tk


def append_to_json_file(data):
    try:
        with open("data.json", "r") as file:
            existing_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    existing_data.append(data)

    with open("data.json", "w") as file:
        json.dump(existing_data, file, indent=4)

def update_json_file(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def save_login_credentials():
    root = tk.Tk()
    root.title("Login credentials")

    url_label = tk.Label(root, text="URL:")
    url_label.pack()
    url_entry = tk.Entry(root)
    url_entry.pack()

    username_label = tk.Label(root, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    password_label = tk.Label(root, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(root)
    password_entry.pack()

    def append_credentials():
        url = url_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        data = {"url": url, "username": username, "password": password}
        append_to_json_file(data)

        root.destroy()

    save_button = tk.Button(root, text="Save", command=append_credentials)
    save_button.pack()

    root.mainloop()

def change_login_credentials():
    root = tk.Tk()
    root.title("Change login credentials")

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    url_label = tk.Label(root, text="URL:")
    url_label.pack()
    url_listbox = tk.Listbox(root)
    url_listbox.pack()

    for item in data:
        url_listbox.insert(tk.END, item['url'])

    def select_url():
        if url_listbox.curselection():
            selected_url = url_listbox.get(url_listbox.curselection())

            for item in data:
                if item['url'] == selected_url:
                    item['username'] = username_entry.get()
                    item['password'] = password_entry.get()
                    break

            update_json_file(data)
            root.destroy()

    username_label = tk.Label(root, text="New Username:")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    password_label = tk.Label(root, text="New Password:")
    password_label.pack()
    password_entry = tk.Entry(root)
    password_entry.pack()

    select_button = tk.Button(root, text="Select", command=select_url)
    select_button.pack()

    root.mainloop()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    print("1. Save login credentials\n2. Change login credentials\n3. Print login credentials\n4. Print fuel prices\n5. Exit")
    try:
        user_input = int(input("Choose an option: "))
    except ValueError:
        print("Please select a number between 1 and 5")
        time.sleep(3)
        continue

    if user_input == 1:
        save_login_credentials()
    elif user_input == 2:
        change_login_credentials()
    elif user_input == 3:
        def print_login_credentials():
            root = tk.Tk()
            root.title("Login credentials")

            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                data = []

            url_label = tk.Label(root, text="URL:")
            url_label.pack()

            url_listbox = tk.Listbox(root)
            url_listbox.pack()

            for item in data:
                url_listbox.insert(tk.END, item['url'])

            def show_credentials():
                if url_listbox.curselection():
                    selected_url = url_listbox.get(url_listbox.curselection())

                    for item in data:
                        if item['url'] == selected_url:
                            username = item['username']
                            password = item['password']
                            break

                    username_label = tk.Label(root, text=f"Username: {username}")
                    username_label.pack()

                    password_label = tk.Label(root, text=f"Password: {password}")
                    password_label.pack()

            show_button = tk.Button(root, text="Show", command=show_credentials)
            show_button.pack()

            root.mainloop()

        print_login_credentials()
    elif user_input == 4:
        response = requests.get("https://henrikhjelm.se/api/getdata.php?lan=stockholms-lan")
        answer = response.json()

        def show_fuel_prices():
            root = tk.Tk()
            root.title("Fuel Prices")

            fuel_prices = {
                "Cirkle K vikdalsvägens Diesel": answer['stockholmslan_Circle_K_NackaVikdalsvagen_41__diesel'],
                "St1 Nacka Saltsjöbaden Repvägen 2 Diesel": answer['stockholmslan_St1_NackaSaltsjobaden_Repvagen_2__diesel'],
                "Circle K Nacka Solsidevägen 2 Saltsjöbaden Diesel": answer['stockholmslan_Circle_K_NackaSolsidevagen_2_Saltsjobaden__diesel'],
                "Preem Nacka Klintvägen 1 Saltsjö-Boo Diesel": answer['stockholmslan_Preem_NackaKlintvagen_1_Saltsjo_Boo__diesel'],
                "OKQ8 Nacka Värmdövägen 79 Diesel": answer['stockholmslan_OKQ8_NackaVarmdovagen_79__diesel'],
                "Ingo Nacka Skvaltans väg 11 Diesel": answer['stockholmslan_Ingo_NackaSkvaltans_vag_11__diesel'],
                "OKQ8 Nacka Kanholmsvägen 2 Saltsjö-Boo Diesel": answer['stockholmslan_OKQ8_NackaKanholmsvagen_2_Saltsjoboo__diesel'],
                "Circle K Nacka Dalaröbryggan Diesel": answer['stockholmslan_Circle_K_NackaDalarobryggan__diesel'],
                "Preem Nacka Vattenverksvägen Diesel": answer['stockholmslan_Preem_NackaVattenverksvagen__diesel'],
                "St1 Nacka Saltsjöbaden Repvägen 2 95": answer['stockholmslan_St1_NackaSaltsjobaden_Repvagen_2__95'],
                "Circle K Nacka Solsidevägen 2 Saltsjöbaden 95": answer['stockholmslan_Circle_K_NackaSolsidevagen_2_Saltsjobaden__95'],
                "Preem Nacka Klintvägen 1 Saltsjö-Boo 95": answer['stockholmslan_Preem_NackaKlintvagen_1_Saltsjo_Boo__95'],
                "Ingo Nacka Skvaltans väg 11 95": answer['stockholmslan_Ingo_NackaSkvaltans_vag_11__95'],
                "OKQ8 Nacka Kanholmsvägen 2 Saltsjö-Boo 95": answer['stockholmslan_OKQ8_NackaKanholmsvagen_2_Saltsjoboo__95'],
                "Circle K Nacka Dalaröbryggan 95": answer['stockholmslan_Circle_K_NackaDalarobryggan__95'],
                "Preem Nacka Vattenverksvägen 95": answer['stockholmslan_Preem_NackaVattenverksvagen__95'],
                "Cirkle K vikdalsvägens 95": answer['stockholmslan_Circle_K_NackaVikdalsvagen_41__95']
            }

            def show_price(station):
                price = fuel_prices[station]
                price_label = tk.Label(root, text=f"{station} price is {price} kr")
                price_label.pack()

            for station in fuel_prices.keys():
                station_button = tk.Button(root, text=station, command=lambda s=station: show_price(s))
                station_button.pack()

            root.mainloop()

        show_fuel_prices()
        time.sleep(3)
    elif user_input == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid input, please try again.")
        time.sleep(1)
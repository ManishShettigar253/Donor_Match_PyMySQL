import tkinter as tk
from tkinter import messagebox
from blood_check import check_donation_eligibility
from database import connect_db, insert_record

def submit(con, rgroup_var, dgroup_var, dage_var, dweight_var, vars_dict):
    try:
        rgroup_label = rgroup_var.get()
        dgroup_label = dgroup_var.get()
        dage = int(dage_var.get())
        dweight = int(dweight_var.get())

        health_conditions = {
            'past_one_year': vars_dict['past_one_year'].get() == 'yes',
            'past_six_months': vars_dict['past_six_months'].get() == 'yes',
            'past_three_months': vars_dict['past_three_months'].get() == 'yes',
            'past_one_month': vars_dict['past_one_month'].get() == 'yes',
            'past_48_hours': vars_dict['past_48_hours'].get() == 'yes',
            'past_24_hours': vars_dict['past_24_hours'].get() == 'yes',
            'past_72_hours': vars_dict['past_72_hours'].get() == 'yes',
            'present': vars_dict['present'].get() == 'yes',
            'women_condition': vars_dict['women_condition'].get() == 'yes',
            'free_from_conditions': vars_dict['free_from_conditions'].get() == 'yes'
        }

        result = check_donation_eligibility(dage, dweight, rgroup_label, dgroup_label, health_conditions)
        
        insert_record(con, rgroup_label, dage, dweight, dgroup_label, result)

        messagebox.showinfo("Result", f"Blood {result.lower()}.")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please Fill all the Details.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def close_app(root):
    root.destroy()

def create_gui():
    con = connect_db()
    
    root = tk.Tk()
    root.title("Blood Donation Checker")

    frame = tk.Frame(root, padx=10, pady=10, bg='white')
    frame.place(relx=0.5, rely=0.5, anchor='center')

    blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

    tk.Label(frame, text="BLOOD DONATION CHECKER", font=("Times New Roman", 20, "bold"), bg='white').grid(row=0, column=0, columnspan=2, pady=(0, 20))

    tk.Label(frame, text="Enter Recipient's Blood Group:", font=("Times New Roman", 14), bg='white').grid(row=1, column=0, sticky='e')
    rgroup_var = tk.StringVar(value=blood_groups[0])
    tk.OptionMenu(frame, rgroup_var, *blood_groups).grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Enter Donor's Age:", font=("Times New Roman", 14), bg='white').grid(row=2, column=0, sticky='e')
    dage_var = tk.StringVar()
    tk.Entry(frame, textvariable=dage_var, font=("Times New Roman", 12)).grid(row=2, column=1, pady=5)

    tk.Label(frame, text="Enter Donor's Weight:", font=("Times New Roman", 14), bg='white').grid(row=3, column=0, sticky='e')
    dweight_var = tk.StringVar()
    tk.Entry(frame, textvariable=dweight_var, font=("Times New Roman", 12)).grid(row=3, column=1, pady=5)

    tk.Label(frame, text="Enter Donor's Blood Group:", font=("Times New Roman", 14), bg='white').grid(row=4, column=0, sticky='e')
    dgroup_var = tk.StringVar(value=blood_groups[0])
    tk.OptionMenu(frame, dgroup_var, *blood_groups).grid(row=4, column=1, pady=5)

    questions = [
        ("Rabies treatment or Hepatitis B globulin (1 year)", 'past_one_year'),
        ("Tattoo, piercing, blood transfusion, major surgery, hepatitis contact (6 months)", 'past_six_months'),
        ("Blood donation or malaria treatment (3 months)", 'past_three_months'),
        ("Immunizations (1 month)", 'past_one_month'),
        ("Antibiotics or medications (48 hours)", 'past_48_hours'),
        ("Alcohol (24 hours)", 'past_24_hours'),
        ("Dental work or Aspirin (72 hours)", 'past_72_hours'),
        ("Cough, flu, sore throat, common cold", 'present'),
        ("Pregnant or breastfeeding (women)", 'women_condition'),
        ("Diabetes, heart disease, high BP, cancer, blood issues, unexplained symptoms", 'free_from_conditions')
    ]

    vars_dict = {}

    for i, (text, var_name) in enumerate(questions):
        tk.Label(frame, text=text, font=("Times New Roman", 12), bg='white', wraplength=500, justify='left').grid(row=5 + i, column=0, columnspan=2, sticky='w', pady=5)
        var = tk.StringVar(value='no')
        vars_dict[var_name] = var
        tk.Radiobutton(frame, text="Yes", variable=var, value='yes', font=("Times New Roman", 12), bg='white').grid(row=5 + i, column=2)
        tk.Radiobutton(frame, text="No", variable=var, value='no', font=("Times New Roman", 12), bg='white').grid(row=5 + i, column=3)

    tk.Button(frame, text="Check", command=lambda: submit(con, rgroup_var, dgroup_var, dage_var, dweight_var, vars_dict), font=("Times New Roman", 14, "bold"), bg='lightblue').grid(row=5 + len(questions), column=0, pady=20)
    tk.Button(frame, text="Close", command=lambda: close_app(root), font=("Times New Roman", 14, "bold"), bg='lightblue').grid(row=5 + len(questions), column=1, pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()

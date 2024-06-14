def check_donation_eligibility(dage, dweight, rgroup_label, dgroup_label, health_conditions):
    compatibility_map = {
        "A+": {"A+", "A-", "O+", "O-"},
        "A-": {"A-", "O-"},
        "B+": {"B+", "B-", "O+", "O-"},
        "B-": {"B-", "O-"},
        "AB+": {"A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"},
        "AB-": {"A-", "B-", "AB-", "O-"},
        "O+": {"O+", "O-"},
        "O-": {"O-"}
    }

    if not (18 <= dage <= 60 and dweight >= 45 and dgroup_label in compatibility_map.get(rgroup_label, set())):
        return "Cannot Donate"

    for condition, answer in health_conditions.items():
        if answer:
            return "Cannot Donate"
    return "Can Donate"

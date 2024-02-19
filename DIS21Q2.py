month_days = [('January', [31]), ('February', [28, 29]), ('March', [31]),
              ('April', [30]), ('May', [31]), ('June', [30]), ('July', [31]),
              ('August', [31]), ('September', [30]), ('October', [31]),
              ('November', [30]), ('December', [31])]

def days_in_month(month, lst):
    for m, days in lst:
        if m == month:
            return (m, days)
    print("Month not found")
    return None

result = days_in_month("January", month_days)
print(result)

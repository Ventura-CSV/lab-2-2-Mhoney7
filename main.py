def main():
    workhours = int(input('50'))
    reg_hours = 40
    reg_rate = 18.25
    ov_rate = 27.78

   ##################################################
   # Code your program here
   ##################################################
    # overtime = workhours - reg_hours
    # overtime_wage = overtime * ov_rate
    # regular_wage = reg_hours * reg_rate
    # total_wage = regular_wage + overtime_wage

workhours = 50
reg_hours = 40
reg_rate = 18.2
ov_rate = 27.78

overtime_hours = (workhours - reg_hours)
overtime_wage = (overtime_hours * ov_rate)
regular_wage = (reg_hours * reg_rate)

total_wage = (regular_wage + overtime_wage)


def main():
    print(f"Regular Charge: {regular_wage:.2f}")
    print(f"Overtime Charge: {overtime_wage:.2f}")
    print(f"Total wage : {total_wage:.2f}")

   ##################################################
   # Do not delete the return statement
   ##################################################
    return regular_wage, overtime_wage, total_wage


if __name__ == '__main__':
    main()

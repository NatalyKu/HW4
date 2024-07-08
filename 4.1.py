from pathlib import Path

def total_salary(path):
    total = 0
    num_empl = 0
    try:    
        with open (path, 'r') as salary:
            for el in salary:
                koma =int(el.find(',', 0))+1
                salary= el[koma:]
                num_empl = num_empl + 1
                total += int(salary)
                avg_salary = (total/num_empl)
                avg_salary = round(avg_salary)
    except FileNotFoundError:
        (print (f'Check your {path}'))
    return(total, avg_salary)

total, avg_salary = total_salary('./HW4/file.txt') 
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {avg_salary}")
         
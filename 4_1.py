from pathlib import Path

def total_salary(path):
    list_salary = []
    total = 0
    num_empl = 0
    try:    
        with open (path, 'r') as salary:
            try:
                for line in salary:
                    list_salary = line.split(',')[1]
                    num_empl = num_empl + 1
                    total += int(line.split(',')[1])
                    avg_salary = (total/num_empl)
            except ZeroDivisionError:
                return "There are no salary data in the file"
    except FileNotFoundError:
        (print (f'Check your path {path}'))
    return(total, avg_salary)

total, avg_salary = total_salary('./HW4/file.txt') 
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {avg_salary}")
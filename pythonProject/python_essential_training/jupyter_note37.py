
# CSV
# Reading
import csv

# with open('10_02_us.csv','r') as f:
#     reader = csv.reader(f,delimiter='\t')
#     for row in reader:
#         print(row)
# type(reader)


with open('10_02_us.csv','r') as f:
    reader = csv.reader(f,delimiter='\t')
    next(reader)
    next(reader)
    for row in reader:
        print(row)


with open('10_02_us.csv','r') as f:
     reader = list(csv.reader(f,delimiter='\t'))
     for row in reader[1:]:
         print(row)


with open('10_02_us.csv','r') as f:
    reader = csv.DictReader(f,delimiter='\t')
    for row in reader:
        print(row)


# Filtering Data

# with open('10_02_us.csv','r') as f:
#      data = list(csv.DictReader(f,delimiter='\t'))
#
# primes = []
# for number in range(2,99999):
#     for fact in range(2, int(number**0.5)):
#         if number % facter == 0:
#             break
#         else:
#             primes.append(number)
# data = [row for row in data if int (row['postal code']) in primes and row ['state code'] == 'MA']
# len(data)



# Writing

with open('10_02_ma_prime.csv','w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow([row['place name'],row['country']])


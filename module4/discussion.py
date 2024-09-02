transactions = [3.40, 5.20, 100.23, 45.56]

rounded_transactions = []
for transaction in transactions:
    rounded_transactions.append(round(transaction))

print(rounded_transactions)

for index in range(0, len(transactions)):
    transaction = transactions[index]
    print(f"transaction: {transaction}")


def do_work():
    print("do work")
    return True

success = False
while not success:
    success = do_work()

while True:
    if do_work():
        break  # success!

max_attempts = 3
for _ in range(max_attempts):
    if do_work():
        break

transactions = [3.40, 5.20, 100.23, 45.56]
print(list(map(round, transactions)))

rounded_transactions = list(map(round, transactions))



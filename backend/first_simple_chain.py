import hashlib
import secrets
import random
import names

class Transaction:

    def __init__(self, sender, reciever, amount):
        self.sender = sender
        self.reciever = reciever
        self.amount = amount
        self.transaction_id = self.generateid()

    def transaction_info(self):
        return f'{self.sender.get_name()} (ID:{self.sender.get_id()}) sent {self.amount} coins to' \
               f' {self.reciever.get_name()} (ID:{self.reciever.get_id()})'

    def generateid(self):
        return secrets.randbelow(99999)

    def get_id(self):
        return self.transaction_id

class Wallet:

    def __init__(self, name):
        self.name = name
        self.id_number = self.generateid()
        self.balance = 0

    def generateid(self):
        return secrets.randbelow(99999)

    def get_id(self):
        return self.id_number

    def get_balance(self):
        return self.balance

    def add_balance(self, amount):
        self.balance = self.balance + amount

    def remove_balance(self, amount):
        self.balance = self.balance - amount

    def get_name(self):
        return self.name

class SingleBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.execute_transaction(transaction_list)
        # 1-3 lines below - hashing strings
        self.transaction_list = []
        for transaction in transaction_list:
            self.transaction_list.append(transaction.transaction_info())

        # 1 line below - hashing objects
        # self.transaction_list = transaction_list
        self.block_data = f"Transactions: {self.transaction_list}, hash of the previous block: {self.previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).digest()  # Digesting because encode() returns an obj

    def execute_transaction(self, transaction_list):
        for transaction in transaction_list:
            transaction.sender.add_balance(transaction.amount)
            transaction.reciever.remove_balance(transaction.amount)
            ###
            '''print(f'{transaction.sender.get_name()} (ID: {transaction.sender.get_id()}) '
                  f'sent {transaction.amount} to {transaction.reciever.get_name()} (ID: {transaction.reciever.get_id()}).'
                  f'Transaction ID is {transaction.get_id()}')'''


class VehicleChain:

    def __init__(self):
        self.chain = []
        self.generate_first_block()

    def generate_first_block(self):
        self.chain.append(SingleBlock(0, [Transaction(Wallet('First sender'), Wallet('First reciever'), 0)]))

    @property
    def last_block(self):
        return self.chain[-1]

    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(SingleBlock(previous_block_hash, transaction_list))

    def display_chain(self):
        print('START OF THE BLOCKCHAIN')
        for i in range(len(self.chain)):
            print('------Beggining of a block inside blockchain-----------------------')
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}")
            print('------Ending of a block inside blockchain-------------------------')
            print('\n')
        print('END OF THE BLOCKCHAIN')





def dummy_people(no_of_people):
    list_of_people = []
    for i in range(no_of_people):
        person = Wallet(names.get_full_name())
        list_of_people.append(person)

    return list_of_people

def dummy_transactions(people, no_of_transactions):
    list_of_transactions = []
    for i in range(no_of_transactions):
        sender = random.choice(people)
        reciever = random.choice(people)
        list_of_transactions.append(Transaction(sender, reciever, random.randrange(0, 100)))

    return list_of_transactions

def rand_examples():
    people = dummy_people(5)
    blockcejn = VehicleChain()
    blockcejn.create_block_from_transaction(dummy_transactions(people, 5))
    blockcejn.display_chain()
    print('---------------------------------')
    print(f'{people[0].get_name()} (ID: {people[0].get_id()}) has {people[0].get_balance()} and '
          f'{people[1].get_name()} (ID: {people[0].get_id()}) has {people[1].get_balance()}')
    blockcejn.create_block_from_transaction([Transaction(people[0], people[1], 100)])
    print(f'Sender has {people[0].get_balance()} and reciever has {people[1].get_balance()}')

    blockcejn.display_chain()

def first_demo():
    print('//////START of the first demo/////////')
    block_chain = VehicleChain()
    sender = dummy_people(1)[0]
    reciever = dummy_people(1)[0]
    random_amount = random.randrange(0,100)

    print(f'Sender {sender.get_name()}  (ID:{sender.get_id()}) has a balance of {sender.get_balance()}')
    print(f'Reciever {reciever.get_name()} (ID:{reciever.get_id()}) has a balance of {reciever.get_balance()}')
    print(f'{sender.get_name()} sends {random_amount} to {reciever.get_name()}')

    our_transaction = Transaction(sender, reciever, random_amount)
    block_chain.create_block_from_transaction([our_transaction])
    block_chain.display_chain()

    print(f'Sender {sender.get_name()} (ID:{sender.get_id()}) has a balance of {sender.get_balance()}')
    print(f'Reciever {reciever.get_name()} (ID:{reciever.get_id()}) has a balance of {reciever.get_balance()}')
    print('//////END of the first demo/////////\n\n')

def second_demo():
    print('//////START of the second demo/////////')
    block_chain = VehicleChain()
    people = dummy_people(5)
    block_chain.create_block_from_transaction(dummy_transactions(people, 5))
    block_chain.display_chain()
    print('//////END of the second demo/////////\n\n')

first_demo()
second_demo()


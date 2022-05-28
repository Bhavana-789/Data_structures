# Function to display hash_table

def display_hash(hash_table):
    for i in range(len(hash_table)):

        print(i, end=" ")

        for j in hash_table[i]:
            print("-->", end=" ")

            print(j, end=" ")

        print()

    # Creating hash_table as


# a nested list.

hash_table = [[] for _ in range(10)]


# Hashing Function to return
# key for every value.

def Hashing(keyvalue):
    return keyvalue % len(hash_table)

def search(keyvalue):
    hash_key = Hashing(keyvalue)
    return hash_table[hash_key]
# Insert Function to add
# values to the hash table

def insert(hash_table, keyvalue, value):
    hash_key = Hashing(keyvalue)

    hash_table[hash_key].append(value)


if __name__ == "__main__":
    insert(hash_table, 10, 'Allahabad')

    insert(hash_table, 25, 'Mumbai')

    insert(hash_table, 20, 'Mathura')

    insert(hash_table, 9, 'Delhi')

    insert(hash_table, 21, 'Punjab')

    insert(hash_table, 21, 'Noida')

    display_hash(hash_table)

    print(search(10))


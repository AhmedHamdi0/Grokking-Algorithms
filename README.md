# Grokking-Algorithms
**Embark on an algorithmic odyssey with the "Grokking Algorithms" by Aditya Y. Bhargava.**

## Chapters Notes
### 1. Introduction to algorithms:
> - Algorithm speed isn't measured in seconds, but in growth of the number of operations.
> - Instead, we talk about how quickly the run time of an algorithm increases as the size of the input increases.
> - **O(log n)** is faster than **O(n)**, but it gets alot faster as the list of items you are searching grows. 

### 2. Selection sort
> - With an **array**, elements are stored right next to each other. 
>   - Arrays allow fast reads **(random access)**.
> - With a **linked list**, elements are strewn all over, and one element stores the address of the next one. 
>   - Linked lists allow fast inserts and deletes.

### 3. Recursion
> **Loops** may achieve a performance gain for your **program**.<br>
> **Recursion** may achieve a performance gain for your **programmer**.

> - When you write a **recursive function**, you have to tell it when to stop recursion.
> - **The recursive case** is when the function calls itself.
> - **The base case** is when the function doesn't call itself again.
> - All function calls **(even recursive)** go onto **the call stack**. 
> - Each call to a recursive function has its own copy of the variables. 
> - You can't access a different function's copy of that variable.

### 4. Quicksort
> - **Divide & conquer (D&C)** is technique to think about a problem.
> - To solve a problem using **divide & conquer**, there are two steps;
>   1. Figure out the base case. This should be the simplest possible case.
>   2. Divider or decrease your problem until it becomes the base case.

> - **Quicksort algorithm** is applying **D&C** by choosing a **pivot** and **partitioning** the items. Here are the steps:
>   1. Pick a pivot.
>   2. Partition the array into two sub-arrays:
>      - elements less than the pivot.
>      - elements greater than the pivot.
>   3. Call quicksort recursively on the two sub-arrays.
> - The performance of **quicksort** heavily depends on the **pivot** you choose. 
>   - If you're implementing **quicksort**, choose a **random** element as the **pivot**.
> - The **average runtime** of quicksort is **O(n log n)** 

> - The **constant** in **Big O** notation can **matter somtimes**.
> - That's why **quicksort** is **faster** than **merge sort**.

### 4. Hash Tables
> - A **hash function** is a function that maps a **value to a key**.
> - The **hash function** must be **consistent** which means consistently **maps the same value to the same key** every time.
> - Put a **hash function** and an **array** together, and you get  a **data structure** called a **hash table**.

> - **Hash tables** in **python** are **dictionaries**. `book = dict()` **or** `book = {}`.
> - **Hash tables** are used for **lookups**, **preventing duplicates entries** and for **caching data**.
> - **Hash tables** takes **O(1)** for everything **(Search, insert, delete)**.

> - **Collisions**: when **two keys** are **mapped** to the **same slot**.
> - **Collisions** are resolved by: `Linear Probing` **or** `Separate Chaining`.
>   - It doesn't mean **instant**, it means the **time taken** will be the **same**, **regardless** of how **big** the **hash table** is.
> - To **avoid collisions**, you need:
>   - **A low load factor**: **number of items in hash table** `/` **total number of slots**
>   - **A good hash function**: your **hash function** should **map keys evenly all over the hash**. 
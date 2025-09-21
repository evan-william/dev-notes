/* STACK
int x = 10;       // Allocated on the STACK
int* p = &x;      // Pointer to stack memory (no 'new' here!)
*/

/* HEAP
int* p = new int; // Allocated on the HEAP
*p = 10;          // Access heap memory through the pointer

Combine with Constructor:
Dog* dog = new Dog("Fluffy", "Shepherd", 2);

This calls the Dog constructor, creates the object on the heap, and gives you back a pointer.
You must use delete dog; later to call the destructor and clean up memory.
*/

/*
| Feature      | Stack                        | Heap                                |
| ------------ | ---------------------------- | ----------------------------------- |
| **Speed**    | Very fast (managed by CPU)   | Slower                              |
| **Size**     | Limited (\~1MB–8MB)          | Large (up to GBs)                   |
| **Lifetime** | Auto-deletes at function end | You manage manually                 |
| **Syntax**   | Simple: `int x = 5;`         | Explicit: `int* p = new int(5);`    |
| **Storage**  | Local vars, function calls   | Dynamic objects, big data           |
| **Danger**   | Stack overflow               | Memory leaks if `delete` is missing |
*/
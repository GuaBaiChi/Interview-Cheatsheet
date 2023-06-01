## Interview cheat sheet
- with terms and examples of code


## Tech Stack

## 1) Describe Object Oriented Programming, how it can be useful, and give an example of the following in the language of your choice.

 - An OOP class
Object-oriented programming is ultimately about taking a huge problem and breaking it down to solvable chunks. For each mini-problem, you write a class that does what you require. And then — best of all — you can reuse those classes, which makes it even quicker to solve the next problem

Object Oriented Programming is ultimately about modeling objects that have specific properties and methods. An object model is known as a Class. Classes allow for managing object properties and methods in a single place. Classes also allow for creating multiple object instances.

 - Encapsulation
Encapsulation is when the property of one object is another object itself.

[Encapsulation code example](https://github.com/GuaBaiChi/Interview-Cheatsheet/blob/main/Encapsulation.py)

In the above, Bar encapsulates Foo

 - Inheritance
Inheritance allows programmers to create classes that are built upon existing classes, to specify a new implementation while maintaining the same behaviors (realizing an interface), to reuse code and to independently extend original software via public classes and interfaces.

 - Abstraction / Interfaces
The short answer: An abstract class allows you to create functionality that subclasses can implement or override. An interface only allows you to define functionality, not implement it. And whereas a class can extend only one abstract class, it can take advantage of multiple interfaces.

 - Polymorphism
It refers to something having many forms, referring to both objects and methods. Polymorphism allows you to code to an interface that reduces coupling, increases reusability, and makes your code easier to read.

More specifically, Polymorphism allows for defining a routine within a base class or interface and override that routine within different inheriting classes



## 2) Describe Data Structures, their applications, and give examples of the following in a language of your choice:

 - Stack

Application of the Stack

A Stack can be used for evaluating expressions consisting of operands and operators.

[Stack code example](https://github.com/GuaBaiChi/Interview-Cheatsheet/blob/main/Stack.py)

Stacks can be used for Backtracking, i.e., to check parenthesis matching in an expression.

https://www.tutorialspoint.com/python_data_structure/python_backtracking.htm

It can also be used to convert one form of expression to another form.
It can be used for systematic Memory Management.
function call stack / stacktrace

[Stack Trace example](https://github.com/GuaBaiChi/Interview-Cheatsheet/blob/main/StackTrace.py)

 - Linked List

A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers as shown in the below image:

https://www.geeksforgeeks.org/data-structures/linked-list/

https://www.freecodecamp.org/news/introduction-to-linked-lists-in-python/

 - Tree

A tree is a type of data structure that represents a hierarchical relationship between data elements, called nodes. The top node in the tree is called the root, and the elements below the root are called child nodes. Each child node may have one or more child nodes of its own, forming a branching structure. The nodes at the bottom of the tree, which do not have any child nodes, are called leaf nodes.
A tree is a non-linear data structure, meaning that elements are not stored in a linear sequence like in an array or a linked list. Instead, elements are organized in a hierarchical structure, with each element having a parent-child relationship with other elements.

Note that the relationships between nodes of a tree are similar to that of nodes in a Linked-List

 - HashMap

Hash maps are a common data structure used to store key-value pairs for efficient retrieval. A value stored in a hash map is retrieved using the key under which it was stored. # `states` is a Hash Map with state abbreviation keys and state name values.

HashMaps are arrays, but instead of indexing into them directly as you would with an array, you HASH the key and MOD by the size of the internal array, giving you a "random" index within the internal array where a value can be stored.

In code it would look something like

[HashMap code example](https://github.com/GuaBaiChi/Interview-Cheatsheet/blob/main/HashMap.py)

## 3) Optimization: Describe time and space complexity and when they are most important. Give an example, in code, of an algorithm that has O(n^2) complexity and another example that performs the same task in O(nlogn) or less.

[Bubble Sort for O(n^2)](https://github.com/GuaBaiChi/Interview-Cheatsheet/blob/main/ComplexityBubble.py)

[Merge Sort for O(nlogn)](https://github.com/GuaBaiChi/Interview-Cheatsheet/blob/main/ComplexityMergeSort.py)

[Youtube tutorial](https://www.youtube.com/watch?v=KXAbAa1mieU) for time and space complexity 


## 4) In your own words, describe the following
- Concurrency
- Parallelism
- Distributed
- Threads
- Asynchronous

- Concurrency & Parallelism

Computer science makes the distinction between parallel and concurrent computations. Parallel computations are those that just run separate independent computations in parallel (in other words, parallelism is pure). Concurrent computations are those where there are multiple interacting threads of computation. Concurrency usually involves threads, locks, messages and deadlocks.

- Distributed 

Distributed computing is the method of making multiple computers work together to solve a common problem. It makes a computer network appear as a powerful single computer that provides large-scale resources to deal with complex challenges.

- Thread 

Threadis an independent set of values for the processor registers (for a single core).
Threads also have their own stack
Since this includes the Instruction Pointer (aka Program Counter), it controls what executes in what order. It also includes the Stack Pointer, which had better point to a unique area of memory for each thread or else they will interfere with each other.

- Asynchronous

Asynchronous programming is a type of parallel programming in which a unit of work is allowed to run separately from the primary application thread. When the work is complete, it notifies the main thread about completion or failure of the worker thread.

https://medium.com/velotio-perspectives/an-introduction-to-asynchronous-programming-in-python-af0189a88bbb




## 5) Briefly describe Linux/Unix operating systems and why software engineers may prefer them over alternatives

Linux(GNU/Linux) is a clone of Unix. open source v copyright.
kernel vs complete OS
Unix is a copyrighted name and IBM AIX, HP-UX and Sun Solaris are the only Unix operating systems remaining till date.

Pros: Bash/terminal, scalability and speed, compatible with programming languages, control, installation size, community support amongst other engineers


## 6) Solve an Easy/Medium leetcode challenge and give a write-up of how you interpreted the problem and came up with a solution.
- Where any specific data structures useful?
- Where any specific algorithms useful?

## 7) Describe collaboration tools used by Software Engineers and what they are used for

I’ve used Github, Discord, Teams, VSC, Docker, Asana, Linux

- Github

Github is an Internet hosting service for software development and version control using Git. It provides the distributed version control of Git plus access control, bug tracking, software feature requests, task management, continuous integration, and wikis for every project

It’s useful for programmers because in addition to the capabilities listed above it allows for collaboration and editing of repositories and projects.

- discord

Discord is a messaging communication platform that allows for sending files and has voice communication. It is useful for programmers because the formatting of messages in Discord allows for markdown format/syntax that allows for seeing code in messages. Though it does require payments for long messages.

- Visual Studio Code(VSC)

An Integrated Development Environment(IDE) made by Microsoft. Recently made free and has amazing integration with Github and has many many useful Extensions that help with coding format, suggestions and syntax and more.

- Asana

Meaning yoga positions and posture. This is a collaboration website that allows for assigning of tasks. This is useful for many kinds of projects but especially useful for software engineers since projects, tasks and issues can snowball quickly and record keeping what needs to be done and assigned to who is capable.

- Linux & Windows Subsystem for Linux (WSL)

Linux is an open source operating system based on a kernel and with many to choose from. WSL is a way for Windows to have Linux running within it. This is especially useful with VSC as it allows for programming to be done in Linux instead of on Windows. This has many advantages for programmers as Linux/WSL consume fewer resources and most importantly run the Bash terminal.

- Teams

Another communication platform useful for communicating with project members.

- Slack

A professional type of Discord


## 8) Discuss reasons why writing code modules is useful as opposed to writing everything in a single file. The following topics should be mentioned.
- Maintainability
- Reusability
- Complexity
- Collaboration


Writing code modules is dividing a program into smaller, self-contained units. Modules improve code organization, readability, and ease of modification. 

They allow for code reuse, reducing redundancy and promoting consistency. Modules manage complexity by isolating functionalities. They enable independent work and seamless integration, supporting collaboration among developers.


- Maintainability

Refers to the ease with which a software system or application can be maintained and updated over time

- Reusability

The ability of software components or modules to be used in multiple contexts or applications without significant modifications.

- Complexity

Can refer to the size of the codebase, the number of modules or components, the interactions between different parts, and the computational resources required to execute a program.

- Collaboration

The cooperative efforts and interaction between individuals or teams working together on a software project.

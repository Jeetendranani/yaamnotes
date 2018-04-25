"""
Architecture quality attributes
    - Modifiability
    - Testability
    - Scalability / performance
    - Security
    - Deployability

Software architecture is a description of the subsystems or components of a software system, and the relationships
between them.

"Architecture is the fundamental organization of a system embodied in its components, their relationships to each other,
and to the environment, and the principles guiding its design and evolution."

- Architecture is involved with the higher level of description structures and interactions in a system. It is connected
with those questions that entail decision making about the skeleton of the system, involving not only its functional but
also its organizational, technical, business, and quality attributes.

- Design is all about teh organization of parts or components of the system and the subsystems involved in making the
system. The problems here are typically closer to teh code or modules in question, such as:
    - What modules to split code into? How to organize them?
    - Which classes (or modules) to assign the different functionalities to?
    - which design pattern should I use for class "C"?
    - How do my objects interact at runtime? what are the messages passed, and how to organize the interaction?

Aspects of software architecture
- System: A system is a collection of components organized in specific wys to achieve a specific functionality. A
software system is a collection of such software components. A system cam often be subgrouped into subsystems.

- Structure: A structure is a set of elements that are grouped or organized together according to a guiding rule or
principle. The elements can be software or hardware systems. A software architecture can exhibit various levels of
structures depending on the observer's context.

- Environment: The context or circumstances in which a software system is built, which has a direct influence on its
architecture, business, professional, operational, and so on.

- Stakeholder: Anyone, a person or groups of persons, who has an interest or concern in the system and its success.

An architecture defines a structure.

An architecture picks a core set of elements.

-   captures early design decisions
- manages stakeholder requirements
- influence the organizational structure
- influenced by its environment
- documents the system
- often conforms to a pattern
    - client-server
    - pipes and filters

Scaling out
    - horizontal scalability
    - Vertical scalability

Performance
    performance of a computer system is the amount of work accomplished by a system using a given unit of computing
    resource. higher the work/unit ratio, higher the performance.

    - Response time
    - Latency
    - Throughput

- defining performance
- software performance engineering todo
- types of performance testing tool todo
- performance complexity and the big-O notations:
    - measuring performance
    - finding performance complexity using graphs
    - improving performance
- profiling
    - deterministic profiling
    - cprofile and profile todo
    - third-party profiles
- other tools
    - objgraph todo
    - pympler todo
- programming for performance - data structures:
    - lists
    - dictionaries
    - sets
    - tuples
- high performance containers - the collections module:
    - deque
    - defaultdict
    - ordereddict
    - counter
    - chainmap
    - namedtuple
- Probabilistic data structure - bloom filters todo

What is performance?
The degree to which the system is able to meet its throughput and / or latency requirements in terms of the number of
transactions per second or time taken for a single transaction.

Performance testing and measurement tools

- Stress testing tools:
    - load generators todo
    - http perf todo
    - apachebench todo
    - loadrunner todo
    - apache jmeter todo
    - locust todo
    - wireshark todo

- Monitoring tools: todo

- instrumentation tools todo

- code or application profiling tools todo

Measuring performance

- time command
    - real: Real time is actual wall clock time that elapsed for the operation.
    - user: user time is the amount of actual cpu time spend within the process in user mode. (outside the kernel)
    - sys: the amount of cpu time spent on executing system call within the kernel for hte program.

- contextmanager todo

- timeit module todo

- finding out time complexity - graphs todo

- measure cpu time with timeit todo

- profiling todo

- Third-part profiler
    - line profiler todo
    - memory profiler todo

- other tools
    - objgraph todo
    - pympler todo

probabilistic data structures - bloom filters todo


Scale

When teh system scales by either adding or making better use of resources inside compute node, such as cpu or ram, it is
said to scale vertically or scale up. On the other hand, when a system scales by adding more computer notes to it,
such as creating a load-balanced cluster of servers, it is said to scale horizontally or scale out.

The degree to which a software system is able to scale when computer resources are added is called its scalability.
Scalability is measured in terms of how much the system's performance characteristics, such as throughput or latency,
improve with respect to the addition of resources. For example, if a system doubles its capacity by double the number of
servers, it is scaling linearly.

Increasing the concurrency of a system often increase its scalability. increases the amount of concurrent processing
done in this store. Concurrency is the amount of work that gets down simultaneously in a system.

- Scalability and performance
- concurrency
    - concurrency and parallelism
    - concurrency in python - multi-threading
        thumbnail generator
        thumbnail generator - producer /consumer architecture
        thumbnail generator - program end condition
        thumbnail generator - resource constraint using locks
        thumbnail generator - resource constraint using semaphores
        resource constraint - semaphore vs lock
        thumbnail generator - url rate controller using conditions
        multi-threading - python and gil
    - concurrency in python - multi-processing
        a primality checker
        sorting disk files
        sorting disk files - using a counter
        sorting disk files - using multi-processing
    - multi-threading vs multi-processing
    - concurrency in python - asynchronous execution todo
        pre-emptive vs co-operative multitasking
        asyncio in python
        waiting for future - async and a wait
        concurrent futures - high level concurrent process
    - concurrency options - how to choose? todo
- parallel processing libraries
    - joblib
    - pymp
        fractals - the mandelbrot set
        fractals - scaling the mandelbrot set implementation
- Scaling for the web
    - scaling workflows - message queues and task queues todo
    - celery - a distributed task queue todo
        the mandelbrot set - using celery todo
    - serving python on the web - wsgi todo
        uwsgi - wsgi middleware on the steroids todo
        gunicorn - unicorn for wsgi todo
        gunicron vs uwsgi
- scalability architectures
    - vertical scalability architectures todo
    - horizontal scalability architectures todo

How do we measure the scalability of a system?

We find that there is a relation between Scalability, performance, concurrency and Latency.

An ideal system is one that has good concurrency and low latency; such a system ahs high performance, and would respond
better to scaling up and / or scaling out.

A system with high concurrency, but also high latency, would have variable characteristics - tis performance, and hence
scalability would be potentially very sensitive to other factors such as current system load, network congestion,
geographical distribution of compute resources and requests, and so on.

Concurrency

- multithreading

- multiprocessing

- asynchronous processing

Security

    - information security architecture
    - secure coding
    - common security vulnerabilities
    - is python secure?
        - reading input
        - evaluating arbitrary input
        - overflow errors
        - serializing objects
        - security issues with web applications
    - strategies for security - python todo
    - secure coding strategies

Information security architecture
    - confidentiality
    - integrity
    - availability
    - authentication
    - authorization
    - non-reputability

security coding
    - definition of areas of interest of the application
    - analysis of software architecture
    - review of implementation detail
    - verification of logic and syntax
    - whitebox /unit testing
    - black box testing

common security vulnerabilities
    - Overflow errors:
        - Buffer overflow
        - integer or arithmetic overflow
    - unvalidated /improperly validated input
    - improper access control
    - cryptography issues
        - http instead of https
    -insecure authentication
    - use of weak passwords
    - reuse of secure hashes /secret keys
    - weak encryption techniques
    - weak hashing techniques
    - invalid or expired certificates /keys
    - password enabled ssh
    - information leak
        - server meta information
        - open index pages
    - Open access to files /folders /databases
    - Race conditions
    - system clock drifts
    - insecure file /folder operations

Security issues with web application

    - server side template injection todo
    - denial of service todo
    - cross site scripting todo

strategies for security - python
    - reading input
    - evaluating expressions
    - serialization
    - overflow error
    - string formatting
    - files
    - handling passwords and sensitive information
    - local data
    - race conditions
    - keep your system up to date

Design pattern in python

    - Design patterns elements todo
    - categories of design patterns todo
    - pluggable hashing algorithm todo
    - summing up pluggable hashing algorithms todo
    - patterns in python - creational
        - singleton
        - borg
        - factory
        - prototype
        - builder
    - pattern in python - structural
        - adapter
        - facade
        - proxy
    - pattern in python - behavioral
        - iterator
        - observer
        - state

"""
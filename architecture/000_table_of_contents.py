"""
Table of contents

Chapter 1: Principles of Software architecture
    Defining software architecture
        Software architecture verse design
        Aspects of software architecture
    Characteristics of software architecture
        an architecture defines a structure
        an architecture picks a core set of elements
        an architecture captures early design decisions
        an architecture manages stakeholder requirements
        an architecture influences the organizational structure
        an architecture is influenced by its environment
        an architecture documents the system
        an architecture often conforms to a pattern
    Importance of software architecture
    System versus enterprise architecture
    Architecture quality attributes
        Modifiability
        Testability
        Scalability
        Performance
        Availability
        Security
        Deployability
    Summary

Chapter 2: Writing modifiable and readable code
    What is modifiability?
    Aspects related to modifiability
    Understanding readability
        python and readability
        readability - antipatterns
        techniques for readability
        document your code
        follow coding and style guiderlines
        review and refactor code
        commenting the code
    Fundamentals of modifiability - cohesion & coupling
        measuring cohesion and coupling
        measuring cohesion and coupling - string and text processing
    Exploring strategies for modifiability
        providing explicit interfaces
        reducing two-way dependencies
        abstract common services
        using inheritances technique
        using late binding technique
    metrics - tools for static analysis
        what are code smells?
        cylomatic complexity - the mccabe metric
            testing for metrics
        running static checkers
    refactoring code
        refactoring code - fixing complexity
        refactoring code - fixing code smells
        refactoring code - fixing styling and coding issues
    summary

Chapter 3: Testability - Writing testable code
    Understanding testability
        software testability and teh related attributes
        testability - architectural aspects
        testability - strategies
            reduce system complexity
            improving predictability
            control and isolate external dependencies
    White-box testing principles
        unit testing
        unit testing in action
            extending our unit test case
        nosing around with nose2
        Testing with py.test
        code coverage
            measuring coverage using coverage.py
            measuring coverage using nose2
            measuring coverage using py.test
        mocking things up
        tests inline in documentation doctests
        integration tests
        test automation
            test automation using selenium web driver
    test driven development
    TDD with palindromes
    summary

Chapter 4: Good performance is rewarding!
    What is performance?
    Software performance engineering
    Performance testing and measurement tools
    performances complexity
    measuring performance
        measuring time using a context manager
        timing code using the limeit module
            measuring the performance of our code using timeit
        finding out time complexity - grphs
        measuring cpu time with timeit
    Profiling
        deterministic profiling
        profiling with cProfile and profile
            prime number iterator class - performance tweaks
        profiling - collecting and reporting statistics
        third-party profilers
            line profiler
            memory profiler
            substring problem
    other tools
        objgraph
        pympler

    Programming for performance - data structures
        Mutable containers - lists, dictionaries, and sets
            lists
            dictionaries
            sets
        immutable containers - tuple
        high performance containers - the collections module
            deque
            defaultdict
            orderedDict
            Counter
            ChainMap
            namedtuple
        Probabilistic data structure - bloom filters
    summary

Chapter 5: writing applications that scale
    scalability and performance
    concurrency
        concurrency versus parallelism
        concurrency in python - multithreading
    thumbnail generator
        thumbnail generator - producer/ consumer architecture
        thumbnail generator - resource constraint using locks
        thumbnail generator - resource constraint using semaphores
        resource constraint - semaphore versus lock
        thumbnail generator - url rate controller using conditions
    multithreading - python and gil
        concurrency in python - multiprocessing
        a primality checker
        sorting disk files
            sorting disk files - using a counter
            sorting disk files - using multiprocessing
    multithreading versus multiprocessing
        concurrency in python - asynchronous exception
    pre-emptive versus cooperative multitasking
    the asyncio module in python
    waiting for a future - async and await
    concurrent futures - high-level concurrent processing
        disk thumbnail generator
        concurrency ooptions - how to choose?
        parallel processing libraries
        joblib
        pymp
        fractals - the mandelbrot set
            fractals - scaling the mandelbrot set implementation
    scaling for teh web
    scaling workflows - messge queues and task queeus
    celery - a distributed task queue
        the mandelbrot set using celery
        serving with python on the web - wsgi
        uwsgi - wsgi middleware on steroids
        gunicon - unicorn for wsgi
        gunicorn versus uwsgi
        scalability architectures
            vertical scalability architectures
            horizontal scalability architectures
    summary

Chapter 6: Security - Writing secure code
    information security architecture
    secure coding
    common security vulnerabilities
    is python secure?
        reading input
        evaluating arbitrary input
        overflow errors
        serializing objects
    security issues with web applications
        server side temlate injection
        server-side template injection - mitigation
        denial of service
        cross site scripting
        mitigation - dos and xss
    strategies for security - python
    secure coding strategies
    summary

Chapter 7: Design patterns in python
    Design patterns - elements
    categories of design patterns
        pluggable hashing algorithms
        summing up pluggable hashing algorithm
    patterns in python - creational
        teh singleton pattern
            the singleton - do we need a signleton?
        state sharing - borg versus singleton
        the prototype pattern
            prototyoe -deep versus shallow copy
            prototyoe using metaclasses
            combining patterns using metaclases
            the prototype factory
        the builder pattern
    patterns in python - structural
        teh adapter pattern
        the facade pattern
            facades in python
        the proxy pattern
            an instance-counting proxy
    patterns in python - behavioral
        the iterator pattern
        the observer pattern
        the state pattern
    summary

Chapter 8: Python - architectureal patterns
    introducing mvc
        moduel template view - django
        django admin - automated model-centric views
        flexible microframework - flask
    event-driven programming
        chat server and client using i/o multiplexing with the select module
        event-driven programming versus concurrent programming
        twisted
            twisted - a simple web client
            chat server using twisted
        eventlet
        greelets and gevent
    microservice architecture
        microservice framework in python
        microservice example - restaurant erservation
        microservice - advantage
    pip and filter architectures
        pipe and filter in python
    summary

Chapter 9: Deploying python applications
    deployability
        factors affecting deployability
    Tiers of software deployment architecture
    software deployment in python
        packaging python code
        pip
        virtualenv
        virtualenv and pp
        relocatable virtal environments
        pypi
        packaging and submision of an application
            the __ini__.py files
            the setup.py file
            installing the package
            submitting the package to PyPI
        pypa
        Remote deployments using fabric
        remote deployment using ansible
        managing remote daemons using superviosr
    deployment - patterns and best practices
    summary

Chapter 10: techniques for debugging
    maximum subarray problem
        the power of print
        analysis and rewrite
        timing and optimizing the code
    simple debugging tricks and techniques
        word searcher program
        word searcher program - debugging step 1
        word searcher program - debugging step 2
        word searcher program - final code
        skipping blocks of code
        stopping execution
        exteranl dependiencies - using wrappers
        replacing functions with their return value/data (mocking)
            saving to / loading dta from files as cache
            saving to / loading data from memory as cache
            returning random / mock data
    ogging as a debugging technique
        simple application logging
        advanced logging - logger objects
            advanced logging - custom formatting and loggers
            advanced logging - writing to syslog
    debugging tools - using debuggers
        a debugging session with pdb
        pdb- similar tools
        ipdb
        pdb++
    advanced debugging -tracing
        the trace module
        the iptrace program
        system call tracing suing strace
    summary



"""
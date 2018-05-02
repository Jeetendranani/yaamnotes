"""
contents

part I: foundations

    chapter 1: the problem of delivering software
        introduction
        some common release anti-patterns
            antipattern: deploying software manually
            antipattern: deploying to a production-like environment only after development is complete
            antipattern: manual configuration management of production environments
            can we do better?
        how do we archive our goal?
        what are the benefits?
            empowering teams
            reducing errors
            lowering stress
            deploying flexibility
            practice makes perfect
        the release candidate
        Principle software delivery
            keep everything in version control
            done means released
        summary

    chapter 2: configuration management
        introduction
        using version control
            use meaningful commit messages
        managing dependencies
            managing external libraries
            managing components
        managing software configuration
            configuration and flexibility
            types of configuration
            managing application configuration

        managing your environment
            tools to manage environments
            managing the change process
        summary

    chapter 3: continuous integration
        introduction
        implementing continuous integration
            what you need before you start
            a basic continuous integration system
        prerequisites for continuous integration
            check in regularly
            managing your development workspace
        using continuous integration software
            basic operation
            bells and whistles
        essential practices
            dont' check in on a broken build
            always run all commit tests locally before committing, or get your ci server to do it for you.
            wait for commit test to pass before moving on
            never go home on a broken build.
            dont commit out failing tests
            take responsibility for all breakages that results from your changes
            test-driven development
        suggested practices
            the impact on process
            centralized continuous integration
            technical issues
            alternative approaches
        Distributed version control systems
        summary

    chapter 4: implementing a testing strategy
        introduction
        types of tests
            technology-facing tests that critique the project
            test doubles
        real-life situations and strategies
            new projects
            mid project
            legacy systems
            integration testing
        process
            managing defect backlogs
        summary

part II: The deployment pipeline
    chapter 5: anatomy of the deployment pipeline
        introduction
        what is a deployment pipeline
            a basic deployment pipeline
        deployment pipeline practices
            only build your binaries once
        deploy into a copy of production

            commit state best practice
        the automated acceptance test gate
        sub
            manual testing
            nonfunctional testing
        preparing to release
            automating deployment and release
            backing out changes
            building on success
        implementing a deployment pipeline
            automating the unit test and code analysis
            automating acceptance testing
            evolving your pipeline
        metrics
        summary

    chapter 6: build and deployment scripting
        introduction
        an overview of build tools
            make
            ant
            nant and MSbulid
            maven
            rake
            buildr
            pasake
        principle and practices of build and  deployment scripting

            project layout
        deployment scripting
            deploying and testing layers
            testing your environment's configuration
        tips and tricks
            always use relative paths
            eliminate manual steps

        summary

    chapter 7: The commit stage
        introduction
        commit stage principles and practices
            provide fast, useful feedback
            what should break the commit stage
            tend the commit stage carefully
            give developers ownership
            use a build master for very large teams
        the results of the commit stage
            teh artifact repository
        commit test suite principles and practices
            avoid the user interface
            use dependency injection
            avoid the database
            avoid asynchrony in unit tests
            using test doubles
            minimizing state in tests
            faking time
            brute force
        summary

    chapter 8: automated acceptance testing
        introduction
        why is automated acceptance testing essential?
        creating acceptance tests
            the role of analysts and testers
            analysis on iterative projects

            how to express your acceptance criteira

            state in acceptance tests

            using test doubles
        The acceptance test stage
            keeping acceptance tests green
            deployment tests
        acceptance test performance
            refactor common tasks
            share expensive resources
            parallel testing
            using computer grids
        summary

    chapter 9: testing nonfunction requirements
        introduction
        managing nonfunction requirements
            analyzing nonfunctional requirements
        programming for capacity
        measuring capacity

        automation capacity testing
            capacity testing via the user interface

        additional benefits of a capacity test system
        summary

    chapter 10: deploying and releasing applications
        introduction
        creating a release strategy
            the release plan
            releasing products
        deploying and promoting your application
            the first deployment
            orchestration
            deployments to staging environments
        rolling back deployments and zero-downtime release
            blue-green deployments
            canary releasing
        emergency fixes
        continuous deployment

            the people who do the deployment should be involved in creating the deployment process
            log deployment activities
            dont' delete the old fine move them

Part III: The delivery ecosystem
    chapter 11: managing infrastructure and environments
        introduction
        understanding the needs of the operations team
            documentation and auditing
            alert for abnormal events
            it service continuity planning

        managing server provisioning and configuration
            provisioning servers
            ongoing management of servers
        managing the configuration of middleware
            managing configuration
            research the product
            examine how your middleware handles state
            look for a configuration api
            use a better technology
        managing infrastructure service
            multihomed systems
        virtualization
            managing virtual environments

            infrastructure in the cloud
            platforms in the cloud
            one size doesn't have to fit all
            criticisms of cloud computing
        monitoring infrastructure and applications
            collecting data
            logging
            creating dashboards
            behavior-driven monitoring
        summary

    chapter 12: managing data


"""
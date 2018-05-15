"""
chapter 12: designing distributed and internet systems

learning objectives

After studying this chapter, you should be able to:
12.1 distinguish between files server and client/server environments, contrasting how each is used in a lan
12.2 describe cloud computing and other current trends that help organizations address is infrastructure related
challenges
12.3 describe the standard shaping the design of internet based systems, options for ensuring internet design
consistency, site management issues influencing customer loyalty, trustworthiness, and security.

Introduction

Advances in computing technology and rapid evolution of mobile technologies are changing the way today's computing
systems are being used to meet ever more demanding business needs. existing models of managing computing resources are
quickly evolving to cloud computing and service oriented based architectures.

A variety of new opportunities and competitive pressures are driving the trend toward these technologies. corporate
restructuring - mergers, acquisitions, and consolidations - requires the integration of disparate systems. Applications
are being downsized of from expensive mainframes and dedicated data centers to both public and private cloud-based
architectures that are much more cost effective, scalable, and manageable. The explosion of electronic and mobile
commerce is today's biggest driver for developing new types of systems. how systems are designed can significantly
influence system performance, usability, and maintenance.

Designing distributed and internet systems

in this section, we briefly discuss the process and deliverables in designing distributed and internet systems. Given
the direction of organizational change and technological evolution, it is likely that most future systems development
efforts will need to consider the issue surrounding the design of distributed and internet-based system.s

The process of designing distributed and internet systems

This is the last chapter in the text that deal with system design within hte system development life cycle (see 12-1).
In the previous chapters on system design, specific techniques for representing and refining data, screens, interfaces,
and design specifications were presented. In this chapter however, no specific techniques will be presented on how to
represent the design of distributed and internet systems because no generally accepted techniques exist. alternatively,
we will focus on increasing your awareness of common environments for deploying these systems and the issues you will
confront surrounding their design and implementation. To distinguish between distributed and internet focused system
design, we will use distributed to refer to lan based file server and client / server architectures.

designing distributed and internet system is much like designing single-location systems. The primary difference is
that, because such a system will be deployed over two or more locations, many more design issues must be considered
that will influence the reliability, availability, and survivability of the system once it is implemented. Because
distributed and internet systems have more components than a single location system - that is, more processors,
networks, locations, data, and so on - there are more potential places for a failure to occur. Consequently, various
strategies can be used when designing and implementing these systems to minimize points of failure.

Thus, when designing distributed and internet systems, you will need to consider numerous trade-offs. to create
effective designs, you need to understand the characteristics of the architectures commonly used to support these
system.

Deliverable and outcomes

When designing distributed and internet systems, the deliverable is a document that will consolidate the information
that must be considered when implementing a system design. Figure 12-2 lists the types of information that should be
considered when implementing such a system. In general, the information that must be considered is the site, processing
needs, and data information for each location (or processor) in the distributed environment. Specifically, information
related to physical distances between locations, counts and usage patterns by users, building and location
infrastructure issues, personannel capabilities, data usage (create, use, update, or destroy), and local organizational
processes should be described. Additionally, the pros and cons of various implementation solutions for each location
should be reviewed. The collection of this information, in conjunction with the physical design information already
developed, will provide the bases for implementing the information system in the distributed environment. Note, however,
that our discussion assumes that any required information systems infrastructure in already in place. In other words,
we focus only on those issues in which you will likely have a choice.

    1. Description of site (for each site)
        a. geographical information
        b. physical location
        c. infrastructure information
        d. personnel charateristics ( eduction, technical skills, etc)
        e. ...

    2. description of Data Usage (for each site)
        a. data elements used
        b. data elements created
        c. data elements updated
        d. data elements deleted

    3. Description of business process (for each site)
        a. list of processes
        b. description of processes

    4. contrasts of alternative is architectures for site, data, and process needs (for each site)
        a. pros and cons of no technological support
        b. pros and cons of non-networked, local system
        c. pros and cons of various distributed configurations
        d. ...

Designing lan and client /server systems

in this section, we focus on issues related to the design of distributed systems that use lan-based file server or
client/server architectures. The section begins by providing a high-level description of both architectures. This is
followed by a brield description of advanced client / server designs using middleware to create a more robust system
deployment model.

Designing systems for lans

Personal computers and workstations can be used as stand-alone systems to support local applications. However,
organizations have discovered that if data is valuable to one employee, it is probably also valuable to other employees
in the same work group or in other groups. By interconnecting there computers, workers can exchanges information
electronically and can also share devices such as printers that may be too expensive to be utilized by only a single
user.

A local area network supports a network of personal computers, each with its own storage; each computer is able to share
common devices and software attached to the lan. each pc and workstation on a lan is typically within a few hundred feet
of another, with a total network cable length of less than 1 mile. usually, at least one computer (a microcomputer or
large) is designated as a file server. on which shared databases and applications are stored. the lan modules of a
dbms. for example, and concurrent access controls, possibly extra security features, and query or transaction queuing
management to support concurrent access from multiple users of a shard database.

Designing systems for a client /server architecture

An improvement in lan-based systems is the client /server architecture in which application processing is divided (not
necessarily evenly) between client and server. The client workstation is most often responsible for managing the user
interface, including presenting data, and the database server is responsible for database storage and access, such as
query processing, the typical client /server architecture is illustrated in Figure 12-5.

In sum, several significant benefits can be realized by adopting a client /server architecture:
1. It allows companies to leverage the benefits of microcomputer technology. Today's workstations deliver impressive
computing power at a fraction fo the cost of mainframe.
2. It allows most processing to be performed close to the source of processed data, thereby improving response times
and reducing network traffic.
3. It facilitates the use of graphical user interfaces and visual presentation techniques commonly available for workstations.
4. It allows for and encourages the acceptance of open systems.

    Several Differences between files server and client/server architectures

    Characteristic
    1. Processing
        FS: client only
        CS: both client and server
    2. Concurrent data access
        FS: low - managed by each client
        CS: high - managed by server
    3. Network Usage
        FS: Large files and data transfers
        CS: Efficient data transfers
    4. Database Security and Integrity
        FS: low -managed by each client
        CS: high - managed by server
    5. Software Maintenance
        FS: low - software changes just on server
        CS: Mixed - some new parts must be delivered to each client
    6. Hardware and system software flexibility
        FS: Client and server decoupled and can be mixed
        CS: Need for greater coordination between client and server

Advanced forms of client /server architectures Client /Server architectures represent the way different application
system functions can be distributed between client and server computers. These variations are based on the concept that
there are three general components to any information system.
1. Data management. These functions manage all interaction between software and files and databases, including data
retrieval /querying, updating, security, concurrency control, and recovery.
2. Data presentation. These functions manage just the interface between system user and the software, including the
display and printing of forms and reports and possibly validating system inputs.
3. Data analysis. These function transform input into outputs, including simple summarization to complex mathematical
modeling such as regression analysis.

Cloud computing

Managing the information systems infrastructure - the hardware, software, data, facilities, human resources, and
services used by organizations to support their decision making, business processes, and competitive strategy - can be
a challenge for many organizations, due to the evolution of hardware and software, the demand for more storage and
networking bandwidth, and the rising costs of energy. Further, organizations need dedicated staff to support their
infrastructure, which incurs further costs; often, managing the IS infrastructure is not among the organization's core
competencies, so others may be better at managing the infrastructure for them.

In many organizations, the IS infrastructure has grown over the years, leading to a fragmented infrastructure that tends
to be difficult to consolidate. However, efficiency, effectiveness, and agility are key for successfully competing in
the digital world, and organizations require a flexible, scalable, infrastructure for their applications and databases.
As a result, over the past decades, there has been a shift away from thinking about developing and maintaining the IS
infrastructure toward thinking about what services the infrastructure should deliver.

What is cloud computing?
Cloud Characteristics The could computing model has several unique and essential characteristics that distinguish cloud
computing from an in-house infrastructure and provide various benefits to users. These characteristics are discussed
next.
- On-Demand self-service
- rapid elasticity
- broad network access
- resource pooling
- measured service
- service models
    - infrastructure as a service iaas
    - platform as a service paas
    - software as a service saas

types of clouds
    - private cloud
    - public could

Managing the cloud
Some of the long-term, strategic issues that management should consider when evaluating different public cloud service
providers include availability, reliability, scalability, viarility, security, privacy, compliance, diversity of
offerings, openness, and cost.
- Availability / reliability
- Scalability
- Viability
- Security, privacy, and compliance
- Diversity of offerings
- Openness
- Costs

Service  oriented architecture

1. Reusability
2. Interoperability
3. Componentization

Web services

The most common approach for deploying a SOA is through the use of web services. A web service is a method of
communication between two electronic device over a network.

Designing internet systems

Internet design fundamentals

Standards play a major role when designing internet-based systems.
"""
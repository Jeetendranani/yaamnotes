"""
Designing a web crawler

Le'ts design a web crawler that will systematically browser and download the world wide web. Web crawlers are also
known as web spiders, robots, worms, walkers and bots.

Difficulty Level: Hard

1. What is a web crawler?

    A web crawler is a software program which browses the world wide web in a methodical and automated manner. It
    collects documents by recursively fetching links from a set fo starting pages. Many sites, particularly search
    engines, use web crawling as a means of providing up to data data. Search engines download all the pages to create
    an index on them to perform faster searches.

    some other uses of web crawlers are:

        - to test web pages and links for valid syntax and structure.
        - To monitor sites to see when their structure or contents changes.
        - to maintain mirror sites for popular web sties.
        - to search for copyright infringements.
        - To build a special purpose index, e.g., one that has some understanding of the content stored in multimedia
        files on the web.

2. Requirements and goals of the system

    Let's assume we need to crawl all the web.

    Scalability: Our service needs to be scalable such that it can crawl the entire web, and can be used fetch
    hundreds of millions of web documents.

    Extensibility: Our service should be designed in a modular way, with teh expectation that new functionality will be
    added to it. There could be newer document types that needs to be downloaded and processed in the future.

3. Some design considerations

    Crawling the web is a complex task, and there are many ways to go about it. WE should be asking a few questions
    before going any further:

    is it a crawler for html pages only? or should we fetch and store other types of media, such as sound files, images,
    videos, etc.? This is important because teh answer can change the design. If we are writing a general-purpose
    crawler to download different media types, we might want to break down the parsing module into different sets of
    modules: one for html, another for images, another for videos, where each module extracts what is considered
    interesting for that media type.

    Let's assume for now that our crawler is going to deal with html only, but it should be extensible and make it easy
    to add support for new media types.

    what protocols are we looking at? http? what about ftp links? what different protocol should our crawler handle?
    For the sake of the exercise, we will assume http. Again, it shouldn't be hard to extend the design to use FTP and
    other protocol later.

    What is the expected number of pages we will crawl? How big will the url database become? Assuming we need to crawl
    one billion websites, since a website can contain many, many urls, let's assume an upper bound of 15 billion
    different web pages that will be reached by our crawler.

    What is 'robots exclusion' and how should we deal with it? courteous web crawlers implement the robots exclusion
    protocol, which allows webmasters to declare parts of their sites off limits to crawlers. the robot exclusion
    protocol requires a web crawler to fetch a special document called robot.txt, containing these declarations from a
    web site before downloading any real content from it.

4. Capacity Estimation and constraints

    If we want to crawl 15 billion pages within four weeks, how many pages do we need to fetch per seconds?

        15B / (4 weeks * 7 days * 86400 sec) ~= 6200 pages/sec

    what about storage? Page sizes vary a lot, but as mentioned about since we will be dealing with html text only,
    let's assume an average page size be 100KB. with each page if we are storing 500 bytes of metadata, total storage
    we would need:

        15B * (100KB + 500) ~= 1.5Petabytes

    Assuming a 70% capacity model (We don't want to go above 70% of the total capacity of our storage system), Total
    storage we will need:

        1.5 Petabytes / 0.7 ~= 2.14 petabytes

5. high level design

    The basic algorithm executed by an web crawler is to take a list of seed urls as its input and repeatedly execute
    the following steps.

        1. Pick a url from the unvisited url list.
        2. Determine the ip address of its host-name
        3. establishing a connection to the host and download the corresponding document.
        4. parse the document contents to look for new urls.
        5. Add the new ruls to the list of unvisited urls.
        6. Process the downloaded document, e.g., store it or index its contents, etc.
        7. go back to step 1.

    how to crawl?

    breadth first of depth first? Breadth - first search (BFS) is usually used. However, Depth First Search (DFS) is
    also utilized in some situations, such as if your crawler has already established a connection with the website,
    it might just DFS all the urls within this website to save more handshaking overhead.

    path-ascending crawling: path-ascending crawling can help discover a lot of isolated resources or resources for
    which no inbound link would have been found in regular each url that it intends to crawl. For example, when given
     a seed url of , it will attempt to crawl /a/b,/a/, and /.

     Difficulties in implementing efficient web crawler.

     There are two important characteristics of the web tht makes web crawling a very difficult task:

     1. Large volume of web pages: A large volume of web page implies that web crawler can only download a fraction of
     the web pages at any time and hence it is critical that web crawler should be intelligent enough to prioritize
     download.

     2. Rate of change on the web pages. Another problem with today's dynamic would is that web pages on teh internet
     change very frequently, as a result, by the time the crawler is downloading the last page from a site, the page
     may change, or a new page has been added to the site.

     A bare minimum crawler needs at least these components:

     1. URL frontier: To store the list of urls to download and also prioritize which urls should be crawled first.
     2. http fetcher: To retrieve a web page from the server
     3. Extractor: To extract links from html documents.
     4. Duplicate eliminator: To make sure same content is not extracted twice unintentionally.
     5. Datastore: To store retrieve pages and url and other metadata.

6. Detailed Component design

    Let's assume our crawler is running on one server, and all the crawling is done by multiple working threads, where
    each working thread performs all the steps needed to download and process a document in a loop.

    The first step of this loop is to remove an absolute url from the shared url frontier from downloading. An absolute
    url begins with a scheme (e.g., 'http'), which identifies the network protocol that should be used to download it.
    We can implement these protocols in a modular way for extensibility, so that later if our crawler needs to support
    more protocols, it can be easily done. Based on the url's scheme, the worker calls the appropriate protocol module
    to download the document. After downloading, the document is placed into a document input stream (DIS). Putting
    documents into DIS will enable other modules to re-read the document multiple times.

    Once the document has been written to the DIS, the worker thread invokes teh dedupe test to determine whether this
    document (associated with a different url) has been seen before. if so, the document is not processed any further,
    and the worker thread removes the next url from the frontier.

    Next, our crawler needs to process the downloaded document, each document can have a different mime type like html
    page, image, video, etc. We can implement these mine schemes in a modular way so that later if our crawler needs
    to support more types, we can easily implement them. based on the downloaded document's mine type. tye worker

    mine type todo

    invokes the process method of each processing modules associated with that mine type.

    Furthermore, our thml processing module will extract all links from the page. Each link is converted into an
    absolute url and tested against a user-supplied url filter to determine if it should be downloaded. If url passes
    the filter, the worker performs the url - seen test, which checks if the url has been seen before, namely, if it is
    in the url frontier or has already been downloaded. If the url is new, it is added to the frontier.

    Let's discuss these components one by one, and see how they can be distributed onto multiple machines.

    1. The url frontier: The url frontier is the data structure that contains all the urls that remain to be downloaded.
    We can crawl by performing a breadth first traversal of the web, starting from the pages in the seed set. Such
    traversals are easily implemented by using a fifo queue.

    Since we will be having a huge list of urls to crawl, so we can distribute or url frontier into multiple servers.
    Let's assume on each server we have multiple worker threads performing the crawling tasks. Let's assume tht our
    hash function maps each url to host which will be responsible for crawling it.

    Following politeness requirements must be kept in mind while designing a distributed url frontier:

        1. Our crawler should not overload a server by downloading a lot of pages from it.
        2. We should not have multiple machine connecting a web server.

    To implement this politeness constraint, our crawler can have a collection of distinct fifo sub-queues on each host.
    Each worker thread will have its separate sub-queue, from which it removes urls for crawling. When a new url needs
    to be added, the fifo sub-queue in which it is placed will be determined by the url's canonical host name. Our hash
    function can map each hostname to a thread number. Together, these two points imply tht at teh most one worker
    thread will download documents from a given web server and also by using fifo queue it will not overload a web
    server.

    how big our url frontier would be? The size would be in the hundreds of millions of urls. Hence, we need to store
    our urls on disk. We can implement our queues in such a way that they have separate buffers for enqueuing and
    dequeuing. Enqueue buffer, once fileed will be dumped to the disk, whereas dequeue buffer will keep a cache of urls
    that need to be visited, it can periodically read form disk to fill the buffer.

    2. The fetcher module: The purpose of a fetcher module is to download teh document corresponding to a given url
    using the appropriate network protocol like http. as discussed above webmasters create robot.txt to make certain
    parts of their websites off limits for the crawler. To avoid downloading this file on every request, our crawler's
    http protocol module can maintain a fixed size cache mapping hostnames their robots exclusion rules.

    3. Document input stream: our crawler's design enables the same document to be processed by multiple processing
    modules. To avoid downloading a document multiple times, we cache the document locally using an abstraction called
    a document input stream (DIS).

    A DIS is an input stream that caches teh entire contents of the document read fro the internet. It also provides
    methods to re-read the document. The DIS can cache small document (64KB or less) entirely in memory, while large
    documents can be temporarily written to a backing file.

    Each worker thread has an associated DIS, which it reuses from document to document. After extracting a url from
    the frontier, the worker passes that url to the relevant protocol module, which initializes the DIS from network
    connection to contain the document's contents. The worker then passes the DIS to all relevant processing modules.

    4. Document Dedup test: many documents on the web are available under multiple different urls. There are also many
    cases in which documents are mirrored on various servers. Both of this effects will cause any web crawler to
    download teh same document contents multiple times. To prevent processing a document more than once, we perform a
    dedupe test on each document to remove duplication.

    To perform this test, we can calculate a 64-bit checksum of every processed document and store it in a database. For
    every new document, we can compare its checksum to all the previously calculated checksum to see the document has
    been seen before. We can use MD5 or SHA to calculate the checksums.

    how big would be the checksum store? If the whole purpose of our checksum store is to do dedup, then we just need to
    keep a unique set containing checksum of all previously processed document. Considering 15 billion distinct web
    pages, we would need:

        15B * 8 bytes => 120GB

    Although this can fit into a modern-day server's memory, if we don't have enough memory available, we can keep
    smaller LRU based cache on each server with everything in a persistent storage. The dedup test first checks if
    the chesum is present in teh cache. If not, it has to check if the checksum resides in the back storage. If the
    checksum is found, we will ignore the document. Otherwise, it will be added to the cache and back storge.

    5. url filters: The url filtering mechanism provides a customizable way to control the set of urls that are
    downloaded. This is used to blacklist websites so that our crawler can ignore them. Before adding each url to the
    frontier, the worker thread consults the user supplied url filter. We can define filters to restrict urls by domain.
    prefix, or protocol type.

    6. Domain name resolution: Before contacting a web server, a web crawler must use the domain name server (DNS) to
    map the web server's hostname into an ip address. DNS name resolution will be a big bottleneck of our crawlers given
    the amount of urls we will be working with. To avoid repeated requests, we can start caching DNS results by
    building our local DNS server.

    7. URL dedup test: While extracting links, any web crawler will encounter multiple links to the same document. To
    avoid downloading and processing a document multiple times, a url dedup test must be performed on each extracted
    liink before adding it to teh url frontier

    To perform the url dedup test, we can store all the urls seen by our crawler in canonical from in a database. To
    save space, we do not store the textual representation of each url in the url set, but rather a fixed-sized
    checksum.

    To reduce the number of operations on the database store, we can keep an in-memory cache of popular urls on each
    host shared by all threads. The reason to have this cache is that links to some urls are quite common, so caching
    the popular ones in memory will lead to a high in memory hit rate.

    how much storage we would need for url's store? If the whole purpose of our checksum is to do url dedup, then we
    just need to keep a unique set containing checksums of all previously seen urls. considering 15billion distinct

    checksum todo

    urls and 2 biytes for checksum, we would need:

        15B * 2bytes => 30GB

    can we use bloom filters for deduping? bloom filters are a probabilistic data structure for set membership testing

    bloom filters todo

    that may yield false positives. A large bit bector represents the set, an element is added to the set by computing
    'n' hash functions of the element and setting teh corresponding bits. An element is deemed to be in the set if the
    bits at all 'n' of the element's hash locations are set. Hence, a document may incorrectly be deemed to be in the
    set, but false negatives are not possible.

    The disadvantage to using a bloom filter for the url seen test is that each false positive will cased the url not
    to be added to hte frontier and therefore the document will never be downloaded. The chance of a false positive can
    be reduced by making the bit vector larger.

    8. Check pointing: A crawl of the entire web takes weeks to complete. To guard against failures, our crawler can
    write regular snapshots of its state to disk. An interrupted or aborted crawl can easily be restarted from the
    latest checkpoint.

7. Fault tolerance.

    We would use consistent hashing for distribution among crawling servers. Extended hashing will not only help in
    replacing a dead host but also help in distributing load among crawling will not only help in replacing a dead host
    but also help in distributing load among crawling servers.

    All our crawling servers will be performing regular checkpointing and storing their fifo queues to disks. If a
    server goes down, we can replace it. meanwhile, extended hashing should shift the load to other servers.

8. Data partitioning

    Our crawler will be dealing with three kinds of data:

        1. urls to visit
        2. url checksums for dedup
        3. document checksums for dedup

    Since we are distributing urls based on the hostnames, we can store these data on the same host. So, each host will
    store its set of urls that need to be visited, checksums of all the previously visited urls and checksums of all
    the downloaded documents. Since we will be using extended hashing, we can assume that urls will be redistributed
    from overloaded hosts.

    Each host will perform checkpointing periodically and dump a snapshot of all the data it is holding into a remote
    server. This will ensure that if a server dies down, another server can replace it by take its data from the
    last snapshot.  todo

9. Crawler Traps

    There are many crawler traps, spam sites, and cloaked content. A crawler trap is a url or set of urls that casuse a
    crawler to crawl indefinitely. some crawler traps are unintentional. For example, a symbolic link within a file
    system can create a cycle. Other crawler traps are introduced intentionally. For example, people have written traps
    that dynamically generate an infinite web of documents. The motivations behind such traps vary. Anti-spam traps are
    designed to catch crawlers used by spammers looking for email addresses, while other site user traps to catch search
    engine crawlers to boost their search ratings.

    AOPIC algorithm (Adaptive online page importance computation), can help mitigating common types of bot-traps. AOPIC
    solves this problem by using a credit system:

    AOPIC todo

        1. start with a set of N seed pages.
        2. Before crawling starts, allocate a fixed X amount of credit to each page.
        3. Select a page P with the highest amount of credit (or select a random page if all pages have the same amount
        of credit).
        4. Crawl page P (let's say that p had 100 credits when it was crawled).
        5. Extract all the links from page P (let's say there are 10 of them).
        6. Set teh credits of P to 0.
        7. Tae a 10% "tax" and allocate it to a Lambda page.
        8. Allocate an equal amount of credits each link found on page P from P's original credit after subtracting the
        tax, so: (100 (P credits) - 10*(10% tax) / 10 (links) = 9 credits per each link.
        9. Repeat from step 3.

    Since the Lambda page continuously collects the tax, eventually it will be the page with the largest amount of
    credit, and we'll have to 'crawl' it. By crawling the lambda page, we just take its credits and distribute them
    equally to all the pages in our database.

    Since bot traps only give internal links credits and they rarely get credit from the outside, they will continually
    leak credits (from taxation) to the lambda page. the lambda page will distribute that credits out to all teh pages
    in the database evenly, and upon each cycle, the bot trap page will lose more and more credits until it has so
    little credits that it almost never gets crawled again. This will not happen with good pages because they often get
    credits from backlinks found on the other pages.
"""
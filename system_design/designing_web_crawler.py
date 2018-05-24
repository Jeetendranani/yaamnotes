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

    1. The url frontier:
"""
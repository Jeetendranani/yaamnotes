"""
Mapreduce: todo
    - high latency
    - no dag-support
    - medium data

    - impala
    - TEZ
    - Spark

Spark
    - Mlib (machine learning) todo
    - Graph algorithm (GraphX) todo
    - Streaming (Spark Streaming) todo
    - Data Volume (Spark SQL) todo

    Storage
        - HDFS todo
        - S3 todo
        - Techyon todo

    Resource management
        - Yarn todo
        - Mesos todo
        - standlone todo

    - Spark SQL for search todo
    - Spark Streaming for real-time application todo
    - Mlib for machine learning todo
    - GraphX for graph computation todo
    - SparkR for math computation todo

    jobs
    - local
    - standalone
    - OnYarn

    1. submit a job
    2. driver initial the process
    3. driver alloc resource and start other executor
    4. executor start process
    5. manage the job, generate stages and tasks
    6. distribute task to executors, executor start a thread to execute the task logic.
    7. driver manage the tasks status
    8. task finished, stage finished, the job finished.

    DAG schedule todo
    Task schedule todo
    RDD (resilient distributed datasets) todo
"""
"""
Requirements:
Parse the input_data/log-events-viewer-result.csv file to provide summary data for:
    - Date & Timestamps of first and last entries.
    - Total CPU Utilisation per 15minutes, 30minutes, 60minutes
    - Total diskIO read / write (as separate figures) for device rdsdev
    - Average memoryUsedPC for each process in process list, in the last hour, grouped by process name

Hints:
    - This is a CSV file, with columns for timestamp and log message
    - You may use pure python (no pip installations required), or external packages if you wish
    - Try to understand one line of the log file before diving into all 300+ rows
    - If you can't satisfy every
"""
import csv
import os
import ast
import json


# if __name__ == '__main__':
#     pass

with open(os.path.join('input_data', 'log-events-viewer-result.csv'), 'r') as csv_file:
    dict_reader = csv.DictReader(csv_file)  # becomes a dictionary?

    date_list = []     # list of timestamps in the message
    timestamp_list = []
    writekb_list = []
    readkb_list = []
    os_process_list = []
    rds_process_list = []
    postgres_list = []
    pg_logger_list = []
    pg_checkpointer_list = []
    pg_backgroundwriter_list = []
    pg_walwriter_list = []
    pg_autovacuum_list = []
    pg_archiver_list = []
    pg_stats_collector_list = []
    pg_logical_replication_launcher_list = []
    pg_rdsadmin_list = []

    for row in dict_reader:
        message = row['message']
        message = ast.literal_eval(message)     # turns string into <dictionary>
        # print(json.dumps(message, indent=2))  # used to read properly
        date_list.append(message['timestamp'])
        timestamp = row['timestamp']
        timestamp_list.append(timestamp)
        disk_io = message['diskIO']
        process_list = message['processList']

        writekb = 0
        readkb = 0
        for item in disk_io:    # list
            if item['device'] == 'rdsdev':  # dictionary in list
                writekb += item['writeKb']
                readkb += item['readKb']

        writekb_list.append(writekb)
        readkb_list.append(readkb)

        os_process = 0
        rds_process = 0
        postgres = 0
        pg_logger = 0
        pg_checkpointer = 0
        pg_backgroundwriter = 0
        pg_walwriter = 0
        pg_autovacuum = 0
        pg_archiver = 0
        pg_stats_collector = 0
        pg_logical_replication_launcher = 0
        pg_rdsadmin = 0

        for item in process_list:    # list
            if item['name'] == 'OS processes':  # dictionary in list
                os_process += item['memoryUsedPc']
            elif item['name'] == 'RDS processes':
                rds_process = item['memoryUsedPc']
            elif item['name'] == 'postgres':
                postgres += item['memoryUsedPc']
            elif item['name'] == 'postgres: logger   ':
                pg_logger += item['memoryUsedPc']
            elif item['name'] == 'postgres: checkpointer   ':
                pg_checkpointer += item['memoryUsedPc']
            elif item['name'] == 'postgres: background writer   ':
                pg_backgroundwriter += item['memoryUsedPc']
            elif item['name'] == 'postgres: walwriter   ':
                pg_walwriter += item['memoryUsedPc']
            elif item['name'] == 'postgres: autovacuum launcher   ':
                pg_autovacuum += item['memoryUsedPc']
            elif item['name'] == 'postgres: archiver   last was 000000010000000C00000020':
                pg_archiver += item['memoryUsedPc']
            elif item['name'] == 'postgres: stats collector   ':
                pg_stats_collector += item['memoryUsedPc']
            elif item['name'] == 'postgres: logical replication launcher  ':
                pg_logical_replication_launcher += item['memoryUsedPc']
            elif item['name'] == 'postgres: rdsadmin rdsadmin localhost(24597) idle':
                pg_rdsadmin += item['memoryUsedPc']
            else:
                break


        os_process_list.append(os_process)
        postgres_list.append(postgres)
        pg_logger_list.append(pg_logger)
        pg_checkpointer_list.append(pg_checkpointer)
        pg_backgroundwriter_list.append(pg_backgroundwriter)
        pg_walwriter_list.append(pg_walwriter)
        pg_autovacuum_list.append(pg_autovacuum)
        pg_archiver_list.append(pg_archiver)
        pg_stats_collector_list.append(pg_stats_collector)
        pg_logical_replication_launcher_list.append(pg_logical_replication_launcher)
        pg_rdsadmin_list.append(pg_rdsadmin)

    print(f"OS Processes: {sum(os_process_list)/len(os_process_list)}")
    print(f"RDS Processes: {sum(postgres_list)/len(postgres_list)}")
    print(sum(pg_logger_list)/len(pg_logger_list))
    print(sum(pg_checkpointer_list)/len(pg_checkpointer_list))
    print(sum(pg_backgroundwriter_list)/len(pg_backgroundwriter_list))
    print(sum(pg_walwriter_list)/len(pg_walwriter_list))
    print(sum(pg_autovacuum_list)/len(pg_autovacuum_list))
    print(sum(pg_archiver_list)/len(pg_archiver_list))
    print(sum(pg_stats_collector_list)/len(pg_stats_collector_list))
    print(sum(pg_logical_replication_launcher_list)/len(pg_logical_replication_launcher_list))
    print(sum(pg_rdsadmin_list)/len(pg_rdsadmin_list))

    print(f"first entry: {date_list[0]} timestamp: {timestamp_list[0]}")
    print(f"last entry: {date_list[-1]} timestamp: {timestamp_list[-1]}\n")

    print(f"Total diskIO read for device 'rdsdev': {sum(readkb_list)}")
    print(f"Total diskIO write for device 'rdsdev': {sum(writekb_list)}")


# first idea
    # list_of_dict = list(dict_reader)
    # first_message = list_of_dict[0]['message']
    # last_message = list_of_dict[-1]['message']
    # # print(ast.literal_eval(first_message)['timestamp'])
    # # print(ast.literal_eval(last_message)['timestamp'])
    #
    # for values in list_of_dict.values():
    #     value1 = list_of_dict.get(key, 0)
    #     value2 = list_of_dict.get(key, -1)
    #     print(value1 + value2)
    #     print(values)

Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    Table_0 = Task(task_id = "Table_0", component = "Dataset", writeOptions = {"writeMode" : "overwrite"})
    Table_1 = Task(task_id = "Table_1", component = "Dataset", writeOptions = {"writeMode" : "overwrite"})
    Table_2 = Task(task_id = "Table_2", component = "Dataset", writeOptions = {"writeMode" : "overwrite"})

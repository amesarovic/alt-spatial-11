Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    Table_1 = Task(task_id = "Table_1", component = "Dataset", writeOptions = {"writeMode" : "overwrite"})
    Table_2 = Task(task_id = "Table_2", component = "Dataset", writeOptions = {"writeMode" : "overwrite"})
    spatial_match_raw_20_fact = Task(
        task_id = "spatial_match_raw_20_fact", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "spatial_match_raw_20_fact", "sourceType" : "Seed"}
    )
    scratch__Limit_1 = Task(task_id = "scratch__Limit_1", component = "Model", modelName = "scratch__Limit_1")
    spatial_match_raw_20_fact.out >> scratch__Limit_1.in_0

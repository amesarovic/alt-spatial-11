Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    SpatialMatch_Workflow__SpatialMatch_1 = Task(
        task_id = "SpatialMatch_Workflow__SpatialMatch_1", 
        component = "Model", 
        modelName = "SpatialMatch_Workflow__SpatialMatch_1"
    )
    Zones = Task(
        task_id = "Zones", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "spatial_match_2", "sourceType" : "Seed"}
    )
    Stores = Task(
        task_id = "Stores", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "spatial_match_raw_1", "sourceType" : "Seed"}
    )
    Stores.out >> SpatialMatch_Workflow__SpatialMatch_1.in_0
    Zones.out >> SpatialMatch_Workflow__SpatialMatch_1.in_1

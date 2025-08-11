Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    SpatialMatch_Workflow_02__SpatialMatch_1 = Task(
        task_id = "SpatialMatch_Workflow_02__SpatialMatch_1", 
        component = "Model", 
        modelName = "SpatialMatch_Workflow_02__SpatialMatch_1"
    )
    Zones_Fact = Task(
        task_id = "Zones_Fact", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "spatial_match_raw_20_fact", "sourceType" : "Seed"}
    )
    Stores = Task(
        task_id = "Stores", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "spatial_match_raw_1", "sourceType" : "Seed"}
    )
    Stores.out >> SpatialMatch_Workflow_02__SpatialMatch_1.in_0
    Zones_Fact.out >> SpatialMatch_Workflow_02__SpatialMatch_1.in_1

Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    spatial_match_1 = Task(
        task_id = "spatial_match_1", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "spatial_match_1", "sourceType" : "Seed"}
    )
    spatial_match_2 = Task(
        task_id = "spatial_match_2", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "spatial_match_2", "sourceType" : "Seed"}
    )
    SpatialMatch__SpatialMatch_1 = Task(
        task_id = "SpatialMatch__SpatialMatch_1", 
        component = "Model", 
        modelName = "SpatialMatch__SpatialMatch_1"
    )
    spatial_match_1.out >> SpatialMatch__SpatialMatch_1.in_0
    spatial_match_2.out >> SpatialMatch__SpatialMatch_1.in_1

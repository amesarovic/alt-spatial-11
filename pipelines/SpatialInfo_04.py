Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    SpatialInfo_04__calc_polygon_centroid = Task(
        task_id = "SpatialInfo_04__calc_polygon_centroid", 
        component = "Model", 
        modelName = "SpatialInfo_04__calc_polygon_centroid"
    )
    us_states_lines = Task(
        task_id = "us_states_lines", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "us_states_lines", "sourceType" : "Seed"}
    )
    SpatialInfo_04__SpatialInfo_04_1_1 = Task(
        task_id = "SpatialInfo_04__SpatialInfo_04_1_1", 
        component = "Model", 
        modelName = "SpatialInfo_04__SpatialInfo_04_1_1"
    )
    us_states_lines.out >> SpatialInfo_04__SpatialInfo_04_1_1.in_0

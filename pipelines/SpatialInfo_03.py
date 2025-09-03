Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    us_states_lines = Task(
        task_id = "us_states_lines", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "us_states_lines", "sourceType" : "Seed"}
    )
    SpatialInfo_03__calc_spatial_centroid = Task(
        task_id = "SpatialInfo_03__calc_spatial_centroid", 
        component = "Model", 
        modelName = "SpatialInfo_03__calc_spatial_centroid"
    )
    SpatialInfo_03__calc_spatial_centroid_1 = Task(
        task_id = "SpatialInfo_03__calc_spatial_centroid_1", 
        component = "Model", 
        modelName = "SpatialInfo_03__calc_spatial_centroid_1"
    )
    us_states_lines.out >> SpatialInfo_03__calc_spatial_centroid_1.in_0

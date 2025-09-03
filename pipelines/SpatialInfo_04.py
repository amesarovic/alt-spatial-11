Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    SpatialInfo_04__calc_line_centroid = Task(
        task_id = "SpatialInfo_04__calc_line_centroid", 
        component = "Model", 
        modelName = "SpatialInfo_04__calc_line_centroid"
    )
    SpatialInfo_04__calc_spatial_info = Task(
        task_id = "SpatialInfo_04__calc_spatial_info", 
        component = "Model", 
        modelName = "SpatialInfo_04__calc_spatial_info"
    )
    us_states_lines = Task(
        task_id = "us_states_lines", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "us_states_lines", "sourceType" : "Seed"}
    )
    us_states_lines.out >> SpatialInfo_04__calc_line_centroid.in_0

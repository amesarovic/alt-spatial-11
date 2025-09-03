Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    SpatialInfo_04__calc_us_state_centroids = Task(
        task_id = "SpatialInfo_04__calc_us_state_centroids", 
        component = "Model", 
        modelName = "SpatialInfo_04__calc_us_state_centroids"
    )
    SpatialInfo_04__calc_line_geometry_info = Task(
        task_id = "SpatialInfo_04__calc_line_geometry_info", 
        component = "Model", 
        modelName = "SpatialInfo_04__calc_line_geometry_info"
    )
    us_states_lines = Task(
        task_id = "us_states_lines", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "us_states_lines", "sourceType" : "Seed"}
    )
    SpatialInfo_04__calc_spatial_metrics = Task(
        task_id = "SpatialInfo_04__calc_spatial_metrics", 
        component = "Model", 
        modelName = "SpatialInfo_04__calc_spatial_metrics"
    )
    us_states_lines.out >> SpatialInfo_04__calc_line_geometry_info.in_0

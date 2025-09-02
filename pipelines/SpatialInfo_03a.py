Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    SpatialInfo_03a__calc_spatial_centroid = Task(
        task_id = "SpatialInfo_03a__calc_spatial_centroid", 
        component = "Model", 
        modelName = "SpatialInfo_03a__calc_spatial_centroid"
    )

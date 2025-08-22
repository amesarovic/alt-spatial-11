Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    SpatialInfo__generate_centroid = Task(
        task_id = "SpatialInfo__generate_centroid", 
        component = "Model", 
        modelName = "SpatialInfo__generate_centroid"
    )

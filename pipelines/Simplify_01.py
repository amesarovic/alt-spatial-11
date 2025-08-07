Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    Simplify_01__simplify_geospatial_data = Task(
        task_id = "Simplify_01__simplify_geospatial_data", 
        component = "Model", 
        modelName = "Simplify_01__simplify_geospatial_data"
    )

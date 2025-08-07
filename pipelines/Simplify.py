Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    Simplify__simplify_geometries = Task(
        task_id = "Simplify__simplify_geometries", 
        component = "Model", 
        modelName = "Simplify__simplify_geometries"
    )

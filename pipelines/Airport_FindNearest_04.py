Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    Airport_FindNearest_04__FilterNearestCities = Task(
        task_id = "Airport_FindNearest_04__FilterNearestCities", 
        component = "Model", 
        modelName = "Airport_FindNearest_04__FilterNearestCities"
    )

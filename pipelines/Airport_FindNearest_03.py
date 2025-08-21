Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    Airport_FindNearest_03__FindNearest = Task(
        task_id = "Airport_FindNearest_03__FindNearest", 
        component = "Model", 
        modelName = "Airport_FindNearest_03__FindNearest"
    )

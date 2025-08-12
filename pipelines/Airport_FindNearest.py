Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    airport_fn_01 = Task(
        task_id = "airport_fn_01", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "airport_fn_01", "sourceType" : "Seed"}
    )
    Airport_FindNearest__find_nearest_points = Task(
        task_id = "Airport_FindNearest__find_nearest_points", 
        component = "Model", 
        modelName = "Airport_FindNearest__find_nearest_points"
    )
    airport_fn_01.out >> Airport_FindNearest__find_nearest_points.in_0

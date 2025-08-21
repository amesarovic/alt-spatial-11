Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    Airport_FindNearest_02__FindNearest = Task(
        task_id = "Airport_FindNearest_02__FindNearest", 
        component = "Model", 
        modelName = "Airport_FindNearest_02__FindNearest"
    )
    customers = Task(
        task_id = "customers", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "customers", "sourceType" : "Seed"}
    )
    customers.out >> Airport_FindNearest_02__FindNearest.in_0

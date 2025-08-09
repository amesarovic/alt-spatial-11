Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    points_02 = Task(
        task_id = "points_02", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "points_02", "sourceType" : "Seed"}
    )
    CreatePoint_Buffer_Workflow__Buffer = Task(
        task_id = "CreatePoint_Buffer_Workflow__Buffer", 
        component = "Model", 
        modelName = "CreatePoint_Buffer_Workflow__Buffer"
    )
    points_02.out >> CreatePoint_Buffer_Workflow__Buffer.in_0

Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    points_02 = Task(
        task_id = "points_02", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "points_02", "sourceType" : "Seed"}
    )
    CreatePoint_Distance_Workflow__Distance = Task(
        task_id = "CreatePoint_Distance_Workflow__Distance", 
        component = "Model", 
        modelName = "CreatePoint_Distance_Workflow__Distance"
    )
    points_02.out >> CreatePoint_Distance_Workflow__Distance.in_0

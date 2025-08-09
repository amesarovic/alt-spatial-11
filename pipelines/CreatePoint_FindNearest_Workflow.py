Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    Center = Task(
        task_id = "Center", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "find_nearest_raw_2", "sourceType" : "Seed"}
    )
    Customer = Task(
        task_id = "Customer", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "find_nearest_raw_1", "sourceType" : "Seed"}
    )
    CreatePoint_FindNearest_Workflow__FindNearestPoints = Task(
        task_id = "CreatePoint_FindNearest_Workflow__FindNearestPoints", 
        component = "Model", 
        modelName = "CreatePoint_FindNearest_Workflow__FindNearestPoints"
    )
    Customer.out >> CreatePoint_FindNearest_Workflow__FindNearestPoints.in_0
    Center.out >> CreatePoint_FindNearest_Workflow__FindNearestPoints.in_1

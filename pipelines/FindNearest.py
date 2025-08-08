Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    find_nearest_1 = Task(
        task_id = "find_nearest_1", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "find_nearest_1", "sourceType" : "Seed"}
    )
    find_nearest_2 = Task(
        task_id = "find_nearest_2", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "find_nearest_2", "sourceType" : "Seed"}
    )
    FindNearest__find_nearest_customers = Task(
        task_id = "FindNearest__find_nearest_customers", 
        component = "Model", 
        modelName = "FindNearest__find_nearest_customers"
    )
    find_nearest_1.out >> FindNearest__find_nearest_customers.in_0
    find_nearest_2.out >> FindNearest__find_nearest_customers.in_1

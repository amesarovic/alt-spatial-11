Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    distances = Task(
        task_id = "distances", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "distances", "sourceType" : "Seed"}
    )
    Distance__calculate_distance = Task(
        task_id = "Distance__calculate_distance", 
        component = "Model", 
        modelName = "Distance__calculate_distance"
    )
    distances.out >> Distance__calculate_distance.in_0

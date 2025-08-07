Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    points = Task(
        task_id = "points", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "points", "sourceType" : "Seed"}
    )
    CreatePoint__create_geo_point = Task(
        task_id = "CreatePoint__create_geo_point", 
        component = "Model", 
        modelName = "CreatePoint__create_geo_point"
    )
    points.out >> CreatePoint__create_geo_point.in_0

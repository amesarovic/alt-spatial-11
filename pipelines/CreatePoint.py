Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    CreatePoint__create_geo_point = Task(
        task_id = "CreatePoint__create_geo_point", 
        component = "Model", 
        modelName = "CreatePoint__create_geo_point"
    )
    points_02 = Task(
        task_id = "points_02", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "points_02", "sourceType" : "Seed"}
    )
    points = Task(
        task_id = "points", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "points", "sourceType" : "Seed"}
    )
    CreatePoint__create_geo_points = Task(
        task_id = "CreatePoint__create_geo_points", 
        component = "Model", 
        modelName = "CreatePoint__create_geo_points"
    )
    points_02.out >> CreatePoint__create_geo_points.in_0
    points.out >> CreatePoint__create_geo_point.in_0

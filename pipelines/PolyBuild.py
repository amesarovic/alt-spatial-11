Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    poly_build = Task(
        task_id = "poly_build", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "poly_build", "sourceType" : "Seed"}
    )
    PolyBuild__Line = Task(task_id = "PolyBuild__Line", component = "Model", modelName = "PolyBuild__Line")
    PolyBuild__Polygon = Task(task_id = "PolyBuild__Polygon", component = "Model", modelName = "PolyBuild__Polygon")
    poly_build.out >> [PolyBuild__Polygon.in_0, PolyBuild__Line.in_0]

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
    PolyBuild__PolyBuild_1_1 = Task(
        task_id = "PolyBuild__PolyBuild_1_1", 
        component = "Model", 
        modelName = "PolyBuild__PolyBuild_1_1"
    )
    PolyBuild__Polygon = Task(task_id = "PolyBuild__Polygon", component = "Model", modelName = "PolyBuild__Polygon")
    PolyBuild__build_route_polygon = Task(
        task_id = "PolyBuild__build_route_polygon", 
        component = "Model", 
        modelName = "PolyBuild__build_route_polygon"
    )
    poly_build.out >> [PolyBuild__Polygon.in_0, PolyBuild__Line.in_0]

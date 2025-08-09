Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    PolyBuild_Simplify_Workflow__Polygon_Simplify = Task(
        task_id = "PolyBuild_Simplify_Workflow__Polygon_Simplify", 
        component = "Model", 
        modelName = "PolyBuild_Simplify_Workflow__Polygon_Simplify"
    )
    PolyBuild_Simplify_Workflow__LineString_Simplify = Task(
        task_id = "PolyBuild_Simplify_Workflow__LineString_Simplify", 
        component = "Model", 
        modelName = "PolyBuild_Simplify_Workflow__LineString_Simplify"
    )
    poly_build = Task(
        task_id = "poly_build", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "poly_build", "sourceType" : "Seed"}
    )
    (
        poly_build.out
        >> [PolyBuild_Simplify_Workflow__LineString_Simplify.in_0, PolyBuild_Simplify_Workflow__Polygon_Simplify.in_0]
    )

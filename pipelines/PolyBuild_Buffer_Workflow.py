Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    PolyBuild_Buffer_Workflow__Buffer_Polygon = Task(
        task_id = "PolyBuild_Buffer_Workflow__Buffer_Polygon", 
        component = "Model", 
        modelName = "PolyBuild_Buffer_Workflow__Buffer_Polygon"
    )
    PolyBuild_Buffer_Workflow__Buffer_Line = Task(
        task_id = "PolyBuild_Buffer_Workflow__Buffer_Line", 
        component = "Model", 
        modelName = "PolyBuild_Buffer_Workflow__Buffer_Line"
    )
    poly_build = Task(
        task_id = "poly_build", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "poly_build", "sourceType" : "Seed"}
    )
    poly_build.out >> [PolyBuild_Buffer_Workflow__Buffer_Line.in_0, PolyBuild_Buffer_Workflow__Buffer_Polygon.in_0]

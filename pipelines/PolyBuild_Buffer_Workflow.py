Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    poly_build = Task(
        task_id = "poly_build", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "poly_build", "sourceType" : "Seed"}
    )
    PolyBuild_Buffer_Workflow__buffer_geometry = Task(
        task_id = "PolyBuild_Buffer_Workflow__buffer_geometry", 
        component = "Model", 
        modelName = "PolyBuild_Buffer_Workflow__buffer_geometry"
    )
    poly_build.out >> PolyBuild_Buffer_Workflow__buffer_geometry.in_0

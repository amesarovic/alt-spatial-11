Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    Buffer__buffer_new_england = Task(
        task_id = "Buffer__buffer_new_england", 
        component = "Model", 
        modelName = "Buffer__buffer_new_england"
    )
    us_states_lines = Task(
        task_id = "us_states_lines", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "us_states_lines", "sourceType" : "Seed", "alias" : ""}
    )
    Buffer__buffer_us_states = Task(
        task_id = "Buffer__buffer_us_states", 
        component = "Model", 
        modelName = "Buffer__buffer_us_states"
    )
    us_states_lines.out >> Buffer__buffer_us_states.in_0

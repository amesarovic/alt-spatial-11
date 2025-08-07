Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    Buffer__buffer_new_england = Task(
        task_id = "Buffer__buffer_new_england", 
        component = "Model", 
        modelName = "Buffer__buffer_new_england"
    )

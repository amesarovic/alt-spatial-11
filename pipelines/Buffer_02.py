Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    Buffer_02__buffer_new_england = Task(
        task_id = "Buffer_02__buffer_new_england", 
        component = "Model", 
        modelName = "Buffer_02__buffer_new_england"
    )

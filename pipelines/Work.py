Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    new_england = Task(
        task_id = "new_england", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {
          "name": "new_england", 
          "sourceType": "Table", 
          "sourceName": "andre_dev.alteryx_spatial", 
          "alias": "", 
          "additionalProperties": None
        }
    )
    Work__JSONParse_1 = Task(task_id = "Work__JSONParse_1", component = "Model", modelName = "Work__JSONParse_1")
    Work__Deduplicate_0 = Task(task_id = "Work__Deduplicate_0", component = "Model", modelName = "Work__Deduplicate_0")
    Script_1 = Task(
        task_id = "Script_1", 
        component = "Script", 
        ports = None, 
        scriptMethodHeader = "def Script(spark: SparkSession, in0: DataFrame) -> DataFrame:", 
        scriptMethodFooter = "return out0", 
        script = ""
    )
    new_england.out >> Script_1.in0

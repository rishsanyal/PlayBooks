import { SOURCES } from "../../../constants/index.ts";
import { PlaybookTask } from "../../../types.ts";
import * as Injector from "../../injectors/index.ts";
import { v4 as uuidv4 } from "uuid";

export const handleStepSourceInjector = (step): PlaybookTask[] => {
  let baseTask: PlaybookTask = {
    name: step.name ?? uuidv4(),
    id: step.id ?? "0",
    type: "METRIC",
    description: step.description ?? "",
    interpreter_type: step.interpreter?.type,
  };

  let tasks: PlaybookTask[] = [];

  console.log(step.source);

  switch (step.source) {
    case SOURCES.CLOUDWATCH:
      tasks = Injector.injectCloudwatchTasks(step, baseTask);
      break;
    case SOURCES.GRAFANA_VPC:
    case SOURCES.GRAFANA:
      tasks = Injector.injectGrafanaTasks(step, baseTask);
      break;
    case SOURCES.GRAFANA_MIMIR:
      tasks = Injector.injectMimirTasks(step, baseTask);
      break;
    case SOURCES.CLICKHOUSE:
      tasks = Injector.injectClickhouseTasks(step, baseTask);
      break;
    case SOURCES.POSTGRES:
      tasks = Injector.injectPostgresTasks(step, baseTask);
      break;
    case SOURCES.EKS:
      tasks = Injector.injectEksTasks(step, baseTask);
      break;
    case SOURCES.NEW_RELIC:
      tasks = Injector.injectNewRelicTasks(step, baseTask);
      break;
    case SOURCES.DATADOG:
      tasks = Injector.injectDatadogTasks(step, baseTask);
      break;
    case SOURCES.API:
      tasks = Injector.injectApiTasks(step, baseTask);
      break;

    case SOURCES.TEXT:
      tasks = Injector.injectTextTasks(step, baseTask);
      break;
    default:
      break;
  }

  return tasks;
};

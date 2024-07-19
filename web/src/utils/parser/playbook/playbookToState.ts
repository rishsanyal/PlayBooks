import { playbookSelector } from "../../../store/features/playbook/playbookSlice.ts";
import { store } from "../../../store/index.ts";
import { Playbook, Step, Task } from "../../../types/index.ts";
import { v4 as uuidv4 } from "uuid";

function playbookToState(playbook: Playbook): Playbook {
  const { supportedTaskTypes } = playbookSelector(store.getState());
  const tasks: Task[] = [];
  const steps = playbook?.steps?.map((e: Step, i: number) => ({
    ...e,
    ui_requirement: {
      stepIndex: i === 0 ? 0 : undefined,
      isOpen: false,
      showError: false,
    },
  }));
  steps.forEach((step: Step) => {
    const stepTasks: Task[] = (step.tasks as Task[]).map((e) => {
      const supportedType = supportedTaskTypes?.find(
        (t: any) =>
          t.source === e.source &&
          t.task_type === e[e.source.toLowerCase()]?.type,
      );
      return {
        ...e,
        reference_id: uuidv4(),
        ui_requirement: {
          stepId: step.id,
          resultType: supportedType?.result_type,
          isOpen: false,
          model_type: supportedType.supported_model_types?.[0]?.model_type,
        },
      };
    });
    step.reference_id = uuidv4();
    tasks.push(...stepTasks);
  });
  playbook?.step_relations?.forEach((relation) => {
    const sourceId =
      typeof relation.parent !== "string" ? (relation.parent as Step).id : "";
    const targetId = (relation.child as Step).id;
    relation.ui_requirement = {
      playbookRelationId: relation.id,
    };
    relation.id = `edge-${sourceId}-${targetId}`;
    const rules = relation.condition?.rules ?? [];
    if (relation.condition) {
      relation.condition.rules = rules.map((rule) => ({
        ...rule,
        task: tasks.find((e) => e.id === rule.task.id) ?? rule.task,
        [rule.type.toLowerCase()]: {
          ...rule?.[rule?.type?.toLowerCase()],
          isNumeric:
            rule?.[rule?.type?.toLowerCase()]?.numeric_value_threshold !==
              undefined ?? false,
        },
      }));
    }
    relation.parent = steps?.find((e) => e.id === sourceId) ?? relation.parent;
    relation.child = steps?.find((e) => e.id === targetId) ?? relation.child;
  });
  return {
    ...playbook,
    steps,
    ui_requirement: {
      tasks,
      isExisting: true,
    },
  };
}

export default playbookToState;

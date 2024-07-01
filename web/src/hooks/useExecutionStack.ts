import { useDispatch, useSelector } from "react-redux";
import {
  playbookSelector,
  popFromExecutionStack,
} from "../store/features/playbook/playbookSlice.ts";
import { useGetPlaybookExecutionQuery } from "../store/features/playbook/api/index.ts";
import { executionToPlaybook } from "../utils/parser/playbook/executionToPlaybook.ts";
import { Step } from "../types.ts";
import { useEffect } from "react";

function useExecutionStack() {
  const {
    executionStack,
    executionId,
    steps: playbookSteps,
  } = useSelector(playbookSelector);
  const dispatch = useDispatch();
  const { data, refetch } = useGetPlaybookExecutionQuery();
  const steps = executionToPlaybook(data?.playbook_execution);
  const executingStep = (playbookSteps ?? []).find(
    (step: Step) => step.outputLoading,
  );
  const nextStep =
    executionStack?.length > 0
      ? playbookSteps.find(
          (e: Step) => e.id === executionStack[executionStack.length - 1],
        )
      : {};

  useEffect(() => {
    if (!executingStep?.outputLoading && executionId) {
      refetch();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [executingStep?.outputLoading]);

  const pop = () => {
    dispatch(popFromExecutionStack());
  };

  return {
    executionStack,
    steps,
    nextStep,
    executingStep,
    pop,
  };
}

export default useExecutionStack;

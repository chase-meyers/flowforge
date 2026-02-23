export interface Timestamps {
  createdAt: string;
  updatedAt: string;
}

export interface WorkflowEdge {
  from: string;
  to: string;
}

export interface WorkflowStep {
  id: string;
  type: string;
}

export interface TriggerDefinition {
  type: string;
  config?: Record<string, unknown>;
}

interface BaseFlowEntity {
  id: string;
  name: string;
  userId: string;
  trigger: TriggerDefinition;
  steps: WorkflowStep[];
  edges: WorkflowEdge[];
  timestamps: Timestamps;
}

export interface Workflow extends BaseFlowEntity {}

export interface Trigger extends BaseFlowEntity {}

export interface Action extends BaseFlowEntity {}

export interface WorkflowRun extends BaseFlowEntity {}

export interface StepRun extends BaseFlowEntity {}

import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import { apiGet, apiPost } from "../lib/api";

function WorkflowDetail() {
  const { id } = useParams();
  const [workflow, setWorkflow] = useState(null);
  const [runMessage, setRunMessage] = useState("");

  useEffect(() => {
    async function fetchWorkflow() {
      const data = await apiGet(`/workflows/${id}`);
      setWorkflow(data);
    }

    fetchWorkflow();
  }, [id]);

  async function handleRunWorkflow() {
    await apiPost(`/workflows/${id}/run`);
    setRunMessage("Workflow run created successfully.");
  }

  if (!workflow) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>{workflow.name}</h1>
      <button type="button" onClick={handleRunWorkflow}>
        Run Workflow
      </button>
      {runMessage && <div>{runMessage}</div>}
      <div>
        <h2>Trigger</h2>
        <pre>{JSON.stringify(workflow.trigger, null, 2)}</pre>
      </div>
      <div>
        <h2>Steps</h2>
        <pre>{JSON.stringify(workflow.steps, null, 2)}</pre>
      </div>
      <div>
        <h2>Edges</h2>
        <pre>{JSON.stringify(workflow.edges, null, 2)}</pre>
      </div>
    </div>
  );
}

export default WorkflowDetail;

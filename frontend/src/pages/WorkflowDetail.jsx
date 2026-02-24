import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import { apiGet } from "../lib/api";

function WorkflowDetail() {
  const { id } = useParams();
  const [workflow, setWorkflow] = useState(null);

  useEffect(() => {
    async function fetchWorkflow() {
      const data = await apiGet(`/workflows/${id}`);
      setWorkflow(data);
    }

    fetchWorkflow();
  }, [id]);

  if (!workflow) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>{workflow.name}</h1>
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

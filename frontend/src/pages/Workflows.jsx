import { useEffect, useState } from "react";

import { apiGet } from "../lib/api";

function Workflows() {
  const [workflows, setWorkflows] = useState([]);

  useEffect(() => {
    async function fetchWorkflows() {
      const data = await apiGet("/workflows");
      setWorkflows(Array.isArray(data) ? data : []);
    }

    fetchWorkflows();
  }, []);

  if (workflows.length === 0) {
    return <div>No workflows yet</div>;
  }

  return (
    <ul>
      {workflows.map((workflow) => (
        <li key={workflow.id}>{workflow.name}</li>
      ))}
    </ul>
  );
}

export default Workflows;
